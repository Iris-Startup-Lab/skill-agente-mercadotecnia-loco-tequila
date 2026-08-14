# Calendario de fechas del mundo de las bebidas — Loco Tequila

Fuente estática de fechas especiales relacionadas con bebidas alcohólicas y prioridades de marca. Estas fechas son **fijas o de regla calendárica** y se extrapolan a cualquier año (no dependen del año de publicación de las fuentes). Complementa a la sub-skill `obtener-feriados-oficiales-no-oficiales`, que detecta los feriados de México vía script.

Fuentes:
- WSET — "The 2026 drinks calendar": https://www.wsetglobal.com/knowledge-centre/blog/2025/the-2026-drinks-calendar
- Gobierno de México — "El Día Nacional del Tequila ya es oficial": https://www.gob.mx/agricultura/articulos/el-dia-nacional-del-tequila-ya-es-oficial-en-mexico?idiom=es

## 1. Fechas ancla de tequila (máxima prioridad)

| Fecha | Evento | Nota |
|---|---|---|
| **24 de julio** | **Día Nacional del Tequila (México)** | Oficial en México (Decreto publicado en DOF el 28/05/2026). Sustituye al antiguo "tercer sábado de marzo" (decreto de 2018, abrogado). |
| **24 de julio** | World Tequila Day | Coincide con el Día Nacional del Tequila. Fecha doblemente relevante. |

## 2. Fechas de coctelería y destilados (WSET)

Fechas fijas, aplicables a cualquier año:

| Fecha | Evento |
|---|---|
| 11 enero | Hot Toddy Day |
| 25 enero | National Irish Coffee Day |
| 7 febrero | International Pisco Sour Day *(primer sábado de febrero)* |
| 8 febrero | International Scotch (whisky) Day |
| 22 febrero | **International Margarita Day** |
| 24 febrero | World Bartender Day |
| 3 marzo | International Irish Whiskey Day |
| 21 marzo | World Vermouth Day |
| 27 marzo | International Whisk(e)y Day |
| 7 abril | National Beer Day (USA) |
| 23 abril | German Beer Day |
| 13 mayo | **World Cocktail Day** |
| 16 mayo | World Whisky Day *(tercer sábado de mayo)* |
| 4 junio | International Cognac Day |
| 13 junio | World Gin Day *(segundo sábado de junio)* |
| 19 junio | National Martini Day |
| 11 julio | World Rum Day / World Mojito Day |
| 19 julio | National Daiquiri Day |
| 24 julio | **World Tequila Day** |
| 7 agosto | International Beer Day |
| 30 agosto | World Mai Tai Day |
| 20 sept – 5 oct | Oktoberfest |
| 1 octubre | World Sake Day |
| 4 octubre | International Vodka Day |
| 19 octubre | International Gin & Tonic Day |
| 20 octubre | International Calvados Day |
| 5 noviembre | International Stout Day |
| 18 noviembre | International Poitín Day |
| 12 diciembre | Coquito Day |

> Las fechas marcadas con *(regla)* son móviles dentro de su mes; el resto son fijas cada año.

## 3. Prioridades de marca (obligatorio considerarlas primero)

La marca da especial importancia a estas temporadas mexicanas. Ante cualquier campaña, estas son las fechas prioritarias a considerar:

| Temporada | Fechas | Ángulo sugerido |
|---|---|---|
| **Fiestas Patrias** | 15 de septiembre (Grito de Dolores) · 16 de septiembre (Día de la Independencia) | Mexicaneidad, orgullo, terruño, celebración; el tequila como símbolo nacional. |
| **Día de Muertos** | 1–2 de noviembre | Memoria, legado, ofrenda, honra a lo que trasciende; arte y cultura mexicana. |
| **Fin de año** | 24 dic (Nochebuena) · 25 dic (Navidad) · 31 dic / 1 ene (Año Nuevo) | Cierre de ciclo, celebración, brindis, "celebrar la vida". |

## 4. Reglas de uso

- **Anticipación:** la skill debe avisar al usuario de las fechas próximas por defecto **un mes antes** de cada fecha (ventana ajustable si el usuario lo pide).
- **Jerarquía:** priorizar (1) prioridades de marca → (2) fechas ancla de tequila → (3) resto de fechas de coctelería/destilados, según el producto y el ángulo de la campaña.
- **Anclaje al copy:** cada campaña debe nombrar la fecha festiva de forma explícita y coherente (ej. "Día Nacional del Tequila", "Fiestas Patrias", "Día de Muertos") sin inventar fechas ni variar nombres.
- **No inventar fechas:** si se requiere una fecha que no está en esta lista ni en los feriados detectados por la sub-skill, marcarla como `[no disponible]` o pedir confirmación al usuario.
