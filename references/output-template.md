# Plantilla de salida — Campaña con copys listos y prompts de imagen/video

La skill entrega el resultado como **texto normal de la conversación** (sin bloques de código), con esta estructura. Por cada red destino y por cada idea (`{{numero_ideas}}` por red):

**CAMPAÑA:** [nombre del concepto / título de campaña]

**RED(ES) DESTINO:** [Facebook | YouTube | LinkedIn | TikTok | Instagram]

**FECHA FESTIVA ANCLADA:** [fecha + nombre oficial, p. ej. "Día Nacional del Tequila — 24 de julio"]

**PRODUCTO:** [Loco Blanco | Loco Ámbar | Loco Puro Corazón | Loco Áureo | Loco Hierofante | Portafolio completo]

**PERSONA OBJETIVO:** [Alejandro | Ana | Leonardo | efecto halo]

**MEDIO:** [imagen | video | ambas]

**REFERENCIAS VISUALES REVISADAS (OneDrive/SharePoint):** [carpeta + N imágenes, o "no aplica"]

---

### ▶ FACEBOOK — Idea 1: [nombre del concepto]

- **Ángulo:** [qué explora esta idea: terruño, arte, ocasión, legado, audacia… y por qué conecta con la fecha festiva y la persona objetivo]
- **Copy listo para publicar:**
  > [texto final, listo para pegar en Facebook]
- **Formato:** [video/carrusel/imagen] · **Relación de aspecto:** [ ] · **Duración:** [ ]
- **CTA:** [ ]
- **Palabras clave insertadas:** [del glosario]
- **Hashtags:** [ ]

*(repetir "Idea 2:", "Idea 3:"… en la misma red)*

### ▶ YOUTUBE — Idea 1: [nombre del concepto]

- **Ángulo:** [ ]
- **Copy listo para publicar:**
  > [título + descripción + CTA, listos para pegar en YouTube]
- **Formato:** [long-form / Shorts]
- **Tags/etiquetas:** [ ]
- **Miniatura (concepto):** [descripción en texto de qué mostrar]

### ▶ LINKEDIN — Idea 1: [nombre del concepto]

- **Ángulo:** [ ]
- **Copy listo para publicar:**
  > [texto con enfoque de negocio/legado, listo para pegar]
- **Formato:** [texto+imagen / documento / video corto]
- **Hashtags corporativos:** [ ]

### ▶ TIKTOK — Idea 1: [nombre del concepto]

- **Ángulo:** [ ]
- **Gancho (primeros 2s):** [ ]
- **Guion/estructura de escenas:** [ ]
- **Copy listo para publicar:**
  > [caption corto + hashtags, listos para pegar]
- **Sonido/tendencia sugerida:** [ ]
- **Texto en pantalla:** [ ]

---

## Prompts ultra detallados para IA generativa

> **Antes de escribir estos bloques, leer `references/prompt-standards.md`.** Los 7 campos de su §1 son obligatorios; un prompt al que le falte cualquiera de ellos no está terminado y se reescribe. Con 3+ redes destino, aplicar la regla de **prompt maestro + variantes de encuadre** (§4) en lugar de un prompt distinto por red.

### 🎨 PROMPT MAESTRO DE IMAGEN — [nombre del concepto]

> **Prompt principal (los 7 campos, en una sola cadena):**
> [Sujeto: SKU exacto + cristalería] · [Escena y anclaje concreto de la fecha festiva] · [Lente `Nmm f/N` + tipo de plano + profundidad de campo] · [Iluminación nombrada: hora del día o esquema de estudio] · [≥2 colores institucionales por nombre: cochineal crimson / deep wine / bone-ivory / obsidian black / volcanic silver] · [Estilo: referencia fotográfica o artística concreta, no adjetivos genéricos] · [`--ar X:Y`]
>
> **Negative prompt (obligatorio, cadena base íntegra):**
> `underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution` + [lo específico del concepto]
>
> **Parámetros técnicos:**
> - Lente / cámara: [`85mm f/1.4, ISO 100, 1/250s`]
> - Paleta declarada: [colores usados]
> - Estilo/modelo sugerido: [fotografía editorial / render / ilustración]
> - Variaciones: [número de variaciones a generar]
>
> **Variantes de encuadre por red** (solo si hay 3+ redes; 1–2 líneas cada una, referidas al maestro):
> - Instagram `--ar 4:5`: [qué cambia en el recorte/plano]
> - TikTok `--ar 9:16`: [qué cambia]
> - YouTube `--ar 16:9`: [qué cambia]

### 🎬 PROMPT DE VIDEO — [nombre del concepto]

> **Prompt principal (descripción de escenas):**
> [Descripción ultra detallada por escena: acción, encuadre, movimiento de cámara, iluminación, paleta, sonido/ambiente, ritmo, y texto en pantalla. Indicar duración total y estructura.]
>
> **Escenas (desglose):**
> - Escena 1 (0–Xs): [descripción]
> - Escena 2 (Xs–Ys): [descripción]
> - …
>
> **Negative prompt (si aplica):**
> [texto no deseado, menores, consumo excesivo, marcas de agua, etc.]
>
> **Parámetros técnicos sugeridos:**
> - Relación de aspecto: [9:16 / 16:9 / 1:1]
> - Duración: [ ]
> - Estilo/modelo sugerido: [cinematográfico / animación / motion graphics]
> - Audio/música: [dirección sonora; sin licencia comercial especificada]

---

**FILTRO LOCURA GENIAL (por idea):** [ES / NO ES — justificar]

**CUMPLIMIENTO:** [+18 incluido: sí/no] · [mensaje consumo responsable: sí/no] · [exclusión de menores en pauta configurada: sí/no/no aplica]

**ADVERTENCIAS / NOTAS:**
- [datos no disponibles, estimaciones (*) o valores [REFERENCIA DE INDUSTRIA] usados]
- [ideas descartadas por no pasar el filtro de Locura Genial, si aplica]
- [cifras de alcance/engagement/benchmarks SOLO si se pidieron o se generaron; si no aplica, no escribir ninguna nota al respecto]

---

## 🖥️ Pasarela Web Interactiva (paso 11 — obligatorio)

Al cerrar la respuesta en markdown, el agente **DEBE** entregar además la Pasarela Web. Son dos acciones con rastro comprobable, no una casilla:

1. Copiar `references/showcase-template.html` a **`showcase/campaign-<YYYY-MM-DD>-<slug>.html`**.
2. Sustituir **únicamente** el bloque `const CAMPAIGN = { … };` (líneas 609–639 del template) por el dataset de los conceptos generados.
3. Publicar el archivo con la herramienta `Artifact` y entregar el link al usuario.

**Nunca reescribir el template completo** (~26 KB): todo el CSS, el HTML estructural y las funciones (`initApp`, `renderTabs`, `selectConcept`, `prevConcept`/`nextConcept`, `setViewMode`, `renderCurrentConcept`, `copyCurrentPrompt`, `copyCurrentCopy`, `copyUniversal`, `showToast`) se heredan intactos y ya funcionan. Los tokens que eso ahorra son los que necesitan los prompts de imagen.

El esquema del dataset, el manejo del logo (data-URI base64, **no** el SVG de 2.2 MB) y el resto del procedimiento están en **`references/showcase-rules.md`**. La verificación correspondiente está en `references/qa-checklist.md`.
