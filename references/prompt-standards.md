# Estándares de prompts para IA generativa (imagen y video)

**Leer ANTES de redactar cualquier prompt (paso 9 del flujo).** Este archivo es la única fuente de verdad para la calidad de los prompts. Sustituye a lo que antes vivía en `AGENTS.md` §4.

---

## 1. Campos obligatorios de todo prompt de imagen

Un prompt de imagen **no está terminado** si le falta cualquiera de estos siete campos. No son sugerencias: son el piso de calidad. Si por presupuesto no alcanza para escribir todos los prompts completos, **se reduce el número de prompts, nunca la densidad de cada uno** (ver §4).

| # | Campo | Qué debe contener | Ejemplo |
|---|---|---|---|
| 1 | **Sujeto / producto (Fidelidad Anatómica)** | Botella exacta del SKU según canon (`references/loco-tequila/`): silueta cónica/trapezoidal, base de cristal macizo de 2 cm, cápsula de cuello por color (Blanco=rojo, Ámbar=bronce, Puro Corazón=plata), logo esmaltado en relieve rojo cochinilla sin etiqueta de papel. Cristalería oficial: copa tequilera Riedel grabada con rombo (silueta tulipán). | `Loco Tequila Blanco iconic trapezoidal conical heavy crystal bottle with 2cm solid glass base, crimson red neck foil wrap, enameled red cochineal logo on glass, narrow tulip-shaped crystal tasting glass with tapered rim (Riedel tequila glassware silhouette)` |
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
> 1. **Logotipo caligráfico principal (único elemento en rojo):** `"Loco"` en relieve esmaltado vítreo rojo cochinilla vitrificado al fuego directo sobre el cristal, borde limpio al ras sin filete blanco, sin trazo ni contorno adhesivo (*direct glass enamel without white border or sticker halo*).
> 2. **Eslogan institucional (pequeño y blanco):** `"ESPIRITU • ORIGEN"` (o `"ESPIRITU DE ORIGEN"`) en tipografía sans-serif diminuta, nítida y discreta en fino esmalte blanco sutil.
> 3. **Categoría y pureza oficial (pequeño y blanco):** `"TEQUILA {SKU} 100% DE AGAVE AZUL"` *(donde `{SKU}` se reemplaza por `BLANCO`, `AMBAR` o `PURO CORAZON`)* en tipografía sans-serif de escala reducida y sutil, ubicada cerca de la base maciza de cristal.
>
> **Prohibición estricta de textos rojos gigantes, contornos tipo calcomanía y microtextos legales:**  
> Los textos secundarios (`ESPIRITU • ORIGEN` y categoría) **NUNCA deben describirse en color rojo ni en tamaño grande**. El logotipo `"Loco"` **nunca debe llevar filete o contorno blanco/plateado** que induzca efecto de pegatina o calcomanía recortada. Tampoco deben solicitarse sellos, marbetes, NOM ni leyendas legales minúsculas que saturen el espacio latente.
>
> **Fórmula canónica en prompt de texto:**  
> `prominent raised crimson red vitreous enamel calligraphic "Loco" logo fused directly onto pure transparent curved crystal glass, sharp flush edge without outline, zero white border, zero sticker stroke, accompanied below by discrete, fine crisp white sans-serif typography in small delicate scale reading exactly "ESPIRITU • ORIGEN" and "TEQUILA {SKU} 100% DE AGAVE AZUL" positioned near the solid glass base, understated micro-hierarchy, generous clear crystal negative space without cluttered legal micro-text`

### 1.2 Directiva Multimodal de Preservación Anatómica (`ADD:`)

> ⚠️ **Preservación de lo Primordial:** Para evitar que la IA ignore los atributos canónicos de la botella (base maciza, silueta cónica trapezoidal y relieve vítreo rojo) o la reemplace por una botella genérica, se añade de forma obligatoria al prompt multimodal la directiva de preservación estricta:

```text
ADD: The added image is the real bottle image. PRESERVE EXACT BOTTLE MORPHOLOGY: Maintain the identical conical trapezoidal heavy crystal silhouette, the thick 2cm solid base, and the raised crimson vitreous enamel "Loco" relief applied directly onto the clear glass without any white border, white stroke, decal halo, or sticker outline. Strictly prohibit generic cylindrical liquor bottles, paper labels, sticker decals, and round screw caps.
```

> **Guía para el usuario:** Se le recuerda al usuario que puede adjuntar una fotografía oficial de la botella real (fondo blanco o neutro de estudio) junto con el prompt maestro generado para emular a la perfección la silueta, los relieves y las proporciones tipográficas reales tanto en imagen como en video (Image-to-Video).

### 1.3 Regla Canónica: CERO Procesos de Creación del Tequila (Salvo Petición Explícita)

> ⚠️ **REGLA DE ORO DE CONTENIDO (Imagen y Video):**  
> **Tanto en imágenes como en videos, ESTÁ ESTRICTAMENTE PROHIBIDO mostrar los procesos de creación o producción del tequila (faenas de jima de agave, jimadores, hornos de mampostería, piedra tahona, tinas de fermentación, alambiques de destilación, maquinaria industrial ni obreros de fábrica), a menos que el cliente lo pida expresamente.**  
>
> Loco Tequila se conceptualiza como un **objeto de arte, lujo contemplativo y celebración de la vida**, no como un documental de proceso fabril. El producto se representa en su gloria terminada sobre elementos nobles (obsidiana, arquitectura moderna, mármol, luz dorada) y terruño místico en calma.

### 1.4 Bottle-Locks Canónicos por Expresión (`references/brand-context.md`)

Para evitar distorsiones de silueta, cada prompt debe concatenar en sus primeros 20 tokens el bloque anatómico exacto de su expresión:
- **Loco Blanco:** `Loco Blanco tequila bottle, iconic conical trapezoidal clear crystal bottle with 2cm solid heavy glass base, crimson red foil neck wrap, direct vitreous raised red cochineal "Loco" enamel without outline or border, subtle crisp white typography reading "ESPIRITU • ORIGEN", narrow tulip-shaped crystal tasting glass with tapered rim (Riedel tequila glassware silhouette)`
- **Loco Ámbar:** `Loco Ámbar tequila bottle, conical trapezoidal clear glass bottle with 2cm solid base, copper-bronze metallic neck cap, luminous golden amber liquid, direct vitreous raised red cochineal "Loco" enamel without outline or border, subtle white typography "ESPIRITU • ORIGEN", narrow tulip-shaped crystal tasting glass with tapered rim (Riedel tequila glassware silhouette)`
- **Loco Puro Corazón:** `Loco Puro Corazón tequila bottle, slender conical trapezoidal crystal bottle with 2cm solid base, brushed silver-white metallic neck wrap, pure diamond-clear luminous liquid, direct vitreous raised red cochineal "Loco" enamel without outline, understated white typography, narrow tulip-shaped crystal tasting glass with tapered rim (Riedel tequila glassware silhouette)`
- **Loco Áureo:** `Loco Áureo tequila bottle, conical trapezoidal crystal bottle with 2cm solid base, matte black neck cap, deep mahogany amber liquid, direct vitreous raised red cochineal "Loco" enamel without outline, fine art studio aesthetic`
- **Loco Hierofante:** `Loco Hierofante tequila bottle, sculpted faceted geode crystal flask with hand-carved relief lines, polished solid silver neck ring with engraved "L" monogram, jewel-like collector piece, transcendental silver reflection ambiance`

### 1.5 Regla de Oro Culinaria y Sentido Común Visual (`references/evaluacion-sentido-comun-escena.md`)

> 🍽️ **Menaje y Vajilla Obligatorios:**  
> **NUNCA generar alimentos servidos directamente sobre mesas, piedras, manteles o superficies crudas (ej. un chile en nogada sin plato).**  
> Todo platillo tradicional o de alta cocina debe servirse sobre vajilla de alta gama explícitamente descrita:  
> - *«artfully plated on a deep matte ivory ceramic artisan dish, glossy nogada sauce pooling elegantly on the plate surface, garnished with ruby pomegranate seeds and fresh parsley»*.  
> - La copa Riedel debe estar apoyada firmemente sobre la mesa o posavasos de cuero/piedra con sombras de contacto reales (`contact shadows`), sin levitar ni inclinarse sin soporte.

## 2. Campos obligatorios de todo prompt de video

Los siete campos de §1 aplican igual, más tres adicionales:

- **Campo 8 — Beats con marcas de tiempo** dentro del tramo (`0–3s / 3–6s / 6–10s`).
- **Campo 9 — Movimiento de cámara** concreto (`slow dolly in`, `static tripod`, `slow orbit`, `top-down`).
- **Campo 10 — Duración** del tramo y **sonido**: `ambient room tone and foley only, no music` (la música va en un prompt aparte, `videos-cliente.md` §3).

**Antes de escribir:** leer `references/videos-cliente.md` (qué se filma: ritmo, mezcla de tomas, luz, atrezo, personas).

### 2.0 Arquitectura del prompt de video ("diseña un plano, no un universo")

**Principios:**
- El prompt es una **lista de tomas ejecutable**, no una descripción poética: solo acciones que una cámara pueda registrar (movimiento, luz, encuadre).
- **Una sola acción principal por tramo** (5–10 s). El ritmo de corte de 1.5–3 s de los videos del cliente se logra en el montaje, no metiendo muchas acciones en un tramo.
- **Inglés limpio** en todo el prompt positivo.
- **Cero meta-texto** en el prompt positivo: nada de encabezados en español (`REFERENCIA DE ENTRADA:`, `ESCENAS:`, `FOTOGRAMA DE SALIDA:`), ni etiquetas que el modelo pueda renderizar como subtítulos. Esos datos van en campos separados de la entrega.
- **Cero texto generado:** prohibido pedir al modelo tagline, leyenda legal, rótulos o tipografía secundaria. Se pide `clean negative space in the lower third for post-production graphics`. Textos, end card y `+18 · Evita el exceso` se montan en postproducción (§2.4).
- **Negative prompt siempre en su casilla aparte**, íntegro (§3.1 + §3.2), nunca dentro del positivo.

**Orden canónico obligatorio del prompt positivo** (las etiquetas en mayúsculas son de estructura en inglés y sí van en el prompt):

```text
[Format & duration: vertical 9:16, 10 seconds]. [CONTINUATION … — solo en tramos de tipo continuation, §2.3]
SETTING & LIGHTING: <entorno, paleta, temperatura de color, contraluz/rim light>.
ACTIVE REFERENCES: @Image1 as master product reference (exact bottle). [@Frame1 as starting frame.] [@Video1 for pour physics.]
ACTION & BEATS: 0–3s <beat 1>. 3–6s <beat 2>. 6–10s <resolución>.
CAMERA: <un movimiento concreto + lente, f/1.4–f/2.8>.
PRESERVATION & LOCKS: <candado de botella, física de fluidos si hay líquido, clean lower third, ambient sound only, no music>.
```

**Menciones `@`:** se escriben genéricas (`@Image1`, `@Frame1`, `@Video1`), con un rol explícito para cada una. Cada herramienta nombra distinto sus referencias (etiquetas, "ingredients", imagen de inicio): la entrega indica en una línea que se renombren al cargarlas. Si no hay referencia adjunta, se omite su mención.

**Rigidez con una sola imagen:** si solo hay **una** foto del producto, la botella queda **estática y rígida** y lo que se mueve es la cámara o el entorno (luz que barre, mano que entra, líquido que cae en la copa), para evitar deformaciones en 3D.

**Dos versiones por tramo:**
- **Completa** (`text`): orden canónico + biblia de continuidad literal + descriptores de fluidos de §2.1. Para herramientas sin límite práctico (Gemini/Veo/Flow, Kling hasta 2 500 caracteres, Seedance vía API).
- **Compacta** (`text_compact`): mismo orden canónico, **máximo 500 caracteres** (contando espacios), con la biblia sustituida por el candado corto `Preserve exact bottle morphology and label from @Image1. Do not redraw typography.` y los fluidos reducidos a `water-thin still spirit, no bubbles, settles in 1.5s`. Para herramientas con tope (Higgsfield Cinema Studio, Runway, Dreamina).

Límites de prompt investigados el 2026-10-02 (verificar antes de cada campaña; no son documentación oficial salvo donde se indica):

| Herramienta | Límite | Fuente |
| --- | --- | --- |
| Higgsfield Cinema Studio 2.5 / 3.0 | 512 caracteres; cada mención `@` consume ~80–100 ocultos | Guía de terceros (OSideMedia) |
| Runway Gen-4 / Gen-4 Turbo | 1 000 caracteres | Terceros (unifically.com) |
| Kling (texto a video) | 2 500 caracteres (igual el negativo) | Pollo AI, Vyond |
| Seedance (API BytePlus) | Hasta 20 000 caracteres | Terceros |
| Dreamina (web) | `[no disponible]` | — |
| Veo / Gemini API | `[no disponible]` (la documentación oficial no fija límite) | ai.google.dev |

El tope de 500 caracteres de la versión compacta lo confirmó el usuario y cubre al más estricto. **Con 2+ menciones `@` en Higgsfield 2.5, apuntar a ~250 caracteres visibles.**

### 2.1 Veracidad Física y Dinámica de Fluidos del Tequila Servido (Anti-Viscosidad y Anti-Carbonatación)
*(Fuente técnica completa: [`especificaciones-fluidos.md`](especificaciones-fluidos.md))*

> ⚠️ **Problema recurrente de la IA de video:** Los modelos generativos (Sora, Runway, Kling, Veo, Wan, Seedance) tienden por defecto a simular líquidos espesos o con efervescencia errónea (similares a miel, jarabe, sidra o cerveza clara) cuando se les pide un servido genérico (*"pouring tequila"*). El tequila 100% de agave a 40% ABV es un **destilado puro con viscosidad casi idéntica al agua (~1.2 a 1.4 mPa·s), completamente plano y sin gas**, no un fermentado ni un licor azucarado.

Cuando un prompt de video incluya escenas de vertido (*pouring*), caída del líquido o movimiento en copa, **es obligatorio** incluir los descriptores reológicos y de hidrodinámica real según `references/especificaciones-fluidos.md`:

1. **Viscosidad ultrabaja y flujo laminar:**  
   `water-thin fluid dynamics`, `ultra-low viscosity liquid (~1.2 cP)`, `crisp high-velocity laminar stream`, `free-flowing natural gravity pour`, `non-viscous distilled agave spirit`.
2. **Impacto, turbulencia y microgotas:**  
   `dynamic liquid impact breaking into sharp crystalline micro-droplets`, `rapid fluid turbulence`, `instant energetic surface ripples on the liquid meniscus`.
3. **Desactivación de emisores de fondo y microburbujas mecánicas:**  
   `no bottom emitters`, `mechanical impact micro-bubbles that burst instantly upon reaching the surface`, `zero residual foam, zero surface ring, zero trapped bubbles on inner crystal walls`.
4. **Tiempo de reposo y estabilización (<1.5s):**  
   `settles into a completely still, inert liquid surface within 1.5 seconds after pouring ceases`, `glass-like flat meniscus with zero internal turbulence`.
5. **Comportamiento en la cristalería Riedel (Piernas / Lágrimas):**  
   `narrow tulip-shaped Riedel crystal tasting glass with tapered rim`, `crisp thin transparent tequila tears (lágrimas del tequila) draining smoothly and swiftly down inner crystal walls, no oily residue, no syrup coating`.
6. **Interacción óptica y transmisión de luz (sin oscurecimiento central):**  
   - Para Blanco/Puro Corazón: `diamond-clear transparency, uniform light transmission with no central darkening, sharp refractive caustics, volcanic silver highlights`.  
   - Para Ámbar/Áureo: `luminous golden-amber crystal translucency, uniform radiant clarity with no murky central darkening, warm honey and copper specular reflections`.

### 2.2 Entradas Multimodales para Video: Botella y Referencia de Vertido

La skill contempla **dos métodos de referencia multimodal** que el usuario puede proporcionar para enriquecer la generación de video, además del respaldo textual autónomo:

1. **Referencia de la Botella Real (Image-to-Video):**  
   El usuario puede adjuntar una fotografía oficial de la botella de Loco Tequila. El prompt incorpora de forma obligatoria la directiva de preservación morfológica:  
   `ADD: The added image is the real bottle image. PRESERVE EXACT BOTTLE MORPHOLOGY: Maintain identical conical trapezoidal crystal silhouette, thick 2cm solid base, and raised red enamel "Loco" relief. Strictly prohibit generic cylindrical liquor bottles, paper labels, and round screw caps.`
2. **Clip de Referencia del Vertido Real (Video-to-Video / Motion Transfer - OPCIONAL):**  
   En modelos generativos de video que admiten referencias visuales multimodales (como Seedance 2.5, Kling o Runway Gen-3), el usuario puede **opcionalmente** adjuntar un clip corto de referencia real de un vertido de destilado transparente (agua o tequila en copa de degustación) para anclar la hidrodinámica. Si se utiliza, se añade la directiva:  
   `MATCH POUR PHYSICS: match the exact water-thin pour physics (~1.2 cP), continuous laminar stream into Riedel crystal glass, instant bubble burst on impact, and zero-carbonation still surface shown in the reference video.`  
3. **Respaldo Autónomo por Texto:**  
   Si el usuario no proporciona imagen ni clip, el prompt detallado en §2.1 y el negative prompt de §3.2 proporcionan por sí solos la protección física completa e independiente.
4. **Video del tramo anterior (videos encadenados, §2.3):**  
   En los tramos `continuation` la referencia **principal** es el video del tramo N‑1 (en los `cut`, la foto oficial de la botella). La fotografía oficial de la botella puede sumarse como segunda referencia si la herramienta acepta varias entradas; si solo acepta una, prevalece el video previo.

### 2.3 Videos encadenados por tramos de 10 s

Los modelos de video rinden mejor en clips de ~10 s. Por eso un video de más de 10 s **no se escribe como un solo prompt largo**, sino como una cadena de prompts, uno por tramo, según `{{duracion_video}}`:

| Duración total | Tramos | Reparto |
| --- | --- | --- |
| 10 s | 1 | 10 |
| 20 s | 2 | 10 + 10 |
| 30 s | 3 | 10 + 10 + 10 |
| 45 s | 5 | 10 + 10 + 10 + 10 + 5 (cierre) |
| 60 s | 6 | 10 × 6 |

Máximo 60 s. Con 10 s se escribe un único prompt, sin directiva de continuidad. Para parecerse a los reels del cliente, 20–30 s es lo más cercano (`videos-cliente.md` §2.1).

**Cómo mantener la consistencia entre tramos (dos capas):**

1. **Capa principal — el video anterior como referencia (tramos `continuation`).** Cada tramo que sigue la misma toma se genera dándole a la herramienta el resultado del tramo N‑1. Según lo que admita la herramienta, en orden de preferencia:
   - **(a) Extender video** (la herramienta continúa el clip previo). Máxima consistencia.
   - **(b) Video como referencia** (video-to-video / referencia multimodal).
   - **(c) Último fotograma como imagen de inicio** (image-to-video). La opción que acepta casi cualquier herramienta.
2. **Capa de respaldo — biblia de continuidad.** Un bloque fijo de descriptores que se copia **literal, palabra por palabra, en todos los tramos**: morfología canónica de la botella (primeros 20 tokens), cristalería Riedel, lente/encuadre base, esquema de iluminación, paleta y los descriptores de fluidos de §2.1 si hay líquido. Es obligatoria aunque se use la referencia, porque cada generación es independiente, muchas herramientas solo ven los últimos segundos o el último fotograma, y la deriva (relieve «Loco», cápsula, tono del líquido) se acumula en cadenas de 5–6 tramos.

**Tipo de tramo (`shot_type`), según el guion y la mezcla de tomas de `videos-cliente.md` §2.2:**

- **`continuation`** — sigue la **misma toma** del tramo anterior. Abre con la directiva `CONTINUATION` y usa el video o el último fotograma del tramo N‑1 como `@Frame1`.
- **`cut`** — **plano nuevo** (otro encuadre, otro momento: de bodegón a manos, de manos a brindis). No lleva `CONTINUATION`; la consistencia la dan `@Image1` (botella) y la biblia de continuidad (misma luz, paleta y set). Es lo que permite reproducir la variedad de tomas de los videos del cliente.

El tramo 1 siempre es `cut`. La continuidad visual por referencia (capas de arriba) aplica a los tramos `continuation`; la biblia aplica a todos.

**Directiva `CONTINUATION` (obligatoria en todo tramo `continuation`, al inicio del prompt, después del formato).** Se entrega en la variante de la modalidad (c), la más compatible; sirve igual con (a) o (b):

```text
CONTINUATION FROM SEGMENT <N-1>: Starts exactly from @Frame1 (final frame of the previous segment) with no cut, no jump and identical lighting, lens, color palette, set and bottle design. Continue the camera movement seamlessly. Opening frame: <copia literal del exit_frame del tramo N-1>.
```

**Reglas por tramo:**

- Cada tramo es **autónomo**: lleva el orden canónico de §2.0 completo, sus beats con tiempos **relativos al tramo** (`0–3s`), su duración (`10 s` o `5 s`) y el **negative prompt íntegro** de §3.1 (+ §3.2 si hay líquido) en su casilla. Nunca "igual que el tramo anterior".
- Cada tramo describe aparte su **fotograma de salida** (`exit_frame`): posición de la botella y la copa, encuadre, luz y estado del líquido (en reposo, según §2.1). Si el tramo siguiente es `continuation`, ese texto abre su prompt.
- Evitar terminar un tramo a mitad de un vertido: la unión debe caer con el líquido en reposo o antes de que empiece a servirse.
- **Gancho** visual (primeros 2 s) en el tramo 1.
- **Ningún tramo pide texto en pantalla.** El tramo final deja la botella en héroe con el tercio inferior limpio; el tagline, las tarjetas de texto, el end card del logo y la leyenda `+18 · Evita el exceso · #EspírituDeOrigen` se montan en postproducción (§2.4).
- Sonido de cada tramo: solo ambiente y efectos (`ambient room tone and foley only, no music`). La música es un prompt aparte por video.
- El tramo de cierre de 5 s (video de 45 s) es un plano de remate: botella en héroe con espacio limpio para el end card. Sin acción nueva.

### 2.4 Postproducción (obligatoria en todo video)

Cada video se entrega con un bloque de postproducción que el usuario monta en el editor (Premiere, CapCut, DaVinci):

- **Orden de montaje:** tramos en orden, con sugerencia de puntos de corte (1.5–3 s por toma, `videos-cliente.md` §2.1).
- **Tarjetas de texto en pantalla** con tiempos: una frase partida en 4–5 tarjetas cortas, en español, coherente con el copy.
- **End card:** logo oficial «Loco» rojo sobre negro, 2–3 s, al final.
- **Leyenda obligatoria:** `+18 · Evita el exceso · #EspírituDeOrigen`, visible en el montaje final (sobre el último tramo o en el end card). Es un guardrail no negociable: los videos reales del cliente la omiten y eso es una falla.
- **Música:** la pista del prompt musical, de la duración total, resolviendo en el end card.

## 3. Negative prompt base (obligatorio, literal)

### 3.1 Base Universal (Imagen y Video — Incluye Anti-Tipografía Basura, Anti-Textos Gigantes, Anti-Procesos de Producción y Anti-Alucinaciones Culinarias)
```text
underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, generic liquor bottle, cylindrical bottle, round wine bottle, paper label, sticker label, white outline, white stroke, white border, sticker border, decal halo, die-cut sticker edge, paper decal, pasted logo, sticker decal, stroked typography, border around letters, screw cap, flat base, thin glass, painted ceramic decanter, food without plate, unplated food, ceramic decanter, hand-painted pattern, old-fashioned glass, ice cubes, salt rim, lime wedge on rim, shot glass, tequila production process, harvesting agave, jimador, jiming agave, industrial distillery, cooking ovens, brick ovens, industrial machinery, tahona stone, fermentation vats, distillation stills, factory workers, text watermark, blurry, low resolution, gibberish text, misspelled words, garbled letters, typo, scrambled typography, fake writing, illegible labels, deformed text, pseudo-letters, nonsense words, oversized text, giant red lettering, large red typography, clunky font, massive font size
```

### 3.2 Descriptores Anti-Viscosidad y Anti-Carbonatación (OBLIGATORIO para todo prompt de video con líquidos o servido)
Se suma de forma mandatoria a la base universal en prompts de video de producto:
```text
viscous, viscosity, syrupy, honey, honey-like pour, thick fluid, gelatinous, molasses, oil, oily texture, motor oil, heavy sluggish liquid, gooey, slime, slow-motion goo, sticky syrup, lingering froth, soapy foam, bottom emitters, continuous bubbles from bottom, effervescent trail, unnatural CGI gel, carbonation, carbonated, effervescent, effervescence, fizzy, fizz, bubbles, bubbly, sparkling, sparkling wine, champagne, cider, apple cider, beer, beer head, ale, lager, fermented beverage, brewed beverage, cloudy liquid, hazy liquid, central darkening, shot glass, caballito, tumbler, flute glass, champagne flute
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
