# Checklist de QA antes de publicar — sección 11

Toda pieza adaptada debe pasar este checklist antes de considerarse entregada.

**Cómo se ejecuta:** es una autoverificación **interna** del paso 10. No genera preguntas al usuario. Si un ítem falla, el agente **corrige por su cuenta y vuelve a verificar**; el usuario ya confirmó los parámetros en los pasos 1–6 y completar un campo faltante es trabajo del agente, no una decisión de negocio. Solo se escala al usuario si la corrección exigiría inventar un hecho de marca o cambiar un parámetro que él eligió.

## Marca, copy y cumplimiento

- [ ] La pieza pasa el filtro de Locura Genial (columna "ES", no "NO ES").
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
- [ ] Si se revisaron piezas previas (Word de análisis en OneDrive/SharePoint), la pieza no repite diseños anteriores.
- [ ] **Ningún prompt nuevo reutiliza texto del §4 (Prompt maestro) ni del §6 (Variantes) de un Word previo** — ni entero ni por fragmentos. Se hereda el ADN, nunca la redacción.
- [ ] **Ningún elemento de la lista INCIDENTAL** de las piezas revisadas reaparece en la campaña nueva (objeto de apoyo, fondo concreto, ángulo específico).
- [ ] Ninguna línea marcada `[INFERIDO]` en un Word de análisis se usó como hecho de marca.
- [ ] Se declaró el alcance de la revisión (10 más recientes o rango de fechas) y qué piezas quedaron dentro.
- [ ] **Se leyó el contenido de cada Word, no solo su nombre de archivo.** Para cada documento usado se reconoció al menos el encabezado §3; los que no se pudieron leer están reportados como no leídos.
- [ ] Ningún ADN ni INCIDENTAL fue inferido del nombre del archivo ni copiado por analogía de otro documento.

## Campos obligatorios de cada prompt (`references/prompt-standards.md` §1)

No son preguntas de sí/no: se lee el prompt y se confirma que la cadena **contiene** cada elemento. Si falta alguno, se reescribe el prompt en silencio.

- [ ] **Sujeto:** nombra el SKU exacto del portafolio y su cristalería.
- [ ] **Lente y encuadre:** contiene distancia focal `Nmm` y apertura `f/N`, más tipo de plano.
- [ ] **Iluminación:** nombra explícitamente la condición de luz (hora del día o esquema de estudio).
- [ ] **Paleta institucional:** contiene al menos **2** colores de marca por nombre (cochineal crimson, deep wine, bone-ivory, obsidian black, volcanic silver).
- [ ] **Estilo visual:** referencia fotográfica o artística concreta, no adjetivos genéricos ("lujoso", "alta calidad" no cuentan).
- [ ] **Relación de aspecto:** parámetro `--ar` explícito.
- [ ] **Negative prompt:** incluye íntegra la cadena base de `prompt-standards.md` §3 (menores, embriaguez, cristalería barata, botellas de competidores, watermark, baja resolución).
- [ ] **Anclaje de fecha:** la fecha festiva aparece como elemento concreto de escena, no como mención abstracta.
- [ ] El prompt corresponde al medio elegido (`{{medio}}`) y a la plataforma destino.
- [ ] Si `{{medio}}` incluye video: el prompt tiene desglose por escena con marcas de tiempo, movimiento de cámara y duración total.
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
