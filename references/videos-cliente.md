# Lenguaje audiovisual de los videos reales de Loco Tequila (referencia para prompts de video)

**Lectura obligatoria antes de escribir cualquier prompt de video** (paso 9). Resume 8 videos reales publicados por el cliente (Loco Tequila MX) para que los videos generados con IA hablen el mismo idioma visual. La norma de *cómo se escribe* el prompt vive en `prompt-standards.md` §2; aquí está *qué se filma*.

> Esto es estilo de filmación, no memoria de marca. Los hechos de producto siguen viviendo solo en `brand-context.md` y `productos.md`. Donde un video real contradice esos archivos (hielo o vaso corto en coctelería), **prevalece `brand-context.md`**: la regla estricta se mantiene.

---

## 1. Inventario de los 8 videos

| Video | Duración | Producto(s) | Ocasión | Tomas aprox.* | Rasgo clave |
| --- | --- | --- | --- | --- | --- |
| *Celebra la travesía de la vida* | 16 s | Ámbar | Navidad | 7 | Pareja madura, brindis, cenitales de mimbre y regalos, *unboxing* |
| *Coleccionar momentos inolvidables* | 22 s | Ámbar | Cosecha / Acción de Gracias | 6–8 | Bodegón con pavo y candelabros; texto partido en 5 tarjetas |
| *Un brindis con Loco Tequila* (Casa Virginia) | 32 s | Ámbar + Blanco + Puro Corazón | Acción de Gracias de gala | 14–16 | Mesa imperial con velas, brindis colectivo, carrito de bar |
| *La elegancia y el lujo* (subasta) | 32 s | Ámbar | Subasta de arte | 18–20 | Cortes rápidos, macros de lotes, luz de vitrina joyera |
| *Moda y arte se fusionaron* | 33 s | Los tres | Fashion fest | 18–22 | Luz natural de ventanal, taller de modas, brindis de cuatro |
| *En Gran Cantina Filomeno* | 42 s | Ámbar | Temporada de chiles en nogada | 16–18 | Macros de cocina, nogada en cámara lenta, olfacción en copa |
| *Loco Ámbar, el protagonista* (Fónico) | 59 s | Ámbar | Acción de Gracias con chef | 20–24 | Arquitectura, cocina, corte de pavo, vertidos a 45° |
| *El arte de enaltecer nuestras tradiciones* | 1:23 | Los tres | Día de Muertos con chef | 28–32 | Drone de apertura, maridaje en tres tiempos |

\* Estimación a partir de los bloques de tiempo de cada auditoría: ninguna cuenta los cortes uno por uno. La auditoría de *Coleccionar…* está incompleta (solo el primer bloque).

## 2. Reglas de filmación que el agente aplica

### 2.1 Formato, duración y ritmo
- **9:16** en todos los videos que declaran formato.
- Rangos reales: reel de producto 16–22 s; cobertura de evento 32–42 s; colaboración con chef 59–83 s. Para videos generados, **20–30 s** es lo más parecido al reel de producto.
- **Ritmo de corte de 1.5–3 s por toma**; bodegones de apertura y cierre de 3–4 s. Un tramo de 10 s es material para **2–4 cortes en el montaje**: el prompt pide una sola acción continua y el editor la corta.

### 2.2 Mezcla de tomas (guía para repartir los tramos)
| Tipo de toma | Peso aprox. | Cómo se ve |
| --- | --- | --- |
| Bodegón / producto héroe | 25–35 % | Botella **con copa servida**, casi siempre con comida o atrezo de temporada |
| Detalle macro | 25–30 % | Comida, vertido, cuello de la botella, relieve del logo |
| Personas o manos | 20–25 % | Manos que brindan o sostienen la copa por el tallo; invitados conversando |
| Plano general de ubicación | 10–15 % | Fachada, letrero, arquitectura, drone; casi siempre al inicio |
| Brindis | 1 toma | En el último tercio (o como gancho de apertura) |

En un video de 3 tramos, una distribución típica es: tramo 1 ubicación o gancho → tramo 2 bodegón y detalle → tramo 3 personas y brindis. Cada cambio de tipo de toma es un tramo de tipo **corte** (`cut`); los tramos que siguen la misma toma son de tipo **continuación** (`continuation`) — ver `prompt-standards.md` §2.3.

### 2.3 Apertura y cierre
- **Apertura:** plano general del lugar (fachada, letrero, arquitectura) o un gancho de producto (brindis, platillo protagonista).
- **Penúltima toma:** bodegón final de botella con copa, o el brindis.
- **Cierre:** **siempre el logo «Loco» en rojo vítreo, en relieve, sobre fondo negro, 1–3 s, sin voz**. Este end card **no se genera con IA**: se monta en postproducción con el logo oficial.

### 2.4 Luz
- Cálida y dorada: **velas cónicas y candelabros**, chimenea, luz lateral rasante.
- **Contraluz** que enciende el líquido y saca destellos de la base maciza.
- De día: luz natural suave de patio o ventanal. De noche en evento: focos de galería con penumbra cálida.

### 2.5 Lente, cámara y paleta
- **f/1.4–f/2.8**, poca profundidad de campo, bokeh marcado; logo y cuello siempre en foco.
- Movimientos **lentos**: traveling a lo largo de la mesa, *flat lay* cenital a 90°, vertidos a 45°, cámara lenta en lo que cae (granada, salsa). Los paneos rápidos solo para montajes de evento.
- Paleta: ámbar/dorado, rojo cochinilla o vino, marfil/lino crudo, maderas oscuras, bronce u oro; acentos de temporada (cempasúchil, granada, esferas rojas mate, tejocote).

### 2.6 Atrezo recurrente
Velas y candelabros de bronce · cuadro contemporáneo de agave en blanco y negro (referencia artística Jan Hendrix) · bandeja dorada · mesa de madera noble o mesa imperial con mantel blanco · frutos secos y de temporada · carrito de bar · cerámica de autor y flores secas. Toda comida, **en vajilla** (`evaluacion-sentido-comun-escena.md`).

### 2.7 Personas
- Adultos **visiblemente de 30 a 55 años**, con sastrería o ropa de gala (blazer marfil, smoking, vestido de lentejuela, lino).
- Preferir **manos y planos medios**: copa tomada por el tallo, brindis, olfacción en copa, conversación.
- **Nunca** consumo acelerado, beber de golpe ni signos de exceso. **Nunca** personas reales identificables (chefs, anfitriones o celebridades de los videos): personajes genéricos, sin nombres (likeness; `manual-cumplimiento-ia-2026.md`).

### 2.8 Texto en pantalla (siempre en postproducción)
- Poco texto: **una frase partida en 4–5 tarjetas** que cambian con cada corte. Ejemplo real: *«El arte de celebrar la vida,» / «De disfrutar el ahora» / «Y compartir momentos inolvidables» / «En esta temporada» / «Con Loco Ámbar, Tequila Reposado»*.
- Rótulos de ocasión (*THANKSGIVING*) o de nombre y cargo cuando hay un anfitrión.
- **Ningún texto se pide al modelo de video.** Las tarjetas, el end card y la leyenda van en el bloque de postproducción.

### 2.9 Lo que los videos reales hacen mal (no repetir)
- **Ninguno de los 8 lleva `+18 · Evita el exceso` ni `#EspírituDeOrigen`.** En la skill la leyenda es obligatoria en el montaje final.
- Cóctel con hielo en vaso corto (subasta) y barra sin copa tulipán (moda): **prohibido** por `brand-context.md`.
- Casi nunca mencionan El Arenal ni Hacienda La Providencia: el copy debe recuperarlo.

### 2.10 Pendiente de confirmar con el cliente
- *Celebra la travesía* muestra un **estuche rígido negro** con interior aterciopelado y una «L» en monograma. `[INFERIDO — confirmar con el cliente]`: puede ser el interior de la caja de anillos de madera de Ámbar. No usarlo como hecho de marca.

---

## 3. Música de los videos (prompt aparte, uno por video)

Los videos reales usan siempre música **instrumental**, con un remate en el end card. Dos arquetipos:

| | Arquetipo A — Organic Deep House / Lounge | Arquetipo B — Neoclásico cinemático |
| --- | --- | --- |
| **Cuándo** | Coctelería, cocina, galerías, subastas, moda, eventos sociales | Brindis, banquetes, fechas conmemorativas, tomas lentas de producto |
| **Tempo** | 118–122 BPM, 4/4 | 80–95 BPM, 3/4 o 4/4 |
| **Modo** | Menor o dórico suave (La m, Re m, Mi m) | Menor o dórico suave |
| **Instrumentos** | Bombo suave 4/4, rimshots, shakers, percusión de madera, sub-bass redondo, pads cálidos, piano eléctrico, mallets | Piano de cola con fieltro, cuerdas cálidas, chelo sostenido, campanas sutiles |
| **Excluir** | Voces, drops agresivos de EDM, distorsión, metales estridentes, >124 BPM | Batería, beats electrónicos, voces, coro, metales agresivos |

**Reglas del prompt musical:**
- Duración = duración total del video (`{{duracion_video}}`); la estructura se sincroniza con los tramos y **resuelve en el end card** (acorde final o *fade-out* en los últimos 2–3 s).
- Siempre instrumental y con espacio para voz en off (mezcla limpia, sin saturar 1.5–4.5 kHz).
- Se entrega en inglés con etiquetas (formato Suno / Udio / Stable Audio) y en español.
- **Derechos comerciales: `[no disponible]`.** Dependen del plan de la herramienta musical; nunca afirmar una licencia.
- Los prompts de video, en cambio, piden `ambient room tone and foley only, no music`, para que el audio de cada tramo no choque con la pista.

Plantilla A (inglés):
```text
[Genre: Organic Deep House, Melodic Lounge, Downtempo Electronic] [Tempo: 120 BPM, 4/4] [Key: A minor, soft dorian color] [Instruments: warm deep sub-bass, soft 4/4 kick, muted rimshots, subtle shakers, organic wood percussion, plush warm pads, delicate electric piano chords, gentle mallets] [Mood: sophisticated, upscale, modern elegance, smooth groove] [Structure: <duración> s, intro 0–4 s, groove builds with each segment, resolves on a final sustained chord in the last 3 s for the logo end card] [Production: clean studio master, wide stereo, headroom for voice-over] [Negative: vocals, singing, heavy distortion, harsh EDM drop, loud brass, aggressive synths, guitar solos]
```

Plantilla B (inglés):
```text
[Genre: Cinematic Neoclassical, Warm Acoustic Ambient, Modern Chamber] [Tempo: 88 BPM, 3/4] [Key: D minor] [Instruments: felted grand piano, warm string ensemble, sustained cello, soft violin swells, sparse bell chimes] [Mood: timeless elegance, intimate celebration, refined, subtle emotion] [Structure: <duración> s, gentle piano intro, strings enter at the second segment, swell at the toast, soft resolution and fade-out in the last 3 s for the logo end card] [Production: natural room acoustics, warm hall reverb, uncompressed dynamics] [Negative: drums, heavy percussion, electronic beats, synth leads, vocals, choir, aggressive brass]
```
