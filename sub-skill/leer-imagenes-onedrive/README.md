# Sub-skill: Lectura de piezas previas en OneDrive / SharePoint

> **Propósito:** revisar las piezas publicitarias anteriores de una carpeta de OneDrive/SharePoint para **mantener coherencia visual sin repetir diseños**.
>
> ✅ **Vía principal — documentos Word de análisis.** Un flujo de **Power Automate** analiza cada imagen y deposita en la misma carpeta un `.docx` con su ficha visual y su prompt de recreación. El conector de Microsoft 365 **sí lee Word**, así que el análisis visual completo llega al agente sin tocar el binario de la imagen. El prompt que alimenta ese flujo vive en [`references/ingenieria-inversa-imagen.md`](../../references/ingenieria-inversa-imagen.md).
>
> ⚠️ **Limitación que esto resuelve:** el conector **no** puede extraer mapas de bits de imágenes (`.jpg`, `.png`, `.webp`) por cómo Microsoft Graph API convierte el stream a texto. Los Word son el puente.

---

## Requisito previo

Plugin **Microsoft 365** (MCP) activo, con `sharepoint_folder_search` y `read_resource`.

---

## Protocolo de ejecución

### Paso 1 — PEDIR EL LINK DE LA CARPETA (obligatorio)

**No existe una carpeta fija.** Cambia según la campaña, el producto o la red. El agente **DEBE PEDIRLA SIEMPRE** al usuario y **nunca**:

- asumir una ruta o un nombre de carpeta,
- reutilizar la carpeta de una conversación anterior,
- deducirla del nombre del producto o de la campaña,
- ni buscar "la carpeta de Loco Tequila" a ciegas con `sharepoint_folder_search`.

Preguntar adelantando ya las opciones de alcance, para que el usuario pueda responder todo de una vez:

> *"¿Me pegas el link de la carpeta de OneDrive/SharePoint con las piezas previas? Y dime también si tomo en cuenta las **10 más recientes** o **desde qué fecha** hasta hoy. Si no aplica para esta campaña, dímelo y la omito."*

Tres respuestas posibles, todas válidas:

| Respuesta del usuario | Qué hacer |
|---|---|
| Link + alcance | Continuar al Paso 2 |
| Solo el link | Preguntar el alcance antes de leer |
| "No aplica" / declina | **Omitir la auditoría y avanzar.** No insistir |

### Paso 1b — Alcance de la revisión

| Modo | Cuándo conviene |
|---|---|
| **10 más recientes** | Revisión rápida, carpeta con historial largo |
| **Rango de fechas** | Acotar a una temporada o campaña concreta (p. ej. "desde el 1 de julio") |

El filtro se resuelve **con el timestamp del nombre de archivo** (ver Paso 3), sin abrir ningún documento.

### Paso 2 — Localizar la carpeta

1. Extraer el nombre de carpeta del URL (la porción tras el último `/` antes de los parámetros `?`). Decodificar caracteres especiales (`%20` = espacio).
2. `Microsoft 365:sharepoint_folder_search` con ese nombre.

### Paso 3 — Triage por nombre de archivo (solo para decidir CUÁLES abrir)

> ⚠️ **El triage no sustituye la lectura.** Este paso solo sirve para elegir qué documentos abrir en el Paso 4. **El contenido del documento SIEMPRE se lee.** El nombre de archivo aporta plataforma y fecha, nada más — no describe la pieza.

`Microsoft 365:read_resource` con el `uri` de la carpeta para listar los elementos, y filtrar `.docx`.

La convención de nombres del flujo de Power Automate es:

```text
facebook_loco_tequila_1.jpg_2026-08-18T21_51_46.8629908Z.docx
└plataforma┘└───pieza───┘└ext┘└───── timestamp ISO ─────┘
```

- **plataforma** — `facebook`, `instagram`, `tiktok`, `linkedin`, `youtube`.
- **pieza** — nombre del archivo original, con su número de secuencia. La secuencia es **por plataforma**, no global: `facebook_loco_tequila_1` e `instagram_loco_tequila_1` son piezas distintas.
- **ext** — formato de la imagen original (`.jpg`, `.png`, `.webp`).
- **timestamp** — ISO 8601 con los `:` sustituidos por `_` (restricción de nombres de Windows). `2026-08-18T21_51_46` = *2026-08-18 21:51:46*.

De ahí se obtienen, **sin gastar una sola lectura**: plataforma, pieza, formato y fecha exacta. Con eso:

1. Ordenar por timestamp descendente.
2. Aplicar el alcance del Paso 1 — los 10 primeros, o los que caigan en el rango de fechas.
3. Agrupar por plataforma al reportar, para que se vea la cobertura por red.

Si un nombre no sigue la convención, no descartarlo: abrirlo y usar su contenido, reportando que su fecha no pudo deducirse del nombre.

### Paso 4 — Leer el CONTENIDO de cada documento (obligatorio)

`read_resource` sobre **cada** `.docx` elegido, para extraer el **texto completo del cuerpo**, no solo sus propiedades. Cada documento sigue la estructura de `references/ingenieria-inversa-imagen.md`, con encabezados numerados del 1 al 7.

**Verificación de lectura efectiva.** Antes de usar un documento, confirmar que la respuesta trae el cuerpo del texto: debe reconocerse al menos el encabezado **§3 (ADN vs INCIDENTAL)**, que es el que sostiene todo el reparto. Según lo que devuelva:

| Resultado de `read_resource` | Qué hacer |
|---|---|
| Texto completo con los encabezados 1–7 | Continuar al Paso 5 con normalidad |
| Texto parcial o sin los encabezados esperados | Usar solo las secciones que sí se leyeron y **declararlo** en las notas de la entrega |
| Solo propiedades/metadatos, sin cuerpo | **Decirlo explícitamente al usuario.** Tratar el documento como no leído |
| Error de lectura | Reportar el archivo que falló y continuar con los demás |

**Prohibición crítica — no inferir el contenido desde el nombre.** El nombre de archivo incluye el nombre de la imagen original, que suele ser descriptivo, y eso hace muy fácil fabricar un análisis plausible sin haber abierto nada. Si un documento no se pudo leer, **su ADN e INCIDENTAL no existen para esta campaña**: no se deducen, no se estiman y no se rellenan por analogía con otros documentos. Se reporta como no leído y se sigue adelante.

### Paso 5 — Reparto: qué se hereda y qué se excluye

Este es el punto del sub-skill. Cada sección del Word tiene un uso **distinto y no intercambiable**:

| Sección del Word | Uso | Regla |
|---|---|---|
| **§1 Ficha visual** | Heredar | Parámetros técnicos que ya funcionaron: óptica, esquema de luz, paleta con HEX |
| **§2 Layout y texto** | Contexto | Composición y espacio para titular. No entra a los prompts nuevos |
| **§3 ADN** | **Heredar** | Es la coherencia de marca: luz, paleta, tratamiento del material. Los prompts nuevos deben compartirlo |
| **§3 INCIDENTAL** | **EXCLUIR** | Ya se usó. El objeto de apoyo, el fondo concreto y el ángulo específico **no se repiten** en la campaña nueva |
| **§4 Prompt maestro** | Solo contexto | **Prohibido reutilizar su texto, entero o por fragmentos.** Sirve para saber qué ya se dijo, no como material |
| **§5 Negative prompt** | Heredar | La cadena base es la misma de `references/prompt-standards.md` §3 |
| **§6 Variantes** | **EXCLUIR** | Son ejecuciones ya exploradas |
| **§7 Parámetros** | Heredar | Relación de aspecto y modelo sugerido |

**Dos prohibiciones explícitas:**

1. **No copiar texto del §4 ni del §6.** El documento contiene un prompt bien escrito y el camino de menor esfuerzo es levantarlo tal cual — que es exactamente lo que rompe el propósito de la auditoría. Los prompts nuevos se redactan desde cero cumpliendo `references/prompt-standards.md`, heredando el *ADN* pero no la *redacción*.
2. **Nada marcado `[INFERIDO]` puede convertirse en hecho de marca.** Esas líneas son deducciones del modelo que analizó la imagen, no información verificada. Los hechos vienen solo de `references/brand-context.md`.

### Paso 6 — Reportar antes de idear

Presentar al usuario, en forma compacta:

- Piezas detectadas, agrupadas por plataforma, con su fecha.
- El **ADN común** que se mantendrá (lo que da coherencia).
- La **lista de exclusión** derivada de INCIDENTAL y de las variantes ya exploradas.

Solo entonces continuar a la ideación.

---

## Respaldo: carpetas sin Word de análisis

Si la carpeta contiene únicamente imágenes y ningún `.docx`, no hay análisis que leer. En ese caso:

1. Usar los nombres y fechas de las imágenes como referencia mínima de qué campañas existieron.
2. Preguntar al usuario: *"Esta carpeta no tiene documentos de análisis. ¿Deseas adjuntar en este chat 1 a 3 imágenes de muestra para analizar su estética, o prefieres que continúe solo con los nombres detectados?"*
3. Si `read_resource` falla al abrir un binario, **no bloquear**: seguir con los nombres y avanzar.

Vale la pena sugerirle al usuario correr el flujo de Power Automate sobre esa carpeta: convierte el respaldo en la vía principal.

---

## 📚 Notas técnicas sobre el conector

1. **Microsoft Graph API — conversión de formato:** `/drive/items/{id}/content` transfiere streams crudos. Cuando el conector MCP invoca lectura de texto (`read_resource`) sobre una imagen sin capa OCR, Graph devuelve *Format conversion failed*. Los `.docx` sí tienen capa de texto y se leen sin problema.
2. **Permisos del conector:** usa permisos delegados (`Files.Read`, `Sites.Read.All`) optimizados para texto en Outlook, Word, OneNote y metadatos de SharePoint. No incluye pipeline multimodal de imágenes.
3. **Visión nativa de Claude:** opera por el cargador de adjuntos de la interfaz (`image/jpeg`, `image/png`, `image/webp`). Es la razón por la que el respaldo pide adjuntar imágenes en el chat en vez de leerlas de la nube.
