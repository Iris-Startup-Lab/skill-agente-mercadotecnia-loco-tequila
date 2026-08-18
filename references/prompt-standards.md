# Estándares de prompts para IA generativa (imagen y video)

**Leer ANTES de redactar cualquier prompt (paso 9 del flujo).** Este archivo es la única fuente de verdad para la calidad de los prompts. Sustituye a lo que antes vivía en `AGENTS.md` §4.

---

## 1. Campos obligatorios de todo prompt de imagen

Un prompt de imagen **no está terminado** si le falta cualquiera de estos siete campos. No son sugerencias: son el piso de calidad. Si por presupuesto no alcanza para escribir todos los prompts completos, **se reduce el número de prompts, nunca la densidad de cada uno** (ver §4).

| # | Campo | Qué debe contener | Ejemplo |
|---|---|---|---|
| 1 | **Sujeto / producto** | Botella exacta del portafolio y su cristalería oficial. Nombrar el SKU. | `Loco Tequila Blanco bottle`, `Loco Hierofante bottle with its Jan Hendrix / Iker Ortiz art object` |
| 2 | **Composición y encuadre** | Distancia focal en `Nmm`, apertura `f/N`, tipo de plano y profundidad de campo | `85mm f/1.4, medium close-up, shallow depth of field` |
| 3 | **Iluminación** | Condición de luz nombrada explícitamente (hora del día o esquema de estudio) | `warm golden hour sun rays`, `editorial studio chiaroscuro, single hard key light` |
| 4 | **Paleta institucional** | Mínimo **2** colores de marca, en inglés y por nombre de color | `cochineal crimson`, `deep wine`, `bone-ivory`, `obsidian black`, `volcanic silver` |
| 5 | **Estilo visual** | Referencia fotográfica o artística concreta | `luxury editorial photography, Hasselblad medium format look` |
| 6 | **Relación de aspecto** | Parámetro técnico explícito | `--ar 4:5` / `--ar 9:16` / `--ar 16:9` |
| 7 | **Negative prompt** | La cadena base completa de §3, más lo específico del concepto | ver §3 |

Además, el prompt **debe anclar visualmente la fecha festiva elegida** (`{{fechas_proximas}}`) con un elemento concreto de escena, no con una mención abstracta. "Día de Muertos" no es un anclaje; `cempasúal marigold petals scattered on the obsidian surface` sí lo es.

## 2. Campos obligatorios de todo prompt de video

Los siete campos de §1 aplican igual, más tres adicionales:

- **Campo 8 — Desglose por escena** con marcas de tiempo (`Escena 1 (0–3s): …`).
- **Campo 9 — Movimiento de cámara** por escena (`slow dolly in`, `static tripod`, `handheld drift`).
- **Campo 10 — Duración total** y **dirección sonora** (sin afirmar licencias comerciales que no se tienen).

## 3. Negative prompt base (obligatorio, literal)

```text
underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution
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

> Luxury editorial product photography of **Loco Tequila Blanco bottle** resting on raw black obsidian volcanic rock with faint morning mist in El Arenal Jalisco, warm golden hour sun rays piercing through blue agave fields in the background, sharp crystal reflections, condensation droplets on pure glass, **85mm f/1.4** medium format look, hyper-detailed, Hasselblad capture, cinematic chiaroscuro, natural earthy tones, vibrant **cochineal crimson** subtle backlighting over **obsidian black** base, `--ar 4:5` `--no underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution`

Contraejemplo de lo que **no** se acepta (le faltan lente, iluminación nombrada, paleta y `--ar`):

> ~~Botella de Loco Blanco en un paisaje de agave, estilo lujoso y editorial, alta calidad.~~

## 6. Corrección silenciosa

Si al autoverificar (paso 10, `qa-checklist.md`) un prompt no cumple los siete campos, **el agente lo reescribe por su cuenta y vuelve a verificar. No pregunta al usuario.** El usuario ya confirmó los parámetros en los pasos 1–6; completar un campo faltante es trabajo del agente, no una decisión de negocio.

## 7. Inyección de keywords en el prompt

Las keywords SEO/GEO (`references/seo-geo-glossary.md`) van en el **copy**, no dentro del prompt de imagen. Meter keywords en el prompt genera texto renderizado no deseado en la imagen. La verificación correspondiente está en `references/qa-checklist.md`.
