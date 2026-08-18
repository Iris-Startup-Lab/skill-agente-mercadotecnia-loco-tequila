#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Obtiene el leaderboard EN VIVO de generadores de imagen (y video) desde Design Arena
y lo cruza con la curaduría propia de Loco Tequila.

Por qué existe: https://www.designarena.ai/leaderboard/image es una app Next.js que
renderiza la tabla en el cliente, así que scrapear el HTML no sirve. Los datos vienen
de un endpoint POST que el bundle consume:

    POST https://www.designarena.ai/api/leaderboard
    {"arenaType": "models", "category": "image", "variationName": "public"}

Salida: elo, winRate, wins/losses/battles y tiempo medio de generación, reales y
verificables. La curaduría (recomendación, tips, rating de marca) NO viene de ahí:
vive en references/curaduria-modelos-imagen.json, indexada por familia de modelo
para sobrevivir al cambio de versiones.

Uso:
    python obtener_leaderboard.py                          # top 12 de imagen, a pantalla
    python obtener_leaderboard.py --categoria video        # ranking de video
    python obtener_leaderboard.py --top 20
    python obtener_leaderboard.py --incluir-anonimos       # incluye modelos en prueba ciega
    python obtener_leaderboard.py --actualizar-showcase    # reescribe showcase/data/leaderboard.json + app.js
    python obtener_leaderboard.py --json salida.json
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Falta 'requests'. Instálalo con: pip install requests")

API_URL = "https://www.designarena.ai/api/leaderboard"
SOURCE_URL = "https://www.designarena.ai/leaderboard/image"
RAIZ = Path(__file__).resolve().parents[2]
CURADURIA = RAIZ / "references" / "curaduria-modelos-imagen.json"
LEADERBOARD_JSON = RAIZ / "showcase" / "data" / "leaderboard.json"
APP_JS = RAIZ / "showcase" / "app.js"

# Familias públicas reconocidas: prefijo/patrón -> clave de curaduría.
# Todo modelId que no case con ninguna se considera nombre clave anónimo
# (modelo en prueba ciega, no disponible al público) y se omite por defecto.
FAMILIAS = [
    (r"^gpt-image", "gpt-image"),
    (r"^dalle", "dalle"),
    (r"^imagen-", "imagen"),
    (r"^gemini", "gemini"),
    (r"^flux", "flux"),
    (r"^recraft", "recraft"),
    (r"^ideogram", "ideogram"),
    (r"^seedream", "seedream"),
    (r"^krea", "krea"),
    (r"^riverflow", "riverflow"),
    (r"^qwen", "qwen"),
    (r"^grok", "grok"),
    (r"^(stable|sd)[-.]?", "stable-diffusion"),
    (r"^midjourney", "midjourney"),
    (r"^mai-image", "mai-image"),
    (r"^hidream", "hidream"),
    (r"^hunyuanimage", "hunyuan"),
    (r"^ernie", "ernie"),
    (r"^glm", "glm"),
    (r"^wan[-.0-9]", "wan"),
    (r"^z-image", "z-image"),
    (r"^reve", "reve"),
    (r"^imagineart", "imagineart"),
    (r"^cosmos", "cosmos"),
    (r"^viduq", "vidu"),
    # --- Arena de video (la skill también genera prompts de video) ---
    (r"^sora", "sora"),
    (r"^veo-", "veo"),
    (r"^kling", "kling"),
    (r"^ray-", "ray"),
    (r"^seedance", "seedance"),
    (r"^(hailuo|minimax)", "minimax"),
    (r"^ltx-", "ltx"),
    (r"^kandinsky", "kandinsky"),
    (r"^hunyuan", "hunyuan"),
    (r"^pika", "pika"),
    (r"^(runway|gen-[34])", "runway"),
    (r"^glam-ai", "glam"),
]

DEV_FALLBACK = {
    "mai-image": "Microsoft AI", "hidream": "HiDream", "hunyuan": "Tencent",
    "ernie": "Baidu", "glm": "Zhipu AI", "wan": "Alibaba", "z-image": "Alibaba",
    "reve": "Reve", "imagineart": "ImagineArt", "cosmos": "NVIDIA", "vidu": "Vidu",
    "sora": "OpenAI", "veo": "Google DeepMind", "kling": "Kuaishou",
    "ray": "Luma AI", "seedance": "ByteDance", "minimax": "MiniMax",
    "ltx": "Lightricks", "kandinsky": "Sber", "pika": "Pika Labs",
    "runway": "Runway", "glam": "Glam AI",
}


def familia_de(model_id):
    """Devuelve la clave de familia, o None si es un nombre clave anónimo."""
    mid = model_id.lower()
    for patron, clave in FAMILIAS:
        if re.search(patron, mid):
            return clave
    return None


def consultar_api(categoria, timeout):
    payload = {"arenaType": "models", "category": categoria, "variationName": "public"}
    try:
        r = requests.post(
            API_URL,
            json=payload,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            timeout=timeout,
        )
    except requests.RequestException as e:
        sys.exit("No se pudo consultar la API de Design Arena: {}".format(e))

    if r.status_code != 200:
        detalle = ""
        try:
            detalle = " — " + str(r.json().get("message", ""))
        except ValueError:
            pass
        sys.exit("La API respondió HTTP {}{}".format(r.status_code, detalle))

    try:
        cuerpo = r.json()
    except ValueError:
        sys.exit("La API respondió algo que no es JSON (¿cambió el contrato?)")

    if cuerpo.get("code") == "rate_limit_exceeded":
        sys.exit("Rate limit de Design Arena alcanzado. Reintenta más tarde.")
    if not cuerpo.get("success"):
        sys.exit("La API respondió success=false: {}".format(cuerpo.get("message", "sin mensaje")))

    return cuerpo.get("data", [])


def cargar_curaduria():
    if not CURADURIA.exists():
        print("Aviso: no se encontró {}; se omite la curaduría.".format(CURADURIA), file=sys.stderr)
        return {}
    with CURADURIA.open(encoding="utf-8") as f:
        return json.load(f).get("familias", {})


def construir(datos, curaduria, top, incluir_anonimos, todas_las_versiones=False):
    modelos, anonimos, familias_vistas = [], [], set()
    for m in datos:
        fam = familia_de(m["modelId"])
        if fam is None:
            anonimos.append(m["modelId"])
            if not incluir_anonimos:
                continue
        # Por defecto solo la mejor versión de cada familia: un leaderboard que
        # responde "qué herramienta uso" no gana nada listando 5 variantes de la misma.
        # Los datos llegan ordenados por elo descendente, así que la primera es la mejor.
        if fam is not None and not todas_las_versiones:
            if fam in familias_vistas:
                continue
            familias_vistas.add(fam)
        cur = curaduria.get(fam, {}) if fam else {}
        modelos.append({
            "rank": 0,  # se asigna abajo, tras el filtrado
            "model_id": m["modelId"],
            "name": m["modelId"],
            "family": fam or "(anónimo)",
            "developer": cur.get("developer") or DEV_FALLBACK.get(fam) or "[no disponible]",
            "elo_score": m.get("elo"),
            "win_rate": m.get("winRate"),
            "battles": m.get("battles"),
            "avg_generation_ms": m.get("avgGenerationTimeMs"),
            "badge": cur.get("badge", "[no disponible]"),
            "category": cur.get("category", "Sin curaduría"),
            "tags": cur.get("tags", []),
            "loco_rating": cur.get("loco_rating", "[no disponible]"),
            "recommendation": cur.get(
                "recommendation",
                "Sin curaduría de Loco Tequila para esta familia. Evaluar antes de recomendarlo.",
            ),
            "settings_tip": cur.get("settings_tip", "[no disponible]"),
            "publicly_available": fam is not None,
        })

    modelos = modelos[:top]
    for i, m in enumerate(modelos, 1):
        m["rank"] = i

    categorias = ["Todos"] + sorted({m["category"] for m in modelos if m["category"] != "Sin curaduría"})
    return modelos, categorias, anonimos


def escribir_leaderboard_json(modelos, categorias, categoria, anonimos, incluir_anonimos):
    doc = {
        "last_updated": date.today().isoformat(),
        "source": "Design Arena — ranking en vivo vía API. Curaduría y tips: Loco Tequila.",
        "source_url": SOURCE_URL,
        "source_api": API_URL,
        "arena_category": categoria,
        "elo_verified": True,
        "elo_disclaimer": "Elo y win rate obtenidos directamente de la API de Design Arena en la fecha indicada.",
        "anonymous_models_excluded": [] if incluir_anonimos else anonimos,
        "curated_fields": ["recommendation", "settings_tip", "loco_rating", "tags", "category", "badge"],
        "categories": categorias,
        "models": modelos,
    }
    LEADERBOARD_JSON.parent.mkdir(parents=True, exist_ok=True)
    with LEADERBOARD_JSON.open("w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write("\n")
    return doc


def sincronizar_app_js(doc):
    """Reescribe el bloque DEFAULT_LEADERBOARD de app.js para que el respaldo
    (usado cuando se abre index.html por file:// y fetch falla) no diverja del JSON."""
    if not APP_JS.exists():
        print("Aviso: no se encontró {}; no se sincronizó el respaldo.".format(APP_JS), file=sys.stderr)
        return False
    texto = APP_JS.read_text(encoding="utf-8")
    marcadores = re.compile(
        r"// ===== DEFAULT_LEADERBOARD:START =====.*?// ===== DEFAULT_LEADERBOARD:END =====",
        re.S,
    )
    bloque = (
        "// ===== DEFAULT_LEADERBOARD:START =====\n"
        "// Respaldo generado por sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py\n"
        "// No editar a mano: se regenera. Fecha del dataset: {}\n"
        "const DEFAULT_LEADERBOARD = {};\n"
        "// ===== DEFAULT_LEADERBOARD:END ====="
    ).format(doc["last_updated"], json.dumps(doc, ensure_ascii=False, indent=2))

    if not marcadores.search(texto):
        print(
            "Aviso: no se encontraron los marcadores DEFAULT_LEADERBOARD:START/END en app.js. "
            "Añádelos alrededor del const para habilitar la sincronización.",
            file=sys.stderr,
        )
        return False
    APP_JS.write_text(marcadores.sub(lambda _: bloque, texto, count=1), encoding="utf-8")
    return True


def advertir_mapa_obsoleto(total, sin_identificar):
    """El mapa FAMILIAS es un allowlist y envejece: cuando salen modelos nuevos
    caen en 'sin identificar' y se omitirían por error. Si la proporción es alta,
    el problema es el mapa, no que sean modelos en prueba ciega. Avisar explícitamente."""
    if not total or not sin_identificar:
        return
    proporcion = len(sin_identificar) / total
    if proporcion >= 0.4:
        print(
            "\n⚠  ADVERTENCIA: {} de {} modelos ({:.0%}) no casaron con ninguna familia conocida.\n"
            "   Una proporción tan alta suele significar que el mapa FAMILIAS de este script\n"
            "   quedó obsoleto, no que todos sean modelos en prueba ciega. Revisa la lista de\n"
            "   abajo: si reconoces proveedores públicos, agrégalos a FAMILIAS antes de confiar\n"
            "   en este ranking. Mientras tanto, usa --incluir-anonimos para verlos todos."
            .format(len(sin_identificar), total, proporcion),
            file=sys.stderr,
        )


def imprimir(modelos, anonimos, incluir_anonimos):
    print("\n{:<4} {:<32} {:<20} {:>6} {:>7} {:>10}".format(
        "#", "MODELO", "PROVEEDOR", "ELO", "WIN%", "BATALLAS"))
    print("-" * 84)
    for m in modelos:
        print("{:<4} {:<32} {:<20} {:>6} {:>6.1f}% {:>10,}".format(
            m["rank"], m["model_id"][:32], m["developer"][:20],
            m["elo_score"] if m["elo_score"] is not None else 0,
            m["win_rate"] or 0.0, m["battles"] or 0))
    sin_cur = [m["model_id"] for m in modelos if m["category"] == "Sin curaduría"]
    if sin_cur:
        print("\nSin curaduría de marca ({}): {}".format(len(sin_cur), ", ".join(sin_cur)))
    if anonimos:
        estado = "incluidos" if incluir_anonimos else "OMITIDOS"
        print("\nSin proveedor identificado — nombre clave en prueba ciega o familia no registrada, {} ({}):\n  {}".format(
            estado, len(anonimos), ", ".join(anonimos)))


def main():
    p = argparse.ArgumentParser(description="Leaderboard en vivo de generadores de imagen (Design Arena) + curaduría Loco Tequila.")
    p.add_argument("--categoria", default="image", choices=["image", "video"],
                   help="Arena a consultar (por defecto: image).")
    p.add_argument("--top", type=int, default=12, help="Cuántos modelos conservar (por defecto: 12).")
    p.add_argument("--incluir-anonimos", action="store_true",
                   help="Incluye los modelos con nombre clave (en prueba ciega, no usables por el público).")
    p.add_argument("--todas-las-versiones", action="store_true",
                   help="Lista todas las versiones de cada familia. Por defecto solo se conserva la mejor de cada una.")
    p.add_argument("--actualizar-showcase", action="store_true",
                   help="Reescribe showcase/data/leaderboard.json y sincroniza el respaldo de app.js.")
    p.add_argument("--json", metavar="ARCHIVO", help="Exporta el resultado a un archivo JSON aparte.")
    p.add_argument("--timeout", type=int, default=30, help="Timeout de la petición en segundos.")
    args = p.parse_args()

    datos = consultar_api(args.categoria, args.timeout)
    if not datos:
        sys.exit("La API no devolvió modelos para la categoría '{}'.".format(args.categoria))

    modelos, categorias, anonimos = construir(
        datos, cargar_curaduria(), args.top, args.incluir_anonimos, args.todas_las_versiones)
    if not modelos:
        sys.exit("Ningún modelo quedó tras el filtrado. Prueba con --incluir-anonimos.")

    print("Design Arena — arena '{}': {} modelos en el ranking, {} sin proveedor identificado.".format(
        args.categoria, len(datos), len(anonimos)))
    imprimir(modelos, anonimos, args.incluir_anonimos)
    advertir_mapa_obsoleto(len(datos), anonimos)

    if args.actualizar_showcase:
        doc = escribir_leaderboard_json(modelos, categorias, args.categoria, anonimos, args.incluir_anonimos)
        print("\nEscrito: {}".format(LEADERBOARD_JSON))
        if sincronizar_app_js(doc):
            print("Sincronizado el respaldo DEFAULT_LEADERBOARD en {}".format(APP_JS))
    elif args.json:
        doc = {
            "last_updated": date.today().isoformat(),
            "source_url": SOURCE_URL,
            "arena_category": args.categoria,
            "elo_verified": True,
            "categories": categorias,
            "models": modelos,
        }
        Path(args.json).write_text(
            json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nExportado: {}".format(args.json))


if __name__ == "__main__":
    main()
