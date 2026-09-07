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

> 💡 **Nota de fidelidad de producto:** *Para emular fielmente la proporción real del envase y su tipografía discreta (o como primer fotograma en video Image-to-Video), puedes adjuntar en tu herramienta generativa una fotografía oficial de la botella de frente junto con este prompt aprovechando la directiva `ADD` incluida.*
>
> **Prompt principal (los 7 campos, en una sola cadena):**
> [Sujeto: SKU exacto + silueta cónica trapezoidal de cristal macizo + cristalería Riedel + logotipo caligráfico "Loco" en relieve esmaltado rojo cochinilla con fino filete plateado + tipografía secundaria diminuta, sutil y discreta en fino esmalte blanco cerca de la base maciza: "ESPIRITU • ORIGEN" y "TEQUILA {SKU} 100% DE AGAVE AZUL", sin microtextos legales ni letras rojas gigantes] · [Escena y anclaje concreto de la fecha festiva o motivo gastronómico] · [Lente `Nmm f/N` + tipo de plano + profundidad de campo] · [Iluminación nombrada: hora del día o esquema de estudio] · [≥2 colores institucionales por nombre: cochineal crimson / deep wine / bone-ivory / obsidian black / volcanic silver] · [Estilo: referencia fotográfica o artística concreta, no adjetivos genéricos] · [`--ar X:Y`] · `ADD: The added image is the real bottle image, you could use it as an inspiration for the exact bottle geometry, crystal transparency, and small subtle typography placement.`
>
> **Negative prompt (obligatorio, cadena base íntegra):**
> `underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution, gibberish text, misspelled words, garbled letters, typo, scrambled typography, fake writing, illegible labels, deformed text, pseudo-letters, nonsense words, oversized text, giant red lettering, large red typography, clunky font, massive font size` + [lo específico del concepto]
>
> **Parámetros técnicos:**
> - Lente / cámara: [`85mm f/1.4, ISO 100, 1/250s`]
> - Paleta declarada: [colores usados]
> - Estilo/modelo sugerido: [fotografía editorial / render / ilustración]
> - Imagen de referencia sugerida: [Fotografía oficial de la botella de frente, fondo blanco o neutro]
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

**CUMPLIMIENTO Y GUARDRAILS:**
- **Normativa General:** [+18 incluido: sí/no] · [mensaje consumo responsable: sí/no] · [exclusión de menores en pauta: sí/no/no aplica]
- **Ficha Técnica IA 2026 (`references/manual-cumplimiento-ia-2026.md`):**
  - **Nivel de Riesgo:** [Nivel 1 Asistencia | Nivel 2 Sintético Realista | Nivel 3 Prohibido]
  - **Directiva de Toggle de Autodivulgación:** [Meta Ads Manager "AI Info" | YouTube Studio "Contenido sintético" | TikTok "AIGC" | No requiere toggle]
  - **Optimización Anti-Slop LinkedIn (Algoritmo 360Brew):** [Cumple — redacción humana con anécdota de terruño y datos verificados, sin clichés de IA]
  - **Veracidad Comercial (FTC 16 CFR Part 465 / EU AI Act):** [Cumple — cero testimonios ficticios de consumidores ni alteraciones anatómicas engañosas]

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
