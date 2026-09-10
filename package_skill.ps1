<#
.SYNOPSIS
    Script de empaquetado para agente-mercadotecnia-loco-tequila.
.DESCRIPTION
    Empaqueta todos los componentes operativos, directrices, plantillas, scripts y documentación
    de la skill en "agente-mercadotecnia-loco-tequila.zip".
    Excluye automáticamente archivos de imagen binarios dentro de "references/" y subcarpetas,
    manteniendo todos los archivos .md descriptivos creados. Excluye también artefactos de desarrollo
    (.git, outputs/, __pycache__, etc.).
#>

[CmdletBinding()]
param(
    [string]$OutputFile = "agente-mercadotecnia-loco-tequila.zip",
    [double]$MaxUncompressedMB = 30.0
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $ScriptDir) { $ScriptDir = Get-Location }

$ZipPath = Join-Path $ScriptDir $OutputFile
$TempDir = Join-Path ([System.IO.Path]::GetTempPath()) ("pkg_skill_" + [System.Guid]::NewGuid().ToString("N"))

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Empaquetando Skill: agente-mercadotecnia-loco-tequila  " -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Directorio origen:     $ScriptDir"
Write-Host "Archivo destino:       $ZipPath"
Write-Host "Límite desempaquetado: $MaxUncompressedMB MB"

# Extensiones de imagen binaria a excluir en references
$ImageExtensions = @(".jpg", ".jpeg", ".png", ".webp", ".bmp", ".gif", ".tiff")

try {
    if (Test-Path $TempDir) {
        Remove-Item -Recurse -Force $TempDir
    }
    New-Item -ItemType Directory -Path $TempDir | Out-Null

    # Archivos y carpetas a incluir
    $ItemsToInclude = @(
        "SKILL.md",
        "README.md",
        "AGENTS.md",
        "FLUJO_SKILL_CLIENTE.md",
        "to_do.md",
        ".gitignore",
        "package_skill.ps1",
        "package_skill.sh",
        "designs",
        "imagenes",
        "references",
        "showcase",
        "sub-skill"
    )

    foreach ($item in $ItemsToInclude) {
        $sourcePath = Join-Path $ScriptDir $item
        if (-not (Test-Path $sourcePath)) {
            Write-Warning "No se encontró el elemento requerido: $item"
            continue
        }

        $destPath = Join-Path $TempDir $item

        if ((Get-Item $sourcePath) -is [System.IO.DirectoryInfo]) {
            # Es un directorio: copiar recursivamente aplicando filtros
            New-Item -ItemType Directory -Path $destPath -Force | Out-Null
            
            Get-ChildItem -Path $sourcePath -Recurse | ForEach-Object {
                $subItem = $_
                $relPath = $subItem.FullName.Substring($sourcePath.Length)
                $targetSubPath = Join-Path $destPath $relPath

                # Exclusiones generales
                if ($subItem.FullName -match "\\(\.git|outputs|__pycache__|\.vscode)") {
                    return
                }

                # Si está dentro de references, excluir imágenes binarias
                if ($item -eq "references") {
                    $ext = $subItem.Extension.ToLower()
                    if ($ImageExtensions -contains $ext) {
                        return
                    }
                }

                if ($subItem.PSIsContainer) {
                    if (-not (Test-Path $targetSubPath)) {
                        New-Item -ItemType Directory -Path $targetSubPath -Force | Out-Null
                    }
                } else {
                    $parentDir = Split-Path -Parent $targetSubPath
                    if (-not (Test-Path $parentDir)) {
                        New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
                    }
                    Copy-Item -Path $subItem.FullName -Destination $targetSubPath -Force
                }
            }
        } else {
            # Es un archivo suelto
            Copy-Item -Path $sourcePath -Destination $destPath -Force
        }
    }

    # Verificar tamaño total desempaquetado antes de comprimir
    Write-Host "Verificando peso total desempaquetado..." -ForegroundColor Cyan
    $UncompressedBytes = (Get-ChildItem -Path $TempDir -Recurse -File | Measure-Object -Property Length -Sum).Sum
    $UncompressedMB = [Math]::Round($UncompressedBytes / 1MB, 2)

    Write-Host "  Tamaño desempaquetado: $UncompressedMB MB (Límite máximo permitido: $MaxUncompressedMB MB)"

    if ($UncompressedMB -gt $MaxUncompressedMB) {
        Write-Error "ERROR: El tamaño de los archivos desempaquetados ($UncompressedMB MB) supera el límite de $MaxUncompressedMB MB permitido por los gestores de skills."
        exit 1
    } else {
        Write-Host "  [OK] El tamaño desempaquetado está dentro del límite permitido (< $MaxUncompressedMB MB)." -ForegroundColor Green
    }

    # Eliminar zip previo si existe
    if (Test-Path $ZipPath) {
        Remove-Item -Force $ZipPath
    }

    Write-Host "Comprimiendo componentes en $OutputFile con formato universal (forward slashes '/' y UTF-8)..." -ForegroundColor Yellow
    Add-Type -AssemblyName System.IO.Compression
    Add-Type -AssemblyName System.IO.Compression.FileSystem

    $zipStream = [System.IO.File]::Create($ZipPath)
    $archive = New-Object System.IO.Compression.ZipArchive($zipStream, [System.IO.Compression.ZipArchiveMode]::Create, $false, [System.Text.Encoding]::UTF8)

    Get-ChildItem -Path $TempDir -Recurse -File | ForEach-Object {
        $filePath = $_.FullName
        $relPath = $filePath.Substring($TempDir.Length).TrimStart('\', '/')
        # Especificación estándar ZIP: todas las rutas DEBEN usar forward slash '/'
        $entryName = $relPath -replace '\\', '/'
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($archive, $filePath, $entryName, [System.IO.Compression.CompressionLevel]::Optimal) | Out-Null
    }

    $archive.Dispose()
    $zipStream.Dispose()

    $ZipSizeMB = [Math]::Round((Get-Item $ZipPath).Length / 1MB, 2)
    Write-Host "--------------------------------------------------------" -ForegroundColor Green
    Write-Host "  Empaquetado exitoso!" -ForegroundColor Green
    Write-Host "  Archivo:               $ZipPath" -ForegroundColor Green
    Write-Host "  Tamaño comprimido:     $ZipSizeMB MB" -ForegroundColor Green
    Write-Host "  Tamaño desempaquetado: $UncompressedMB MB (Límite: $MaxUncompressedMB MB)" -ForegroundColor Green
    Write-Host "--------------------------------------------------------" -ForegroundColor Green
}
finally {
    if (Test-Path $TempDir) {
        Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue
    }
}
