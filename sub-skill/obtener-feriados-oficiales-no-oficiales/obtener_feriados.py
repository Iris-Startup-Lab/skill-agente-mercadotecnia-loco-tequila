# -*- coding: utf-8 -*-
"""Obtener feriados oficiales y no oficiales de México.

Genera un listado de días festivos de México para un año dado:
  - Oficiales: usando la librería `holidays` (holidays.MX).
  - No oficiales: scrapeando el anexo de Wikipedia "Anexo:Días festivos en México".

Uso:
    python obtener_feriados.py [--year 2026] [--dias 30] [--json feriados.json]

Opciones:
    --year AÑO      Año a consultar (por defecto el año actual).
    --dias N        Mostrar solo los feriados dentro de los próximos N días
                    desde hoy (útil para avisar con anticipación, p. ej. 30).
    --json ARCHIVO  Guardar también la salida en formato JSON.
"""

import argparse
import json
import re
import sys
from datetime import date, timedelta

import holidays
import requests
from bs4 import BeautifulSoup

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKIPEDIA_URL = "https://es.wikipedia.org/wiki/Anexo:D%C3%ADas_festivos_en_M%C3%A9xico"

SPANISH_MONTHS = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10,
    "noviembre": 11, "diciembre": 12,
}

# Nombres exactos a descartar (tragedias / fechas no celebrables).
NO_DESEADOS = [
    "Conmemoración de los sismos de1985,2017y2022",
    "Colisión de trenes en Indios Verdes",
    "Conmemoración de laMasacre de Tlatelolco",
    "Colisión de trenes en el Metro de la Ciudad de México de 1975",
    "En conmemoración del",
    "Del 16 al",
    "Conmemoración delEl Halconazo",
    "Accidente del Metro de la Ciudad de México de 2021",
    "Conmemoración de laMasacre en La Alameda",
    "Gesta Heroica delBatallón de San Patricioen la...",
    "Conmemoración de la gesta heroica del Batallón...",
]

# Palabras clave que indican una fecha no celebrable (tragedias).
TRAGEDIA_KEYWORDS = [
    "sismo", "terremoto", "colisión", "accidente", "masacre", "halconazo",
    "explosión", "incendio", "hundimiento", "derrumbe", "epidemia",
    "batallón de san patricio", "gesta heroica del batallón",
]


def get_official_holidays(year: int) -> list:
    """Devuelve [(date, nombre, 'Oficial')] de México para el año dado."""
    mx = holidays.MX(years=[year])
    return [(d, name, "Oficial") for d, name in sorted(mx.items())]


def is_tragedy(name: str) -> bool:
    """Determina si un nombre corresponde a una tragedia / fecha no celebrable."""
    if name in NO_DESEADOS:
        return True
    lowered = name.lower()
    return any(kw in lowered for kw in TRAGEDIA_KEYWORDS)


def clean_name(raw_name: str) -> str:
    """Limpia un nombre de festivo: quita notas [1], años entre paréntesis y textos residuales."""
    # Eliminar notas al pie de Wikipedia tipo [1], [ 6 ], etc.
    name = re.sub(r"\[\s*\d+\s*\]", "", raw_name)
    # Quitar paréntesis envolventes si todo el texto está entre paréntesis
    name = name.strip()
    if name.startswith("(") and name.endswith(")"):
        name = name[1:-1].strip()
    # Quitar años entre paréntesis tipo (2024)
    name = re.sub(r"\s*\(\d{4}\)", "", name)
    # Quitar paréntesis adicionales solo si no vacían el nombre
    if "(" in name and not name.startswith("("):
        prefix = name.split("(", 1)[0].strip()
        if prefix:
            name = prefix
    # Quitar punto final si existe
    name = name.rstrip(".")
    name = re.sub(r"\s+", " ", name)
    return name.strip()


def scrape_unofficial_holidays(year: int) -> list:
    """Scrapea Wikipedia y devuelve [(date, nombre, 'No oficial')]."""
    unofficial = []
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }
    try:
        response = requests.get(WIKIPEDIA_URL, headers=headers, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        print(f"[aviso] No se pudo scrapear Wikipedia: {exc}", flush=True)
        return unofficial

    soup = BeautifulSoup(response.text, "html.parser")

    # Detenerse antes de secciones luctuosas / lutos nacionales para evitar tragedias
    luto_header = soup.find(
        lambda tag: tag.name in ["h2", "h3"]
        and any(k in tag.get_text().lower() for k in ["luto", "luctuos", "tragedia"])
    )

    tables = []
    for el in soup.find_all(["table", "h2", "h3"]):
        if luto_header and el == luto_header:
            break
        if el.name == "table" and "wikitable" in el.get("class", []):
            tables.append(el)

    date_pattern = re.compile(r"(\d{1,2})\s+de\s+([a-záéíóúüñ]+)", re.IGNORECASE)

    for table in tables:
        for row in table.find_all("tr"):
            cols = row.find_all(["th", "td"])
            col_texts = [ele.get_text(separator=" ", strip=True) for ele in cols]

            for i, text in enumerate(col_texts):
                match = date_pattern.search(text)
                if not match:
                    continue
                day = int(match.group(1))
                month_name = match.group(2).lower()
                month = SPANISH_MONTHS.get(month_name)
                if not day or not month:
                    continue
                try:
                    hol_date = date(year, month, day)
                except ValueError:
                    continue

                candidate_name = ""
                if i + 1 < len(col_texts) and col_texts[i + 1]:
                    candidate_name = col_texts[i + 1]
                else:
                    candidate_name = text.replace(match.group(0), "").strip()

                name = clean_name(candidate_name)
                if not name or is_tragedy(name):
                    continue
                # Si el nombre empieza con conectores de narrativa tipo 'El de...', omitir
                if re.match(r"^(el|en el|del)\s+de\s+\d{4}", name, re.IGNORECASE):
                    continue
                if name.lower().startswith("en conmemoración del"):
                    continue
                unofficial.append((hol_date, name, "No oficial"))
                break

    return unofficial


def normalize(name: str) -> str:
    """Normaliza un nombre para deduplicar aproximados."""
    n = name.lower()
    n = re.sub(r"\[\s*\d+\s*\]", "", n)
    n = re.sub(r"\s*\(\d{4}\)", "", n)
    # Homogeneizar variaciones comunes
    n = re.sub(r"\btrabajador(es)?\b", "trabajo", n)
    n = re.sub(r"\breyes magos\b", "reyes", n)
    n = re.sub(
        r"\b(día|días|aniversario|natalicio|conmemoración|festividad|de|la|el|los|las|y|del|méxico)\b",
        "",
        n,
    )
    n = re.sub(r"[^\wáéíóúüñ ]", "", n)
    return " ".join(sorted(set(n.split()))).strip()


def combine(official: list, unofficial: list) -> list:
    """Combina oficiales y no oficiales, deduplicando por fecha + nombre normalizado."""
    combined = list(official)
    seen = {(d, normalize(n)) for d, n, _ in official}
    for d, n, _ in unofficial:
        norm = normalize(n)
        key = (d, norm)
        # Si la clave ya está registrada o está vacía tras normalizar en la misma fecha
        if key not in seen and norm:
            combined.append((d, n, "No oficial"))
            seen.add(key)
    combined.sort(key=lambda x: (x[0], 0 if x[2] == "Oficial" else 1, x[1]))
    return combined


def main():
    parser = argparse.ArgumentParser(description="Feriados oficiales y no oficiales de México.")
    parser.add_argument("--year", type=int, default=date.today().year, help="Año a consultar.")
    parser.add_argument("--dias", type=int, default=None,
                        help="Mostrar solo feriados dentro de los próximos N días.")
    parser.add_argument("--json", dest="json_path", default=None,
                        help="Guardar la salida en un archivo JSON.")
    args = parser.parse_args()

    official = get_official_holidays(args.year)
    unofficial = scrape_unofficial_holidays(args.year)
    combined = combine(official, unofficial)

    if args.dias is not None:
        today = date.today()
        horizon = today + timedelta(days=args.dias)
        combined = [
            (d, n, t) for d, n, t in combined
            if today <= d <= horizon
        ]

    records = [
        {"fecha": d.isoformat(), "nombre": n, "tipo": t}
        for d, n, t in combined
    ]

    if args.json_path:
        with open(args.json_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
        print(f"[ok] JSON guardado en {args.json_path}", flush=True)

    print(f"--- Feriados {'próximos (' + str(args.dias) + ' días)' if args.dias is not None else 'del año ' + str(args.year)} ---")
    for d, n, t in combined:
        print(f"{d.isoformat()}: {n} ({t})")


if __name__ == "__main__":
    main()
