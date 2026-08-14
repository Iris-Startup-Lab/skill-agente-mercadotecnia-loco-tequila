/**
 * LOCO TEQUILA — SHOWCASE WEB / PASARELA DE PROMPTS & COPYS
 * Lógica interactiva de pasarela, leaderboard dinámico y copiado al portapapeles
 */

// Datos integrados de respaldo (fallback instantáneo si se abre vía file:// sin servidor local)
const DEFAULT_CAMPAIGN = {
  "brand": "Loco Tequila",
  "campaign_title": "Espíritu de Origen — Vendimia & Terruño",
  "date_context": "Día Nacional del Tequila / Temporada de Cosecha",
  "target_window": "Próximos 30 días",
  "items": [
    {
      "id": 1,
      "sku": "Loco Blanco",
      "sku_token": "--p-blanco",
      "sku_color": "#9B1C31",
      "inventiveness": "Original",
      "platform": "Instagram",
      "target_persona": "Leonardo (Visionario, conocedor contemporáneo)",
      "concept_title": "La Pureza Mineral de El Arenal",
      "filter_justification": "Desafía la idea del tequila blanco genérico exponiendo la raíz mineral y el agua pura del Bosque de la Primavera.",
      "prompt": {
        "text": "Ultra luxury editorial photography of a bespoke Loco Blanco Tequila bottle positioned gracefully on a dark obsidian volcanic stone in the historic agave fields of El Arenal, Jalisco. Golden hour dramatic side lighting, warm sunset casting amber and crimson reflections on the pristine transparent liquid inside the bottle. High-end crystal tasting glass beside the bottle with delicate condensation droplets and subtle tequila legs. Deep rich contrast, shallow depth of field (85mm f/1.4 lens, f/2.0 aperture), cinematic luxury atmosphere, background showing subtle blue agave silhouettes under a cochineal red dusk sky. Shot on Hasselblad H6D-100c, 8k resolution, crisp glass textures, pristine liquid refraction, no text artifacts.",
        "aspect_ratio": "4:5 (1080x1350 px)",
        "negative_prompt": "underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution, plastic, cartoon, extra bottles",
        "camera_settings": "85mm f/1.4, ISO 100, 1/250s, natural golden hour rim light + studio black bounce reflector",
        "color_palette": "Crimson (#9B1C31), Obsidian Black (#0E0E10), Golden Sun (#F2C14E), Raw Agave Blue"
      },
      "copy": {
        "headline": "La pureza no se inventa: nace del terruño volcánico.",
        "body": "En las faldas del volcán de Tequila, donde el agua cristalina del Bosque de la Primavera nutre agaves centenarios, nace Loco Blanco. Una destilación de autor sin atajos ni artificios: solo la mineralidad pura de El Arenal en su máxima expresión.\n\nPara quienes no siguen tendencias, sino orígenes excepcionales.",
        "keywords": ["tequila blanco premium", "tequila de terruño", "destilado de autor", "Locura Genial"],
        "call_to_action": "Descubre la colección completa en el enlace de nuestra biografía.",
        "legal": "+18 | Evita el exceso",
        "hashtags": ["#EspírituDeOrigen", "#LocoTequila", "#TequilaDeTerruño", "#ElArenalJalisco", "#DestiladoDeAutor"]
      }
    },
    {
      "id": 2,
      "sku": "Loco Ámbar",
      "sku_token": "--p-ambar",
      "sku_color": "#A96C43",
      "inventiveness": "Locura Genial",
      "platform": "LinkedIn",
      "target_persona": "Alejandro (UHNWI, coleccionista, mentor)",
      "concept_title": "La Alquimia de las 4 Barricas",
      "filter_justification": "Provocación técnica: desafía la maduración convencional reposando en cuatro maderas distintas sin perder la pureza del terruño.",
      "prompt": {
        "text": "Cinematic luxury still life of the prestigious Loco Ámbar Tequila bottle set inside a private dimly lit architectural tasting cellar in Hacienda La Providencia. Dramatic chiaroscuro lighting sculpting the bottle's amber tones and rich golden reflections. Beside the bottle rests an exquisite snifter glass containing aged tequila, illuminated by a warm beam of spotlight highlighting velvety tears on the crystal. In the deep blurred background, authentic French and American oak barrel staves with refined textures. Deep crimson and obsidian shadow palette, high dynamic range, masterwork editorial composition, Hasselblad medium format look, rich tactile wood grain, glowing amber hues, 8k hyper-detailed.",
        "aspect_ratio": "16:9 (1920x1080 px)",
        "negative_prompt": "underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution, cluttered, overexposed",
        "camera_settings": "50mm f/1.8 lens, ISO 200, 1/125s, key light with soft grid + warm amber rim accent",
        "color_palette": "Rich Amber (#A96C43), Deep Maroon (#6E1E28), Warm Gold (#E8A33D), Obsidian Shadow"
      },
      "copy": {
        "headline": "La maduración también puede ser un acto de disrupción.",
        "body": "El verdadero liderazgo no replica fórmulas establecidas; redefine los estándares de la categoría. Loco Ámbar desafía la maduración tradicional a través de un reposo inusual en cuatro barricas distintas, logrando un equilibrio sofisticado donde la madera enaltece el agave sin enmascarar su terruño.\n\nUna pieza para coleccionistas que aprecian la maestría artesanal y la visión fuera de serie.",
        "keywords": ["tequila reposado 4 barricas", "tequila de colección para coleccionistas de arte", "Locura Genial", "maestría en sabores y aromas"],
        "call_to_action": "Conoce los puntos de cata exclusiva para miembros de nuestra comunidad.",
        "legal": "+18 | Evita el exceso",
        "hashtags": ["#EspírituDeOrigen", "#LocoTequila", "#AltaGama", "#ColeccionistasDeArte", "#LiderazgoConPropósito"]
      }
    },
    {
      "id": 3,
      "sku": "Loco Puro Corazón",
      "sku_token": "--p-corazon",
      "sku_color": "#9A9A9A",
      "inventiveness": "Original",
      "platform": "Instagram",
      "target_persona": "Ana (HNWI, disruptiva, coleccionista de arte)",
      "concept_title": "El Corte Tripartita Imposible",
      "filter_justification": "Creatividad trascendental: aislar únicamente el centro del corazón de la destilación en una botella de líneas arquitectónicas puras.",
      "prompt": {
        "text": "High fashion luxury editorial product shot featuring the iconic Loco Puro Corazón bottle centered on a minimalist white sculpted marble pedestal with raw fractured volcanic stone edges. High contrast studio lighting, soft cochineal maroon gradient backdrop, flawless crystal refraction of the ultra-premium clear spirit. Elegant bespoke stemmed tulip tequila glass catching a sharp crystalline reflection. Ultra-refined composition, crisp edges, modern art gallery ambiance, luxury perfume-grade lighting, medium format Hasselblad 100MP, zero digital grain, ultra high fidelity.",
        "aspect_ratio": "4:5 (1080x1350 px)",
        "negative_prompt": "underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution, noisy, dirty surfaces",
        "camera_settings": "90mm Tilt-Shift lens, f/8 for total plane sharpness, strobe softbox overhead + dual strip lights with crimson gels",
        "color_palette": "Cochineal Red (#6E1E28), Bone White (#FBF3DD), Pure Crystal Silver, Obsidian Charcoal"
      },
      "copy": {
        "headline": "Solo el corazón del destilado. Nada menos.",
        "body": "Cuando el arte contemporáneo y el legado destilador convergen, nace Loco Puro Corazón. Un corte infinitesimal de la destilación que extrae únicamente la esencia más noble y etérea del agave.\n\nDiseñado para quienes entienden que el verdadero lujo radica en lo que se decide no incluir.",
        "keywords": ["tequila blanco de lujo", "tequila disruptivo", "tequila y arte contemporáneo mexicano", "tequila objeto de arte"],
        "call_to_action": "Disponible en reservas limitadas para conocedores.",
        "legal": "+18 | Evita el exceso",
        "hashtags": ["#EspírituDeOrigen", "#LocoPuroCorazón", "#ArteContemporáneo", "#LuxurySpirits", "#TequilaDeColección"]
      }
    },
    {
      "id": 4,
      "sku": "Loco Hierofante",
      "sku_token": "--p-269",
      "sku_color": "#1F1F1F",
      "inventiveness": "Locura Genial",
      "platform": "Facebook",
      "target_persona": "Alejandro / Ana (Círculo EÓN Hierofante)",
      "concept_title": "El Objeto de Arte Tripartita",
      "filter_justification": "Unión insólita de escultura de autor (Jan Hendrix & Iker Ortiz) con la más alta alquimia de tequila añejo de terruño.",
      "prompt": {
        "text": "Museum gallery presentation of the ultra-exclusive Loco Hierofante art bottle created in collaboration with Jan Hendrix and Iker Ortiz. The sculpted masterpiece bottle with oxidized silver and volcanic basalt textures rests inside an illuminated glass museum vitrine. Dramatic pinpoint beam lighting falling strictly from above, casting intricate artistic shadows on a polished dark obsidian floor. Surrounding atmosphere dark and reverent, deep burgundy velvet ambient tones, exquisite museum depth of field, ultra-luxury tactile textures, 8k resolution, Leica SL2 50mm Summilux look.",
        "aspect_ratio": "1:1 (1080x1080 px)",
        "negative_prompt": "underage, minors, drunk, drunkenness, excessive drinking, cheap glass, competitor bottles, Casa Dragones bottle, Clase Azul bottle, text watermark, blurry, low resolution, crowded, kitsch",
        "camera_settings": "50mm f/1.4, ISO 50, 1/160s, narrow beam ceiling spotlight (CRI 98) + subtle floor rim bounce",
        "color_palette": "Deep Obsidian (#0E0E10), Volcanic Silver (#9A9A9A), Burgundy Wine (#5A1822), Platinum"
      },
      "copy": {
        "headline": "Donde el tequila trasciende su naturaleza para convertirse en obra de arte.",
        "body": "Loco Hierofante no es solo un destilado excepcional; es una escultura tripartita concebida junto a los maestros Jan Hendrix e Iker Ortiz. Una pieza numerada de culto que inaugura una nueva dimensión para el coleccionismo internacional.\n\nPertenecer al círculo EÓN Hierofante es custodiar un fragmento del alma de El Arenal.",
        "keywords": ["obra de arte tripartita", "círculo de membresía EÓN Hierofante", "tequila objeto de arte", "tequila de colección para coleccionistas de arte"],
        "call_to_action": "Solicita acceso privado a la curaduría EÓN.",
        "legal": "+18 | Evita el exceso",
        "hashtags": ["#EspírituDeOrigen", "#LocoHierofante", "#JanHendrix", "#IkerOrtiz", "#ObjetoDeArte", "#EÓNHierofante"]
      }
    }
  ]
};

const DEFAULT_LEADERBOARD = {
  "last_updated": "2026-08-14",
  "source": "Design Arena & Industry Benchmarks",
  "source_url": "https://www.designarena.ai/leaderboard?tab=image",
  "categories": ["Todos", "Ultra Realismo", "Botellas & Cristal", "Tipografía & Etiquetas", "Arte & Editorial"],
  "models": [
    {
      "rank": 1,
      "name": "FLUX.1 [pro] / FLUX.2",
      "developer": "Black Forest Labs",
      "elo_score": 1285,
      "badge": "Líder Global 2026",
      "category": "Botellas & Cristal",
      "tags": ["Fotorrealismo", "Refracción de Líquidos", "Cristal", "Paisajes Agaveros"],
      "loco_rating": "⭐⭐⭐⭐⭐ (Recomendación #1)",
      "recommendation": "Insuperable para la silueta estilizada de Loco Tequila, el brillo del cristal de obsidiana y las gotas de condensación en copas de degustación.",
      "settings_tip": "Aspect ratio 4:5 o 1:1, guidance_scale: 3.5, 30-50 steps. No sobrecargar con palabras redundantes como 'photorealistic'."
    },
    {
      "rank": 2,
      "name": "Midjourney v6.1",
      "developer": "Midjourney",
      "elo_score": 1272,
      "badge": "Maestría Editorial",
      "category": "Arte & Editorial",
      "tags": ["Claroscuro", "Texturas Artesanales", "Lujo", "Editorial"],
      "loco_rating": "⭐⭐⭐⭐⭐ (Recomendación #1 en Estilo)",
      "recommendation": "La mejor opción para capturar el misticismo del Paisaje Agavero al atardecer en El Arenal, Hacienda La Providencia y tomas editoriales dramáticas.",
      "settings_tip": "Usar parámetros --ar 4:5 --style raw --v 6.1 --s 250 para evitar sobre-estilización de fantasía."
    },
    {
      "rank": 3,
      "name": "Google Imagen 3",
      "developer": "Google DeepMind",
      "elo_score": 1258,
      "badge": "Fidelidad Fotográfica",
      "category": "Ultra Realismo",
      "tags": ["Color Natural", "Fidelidad", "Luz Natural", "Terruño"],
      "loco_rating": "⭐⭐⭐⭐½",
      "recommendation": "Excelente para destacar los tonos rojos cochinilla, tierra volcánica y el agua cristalina del Bosque de la Primavera sin saturación artificial.",
      "settings_tip": "Excelente respuesta a descripciones de composición y lentes fotográficos (85mm f/1.4 lens, shallow depth of field)."
    },
    {
      "rank": 4,
      "name": "Ideogram 2.0",
      "developer": "Ideogram",
      "elo_score": 1245,
      "badge": "Líder en Tipografía",
      "category": "Tipografía & Etiquetas",
      "tags": ["Texto en Botella", "Etiquetas de Lujo", "Tipografía Nítida"],
      "loco_rating": "⭐⭐⭐⭐½",
      "recommendation": "La herramienta predilecta si el prompt requiere renderizar textualmente el nombre 'Loco Tequila' o el tagline 'Espíritu de Origen' sobre la botella o etiqueta.",
      "settings_tip": "Poner los textos entre comillas dobles \"Loco Tequila\" y usar estilo Realistic/Design."
    },
    {
      "rank": 5,
      "name": "Recraft v3",
      "developer": "Recraft",
      "elo_score": 1238,
      "badge": "Consistencia de Marca",
      "category": "Arte & Editorial",
      "tags": ["Branding", "Control de Color HEX", "Composición Limpia"],
      "loco_rating": "⭐⭐⭐⭐",
      "recommendation": "Ideal para aplicar con precisión los códigos de color exactos de Loco Tequila (#6E1E28, #9B1C31, #A96C43) y mantener consistencia visual.",
      "settings_tip": "Seleccionar el preset 'Editorial / Digital Art Luxury' e inyectar paleta de color personalizada."
    },
    {
      "rank": 6,
      "name": "Stable Diffusion 3.5 Large",
      "developer": "Stability AI",
      "elo_score": 1226,
      "badge": "Máximo Control Técnico",
      "category": "Ultra Realismo",
      "tags": ["LoRAs Propios", "ControlNet", "Generación Offline"],
      "loco_rating": "⭐⭐⭐⭐",
      "recommendation": "Recomendado para equipos técnicos que entrenen un LoRA específico de la botella real de Loco Blanco, Ámbar o Hierofante para reproducción exacta.",
      "settings_tip": "Utilizar con ComfyUI / Forge, DPM++ 2M Karras, CFG 4.5, Negative Prompt estricto."
    }
  ]
};

// Estado global de la aplicación
let currentCampaign = DEFAULT_CAMPAIGN;
let currentLeaderboard = DEFAULT_LEADERBOARD;
let activeIndex = 0;
let currentCategoryFilter = "Todos";

// Inicialización
document.addEventListener("DOMContentLoaded", async () => {
  await loadData();
  renderHero();
  renderConceptTabs();
  renderStage();
  renderLeaderboardFilters();
  renderLeaderboard();
  setupEventListeners();
});

// Carga asíncrona de datos con fallback
async function loadData() {
  try {
    const campaignRes = await fetch("data/campaign.json");
    if (campaignRes.ok) currentCampaign = await campaignRes.json();
  } catch (e) {
    console.warn("Usando dataset de campaña de respaldo:", e);
  }

  try {
    const leaderboardRes = await fetch("data/leaderboard.json");
    if (leaderboardRes.ok) currentLeaderboard = await leaderboardRes.json();
  } catch (e) {
    console.warn("Usando leaderboard de respaldo:", e);
  }
}

// Render del Hero
function renderHero() {
  document.getElementById("hero-campaign-title").textContent = currentCampaign.campaign_title;
  document.getElementById("hero-date-context").textContent = currentCampaign.date_context;
  document.getElementById("hero-target-window").textContent = currentCampaign.target_window;
}

// Render de Tabs de Conceptos
function renderConceptTabs() {
  const container = document.getElementById("concept-tabs-container");
  container.innerHTML = "";

  currentCampaign.items.forEach((item, index) => {
    const tab = document.createElement("button");
    tab.className = `concept-tab-pill ${index === activeIndex ? "active" : ""}`;
    tab.innerHTML = `
      <span class="dot" style="background-color: ${item.sku_color}"></span>
      <span>${item.sku} — ${item.inventiveness}</span>
    `;
    tab.addEventListener("click", () => {
      activeIndex = index;
      updateActiveTab();
      renderStage();
    });
    container.appendChild(tab);
  });
}

function updateActiveTab() {
  const tabs = document.querySelectorAll(".concept-tab-pill");
  tabs.forEach((tab, idx) => {
    if (idx === activeIndex) tab.classList.add("active");
    else tab.classList.remove("active");
  });
}

// Render de la Pasarela (Stage Principal)
function renderStage() {
  const item = currentCampaign.items[activeIndex];
  if (!item) return;

  // Contador
  document.getElementById("concept-counter-display").textContent = `${activeIndex + 1} / ${currentCampaign.items.length}`;

  // Header del Stage
  const skuBadge = document.getElementById("stage-sku-badge");
  skuBadge.textContent = item.sku;
  skuBadge.style.backgroundColor = item.sku_color;

  document.getElementById("stage-inventiveness-badge").textContent = item.inventiveness;
  document.getElementById("stage-platform-badge").textContent = item.platform;
  document.getElementById("stage-persona-text").textContent = `Persona: ${item.target_persona}`;

  // Bloque de PROMPT
  document.getElementById("prompt-title").textContent = `Prompt ${activeIndex + 1} · ${item.concept_title}`;
  document.getElementById("prompt-text-display").textContent = item.prompt.text;
  document.getElementById("meta-aspect-ratio").textContent = item.prompt.aspect_ratio;
  document.getElementById("meta-camera").textContent = item.prompt.camera_settings;
  document.getElementById("meta-palette").textContent = item.prompt.color_palette;
  document.getElementById("meta-filter-just").textContent = item.filter_justification;

  // Bloque de COPY
  document.getElementById("copy-title").textContent = `Copy ${activeIndex + 1} · Nativo para ${item.platform}`;
  document.getElementById("copy-headline-display").textContent = item.copy.headline;
  document.getElementById("copy-body-display").textContent = item.copy.body;

  // Keywords
  const kwContainer = document.getElementById("copy-keywords-container");
  kwContainer.innerHTML = "";
  item.copy.keywords.forEach(kw => {
    const badge = document.createElement("span");
    badge.className = "keyword-badge";
    badge.textContent = kw;
    kwContainer.appendChild(badge);
  });

  // Hashtags
  const hashContainer = document.getElementById("copy-hashtags-container");
  hashContainer.innerHTML = item.copy.hashtags.map(h => `<span>${h}</span>`).join(" ");

  // Legal
  document.getElementById("copy-legal-display").textContent = `${item.copy.legal} · ${item.copy.call_to_action}`;
}

// Render de Filtros de Leaderboard
function renderLeaderboardFilters() {
  const container = document.getElementById("leaderboard-filters");
  container.innerHTML = "";

  currentLeaderboard.categories.forEach(cat => {
    const btn = document.createElement("button");
    btn.className = `filter-btn ${cat === currentCategoryFilter ? "active" : ""}`;
    btn.textContent = cat;
    btn.addEventListener("click", () => {
      currentCategoryFilter = cat;
      document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      renderLeaderboard();
    });
    container.appendChild(btn);
  });
}

// Render de Tarjetas del Leaderboard
function renderLeaderboard() {
  const container = document.getElementById("models-grid-container");
  container.innerHTML = "";

  const filtered = currentCategoryFilter === "Todos"
    ? currentLeaderboard.models
    : currentLeaderboard.models.filter(m => m.category === currentCategoryFilter || m.tags.includes(currentCategoryFilter));

  filtered.forEach(m => {
    const card = document.createElement("div");
    card.className = `model-card ${m.rank <= 2 ? "top-rank" : ""}`;
    card.innerHTML = `
      <div>
        <div class="model-header">
          <div>
            <div class="model-name">${m.name}</div>
            <div class="model-dev">${m.developer} · <span style="color: var(--brand-gold-bright)">${m.badge}</span></div>
          </div>
          <div class="elo-score-box">
            <div class="score-val">${m.elo_score}</div>
            <div class="score-lbl">Elo Score</div>
          </div>
        </div>
        <div class="model-loco-rating">${m.loco_rating}</div>
        <div class="model-recommendation">${m.recommendation}</div>
      </div>
      <div class="model-tip-box">
        <strong>Tip de Configuración:</strong> ${m.settings_tip}
      </div>
    `;
    container.appendChild(card);
  });
}

// Event Listeners y Copiado al Portapapeles
function setupEventListeners() {
  // Navegación Pasarela
  document.getElementById("btn-prev-concept").addEventListener("click", () => {
    activeIndex = (activeIndex - 1 + currentCampaign.items.length) % currentCampaign.items.length;
    updateActiveTab();
    renderStage();
  });

  document.getElementById("btn-next-concept").addEventListener("click", () => {
    activeIndex = (activeIndex + 1) % currentCampaign.items.length;
    updateActiveTab();
    renderStage();
  });

  // Teclado
  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") document.getElementById("btn-prev-concept").click();
    if (e.key === "ArrowRight") document.getElementById("btn-next-concept").click();
  });

  // Switch de modos de vista (Ambos, Solo Prompt, Solo Copy)
  const viewBtns = document.querySelectorAll(".view-switch-btn");
  viewBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      viewBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const mode = btn.getAttribute("data-mode");
      applyViewMode(mode);
    });
  });

  // Copiar Prompt
  const copyPromptBtn = document.getElementById("btn-copy-prompt");
  if (copyPromptBtn) {
    copyPromptBtn.addEventListener("click", () => {
      const item = currentCampaign && currentCampaign.items ? currentCampaign.items[activeIndex] : null;
      const textToCopy = item ? `${item.prompt.text}\n\n--ar ${item.prompt.aspect_ratio} --no ${item.prompt.negative_prompt}` : document.getElementById("prompt-text-display").innerText;
      copyToClipboard(textToCopy, "Prompt copiado al portapapeles", copyPromptBtn);
    });
  }

  // Copiar Copy
  const copyCopyBtn = document.getElementById("btn-copy-copy");
  if (copyCopyBtn) {
    copyCopyBtn.addEventListener("click", () => {
      const item = currentCampaign && currentCampaign.items ? currentCampaign.items[activeIndex] : null;
      const textToCopy = item ? `${item.copy.headline}\n\n${item.copy.body}\n\n${item.copy.call_to_action}\n\n${item.copy.hashtags.join(' ')}\n\n${item.copy.legal}` : `${document.getElementById("copy-headline-display").innerText}\n\n${document.getElementById("copy-body-display").innerText}`;
      copyToClipboard(textToCopy, "Copy nativo copiado al portapapeles", copyCopyBtn);
    });
  }

  // Copiar Negative Prompt Global
  const copyNegBtn = document.getElementById("btn-copy-negative");
  if (copyNegBtn) {
    copyNegBtn.addEventListener("click", () => {
      const negText = document.getElementById("negative-prompt-text").innerText;
      copyToClipboard(negText, "Negative Prompt copiado", copyNegBtn);
    });
  }
}

function applyViewMode(mode) {
  const promptZone = document.querySelector(".prompt-zone");
  const connector = document.querySelector(".runway-connector");
  const copyZone = document.querySelector(".copy-zone");

  if (!promptZone || !copyZone) return;

  if (mode === "all") {
    promptZone.classList.remove("zone-hidden");
    if (connector) connector.classList.remove("zone-hidden");
    copyZone.classList.remove("zone-hidden");
  } else if (mode === "prompt") {
    promptZone.classList.remove("zone-hidden");
    if (connector) connector.classList.add("zone-hidden");
    copyZone.classList.add("zone-hidden");
  } else if (mode === "copy") {
    promptZone.classList.add("zone-hidden");
    if (connector) connector.classList.add("zone-hidden");
    copyZone.classList.remove("zone-hidden");
  }
}

// Utilidad de Copiado Universal (100% compatible con iframes, sandboxes y Claude Artifacts)
function copyToClipboard(text, toastMsg, buttonEl) {
  if (!text) return;

  let successful = false;

  // Intento 1: API de textarea temporal (funciona dentro de iframes sin permisos de clipboard)
  try {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.left = "-9999px";
    textArea.style.top = "-9999px";
    textArea.style.opacity = "0";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    successful = document.execCommand("copy");
    document.body.removeChild(textArea);
  } catch (err) {
    successful = false;
  }

  // Intento 2: API moderna navigator.clipboard
  if (!successful && navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(toastMsg);
      highlightButton(buttonEl);
    }).catch(err => {
      console.warn("Fallo de copiado directo:", err);
      promptFallback(text);
    });
    return;
  }

  if (successful) {
    showToast(toastMsg);
    highlightButton(buttonEl);
  } else {
    promptFallback(text);
  }
}

function highlightButton(buttonEl) {
  if (!buttonEl) return;
  const originalHTML = buttonEl.innerHTML;
  buttonEl.classList.add("copied");
  buttonEl.innerHTML = `
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
    ¡Copiado!
  `;
  setTimeout(() => {
    buttonEl.classList.remove("copied");
    buttonEl.innerHTML = originalHTML;
  }, 2000);
}

function promptFallback(text) {
  window.prompt("Copia el texto manualmente con Ctrl+C / Cmd+C:", text);
}

function showToast(msg) {
  const container = document.getElementById("toast-container");
  if (!container) return;
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = `
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#F2C14E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M20 6L9 17l-5-5"/>
    </svg>
    <span>${msg}</span>
  `;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(10px)";
    toast.style.transition = "all 0.3s ease";
    setTimeout(() => toast.remove(), 300);
  }, 2500);
}
