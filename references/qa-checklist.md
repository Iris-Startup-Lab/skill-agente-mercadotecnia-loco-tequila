# Checklist de QA antes de publicar — sección 11

Toda pieza adaptada debe pasar este checklist antes de considerarse entregada.

**Cómo se ejecuta:** es una autoverificación **interna** del paso 10. No genera preguntas al usuario. Si un ítem falla, el agente **corrige por su cuenta y vuelve a verificar**; el usuario ya confirmó los parámetros en los pasos 1–6 y completar un campo faltante es trabajo del agente, no una decisión de negocio. Solo se escala al usuario si la corrección exigiría inventar un hecho de marca o cambiar un parámetro que él eligió.

## Estilo de la respuesta (audiencia no técnica)

Se verifica sobre el texto que verá el usuario, antes de enviarlo.

- [ ] Toda la respuesta está **en español**; no quedó ninguna frase en inglés.
- [ ] **No hay narración del proceso interno ni de la fontanería de herramientas** (nada de "voy a revisar si existe", "el comando anterior falló porque", "let me install…"). Solo resultados.
- [ ] Los fallos técnicos están expresados como **consecuencia** ("las fechas salen del calendario estático"), no como traceback, módulo faltante ni comando fallido.
- [ ] **No se le pidió al usuario ejecutar código, instalar nada ni abrir una terminal.** Si algo había que ejecutar, lo ejecutó el agente.
- [ ] **No se alegó ninguna limitación propia inexistente.** Si algo no se pudo hacer, la causa declarada es concreta y verificable (falta un dato, el script falló, el usuario declinó), no un impedimento genérico.

## Marca, copy y cumplimiento

- [ ] La pieza pasa el filtro de Locura Genial (columna "ES", no "NO ES").
- [ ] **Regla «Anti-Novela» (Prohibición de Prosa Poética Barroca):** El copy NO es un relato novelesco ni prosa poética extendida sobre el tiempo o el más allá. Su extensión es concisa y afilada: 2 a 3 oraciones contundentes (35 a 50 palabras para feed de Instagram/Facebook; 1 sola línea para Stories y TikTok). Cero párrafos de novela.
- [ ] **Gancho Frontal (<125 caracteres):** La primera línea atrapa al instante antes del botón «...más / ver más».
- [ ] **Anclaje Ineludible en los 3 Pilares:** El copy se fundamenta en la tríada oficial: *Radical Authenticity* (terruño de El Arenal, sin aditivos), *Transcendent Creativity* (arte contemporáneo, Jan Hendrix, botella como escultura) y *Locura Genial* (obsesión por la perfección), no en metáforas poéticas trilladas.
- [ ] **Tono Magnético vs. Sentimental:** Es audaz, contemporáneo, impecable y de una elegancia desafiante; cero cursilería, timidez o nostalgia soñadora.
- [ ] El copy fue reescrito para la gramática nativa de la plataforma (no es un corte de Instagram).
- [ ] Se usaron los términos del glosario maestro sin variaciones libres.
- [ ] Incluye +18 / mensaje de consumo responsable donde aplica.
- [ ] Formato técnico (aspecto, duración) corresponde a la plataforma.
- [ ] CTA es coherente con el propósito de la plataforma (no vender directo en LinkedIn/TikTok).
- [ ] El mensaje de marca ("Espíritu de Origen", terruño, El Arenal) sigue siendo identificable.
- [ ] La pieza es consistente con al menos una persona (Alejandro / Ana / Leonardo) o el efecto halo.
- [ ] Si hay pauta paga, la segmentación de edad/alcohol está configurada según política de la plataforma.
- [ ] Los datos usados son verificados o están marcados (`[no disponible]`, `*` para estimaciones, `[REFERENCIA DE INDUSTRIA]` para benchmarks sin dato propio).
- [ ] La fecha festiva anclada es real y está correctamente nombrada (feriados detectados por la sub-skill o `references/fechas-alcohol.md`).
- [ ] El producto elegido es coherente con la campaña y usa sus keywords específicas (`references/productos.md` + glosario 10.4).
- [ ] **Consulta de Referencias Previas:** Se preguntó siempre al usuario ofreciendo las 4 modalidades completas: (1) link de nube (OneDrive/SharePoint/GoogleDrive) + alcance, (2) ruta de carpeta local/cowork en disco, (3) 1 a 3 imágenes propias adjuntas en el chat, o (4) ninguna para inspirarse en el acervo canónico integrado en la skill.
- [ ] Si se revisaron piezas previas (Word de análisis en OneDrive/SharePoint, Google Drive, carpeta local/cowork o imágenes adjuntas), la pieza no repite diseños anteriores.
- [ ] **Ningún prompt nuevo reutiliza texto del §4 (Prompt maestro) ni del §6 (Variantes) de un Word previo** — ni entero ni por fragmentos. Se hereda el ADN, nunca la redacción.
- [ ] **Ningún elemento de la lista INCIDENTAL** de las piezas revisadas reaparece en la campaña nueva (objeto de apoyo, fondo concreto, ángulo específico).
- [ ] Ninguna línea marcada `[INFERIDO]` en un Word de análisis se usó como hecho de marca.
- [ ] Se declaró el alcance de la revisión (10 más recientes o rango de fechas) y qué piezas quedaron dentro.
- [ ] **Se leyó el contenido de cada Word, no solo su nombre de archivo.** Para cada documento usado se reconoció al menos el encabezado §3; los que no se pudieron leer están reportados como no leídos.
- [ ] Ningún ADN ni INCIDENTAL fue inferido del nombre del archivo ni copiado por analogía de otro documento.

## Cumplimiento Regulatorio y Algorítmico IA 2026 (`references/manual-cumplimiento-ia-2026.md`)

- [ ] **Clasificación de Riesgo:** La pieza está clasificada correctamente (Nivel 1 Asistencia vs. Nivel 2 Sintético Realista).
- [ ] **Autodivulgación / Toggles en Pauta:** Para contenidos visuales Nivel 2, se incluye la indicación operativa de activar el toggle en Ads Manager ("AI Info" en Meta, "Contenido sintético" en YouTube Studio, "AIGC" en TikTok) para prevenir desmonetización o supresión de alcance (-80%).
- [ ] **FTC 16 CFR Part 465 (Veracidad):** Cero testimonios ficticios de consumidores inventados con IA, ni avatares haciéndose pasar por expertos sin respaldo real.
- [ ] **LinkedIn Anti-Slop (Algoritmo 360Brew):** En LinkedIn, el copy evita frases trilladas de IA genérica, exceso de viñeteado y oraciones clónicas; incorpora perspectiva humana, anécdotas de terruño y datos reales de Loco Tequila para no sufrir penalización de alcance (-30%) ni desvío exclusivo a red de 1er grado.
- [ ] **Fidelidad Física del Producto:** La descripción del producto en el prompt respeta al 100% la anatomía física oficial de `references/loco-tequila/` y `references/brand-context.md` (silueta cónica, base de cristal macizo de 2 cm, cápsula codificada por color y serigrafía vítrea en relieve sin etiquetas de papel) y los estándares de cristalería de `references/old_campaigns/`.
- [ ] **Cero Procesos de Creación de Tequila:** Salvo petición explícita del cliente, la pieza NO muestra faenas de jima, jimadores, hornos de mampostería, piedra tahona, tinas de fermentación, alambiques de destilación ni operarios industriales (`references/brand-context.md` §9).
- [ ] **Coherencia Escenográfica por Producto:** El registro visual corresponde a la expresión seleccionada según `references/brand-context.md` §8 (Blanco en diseño/terrazas; Ámbar en terruño al atardecer; Puro Corazón en lifestyle aspiracional; Áureo en biblioteca/arte/intelecto; Hierofante en espacio cósmico/plateado).
- [ ] **Sentido Común Visual y Vajilla Gastronómica (`references/evaluacion-sentido-comun-escena.md`):** Si hay comida (chiles en nogada, mole, etc.), está explícitamente emplatada en vajilla artesanal de alta gama (cerámica, gres, porcelana mate), NUNCA servida directamente sobre la mesa o piedra. La copa Riedel tiene punto de apoyo estable con sombras de contacto reales.

## Campos obligatorios de cada prompt (`references/prompt-standards.md` §1)

No son preguntas de sí/no: se lee el prompt y se confirma que la cadena **contiene** cada elemento. Si falta alguno, se reescribe el prompt en silencio.

- [ ] **Sujeto (Fidelidad Anatómica y Jerarquía Tipográfica):** nombra el SKU exacto del portafolio, cristalería oficial (copa Riedel grabada), rasgos físicos de botella oficial y jerarquía tipográfica real: solo `"Loco"` en relieve rojo con fino filete plateado; textos secundarios `"ESPIRITU • ORIGEN"` y `"TEQUILA {SKU} 100% DE AGAVE AZUL"` en tipografía pequeña, sutil y discreta en blanco/plata cerca de la base, sin letras rojas gigantes ni microtextos legales (`prompt-standards.md` §1.1). Incluye la directiva multimodal `ADD: The added image is the real bottle image. PRESERVE EXACT BOTTLE MORPHOLOGY...` (§1.2), el bottle-lock canónico (§1.4) y vajilla si hay comida (§1.5).
- [ ] **Lente y encuadre:** contiene distancia focal `Nmm` y apertura `f/N`, más tipo de plano.
- [ ] **Iluminación:** nombra explícitamente la condición de luz (hora del día o esquema de estudio).
- [ ] **Paleta institucional:** contiene al menos **2** colores de marca por nombre (cochineal crimson, deep wine, bone-ivory, obsidian black, volcanic silver).
- [ ] **Estilo visual:** referencia fotográfica o artística concreta, no adjetivos genéricos ("lujoso", "alta calidad" no cuentan).
- [ ] **Relación de aspecto:** parámetro `--ar` explícito.
- [ ] **Negative prompt:** incluye íntegra la cadena base de `prompt-standards.md` §3.1 (incluyendo anti-botellas genéricas, anti-comida sin plato, anti-procesos de producción de tequila, anti-cerámica folclórica, anti-tipografía basura y anti-textos gigantes) y §3.2 para video.
- [ ] **Anclaje de fecha:** la fecha festiva aparece como elemento concreto de escena, no como mención abstracta.
- [ ] El prompt corresponde al medio elegido (`{{medio}}`) y a la plataforma destino.
- [ ] Si `{{medio}}` incluye video: el prompt tiene desglose por escena con marcas de tiempo, movimiento de cámara y duración total.
- [ ] **Física de fluidos en video (Anti-Viscosidad):** Si el video muestra servido o líquido en movimiento, incluye obligatoriamente descriptores de ultrabaja viscosidad (`water-thin fluid dynamics`, `~1.2 cP`, flujo laminar veloz, microgotas cristalinas) y el negative prompt anti-viscosidad (`prompt-standards.md` §3.2: `viscous, syrupy, honey, molasses, oil, gelatinous`).
- [ ] Las keywords SEO/GEO están en el copy, **no** dentro del prompt de imagen.
- [ ] El total de conceptos no excede 6; si se recortó `{{numero_ideas}}`, está declarado en las notas.

## Entregable de la Pasarela Web (`references/showcase-rules.md`)

Este bloque **no se satisface marcando casillas**: son acciones con rastro comprobable. Si el archivo no existe, la entrega no está terminada.

- [ ] Existe el archivo `showcase/campaign-<fecha>-<slug>.html` en disco.
- [ ] Se generó copiando el template y sustituyendo **solo** el bloque `const CAMPAIGN = {…}` (no se reescribió el HTML/CSS completo).
- [ ] `CAMPAIGN.items` contiene **todos** los conceptos entregados en el markdown, con el prompt completo en `prompt.text`.
- [ ] **Si `{{medio}}` es video o ambas: cada concepto tiene `prompt_video` poblado** (con `duration`, `camera_movement` y `scenes[]`). Sin ese objeto el prompt de video no aparece en la pasarela, aunque sí esté en el markdown.
- [ ] Si `{{medio}}` es solo video, se omitió el objeto `prompt` en lugar de dejarlo vacío (la etiqueta de la pestaña debe leerse `VID`, no `IMG+VID`).
- [ ] El logo va como data-URI base64 (`showcase/assets/logo_base64.txt`), no como ruta relativa al SVG de 2.2 MB.
- [ ] Se publicó con la herramienta `Artifact` y el link se entregó al usuario — o, si la herramienta no está disponible, se informó la ruta del archivo escrito.

## Solo si se generaron piezas con OpenRouter (paso 12b)

Este bloque **no aplica** si el usuario no pidió el extra. Si lo pidió, todos son obligatorios.

- [ ] El usuario **pidió explícitamente** generar las piezas. No se generó por iniciativa propia.
- [ ] **El script lo corrió el agente.** No se le pidió al usuario ejecutarlo, ni se le ofreció "una guía para su terminal" como alternativa.
- [ ] Los prompts se leyeron de la pasarela con `--action extract-prompts`. **Ninguno se reescribió de memoria ni a mano.**
- [ ] El modelo salió del catálogo en vivo (`--action list-models`), no de memoria.
- [ ] Se corrió `--dry-run` y **se le mostró el costo estimado al usuario antes de gastar**.
- [ ] La cantidad generada respeta el techo real (`max_imagenes` / `max_videos`), no el total de conceptos.
- [ ] Si el medio fue "ambas": se generaron **primero las imágenes** y después los videos.
- [ ] Cada pieza se entregó con **las tres cosas**: archivo, copy de la pasarela y prompt + especificaciones.
- [ ] **Todo aviso del script se trasladó al usuario** (`aviso_duracion`, `aviso_aspect_ratio`, `aviso_costo`, `aviso_catalogo`). Ningún recorte de duración o de aspecto quedó sin declarar.
- [ ] Cada pieza generada se revisó contra los guardrails de marca; las que los violan se descartaron y se dijo por qué.
