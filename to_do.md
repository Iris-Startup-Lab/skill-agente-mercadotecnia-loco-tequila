# Bitácora de Tareas y Mejoras Realizadas (`to_do.md`)

Este documento registra de forma pormenorizada las tareas implementadas para elevar la calidad, rigor técnico, cumplimiento normativo y directrices de arte en la skill `agente-mercadotecnia-loco-tequila`.

---

## 📋 Resumen de Tareas Ejecutadas

- [x] **Tarea 1: Integración del Manual de Cumplimiento IA 2026**
  - Se incorporó `references/manual-cumplimiento-ia-2026.md` como fuente de verdad en `SKILL.md`, `references/prompt-standards.md` y `references/qa-checklist.md`.
  - Implementación de la Taxonomía de Tres Niveles de Riesgo (Nivel 1 Asistencia, Nivel 2 Sintético Realista, Nivel 3 Prohibido/Engañoso).
  - Reglas de autodivulgación en pauta publicitaria (toggles obligatorios en Meta Ads Manager "AI Info", YouTube Studio "Contenido sintético", TikTok "AIGC") para prevenir desmonetización o supresiones algorítmicas de alcance (-80%).
  - Normas anti-slop para superar el filtro del algoritmo 360Brew de LinkedIn (LLaMA-3 150B): redacción con anécdotas reales de terruño, voz humana auténtica, erradicación de viñeteado excesivo y frases clónicas de IA.
  - Apego estricto a las regulaciones de la FTC (16 CFR Part 465) y EU AI Act (Art. 50): prohibición tajante de testimonios o reseñas de consumidores ficticios generados por IA.

- [x] **Tarea 2: Detección y Canon Anatómico de Botellas Oficiales (`references/loco-tequila/`)**
  - Análisis de las imágenes oficiales de producto en `references/loco-tequila/bottle_tequila_offiicial_images/` para Loco Blanco, Loco Ámbar, Loco Puro Corazón, Loco Áureo y Loco Hierofante.
  - Detección de la geometría escultórica: prisma cónico / trapezoidal de base sólida y ancha de cristal macizo de 2.0 a 2.5 cm de espesor (*heavy glass base*), cuello alargado y esbelto, y ausencia total de etiquetas de papel adhesivo.
  - Esmaltado vítreo vitrificado al fuego directo en el cristal con el logotipo caligráfico "Loco" en Rojo Grana Cochinilla (`#A6192E`).
  - Código cromático de cápsulas metálicas de cuello: Rojo Cochinilla con rombo blanco (Blanco), Bronce/Cobre con rombo oro viejo (Ámbar), Plata/Blanco perla (Puro Corazón), lacre negro/dorado (Áureo) y decantadores escultóricos de Jan Hendrix (*Luminis* y *Umbra*) para Hierofante.
  - Actualización y enriquecimiento del documento maestro [resumen_bottle_tequila_offiicial_images.md](references/loco-tequila/bottle_tequila_offiicial_images/resumen_bottle_tequila_offiicial_images.md).

- [x] **Tarea 3: Análisis Visual y Resúmenes de Campañas Históricas (`references/old_campaigns/`)**
  - Inspección de todas las imágenes de campañas previas en las subcarpetas temáticas y redacción de resúmenes en formato `.md` de alta fidelidad:
    1. [resumen_Dia_de_muertos.md](references/old_campaigns/Dia_de_muertos/resumen_Dia_de_muertos.md): Análisis de instalación floral monumental de cempasúchil con caligrafía de "Loco" en flores magentas de celosía, pencas de agave en abanico, suelo de tierra volcánica negra, pedestales de basalto y velas votivas de cera natural.
    2. [resumen_Loco_tequila_ambar.md](references/old_campaigns/Loco_tequila_ambar/resumen_Loco_tequila_ambar.md): Estilo de vida costero en Chileno Bay (Los Cabos), albercas infinity, barras de mixología de lujo (Fifty Mils Four Seasons), cócteles con hielo cristalino y guarnición de romero quemado.
    3. [resumen_Loco_tequila_blanco.md](references/old_campaigns/Loco_tequila_blanco/resumen_Loco_tequila_blanco.md): Arquitectura brutalista de alberca interior de hormigón aparente con ventanales a bosque lluvioso, terrazas con azulejería hidráulica artesanal y cóctel de autor "Frutos Locos" con lámpara de esfera opalina.
    4. [resumen_Loco_tequila_puro_corazon.md](references/old_campaigns/Loco_tequila_puro_corazon/resumen_Loco_tequila_puro_corazon.md): Atelier de calzado a medida y marroquinería de Adriana Soto con pieles curtidas y hormas de madera, biblioteca con monografía fotográfica *Giacomo Brunelli: New York*, y maridaje desenfadado de tacos Baja en plato de peltre blanco.
    5. [resumen_Mexicanidad.md](references/old_campaigns/Mexicanidad/resumen_Mexicanidad.md): Maridaje estelar con Chiles en Nogada tradicionales en colaboración con el chef Ángel Vázquez, bodegones con platos festoneados negros y barro vidriado, estuche de colección de madera de barricas y mesa formal de cata con minutas rojas, cloches de cristal y tapas aromatizadoras oficiales para copas Riedel.
    6. [resumen_old_campaigns.md](references/old_campaigns/resumen_old_campaigns.md): Memoria visual y directriz de dirección de arte transversal en la raíz de la carpeta.
  - Vinculación formal de todas las referencias nuevas en [SKILL.md](SKILL.md) y [README.md](README.md).

- [x] **Tarea 4: Automatización de Empaquetado Limpio (`package_skill.ps1` y `package_skill.sh`)**
  - Creación de scripts para empaquetar la skill en `agente-mercadotecnia-loco-tequila.zip`.
  - Exclusión selectiva estricta: se omiten archivos de imagen binarios en `references/` (`*.png`, `*.jpg`, `*.jpeg`), respetando y empaquetando íntegramente todos los archivos `.md` descriptivos recién creados.
  - Exclusión de directorios de desarrollo y temporales (`.git`, `outputs/`, `__pycache__`, `.vscode`).
  - **Verificación automática de límites desempaquetados (< 30 MB y <= 200 archivos):** los empaquetadores calculan y auditan el peso total descomprimido (actualmente **4.86 MB**) y la cantidad de archivos (actualmente **57 archivos**), abortando la ejecución con error si se excede el umbral de 30 MB o el máximo de 200 archivos por ZIP requerido por gestores de skills.
  - Verificación y validación de integridad del empaquetado.

- [x] **Tarea 5: Calendario Gastronómico Mexicano y Consulta Interactiva de Motivo Culinario**
  - Creación del documento [calendario-gastronomico-mexicano.md](references/calendario-gastronomico-mexicano.md) con fundamentación documental completa y citación explícita de:
    - *Wikipedia:* [https://es.wikipedia.org/wiki/Gastronom%C3%ADa_de_M%C3%A9xico](https://es.wikipedia.org/wiki/Gastronom%C3%ADa_de_M%C3%A9xico) (Declaratoria UNESCO 2010, Milpa, nixtamalización y mestizaje virreinal).
    - *SIC Gob Ficha 45:* [https://sic.gob.mx/ficha.php?table=gastronomia&table_id=45](https://sic.gob.mx/ficha.php?table=gastronomia&table_id=45) (Calendario ritual oficial: Reyes, Candelaria, Carnaval, Cuaresma, Santa Cruz, Corpus Christi, Fiestas Patrias, Día de Muertos, Guadalupe, Posadas, Navidad).
  - Elaboración de matriz de maridaje de alta gama para el portafolio Loco Tequila (Blanco, Ámbar, Puro Corazón, Áureo, Hierofante).
- [x] **Tarea 6: Estandarización de Física de Fluidos Anti-Viscosidad para Video**
  - Identificación del sesgo por defecto en modelos generativos de video (Sora, Kling, Runway, Veo) hacia fluidos espesos, densos o almibarados al servir líquidos.
  - Actualización de [prompt-standards.md](references/prompt-standards.md) (§2.1 y §3.2) con parámetros de hidrodinámica real para tequila 40% ABV: ultrabaja viscosidad similar al agua (~1.2 a 1.4 mPa·s), flujo laminar de alta velocidad, rompimiento en microgotas cristalinas, rápida atenuación de turbulencia y ausencia de espuma o texturas aceitosas.
- [x] **Tarea 7: Consulta Tripartita de Referencias Visuales (Paso 5 de SKILL.md)**
  - Unificación de la pregunta obligatoria de referencias previas ofreciendo tres vías equivalentes en la misma consulta: (a) Link de carpeta OneDrive/SharePoint con alcance, (b) 1 a 3 imágenes propias adjuntas en el chat de muestra para inspirarse, o (c) Ninguna para omitir referencias y avanzar directamente.
  - Actualización del Paso 5 en [SKILL.md](SKILL.md).
  - Actualización del Principio 5 y del diagrama de secuencia Mermaid en [AGENTS.md](AGENTS.md).
- [x] **Tarea 8: Estandarización Tipográfica Anti-Alucinaciones en Botellas (Anti-Typos & Micro-textos)**
  - Detección de la causa raíz de deformaciones tipográficas y faltas de ortografía en modelos de difusión (p. ej. *"BLANEO"*, *"ACWE A20L"*, letras inventadas): saturación de microtextos legales (750ml, % alc, NOM) que agotan la capacidad latente del modelo.
  - Creación de la regla canónica de tres líneas en comillas dobles en [prompt-standards.md](references/prompt-standards.md) (§1.1):
    1. `"Loco"` (logotipo caligráfico esmaltado en relieve rojo).
    2. `"ESPIRITU DE ORIGEN"` (eslogan institucional en mayúsculas).
    3. `"TEQUILA {SKU} 100% DE AGAVE AZUL"` (donde `{SKU}` se reemplaza dinámicamente por `BLANCO`, `AMBAR`, o `PURO CORAZON`).
  - Prohibición estricta de solicitar microtextos legales o tipografías minúsculas densas en las botellas generadas.
- [x] **Tarea 9: Escala Tipográfica Fina (Micro-jerarquía Blanca), Directiva Multimodal `ADD:` y Nota de Fidelidad**
  - Diagnóstico de contaminación cromática y desproporción tipográfica: evitar que los textos secundarios hereden el color rojo del logo o se generen en tamaños gigantescos y toscos.
  - Estandarización de la jerarquía visual real de la botella en [prompt-standards.md](references/prompt-standards.md) (§1.1):
    - Logotipo `"Loco"` como único elemento en relieve esmaltado rojo cochinilla con filete plateado de contorno.
    - Textos secundarios (`ESPIRITU • ORIGEN` y `TEQUILA {SKU} 100% DE AGAVE AZUL`) en tipografía diminuta, discreta y sutil en fino esmalte blanco cerca de la base maciza, manteniendo amplios espacios negativos de cristal transparente diáfano.
  - Implementación de la directiva multimodal estándar en §1.2:
    `ADD: The added image is the real bottle image, you could use it as an inspiration for the exact bottle geometry, crystal transparency, and small subtle typography placement.`
  - Inclusión de tokens anti-textos gigantes en negative prompt (§3.1): `oversized text, giant red lettering, large red typography, clunky font, massive font size`.
  - Actualización de la lista de verificación [qa-checklist.md](references/qa-checklist.md).
- [x] **Tarea 10: Compatibilidad Universal de Rutas en ZIP para Claude / Linux (Anti-Invalid Characters)**
  - Identificación del error `Zip file contains path with invalid characters` en Claude Desktop y Claude Web: el cmdlet nativo de Windows `Compress-Archive` empaquetaba las rutas internas con barras invertidas (`\`) propias del sistema de archivos de Windows (p. ej. `references\loco-tequila\...`).
  - El estándar oficial de compresión ZIP (PKWARE APPNOTE §4.4.17.1) y los entornos Unix/Linux de Claude exigen estrictamente barras diagonales (`/`) y rechazan `\` considerándolo un carácter inválido o riesgo de seguridad de directorio.
  - Reemplazo de `Compress-Archive` en [package_skill.ps1](package_skill.ps1) por la API .NET `System.IO.Compression.ZipArchive`:
    - Normalización forzada de todos los nombres de entrada sustituyendo `\` por `/`.
    - Codificación explícita de caracteres en `UTF-8`.
    - Omisión de carpetas vacías intermedias que generaban entradas redundantes con caracteres de escape.
  - Verificación exitosa de todas las entradas del archivo `.zip` generado.

- [x] **Tarea 11: Optimización de Física de Fluidos en Video (Anti-Carbonatación y Anti-Viscosidad) y Silueta Tulipán**
  - Erradicación de términos causantes del sesgo de carbonatación (`effervescent micro-bubbles`) en [prompt-standards.md](references/prompt-standards.md) (§2.1) y sustitución por superficie en reposo libre de burbujas, gas o espuma (`completely still, non-carbonated liquid surface immediately after impact — no bubbles of any kind, no fizz, no foam`).
  - Ampliación del negative prompt base (§3.2) con el bloque anti-carbonatación, anti-fermentados y anti-espumosos (`carbonation, carbonated, effervescent, fizz, bubbles, sparkling wine, champagne, cider, beer, flute glass, champagne flute`).
  - Reemplazo de la denominación comercial `flute` en los prompts positivos por la silueta morfológica precisa `narrow tulip-shaped crystal tasting glass with tapered rim (Riedel tequila glassware silhouette)` en [prompt-standards.md](references/prompt-standards.md) y [brand-context.md](references/brand-context.md), blindando con `flute glass` en el negative prompt.
  - Corrección de `curaduria-modelos-imagen.json`: ajuste del `settings_tip` y tags de Kling para solicitar velocidad real/normal en el vertido (evitando cámara lenta que falsee la viscosidad del destilado) y corrección en Sora eliminando referencias a procesos de producción prohibidos.
  - Documentación de la capacidad de referencia multimodal de video (§2.2): se integra la directiva opcional `MATCH POUR PHYSICS (OPTIONAL)`, estipulando de manera explícita que es **100% opcional y no obligatoria**.
  - Actualización consistente en [qa-checklist.md](references/qa-checklist.md), [evaluacion-sentido-comun-escena.md](references/evaluacion-sentido-comun-escena.md) y [sub-skill/evaluador-sentido-comun-visual/README.md](sub-skill/evaluador-sentido-comun-visual/README.md).
  - Verificación del script de empaquetado [package_skill.ps1](package_skill.ps1), confirmando total adaptabilidad (< 30 MB).

- [x] **Tarea 12: Especialización de Física de Fluidos en Vertido de Tequila en Copa Riedel para Video**
  - Especialización completa de [references/especificaciones-fluidos.md](references/especificaciones-fluidos.md) exclusivamente para Loco Tequila: erradicación de referencias a vino tinto y a vasos de shot/caballitos (prohibidos por el canon de marca).
  - Definición de los dos perfiles lumínicos y ópticos: Blanco/Puro Corazón (diamantino/plata, 100% incoloro, sin oscurecimiento central) y Ámbar/Áureo (dorado traslúcido, miel y cobre cálido sin sombras fangosas).
  - Regla Crítica Cero: desactivación absoluta de emisores de fondo (*Bottom Emitters OFF*) para anular cualquier efervescencia continua tipo sidra o refresco.
  - Dinámica de microburbujas mecánicas por choque con ciclo de vida ultracorto (<0.3 s) y estallido instantáneo al contacto con la atmósfera (cero espuma, cero halo residual en cristal).
  - Estabilización hidrodinámica a reposo superficial completo en menos de 1 a 1.5 segundos tras cesar el vertido de la botella.
  - Comportamiento en la copa Riedel Tequila: lágrimas finas, nítidas y transparentes de escurrimiento ágil (*thin tequila tears*).
  - Estructuración de las dos modalidades de entrada multimodal para video:
    1. Fotografía de botella oficial (Image-to-Video) con directiva `ADD: PRESERVE EXACT BOTTLE MORPHOLOGY`.
    2. Clip de muestra de vertido real (Video-to-Video) con directiva `MATCH POUR PHYSICS`.
    3. Respaldo autónomo textual por si el usuario no proporciona archivos.
  - Armonización transversal en [references/prompt-standards.md](references/prompt-standards.md) (§2.1, §2.2, §3.2), [SKILL.md](SKILL.md) (índice y paso 9), [references/qa-checklist.md](references/qa-checklist.md) y [references/evaluacion-sentido-comun-escena.md](references/evaluacion-sentido-comun-escena.md).
  - Reempaquetado del paquete `.zip` distribuible.

- [x] **Tarea 13: Videos Encadenados en Tramos de 10 Segundos**
  - Nueva pregunta obligatoria de duración de video (10, 20, 30, 45 o 60 s), una vez por campaña y solo si el medio incluye video: [AGENTS.md](AGENTS.md) §1.14 y diagrama, [CLAUDE.md](CLAUDE.md) §2.6, [SKILL.md](SKILL.md) paso 6b y [README.md](README.md).
  - Reparto de tramos: 10 s → 1, 20 s → 2, 30 s → 3, 45 s → 5 (4 × 10 s + cierre de 5 s), 60 s → 6.
  - Norma en [references/prompt-standards.md](references/prompt-standards.md) §2.3: video anterior como referencia principal (extender, video de referencia o último fotograma), biblia de continuidad repetida literal, directiva `CONTINUATION`, fotograma de salida, gancho en el tramo 1 y +18 en el último.
  - Plantilla de salida, checklist QA, reglas de la pasarela y matriz de plataformas actualizadas.
  - Pasarela ([references/showcase-template.html](references/showcase-template.html)): píldoras de tramo, línea de tiempo, referencia de entrada / fotograma de salida, copiar tramo y copiar todos. Retrocompatible con videos sin `segments`. Ejemplo Ámbar reescrito a 20 s en 2 tramos, sin procesos de producción.
  - Script OpenRouter ([generar_medios.py](sub-skill/generar-medios-openrouter/generar_medios.py)): cada tramo se genera por separado, `--segments`, `max_tramos_video` y `aviso_encadenado`.
  - Reempaquetado del `.zip` distribuible cumpliendo límites de peso (< 30 MB) y cantidad de archivos (<= 200 archivos).

- [x] **Tarea 14: Flexibilización de Referencias en la Nube (Con Link o Búsqueda Directa con Conector sin Link)**
  - Habilitación de la búsqueda directa en carpetas de OneDrive/SharePoint y Google Drive sin necesidad obligatoria de link URL, siempre y cuando el agente cuente con acceso activo al conector correspondiente (Microsoft 365 MCP o Google Drive MCP).
  - Si el conector no está disponible, el agente lo notifica con amabilidad y solicita el enlace directo o continuar con las demás alternativas.
  - Actualización de [AGENTS.md](AGENTS.md) (§1.5 y diagrama Mermaid), [SKILL.md](SKILL.md) (definición de `{{carpeta_referencias}}` y Paso 5a), [CLAUDE.md](CLAUDE.md) (§2.5), [sub-skill/leer-imagenes-onedrive/README.md](sub-skill/leer-imagenes-onedrive/README.md), [README.md](README.md), [FLUJO_SKILL_CLIENTE.md](FLUJO_SKILL_CLIENTE.md) y [references/qa-checklist.md](references/qa-checklist.md).

- [x] **Tarea 15: Lenguaje Audiovisual del Cliente, Música por Video y Prompts por Proveedor**
  - Nueva referencia [references/videos-cliente.md](references/videos-cliente.md): síntesis de 8 videos reales del cliente (ritmo de corte de 1.5–3 s, mezcla de tomas, apertura y cierre con logo rojo sobre negro, luz de vela, f/1.4–f/2.8, atrezo, personas adultas, texto en tarjetas) y los dos arquetipos musicales.
  - [references/prompt-standards.md](references/prompt-standards.md) §2.0–§2.4: orden canónico de lista de tomas, una acción por tramo, menciones `@`, botella rígida con una sola foto, tramos `cut` / `continuation`, versión completa + compacta (≤500 caracteres, confirmado por el usuario con la tabla de límites por proveedor), cero meta-texto y cero texto generado, bloque de postproducción.
  - Música por video: prompt instrumental aparte (arquetipo A Lounge 118–122 BPM o B Neoclásico 80–95 BPM), derechos `[no disponible]` ([AGENTS.md](AGENTS.md) §1.15).
  - `+18 · Evita el exceso` sale del último tramo y pasa a postproducción, obligatoria en el montaje final.
  - Pasarela: interruptor Completa / Compacta con contador, «Copiar Prompt» sin encabezados en español, «Copiar negativo», «Copiar guion completo», píldora 🎵 Música y caja ✂️ Postproducción. Ejemplo Ámbar reescrito.
  - Script OpenRouter: `--prompt-version`, `aviso_longitud`, música y postproducción expuestas en `extract-prompts`.
  - Se mantienen: negative prompt completo (en casilla aparte) y prohibición de hielo y vaso corto.
  - Pendiente: borrar `new_references_to_delete/`, confirmar con el cliente el estuche negro de Ámbar y el límite real de Dreamina, y reempaquetar el `.zip`.

