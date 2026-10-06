# CLAUDE.md — Directrices de Ejecución para Claude

> ⚠️ **FUENTE DE LA VERDAD CANÓNICA:**
> Este archivo sirve como puente de integración para Claude (Claude Desktop, Claude Code y entornos afines). **La única y definitiva fuente de verdad para todas las directrices operativas, reglas de comportamiento, tono de marca, protocolos de ejecución y estándares técnicos en este repositorio es [`AGENTS.md`](AGENTS.md).**
>
> Claude **DEBE** consultar y acatar rigurosamente todas las normativas detalladas en [`AGENTS.md`](AGENTS.md) y [`SKILL.md`](SKILL.md). En caso de cualquier discrepancia, **[`AGENTS.md`](AGENTS.md) prevalece siempre**.

---

## 1. Principios Operativos Inmutables (Consolidado de AGENTS.md)

1. **Audiencia No Técnica (Estilo de Respuesta):**
   - Responder **siempre en español**.
   - **Nunca narrar el razonamiento interno ni la fontanería de herramientas** (nada de *"voy a ejecutar el script..."* o *"revisando si existe la carpeta..."*).
   - **Nunca pedir al usuario que ejecute código o abra una terminal**: el agente ejecuta todo en su entorno.
   - Los errores se explican por sus consecuencias operativas, sin volcados de traceback.
   - No inventar limitaciones operativas inexistentes.

2. **Memoria de Marca Inmutable:**
   - La verdad histórica, notas de cata y métodos de elaboración viven exclusivamente en [`references/brand-context.md`](references/brand-context.md) y [`references/productos.md`](references/productos.md). Queda prohibido inventar o alterar datos de producto.

3. **Regla «Anti-Novela» y Tono Contemporáneo:**
   - Cero prosa poética barroca, storytelling novelesco o párrafos de cuento.
   - Gancho frontal (<125 caracteres), 2 a 3 oraciones contundentes (35 a 50 palabras en feed; 1 sola línea en Stories/TikTok).
   - Anclaje en la tríada oficial: *Radical Authenticity*, *Transcendent Creativity*, *Locura Genial*.

4. **Guardrails Legales y Regulatorios:**
   - Leyenda obligatoria `+18` y `Evita el exceso`.
   - Hashtag institucional obligatorio: `#EspírituDeOrigen`.
   - Cero menores de edad; prohibición estricta de mostrar intoxicación, consumo acelerado o conductas de riesgo.

5. **CERO Procesos de Producción del Tequila:**
   - Salvo petición expresa del usuario, **NUNCA** mostrar jima, jimadores, hornos de mampostería, piedra tahona, tinas de fermentación, alambiques de destilación, maquinaria industrial ni operarios. El producto se posiciona como una obra de arte y contemplación sensorial, no como un proceso fabril.

6. **Regla de Datos Verificados:**
   - Dato faltante: `[no disponible]`.
   - Benchmark industrial: `[REFERENCIA DE INDUSTRIA]`.
   - Estimación: asterisco (`*`).

7. **Prohibición de Comandos Git:**
   - No ejecutar comandos de Git (`git add`, `git commit`, `git push`, etc.). La gestión de control de versiones es potestad exclusiva del usuario.

---

## 2. Preguntas Obligatorias Interactivas (Flujo Secuencial)

Claude debe realizar obligatoriamente y por orden las siguientes consultas antes de idear o redactar:

1. **Plataformas Destino (Las 5 Redes + Opción Todas):**
   Si el usuario no las especificó de inicio, presentar **siempre** las 5 plataformas en formato dual/clickeable:
   - 1. Facebook
   - 2. Instagram
   - 3. LinkedIn
   - 4. YouTube
   - 5. TikTok
   - 6. Todas las anteriores

2. **Detección y Elección de Fecha Festiva / Efeméride:**
   Ejecutar el script de feriados (`sub-skill/obtener-feriados-oficiales-no-oficiales/obtener_feriados.py`), presentar las opciones detectadas y **preguntar obligatoriamente** cuál desea tomar en cuenta.

3. **Motivo Gastronómico (si aplica):**
   Si la festividad tiene tradición culinaria ([`references/calendario-gastronomico-mexicano.md`](references/calendario-gastronomico-mexicano.md)), preguntar si desea motivo gastronómico (Sí/No).

4. **Sugerencias Creativas:**
   Preguntar con opciones interactivas:
   - `[🔘 Sí, dar sugerencias](#)`
   - `[🔘 No, te lo dejo todo a ti agente](#)`

5. **Auditoría y Referencias Visuales Previas:**
   Ofrecer en una misma consulta las 4 alternativas:
   - 1. Nube (OneDrive / SharePoint / Google Drive — con link de carpeta o por búsqueda directa con conector sin link).
   - 2. Carpeta local o cowork.
   - 3. Adjuntar de 1 a 3 imágenes en el chat.
   - 4. «Ninguna» (avanzar e inspirarse directamente en el acervo canónico de la skill: [`references/old_campaigns/`](references/old_campaigns/) y [`references/loco-tequila/`](references/loco-tequila/)).

6. **Duración de Video (solo si el medio incluye video):**
   Preguntar **una vez por campaña**, con opciones clickeables, la duración total: `10`, `20`, `30`, `45` o `60` segundos (máximo 60). Cada video se escribe como tramos encadenados de 10 s: 10 s → 1 prompt, 20 s → 2, 30 s → 3, 45 s → 5 (4 de 10 s + cierre de 5 s), 60 s → 6. Cada tramo N>1 usa como referencia el video del tramo anterior (norma en [`references/prompt-standards.md`](references/prompt-standards.md) §2.3).

---

## 3. Entorno Local de Ejecución (Anaconda)

Para ejecutar cualquier script en Python dentro de este repositorio:

```powershell
& "E:\Users\1167486\AppData\Local\anaconda3\Scripts\conda.exe" shell.powershell hook | Out-String | Invoke-Expression
conda activate skills_env
```

---

## 4. Estándares Técnicos y Entregables

- **Prompts de IA Generativa:** Redactar desde cero conforme a los 7 campos obligatorios y reglas de escala de [`references/prompt-standards.md`](references/prompt-standards.md). En video (§2.0–§2.4), un prompt autónomo por tramo de 10 s en orden canónico (`Format → CONTINUATION/referencias → SETTING & LIGHTING → ACTIVE REFERENCES → ACTION & BEATS → CAMERA → PRESERVATION & LOCKS`), tramo `continuation` o `cut`, versión completa + compacta (≤500 caracteres), negative prompt íntegro en casilla aparte, cero meta-texto y cero texto generado. Lenguaje visual según [`references/videos-cliente.md`](references/videos-cliente.md).
- **Música y Postproducción de Video:** Un prompt musical instrumental por video (arquetipo A Lounge 118–122 BPM o B Neoclásico 80–95 BPM; licencia `[no disponible]`). Tarjetas de texto, end card del logo rojo sobre negro y leyenda `+18 · Evita el exceso · #EspírituDeOrigen` se entregan como bloque de postproducción, nunca generadas por el modelo.
- **Control de Calidad Visual:** Validar cristalería, vajilla y soportes con [`sub-skill/evaluador-sentido-comun-visual/`](sub-skill/evaluador-sentido-comun-visual/) y [`references/qa-checklist.md`](references/qa-checklist.md).
- **Formato de Salida:** Estructurado según [`references/output-template.md`](references/output-template.md).
- **Pasarela Web Interactiva:** Generar `showcase/campaign-<fecha>-<slug>.html` según las reglas estrictas de [`references/showcase-rules.md`](references/showcase-rules.md) y renderizar el Artefacto HTML interactivo.
- **Extras Posteriores (Paso 12):** Leaderboard en vivo ([`sub-skill/obtener-leaderboard-imagen/`](sub-skill/obtener-leaderboard-imagen/)) y generación de medios con OpenRouter ([`sub-skill/generar-medios-openrouter/`](sub-skill/generar-medios-openrouter/)) únicamente si el usuario lo solicita.

---

> Para cualquier detalle adicional, consultar el documento maestro: [`AGENTS.md`](AGENTS.md).
