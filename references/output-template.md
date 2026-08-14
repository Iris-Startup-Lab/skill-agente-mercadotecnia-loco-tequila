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

### 🎨 PROMPT DE IMAGEN — [nombre del concepto]

> **Prompt principal:**
> [Prompt en inglés o español según la herramienta, ultra detallado, describiendo: sujeto/producto, encuadre y composición, iluminación y hora del día, paleta de color de marca (rojo cochinilla / vino profundo, hueso-marfil, negro y plata), atmósfera, texto/elementos gráficos, estilo fotográfico o artístico, y referencia a la fecha festiva anclada.]
>
> **Negative prompt (si aplica):**
> [texto no deseado, marcas de agua, menores de edad, consumo excesivo, imitación de botellas de competidores, etc.]
>
> **Parámetros técnicos sugeridos:**
> - Relación de aspecto: [1:1 / 4:5 / 9:16 / 16:9]
> - Estilo/modelo sugerido: [fotografía editorial / render / ilustración]
> - Variaciones: [número de variaciones a generar]

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

## 🖥️ Pasarela Web Interactiva (Showcase HTML / Claude Artifact)

Al finalizar la respuesta en texto markdown, el agente **DEBE generar un Artefacto HTML autónomo (Claude Artifact)** con la Pasarela Web interactiva.

Para garantizar que el artefacto funcione al 100% (renderice el logo oficial, muestre los prompts generados, responda a los clics de filtros/paginador y copie al portapapeles), el agente **DEBE utilizar la estructura y funciones de [showcase-template.html](file:///e:/Users/1167486/Local/scripts/skills_generales/agente-mercadotecnia-loco-tequila/references/showcase-template.html)**:

### Reglas obligatorias para la generación del HTML:
1. **Inyección Directa de Datos (`const CAMPAIGN`):** Inyectar el array completo de conceptos generados (título, SKU, plataforma, target persona, prompt ultra detallado con lente/aspect ratio/negative prompt, copy nativo con titular/cuerpo/keywords/hashtags/legal, y justificación del filtro).
2. **Pre-renderizado en el HTML:** Escribir el texto del primer prompt en `#prompt-text-display` y del primer copy en `#copy-headline-display` / `#copy-body-display` para asegurar visibilidad inmediata.
3. **Logotipo Oficial:** Usar el archivo oficial de logo vectorial `showcase/assets/Loco_Tequila_Logo_white.svg` (o `assets/Loco_Tequila_Logo_white.svg` / `imagenes/Loco_Tequila_Logo_white.svg`) en el header de la pasarela.
4. **Controles Interactivos con `onclick` Directo:**
   - Switch de Modo de Vista: `onclick="setViewMode('all')"` (✨ Ambos), `onclick="setViewMode('prompt')"` (🎨 Solo Prompt), `onclick="setViewMode('copy')"` (📝 Solo Copy).
   - Paginador de Conceptos: `onclick="prevConcept()"` y `onclick="nextConcept()"`.
   - Píldoras de Tabs: `onclick="selectConcept(idx)"`.
5. **Copiado Universal sin Errores:**
   - Botón Prompt: `onclick="copyCurrentPrompt(this)"`.
   - Botón Copy: `onclick="copyCurrentCopy(this)"`.
   - Utilizar la función `copyUniversal(text, btn, msg)` con `<textarea>` temporal y `document.execCommand('copy')` para garantizar funcionamiento en el sandbox de iframes de Claude.
6. **Feedback Visual:** Notificaciones flotantes tipo *Toast* confirmando cada copiado al portapapeles.
