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

// ===== DEFAULT_LEADERBOARD:START =====
// Respaldo generado por sub-skill/obtener-leaderboard-imagen/obtener_leaderboard.py
// No editar a mano: se regenera. Fecha del dataset: 2026-08-17
const DEFAULT_LEADERBOARD = {
  "last_updated": "2026-08-17",
  "source": "Design Arena — ranking en vivo vía API. Curaduría y tips: Loco Tequila.",
  "source_url": "https://www.designarena.ai/leaderboard/image",
  "source_api": "https://www.designarena.ai/api/leaderboard",
  "arena_category": "image",
  "elo_verified": true,
  "elo_disclaimer": "Elo y win rate obtenidos directamente de la API de Design Arena en la fecha indicada.",
  "anonymous_models_excluded": [
    "carillon_2",
    "babylon",
    "chestnut",
    "mantis",
    "uni-1.1-max",
    "uni-1.1",
    "aurora",
    "magnolia",
    "fennel",
    "juniper",
    "thistle",
    "boogu-image",
    "nucleus-image",
    "apple"
  ],
  "curated_fields": [
    "recommendation",
    "settings_tip",
    "loco_rating",
    "tags",
    "category",
    "badge"
  ],
  "categories": [
    "Todos",
    "Arte & Editorial",
    "Botellas & Cristal",
    "Tipografía & Etiquetas",
    "Ultra Realismo"
  ],
  "models": [
    {
      "rank": 1,
      "model_id": "riverflow-2.5-pro",
      "name": "riverflow-2.5-pro",
      "family": "riverflow",
      "developer": "Sourceful",
      "elo_score": 1404,
      "win_rate": 73.1,
      "battles": 10534,
      "avg_generation_ms": 201483,
      "badge": "Diseño Gráfico y Packaging",
      "category": "Tipografía & Etiquetas",
      "tags": [
        "Packaging",
        "Etiquetas",
        "Diseño Gráfico"
      ],
      "loco_rating": "⭐⭐⭐⭐",
      "recommendation": "Orientado a diseño gráfico y packaging: candidato para explorar variantes de etiqueta o presentación de estuche.",
      "settings_tip": "Describir el soporte físico (etiqueta, estuche, caja) y el acabado (mate, hot stamping, relieve).",
      "publicly_available": true
    },
    {
      "rank": 2,
      "model_id": "gpt-image-2",
      "name": "gpt-image-2",
      "family": "gpt-image",
      "developer": "OpenAI",
      "elo_score": 1384,
      "win_rate": 72.3,
      "battles": 53732,
      "avg_generation_ms": 66207,
      "badge": "Seguimiento de Instrucciones",
      "category": "Arte & Editorial",
      "tags": [
        "Prompt Largo",
        "Composición Compleja",
        "Texto Legible"
      ],
      "loco_rating": "⭐⭐⭐⭐⭐",
      "recommendation": "El más fiel a prompts largos y con muchas condiciones: ideal cuando el concepto exige varios elementos simultáneos (botella + fecha festiva + escenografía + paleta) sin que ignore ninguno.",
      "settings_tip": "Redactar el prompt en prosa ordenada por prioridad visual. Tolera bien instrucciones negativas escritas en lenguaje natural.",
      "publicly_available": true
    },
    {
      "rank": 3,
      "model_id": "grok-imagine-image-2",
      "name": "grok-imagine-image-2",
      "family": "grok",
      "developer": "xAI",
      "elo_score": 1315,
      "win_rate": 67.2,
      "battles": 5594,
      "avg_generation_ms": 82700,
      "badge": "Velocidad",
      "category": "Ultra Realismo",
      "tags": [
        "Rapidez",
        "Exploración",
        "Bocetos"
      ],
      "loco_rating": "⭐⭐⭐",
      "recommendation": "Para explorar rápido muchas variantes de un concepto antes de invertir en el render final.",
      "settings_tip": "Usar en fase de bocetaje; el acabado final conviene ejecutarlo en un modelo de mayor fidelidad.",
      "publicly_available": true
    },
    {
      "rank": 4,
      "model_id": "gemini-3.1-flash-image-gen-2k",
      "name": "gemini-3.1-flash-image-gen-2k",
      "family": "gemini",
      "developer": "Google DeepMind",
      "elo_score": 1296,
      "win_rate": 65.1,
      "battles": 89334,
      "avg_generation_ms": 23777,
      "badge": "Iteración y Edición",
      "category": "Ultra Realismo",
      "tags": [
        "Edición Conversacional",
        "Consistencia",
        "Rapidez"
      ],
      "loco_rating": "⭐⭐⭐⭐½",
      "recommendation": "El mejor para iterar sobre una toma ya aprobada: permite ajustar luz, fondo o encuadre conservando la botella, sin regenerar desde cero.",
      "settings_tip": "Partir de una imagen base y pedir cambios acotados de uno en uno. Útil para derivar los recortes por red (4:5, 9:16, 16:9) de un mismo maestro.",
      "publicly_available": true
    },
    {
      "rank": 5,
      "model_id": "seedream-5.0-pro",
      "name": "seedream-5.0-pro",
      "family": "seedream",
      "developer": "ByteDance",
      "elo_score": 1296,
      "win_rate": 60.1,
      "battles": 12879,
      "avg_generation_ms": 131780,
      "badge": "Estética Editorial",
      "category": "Arte & Editorial",
      "tags": [
        "Claroscuro",
        "Lujo",
        "Editorial",
        "Retrato de Producto"
      ],
      "loco_rating": "⭐⭐⭐⭐",
      "recommendation": "Buen rendimiento en bodegón de lujo con luz dura y sombra marcada; útil para el claroscuro editorial de la marca.",
      "settings_tip": "Especificar explícitamente el esquema de luz (single hard key light, deep shadow) para evitar iluminación plana.",
      "publicly_available": true
    },
    {
      "rank": 6,
      "model_id": "qwen-image-3",
      "name": "qwen-image-3",
      "family": "qwen",
      "developer": "Alibaba",
      "elo_score": 1282,
      "win_rate": 62.4,
      "battles": 6156,
      "avg_generation_ms": 130142,
      "badge": "Texto Bilingüe",
      "category": "Tipografía & Etiquetas",
      "tags": [
        "Texto en Imagen",
        "Bilingüe",
        "Composición"
      ],
      "loco_rating": "⭐⭐⭐½",
      "recommendation": "Alternativa cuando se requiere texto legible en la pieza y las opciones de tipografía no están disponibles.",
      "settings_tip": "Indicar el texto exacto entre comillas y su ubicación en el encuadre.",
      "publicly_available": true
    },
    {
      "rank": 7,
      "model_id": "mai-image-2.5",
      "name": "mai-image-2.5",
      "family": "mai-image",
      "developer": "Microsoft AI",
      "elo_score": 1238,
      "win_rate": 53.8,
      "battles": 20252,
      "avg_generation_ms": 20993,
      "badge": "Integración Office",
      "category": "Arte & Editorial",
      "tags": [
        "Accesible",
        "Flujo Corporativo",
        "Rapidez"
      ],
      "loco_rating": "⭐⭐⭐",
      "recommendation": "Conveniente si el equipo ya trabaja dentro del ecosistema Microsoft 365 (el mismo que la skill usa para auditar campañas previas en OneDrive). Calidad suficiente para bocetos, no para la pieza final.",
      "settings_tip": "Prompt descriptivo y directo; no espera parámetros tipo --ar, definir el encuadre en palabras.",
      "publicly_available": true
    },
    {
      "rank": 8,
      "model_id": "krea-2-medium",
      "name": "krea-2-medium",
      "family": "krea",
      "developer": "Krea",
      "elo_score": 1228,
      "win_rate": 49.5,
      "battles": 170790,
      "avg_generation_ms": 21598,
      "badge": "Control Estético",
      "category": "Arte & Editorial",
      "tags": [
        "Estilo Dirigido",
        "Referencias Visuales",
        "Texturas"
      ],
      "loco_rating": "⭐⭐⭐⭐",
      "recommendation": "Útil cuando ya existe una referencia estética de campaña previa (OneDrive) y se busca continuidad de estilo sin repetir el diseño.",
      "settings_tip": "Cargar referencia de estilo y bajar su peso para inspirarse sin clonar la pieza anterior.",
      "publicly_available": true
    },
    {
      "rank": 9,
      "model_id": "flux-2-flex",
      "name": "flux-2-flex",
      "family": "flux",
      "developer": "Black Forest Labs",
      "elo_score": 1221,
      "win_rate": 55.9,
      "battles": 61663,
      "avg_generation_ms": 19318,
      "badge": "Cristal y Refracción",
      "category": "Botellas & Cristal",
      "tags": [
        "Fotorrealismo",
        "Refracción de Líquidos",
        "Cristal",
        "Paisajes Agaveros"
      ],
      "loco_rating": "⭐⭐⭐⭐⭐",
      "recommendation": "Insuperable para la silueta estilizada de la botella, el brillo del cristal sobre obsidiana y las gotas de condensación en copas de degustación.",
      "settings_tip": "Aspect ratio 4:5 o 1:1, guidance_scale 3.5, 30–50 steps. No sobrecargar con palabras redundantes como 'photorealistic'.",
      "publicly_available": true
    },
    {
      "rank": 10,
      "model_id": "recraftv4_1_utility_pro_raster",
      "name": "recraftv4_1_utility_pro_raster",
      "family": "recraft",
      "developer": "Recraft",
      "elo_score": 1213,
      "win_rate": 53.2,
      "battles": 13052,
      "avg_generation_ms": 25923,
      "badge": "Consistencia de Marca",
      "category": "Arte & Editorial",
      "tags": [
        "Branding",
        "Control de Color HEX",
        "Composición Limpia"
      ],
      "loco_rating": "⭐⭐⭐⭐",
      "recommendation": "Ideal para aplicar con precisión los códigos de color institucionales (#6E1E28, #9B1C31, #A96C43) y mantener consistencia visual entre piezas de una misma campaña.",
      "settings_tip": "Preset 'Editorial / Digital Art Luxury' e inyectar la paleta de marca como color personalizado.",
      "publicly_available": true
    }
  ]
};
// ===== DEFAULT_LEADERBOARD:END =====

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
            <div class="score-lbl" title="${currentLeaderboard.elo_disclaimer || ''}">Elo Score${currentLeaderboard.elo_verified === false ? '*' : ''}</div>
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

  renderLeaderboardDisclaimer();
}

// Disclaimer de datos del leaderboard (regla de datos de la skill)
function renderLeaderboardDisclaimer() {
  const el = document.getElementById("leaderboard-disclaimer");
  if (!el) return;
  const lb = currentLeaderboard;
  const partes = [];
  if (lb.elo_verified === false) {
    partes.push(`<strong>*</strong> ${lb.elo_disclaimer || "[REFERENCIA DE INDUSTRIA] Elo no verificado."}`);
  } else if (lb.elo_disclaimer) {
    partes.push(lb.elo_disclaimer);
  }
  if (lb.last_updated) partes.push(`Dataset del ${lb.last_updated}.`);
  const omitidos = (lb.anonymous_models_excluded || []).length;
  if (omitidos) {
    partes.push(`Se omitieron ${omitidos} modelos en prueba ciega, sin disponibilidad pública.`);
  }
  partes.push("Las recomendaciones y tips de configuración son curaduría propia de Loco Tequila.");
  el.innerHTML = partes.join(" ");
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
