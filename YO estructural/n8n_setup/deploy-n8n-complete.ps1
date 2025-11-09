#!/usr/bin/env pwsh
<#
.SYNOPSIS
    GUÍA EJECUTIVA: Instalación completa de n8n en 3 pasos desde PowerShell
    
.DESCRIPTION
    Este script es el "punto de entrada" completo. Cópialo, pégalo y ejecuta.
    Todo lo demás se genera automáticamente.

.AUTHOR
    Sistema YO Estructural v3.0 - 2025-10-31

.EXAMPLE
    PS> .\deploy-n8n-complete.ps1

    O directamente en PowerShell:
    PS> & {iwr -useb "ruta_a_este_script" | iex}
#>

Write-Host @"

╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║     🧠 DESPLIEGUE COMPLETO: N8N + YO ESTRUCTURAL v3.0                        ║
║                                                                                ║
║              ¡INSTALACIÓN 100% DESDE POWERSHELL!                              ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝

" -ForegroundColor Magenta

# ============================================================================
# VERIFICAR PERMISOS ADMINISTRATIVOS
# ============================================================================

$isAdmin = ([System.Security.Principal.WindowsIdentity]::GetCurrent() | 
           ForEach-Object { [System.Security.Principal.WindowsPrincipal]$_ }).IsInRole(
           [System.Security.Principal.WindowsBuiltinRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "⚠ Este script requiere permisos de administrador" -ForegroundColor Yellow
    Write-Host "Por favor, abre PowerShell como Administrador y ejecuta de nuevo" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Presiona Enter para cerrar..." -ForegroundColor Gray
    Read-Host
    exit 1
}

Write-Host "✓ Permisos administrativos detectados" -ForegroundColor Green
Write-Host ""

# ============================================================================
# PASO 1: PREPARACIÓN
# ============================================================================

Write-Host "═" * 80 -ForegroundColor Cyan
Write-Host "PASO 1: PREPARACIÓN DEL SISTEMA" -ForegroundColor Cyan
Write-Host "═" * 80 -ForegroundColor Cyan
Write-Host ""

# Permitir ejecución de scripts
Write-Host "[1/3] Configurando política de ejecución de scripts..." -ForegroundColor Gray
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force | Out-Null
Write-Host "✓ Política actualizada" -ForegroundColor Green

# Obtener ruta del proyecto
$projectRoot = Split-Path -Parent $PSScriptRoot
$n8nSetupPath = Join-Path $projectRoot "n8n_setup"

Write-Host "[2/3] Localizando carpeta del proyecto..." -ForegroundColor Gray
Write-Host "  Proyecto: $projectRoot" -ForegroundColor Gray
Write-Host "  n8n setup: $n8nSetupPath" -ForegroundColor Gray

if (-not (Test-Path $n8nSetupPath)) {
    Write-Host "✗ Carpeta n8n_setup no encontrada" -ForegroundColor Red
    Write-Host "  Asegúrate de estar en el directorio correcto" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Directorio validado" -ForegroundColor Green

# Verificar Node.js
Write-Host "[3/3] Verificando dependencias..." -ForegroundColor Gray
$hasNode = $null -ne (Get-Command node -ErrorAction SilentlyContinue)

if ($hasNode) {
    $nodeVersion = node -v
    Write-Host "✓ Node.js $nodeVersion encontrado" -ForegroundColor Green
} else {
    Write-Host "⚠ Node.js no encontrado - se instalará automáticamente" -ForegroundColor Yellow
}

Write-Host ""

# ============================================================================
# PASO 2: EJECUTAR INSTALACIÓN
# ============================================================================

Write-Host "═" * 80 -ForegroundColor Cyan
Write-Host "PASO 2: EJECUCIÓN DEL INSTALADOR" -ForegroundColor Cyan
Write-Host "═" * 80 -ForegroundColor Cyan
Write-Host ""

Write-Host "Ejecutando script de instalación completa..." -ForegroundColor Gray
Write-Host ""

# Ejecutar script maestro
$installScript = Join-Path $n8nSetupPath "install-n8n-complete.ps1"

if (Test-Path $installScript) {
    & $installScript
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "✗ Error durante la instalación" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✗ Script de instalación no encontrado: $installScript" -ForegroundColor Red
    exit 1
}

Write-Host ""

# ============================================================================
# PASO 3: VALIDACIÓN
# ============================================================================

Write-Host "═" * 80 -ForegroundColor Cyan
Write-Host "PASO 3: VALIDACIÓN DE LA INSTALACIÓN" -ForegroundColor Cyan
Write-Host "═" * 80 -ForegroundColor Cyan
Write-Host ""

Write-Host "Ejecutando validación..." -ForegroundColor Gray
Write-Host ""

$validateScript = Join-Path $n8nSetupPath "validate-installation.ps1"

if (Test-Path $validateScript) {
    & $validateScript -QuickTest
} else {
    Write-Host "⚠ Script de validación no encontrado" -ForegroundColor Yellow
}

# ============================================================================
# RESUMEN FINAL
# ============================================================================

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║                    ✓ ¡INSTALACIÓN COMPLETADA!                                 ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════════════════════╝" -ForegroundColor Green

Write-Host @"

🎯 PRÓXIMAS ACCIONES:

1. INICIAR N8N
   ──────────────────────────────────────────────────────────
   PowerShell:
     n8n start --env-file `$env:USERPROFILE\.n8n\.env
   
   O con soporte para webhooks públicos:
     n8n start --tunnel


2. ACCEDER A LA INTERFAZ WEB
   ──────────────────────────────────────────────────────────
   Abre tu navegador y ve a:
     http://localhost:5678
   
   Usuario: admin
   Contraseña: (la que estableciste durante la instalación)


3. VERIFICAR LOS WORKFLOWS
   ──────────────────────────────────────────────────────────
   En la UI de n8n deberías ver 3 workflows:
     ✓ Workflow 1: Monitor Archivos Locales
     ✓ Workflow 2: Sync Neo4j
     ✓ Workflow 3: Text Processing & Embeddings
   
   Asegúrate de que todos estén ACTIVE (no pausados)


4. PROBAR CON UN ARCHIVO DE PRUEBA
   ──────────────────────────────────────────────────────────
   Crea un archivo .md o .txt en tu carpeta monitoreada:
     C:\yo_estructural\datos\
   
   El workflow 1 debería detectarlo y procesarlo automáticamente


5. INTEGRAR CON TU CÓDIGO PYTHON
   ──────────────────────────────────────────────────────────
   En tu motor_yo/sistema_yo_emergente.py:
   
     from integraciones.n8n_config import N8nIntegrator
     
     n8n = N8nIntegrator()
     resultado = n8n.enviar_datos_webhook({
         "contenido": "Tu texto",
         "id": "doc_001"
     })


📚 DOCUMENTACIÓN DISPONIBLE

  • README.md                      ← Inicio rápido
  • SETUP_GUIDE.md                 ← Guía completa con diagrams
  • Archivo .env                   ← Variables de configuración
  • Workflows JSON                 ← Definiciones de flujos


🔧 COMANDOS ÚTILES

  # Ver workflows
  n8n list:workflows
  
  # Exportar workflows (backup)
  n8n export:workflow --all --output backup.json
  
  # Ver ejecuciones recientes
  n8n list:executions
  
  # Testear conectividad
  Invoke-RestMethod http://localhost:5678/healthz
  
  # Ver logs en tiempo real
  tail -f `$env:USERPROFILE\.n8n\logs\*


💾 UBICACIONES IMPORTANTES

  Configuración:        `$env:USERPROFILE\.n8n\.env
  Base de datos:        `$env:USERPROFILE\.n8n\n8n.db
  Workflows:            `$env:USERPROFILE\.n8n\workflows\
  Logs:                 `$env:USERPROFILE\.n8n\logs\
  Credenciales:         `$env:USERPROFILE\.n8n\credentials.json (cifrado)


⚠ IMPORTANTE

  • NUNCA compartir el archivo .env con credenciales
  • Hacer backup periódico de `$env:USERPROFILE\.n8n\
  • Cambiar contraseñas en producción
  • Usar SSL/HTTPS si expones webhooks a Internet


🆘 SOPORTE

  Si algo falla:
  
  1. Revisar logs:
     tail -f `$env:USERPROFILE\.n8n\logs\*
  
  2. Ejecutar validación:
     .\n8n_setup\validate-installation.ps1
  
  3. Leer SETUP_GUIDE.md (sección Troubleshooting)


╔════════════════════════════════════════════════════════════════════════════════╗
║  ¡Sistema listo! Ejecuta 'n8n start' y abre http://localhost:5678             ║
╚════════════════════════════════════════════════════════════════════════════════╝

" -ForegroundColor Cyan

Write-Host ""
