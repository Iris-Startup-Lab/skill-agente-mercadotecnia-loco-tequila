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

### 1.1 Estándar Tipográfico Oficial en la Botella (Anti-Alucinaciones)

> ⚠️ **Regla de Oro contra la alucinación tipográfica:** Para evitar palabras deformadas o faltas de ortografía (como *"BLANEO"* o *"ACWE A20L"*), el prompt **NUNCA debe solicitar textos legales minúsculos** (como 750ml, % alc, NOM o leyendas largas). Cuando se requiera texto legible en la botella, se debe usar **estrictamente la fórmula oficial de 3 líneas entre comillas dobles**:
>
> 1. Logotipo caligráfico principal: `"Loco"` (en rojo cochinilla esmaltado al fuego).
> 2. Eslogan institucional: `"ESPIRITU DE ORIGEN"`
> 3. Categoría y pureza exacta según el SKU: `"TEQUILA {SKU} 100% DE AGAVE AZUL"`  
>    *(donde `{SKU}` se reemplaza por `BLANCO`, `AMBAR` o `PURO CORAZON`)*
>
> **Ejemplo de integración en prompt:**  
> `silkscreened raised red enamel branding on clear glass with crisp typography reading exactly "Loco" above "ESPIRITU DE ORIGEN" and "TEQUILA BLANCO 100% DE AGAVE AZUL", sharp legible letterforms, perfectly aligned serif and sans-serif typography, clean transparent bottle surface without cluttered legal micro-text`

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

### 3.1 Base Universal (Imagen y Video — Incluye Anti-Tipografía Basura)
```text
underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution, gibberish text, misspelled words, garbled letters, typo, scrambled typography, fake writing, illegible labels, deformed text, pseudo-letters, nonsense words
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

Este es el estándar contra el cual se mide cada prompt. Cumple los 7 campos:

> Luxury editorial product photography of **Loco Tequila Blanco iconic trapezoidal crystal bottle** resting on raw black obsidian volcanic rock with faint morning mist in El Arenal Jalisco, silkscreened raised red enamel branding on clear glass with crisp typography reading exactly "Loco" above "ESPIRITU DE ORIGEN" and "TEQUILA BLANCO 100% DE AGAVE AZUL", warm golden hour sun rays piercing through blue agave fields in the background, sharp crystal reflections, condensation droplets on pure glass, **85mm f/1.4** medium format look, hyper-detailed, Hasselblad capture, cinematic chiaroscuro, natural earthy tones, vibrant **cochineal crimson** subtle backlighting over **obsidian black** base, `--ar 4:5` `--no underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution, gibberish text, misspelled words, garbled letters, typo, scrambled typography, fake writing, illegible labels, deformed text, pseudo-letters, nonsense words`

Contraejemplo de lo que **no** se acepta (le faltan lente, iluminación nombrada, paleta y `--ar`):

> ~~Botella de Loco Blanco en un paisaje de agave, estilo lujoso y editorial, alta calidad.~~

## 6. Corrección silenciosa

Si al autoverificar (paso 10, `qa-checklist.md`) un prompt no cumple los siete campos, **el agente lo reescribe por su cuenta y vuelve a verificar. No pregunta al usuario.** El usuario ya confirmó los parámetros en los pasos 1–6; completar un campo faltante es trabajo del agente, no una decisión de negocio.

## 7. Inyección de keywords en el prompt

Las keywords SEO/GEO (`references/seo-geo-glossary.md`) van en el **copy**, no dentro del prompt de imagen. Meter keywords en el prompt genera texto renderizado no deseado en la imagen. La verificación correspondiente está en `references/qa-checklist.md`.
