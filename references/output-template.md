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

### Reglas técnicas obligatorias para el artefacto HTML:
1. **100% Autocontenido:** No debe realizar llamadas `fetch()` a archivos externos. Todos los datos de la campaña generada deben inyectarse directamente en una variable JavaScript en línea: `const CAMPAIGN = { ... }`.
2. **Sistema de Diseño e Identidad Visual (`designs/Design.md`):**
   - Estilos CSS embebidos en `<style>` utilizando la banda institucional maroon (`--brand-maroon` `#6E1E28`), fondo dark luxury (`#0A0A0C`, `#121216`), fuentes Google Fonts (*Cinzel*, *Outfit*, *Plus Jakarta Sans*) y acentos dorados (`#F2C14E`).
   - **Logotipo Institucional en el Header:** Debe incluir la insignia oficial de **LOCO TEQUILA** (mediante tipografía de lujo *Cinzel* en blanco hueso con acento *TEQUILA* en *Outfit* dorado y subtítulo *Espíritu de Origen*) para garantizar que el logo siempre se visualice nítido y elegante sin depender de rutas locales de imagen en la nube.
3. **Controles de Pasarela y Alternancia:**
   - **Tabs de Conceptos:** Selector con píldoras de color por SKU (Idea 1, Idea 2, Idea 3...) y botones Anterior $\leftarrow$ y Siguiente $\rightarrow$.
   - **Switch de Modo de Vista:** Botones para alternar entre `[✨ Ambos (Pasarela)]`, `[🎨 Solo Prompt]` y `[📝 Solo Copy]`.
4. **Tarjetas de Contenido:**
   - **Zona de Prompt (Arriba):** Muestra el prompt ultra detallado, chips de configuración (aspect ratio, lente, paleta) y botón interactivo para **Copiar Prompt**.
   - **Zona de Copy (Abajo):** Muestra titular, cuerpo, keywords SEO/GEO, hashtags, guardrail `+18 | Evita el exceso` y botón interactivo para **Copiar Copy**.
5. **Leaderboard de IA ([Design Arena](https://www.designarena.ai/leaderboard?tab=image)):** Grid interactivo con ranking de modelos (*FLUX.1 pro, Midjourney v6.1, Google Imagen 3, Ideogram 2.0, Recraft v3, SD 3.5 Large*) con filtros por categoría.
6. **Tips de Configuración:** Tabla de aspect ratios y botón con un clic para copiar el Negative Prompt estricto de marca.
7. **Función de Copiado Universal (Compatible con iframes y Claude Artifacts):**
   Para garantizar que los botones "Copiar Prompt" y "Copiar Copy" funcionen dentro del sandbox del iframe de Claude, el `<script>` DEBE usar el método de `textarea` temporal con `document.execCommand('copy')`:
   ```javascript
   function copyToClipboard(text, toastMsg, buttonEl) {
     if (!text) return;
     let ok = false;
     try {
       const ta = document.createElement("textarea");
       ta.value = text;
       ta.style.position = "fixed";
       ta.style.left = "-9999px";
       ta.style.opacity = "0";
       document.body.appendChild(ta);
       ta.focus();
       ta.select();
       ok = document.execCommand("copy");
       document.body.removeChild(ta);
     } catch (e) { ok = false; }

     if (!ok && navigator.clipboard && navigator.clipboard.writeText) {
       navigator.clipboard.writeText(text).then(() => showToast(toastMsg));
     } else if (ok) {
       showToast(toastMsg);
     }
     if (buttonEl) {
       const orig = buttonEl.innerHTML;
       buttonEl.innerHTML = "✓ ¡Copiado!";
       setTimeout(() => { buttonEl.innerHTML = orig; }, 2000);
     }
   }
   ```
8. **Feedback Visual:** Notificaciones flotantes tipo *Toast* confirmando cada copiado al portapapeles.
