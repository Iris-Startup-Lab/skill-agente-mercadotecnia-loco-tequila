# Sub-skill: Lectura de Metadatos en OneDrive / SharePoint

> **Propósito:** Audita los metadatos (nombres y fechas) de los archivos de campañas anteriores en una carpeta de OneDrive/SharePoint compartida mediante link. Permite al agente conocer qué campañas y temas se han trabajado previamente para no repetir conceptos.
>
> ⚠️ **Alcance Técnico:** El conector de Microsoft 365 MCP **solo lee metadatos (nombres, fechas, tamaños y estructura de carpetas)**. No puede extraer mapas de bits de imágenes binarias (`.jpg`, `.png`, `.webp`) debido a limitaciones de Microsoft Graph API.

---

## Requisito previo

Requiere el plugin **Microsoft 365** activo (MCP) con la herramienta `sharepoint_folder_search` y `read_resource`.

---

## Protocolo de Ejecución Paso a Paso

### Paso 1: Preguntar confirmación de lectura de metadatos

Al recibir el link de OneDrive/SharePoint (o al solicitarlo):
1. **Pregunta activamente al usuario:**
   > *"He recibido el enlace de OneDrive/SharePoint. ¿Deseas que lea los documentos y archivos de la carpeta para conocer los **nombres y temáticas de campañas pasadas**? (Límite de hasta 10 archivos a partir de la fecha más reciente)."*
2. **Ofrecer adjuntar imágenes de ejemplo (Opcional para el usuario):**
   > *"Nota: El conector de Microsoft 365 solo lee metadatos de texto y nombres de archivo. Si deseas que analice la **composición visual, iluminación o diseño exacto** para evitar repetir estilos visuales, puedes adjuntar libremente 1 a 3 imágenes de ejemplo directamente aquí en el chat 📎."*

### Paso 2: Identificar y buscar la carpeta

1. Extrae el nombre de la carpeta del URL (la porción tras el último `/` antes de los parámetros `?`). Decodifica caracteres especiales (`%20` = espacio).
2. Usa `Microsoft 365:sharepoint_folder_search` con ese nombre para localizar la carpeta.

### Paso 3: Listar contenido y extraer metadatos

1. Usa `Microsoft 365:read_resource` con el `uri` de la carpeta encontrada para listar los elementos.
2. Filtra los archivos de imagen/publicidad (`.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.pdf`).
3. Ordénalos por fecha de modificación (más reciente primero) y toma hasta un máximo de 10 archivos.

### Paso 4: Manejo de la limitación técnica de Graph API

> ⚠️ **Regla de oro ante errores de binarios:**
> Si al intentar inspeccionar un archivo individual `.jpg`/`.png` con `read_resource`, Graph API arroja el error `Internal Graph API error (Format conversion failed)`:
> - **NUNCA detener el flujo ni pedir reintentos al usuario.**
> - Utiliza directamente la **lista de nombres de archivo y fechas** obtenida en el Paso 3 (ej. `facebook_loco_tequila_1.jpg`, `instagram_loco_blanco_verano.png`).
> - Notifica brevemente: *"Se identificaron las siguientes piezas previas: [Lista de nombres]. Usaré estos temas como referencia para no duplicar conceptos."*
> - Avanza inmediatamente a la confirmación de fechas festivas y producto.

---

## 📚 Referencias Técnicas sobre el Conector Microsoft 365 y Graph API

1. **Microsoft Graph API — Formatos Soportados:**
   - La API de Microsoft Graph (`/drive/items/{id}/content`) está diseñada para la transferencia de streams de datos crudos. Cuando un conector MCP de IA invoca herramientas de lectura de texto (`read_resource`), el conector intenta convertir la respuesta en texto codificado en UTF-8. En archivos de imagen binarios (sin capa de texto OCR), Graph API devuelve un error de conversión de formato (*Format conversion failed*).
2. **Documentación Oficial de Claude & Microsoft 365 Connector:**
   - El conector oficial de Microsoft 365 utiliza permisos delegados (`Files.Read`, `Sites.Read.All`) optimizados para búsqueda de texto en correos de Outlook, documentos de Word, notas de OneNote y metadatos de SharePoint. No incluye un pipeline de procesamiento multimodal de imágenes descargadas.
3. **Visión Multimodal Nativa de Claude:**
   - La capacidad de visión por computadora de Claude opera directamente a través del cargador de adjuntos de la interfaz de usuario (`image/jpeg`, `image/png`, `image/webp`), garantizando análisis visual fotorrealista y estilístico completo.

