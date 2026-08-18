# AGENTS.md — Directrices Operativas para Agentes de IA

Este documento contiene las reglas de comportamiento, protocolo de ejecución y estándares operativos para cualquier Agente de IA (Antigravity, Claude, ChatGPT, etc.) que opere en este repositorio o ejecute la skill `agente-mercadotecnia-loco-tequila`.

---

## 1. Principios Fundamentales del Agente

1. **Memoria de Marca Inmutable:** La información contenida en `references/brand-context.md` y `references/productos.md` es la única fuente de verdad. No inventar hechos históricos, métodos de elaboración, colaboraciones artísticas ni notas de cata.
2. **Gramática Nativa por Plataforma:** Cada red social (Facebook, YouTube, LinkedIn, TikTok, Instagram) tiene un propósito, tono y formato técnico específicos detallados en `references/platforms-process.md`. Nunca realizar cortes o traducciones literales de un copy entre redes.
3. **Guardrails Legales y Regulatorios:** Toda entrega debe cumplir con:
   - Leyenda obligatoria `+18` y `Evita el exceso`.
   - Hashtag institucional `#EspírituDeOrigen`.
   - Exclusión de menores de edad y prohibición estricta de mostrar intoxicación, consumo acelerado o conductas de riesgo.
4. **Regla de Datos Verificados:**
   - Si falta un dato o métrica: escribir `[no disponible]`.
   - Si se usa un benchmark de la industria: marcar como `[REFERENCIA DE INDUSTRIA]`.
   - Si es una estimación: marcar con asterisco (`*`).
   - Nunca alucinar cifras de alcance o conversiones no proporcionadas.
5. **Auditoría de piezas previas (OneDrive/SharePoint) — vía Word:** el conector de Microsoft 365 no lee imágenes binarias, pero **sí lee `.docx`**. Un flujo de Power Automate deposita en la carpeta un Word de análisis por cada pieza, con su ficha visual y su prompt (ver `references/ingenieria-inversa-imagen.md`). Esa es la **vía principal**.
   - **El agente DEBE PEDIR SIEMPRE el link de la carpeta al usuario.** No existe una carpeta fija: cambia en cada campaña. Prohibido asumir una ruta, reutilizar la de una conversación anterior, deducirla del nombre del producto o buscarla a ciegas con `sharepoint_folder_search`.
   - **En la misma pregunta, DEBE preguntar el alcance:** las **10 piezas más recientes** o un **rango de fechas** desde la que indique el usuario hasta hoy. El filtro se resuelve con el timestamp del nombre de archivo, sin abrir documentos.
   - Si el usuario declina, se omite la auditoría y se avanza sin bloquear. Lo obligatorio es **preguntar**, no obtener la carpeta.
6. **Reparto inspirar / excluir:** del Word se **hereda** el ADN (§3), la ficha visual (§1) y los parámetros (§7) para mantener coherencia de marca; se **excluye** la lista INCIDENTAL (§3) y las variantes (§6) por estar ya usadas. **Prohibido reutilizar el texto del prompt maestro (§4)**, entero o por fragmentos: los prompts nuevos se redactan desde cero según `references/prompt-standards.md`. Nada marcado `[INFERIDO]` puede convertirse en hecho de marca. Solo si la carpeta no tiene Word de análisis se cae al respaldo de pedir 1 a 3 imágenes adjuntas en el chat.
7. **Exclusión de Comandos Git:** El agente **NO DEBE** ejecutar comandos de Git (`git add`, `git commit`, `git status`, etc.) ni gestionar el control de versiones. La gestión de Git es responsabilidad exclusiva del usuario.
8. **Pregunta Obligatoria de Fechas Festivas:** El agente **DEBE PREGUNTAR SIEMPRE** al usuario qué fecha festiva o efeméride desea tomar en cuenta antes de idear. Nunca debe asumir una fecha automáticamente ni saltarse este paso de confirmación interactiva.

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
    Agente->>Shell: Ejecutar script de feriados (próximos 30 días)
    Agente->>Ref: Consultar fechas-alcohol.md y prioridades de marca
    Agente->>Usuario: Presentar fechas festivas detectadas y PREGUNTAR OBLIGATORIAMENTE cuál tomar en cuenta
    Usuario->>Agente: Confirma fecha elegida, producto, red(es), medio e inventiva
    Agente->>Usuario: PIDE OBLIGATORIAMENTE el link de la carpeta + el alcance (¿10 más recientes o desde qué fecha?)
    Note over Agente,Usuario: La carpeta cambia en cada campaña: nunca asumirla ni reutilizarla
    alt El usuario pega el link
        Usuario->>Agente: Link de la carpeta + alcance
        Agente->>Ref: Ejecutar sub-skill leer-imagenes-onedrive
        Note over Agente,Ref: Triage por nombre de archivo (plataforma + fecha), sin abrir documentos
        Agente->>Ref: Leer los .docx de análisis seleccionados
        Agente->>Usuario: Reporta piezas detectadas, el ADN a heredar y la lista de exclusión (INCIDENTAL)
        opt La carpeta no tiene Word de análisis
            Agente->>Usuario: Respaldo — pregunta si desea adjuntar 1 a 3 imágenes de muestra en el chat
            Usuario->>Agente: Adjunta imágenes o confirma continuar sin adjuntar
        end
    else El usuario declina
        Usuario->>Agente: "No aplica"
        Note over Agente: Omite la auditoría y avanza sin bloquear
    end
    Agente->>Ref: Consultar matriz de plataformas y glosario SEO/GEO
    Agente->>Agente: Aplicar Filtro de Locura Genial
    Agente->>Agente: Redactar copys nativos + Prompts para IA generativa
    Agente->>Ref: Validar contra qa-checklist.md
    Agente->>Usuario: Entrega estructurada con output-template.md
```

---

## 4. Estándares de Generación de Prompts para IA Generativa

> ⚠️ **Fuente de verdad movida.** Estos estándares viven ahora en **`references/prompt-standards.md`**, que sí se carga cuando la skill se invoca desde cualquier directorio de trabajo. Este archivo (`AGENTS.md`) **no entra en contexto automáticamente** si el cwd no es este repositorio, por lo que no debe contener normas que la skill necesite para operar.

Resumen no normativo (el detalle, los 7 campos obligatorios, la regla de escala y el prompt ejemplar están en la referencia):

- Sujeto/producto con SKU exacto y cristalería oficial.
- Composición con distancia focal y apertura explícitas.
- Iluminación nombrada (hora del día o esquema de estudio).
- Paleta institucional: rojo cochinilla, vino profundo, hueso-marfil, negro obsidiana, plata volcánica.
- Estilo visual con referencia concreta (*luxury editorial photography, Hasselblad medium format look*).
- Relación de aspecto explícita (`--ar`).
- Negative prompt base íntegro (menores, embriaguez, cristalería barata, botellas de competidores, watermark, baja resolución).

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
- **El leaderboard de generadores es un EXTRA informativo y OPCIONAL**, no parte del entregable: le dice al usuario con qué herramienta conviene ejecutar los prompts. **Se ofrece en la pregunta del paso 6** (junto con `{{medio}}`) y solo se ejecuta si el usuario acepta (`{{mostrar_leaderboard}}`); si dijo no o no contestó, se omite y no se vuelve a preguntar. Ya está implementado en `showcase/index.html` + `app.js`. Fuente: <https://www.designarena.ai/leaderboard/image>. El HTML no sirve (app Next.js con render en cliente), pero **sí hay API**: ejecutar `sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py` (arenas `image` y `video`; `--actualizar-showcase` para persistirlo) y obtener Elo y win rate reales. **Nunca escribir posiciones ni Elo de memoria**; si el script no corre, omitir el bloque o marcarlo `[no disponible]`. Nunca bloquea la entrega.

### Resiliencia ante limitaciones de Microsoft 365 MCP / Graph API

- Si `read_resource` arroja error de conversión de formato al leer imágenes binarias (`.jpg`, `.png`), **NUNCA detener el flujo ni bloquearse**.
- Utilizar los nombres de archivos y fechas detectados como referencia de contexto para no repetir esas campañas anteriores y avanzar inmediatamente a la ideación.


