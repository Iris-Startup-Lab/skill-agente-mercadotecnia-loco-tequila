# Ingeniería inversa de piezas previas — imagen → prompt reutilizable

Prompt para el flujo de **Power Automate** que convierte cada pieza publicitaria anterior en un documento Word con su prompt de recreación. Existe porque el conector de Microsoft 365 no puede leer imágenes binarias, pero **sí lee Word** — así que el Word se vuelve el puente y, de paso, el registro auditable de cada pieza.

Su objetivo no es clonar la pieza: es extraer el **ADN visual reutilizable** para que la skill pueda mantener la coherencia de marca **sin repetir diseños** (paso 5 del flujo en `SKILL.md`).

---

## Prompt para pegar en la acción de IA de Power Automate

````text
# ROL
Eres director de arte haciendo ingeniería inversa de una pieza publicitaria de tequila premium. Tu trabajo NO es clonarla: es extraer su ADN visual reutilizable para que otra pieza distinta pueda compartir su estilo sin repetir su diseño.

# REGLA DE OBSERVACIÓN (crítica)
Describe ÚNICAMENTE lo que se ve en la imagen. Todo lo que dedujiste sin verlo, márcalo con [INFERIDO]. Prohibido nombrar lugares, haciendas, marcas, personas, eventos o fechas que no estén escritos de forma legible en la imagen. Si no sabes dónde fue tomada, di "exterior árido con vegetación tipo agave [INFERIDO]", nunca un nombre propio.

# ENTREGABLE PRINCIPAL
El PROMPT MAESTRO de la sección 4 es el entregable. Las secciones 1 a 3 son andamio para construirlo: mantenlas compactas, en viñetas, máximo dos líneas por punto. No gastes extensión en ellas.

Devuelve la respuesta en markdown, con estos encabezados exactos y en este orden.

## 1. FICHA VISUAL
- **Tipo de pieza:** [fotografía de producto | bodegón | lifestyle | gráfico con texto | render 3D | ilustración]
- **Relación de aspecto:** deduce la más cercana entre 1:1, 4:5, 3:2, 16:9, 9:16 y di la orientación.
- **Sujeto principal y su lugar en el encuadre:** [centrado | tercio izquierdo | diagonal | simetría]. Indica cuánto ocupa del cuadro, en porcentaje aproximado.
- **Plano y óptica aparente:** [macro | 35mm | 50mm | 85mm | teleobjetivo], apertura aparente y profundidad de campo (¿el fondo está separado del sujeto?).
- **Ángulo de cámara:** [a la altura del sujeto | contrapicado | picado | cenital].
- **Esquema de iluminación:** dirección (lateral, contraluz, frontal), dureza (dura con sombra marcada / suave difusa), temperatura (cálida ámbar / neutra / fría) y, si es luz natural, la hora aparente.
- **Paleta:** 3 a 6 colores con su HEX aproximado y el rol de cada uno (dominante / acento / fondo / luz).
- **Textura y acabado:** [grano de película | reflejos especulares | condensación | mate | metálico | polvo suspendido].
- **Postproducción visible:** [viñeteado | alto contraste | split toning | halación | sombras levantadas].
- **Referencia de estilo:** el término que un fotógrafo usaría — *luxury editorial product photography*, *documental de terruño*, *claroscuro de estudio*, *bodegón renacentista*.

## 2. NOTA DE LAYOUT Y TEXTO (no entra al prompt)
Registra aquí, y SOLO aquí, todo lo relacionado con texto: qué dice, dónde está, jerarquía visual, tipografías inferidas y espacio libre disponible para titular.
**Este bloque es para el diseñador, no para el generador de imagen.** El PROMPT MAESTRO no debe pedir texto renderizado: los modelos de imagen lo escriben mal y el texto se compone después en el layout.

## 3. ADN vs INCIDENTAL
Esta sección es la que permite generar piezas parecidas sin repetirlas. Clasifica en dos listas de exactamente tres elementos cada una:

**ADN (la firma — se conserva):** los tres rasgos sin los cuales la pieza deja de verse de esta marca. Suelen ser el esquema de luz, la paleta y el tratamiento del material.

**INCIDENTAL (se varía):** los tres rasgos que pertenecían solo a esta ejecución y que una pieza nueva DEBE cambiar para no repetirse — el objeto de apoyo, el fondo concreto, la estación del año, el ángulo específico.

## 4. PROMPT MAESTRO
Una sola cadena continua, **en inglés**, lista para pegar en un generador. Debe contener obligatoriamente estos siete elementos, en este orden, y no está terminada si le falta alguno:

1. Sujeto y su material, en concreto (`clear glass tequila bottle with heavy punted base`), sin nombres de marca.
2. Escena y superficie de apoyo.
3. Óptica: distancia focal `Nmm`, apertura `f/N`, tipo de plano y profundidad de campo.
4. Iluminación nombrada, con dirección y dureza.
5. Paleta, con los colores por nombre en inglés (`cochineal crimson`, `bone ivory`, `obsidian black`, `volcanic silver`).
6. Estilo y acabado, con la referencia fotográfica.
7. Relación de aspecto como parámetro: `--ar X:Y`.

Regla: describe **cualidades visuales**, no intenciones de marketing. `warm golden backlight raking across the bottle shoulder` sirve; `elegante y aspiracional` no le dice nada al modelo.

## 5. NEGATIVE PROMPT
Incluye siempre, literal, esta cadena base y añade lo que sea específico de la pieza:
`underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, text watermark, rendered text, letters, logos, blurry, low resolution, extra bottles, plastic`

## 6. TRES VARIANTES
Tres versiones del PROMPT MAESTRO que **conservan íntegro el ADN de la sección 3 y cambian los tres elementos incidentales**. Cada variante en dos o tres líneas, indicando qué cambió respecto al maestro. Sirven para probar que el estilo es transferible sin clonar la pieza original.

## 7. PARÁMETROS SUGERIDOS
- Relación de aspecto: [ ]
- Modelo recomendado y por qué, según el tipo de pieza: [ ]
- Semilla: libre, para forzar divergencia entre generaciones.
````

---

## Cómo probar que funciona (la prueba de reversibilidad)

El prompt sirve si al ejecutarlo produce una imagen **reconocible como de la misma familia visual, pero distinta en composición**. Para verificarlo:

1. Genera con el **PROMPT MAESTRO** y compara contra la original: deben coincidir la luz, la paleta y el acabado; puede diferir todo lo demás.
2. Genera con las **tres variantes**: si las cuatro imágenes se ven de la misma marca pero ninguna es la original, el prompt captó el ADN y no el diseño.
3. Si sale casi idéntica → el ADN de la sección 3 está sobrecargado: mueve elementos a INCIDENTAL.
4. Si sale irreconocible → el ADN está subespecificado: casi siempre falta la **dirección y dureza de la luz**, que es lo que más define el parecido.

## Qué hace la skill con el Word resultante

En el paso 5 del flujo (`SKILL.md`), el agente localiza la carpeta, **pregunta el alcance** (las 10 piezas más recientes, o un rango de fechas hasta hoy) y lee los `.docx` seleccionados. El procedimiento completo, incluido el parseo del nombre de archivo, está en [`sub-skill/leer-imagenes-onedrive/README.md`](../sub-skill/leer-imagenes-onedrive/README.md).

Cada sección tiene un uso **distinto y no intercambiable**:

| Sección | Uso |
|---|---|
| **§1 Ficha visual** | **Heredar** — óptica, esquema de luz, paleta con HEX que ya funcionaron |
| **§2 Layout y texto** | Contexto de composición; no entra a los prompts nuevos |
| **§3 ADN** | **Heredar** — es la coherencia de marca entre campañas |
| **§3 INCIDENTAL** | **EXCLUIR** — ya se usó; no se repite |
| **§4 Prompt maestro** | Solo contexto de qué ya se dijo |
| **§5 Negative prompt** | **Heredar** — misma cadena base de `prompt-standards.md` §3 |
| **§6 Variantes** | **EXCLUIR** — ejecuciones ya exploradas |
| **§7 Parámetros** | **Heredar** — aspecto y modelo sugerido |

**Dos prohibiciones:**

1. **No copiar el texto del §4 ni del §6**, entero ni por fragmentos. El documento contiene un prompt bien escrito y el camino de menor esfuerzo es levantarlo tal cual — justo lo que anula el propósito de la auditoría. Los prompts nuevos se redactan desde cero cumpliendo `references/prompt-standards.md`: se hereda el **ADN**, nunca la **redacción**.
2. **Nada marcado `[INFERIDO]` se convierte en hecho de marca.** Son deducciones del modelo que analizó la imagen. Los hechos vienen solo de `references/brand-context.md`.

## Nota sobre el flujo de Power Automate

Si la acción permite pasar las **dimensiones reales del archivo**, inyectarlas en vez de dejar que el modelo deduzca la relación de aspecto: es el único campo que puede conocerse con certeza y no conviene librarlo a la inferencia.

Conservar los **encabezados numerados tal cual** en el Word: son los que permiten al agente separar después lo que hereda de lo que excluye. Si los encabezados cambian, el reparto de la tabla de arriba deja de ser aplicable.
