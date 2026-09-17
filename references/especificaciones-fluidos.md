# Especificaciones de Física de Fluidos: Vertido de Tequila en Copa Riedel (Video)

Este documento detalla los parámetros físicos, hidrodinámicos y ópticos obligatorios para simular el comportamiento realista del vertido (*pouring*) y movimiento de **Loco Tequila** en modelos generativos de video (Sora, Runway Gen-3, Kling, Veo, Wan, Seedance 2.5).

El objetivo es erradicar el vicio recurrente de la IA de simular líquidos espesos o carbonatados (efecto jarabe, refresco, sidra o cerveza) y garantizar que el destilado 100% de agave se comporte con fidelidad física absoluta en la **copa oficial de degustación Riedel Tequila**.

---

## 🟢 Regla Crítica Cero: Desactivación de Emisores de Fondo (*Bottom Emitters OFF*)

> ⚠️ **Principio Físico Inviolable:**  
> Loco Tequila es un **destilado puro a 40% ABV, completamente plano y libre de gas carbónico**.  
> **Queda estrictamente prohibida la generación continua o ascendente de burbujas desde la base del recipiente.**  
> Cualquier burbuja presente es **exclusivamente aire atrapado mecánicamente por el impacto del chorro**, el cual asciende de inmediato y **estalla en milisegundos al tocar la atmósfera**.

---

## 🥃 1. Perfiles de Fluido según Expresión de Loco Tequila

A diferencia de fermentados densos (como el vino tinto) o licores dulces, el tequila no presenta una masa pesada ni oscurecimiento central opaco. Se divide en dos comportamientos lumínicos:

### Perfil A: Loco Blanco y Loco Puro Corazón (Cristalino / Diamante)
* **Viscosidad:** Ultrabaja (~1.2 a 1.4 mPa·s / cP, prácticamente idéntica al agua pura).
* **Cromaticidad:** 100% incoloro, diáfano y con brillo diamantino.
* **Comportamiento Óptico:** Alta refracción y transmisión de luz uniforme a través de todo el volumen. **Cero oscurecimiento en el centro del cáliz**.
* **Cáusticas y Reflejos:** Proyecta cáusticas refractivas nítidas y brillantes sobre la superficie de apoyo, con destellos plata volcánica en los bordes y en el menisco.

### Perfil B: Loco Ámbar y Loco Áureo (Ámbar Dorado / Reposado Cuatro Barricas)
* **Viscosidad:** Ultrabaja (~1.2 a 1.4 mPa·s / cP). La maduración en barricas aporta color y aromas, no densidad jarabosa ni azúcares viscosos.
* **Cromaticidad:** Ámbar dorado luminoso, miel translúcida y destellos de cobre cálido.
* **Comportamiento Óptico:** Cristalino y diáfano. La luz atraviesa el centro del volumen sin generar zonas opacas ni sombras fangosas (**cero oscurecimiento central denso**).
* **Reflejos Especulares:** Brillos duros y definidos de las fuentes de iluminación sobre la superficie dorada y las curvas del cristal.

---

## 🌊 2. Cinemática del Vertido e Impacto Hidrodinámico

### A. Dinámica del Chorro de Caída
* **Flujo:** Chorro laminar cilíndrico, ágil y continuo, impulsado por gravedad natural a velocidad cinematográfica real (1x), nunca en cámara lenta viscosa artificial.
* **Salpicadura en el impacto:** Al golpear el fondo de la copa o el líquido acumulado, genera una salpicadura limpia de **microgotas cristalinas afiladas** que rebotan sin atomizarse en brisa o spray nebuloso.

### B. Dinámica de Microburbujas Mecánicas
* **Génesis:** Únicamente en el punto de contacto donde el chorro penetra el menisco.
* **Ciclo de vida:** **Ultracorto (<0.3 segundos)**. Las microburbujas son arrastradas momentáneamente hacia abajo, suben en un barrido continuo y **estallan instantáneamente al contactar el aire**.
* **Prohibición Absoluta:**
  - Cero generación de burbujas en reposo.
  - Cero espuma superficial, corona o efervescencia residual.
  - Cero microburbujas estáticas pegadas a las paredes internas del cristal.

### C. Tiempo de Reposo y Estabilización Superficial
* **Disipación cinética:** Al cesar el flujo de la botella, la turbulencia y las ondas superficiales se disipan en **menos de 1 a 1.5 segundos**.
* **Estado final:** La superficie del líquido queda completamente **plana, estática, inerte y libre de movimiento interno**.

---

## 🍷 3. Interacción con la Cristalería Oficial (Copa Riedel Tequila)

> 🚫 **Prohibición de Cristalería Corriente:**  
> En Loco Tequila está **estrictamente prohibido el uso de vasos de shot, caballitos tequileros, vasos old-fashioned o vasos desechables**. Toda degustación y vertido se realiza en la **copa oficial de degustación Riedel Tequila** (silueta tulipán estilizada de cuello angosto y cáliz cóncavo).

### Comportamiento en las Paredes de Cristal (Lágrimas del Tequila / Piernas)
* Al chocar y arremolinarse contra el cáliz cóncavo de la copa Riedel, el destilado forma un fino anillo o corona en el cristal.
* De este menisco descienden **lágrimas delgadas, nítidas y transparentes** (*thin transparent tequila legs/tears*) con un escurrimiento ágil y limpio.
* **Prohibición:** No debe dejar películas pegajosas, aceitosas ni rastros densos como licor azucarado o jarabe.

---

## 🎬 4. Métodos de Entrada Multimodal (Image-to-Video y Video-to-Video)

Para asegurar la máxima fidelidad en modelos generativos de video avanzados, la skill contempla dos modalidades de anclaje que el usuario puede proporcionar:

### A. Referencia Visual de Botella (Image-to-Video)
El usuario puede adjuntar una fotografía oficial de la botella de Loco Tequila con fondo neutro de estudio. El prompt integra obligatoriamente la directiva:
```text
ADD: The added image is the real bottle image. PRESERVE EXACT BOTTLE MORPHOLOGY: Maintain the identical conical trapezoidal heavy crystal silhouette, the thick 2cm solid base, and the raised crimson enamel "Loco" relief. Strictly prohibit generic cylindrical liquor bottles, paper labels, and round screw caps.
```

### B. Referencia de Movimiento del Vertido (Video-to-Video / Clip de Vertido)
Si el usuario dispone de un clip de referencia de vertido real (agua o destilado claro cayendo en copa de degustación), se integra la directiva:
```text
MATCH POUR PHYSICS: Match the exact water-thin pour physics (~1.2 cP), continuous laminar stream into Riedel crystal glass, instant bubble burst on impact, and zero-carbonation still surface shown in the reference video.
```

### C. Respaldo Autónomo por Texto
Si el usuario no proporciona archivos de referencia, los descriptores del prompt maestro (§5) y el *negative prompt* (§6) garantizan por sí solos la física correcta en el motor de video.

---

## 📝 5. Bloque Canónico para Prompts de Video (Servido de Tequila)

Al redactar escenas de vertido en el Campo 8 (Desglose por escena) de `references/prompt-standards.md`, integrar obligatoriamente las siguientes cláusulas según la expresión:

### Para Loco Blanco / Puro Corazón:
```text
water-thin fluid dynamics (~1.2 cP), crisp high-velocity laminar stream pouring from the bottle mouth into a narrow tulip-shaped Riedel crystal tasting glass, dynamic liquid impact breaking into sharp crystalline micro-droplets, mechanical impact micro-bubbles that burst instantly upon reaching the surface, no bottom emitters, non-carbonated distilled agave spirit, completely still and inert liquid surface within 1.5 seconds after pouring, diamond-clear transparency with uniform light transmission and no central darkening, crisp thin transparent tequila tears draining smoothly down inner crystal walls, sharp refractive caustics and volcanic silver highlights
```

### Para Loco Ámbar / Áureo:
```text
water-thin fluid dynamics (~1.2 cP), crisp high-velocity laminar stream pouring from the bottle mouth into a narrow tulip-shaped Riedel crystal tasting glass, dynamic liquid impact breaking into sharp crystalline micro-droplets, mechanical impact micro-bubbles that burst instantly upon reaching the surface, no bottom emitters, non-carbonated distilled agave spirit, completely still and inert liquid surface within 1.5 seconds after pouring, luminous golden-amber translucency with uniform light transmission and no murky central darkening, crisp thin tears draining smoothly down inner crystal walls, radiant honey and copper specular reflections
```

---

## 🚫 6. Descriptores Mandatorios en Negative Prompt de Video

Todo prompt de video que muestre líquidos o vertido debe incluir sin excepción el bloque anti-viscosidad y anti-carbonatación:
```text
viscous, viscosity, syrupy, honey, honey-like pour, thick fluid, gelatinous, molasses, oil, oily texture, heavy sluggish liquid, gooey, slime, slow-motion goo, sticky syrup, lingering froth, soapy foam, bottom emitters, continuous bubbles from bottom, effervescent trail, carbonation, carbonated, effervescent, effervescence, fizzy, fizz, bubbles, bubbly, sparkling, sparkling wine, champagne, cider, apple cider, beer, beer head, ale, lager, fermented beverage, brewed beverage, cloudy liquid, hazy liquid, central darkening, shot glass, caballito, tumbler, flute glass, champagne flute
```
