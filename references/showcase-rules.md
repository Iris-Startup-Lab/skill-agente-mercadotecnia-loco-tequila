# Reglas de la Pasarela Web Interactiva (paso 11)

**Entregable obligatorio y verificable.** Sustituye a lo que antes vivía en `AGENTS.md` §7 y al pie de `output-template.md`.

---

## 1. Qué es el entregable, exactamente

No es "un artefacto de Claude" en abstracto. Son **dos acciones concretas y comprobables**:

1. **Escribir el archivo en disco:** `showcase/campaign-<YYYY-MM-DD>-<slug-campaña>.html`
   (ejemplo: `showcase/campaign-2026-09-16-independencia-locura.html`).
2. **Publicarlo** con la herramienta `Artifact` apuntando a esa ruta, y **entregar el link al usuario** en la respuesta.

Si el entorno no tiene la herramienta `Artifact` disponible, el paso 1 sigue siendo obligatorio y se informa al usuario la ruta del archivo escrito. Lo que **nunca** es aceptable es terminar la entrega sin ninguna de las dos.

La verificación es objetiva: existe el archivo, o no existe. No se marca como cumplido con una casilla.

## 2. Cómo generarlo sin gastar el presupuesto de salida

`references/showcase-template.html` pesa ~26 KB. **Nunca reescribirlo completo.** El procedimiento correcto:

1. Copiar el template al destino:
   ```powershell
   Copy-Item references/showcase-template.html showcase/campaign-<fecha>-<slug>.html
   ```
2. Hacer **exactamente dos sustituciones**, ambas delimitadas por marcadores literales en el template:
   - Todo lo que está entre `// ===== CAMPAIGN:START` y `// ===== CAMPAIGN:END =====` → el dataset generado (§3).
   - El literal `__LOGO_BASE64__` → el contenido de `showcase/assets/logo_base64.txt` (§4).

Todo lo demás —CSS, HTML estructural, las funciones `initApp`, `renderTabs`, `selectConcept`, `nextConcept`, `prevConcept`, `setViewMode`, `renderCurrentConcept`, `copyCurrentPrompt`, `copyCurrentCopy`, `copyUniversal`, `showToast`— **se hereda intacto**. No hay que reescribir ni verificar esas funciones: ya funcionan.

Esto reduce el costo de salida del paso 11 de ~10 000 tokens a unos ~1 500. Esos tokens liberados son exactamente los que necesitan los prompts de imagen (ver `references/prompt-standards.md` §4).

## 3. Esquema del dataset a inyectar

```js
const CAMPAIGN = {
  title: "<nombre de campaña en mayúsculas>",
  subtitle: "<una línea>",
  date_context: "<fecha festiva anclada>",
  items: [
    {
      sku: "Loco Blanco",                     // SKU del portafolio
      sku_color: "#E8A33D",                   // color de la píldora
      platform: "Instagram",
      inventiveness: "Original",              // Original | Locura Genial
      target_persona: "Leonardo (Conocedor & Sibarita)",
      concept_title: "<título del concepto>",
      // PROMPT DE IMAGEN — omitir el objeto entero si {{medio}} es solo video
      prompt: {
        text: "<prompt maestro completo: los 7 campos de prompt-standards.md §1>",
        aspect_ratio: "4:5 (1080x1350)",
        camera_settings: "85mm f/1.4, ISO 100, 1/250s",
        color_palette: "Crimson, Obsidian, Golden Agave",
        negative_prompt: "<cadena base de prompt-standards.md §3>"
      },
      // PROMPT DE VIDEO — obligatorio si {{medio}} es video o ambas; omitir si es solo imagen
      prompt_video: {
        text: "<prompt de video: los 7 campos de §1 + los 3 de §2>",
        aspect_ratio: "9:16 (1080x1920)",
        duration: "24 s",
        camera_movement: "<movimiento por escena>",
        audio: "<dirección sonora; sin afirmar licencias que no se tienen>",
        scenes: [
          { time: "0–3 s", description: "<gancho>" },
          { time: "3–12 s", description: "<desarrollo>" }
        ],
        negative_prompt: "<cadena base de prompt-standards.md §3>"
      },
      copy: {
        headline: "", body: "", call_to_action: "",
        keywords: [], hashtags: [],
        legal: "+18 · Evita el exceso · #EspírituDeOrigen"
      },
      filter_justification: "<por qué pasa el filtro de Locura Genial>"
    }
    // …un objeto por concepto
  ]
};
```

`items` acepta N conceptos: el paginador y las píldoras se generan solos desde `CAMPAIGN.items.length`.

### Imagen y video en la misma pasarela

La pasarela detecta sola qué medios trae cada concepto y se adapta — no hay que tocar código:

- **Etiqueta en la pestaña:** cada píldora muestra `IMG`, `VID` o `IMG+VID`, así que de un vistazo se ve qué se generó para cada concepto.
- **Switch de medio:** si el concepto trae los dos, aparecen las píldoras 🎨 Imagen / 🎬 Video dentro de la caja de prompt. Con un solo medio el switch se oculta.
- **La caja se re-etiqueta:** el título alterna entre *(Text-to-Image)* y *(Text-to-Video)*, y los slots 2 y 3 de la rejilla cambian de significado — en imagen son **Lente** y **Paleta**; en video son **Duración** y **Movimiento de Cámara**.
- **Desglose por escena:** el bloque de escenas solo se muestra en modo video, alimentado por `scenes[]`.
- **El botón de copiado** copia el prompt del medio activo, incluyendo escenas y negative prompt.

Por eso el único requisito real es **poblar `prompt_video` cuando `{{medio}}` sea video o ambas**. Si se deja fuera, el prompt de video simplemente no existe en la pasarela — que era el hueco que tenía el template.

## 4. Logotipo — usar el PNG en base64, no el SVG

`showcase/assets/Loco_Tequila_Logo_white.svg` pesa **2.2 MB** (es un raster trazado). El template lo cargaba con ruta relativa `assets/…`, que **se rompe al publicar como artefacto** porque no existe el directorio hermano; ya se corrigió a un marcador de sustitución.

El template ya trae el marcador `__LOGO_BASE64__` en el `<img>` del header. Sustituirlo por el contenido íntegro de `showcase/assets/logo_base64.txt` (18 KB, ya empieza con `data:image/png;base64,`), que funciona tanto en disco como publicado. En PowerShell:

```powershell
$logo = Get-Content showcase/assets/logo_base64.txt -Raw
(Get-Content $destino -Raw).Replace('__LOGO_BASE64__', $logo.Trim()) | Set-Content $destino -NoNewline
```

## 5. Leaderboard de modelos de imagen — es un EXTRA, no parte del entregable

Su propósito es informativo: decirle al usuario **qué generadores de imagen son hoy los mejores** para ejecutar los prompts que la skill acaba de escribir. No es parte de la campaña y **nunca bloquea la entrega**.

**Dónde vive.** Ya está implementado y funcionando en la pasarela persistente: [`showcase/index.html`](../showcase/index.html) + `renderLeaderboard()` en [`showcase/app.js`](../showcase/app.js), alimentado por `showcase/data/leaderboard.json` (con `DEFAULT_LEADERBOARD` en app.js como respaldo). El template por campaña (`showcase-template.html`) **no lo incluye**, y no hace falta construirlo ahí para cumplir el paso 11. Si se decide añadirlo, es un cambio al template hecho **una vez** y heredado por todas las campañas — nunca improvisado por entrega.

**Fuente:** [Design Arena — Image Leaderboard](https://www.designarena.ai/leaderboard/image). Columnas reales: **Elo Rating** y **Win Rate**. Categorías reales del sitio: Abstract, Architecture, Cartoon, Landscape, **Marketing**, Portrait, **Product**, Typography. Para esta marca las dos relevantes son **Product** (la botella) y **Marketing** (la pieza publicitaria) — no el ranking global.

**Sí es consultable — pero no por HTML.** El sitio es una app Next.js que renderiza la tabla en el cliente: pedir el HTML devuelve el cascarón vacío y WebFetch no ve nada. Los datos viven en un endpoint POST interno. Ya está resuelto en **`sub-skill/obtener-leaderboard-imagen/`**:

```powershell
conda activate skills_env
python sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py --top 10 --actualizar-showcase
```

Eso reescribe `showcase/data/leaderboard.json` con Elo, win rate y batallas **reales**, sella `last_updated` con la fecha de consulta, sincroniza el respaldo de `app.js` y filtra los modelos en prueba ciega (nombres clave sin disponibilidad pública). Detalles, flags y limitaciones en el README de la sub-skill.

- **Nunca escribir posiciones ni Elo de memoria.** Serían cifras inventadas, exactamente lo que prohíbe la regla de datos de la skill. Si el script no se puede ejecutar, omitir el bloque o marcarlo `[no disponible]` — no rellenarlo a mano.
- El dataset lleva `elo_verified`. Cuando es `false`, la pasarela muestra los Elo con `*` y el disclaimer `[REFERENCIA DE INDUSTRIA]`; cuando el script los obtuvo en vivo, pasa a `true` y se muestra la fecha real.

**Qué sí es nuestro y no depende de la fuente:** los campos `recommendation`, `settings_tip`, `loco_rating` y `tags` de cada modelo son curaduría propia de Loco Tequila (qué modelo rinde mejor con cristal y refracción, cuál con tipografía en etiqueta, qué parámetros usar). Esa capa es la parte realmente útil del leaderboard y se mantiene con o sin Elo verificado. Las categorías del JSON ("Botellas & Cristal", "Tipografía & Etiquetas"…) son también curaduría propia, no categorías de Design Arena.

> Nota de mantenimiento: el dataset está **duplicado** en `showcase/data/leaderboard.json` y en `DEFAULT_LEADERBOARD` de `app.js`. Al editar uno, actualizar el otro o diverjan.

## 6. Copiado al portapapeles

Ya resuelto en el template: `copyUniversal()` usa un `<textarea>` temporal con `document.execCommand('copy')` para funcionar dentro de iframes con sandbox restringido. **No reimplementarlo.**

## 7. Sincronización opcional en disco

Si el usuario lo pide explícitamente, actualizar también `showcase/data/campaign.json` y `showcase/data/leaderboard.json` para que la pasarela persistente de `showcase/index.html` refleje la última campaña. Es opcional: no bloquea la entrega.
