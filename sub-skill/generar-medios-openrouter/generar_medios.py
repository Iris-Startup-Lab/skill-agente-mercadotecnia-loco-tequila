#!/usr/bin/env python3
"""
OpenRouter Media Generator (Images & Ultra-Short Videos <= 10s)
Sub-skill de `agente-mercadotecnia-loco-tequila`.

Ejecuta los prompts que la skill ya escribió (los que viven en la Pasarela Web
generada en el paso 11) contra los modelos de imagen/video de OpenRouter.

Acciones:
  --action list-models      Catálogo en vivo de modelos (image | video) con precios
  --action extract-prompts  Lee el bloque CAMPAIGN de un HTML de campaña y lista los conceptos
  --action generate         Genera imagen(es) o video(s) — desde la pasarela o desde --prompt

NUNCA escribe la API key en disco ni la imprime en la salida.
"""

import os
import sys
import json
import time
import argparse
import base64
import re
from pathlib import Path
from typing import Optional, Dict, Any, List

try:
    import requests
except ImportError:
    print(json.dumps({
        "status": "error",
        "message": "Falta la librería 'requests'. Instálala con: pip install requests"
    }, ensure_ascii=False))
    sys.exit(1)

# Configuración de URLs base de OpenRouter
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
CHAT_COMPLETIONS_URL = f"{OPENROUTER_BASE_URL}/chat/completions"
IMAGES_GENERATIONS_URL = f"{OPENROUTER_BASE_URL}/images/generations"
MODELS_URL = f"{OPENROUTER_BASE_URL}/models"
VIDEOS_URL = f"{OPENROUTER_BASE_URL}/videos"
# Catálogo de video: `/models` NO lista modelos de video (solo text/image/audio).
# El catálogo real, con duraciones y aspectos soportados por modelo, vive aquí.
VIDEO_MODELS_URL = f"{OPENROUTER_BASE_URL}/videos/models"

# Tope de seguridad de COSTO, no límite de la API: varios modelos aceptan 15 s
# (Kling, Seedance) o 20 s (Sora 2 Pro), y el precio es por segundo. Se puede
# subir con --max-duration cuando el usuario lo autorice explícitamente.
MAX_VIDEO_DURATION_SECONDS = 10

# Catálogo fallback en caso de error de red en consulta en vivo
FALLBACK_IMAGE_MODELS = [
    {
        "id": "google/gemini-3.1-flash-image",
        "name": "Google: Nano Banana 2 (Gemini 3.1 Flash Image)",
        "description": "Último estado del arte de Google en generación de imágenes.",
        "recommended": True
    },
    {
        "id": "google/gemini-3-pro-image",
        "name": "Google: Nano Banana Pro (Gemini 3 Pro Image)",
        "description": "Máxima resolución y comprensión visual avanzada basada en Gemini 3 Pro.",
        "recommended": True
    },
    {
        "id": "openai/gpt-5.4-image-2",
        "name": "OpenAI: GPT-5.4 Image 2",
        "description": "Excelente coherencia estilística, tipografía e iluminación fotorrealista.",
        "recommended": True
    },
    {
        "id": "openai/gpt-5-image",
        "name": "OpenAI: GPT-5 Image",
        "description": "Capacidades avanzadas de generación visual con GPT-5.",
        "recommended": False
    },
    {
        "id": "openai/gpt-5-image-mini",
        "name": "OpenAI: GPT-5 Image Mini",
        "description": "Generación ultrarrápida y económica para prototipado.",
        "recommended": False
    },
    {
        "id": "google/gemini-3.1-flash-lite-image",
        "name": "Google: Nano Banana 2 Lite",
        "description": "Opción de latencia ultrabaja.",
        "recommended": False
    },
    {
        "id": "openrouter/auto",
        "name": "Auto Router (Image)",
        "description": "Enrutamiento automático al mejor modelo visual disponible.",
        "recommended": False
    }
]

# Respaldo de video verificado contra `/api/v1/videos/models`. Los ids del
# respaldo anterior (minimax/video-01, runway/gen-3a-turbo, luma/ray-2,
# kling/kling-v1.5, openrouter/auto) NO existen en el catálogo: usarlos era
# garantía de 400. `openrouter/auto` tampoco aplica a video.
FALLBACK_VIDEO_MODELS = [
    {
        "id": "google/veo-3.1",
        "name": "Google: Veo 3.1",
        "description": "Calidad cinematográfica con audio nativo. Duraciones 4/6/8 s, 16:9 y 9:16, hasta 4K.",
        "supported_durations": [4, 6, 8],
        "supported_aspect_ratios": ["16:9", "9:16"],
        "recommended": True
    },
    {
        "id": "google/veo-3.1-fast",
        "name": "Google: Veo 3.1 Fast",
        "description": "Veo 3.1 con menor latencia y costo por segundo.",
        "recommended": True
    },
    {
        "id": "bytedance/seedance-2.0",
        "name": "ByteDance: Seedance 2.0",
        "description": "El más flexible en formato: 7 relaciones de aspecto (incluye 3:4 y 21:9), 4–15 s, hasta 4K.",
        "supported_durations": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "supported_aspect_ratios": ["1:1", "3:4", "9:16", "4:3", "16:9", "21:9", "9:21"],
        "recommended": True
    },
    {
        "id": "kwaivgi/kling-v3.0-pro",
        "name": "Kling: Video v3.0 Pro",
        "description": "Muy económico por segundo (720p). Acepta negative_prompt nativo. 3–15 s.",
        "supported_durations": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "supported_aspect_ratios": ["16:9", "9:16", "1:1"],
        "recommended": True
    },
    {
        "id": "openai/sora-2-pro",
        "name": "OpenAI: Sora 2 Pro",
        "description": "Máxima coherencia narrativa. Solo 16:9 y 9:16; duraciones 4/8/12/16/20 s. El más caro por segundo.",
        "supported_durations": [4, 8, 12, 16, 20],
        "supported_aspect_ratios": ["16:9", "9:16"],
        "recommended": False
    },
    {
        "id": "minimax/hailuo-3",
        "name": "MiniMax: H3",
        "description": "Física de fluidos y movimiento de cámara naturales.",
        "recommended": False
    }
]


# ---------------------------------------------------------------------------
# Utilidades de archivos
# ---------------------------------------------------------------------------

def default_key_file() -> Path:
    """Ruta por defecto del archivo de clave, FUERA del repositorio."""
    return Path.home() / ".openrouter" / "api_key.txt"


def resolve_api_key(
    cli_key: Optional[str] = None,
    key_file: Optional[str] = None,
) -> Any:
    """
    Resuelve la API Key para interactuar con OpenRouter.

    Orden de prioridad:
      1. `--api-key` (explícito)
      2. Variable de entorno `OPENROUTER_API_KEY`
      3. Archivo de clave (por defecto `~/.openrouter/api_key.txt`)

    Devuelve `(clave, origen)`. **Nunca** devuelve ni imprime la clave completa
    en reportes (se enmascara para seguridad).
    """
    if cli_key and cli_key.strip():
        return cli_key.strip(), "parametro --api-key"

    env_key = os.getenv("OPENROUTER_API_KEY")
    if env_key and env_key.strip():
        return env_key.strip(), "variable de entorno OPENROUTER_API_KEY"

    ruta = Path(key_file) if key_file else default_key_file()
    try:
        if ruta.is_file():
            contenido = ruta.read_text(encoding="utf-8-sig", errors="replace").strip()
            # Tolera que el usuario haya pegado `OPENROUTER_API_KEY=sk-or-...`
            # o haya dejado líneas vacías / comentarios.
            for linea in contenido.splitlines():
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                if "=" in linea and linea.split("=", 1)[0].strip().isupper():
                    linea = linea.split("=", 1)[1].strip()
                linea = linea.strip("'\"")
                if linea:
                    return linea, f"archivo {ruta}"
    except OSError:
        pass

    return None, None


def enmascarar(clave: Optional[str]) -> str:
    """Representación segura para reportes: nunca revela la clave."""
    if not clave:
        return "[sin clave]"
    return f"{clave[:7]}...{clave[-4:]} ({len(clave)} caracteres)" if len(clave) > 14 else "[clave corta]"


def check_key(cli_key: Optional[str], key_file: Optional[str], validar: bool = True) -> Dict[str, Any]:
    """
    Informa si hay una clave disponible y de dónde sale, SIN imprimirla.
    Con `validar`, confirma contra `GET /api/v1/key` que sirve y cuánto saldo queda.
    """
    clave, origen = resolve_api_key(cli_key, key_file)
    ruta = Path(key_file) if key_file else default_key_file()

    if not clave:
        return {
            "status": "error",
            "code": "MISSING_API_KEY",
            "clave_disponible": False,
            "archivo_esperado": str(ruta).replace("\\", "/"),
            "archivo_existe": ruta.is_file(),
            "message": (
                "No hay API Key disponible. El usuario puede proporcionarla en el chat "
                "(para que el agente la configure de inmediato) o guardarla en el "
                f"archivo {ruta} (con el Bloc de notas)."
            ),
        }

    salida = {
        "status": "success",
        "clave_disponible": True,
        "origen": origen,
        "clave_enmascarada": enmascarar(clave),
    }

    if not validar:
        return salida

    try:
        r = requests.get(f"{OPENROUTER_BASE_URL}/key", headers=_headers(clave), timeout=20)
        if r.status_code == 401:
            salida.update({
                "status": "error", "code": "INVALID_KEY",
                "message": "OpenRouter rechazó la clave (401). Puede estar revocada o mal copiada.",
            })
            return salida
        r.raise_for_status()
        d = (r.json() or {}).get("data") or {}
        salida["verificada"] = True
        salida["etiqueta"] = d.get("label")
        salida["saldo_restante_usd"] = d.get("limit_remaining")
        salida["consumo_total_usd"] = d.get("usage")
        salida["es_nivel_gratuito"] = d.get("is_free_tier")
        if d.get("limit_remaining") == 0:
            salida["aviso_saldo"] = (
                "La clave funciona pero el saldo está en 0: las llamadas fallarán "
                "con 402. Hay que cargar créditos en Settings → Credits."
            )
    except requests.exceptions.RequestException as e:
        salida["verificada"] = False
        salida["aviso_verificacion"] = (
            f"No se pudo verificar la clave contra OpenRouter ({e}). Se intentará "
            "generar de todos modos."
        )
    return salida


def ensure_output_dirs(base_dir: Path) -> Dict[str, Path]:
    img_dir = base_dir / "outputs" / "images"
    vid_dir = base_dir / "outputs" / "videos"
    img_dir.mkdir(parents=True, exist_ok=True)
    vid_dir.mkdir(parents=True, exist_ok=True)
    return {"images": img_dir, "videos": vid_dir}


def save_b64_file(b64_data: str, out_path: Path) -> Path:
    if "," in b64_data:
        b64_data = b64_data.split(",", 1)[1]
    data_bytes = base64.b64decode(b64_data)
    with open(out_path, "wb") as f:
        f.write(data_bytes)
    return out_path


def download_file(url: str, out_path: Path) -> Path:
    response = requests.get(url, stream=True, timeout=90)
    response.raise_for_status()
    with open(out_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return out_path


def slugify(text: str, max_len: int = 40) -> str:
    text = (text or "").lower()
    text = re.sub(r"[áàä]", "a", text)
    text = re.sub(r"[éèë]", "e", text)
    text = re.sub(r"[íìï]", "i", text)
    text = re.sub(r"[óòö]", "o", text)
    text = re.sub(r"[úùü]", "u", text)
    text = re.sub(r"ñ", "n", text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:max_len] or "concepto"


# ---------------------------------------------------------------------------
# Lectura de prompts desde la Pasarela Web generada (paso 11)
# ---------------------------------------------------------------------------

CAMPAIGN_START = "// ===== CAMPAIGN:START"
CAMPAIGN_END = "// ===== CAMPAIGN:END"

# Flags de sintaxis Midjourney que NO deben viajar dentro del texto del prompt
# hacia modelos de OpenRouter (Gemini, GPT-Image, etc.): ahí son ruido literal
# que el modelo puede llegar a renderizar como texto dentro de la imagen.
#
# Se corta desde el PRIMER flag hasta el final de la cadena, porque
# `references/prompt-standards.md` §1 los define como parámetros terminales
# (`--ar` es el campo 6 y el negative prompt va después). Cortar por tramos
# dejaba fragmentos sueltos cuando un negativo contenía guiones
# ("low-resolution" → "-resolution").
MJ_FLAG_RE = re.compile(
    r"\s*--(?:ar|no|stylize|s|chaos|c|v|q|quality|style|seed|weird|iw|niji)\b[\s\S]*$",
    re.IGNORECASE,
)
AR_RE = re.compile(r"(\d{1,2})\s*:\s*(\d{1,2})")


def _js_unescape(raw: str) -> str:
    """Convierte los escapes de un literal de cadena JS a texto plano."""
    out = []
    i = 0
    n = len(raw)
    simple = {"n": "\n", "t": "\t", "r": "\r", "b": "\b", "f": "\f",
              "\\": "\\", '"': '"', "'": "'", "/": "/", "`": "`", "\n": ""}
    while i < n:
        c = raw[i]
        if c == "\\" and i + 1 < n:
            nxt = raw[i + 1]
            if nxt == "u" and i + 5 < n:
                try:
                    out.append(chr(int(raw[i + 2:i + 6], 16)))
                    i += 6
                    continue
                except ValueError:
                    pass
            if nxt in simple:
                out.append(simple[nxt])
                i += 2
                continue
            out.append(nxt)
            i += 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def js_object_to_json(src: str) -> str:
    """
    Convierte un literal de objeto JavaScript (claves sin comillas, comentarios,
    comas finales, comillas simples y template literals) a JSON válido.

    El escaneo respeta las cadenas: se extraen primero a un marcador opaco para
    que ni los comentarios ni el requoteo de claves toquen su contenido.
    """
    strings: List[str] = []
    out: List[str] = []
    i = 0
    n = len(src)
    while i < n:
        c = src[i]
        if c in ('"', "'", "`"):
            quote = c
            j = i + 1
            buf: List[str] = []
            while j < n:
                if src[j] == "\\":
                    buf.append(src[j:j + 2])
                    j += 2
                    continue
                if src[j] == quote:
                    break
                buf.append(src[j])
                j += 1
            strings.append(_js_unescape("".join(buf)))
            out.append("\x00%d\x00" % (len(strings) - 1))
            i = j + 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            while i < n and src[i] != "\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            i += 2
            while i + 1 < n and not (src[i] == "*" and src[i + 1] == "/"):
                i += 1
            i += 2
            continue
        out.append(c)
        i += 1

    text = "".join(out)
    text = re.sub(r"([{,]\s*)([A-Za-z_$][A-Za-z0-9_$]*)(\s*:)", r'\1"\2"\3', text)
    text = re.sub(r",(\s*[}\]])", r"\1", text)

    def _restore(match: "re.Match") -> str:
        return json.dumps(strings[int(match.group(1))], ensure_ascii=False)

    return re.sub(r"\x00(\d+)\x00", _restore, text)


def load_campaign(path: Path) -> Dict[str, Any]:
    """
    Extrae el dataset CAMPAIGN de un HTML de campaña (o lee un .json directo).
    Devuelve el objeto con `title`, `items`, etc.
    """
    raw = path.read_text(encoding="utf-8", errors="replace")

    if path.suffix.lower() == ".json":
        return json.loads(raw)

    start = raw.find(CAMPAIGN_START)
    end = raw.find(CAMPAIGN_END)
    if start == -1 or end == -1:
        raise ValueError(
            "No se encontraron los marcadores CAMPAIGN:START / CAMPAIGN:END en "
            f"{path.name}. ¿Se generó con references/showcase-template.html?"
        )

    block = raw[start:end]
    brace = block.find("{")
    if brace == -1:
        raise ValueError("El bloque CAMPAIGN no contiene un objeto.")

    # Recorte balanceado del objeto, respetando cadenas.
    depth = 0
    in_str: Optional[str] = None
    for idx in range(brace, len(block)):
        ch = block[idx]
        if in_str:
            if ch == "\\":
                continue
            if ch == in_str:
                in_str = None
            continue
        if ch in ('"', "'", "`"):
            in_str = ch
            continue
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                literal = block[brace:idx + 1]
                break
    else:
        raise ValueError("El objeto CAMPAIGN no está balanceado.")

    return json.loads(js_object_to_json(literal))


def clean_prompt_text(text: str) -> str:
    """Quita los flags de Midjourney del cuerpo del prompt."""
    return MJ_FLAG_RE.sub("", text or "").strip().strip(",").strip()


def parse_aspect_ratio(*candidates: Optional[str]) -> str:
    """Primer `N:M` que aparezca en los candidatos (aspect_ratio o texto del prompt)."""
    for cand in candidates:
        if not cand:
            continue
        m = AR_RE.search(cand)
        if m:
            return f"{int(m.group(1))}:{int(m.group(2))}"
    return "1:1"


def parse_duration(raw: Optional[str]) -> Optional[int]:
    if not raw:
        return None
    m = re.search(r"(\d+)", str(raw))
    return int(m.group(1)) if m else None


def describe_concepts(campaign: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Aplana los items de CAMPAIGN a una lista utilizable para generar."""
    out = []
    for idx, item in enumerate(campaign.get("items", []), start=1):
        prompt_img = item.get("prompt") or {}
        prompt_vid = item.get("prompt_video") or {}
        medios = []
        if prompt_img.get("text"):
            medios.append("image")
        if prompt_vid.get("text"):
            medios.append("video")
        out.append({
            "index": idx,
            "sku": item.get("sku"),
            "platform": item.get("platform"),
            "concept_title": item.get("concept_title"),
            "inventiveness": item.get("inventiveness"),
            "target_persona": item.get("target_persona"),
            "medios_disponibles": medios,
            "prompt": prompt_img or None,
            "prompt_video": prompt_vid or None,
            "copy": item.get("copy") or {},
            "filter_justification": item.get("filter_justification"),
        })
    return out


def build_send_text(
    prompt_text: str,
    negative_prompt: Optional[str],
    negative_mode: str = "append",
    media_type: str = "image",
) -> str:
    """
    Texto final que viaja al modelo: cuerpo sin flags de Midjourney, con el
    negative prompt traducido a lenguaje natural (los endpoints de OpenRouter
    no exponen un parámetro `negative_prompt`).
    """
    body = clean_prompt_text(prompt_text)
    if negative_mode == "append" and negative_prompt:
        neg = clean_prompt_text(negative_prompt)
        if neg:
            soporte = "video" if media_type == "video" else "image"
            body += (
                f"\n\nStrictly do NOT include any of the following in the {soporte}: "
                + neg
                + "."
            )
    return body


# ---------------------------------------------------------------------------
# Catálogo en vivo
# ---------------------------------------------------------------------------

RECOMENDADOS_IMAGEN = ["gemini-3.1-flash-image", "gemini-3-pro-image", "gpt-5.4-image"]
RECOMENDADOS_VIDEO = ["google/veo-3.1", "bytedance/seedance-2.0", "kwaivgi/kling-v3.0-pro"]


def _headers(api_key: Optional[str] = None) -> Dict[str, str]:
    h = {
        "HTTP-Referer": "https://openrouter.ai",
        "X-Title": "Loco Tequila Media Generator",
    }
    if api_key and api_key.strip():
        h["Authorization"] = f"Bearer {api_key.strip()}"
    return h


def _precio_por_segundo(pricing_skus: Dict[str, Any]) -> Optional[float]:
    """
    Extrae el precio por segundo de `pricing_skus`. Las llaves varían por
    proveedor (`duration_seconds`, `duration_seconds_720p`,
    `duration_seconds_with_audio`…). Los modelos que cobran por token de video
    (`video_tokens`) no son estimables desde aquí y devuelven None.
    """
    if not pricing_skus:
        return None
    preferidas = [
        "duration_seconds_with_audio", "duration_seconds", "duration_seconds_720p",
        "duration_seconds_1080p", "text_to_video_duration_seconds_720p",
        "duration_seconds_without_audio",
    ]
    for k in preferidas:
        if k in pricing_skus:
            try:
                return float(pricing_skus[k])
            except (TypeError, ValueError):
                continue
    for k, v in pricing_skus.items():
        if "duration_seconds" in k:
            try:
                return float(v)
            except (TypeError, ValueError):
                continue
    return None


def fetch_video_models(api_key: Optional[str] = None) -> Dict[str, Any]:
    """Catálogo de video desde `/api/v1/videos/models`, con capacidades por modelo."""
    try:
        r = requests.get(VIDEO_MODELS_URL, headers=_headers(api_key), timeout=25)
        r.raise_for_status()
        data = r.json().get("data", [])
        modelos = []
        for m in data:
            mid = m.get("id", "")
            desc = m.get("description", "") or ""
            pps = _precio_por_segundo(m.get("pricing_skus") or {})
            modelos.append({
                "id": mid,
                "name": m.get("name", mid),
                "description": desc[:160] + "..." if len(desc) > 160 else desc,
                "supported_durations": m.get("supported_durations"),
                "supported_aspect_ratios": m.get("supported_aspect_ratios"),
                "supported_resolutions": m.get("supported_resolutions"),
                "generate_audio": m.get("generate_audio"),
                "precio_usd_por_segundo": pps,
                "pricing_skus": m.get("pricing_skus"),
                "allowed_passthrough_parameters": m.get("allowed_passthrough_parameters"),
                "recommended": any(k in mid for k in RECOMENDADOS_VIDEO),
            })
        if not modelos:
            raise ValueError("El catálogo de video llegó vacío.")
        modelos.sort(key=lambda x: (not x["recommended"], x["precio_usd_por_segundo"] or 9e9))
        return {
            "status": "success", "source": "live_api", "modality": "video",
            "endpoint": VIDEO_MODELS_URL, "count": len(modelos), "models": modelos,
        }
    except Exception as e:
        return {
            "status": "fallback", "source": "cached_fallback", "modality": "video",
            "message": f"No se pudo consultar el catálogo de video ({e}). Usando respaldo.",
            "count": len(FALLBACK_VIDEO_MODELS), "models": FALLBACK_VIDEO_MODELS,
        }


def fetch_live_models(api_key: Optional[str] = None, modality: str = "image") -> Dict[str, Any]:
    if modality == "video":
        return fetch_video_models(api_key)

    try:
        response = requests.get(MODELS_URL, headers=_headers(api_key), timeout=25)
        response.raise_for_status()
        data = response.json().get("data", [])

        matched_models = []
        for m in data:
            arch = m.get("architecture", {})
            out_mods = arch.get("output_modalities", []) or []
            model_id = m.get("id", "")
            desc = m.get("description", "") or ""
            pricing = m.get("pricing", {}) or {}

            if "image" in out_mods or model_id in ("openrouter/auto", "openrouter/auto-beta"):
                matched_models.append({
                    "id": model_id,
                    "name": m.get("name", model_id),
                    "description": desc[:160] + "..." if len(desc) > 160 else desc,
                    "precio_usd_por_imagen": (
                        float(pricing["image_output"]) if pricing.get("image_output") else None
                    ),
                    "pricing": {
                        "prompt": pricing.get("prompt"),
                        "completion": pricing.get("completion"),
                        "image_output": pricing.get("image_output"),
                    },
                    "recommended": any(k in model_id.lower() for k in RECOMENDADOS_IMAGEN),
                })

        if not matched_models:
            raise ValueError("El catálogo de imagen llegó vacío.")
        matched_models.sort(key=lambda x: (not x["recommended"], x["precio_usd_por_imagen"] or 9e9))
        return {
            "status": "success", "source": "live_api", "modality": "image",
            "endpoint": MODELS_URL, "count": len(matched_models), "models": matched_models,
        }

    except Exception as e:
        return {
            "status": "fallback", "source": "cached_fallback", "modality": "image",
            "message": f"No se pudo consultar la API en vivo ({e}). Usando catálogo de respaldo.",
            "count": len(FALLBACK_IMAGE_MODELS), "models": FALLBACK_IMAGE_MODELS,
        }


# ---------------------------------------------------------------------------
# Encaje de parámetros a lo que el modelo realmente acepta
# ---------------------------------------------------------------------------

def snap_duration(pedida: int, soportadas: Optional[List[int]]) -> Any:
    """Ajusta la duración a la más cercana que el modelo acepta."""
    if not soportadas:
        return pedida, None
    if pedida in soportadas:
        return pedida, None
    elegida = min(soportadas, key=lambda d: (abs(d - pedida), d))
    return elegida, (
        f"{pedida}s no está entre las duraciones que acepta el modelo "
        f"({soportadas}); se usa {elegida}s."
    )


def snap_aspect_ratio(pedido: str, soportados: Optional[List[str]]) -> Any:
    """Ajusta el aspect ratio al más cercano que el modelo acepta."""
    if not soportados or pedido in soportados:
        return pedido, None

    def valor(txt: str) -> Optional[float]:
        m = AR_RE.search(txt or "")
        if not m or int(m.group(2)) == 0:
            return None
        return int(m.group(1)) / int(m.group(2))

    objetivo = valor(pedido)
    validos = [(s, valor(s)) for s in soportados]
    validos = [(s, v) for s, v in validos if v]
    if objetivo is None or not validos:
        return soportados[0], f"No se pudo interpretar '{pedido}'; se usa {soportados[0]}."
    elegido = min(validos, key=lambda sv: abs(sv[1] - objetivo))[0]
    return elegido, (
        f"El modelo no acepta {pedido} (solo {soportados}); se usa {elegido}. "
        "El encuadre del prompt fue pensado para el otro formato: revisa el recorte."
    )


# ---------------------------------------------------------------------------
# Generación de imagen
# ---------------------------------------------------------------------------

def generate_image(
    api_key: str,
    prompt: str,
    model: str,
    aspect_ratio: str = "1:1",
    output_dir: Optional[Path] = None,
    file_stem: Optional[str] = None,
    site_url: str = "https://openrouter.ai",
    site_name: str = "Loco Tequila Media Generator"
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key.strip()}",
        "HTTP-Referer": site_url,
        "X-Title": site_name,
        "Content-Type": "application/json"
    }

    aspect_ratio_map = {
        "1:1": {"width": 1024, "height": 1024},
        "16:9": {"width": 1344, "height": 768},
        "9:16": {"width": 768, "height": 1344},
        "4:3": {"width": 1152, "height": 864},
        "3:4": {"width": 864, "height": 1152},
        "4:5": {"width": 896, "height": 1120},
        "5:4": {"width": 1120, "height": 896},
        "21:9": {"width": 1536, "height": 640}
    }
    dimensions = aspect_ratio_map.get(aspect_ratio, {"width": 1024, "height": 1024})

    timestamp = int(time.time())
    sanitized_model = model.replace("/", "_").replace(":", "_")[:25]
    stem = file_stem or f"image_{timestamp}_{sanitized_model}"
    file_name = f"{stem}.png"
    out_file = (output_dir or Path("./outputs/images")) / file_name

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "modalities": ["image", "text"]
    }

    try:
        response = requests.post(CHAT_COMPLETIONS_URL, headers=headers, json=payload, timeout=180)

        if response.status_code == 404 or response.status_code == 400:
            direct_payload = {
                "model": model,
                "prompt": prompt,
                "n": 1,
                "size": f"{dimensions['width']}x{dimensions['height']}"
            }
            alt_res = requests.post(IMAGES_GENERATIONS_URL, headers=headers, json=direct_payload, timeout=180)
            if alt_res.status_code == 200:
                response = alt_res

        response.raise_for_status()
        res_json = response.json()

        image_url = None
        local_path = None

        if "choices" in res_json and len(res_json["choices"]) > 0:
            choice = res_json["choices"][0]
            msg = choice.get("message", {})
            content = msg.get("content", "")

            if isinstance(content, list):
                for part in content:
                    if isinstance(part, dict):
                        if part.get("type") == "image_url":
                            img_obj = part.get("image_url", {})
                            raw_url = img_obj.get("url", "")
                            if raw_url.startswith("data:image"):
                                local_path = save_b64_file(raw_url, out_file)
                            elif raw_url.startswith("http"):
                                image_url = raw_url
                                local_path = download_file(image_url, out_file)
                        elif part.get("type") == "image":
                            source = part.get("source", {})
                            if source.get("type") == "base64":
                                data = source.get("data", "")
                                local_path = save_b64_file(data, out_file)

            elif isinstance(content, str):
                urls = re.findall(r'(https?://[^\s)"]+)', content)
                for u in urls:
                    if any(u.lower().endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".webp"]) or "image" in u:
                        image_url = u
                        try:
                            local_path = download_file(image_url, out_file)
                            break
                        except Exception:
                            continue

            if not local_path and "images" in msg:
                for img_item in msg["images"]:
                    if isinstance(img_item, str):
                        if img_item.startswith("http"):
                            image_url = img_item
                            local_path = download_file(image_url, out_file)
                            break
                        elif len(img_item) > 100:
                            local_path = save_b64_file(img_item, out_file)
                            break
                    elif isinstance(img_item, dict):
                        if "url" in img_item:
                            candidate = img_item["url"]
                            if isinstance(candidate, dict):
                                candidate = candidate.get("url", "")
                            if isinstance(candidate, str) and candidate.startswith("data:image"):
                                local_path = save_b64_file(candidate, out_file)
                                break
                            if isinstance(candidate, str) and candidate.startswith("http"):
                                image_url = candidate
                                local_path = download_file(image_url, out_file)
                                break
                        if img_item.get("type") == "image_url":
                            candidate = (img_item.get("image_url") or {}).get("url", "")
                            if candidate.startswith("data:image"):
                                local_path = save_b64_file(candidate, out_file)
                                break
                            if candidate.startswith("http"):
                                image_url = candidate
                                local_path = download_file(image_url, out_file)
                                break

        elif "data" in res_json and len(res_json["data"]) > 0:
            item = res_json["data"][0]
            if "url" in item:
                image_url = item["url"]
                local_path = download_file(image_url, out_file)
            elif "b64_json" in item:
                local_path = save_b64_file(item["b64_json"], out_file)
                image_url = str(local_path.resolve())

        abs_path_str = str(local_path.resolve()).replace("\\", "/") if local_path else None

        if not abs_path_str:
            return {
                "status": "error",
                "type": "image",
                "model": model,
                "message": "OpenRouter respondió 200 pero no se encontró imagen en la respuesta.",
                "detail": json.dumps(res_json)[:1200]
            }

        return {
            "status": "success",
            "type": "image",
            "model": model,
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "dimensions": f"{dimensions['width']}x{dimensions['height']}",
            "cost": (res_json.get("usage") or {}).get("cost"),
            "file_path": abs_path_str,
            "url": image_url or f"file:///{abs_path_str}",
            "markdown_display": f"![{prompt[:40]}]({abs_path_str})"
        }

    except requests.exceptions.RequestException as e:
        error_detail = ""
        if hasattr(e, "response") and e.response is not None:
            try:
                error_detail = e.response.text[:1200]
            except Exception:
                pass
        return {
            "status": "error",
            "type": "image",
            "model": model,
            "message": f"Error en llamada a OpenRouter: {str(e)}",
            "detail": error_detail
        }


# ---------------------------------------------------------------------------
# Generación de video
# ---------------------------------------------------------------------------

def generate_video(
    api_key: str,
    prompt: str,
    model: str,
    duration_seconds: int = 5,
    aspect_ratio: str = "16:9",
    output_dir: Optional[Path] = None,
    file_stem: Optional[str] = None,
    poll_interval_seconds: int = 5,
    max_poll_attempts: int = 60,
) -> Dict[str, Any]:
    """
    Genera un video ultra-corto usando el endpoint asíncrono de OpenRouter
    (POST /api/v1/videos + polling en polling_url) en lugar del endpoint
    de chat completions, que no soporta la modalidad "video" para todos
    los modelos (p. ej. bytedance/seedance-2.0-mini).
    """
    # La duración llega YA encajada a `supported_durations` del modelo por
    # quien llama (modo lote) o acotada por --max-duration (modo manual).
    # Aquí solo se aplica un piso de sanidad: clamparla otra vez a 10 s rompería
    # los modelos de duraciones discretas (Sora acepta 4/8/12/16/20).
    if duration_seconds < 2:
        duration_seconds = 3

    headers = {
        "Authorization": f"Bearer {api_key.strip()}",
        "Content-Type": "application/json",
    }

    timestamp = int(time.time())
    sanitized_model = model.replace("/", "_").replace(":", "_")[:25]
    stem = file_stem or f"video_{timestamp}_{sanitized_model}"
    file_name = f"{stem}.mp4"
    out_file = (output_dir or Path("./outputs/videos")) / file_name

    # Payload base. Algunos modelos no aceptan duration/aspect_ratio;
    # si el submit falla con 400 por parámetros desconocidos, se reintenta
    # con el payload mínimo.
    payload = {
        "model": model,
        "prompt": prompt,
        "duration": duration_seconds,
        "aspect_ratio": aspect_ratio,
    }

    try:
        submit_res = requests.post(
            VIDEOS_URL, headers=headers, json=payload, timeout=60
        )

        if submit_res.status_code == 400:
            # Reintento con payload mínimo (solo model + prompt)
            minimal_payload = {"model": model, "prompt": prompt}
            submit_res = requests.post(
                VIDEOS_URL, headers=headers, json=minimal_payload, timeout=60
            )

        submit_res.raise_for_status()
        submit_data = submit_res.json()

        job_id = submit_data.get("id")
        polling_url = submit_data.get("polling_url")

        if not polling_url:
            return {
                "status": "error",
                "type": "video",
                "model": model,
                "message": "La respuesta de OpenRouter no incluyó polling_url.",
                "detail": json.dumps(submit_data)[:1200],
            }

        # --- Polling hasta completar o fallar ---
        status_data: Dict[str, Any] = {}
        for _ in range(max_poll_attempts):
            poll_res = requests.get(polling_url, headers=headers, timeout=30)
            poll_res.raise_for_status()
            status_data = poll_res.json()
            status = status_data.get("status")

            if status == "completed":
                break
            elif status == "failed":
                return {
                    "status": "error",
                    "type": "video",
                    "model": model,
                    "message": "La generación del video falló en OpenRouter.",
                    "detail": status_data.get("error", "Unknown error"),
                }
            time.sleep(poll_interval_seconds)
        else:
            return {
                "status": "error",
                "type": "video",
                "model": model,
                "message": f"Timeout esperando la generación (job_id={job_id}).",
                "detail": json.dumps(status_data)[:1200],
            }

        # --- Descarga del contenido generado ---
        unsigned_urls = status_data.get("unsigned_urls", [])
        video_url = unsigned_urls[0] if unsigned_urls else None
        local_path = None

        if video_url:
            out_file.parent.mkdir(parents=True, exist_ok=True)
            local_path = download_file(video_url, out_file)

        abs_path_str = (
            str(local_path.resolve()).replace("\\", "/") if local_path else None
        )

        result = {
            "status": "success",
            "type": "video",
            "model": model,
            "prompt": prompt,
            "duration_seconds": duration_seconds,
            "aspect_ratio": aspect_ratio,
            "job_id": job_id,
            "cost": (status_data.get("usage") or {}).get("cost"),
            "file_path": abs_path_str,
            "url": video_url,
            "markdown_display": f"![Video: {prompt[:40]}]({abs_path_str if abs_path_str else video_url})",
        }
        return result

    except requests.exceptions.RequestException as e:
        error_detail = ""
        if hasattr(e, "response") and e.response is not None:
            try:
                error_detail = e.response.text[:1200]
            except Exception:
                pass
        return {
            "status": "error",
            "type": "video",
            "model": model,
            "message": f"Error en llamada a OpenRouter para video: {str(e)}",
            "detail": error_detail,
        }


# ---------------------------------------------------------------------------
# Lote desde la Pasarela
# ---------------------------------------------------------------------------

def resolve_indices(spec: Optional[str], first: Optional[int], available: List[int]) -> List[int]:
    """Traduce --indices / --first a la lista concreta de índices a generar."""
    if spec:
        wanted = []
        for chunk in spec.split(","):
            chunk = chunk.strip()
            if not chunk:
                continue
            if "-" in chunk:
                a, b = chunk.split("-", 1)
                wanted.extend(range(int(a), int(b) + 1))
            else:
                wanted.append(int(chunk))
        return [i for i in wanted if i in available]
    if first:
        return available[:first]
    return available


def generate_from_campaign(
    api_key: str,
    campaign_path: Path,
    media_type: str,
    model: str,
    indices_spec: Optional[str],
    first: Optional[int],
    dirs: Dict[str, Path],
    aspect_override: Optional[str],
    duration_override: Optional[int],
    max_duration: int,
    negative_mode: str,
    dry_run: bool,
) -> Dict[str, Any]:
    campaign = load_campaign(campaign_path)
    concepts = describe_concepts(campaign)
    available = [c["index"] for c in concepts if media_type in c["medios_disponibles"]]
    sin_medio = [c["index"] for c in concepts if media_type not in c["medios_disponibles"]]

    if not available:
        return {
            "status": "error",
            "code": "NO_PROMPTS_FOR_MEDIA",
            "message": (
                f"Ningún concepto de {campaign_path.name} tiene prompt de {media_type}. "
                f"Conceptos totales: {len(concepts)}."
            ),
            "campaign_title": campaign.get("title"),
        }

    targets = resolve_indices(indices_spec, first, available)
    if not targets:
        return {
            "status": "error",
            "code": "NO_VALID_INDICES",
            "message": f"Los índices pedidos no tienen prompt de {media_type}.",
            "indices_disponibles": available,
        }

    # Capacidades reales del modelo elegido: duraciones y aspectos que acepta,
    # y precio por segundo. Sin esto se envían valores que el proveedor rechaza
    # con 400 (Veo 3.1 solo admite 4/6/8 s y 16:9 o 9:16).
    especificaciones_modelo: Dict[str, Any] = {}
    aviso_catalogo = None
    catalogo = fetch_live_models(api_key or None, media_type)
    encontrado = next((m for m in catalogo["models"] if m["id"] == model), None)
    if encontrado:
        especificaciones_modelo = encontrado
    else:
        aviso_catalogo = (
            f"'{model}' no aparece en el catálogo de {media_type} de OpenRouter. "
            "No se pudo encajar parámetros ni estimar costo; si el proveedor los "
            f"rechaza, verifica el id con: --action list-models --type {media_type}"
        )

    by_index = {c["index"]: c for c in concepts}
    results = []
    costo_estimado = 0.0
    estimacion_incompleta = False

    for idx in targets:
        concept = by_index[idx]
        block = concept["prompt"] if media_type == "image" else concept["prompt_video"]
        send_text = build_send_text(
            block.get("text", ""), block.get("negative_prompt"), negative_mode, media_type
        )
        ar_pedido = aspect_override or parse_aspect_ratio(block.get("aspect_ratio"), block.get("text"))
        ar, aviso_ar = snap_aspect_ratio(
            ar_pedido, especificaciones_modelo.get("supported_aspect_ratios")
        )
        stem = f"{slugify(concept.get('platform') or '')}-{idx:02d}-{slugify(concept.get('concept_title') or '')}-{int(time.time())}"

        specs = {
            "concepto": idx,
            "sku": concept.get("sku"),
            "plataforma": concept.get("platform"),
            "titulo_concepto": concept.get("concept_title"),
            "inventiva": concept.get("inventiveness"),
            "persona_objetivo": concept.get("target_persona"),
            "aspect_ratio_prompt": block.get("aspect_ratio"),
            "aspect_ratio_enviado": ar,
            "negative_prompt": block.get("negative_prompt"),
            "prompt_original": block.get("text"),
            "prompt_enviado": send_text,
        }
        if aviso_ar:
            specs["aviso_aspect_ratio"] = aviso_ar

        dur = None
        if media_type == "image":
            specs["camera_settings"] = block.get("camera_settings")
            specs["color_palette"] = block.get("color_palette")
            pxi = especificaciones_modelo.get("precio_usd_por_imagen")
            if pxi:
                costo_estimado += pxi
                specs["costo_estimado_usd"] = round(pxi, 6)
            else:
                estimacion_incompleta = True
        else:
            # Duración y aspecto se resuelven ANTES de generar para que todo
            # recorte sea visible en --dry-run, no una sorpresa ya pagada.
            pedida = duration_override or parse_duration(block.get("duration")) or 5
            acotada = min(pedida, max_duration)
            dur, aviso_dur = snap_duration(
                acotada, especificaciones_modelo.get("supported_durations")
            )
            specs["duracion_prompt"] = block.get("duration")
            specs["duracion_enviada_s"] = dur
            avisos = []
            if pedida > acotada:
                avisos.append(
                    f"El prompt pide {pedida}s y el tope de costo es {max_duration}s "
                    "(--max-duration para subirlo). Se obtendrá un FRAGMENTO, no la "
                    "pieza completa: el resto se edita fuera."
                )
            if aviso_dur:
                avisos.append(aviso_dur)
            if avisos:
                specs["aviso_duracion"] = " ".join(avisos)

            pps = especificaciones_modelo.get("precio_usd_por_segundo")
            if pps and dur:
                sub = pps * dur
                costo_estimado += sub
                specs["costo_estimado_usd"] = round(sub, 4)
                specs["precio_usd_por_segundo"] = pps
            else:
                estimacion_incompleta = True

            specs["movimiento_camara"] = block.get("camera_movement")
            specs["audio"] = block.get("audio")
            specs["escenas"] = block.get("scenes")

        entry = {
            "concepto": idx,
            "especificaciones": specs,
            "copy": concept.get("copy"),
            "filter_justification": concept.get("filter_justification"),
        }

        if dry_run:
            entry["generacion"] = {"status": "dry_run", "type": media_type, "model": model}
            results.append(entry)
            continue

        if media_type == "image":
            entry["generacion"] = generate_image(
                api_key=api_key, prompt=send_text, model=model,
                aspect_ratio=ar, output_dir=dirs["images"], file_stem=stem,
            )
        else:
            entry["generacion"] = generate_video(
                api_key=api_key, prompt=send_text, model=model,
                duration_seconds=dur or 5, aspect_ratio=ar,
                output_dir=dirs["videos"], file_stem=stem,
            )
        results.append(entry)

    ok = [r for r in results if (r["generacion"].get("status") in ("success", "dry_run"))]
    costs = [r["generacion"].get("cost") for r in results if r["generacion"].get("cost")]

    salida = {
        "status": "success" if len(ok) == len(results) else "partial",
        "action": "generate",
        "dry_run": dry_run,
        "campaign_file": str(campaign_path).replace("\\", "/"),
        "campaign_title": campaign.get("title"),
        "media_type": media_type,
        "model": model,
        "modelo_en_catalogo": bool(especificaciones_modelo),
        "solicitados": len(targets),
        "exitosos": len(ok),
        "conceptos_sin_este_medio": sin_medio,
        "costo_estimado_total_usd": round(costo_estimado, 4) if costo_estimado else None,
        "costo_real_total_usd": round(sum(costs), 6) if costs else None,
        "results": results,
    }
    if aviso_catalogo:
        salida["aviso_catalogo"] = aviso_catalogo
    if estimacion_incompleta:
        salida["aviso_costo"] = (
            "La estimación de costo está INCOMPLETA: al menos un modelo no publica "
            "precio por segundo/imagen en el catálogo (p. ej. los que cobran por "
            "token de video). El costo real llega en `costo_real_total_usd` después "
            "de generar. Trátalo como estimación marcada con `*`."
        )
    if dry_run:
        salida["nota"] = (
            "DRY-RUN: no se llamó a la API ni se gastaron créditos. Revisa "
            "`prompt_enviado`, `aspect_ratio_enviado`, `duracion_enviada_s` y el "
            "costo estimado antes de generar de verdad."
        )
    return salida


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generador de imágenes y videos ultracortos (OpenRouter) para Loco Tequila"
    )
    parser.add_argument("--action",
                        choices=["generate", "list-models", "extract-prompts", "check-key"],
                        default="generate", help="Acción a realizar")
    parser.add_argument("--type", choices=["image", "video"], default="image",
                        help="Tipo de medio (image o video)")
    parser.add_argument("--prompt", default="", help="Prompt suelto (modo manual, sin pasarela)")
    parser.add_argument("--model", default="", help="Modelo oficial de OpenRouter a utilizar")
    parser.add_argument("--api-key", default=None,
                        help="API Key de OpenRouter (ingresada en chat o pasada por el agente)")
    parser.add_argument("--api-key-file", default=None,
                        help=f"Archivo con la clave (por defecto {default_key_file()})")
    parser.add_argument("--from-showcase", default=None,
                        help="Ruta del HTML de campaña (showcase/campaign-*.html) del que se leen los prompts")
    parser.add_argument("--indices", default=None,
                        help="Conceptos a generar: '1,3' o '1-4'. Por defecto, todos los disponibles")
    parser.add_argument("--first", type=int, default=None,
                        help="Generar los primeros N conceptos disponibles")
    parser.add_argument("--aspect-ratio", default=None,
                        help="Forzar aspect ratio. Por defecto se toma del prompt")
    parser.add_argument("--duration", type=int, default=None,
                        help="Duración en segundos para video. Por defecto se toma del prompt")
    parser.add_argument("--max-duration", type=int, default=MAX_VIDEO_DURATION_SECONDS,
                        help=(f"Tope de COSTO en segundos de video (por defecto "
                              f"{MAX_VIDEO_DURATION_SECONDS}s). No es un límite de la API: "
                              "el precio es por segundo, así que subirlo cuesta más"))
    parser.add_argument("--negative-mode", choices=["append", "omit"], default="append",
                        help="Cómo tratar el negative prompt (OpenRouter no tiene parámetro nativo)")
    parser.add_argument("--out-dir", default=None, help="Directorio base para outputs/")
    parser.add_argument("--dry-run", action="store_true",
                        help="Resuelve prompts, aspect ratios y specs SIN llamar a la API ni gastar créditos")

    args = parser.parse_args()

    # La clave se RESUELVE, no se recibe: sale del archivo del usuario, de la
    # variable de entorno o de --api-key, en ese orden inverso de preferencia.
    api_key, origen_clave = resolve_api_key(args.api_key, args.api_key_file)

    if args.action == "check-key":
        resultado = check_key(args.api_key, args.api_key_file)
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
        sys.exit(0 if resultado.get("status") == "success" else 1)

    # --- Acciones que no requieren API key ---
    if args.action == "list-models":
        print(json.dumps(fetch_live_models(api_key=api_key, modality=args.type),
                         indent=2, ensure_ascii=False))
        return

    if args.action == "extract-prompts":
        if not args.from_showcase:
            print(json.dumps({
                "status": "error",
                "code": "MISSING_SHOWCASE",
                "message": "extract-prompts requiere --from-showcase <ruta del HTML de campaña>."
            }, indent=2, ensure_ascii=False))
            sys.exit(1)
        try:
            campaign = load_campaign(Path(args.from_showcase))
        except Exception as e:
            print(json.dumps({
                "status": "error", "code": "CAMPAIGN_PARSE_FAILED", "message": str(e)
            }, indent=2, ensure_ascii=False))
            sys.exit(1)
        conceptos = describe_concepts(campaign)
        print(json.dumps({
            "status": "success",
            "action": "extract-prompts",
            "campaign_file": str(Path(args.from_showcase)).replace("\\", "/"),
            "campaign_title": campaign.get("title"),
            "date_context": campaign.get("date_context"),
            "total_conceptos": len(conceptos),
            "max_imagenes": sum(1 for c in conceptos if "image" in c["medios_disponibles"]),
            "max_videos": sum(1 for c in conceptos if "video" in c["medios_disponibles"]),
            "conceptos": conceptos,
        }, indent=2, ensure_ascii=False))
        return

    # --- generate: requiere API key ---
    if not args.dry_run and not api_key:
        ruta = Path(args.api_key_file) if args.api_key_file else default_key_file()
        print(json.dumps({
            "status": "error",
            "code": "MISSING_API_KEY",
            "archivo_esperado": str(ruta).replace("\\", "/"),
            "message": (
                "No hay API Key disponible. El usuario puede ingresar su clave de OpenRouter "
                f"en el chat o guardarla en el archivo {ruta}. "
                "Verificar después con --action check-key."
            ),
        }, indent=2, ensure_ascii=False))
        sys.exit(1)

    base_workspace = Path(args.out_dir) if args.out_dir else Path.cwd()
    dirs = ensure_output_dirs(base_workspace)

    # Modo lote desde la pasarela
    if args.from_showcase:
        if not args.model:
            print(json.dumps({
                "status": "error", "code": "MISSING_MODEL",
                "message": "--model es obligatorio. Pregunta al usuario qué modelo usar (ver --action list-models)."
            }, indent=2, ensure_ascii=False))
            sys.exit(1)
        try:
            result = generate_from_campaign(
                api_key=api_key or "", campaign_path=Path(args.from_showcase),
                media_type=args.type, model=args.model, indices_spec=args.indices,
                first=args.first, dirs=dirs, aspect_override=args.aspect_ratio,
                duration_override=args.duration, max_duration=args.max_duration,
                negative_mode=args.negative_mode, dry_run=args.dry_run,
            )
        except Exception as e:
            result = {"status": "error", "code": "BATCH_FAILED", "message": str(e)}
        print(json.dumps(result, indent=2, ensure_ascii=False))
        sys.exit(0 if result.get("status") in ("success", "partial") else 1)

    # Modo manual (un prompt suelto)
    if not args.model or not args.prompt:
        print(json.dumps({
            "status": "error",
            "code": "MISSING_REQUIRED_PARAMS",
            "message": ("Faltan parámetros: usa --from-showcase (recomendado) o bien "
                        "--prompt y --model juntos.")
        }, indent=2, ensure_ascii=False))
        sys.exit(1)

    if args.type == "image":
        result = generate_image(
            api_key=api_key, prompt=args.prompt, model=args.model,
            aspect_ratio=args.aspect_ratio or parse_aspect_ratio(args.prompt),
            output_dir=dirs["images"],
        )
    else:
        result = generate_video(
            api_key=api_key, prompt=args.prompt, model=args.model,
            duration_seconds=min(args.duration or 5, args.max_duration),
            aspect_ratio=args.aspect_ratio or "16:9", output_dir=dirs["videos"],
        )

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
