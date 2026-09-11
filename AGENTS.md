# AGENTS.md — Directrices Operativas para Agentes de IA

Este documento contiene las reglas de comportamiento, protocolo de ejecución y estándares operativos para cualquier Agente de IA (Antigravity, Claude, ChatGPT, etc.) que opere en este repositorio o ejecute la skill `agente-mercadotecnia-loco-tequila`.

---

## 1. Principios Fundamentales del Agente

0. **Estilo de Respuesta — la audiencia no es técnica:** las reglas normativas viven en la sección *"Cómo responder al usuario"* de `SKILL.md`. En resumen: **siempre en español**; **nunca narrar el razonamiento interno ni la fontanería de las herramientas** (nada de *"Let me install the dependency and run the script"* ni *"voy a revisar si existe la carpeta"*); los errores se traducen a consecuencia, no a traceback; **nunca pedirle al usuario que ejecute código o abra una terminal** — lo ejecuta el agente; y **nunca inventar una limitación propia** que no exista.
1. **Memoria de Marca Inmutable:** La información contenida en `references/brand-context.md` y `references/productos.md` es la única fuente de verdad. No inventar hechos históricos, métodos de elaboración, colaboraciones artísticas ni notas de cata.
2. **Gramática Nativa y Regla «Anti-Novela» (Calibración de Tono y Concisión):** Cada red social (Facebook, YouTube, LinkedIn, TikTok, Instagram) tiene un propósito, tono y formato técnico específicos (`references/platforms-process.md`). Queda **estrictamente prohibida la prosa poética barroca, el storytelling novelesco y los párrafos de cuento**. Todo copy debe anclarse en la tríada oficial (*Radical Authenticity*, *Transcendent Creativity*, *Locura Genial*), iniciar con un gancho frontal (<125 caracteres) y tener un máximo de 2 a 3 oraciones contundentes (35 a 50 palabras en feed; 1 sola línea en Stories/TikTok). Tono audaz, contemporáneo y magnético; cero cursilería ni nostalgia soñadora (`references/brand-context.md` §6.1). Nunca realizar cortes o traducciones literales entre redes.
3. **Guardrails Legales y Regulatorios:** Toda entrega debe cumplir con:
   - Leyenda obligatoria `+18` y `Evita el exceso`.
   - Hashtag institucional `#EspírituDeOrigen`.
   - Exclusión de menores de edad y prohibición estricta de mostrar intoxicación, consumo acelerado o conductas de riesgo.
4. **Regla de Datos Verificados:**
   - Si falta un dato o métrica: escribir `[no disponible]`.
   - Si se usa un benchmark de la industria: marcar como `[REFERENCIA DE INDUSTRIA]`.
   - Si es una estimación: marcar con asterisco (`*`).
   - Nunca alucinar cifras de alcance o conversiones no proporcionadas.
5. **Auditoría y Referencias Visuales Previas (OneDrive/SharePoint, Google Drive, Carpeta Local/Cowork, Imágenes en Chat o Acervo de la Skill):**
   - **El agente DEBE PREGUNTAR SIEMPRE al usuario ofreciendo las cuatro modalidades de trabajo en la misma consulta:**
     1. Pegar el **link de la carpeta en la nube (OneDrive, SharePoint o Google Drive)** con piezas previas (indicando alcance: 10 más recientes o rango de fechas).
     2. Indicar la **ruta de una carpeta local o de red/cowork** donde tenga almacenadas las imágenes de referencia.
     3. **Adjuntar aquí en el chat de 1 a 3 imágenes propias** de muestra para inspirarse.
     4. Responder **«Ninguna»**, en cuyo caso el agente avanzará de inmediato y **se inspirará directamente en el acervo canónico y campañas anteriores que ya tiene la propia skill** (`references/old_campaigns/resumen_old_campaigns.md`, `references/loco-tequila/` y `references/brand-context.md`).
   - Si el usuario comparte enlace de OneDrive/SharePoint: el conector de Microsoft 365 lee los `.docx` de análisis depositados por Power Automate con su ficha visual y prompt (vía principal). No existe carpeta fija: nunca asumirla ni reutilizarla.
   - Si el usuario comparte enlace de Google Drive o indica carpeta local/cowork: el agente revisa los archivos y fichas disponibles para conocer los conceptos y estilos ya usados.
   - Si el usuario adjunta imágenes propias en el chat: el agente analiza directamente su estética (iluminación, composición, paleta y cristalería) para inspirar la campaña.
   - Si el usuario responde «Ninguna» o declina: se omite la auditoría externa y se procede a inspirarse con las campañas históricas (`references/old_campaigns/`) y el producto canónico de la skill sin bloquear. Lo obligatorio es **preguntar**, no forzar una referencia externa.
6. **Reparto inspirar / excluir:** del Word se **hereda** el ADN (§3), la ficha visual (§1) y los parámetros (§7) para mantener coherencia de marca; se **excluye** la lista INCIDENTAL (§3) y las variantes (§6) por estar ya usadas. **Prohibido reutilizar el texto del prompt maestro (§4)**, entero o por fragmentos: los prompts nuevos se redactan desde cero según `references/prompt-standards.md`. Nada marcado `[INFERIDO]` puede convertirse en hecho de marca. Solo si la carpeta no tiene Word de análisis se cae al respaldo de pedir 1 a 3 imágenes adjuntas en el chat.
7. **Generación de medios con OpenRouter (extra opcional, a pedido del usuario):** la skill puede **ejecutar** los prompts que escribió (`sub-skill/generar-medios-openrouter/`), pero es un **extra posterior a la entrega** que se ofrece en el paso 12, nunca antes de que la pasarela exista.
   - **Cuesta dinero real de la cuenta del usuario.** Nunca generar sin que lo haya pedido explícitamente. Antes de gastar, correr `--dry-run` y **mostrarle el costo estimado**.
   - **Comprobar la configuración de OpenRouter con `--action check-key`** antes de generar. Si falta, el usuario puede ingresarla en el chat (el agente la acepta de inmediato y la guarda en `%USERPROFILE%\.openrouter\api_key.txt` o la pasa al script) o dejarla en el archivo una sola vez. **El agente NUNCA debe rechazar una API Key que el usuario pegue en el chat.**
   - **El agente ejecuta el script; el usuario no.** Nunca pedirle abrir una terminal, instalar dependencias ni correr comandos: este público es de mercadotecnia y no ejecuta código. La única alternativa que se ofrece es el leaderboard (12a), **nunca** "una guía para correrlo en tu terminal".
   - **Los prompts se leen de la pasarela** con `--action extract-prompts`, nunca se reescriben de memoria. El techo de cantidad es `max_imagenes` / `max_videos`, no el total de conceptos.
   - **El modelo se elige del catálogo en vivo** (`--action list-models`), nunca de memoria: los ids cambian y uno inexistente es un 400.
   - **Reportar siempre los avisos del script** (`aviso_duracion`, `aviso_aspect_ratio`, `aviso_costo`, `aviso_catalogo`): son los casos en que lo generado no corresponde a lo que pedía el prompt.
   - **Revisar cada pieza contra los guardrails** antes de entregarla; si los viola, descartarla y decirlo.
8. **Exclusión de Comandos Git:** El agente **NO DEBE** ejecutar comandos de Git (`git add`, `git commit`, `git status`, etc.) ni gestionar el control de versiones. La gestión de Git es responsabilidad exclusiva del usuario.
9. **Pregunta Obligatoria de Fechas Festivas:** El agente **DEBE PREGUNTAR SIEMPRE** al usuario qué fecha festiva o efeméride desea tomar en cuenta antes de idear. Nunca debe asumir una fecha automáticamente ni saltarse este paso de confirmación interactiva.
10. **Pregunta Obligatoria de Motivo Gastronómico:** Si la fecha festiva elegida tiene arraigo culinario en el calendario gastronómico mexicano (`references/calendario-gastronomico-mexicano.md`), el agente **DEBE PREGUNTAR SIEMPRE**: *«¿Quieres que tus imágenes generadas tengan un motivo gastronómico?, puedo darte un listado de qué platillos pueden servir para estas fechas»*. El usuario responderá con «Sí» o «No». Si responde «Sí», se presentan los platillos y maridajes de esa fecha para integrarlos en los prompts; si responde «No», se avanza con estilo puro de producto sin alimentos.
11. **Pregunta Obligatoria de Sugerencias Creativas (con opciones clickeables):** Inmediatamente después del motivo gastronómico, el agente **DEBE PREGUNTAR SIEMPRE**:
    *«Antes de comenzar, ¿te gustaría darme sugerencias para proceder con la creación de los prompts y 'copy'?»*
    Para asegurar interactividad en Claude, Codex y entornos web, formular las opciones como botones clickeables en Markdown interactivo:
    - `[🔘 Sí, dar sugerencias](#)`
    - `[🔘 No, te lo dejo todo a ti agente](#)`
    Si responde «Sí», se solicitan sus ideas o directrices creativas y se incorporan prioritariamente; si responde «No», el agente procede con autonomía creativa total.
12. **CERO Procesos de Creación del Tequila (Salvo Petición Explícita):** Tanto en imágenes como en videos, **NO se deben mostrar procesos de producción del tequila** (jima de agave, jimadores, hornos de mampostería, piedra tahona, tinas de fermentación, alambiques de destilación, maquinaria industrial ni obreros de fábrica), a menos que el cliente lo pida expresamente (`references/brand-context.md` §9). La marca se posiciona como una obra de arte, elegancia contemplativa y celebración de la vida, no como un proceso industrial.
13. **Pregunta Obligatoria de Plataformas Destino (Las 5 Redes + Opción Todas):** Si el usuario no especificó en su mensaje inicial las redes exactas a trabajar, el agente **DEBE PREGUNTAR SIEMPRE Y DE FORMA OBLIGATORIA** qué redes sociales se requieren, presentando sin excepción la lista completa de las 5 plataformas oficiales más la opción «Todas»:
    - 1. Facebook
    - 2. Instagram
    - 3. LinkedIn
    - 4. YouTube
    - 5. TikTok
    - 6. Todas las anteriores
    El agente **NUNCA DEBE OMITIR NINGUNA DE LAS 5 REDES** al formular esta pregunta ni asumir solo una o dos por defecto. Debe formular la consulta con opciones interactivas clickeables en Markdown dual:
    ```markdown
    *«¿En qué redes sociales deseas enfocar esta campaña? (puedes elegir una, varias o todas):»*

    - [🔘 1. Facebook](#)
    - [🔘 2. Instagram](#)
    - [🔘 3. LinkedIn](#)
    - [🔘 4. YouTube](#)
    - [🔘 5. TikTok](#)
    - [🔘 6. Todas las anteriores](#)
    ```

---

## 2. Entorno Local de Ejecución (Anaconda)

Para ejecutar cualquier script en Python dentro de este repositorio, el agente **DEBE** inicializar Anaconda y activar el entorno `skills_env`:

```powershell
& "E:\Users\1167486\AppData\Local\anaconda3\Scripts\conda.exe" shell.powershell hook | Out-String | Invoke-Expression
conda activate skills_env
```

### Comando para Detección de Feriados

```powershell
python sub-skill/obtener-feriados-oficiales-no-oficiales/obtener_feriados.py --year 2026 --dias 30
```

### Comandos de Generación de Medios (OpenRouter)

```powershell
# Catálogo en vivo (no requiere API Key)
python sub-skill/generar-medios-openrouter/generar_medios.py --action list-models --type image
python sub-skill/generar-medios-openrouter/generar_medios.py --action list-models --type video

# Leer los prompts de una pasarela ya generada (no requiere API Key)
python sub-skill/generar-medios-openrouter/generar_medios.py --action extract-prompts `
  --from-showcase showcase/campaign-<fecha>-<slug>.html

# Ensayo SIN costo: resuelve prompts, aspecto, duración y costo estimado
python sub-skill/generar-medios-openrouter/generar_medios.py `
  --from-showcase showcase/campaign-<fecha>-<slug>.html `
  --type image --model <id> --first 3 --dry-run
```

Comprobar la configuración de OpenRouter antes de generar (los comandos van sin parámetro de clave: el script la toma de `~/.openrouter/api_key.txt`):

```powershell
python sub-skill/generar-medios-openrouter/generar_medios.py --action check-key
```

---

## 3. Protocolo de Ejecución Paso a Paso

```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Agente as Agente de IA
    participant Shell as Python (skills_env)
    participant Ref as References & Sub-Skills

    Usuario->>Agente: Solicitud de campaña / contenido
    Agente->>Agente: Verificar parámetros de entrada
    opt Si faltan plataformas destino
        Agente->>Usuario: PREGUNTA OBLIGATORIA (clickeable): ¿En qué redes sociales deseas enfocar la campaña? (Presentar SIEMPRE las 5: Facebook, Instagram, LinkedIn, YouTube, TikTok + Todas)
        Usuario->>Agente: Confirma red(es) o "Todas"
    end
    Agente->>Shell: Ejecutar script de feriados (próximos 30 días)
    Agente->>Ref: Consultar fechas-alcohol.md y prioridades de marca
    Agente->>Usuario: Presentar fechas festivas detectadas y PREGUNTAR OBLIGATORIAMENTE cuál tomar en cuenta
    Usuario->>Agente: Confirma fecha elegida
    opt Festividad con tradición culinaria (calendario-gastronomico-mexicano.md)
        Agente->>Usuario: PREGUNTA OBLIGATORIA: ¿Quieres que tus imágenes generadas tengan un motivo gastronómico?
        Usuario->>Agente: "Sí" o "No"
        opt Si el usuario responde "Sí"
            Agente->>Ref: Consultar platillos y maridajes de esa fecha en calendario-gastronomico-mexicano.md
            Agente->>Usuario: Presenta listado de platillos y maridajes recomendados con Loco Tequila
            Usuario->>Agente: Selecciona/confirma platillo o rumbo culinario
        end
    end
    Agente->>Usuario: PREGUNTA OBLIGATORIA (clickeable): ¿Te gustaría darme sugerencias para prompts y copy?
    alt Usuario responde "Sí, dar sugerencias"
        Usuario->>Agente: Aporta sugerencias / rumbo creativo específico
        Agente->>Agente: Incorpora sugerencias de forma prioritaria
    else Usuario responde "No, te lo dejo todo a ti agente"
        Usuario->>Agente: Confirma delegación creativa completa
        Agente->>Agente: Asume total autonomía creativa según memoria de marca
    end
    Usuario->>Agente: Confirma producto, red(es), medio e inventiva
    Agente->>Usuario: PREGUNTA OBLIGATORIA (clickeable): ¿Cómo prefieres dar referencias previas? (1. Nube OneDrive/SharePoint/GoogleDrive, 2. Carpeta local/cowork, 3. Imágenes en chat, o 4. Ninguna e inspirarse en el acervo de la skill)
    alt (a) El usuario pega link de nube (OneDrive/SharePoint o Google Drive)
        Usuario->>Agente: Link de la carpeta en la nube + alcance
        Agente->>Ref: Ejecutar sub-skill leer-imagenes-onedrive o inspeccionar nube
        Note over Agente,Ref: Triage por nombre de archivo (plataforma + fecha), sin abrir documentos innecesarios
        Agente->>Ref: Leer los .docx / fichas de análisis seleccionadas
        Agente->>Usuario: Reporta piezas detectadas, el ADN a heredar y la lista de exclusión (INCIDENTAL)
    else (b) El usuario indica carpeta local o cowork
        Usuario->>Agente: Ruta local de carpeta o directorio de cowork
        Agente->>Ref: Inspecciona archivos de campañas previas en disco local
        Agente->>Usuario: Identifica conceptos pasados y directrices estéticas para no duplicar
    else (c) El usuario adjunta imágenes propias en el chat
        Usuario->>Agente: Adjunta 1 a 3 imágenes de muestra
        Agente->>Agente: Analiza estilo, composición, iluminación y cristalería para inspirarse
    else (d) El usuario responde "Ninguna" (usar acervo interno)
        Usuario->>Agente: "Ninguna" / "Inspírate con lo que tiene la skill"
        Agente->>Ref: Consultar references/old_campaigns/ y references/loco-tequila/
        Note over Agente: Avanza de inmediato inspirándose en el acervo oficial y campañas históricas de la skill
    end
    Agente->>Ref: Consultar matriz de plataformas y glosario SEO/GEO
    Agente->>Agente: Aplicar Filtro de Locura Genial
    Agente->>Agente: Redactar copys nativos por red
    Agente->>Ref: Segunda Evaluación: Sentido Común Visual (vajilla en comida, soporte de copa y botella)
    Agente->>Agente: Generar Prompts ultra detallados según prompt-standards.md
    Agente->>Ref: Validar contra qa-checklist.md
    Agente->>Usuario: Entrega estructurada + Pasarela Web publicada (paso 11)

    Note over Agente,Usuario: La entrega YA está completa. Lo que sigue son extras opcionales
    Agente->>Usuario: Ofrece (a) top en vivo de generadores o (b) generar piezas con OpenRouter
    alt (a) Leaderboard
        Usuario->>Agente: "Muéstrame el top"
        Agente->>Shell: obtener_leaderboard.py --categoria image|video
        Agente->>Usuario: Ranking real (Elo + win rate) cruzado con la curaduría
    else (b) Generar con OpenRouter
        Usuario->>Agente: "Genera las piezas"
        Agente->>Shell: check-key (comprueba configuración y saldo)
        alt Falta configurar
            Agente->>Usuario: Pide la clave (la acepta en el chat o indica cómo guardarla en el archivo)
            alt Usuario pega la clave en el chat
                Usuario->>Agente: Pega su API Key
                Agente->>Shell: Guarda la clave en ~/.openrouter/api_key.txt y verifica con check-key
            else Usuario la guarda por su cuenta
                Usuario->>Agente: Confirma que ya la guardó en el archivo
                Agente->>Shell: check-key (verifica saldo)
            end
        end
        alt El usuario no tiene cuenta de OpenRouter
            Agente->>Usuario: Orienta cómo crearla y ofrece el leaderboard como alternativa gratuita
        else Configuración lista
            Agente->>Shell: extract-prompts --from-showcase (nunca reescribir prompts de memoria)
            Agente->>Usuario: Pregunta medio, cantidad (tope = max_imagenes/max_videos) y modelo
            Agente->>Shell: list-models (catálogo en vivo, nunca de memoria)
            Agente->>Shell: generate --dry-run
            Agente->>Usuario: Muestra el COSTO ESTIMADO antes de gastar
            Usuario->>Agente: Autoriza
            Agente->>Shell: generate (imágenes primero; después videos)
            Agente->>Agente: Revisar cada pieza contra los guardrails
            Agente->>Usuario: Pieza + copy + prompt y especificaciones + avisos del script
        end
    else Ninguno
        Note over Agente: La entrega ya estaba completa. No insistir
    end
```

---

## 4. Estándares de Generación de Prompts para IA Generativa

> ⚠️ **Fuente de verdad movida.** Estos estándares viven ahora en **`references/prompt-standards.md`**, que sí se carga cuando la skill se invoca desde cualquier directorio de trabajo. Este archivo (`AGENTS.md`) **no entra en contexto automáticamente** si el cwd no es este repositorio, por lo que no debe contener normas que la skill necesite para operar.

Resumen no normativo (el detalle, los 7 campos obligatorios, la regla de escala y el prompt ejemplar están en la referencia):

- Sujeto/producto con SKU exacto, botella canónica (`references/brand-context.md`) y cristalería oficial (copa Riedel grabada).
- Composición con distancia focal y apertura explícitas.
- Iluminación nombrada (hora del día o esquema de estudio).
- Paleta institucional: rojo cochinilla, vino profundo, hueso-marfil, negro obsidiana, plata volcánica.
- Estilo visual con referencia concreta (*luxury editorial photography, Hasselblad medium format look*).
- Relación de aspecto explícita (`--ar`).
- Negative prompt base íntegro (menores, embriaguez, cristalería barata, botellas de competidores, cerámica pintada, marcas de agua, y **prohibición estricta de procesos de producción de tequila** salvo petición expresa del usuario: nada de jima, jimadores, hornos, alambiques, molienda ni operarios).

---

## 5. Inyección de Palabras Clave (SEO + GEO)

Cada pieza generada debe integrar la **Regla de Oro** (máximo 5 keywords):

- **1 Keyword de Territorio Mítico:** (ej. `tequila de terruño`, `Locura Genial`, `tequila objeto de arte`).
- **1 Keyword por Buyer Persona:**
  - *Alejandro:* `destilado de autor`, `tequila de colección para coleccionistas de arte`.
  - *Ana:* `tequila disruptivo`, `tequila y arte contemporáneo mexicano`.
  - *Leonardo:* `tequila audaz y original`, `grupo selecto de conocedores`.
- **1 Keyword de Expresión de Portafolio:**
  - *Loco Blanco:* `tequila blanco premium`, `tequila blanco carácter robusto y suave`.
  - *Loco Ámbar:* `tequila reposado 4 barricas`, `tequila reposado inusual`.
  - *Loco Puro Corazón:* `tequila blanco de lujo`, `tequila para ocasiones especiales`.
  - *Loco Áureo:* `tequila de colección`, `maestría en sabores y aromas`.
  - *Loco Hierofante:* `obra de arte tripartita`, `círculo de membresía EÓN Hierofante`.

---

## 6. Formato de Salida Obligatorio

Toda respuesta final debe estructurarse estrictamente siguiendo la plantilla de [output-template.md](file:///e:/Users/1167486/Local/scripts/skills_generales/agente-mercadotecnia-loco-tequila/references/output-template.md) entregada como texto markdown claro, complementada al final con el **Artefacto HTML de la Pasarela Interactiva** (código HTML/CSS/JS autocontenido que se renderiza directamente en el entorno de Claude como artefacto interactivo).

---

## 7. Pasarela Web Interactiva

> ⚠️ **Fuente de verdad movida.** El procedimiento completo vive ahora en **`references/showcase-rules.md`** por la misma razón que §4.

Resumen no normativo:

- El entregable son **dos acciones verificables**: escribir `showcase/campaign-<fecha>-<slug>.html` y publicarlo con la herramienta `Artifact`, entregando el link.
- Se genera **copiando** `references/showcase-template.html` y sustituyendo **solo** el bloque `const CAMPAIGN = {…}`. Nunca se reescribe el template completo.
- El logo va como data-URI base64 (`showcase/assets/logo_base64.txt`); el SVG pesa 2.2 MB y su ruta relativa se rompe al publicar.
- El copiado al portapapeles ya está resuelto en el template (`copyUniversal()` con `<textarea>` temporal y `document.execCommand('copy')`); no reimplementarlo.
- El template por campaña **no tiene** secciones de leaderboard ni tips técnicos: no hay que improvisarlas por entrega. Añadirlas es un cambio al template, hecho una vez.
- **El leaderboard de generadores es un EXTRA informativo y OPCIONAL**, no parte del entregable: le dice al usuario con qué herramienta conviene ejecutar los prompts. **Se ofrece en el paso 12**, ya con la pasarela entregada, junto con la opción de generar las piezas con OpenRouter, y solo se ejecuta si el usuario acepta (`{{mostrar_leaderboard}}`); si dijo no o no contestó, se omite y no se vuelve a preguntar. Ya está implementado en `showcase/index.html` + `app.js`. Fuente: <https://www.designarena.ai/leaderboard/image>. El HTML no sirve (app Next.js con render en cliente), pero **sí hay API**: ejecutar `sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py` (arenas `image` y `video`; `--actualizar-showcase` para persistirlo) y obtener Elo y win rate reales. **Nunca escribir posiciones ni Elo de memoria**; si el script no corre, omitir el bloque o marcarlo `[no disponible]`. Nunca bloquea la entrega.

### Resiliencia ante limitaciones de Microsoft 365 MCP / Graph API

- Si `read_resource` arroja error de conversión de formato al leer imágenes binarias (`.jpg`, `.png`), **NUNCA detener el flujo ni bloquearse**.
- Utilizar los nombres de archivos y fechas detectados como referencia de contexto para no repetir esas campañas anteriores y avanzar inmediatamente a la ideación.

---

## 8. Generación de Medios con OpenRouter (paso 12b)

> ⚠️ **Fuente de verdad:** **`sub-skill/generar-medios-openrouter/README.md`**. Este resumen no es normativo; ese README sí, y debe leerse antes de ejecutar el script (sobre todo su §3, manejo de la API Key).

Resumen no normativo:

- **Es un extra posterior a la entrega**, ofrecido en el paso 12 junto con el leaderboard. La campaña ya está entregada; ningún fallo aquí la invalida.
- **Cuesta dinero de la cuenta del usuario.** No se genera sin petición explícita, y antes de gastar se corre `--dry-run` para mostrarle el **costo estimado**.
- **Manejo de la clave:** El script la toma del archivo de configuración del usuario (`~/.openrouter/api_key.txt`), de la variable de entorno `OPENROUTER_API_KEY` o de `--api-key`. Si el usuario la proporciona en el chat, el agente la acepta de inmediato y la configura/utiliza sin rechazarla.
- **El agente corre el script, no el usuario.** Nunca proponerle una terminal como salida.
- **Los prompts se leen de la pasarela** (`--action extract-prompts`), nunca se reescriben de memoria: se ejecuta exactamente lo que se entregó.
- **El modelo se elige del catálogo en vivo** (`--action list-models`). Los ids cambian: uno de memoria es un 400. Ojo — `/api/v1/models` **no** lista modelos de video; el catálogo de video está en `/api/v1/videos/models` y el script ya usa el correcto.
- **Las duraciones de video son conjuntos discretos, no rangos** (Veo 3.1 solo acepta 4/6/8 s). El script encaja duración y aspecto a lo que el modelo admite y **declara el ajuste**; ese aviso hay que trasladárselo al usuario.
- **Un `prompt_video` de 24 s no se genera completo:** lo que se obtiene es un fragmento. Decirlo, no entregar 8 segundos como si fueran el spot.
- **Revisar cada pieza contra los guardrails de marca** antes de entregarla. Que la haya producido un modelo externo no relaja +18, exclusión de menores ni la prohibición de botellas de competidores.
- Los archivos van a `outputs/images/` y `outputs/videos/`, excluidos de Git. Son borradores de trabajo, no piezas aprobadas.
