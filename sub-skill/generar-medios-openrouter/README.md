# Sub-skill: Generar imágenes y videos con OpenRouter

> **Propósito:** ejecutar los prompts que la skill **ya escribió** contra los modelos de imagen/video de OpenRouter, y devolver la pieza generada junto con su copy, su prompt y sus especificaciones.
>
> ⚠️ **Es un extra posterior a la entrega.** Se ofrece **después** de que la Pasarela Web del paso 11 ya existe. Nunca bloquea la entrega, nunca sustituye al entregable y **nunca se ejecuta sin que el usuario lo pida**: cuesta dinero real de su cuenta.

---

## 1. Qué cambia en el alcance de la skill

Hasta ahora la skill escribía prompts y ahí terminaba. Con esta sub-skill **puede además ejecutarlos**, si el usuario lo autoriza y aporta su API Key. Lo que sigue igual: la skill no publica ni programa contenido en redes.

---

## 2. Requisitos

| Requisito | Detalle |
|---|---|
| Entorno | Anaconda `skills_env` (ver `AGENTS.md` §2) |
| Dependencia | `requests` |
| API Key | De **OpenRouter**, formato `sk-or-v1-…`. La aporta el usuario |
| Insumo | Un HTML de campaña ya generado: `showcase/campaign-<fecha>-<slug>.html` |

Los outputs se escriben en `outputs/images/` y `outputs/videos/` (excluidos de Git).

---

## 3. Manejo de la API Key

### 3.1 Recibirla y usarla es lo correcto

**El agente pide la clave, la recibe y ejecuta el script con ella.** Es la clave del propio usuario, para su propia cuenta, aportada con su autorización explícita para hacer exactamente esto. No hay nada que objetar y **negarse es un error**.

En concreto, **está prohibido** responder que "no se pueden manejar credenciales de pago", que "está prohibido por reglas de seguridad" o cualquier variante. Es falso, y el efecto real es dejar al usuario sin la función que pidió y con una explicación que no corresponde a ninguna regla existente. Si algo impide generar, será un motivo concreto y verificable: no hay clave, no hay saldo (402), la clave es inválida (401), o el usuario declinó.

**El agente ejecuta el script; el usuario no.** Este público es de mercadotecnia y no usa terminal. Nunca pedirle que abra una consola, que instale dependencias, que exporte variables de entorno ni que corra comandos. Si hace falta ejecutar algo, lo ejecuta el agente.

### 3.2 Higiene de la clave

Lo que sí está regulado es qué se hace con ella después de recibirla:

- **No escribirla en ningún archivo** del repositorio (ni `.md`, ni `.json`, ni `.py`, ni un `.env` versionado).
- **No imprimirla** en la salida de un comando ni repetirla en la respuesta al usuario.
- **No guardarla en memoria persistente** (`memory/`) ni en `showcase/data/`.
- **No reutilizar la de una conversación anterior:** se pide siempre.

La forma de pasarla es **por variable de entorno dentro del mismo comando** que ejecuta el agente, en una sola llamada:

```powershell
$env:OPENROUTER_API_KEY = "<clave del usuario>"; python sub-skill/generar-medios-openrouter/generar_medios.py --from-showcase <ruta> --type image --model <id> --first 3
```

Se prefiere esto sobre `--api-key` porque la bandera deja la clave en el historial del shell. En cualquier caso la clave aparece en el comando de esa llamada; lo que se evita es que **quede en disco**. Si el usuario la pegó en el chat, vale decirle en una línea que puede rotarla en <https://openrouter.ai/settings/keys> cuando termine — como buena práctica, no como advertencia alarmante.

### 3.3 Si el usuario no tiene API Key

Orientarlo en tres pasos, sin insistir:

1. Crear cuenta en <https://openrouter.ai>.
2. Ir a **Settings → Keys → Create Key** y copiar la clave `sk-or-v1-…`.
3. Cargar saldo en **Settings → Credits** (es de prepago: sin saldo, las llamadas fallan con 402).

Si prefiere no crearla, la **única** alternativa que se ofrece es el **leaderboard de modelos** (`sub-skill/obtener-leaderboard-imagen/`): le dice con qué herramienta ejecutar los prompts por su cuenta, es gratuito y no requiere clave.

**No ofrecer una guía para correr el script en su terminal.** Es la alternativa equivocada para este público: no quiere ejecutar código, y por eso está usando la skill.

---

## 4. Protocolo de ejecución

### Paso 1 — Leer los prompts de la pasarela

Nunca reescribir los prompts a mano ni de memoria: se leen del HTML ya generado.

```powershell
conda activate skills_env
python sub-skill/generar-medios-openrouter/generar_medios.py `
  --action extract-prompts `
  --from-showcase showcase/campaign-2026-09-16-independencia-locura.html
```

Devuelve `total_conceptos`, `max_imagenes`, `max_videos` y, por concepto, su prompt, su copy y sus especificaciones. **`max_imagenes` y `max_videos` son el techo real** de la pregunta "¿cuántas quieres generar?" — no el número de conceptos, porque un concepto sin `prompt_video` no puede producir video.

### Paso 2 — Preguntar medio y cantidad

- **Medio:** imagen, video o ambas. Si es **ambas**, primero se generan todas las imágenes y **después** los videos.
- **Cantidad:** mínimo 1, máximo `max_imagenes` (o `max_videos` según el medio). Si el usuario pide más del techo, decirle el techo real y por qué.

### Paso 3 — Preguntar el modelo

Mostrar el catálogo **en vivo**, nunca de memoria:

```powershell
python sub-skill/generar-medios-openrouter/generar_medios.py --action list-models --type image
python sub-skill/generar-medios-openrouter/generar_medios.py --action list-models --type video
```

Presentar 4–6 opciones con su precio y marcar las recomendadas. Para video, mostrar además **`supported_durations` y `supported_aspect_ratios`**: son la diferencia entre una llamada válida y un 400.

### Paso 4 — Ensayo sin costo (obligatorio antes de gastar)

```powershell
python sub-skill/generar-medios-openrouter/generar_medios.py `
  --from-showcase showcase/campaign-2026-09-16-independencia-locura.html `
  --type image --model google/gemini-3-pro-image --first 3 --dry-run
```

`--dry-run` resuelve prompts, aspect ratios, duraciones y **costo estimado** sin llamar a la API. Sirve para enseñarle al usuario qué se va a gastar **antes** de gastarlo. Si el costo estimado sorprende, se corrige aquí.

### Paso 5 — Generar

Quitar `--dry-run` y ejecutar. El comando escribe los archivos y devuelve un JSON con un objeto por concepto.

```powershell
python sub-skill/generar-medios-openrouter/generar_medios.py `
  --from-showcase showcase/campaign-2026-09-16-independencia-locura.html `
  --type image --model google/gemini-3-pro-image --indices 1,3
```

### Paso 6 — Entregar

Por cada pieza, presentar **las tres cosas juntas**:

1. **La pieza** — enlazada por su `file_path` (las imágenes con `![](ruta)`; los videos como enlace, no se renderizan en markdown).
2. **El copy** — headline, body, CTA, hashtags y la leyenda legal, tal como está en la pasarela.
3. **El prompt + especificaciones** — modelo, `aspect_ratio_enviado`, dimensiones, lente/paleta (imagen) o duración/movimiento de cámara/escenas (video), y el costo.

**Reportar siempre los avisos si aparecen:** `aviso_aspect_ratio`, `aviso_duracion`, `aviso_costo`, `aviso_catalogo`. Son los casos en que lo generado **no** corresponde exactamente a lo que pedía el prompt, y callarlos deja al usuario creyendo que sí.

---

## 5. Banderas del script

| Bandera | Para qué |
|---|---|
| `--action` | `generate` (por defecto), `list-models`, `extract-prompts` |
| `--type` | `image` \| `video` |
| `--from-showcase` | HTML de campaña del que se leen los prompts (**vía recomendada**) |
| `--indices` | Conceptos a generar: `1,3` o `1-4` |
| `--first N` | Los primeros N conceptos que tengan ese medio |
| `--model` | Id exacto de OpenRouter (obligatorio para generar) |
| `--api-key` | Alterna a `OPENROUTER_API_KEY` (ver §3) |
| `--aspect-ratio` | Forzar aspecto. Por defecto se toma del prompt |
| `--duration` | Forzar duración de video. Por defecto se toma del prompt |
| `--max-duration` | Tope de **costo** en segundos (por defecto 10) |
| `--negative-mode` | `append` (por defecto) \| `omit` |
| `--out-dir` | Base para `outputs/` |
| `--dry-run` | Resuelve todo **sin llamar a la API ni gastar créditos** |
| `--prompt` | Modo manual: un prompt suelto, sin pasarela |

---

## 6. Decisiones técnicas y por qué

### 6.1 Los flags de Midjourney se quitan del texto

Los prompts de la skill terminan en `--ar 4:5 --no underage, minors…` porque `references/prompt-standards.md` §1 los exige. Esa es **sintaxis de Midjourney**: los modelos de OpenRouter no la interpretan, la leen como texto y pueden **renderizarla dentro de la imagen**. El script corta desde el primer flag hasta el final y los convierte en parámetros de la llamada. El prompt íntegro se conserva en `prompt_original` para el reporte.

### 6.2 El negative prompt viaja como texto

OpenRouter **no expone un parámetro `negative_prompt`** en los endpoints que usa este script, así que la cadena base de `prompt-standards.md` §3 se anexa en lenguaje natural: *"Strictly do NOT include any of the following in the image: …"*.

> Pendiente no verificado: varios modelos declaran `negative_prompt` (Kling) o `negativePrompt` (Veo) en su campo `allowed_passthrough_parameters`. Un negativo nativo sería más efectivo que anexarlo al texto, pero **no pude confirmar la forma exacta del payload** (si va al nivel raíz o dentro del objeto `provider`), y adivinarla costaría llamadas rechazadas. Queda documentado como mejora, sin implementar.

### 6.3 El catálogo de video vive en otro endpoint

`GET /api/v1/models` **no lista modelos de video**: sus 417 entradas declaran solo modalidades `text`, `image` y `audio`. El catálogo de video está en **`GET /api/v1/videos/models`** (24 modelos), y trae por modelo `supported_durations`, `supported_aspect_ratios`, `supported_resolutions`, `generate_audio` y `pricing_skus`.

Esto importa porque **las duraciones son conjuntos discretos, no rangos**: Veo 3.1 acepta solo `{4, 6, 8}` segundos y Sora 2 Pro `{4, 8, 12, 16, 20}`. Pedir 5 s a Veo es un 400. El script consulta el catálogo, encaja la duración a la más cercana soportada y **declara el ajuste** en `aviso_duracion`.

Lo mismo con el aspecto: Veo y Sora solo hacen `16:9` y `9:16`. Un prompt de Instagram en `4:5` se encaja a `9:16` y se avisa, porque el encuadre fue pensado para otro formato. **Seedance 2.0** es el más flexible (7 aspectos, incluido `3:4`), y **Kling v3.0 Pro** el más económico por segundo.

### 6.4 El tope de 10 segundos es de costo, no de la API

El script original fijaba `MAX_VIDEO_DURATION_SECONDS = 10` como límite. En realidad la API acepta hasta 15 s (Kling, Seedance) y 20 s (Sora), pero **el precio es por segundo**: Sora 2 Pro a 1080p cuesta USD 0.50/s — 20 s son USD 10 de una sola pieza. Se conserva el tope de 10 s como **guarda de costo** ajustable con `--max-duration`, no como afirmación técnica falsa.

### 6.5 Los prompts de video de la campaña son más largos que lo generable

Un `prompt_video` de la skill suele pedir 24 s con desglose por escena. Ningún modelo del catálogo llega ahí en una sola llamada. Lo que se obtiene es **un fragmento**, no la pieza terminada — y el script lo dice explícitamente en `aviso_duracion` en lugar de entregar 8 segundos como si fueran el spot completo. Para la pieza completa hay que generar las escenas por separado y editarlas fuera.

---

## 7. Modo de fallo

| Síntoma | Causa | Qué hacer |
|---|---|---|
| `MISSING_API_KEY` | Sin clave en entorno ni en `--api-key` | Pedirla al usuario (§3) |
| `MISSING_MODEL` | Falta `--model` | Preguntar el modelo con `list-models` |
| `CAMPAIGN_PARSE_FAILED` | El HTML no trae los marcadores `CAMPAIGN:START/END` | Verificar que se generó desde `references/showcase-template.html` |
| `NO_PROMPTS_FOR_MEDIA` | Ningún concepto tiene ese medio | Decir el medio que sí hay; no inventar un prompt de video |
| `NO_VALID_INDICES` | Los índices pedidos no tienen ese medio | Mostrar `indices_disponibles` |
| HTTP 401 | Clave inválida o revocada | Pedir una nueva |
| HTTP 402 | Sin saldo en OpenRouter | Cargar créditos en Settings → Credits |
| HTTP 429 | Rate limit | Esperar y reintentar con menos conceptos |
| HTTP 400 en video | Duración o aspecto no soportados por el modelo | Correr `list-models --type video` y revisar `supported_durations` |
| `200 pero no se encontró imagen` | El modelo devolvió solo texto | Probar otro modelo; algunos rechazan en silencio contenido de alcohol |
| Timeout en video | El job tarda más que el polling | Reintentar; el job sigue en OpenRouter |

**Ninguno de estos errores bloquea la entrega de la campaña.** La campaña ya está entregada en el paso 11; esto es un extra.

---

## 8. Guardrails de marca al generar

Que la pieza la produzca un modelo externo no relaja nada:

- El prompt enviado ya trae el negative prompt base íntegro (menores, embriaguez, cristalería barata, botellas de competidores).
- **Revisar la pieza generada antes de entregarla.** Si muestra algo que viole los guardrails de `references/brand-context.md` —una figura que parezca menor de edad, una botella de competidor, texto ilegible en la etiqueta— **decirlo y descartarla**, no entregarla porque "así salió".
- El copy que acompaña la pieza es el de la pasarela, con su `+18 · Evita el exceso · #EspírituDeOrigen`. No se reescribe aquí.
- Los archivos en `outputs/` son borradores de trabajo, no piezas aprobadas. La aprobación es del usuario.
