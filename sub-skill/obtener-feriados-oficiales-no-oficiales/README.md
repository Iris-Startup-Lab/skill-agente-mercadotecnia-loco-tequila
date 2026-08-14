# Sub-skill: Obtener Feriados Oficiales y No Oficiales (México)

> **Propósito:** Detecta los días festivos oficiales y no oficiales de México para un año dado (o los que se aproximan en los próximos N días), combinando la librería `holidays` (oficiales) con el scrapeo del anexo de Wikipedia (no oficiales), filtrando tragedias. Úsala cuando la master skill de mercadotecnia de Loco Tequila necesite saber qué fechas festivas se aproximan para planear una campaña.

Detecta feriados de México para anclar las campañas de Loco Tequila a fechas festivas relevantes.

## Qué hace

- **Oficiales:** usa la librería `holidays` (`holidays.MX`) para el año solicitado.
- **No oficiales:** scrapea el anexo de Wikipedia "Anexo:Días festivos en México".
- **Filtra tragedias:** descarta sismos, colisiones, accidentes, masacres y conmemoraciones luctuosas (lista `NO_DESEADOS` + palabras clave en el script).
- **Deduplica:** prioriza la versión oficial cuando hay coincidencias de fecha/nombre.
- **Ventana de anticipación:** con `--dias N` muestra solo lo que se aproxima (por defecto usar `--dias 30` para el aviso de "un mes antes").

## Cómo ejecutar

El script corre en el ambiente Conda `skills_env`. Antes de ejecutar, activar Anaconda y el ambiente:

```powershell
& "E:\Users\1167486\AppData\Local\anaconda3\Scripts\conda.exe" shell.powershell hook | Out-String | Invoke-Expression
conda activate skills_env
```

Luego ejecutar el script:

```powershell
python obtener_feriados.py --year 2026 --dias 30 --json feriados_2026.json
```

- `--year` (opcional): año a consultar. Por defecto, el año actual. Extrapolable a cualquier año.
- `--dias N` (opcional): muestra solo feriados dentro de los próximos N días. Usar `--dias 30` para el aviso de un mes de anticipación. Si se omite, lista el año completo.
- `--json ARCHIVO` (opcional): guarda la salida en JSON (lista de `{fecha, nombre, tipo}`).

## Dependencias

`holidays`, `requests`, `beautifulsoup4`. Si faltan en `skills_env`:

```powershell
conda activate skills_env
pip install holidays requests beautifulsoup4
```

## Notas

- Si el scrapeo de Wikipedia falla (sin red o la página cambió), el script igual devuelve los feriados **oficiales** e imprime un `[aviso]`. Combinar con `references/fechas-alcohol.md` para las fechas del mundo de las bebidas.
- No inventar fechas: si un feriado no aparece en la salida del script ni en `references/fechas-alcohol.md`, marcarlo `[no disponible]` o pedir confirmación.
