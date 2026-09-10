# Sub-skill: Evaluador de Sentido Común Visual y Verosimilitud de Escena

> **Propósito:** Realizar una **segunda evaluación obligatoria** antes de redactar y consolidar los prompts definitivos para generadores de IA (Midjourney, Flux, Sora, etc.). Su objetivo es garantizar la coherencia física, culinaria, espacial y de etiqueta de lujo de la escena, erradicando alucinaciones de sentido común (ej. comida servida sin plato, copas flotando, líquidos brotando sin gravedad, botellas en equilibrio imposible).

---

## 1. El Problema que Resuelve

Los modelos generativos de IA destacan en textura e iluminación, pero **carecen de sentido común físico y culinario innato**. Tienden a generar:
- Alimentos apoyados directamente sobre mesas de madera, piedras volcánicas o manteles sin plato ni soporte adecuado (ej. un *chile en nogada sin plato*).
- Copas suspendidas en el aire, sin posavasos o con inclinaciones que desafían la gravedad.
- Botellas abiertas sin corcho/tapa visible en proximidad.
- Comida sumergida en copas de degustación o hielo en destilados premium.
- Escalas desproporcionadas (un platillo más grande que la botella, o cubiertos gigantes).

---

## 2. Los 5 Criterios de Evaluación de Sentido Común (Pre-Flight)

Antes de autorizar un prompt maestro de imagen o video, el agente debe auditar la escena contra estos 5 criterios:

### 2.1 Criterio Gastronómico: Menaje y Vajilla Obligatoria
- **Regla Inflexible:** **NUNCA** se describe un alimento apoyado directamente sobre la mesa, piedra, barra o superficie cruda.
- **Vajilla de Alta Gama Explicita:**
  - Si hay platillos tradicionales o de alta cocina (chiles en nogada, mole poblano, tacos ceremoniales, tamales de quelites): **debe especificarse el plato o recipiente** (ej. *«served on an artisan high-temperature glazed ceramic plate»*, *«matte porcelain rimmed dish»*, o *«contemporary black stoneware plate»*).
  - La salsa, crema o caldo (como la nogada o el mole) debe reposar con naturalidad sobre el fondo del plato, con ligera interacción de brillo y textura.
  - Si la escena lo amerita, incluir menaje de apoyo coherente: cubertería de plata mate o acero forjado, servilleta de lino doblada al costado.

### 2.2 Criterio de Cristalería y Soporte Físico
- La copa de degustación oficial (Riedel tequilera grabada) debe contar con un punto de apoyo definido y estable:
  - Sobre un posavasos artesanal de piel/cuero curtido, bajoplato de piedra volcánica pulida o madera de parota.
  - Sombra de contacto (*contact shadow*) y oclusión ambiental nítida en la base del pie de la copa.
  - NUNCA copas inclinadas sin una mano humana visible que las sostenga con delicadeza.

### 2.3 Criterio Anatómico de Botella (Preservación de lo Primordial)
- Para evitar que el generador diluya o ignore los atributos primordiales de la botella:
  - La botella debe especificarse con su bloque anatómico canon en las primeras 20 palabras del prompt.
  - Enfoque nítido y presencia del fondo de cristal macizo de 2 cm y cápsula metálica.
  - La botella debe estar debidamente apoyada sobre su base pesada, jamás flotando ni recortada por el marco de forma torpe.

### 2.4 Criterio de Gravedad, Escala y Espacio
- Relación de escala real: una botella de 750 ml mide ~28-30 cm de altura; una copa Riedel mide ~21 cm; un plato extendido de cena mide ~27-30 cm de diámetro. La botella no debe verse miniaturizada ni gigantesca frente a la comida.
- Si hay vertido de líquido (*pour*): el chorro debe tener origen exacto en el cuello de la botella y destino visible dentro del cáliz de la copa, con física laminar fluida y sin salpicaduras aceitosas irreales.

### 2.5 Criterio de Etiqueta y Armonía de Bodegón
- Composición armónica entre gastronomía y tequila:
  - El plato gastronómico y la copa se sitúan en el plano de interacción del comensal.
  - La botella acompaña la escena en segundo plano ligeramente desenfocada o en co-protagonismo editorial equilibrado.
  - Iluminación compartida: la misma temperatura de luz (luz dorada cálida de atardecer o velas tenues) debe bañar uniformemente el plato, la copa y la botella.

---

## 3. Matriz de Corrección Rápida de Sentido Común

| Error detectado en la ideación | Corrección obligatoria en el prompt |
|---|---|
| Alimento sobre superficie cruda (ej. chile en nogada sobre mesa de madera) | Agregar: *«artfully plated on a deep matte ivory ceramic artisan dish, glossy nogada sauce pooling elegantly on the plate surface, garnished with ruby pomegranate seeds and fresh parsley»* |
| Copa flotando o sin anclaje visual | Agregar: *«Riedel glass resting securely on an obsidian stone coaster with soft contact shadows and crisp reflections»* |
| Botella genérica o sin rasgos primordiales | Añadir directiva: *«PRESERVE EXACT BOTTLE MORPHOLOGY: conical trapezoidal clear crystal bottle, thick 2cm solid glass base, raised red cochineal enamel "Loco" wordmark with silver outline»* |
| Botella abierta con líquido sin tapón | Especificar botella cerrada con su cápsula metálica oficial, o con el tapón colocado a un lado sobre la mesa con intención estética |
| Hielo o rodajas en la copa | Eliminar y añadir al Negative Prompt: *«ice cubes, salt rim, lime wedge, shot glass»* |

---

## 4. Protocolo de Integración en el Flujo

1. **Ideación inicial:** Se concibe la idea creativa (anclaje de fecha + producto + gastronomía si aplica).
2. **Segunda Evaluación (Sub-skill):** El agente revisa mentalmente la escena contra los 5 criterios: ¿Tiene plato? ¿Tiene soporte la copa? ¿La botella conserva sus rasgos primordiales? ¿La gravedad es creíble?
3. **Ajuste automático silencioso:** Si falta el plato, el posavasos o la morfología de botella, el agente **inyecta los descriptores de sentido común antes de generar el prompt final**.
4. **Validación final:** Pasa al checklist de QA multicanal.
