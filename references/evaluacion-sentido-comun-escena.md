# Evaluación de Sentido Común Visual y Verosimilitud de Escena

> **Norma de Calidad Pre-Prompt (Paso 8b del Flujo):**  
> Antes de redactar y consolidar los prompts maestros de imagen o video, el agente debe someter la escena a una **segunda evaluación obligatoria de sentido común físico y gastronómico**. Ningún prompt debe generar composiciones inverosímiles (alimentos sin vajilla, objetos flotantes, botellas deformadas o desproporciones).

---

## 1. Regla de Oro Culinaria: Menaje y Vajilla Obligatorios

**Caso de Estudio (Evitar):** Generar un platillo ceremonial (ej. *chile en nogada, mole poblano, tacos de lechón, postre de elote*) apoyado directamente sobre una mesa, roca, mantel o superficie cruda.

### Directiva de Sentido Común Gastronómico:
1. **Todo alimento DEBE ser presentado en vajilla de alta gama:**
   - Vajilla recomendada: platos de cerámica artesanal de alta temperatura (*stoneware*), porcelana mate con reborde fino (*matte porcelain dish*), o barro negro bruñido de Oaxaca para toques tradicionales sobrios.
   - Especificar siempre la relación plato-alimento: el platillo reposa centrado o en emplatado de diseño contemporáneo, la salsa (nogada, mole, adobo) cubre de manera fluida y contenida el fondo del plato sin derrames desordenados.
2. **Complementos de mesa indispensables:**
   - Cubertería elegante de diseño (tenedor y cuchillo de plata o acero forjado oscuro).
   - Servilleta de lino natural plegada con discreción.
   - Superficie noble: madera de nogal/parota tratada, mármol cálido, lino crudo o piedra volcánica como bajoplato.

---

## 2. Refuerzo de lo Primordial de la Botella (Anti-Olvido de la IA)

Los generadores de IA (Midjourney, Flux, Imagen 3, Sora) a menudo ignoran la silueta de la botella o la convierten en un envase genérico. Para reforzar **lo primordial** de Loco Tequila:

1. **Prioridad de Apertura (Primeros 15-20 tokens):**
   El prompt debe iniciar siempre con el descriptor anatómico canónico de la botella antes del escenario.
2. **Los 5 Atributos Primordiales Innegociables:**
   - **Morfología cónica trapezoidal** con hombros sutiles que se estrechan hacia el cuello.
   - **Base pesada maciza de cristal macizo de 2 cm** (`solid 2cm clear crystal base`).
   - **Logotipo "Loco" en relieve esmaltado vítreo rojo cochinilla vitrificado** con fino contorno plateado. Es el único elemento en rojo.
   - **Cápsula de cuello metálica según el SKU:** Rojo para Blanco, Cobre/Bronce para Ámbar, Plata mate para Puro Corazón, Negro mate para Áureo.
   - **Cristal de transparencia diamantina sin etiquetas de papel** (`pure transparent crystal bottle with zero paper labels`).
3. **Directiva de Preservación de Morfología:**
   ```text
   PRESERVE EXACT BOTTLE MORPHOLOGY: Keep the exact iconic conical trapezoidal heavy crystal bottle with 2cm solid base, and raised red enamel "Loco" relief. Strictly prohibit generic cylindrical bottles, paper labels, and round screw caps.
   ```
4. **Negativos Específicos contra Botellas Genéricas:**
   ```text
   generic liquor bottle, cylindrical bottle, round wine bottle, paper label, sticker label, screw cap, flat base, thin glass, painted ceramic decanter
   ```

---

## 3. Lógica Espacial, Cristalería y Gravedad

1. **La Copa Oficial Riedel:**
   - Copa tequilera Riedel oficial grabada con rombo institucional.
   - Debe descansar firmemente sobre la mesa o posavasos de cuero/piedra con sombra de contacto (*contact shadow*).
   - NUNCA copas flotando en el aire ni colocadas en bordes precarios.
2. **Relación Espacial y Escala Real:**
   - La botella de 750 ml (~28-30 cm) guarda una escala proporcionada frente al plato de comida (~27-30 cm) y la copa (~21 cm).
   - En tomas de maridaje: el plato de comida en primer o plano medio, la copa a la derecha o alcance natural de la mano, y la botella como ancla visual de fondo en bokeh sutil o en co-protagonismo editorial.
3. **Física del Vertido y Dinámica de Fluidos:**
   - El chorro de vertido proviene de la boca de la botella y cae directamente en el centro del cáliz de la copa.
   - Líquido cristalino ultraligero (~1.2 cP), sin viscosidad aceitosa ni espuma persistente.

---

## 4. Checklist Rápido de Validación Pre-Prompt

Antes de dar por bueno un prompt:
- [ ] Si hay comida: ¿tiene plato/vajilla explícita y de alta gastronomía?
- [ ] ¿La salsa/crema descansa de forma natural en el plato sin flotar en el aire ni derramarse en superficies crudas?
- [ ] ¿La botella describe su morfología canónica (base de 2 cm maciza, relieve rojo vítreo, cápsula exacta)?
- [ ] ¿La directiva de preservación de botella está presente en el prompt multimodal?
- [ ] ¿La copa Riedel tiene una superficie de apoyo creíble y sombras de contacto reales?
- [ ] ¿Se eliminó cualquier cliché no permitido (hielo, sal, limón en el borde, caballito de shot)?
