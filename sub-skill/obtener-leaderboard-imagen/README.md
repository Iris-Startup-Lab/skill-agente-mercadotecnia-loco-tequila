# Sub-skill — Obtener leaderboard de generadores de imagen y video

Consulta **en vivo** el ranking de modelos generativos de [Design Arena](https://www.designarena.ai/leaderboard/image) y lo cruza con la curaduría propia de Loco Tequila para responder una pregunta concreta: **¿con qué herramienta conviene ejecutar los prompts que la skill acaba de escribir?**

Es un **extra opcional**. No forma parte del entregable de campaña y **nunca debe bloquear la entrega**: si la API falla, se informa y se continúa.

---

## 1. Por qué existe este script

La página del leaderboard es una aplicación Next.js que **renderiza la tabla en el cliente**. Una petición HTTP normal devuelve el cascarón sin datos, así que ni scrapear el HTML ni usar WebFetch sirven — WebFetch además convierte a markdown y descarta los `<script>`.

Los datos viven en un endpoint que el bundle del sitio consume:

```http
POST https://www.designarena.ai/api/leaderboard
Content-Type: application/json

{"arenaType": "models", "category": "image", "variationName": "public"}
```

De ahí salen `elo`, `winRate`, `wins`/`losses`/`battles` y `avgGenerationTimeMs` **reales y verificables**. `category` acepta `image` y `video`; otros valores devuelven HTTP 400.

> **Regla de datos:** las posiciones y los Elo **jamás** se escriben de memoria — serían cifras inventadas, justo lo que prohíbe [SKILL.md](../../SKILL.md). O se obtienen con este script, o se marcan `[REFERENCIA DE INDUSTRIA]` con `*`.

## 2. Entorno

Igual que el resto del repositorio: Anaconda con el entorno `skills_env`.

```powershell
& "E:\Users\1167486\AppData\Local\anaconda3\Scripts\conda.exe" shell.powershell hook | Out-String | Invoke-Expression
conda activate skills_env
```

Única dependencia: `requests` (ya incluida en el entorno).

## 3. Uso

```powershell
# Top 12 de imagen, solo a pantalla
python sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py

# Ranking de video (para prompts de video)
python sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py --categoria video

# Actualizar la pasarela persistente (showcase/data/leaderboard.json + respaldo en app.js)
python sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py --top 10 --actualizar-showcase

# Exportar a un archivo aparte sin tocar el showcase
python sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py --json ranking.json
```

| Flag | Por defecto | Qué hace |
|---|---|---|
| `--categoria image\|video` | `image` | Arena a consultar. `video` sirve cuando `{{medio}}` incluye video. |
| `--top N` | `12` | Cuántos modelos conservar tras el filtrado. |
| `--incluir-anonimos` | desactivado | Incluye los modelos con nombre clave (ver §4). |
| `--todas-las-versiones` | desactivado | Lista todas las versiones de cada familia en vez de solo la mejor. |
| `--actualizar-showcase` | desactivado | Reescribe `showcase/data/leaderboard.json` y sincroniza el respaldo `DEFAULT_LEADERBOARD` de `app.js`. |
| `--json ARCHIVO` | — | Exporta a un JSON aparte sin tocar el showcase. |
| `--timeout N` | `30` | Timeout de la petición, en segundos. |

## 4. Dos filtros que importan

**a) Modelos en prueba ciega, omitidos por defecto.** Buena parte del top del ranking son nombres clave (`babylon`, `chestnut`, `mantis`, `aurora`, `magnolia`, `fennel`, `juniper`, `thistle`, `apple`, `carillon_2`…): modelos anónimos en evaluación, **no disponibles al público**. Recomendarlos a un equipo de marketing sería inútil. El script los detecta por no pertenecer a ninguna familia de proveedor conocida (lista `FAMILIAS` en el script), los omite, y **los reporta explícitamente** — nunca los descarta en silencio. Con `--incluir-anonimos` se conservan.

**b) Una sola versión por familia.** El ranking crudo puede traer cinco variantes de Gemini seguidas, lo que no aporta a quien solo quiere saber qué herramienta usar. Por defecto se conserva la mejor versión de cada familia. Con `--todas-las-versiones` se ven todas.

## 5. Dónde vive la curaduría

El script **no inventa recomendaciones**. Cruza los datos de la API con [`references/curaduria-modelos-imagen.json`](../../references/curaduria-modelos-imagen.json), indexado por **familia** de modelo (`flux`, `gpt-image`, `imagen`, `ideogram`, `recraft`…) y no por versión exacta, para que la curaduría **sobreviva al cambio constante de versiones** en el ranking.

| Campo | Origen |
|---|---|
| `elo_score`, `win_rate`, `battles`, `avg_generation_ms` | API de Design Arena — verificable |
| `recommendation`, `settings_tip`, `loco_rating`, `tags`, `category`, `badge` | Curaduría propia de Loco Tequila |
| `developer` | Curaduría, con respaldo en `DEV_FALLBACK` |

Si aparece una familia nueva en el top sin curaduría, el script la incluye marcando `"Sin curaduría"` y avisando en pantalla — señal de que toca añadirla al JSON de curaduría.

## 6. Salida

Con `--actualizar-showcase` reescribe `showcase/data/leaderboard.json` con `last_updated` en la fecha real de consulta, `elo_verified: true` y la lista de modelos anónimos excluidos. La pasarela [`showcase/index.html`](../../showcase/index.html) lo consume sola y muestra el disclaimer de datos al pie del leaderboard.

También sincroniza el bloque `DEFAULT_LEADERBOARD` de `app.js` entre los marcadores `// ===== DEFAULT_LEADERBOARD:START/END =====`. Ese bloque es el respaldo que se usa cuando `index.html` se abre por `file://` y `fetch()` falla por CORS; sincronizarlo evita que los dos datasets diverjan.

## 7. Si algo falla

| Situación | Qué hace el script | Qué debe hacer el agente |
|---|---|---|
| Sin red o timeout | Sale con mensaje de error | Informar y **continuar**; el leaderboard es opcional |
| HTTP 400 | Reporta la categoría inválida | Usar solo `image` o `video` |
| `rate_limit_exceeded` | Sale avisando del límite | Reintentar más tarde, no en bucle |
| Cambió el contrato de la API | Sale avisando que la respuesta no es JSON o `success=false` | Revisar el endpoint en el bundle del sitio; no inventar cifras |

En ningún caso se rellena el ranking de memoria.

## 8. Limitación conocida

Las subcategorías del sitio (**Product**, **Marketing**, Portrait, Typography, Landscape, Abstract, Architecture, Cartoon) **no son alcanzables** por este endpoint: se probaron como `category` (HTTP 400) y como `variationName` (respuesta vacía). Parecen un filtro de cliente. Para esta marca las relevantes serían Product y Marketing; mientras no haya forma de consultarlas, se usa el ranking global de la arena, que es suficiente para el propósito del extra.
