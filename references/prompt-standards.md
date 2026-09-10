# Estándares de prompts para IA generativa (imagen y video)

**Leer ANTES de redactar cualquier prompt (paso 9 del flujo).** Este archivo es la única fuente de verdad para la calidad de los prompts. Sustituye a lo que antes vivía en `AGENTS.md` §4.

---

## 1. Campos obligatorios de todo prompt de imagen

Un prompt de imagen **no está terminado** si le falta cualquiera de estos siete campos. No son sugerencias: son el piso de calidad. Si por presupuesto no alcanza para escribir todos los prompts completos, **se reduce el número de prompts, nunca la densidad de cada uno** (ver §4).

| # | Campo | Qué debe contener | Ejemplo |
|---|---|---|---|
| 1 | **Sujeto / producto (Fidelidad Anatómica)** | Botella exacta del SKU según canon (`references/loco-tequila/`): silueta cónica/trapezoidal, base de cristal macizo de 2 cm, cápsula de cuello por color (Blanco=rojo, Ámbar=bronce, Puro Corazón=plata), logo esmaltado en relieve rojo cochinilla sin etiqueta de papel. Cristalería oficial: copa tequilera Riedel grabada con rombo. | `Loco Tequila Blanco iconic trapezoidal conical heavy crystal bottle with 2cm solid glass base, crimson red neck foil wrap, enameled red cochineal logo on glass, official engraved Riedel tequila flute glass` |
| 2 | **Composición y encuadre** | Distancia focal en `Nmm`, apertura `f/N`, tipo de plano y profundidad de campo | `85mm f/1.4, medium close-up, shallow depth of field` |
| 3 | **Iluminación** | Condición de luz nombrada explícitamente (hora del día o esquema de estudio) | `warm golden hour sun rays`, `editorial studio chiaroscuro, single hard key light` |
| 4 | **Paleta institucional** | Mínimo **2** colores de marca, en inglés y por nombre de color | `cochineal crimson`, `deep wine`, `bone-ivory`, `obsidian black`, `volcanic silver` |
| 5 | **Estilo visual** | Referencia fotográfica o artística concreta | `luxury editorial photography, Hasselblad medium format look` |
| 6 | **Relación de aspecto** | Parámetro técnico explícito | `--ar 4:5` / `--ar 9:16` / `--ar 16:9` |
| 7 | **Negative prompt** | La cadena base completa de §3, más lo específico del concepto | ver §3 |

Además, el prompt **debe anclar visualmente la fecha festiva elegida** (`{{fechas_proximas}}`) con un elemento concreto de escena, no con una mención abstracta. "Día de Muertos" no es un anclaje; `cempasúchil marigold petals scattered on the volcanic obsidian surface` sí lo es.

> **Veracidad de Producto (Cumplimiento 2026 - FTC / TikTok Shop / Meta):** De acuerdo con `references/manual-cumplimiento-ia-2026.md`, está estrictamente prohibido alterar las propiedades físicas reales del producto (forma, color del destilado, volumen 750ml o empaque). La botella de Loco Tequila nunca debe representarse como cilíndrica estándar ni con etiquetas de papel adhesivo. Consultar `references/loco-tequila/bottle_tequila_offiicial_images/resumen_bottle_tequila_offiicial_images.md` y las lecciones de campañas históricas en `references/old_campaigns/resumen_old_campaigns.md`.

### 1.1 Estándar Tipográfico Oficial en la Botella (Anti-Alucinaciones y Escala Real)

> ⚠️ **Regla de Oro contra la alucinación tipográfica y escala deformada:**  
> Para evitar palabras deformadas o faltas de ortografía (como *"BLANEO"* o *"ACWE A20L"*) y **prevenir textos rojos gigantescos o desproporcionados**, el prompt debe establecer con absoluta precisión la jerarquía visual de la botella real:
>
> 1. **Logotipo caligráfico principal (único elemento en rojo):** `"Loco"` en relieve esmaltado vítreo rojo cochinilla vitrificado al fuego, con fino filete plateado de contorno.
> 2. **Eslogan institucional (pequeño y blanco):** `"ESPIRITU • ORIGEN"` (o `"ESPIRITU DE ORIGEN"`) en tipografía sans-serif diminuta, nítida y discreta en fino esmalte blanco sutil.
> 3. **Categoría y pureza oficial (pequeño y blanco):** `"TEQUILA {SKU} 100% DE AGAVE AZUL"` *(donde `{SKU}` se reemplaza por `BLANCO`, `AMBAR` o `PURO CORAZON`)* en tipografía sans-serif de escala reducida y sutil, ubicada cerca de la base maciza de cristal.
>
> **Prohibición estricta de textos rojos gigantes y microtextos legales:**  
> Los textos secundarios (`ESPIRITU • ORIGEN` y categoría) **NUNCA deben describirse en color rojo ni en tamaño grande**. Tampoco deben solicitarse sellos, marbetes, NOM ni leyendas legales minúsculas que saturen el espacio latente.
>
> **Fórmula canónica en prompt de texto:**  
> `prominent raised crimson red enamel calligraphic "Loco" logo with fine silver relief outline centered on pure transparent glass, accompanied below by discrete, fine crisp white sans-serif typography in small delicate scale reading exactly "ESPIRITU • ORIGEN" and "TEQUILA {SKU} 100% DE AGAVE AZUL" positioned near the solid glass base, understated micro-hierarchy, generous clear crystal negative space without cluttered legal micro-text`

### 1.2 Directiva Multimodal de Preservación Anatómica (`ADD:`)

> ⚠️ **Preservación de lo Primordial:** Para evitar que la IA ignore los atributos canónicos de la botella (base maciza, silueta cónica trapezoidal y relieve vítreo rojo) o la reemplace por una botella genérica, se añade de forma obligatoria al prompt multimodal la directiva de preservación estricta:

```text
ADD: The added image is the real bottle image. PRESERVE EXACT BOTTLE MORPHOLOGY: Maintain the identical conical trapezoidal heavy crystal silhouette, the thick 2cm solid base, and the raised crimson enamel "Loco" relief. Strictly prohibit generic cylindrical liquor bottles, paper labels, and round screw caps.
```

> **Guía para el usuario:** Se le recuerda al usuario que puede adjuntar una fotografía oficial de la botella real (fondo blanco o neutro de estudio) junto con el prompt maestro generado para emular a la perfección la silueta, los relieves y las proporciones tipográficas reales tanto en imagen como en video (Image-to-Video).

### 1.3 Regla Canónica: CERO Procesos de Creación del Tequila (Salvo Petición Explícita)

> ⚠️ **REGLA DE ORO DE CONTENIDO (Imagen y Video):**  
> **Tanto en imágenes como en videos, ESTÁ ESTRICTAMENTE PROHIBIDO mostrar los procesos de creación o producción del tequila (faenas de jima de agave, jimadores, hornos de mampostería, piedra tahona, tinas de fermentación, alambiques de destilación, maquinaria industrial ni obreros de fábrica), a menos que el cliente lo pida expresamente.**  
>
> Loco Tequila se conceptualiza como un **objeto de arte, lujo contemplativo y celebración de la vida**, no como un documental de proceso fabril. El producto se representa en su gloria terminada sobre elementos nobles (obsidiana, arquitectura moderna, mármol, luz dorada) y terruño místico en calma.

### 1.4 Bottle-Locks Canónicos por Expresión (`references/brand-context.md`)

Para evitar distorsiones de silueta, cada prompt debe concatenar en sus primeros 20 tokens el bloque anatómico exacto de su expresión:
- **Loco Blanco:** `Loco Blanco tequila bottle, iconic conical trapezoidal clear crystal bottle with 2cm solid heavy glass base, crimson red foil neck wrap, enameled raised red cochineal "Loco" wordmark with silver outline, subtle crisp white typography reading "ESPIRITU • ORIGEN", official engraved Riedel tequila flute glass`
- **Loco Ámbar:** `Loco Ámbar tequila bottle, conical trapezoidal clear glass bottle with 2cm solid base, copper-bronze metallic neck cap, luminous golden amber liquid, enameled raised red cochineal "Loco" wordmark with silver outline, subtle white typography "ESPIRITU • ORIGEN", official Riedel tequila flute`
- **Loco Puro Corazón:** `Loco Puro Corazón tequila bottle, slender conical trapezoidal crystal bottle with 2cm solid base, brushed silver-white metallic neck wrap, pure diamond-clear luminous liquid, enameled raised red cochineal "Loco" wordmark, understated white typography, Riedel crystal flute`
- **Loco Áureo:** `Loco Áureo tequila bottle, conical trapezoidal crystal bottle with 2cm solid base, matte black neck cap, deep mahogany amber liquid, enameled raised red cochineal "Loco" wordmark with silver outline, fine art studio aesthetic`
- **Loco Hierofante:** `Loco Hierofante tequila bottle, sculpted faceted geode crystal flask with hand-carved relief lines, polished solid silver neck ring with engraved "L" monogram, jewel-like collector piece, transcendental silver reflection ambiance`

### 1.5 Regla de Oro Culinaria y Sentido Común Visual (`references/evaluacion-sentido-comun-escena.md`)

> 🍽️ **Menaje y Vajilla Obligatorios:**  
> **NUNCA generar alimentos servidos directamente sobre mesas, piedras, manteles o superficies crudas (ej. un chile en nogada sin plato).**  
> Todo platillo tradicional o de alta cocina debe servirse sobre vajilla de alta gama explícitamente descrita:  
> - *«artfully plated on a deep matte ivory ceramic artisan dish, glossy nogada sauce pooling elegantly on the plate surface, garnished with ruby pomegranate seeds and fresh parsley»*.  
> - La copa Riedel debe estar apoyada firmemente sobre la mesa o posavasos de cuero/piedra con sombras de contacto reales (`contact shadows`), sin levitar ni inclinarse sin soporte.

## 2. Campos obligatorios de todo prompt de video

Los siete campos de §1 aplican igual, más tres adicionales:

- **Campo 8 — Desglose por escena** con marcas de tiempo (`Escena 1 (0–3s): …`).
- **Campo 9 — Movimiento de cámara** por escena (`slow dolly in`, `static tripod`, `handheld drift`).
- **Campo 10 — Duración total** y **dirección sonora** (sin afirmar licencias comerciales que no se tienen).

### 2.1 Veracidad Física y Dinámica de Fluidos del Tequila Servido (Anti-Viscosidad)

> ⚠️ **Problema recurrente de la IA de video:** Los modelos generativos (Sora, Runway, Kling, Veo, Wan) tienden por defecto a simular líquidos espesos, gelatinosos o aceitosos (similares a miel, jarabe o CGI pesado) cuando se les pide un servido genérico (*"pouring tequila"*). El tequila 100% de agave a 40% ABV es un **destilado puro con viscosidad casi idéntica al agua (~1.2 a 1.4 mPa·s)**, no un licor azucarado.

Cuando un prompt de video incluya escenas de vertido (*pouring*), caída del líquido o movimiento en copa, **es obligatorio** incluir los descriptores reológicos y de hidrodinámica real:

1. **Viscosidad ultrabaja y flujo laminar:**  
   `water-thin fluid dynamics`, `ultra-low viscosity liquid (~1.2 cP)`, `crisp high-velocity laminar stream`, `free-flowing natural gravity pour`, `non-viscous distilled agave spirit`.
2. **Impacto, turbulencia y microgotas:**  
   `sharp dynamic liquid splash breaking into fine crystalline micro-droplets`, `rapid fluid turbulence`, `instant energetic surface ripples on the liquid meniscus`.
3. **Aeración instantánea sin espuma:**  
   `transient effervescent micro-bubbles rising and instantly popping with zero residual foam or lather`, `crystal-clear refractive caustics`.
4. **Comportamiento en la cristalería Riedel (Piernas / Lágrimas):**  
   `thin fast-draining tears (lagrimas del tequila) coating the inner crystal walls with crisp transparent runoff, no oily clinging, no syrup coating`.

## 3. Negative prompt base (obligatorio, literal)

### 3.1 Base Universal (Imagen y Video — Incluye Anti-Tipografía Basura, Anti-Textos Gigantes, Anti-Procesos de Producción y Anti-Alucinaciones Culinarias)
```text
underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, generic liquor bottle, cylindrical bottle, round wine bottle, paper label, sticker label, screw cap, flat base, thin glass, painted ceramic decanter, food without plate, unplated food, ceramic decanter, hand-painted pattern, old-fashioned glass, ice cubes, salt rim, lime wedge on rim, shot glass, tequila production process, harvesting agave, jimador, jiming agave, industrial distillery, cooking ovens, brick ovens, industrial machinery, tahona stone, fermentation vats, distillation stills, factory workers, text watermark, blurry, low resolution, gibberish text, misspelled words, garbled letters, typo, scrambled typography, fake writing, illegible labels, deformed text, pseudo-letters, nonsense words, oversized text, giant red lettering, large red typography, clunky font, massive font size
```

### 3.2 Descriptores Anti-Viscosidad (OBLIGATORIO para todo prompt de video con líquidos o servido)
Se suma de forma mandatoria a la base universal en prompts de video:
```text
viscous, viscosity, syrupy, honey, honey-like pour, thick fluid, gelatinous, molasses, oil, oily texture, motor oil, heavy sluggish liquid, gooey, slime, slow-motion goo, sticky syrup, lingering froth, soapy foam, unnatural CGI gel
```

Se puede **añadir**, nunca recortar.

## 4. Regla de escala: prompt maestro + variantes de encuadre

Cuando `{{plataformas_destino}}` incluye **3 o más redes**, escribir un prompt distinto por cada combinación red × idea degrada todos los prompts. En ese caso:

- Se escribe **un prompt maestro completo** (los 7 campos de §1) **por concepto creativo**, no por red.
- Cada red recibe una **variante de encuadre** del maestro: solo cambian `--ar`, el recorte/plano y, si aplica, el texto en pantalla. La variante se expresa en 1–2 líneas referidas al maestro, no se reescribe entero.
- El resultado son pocos prompts excelentes con recortes, en lugar de muchos prompts adelgazados.

Tope duro: **máximo 6 prompts maestros por entrega.** Si `redes × {{numero_ideas}}` excede 6 conceptos, se reduce `{{numero_ideas}}` y se avisa al usuario en las notas de la entrega qué se recortó y por qué.

## 5. Prompt ejemplar (ancla de calidad)

> Luxury editorial product photography of **Loco Tequila Blanco iconic trapezoidal crystal bottle with 2cm solid heavy glass base** resting on raw black obsidian volcanic rock with faint morning mist in El Arenal Jalisco, centered prominent raised crimson red enamel "Loco" logo with delicate silver relief outline, accompanied below by discrete, fine crisp white sans-serif typography in small delicate scale reading "ESPIRITU • ORIGEN" and "TEQUILA BLANCO 100% DE AGAVE AZUL" near the solid glass base, generous crystal negative space, warm golden hour sun rays piercing through blue agave fields in the background, sharp crystal reflections, condensation droplets on pure glass, **85mm f/1.4** medium format look, hyper-detailed, Hasselblad capture, cinematic chiaroscuro, natural earthy tones, vibrant **cochineal crimson** subtle backlighting over **obsidian black** base, `--ar 4:5` `ADD: The added image is the real bottle image. PRESERVE EXACT BOTTLE MORPHOLOGY: Maintain identical conical trapezoidal crystal silhouette, thick 2cm solid base, and raised red enamel "Loco" relief. Strictly prohibit generic cylindrical liquor bottles, paper labels, and round screw caps.` `--no underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, generic liquor bottle, cylindrical bottle, round wine bottle, paper label, sticker label, screw cap, flat base, thin glass, painted ceramic decanter, food without plate, unplated food, ceramic decanter, hand-painted pattern, old-fashioned glass, ice cubes, salt rim, lime wedge on rim, shot glass, tequila production process, harvesting agave, jimador, industrial distillery, cooking ovens, brick ovens, industrial machinery, tahona stone, fermentation vats, distillation stills, text watermark, blurry, low resolution, gibberish text, misspelled words, garbled letters, typo, scrambled typography, fake writing, illegible labels, deformed text, pseudo-letters, nonsense words, oversized text, giant red lettering, large red typography, clunky font, massive font size`

Contraejemplo de lo que **no** se acepta (le faltan lente, iluminación nombrada, paleta y `--ar`):

> ~~Botella de Loco Blanco en un paisaje de agave, estilo lujoso y editorial, alta calidad.~~

## 6. Corrección silenciosa

Si al autoverificar (paso 10, `qa-checklist.md`) un prompt no cumple los siete campos, **el agente lo reescribe por su cuenta y vuelve a verificar. No pregunta al usuario.** El usuario ya confirmó los parámetros en los pasos 1–6; completar un campo faltante es trabajo del agente, no una decisión de negocio.

## 7. Inyección de keywords en el prompt

Las keywords SEO/GEO (`references/seo-geo-glossary.md`) van en el **copy**, no dentro del prompt de imagen. Meter keywords en el prompt genera texto renderizado no deseado en la imagen. La verificación correspondiente está en `references/qa-checklist.md`.
