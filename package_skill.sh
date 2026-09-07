#!/usr/bin/env bash
# ==============================================================================
# Script de empaquetado para agente-mercadotecnia-loco-tequila
# ==============================================================================
# Empaqueta todos los componentes operativos, directrices, plantillas y scripts
# en "agente-mercadotecnia-loco-tequila.zip".
# Excluye imágenes binarias (*.jpg, *.jpeg, *.png, etc.) dentro de references/,
# pero conserva todos los archivos .md descriptivos.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_FILE="${1:-agente-mercadotecnia-loco-tequila.zip}"
ZIP_PATH="${SCRIPT_DIR}/${OUTPUT_FILE}"
TEMP_DIR="$(mktemp -d 2>/dev/null || mktemp -d -t 'pkg_skill')"

echo "========================================================"
echo "  Empaquetando Skill: agente-mercadotecnia-loco-tequila  "
echo "========================================================"
echo "Directorio origen: ${SCRIPT_DIR}"
echo "Archivo destino:   ${ZIP_PATH}"

cleanup() {
    rm -rf "${TEMP_DIR}"
}
trap cleanup EXIT

# Lista de elementos raíz a incluir
ITEMS=(
    "SKILL.md"
    "README.md"
    "AGENTS.md"
    "to_do.md"
    ".gitignore"
    "package_skill.ps1"
    "package_skill.sh"
    "designs"
    "imagenes"
    "references"
    "showcase"
    "sub-skill"
)

# Copiar selectivamente los elementos
for item in "${ITEMS[@]}"; do
    SRC="${SCRIPT_DIR}/${item}"
    DEST="${TEMP_DIR}/${item}"

    if [ ! -e "${SRC}" ]; then
        echo "Aviso: Elemento no encontrado: ${item}"
        continue
    fi

    if [ -d "${SRC}" ]; then
        mkdir -p "${DEST}"
        if command -v rsync >/dev/null 2>&1; then
            if [ "${item}" = "references" ]; then
                rsync -av \
                    --exclude="*.git*" \
                    --exclude="outputs" \
                    --exclude="__pycache__" \
                    --exclude="*.pyc" \
                    --exclude="*.jpg" \
                    --exclude="*.jpeg" \
                    --exclude="*.png" \
                    --exclude="*.webp" \
                    --exclude="*.bmp" \
                    --exclude="*.gif" \
                    --exclude="*.JPG" \
                    --exclude="*.PNG" \
                    "${SRC}/" "${DEST}/" >/dev/null
            else
                rsync -av \
                    --exclude="*.git*" \
                    --exclude="outputs" \
                    --exclude="__pycache__" \
                    --exclude="*.pyc" \
                    "${SRC}/" "${DEST}/" >/dev/null
            fi
        else
            cp -R "${SRC}/." "${DEST}/"
            # Eliminar manualmente imágenes si está en references
            if [ "${item}" = "references" ]; then
                find "${DEST}" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" -o -iname "*.bmp" -o -iname "*.gif" \) -delete
            fi
            # Eliminar artefactos de desarrollo
            find "${DEST}" -type d \( -name ".git" -o -name "outputs" -o -name "__pycache__" \) -exec rm -rf {} + 2>/dev/null || true
            find "${DEST}" -type f -name "*.pyc" -delete 2>/dev/null || true
        fi
    else
        cp "${SRC}" "${DEST}"
    fi
done

# Eliminar zip previo si existe
if [ -f "${ZIP_PATH}" ]; then
    rm -f "${ZIP_PATH}"
fi

echo "Comprimiendo componentes en ${OUTPUT_FILE}..."
if command -v zip >/dev/null 2>&1; then
    (cd "${TEMP_DIR}" && zip -r -q "${ZIP_PATH}" .)
else
    # Fallback con python si zip no está instalado
    python -c "
import shutil
import sys
shutil.make_archive('${ZIP_PATH%.zip}', 'zip', '${TEMP_DIR}')
"
fi

if [ -f "${ZIP_PATH}" ]; then
    SIZE_KB=$(du -k "${ZIP_PATH}" | cut -f1)
    echo "--------------------------------------------------------"
    echo "  Empaquetado exitoso!"
    echo "  Archivo: ${ZIP_PATH}"
    echo "  Tamaño:  ~${SIZE_KB} KB"
    echo "--------------------------------------------------------"
else
    echo "Error: No se pudo generar el archivo ZIP."
    exit 1
fi
