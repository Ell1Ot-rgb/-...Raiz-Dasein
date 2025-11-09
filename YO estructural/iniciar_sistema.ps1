# ===================================================================
# SCRIPT DE INICIO AUTOMÁTICO - YO ESTRUCTURAL v3.0
# Infraestructura: Dual Core (n8n + Python) + i5 Core (Neo4j)
# ===================================================================

param(
    [switch]$SkipBrowser,
    [switch]$Verbose
)

$ErrorActionPreference = "Stop"

# Colores
function Write-Success { Write-Host $args -ForegroundColor Green }
function Write-Info { Write-Host $args -ForegroundColor Cyan }
function Write-Warning { Write-Host $args -ForegroundColor Yellow }
function Write-Error { Write-Host $args -ForegroundColor Red }

Write-Info "╔════════════════════════════════════════════════════════════╗"
Write-Info "║     🚀 INICIANDO YO ESTRUCTURAL v3.0                      ║"
Write-Info "║     Fenomenología Computacional + n8n + Neo4j             ║"
Write-Info "╚════════════════════════════════════════════════════════════╝"
Write-Host ""

# ===================================================================
# 1. VERIFICAR NEO4J EN i5 CORE
# ===================================================================

Write-Info "📊 PASO 1/5: Verificando Neo4j en i5 Core..."

# Leer configuración desde .env
$envPath = "$env:USERPROFILE\.n8n\.env"
if (Test-Path $envPath) {
    Get-Content $envPath | ForEach-Object {
        if ($_ -match '^NEO4J_HOST=(.+)$') {
            $neo4jHost = $matches[1]
        }
        if ($_ -match '^NEO4J_PORT=(.+)$') {
            $neo4jPort = $matches[1]
        }
    }
} else {
    Write-Warning "⚠ Archivo .env no encontrado. Usando valores por defecto."
    $neo4jHost = "192.168.1.37"
    $neo4jPort = "7687"
}

Write-Host "   Host: $neo4jHost"
Write-Host "   Puerto: $neo4jPort"

$neo4jTest = Test-NetConnection -ComputerName $neo4jHost -Port $neo4jPort -InformationLevel Quiet -WarningAction SilentlyContinue

if ($neo4jTest) {
    Write-Success "   ✓ Neo4j accesible en $neo4jHost:$neo4jPort"
} else {
    Write-Error "   ✗ Neo4j NO accesible"
    Write-Warning "   → Verificar que Neo4j esté corriendo en i5 Core"
    Write-Warning "   → Ejecutar en i5: docker ps (si usa Docker)"
    Write-Warning "   → O: sudo systemctl status neo4j (si es nativo)"
    
    $continue = Read-Host "`n¿Continuar de todos modos? (s/N)"
    if ($continue -ne "s" -and $continue -ne "S") {
        Write-Error "Instalación abortada por el usuario."
        exit 1
    }
}

Write-Host ""

# ===================================================================
# 2. VERIFICAR INSTALACIÓN DE N8N
# ===================================================================

Write-Info "🤖 PASO 2/5: Verificando instalación de n8n..."

$n8nInstalled = Get-Command n8n -ErrorAction SilentlyContinue

if ($n8nInstalled) {
    $n8nVersion = (n8n --version 2>&1) -replace '^n8n@', ''
    Write-Success "   ✓ n8n instalado (versión: $n8nVersion)"
} else {
    Write-Error "   ✗ n8n NO está instalado"
    Write-Warning "   → Ejecutar primero: .\n8n_setup\deploy-n8n-complete.ps1"
    exit 1
}

Write-Host ""

# ===================================================================
# 3. VERIFICAR VARIABLES DE ENTORNO
# ===================================================================

Write-Info "⚙️ PASO 3/5: Verificando configuración (.env)..."

if (Test-Path $envPath) {
    Write-Success "   ✓ Archivo .env encontrado"
    
    $envContent = Get-Content $envPath
    $requiredVars = @(
        'N8N_PORT',
        'N8N_ENCRYPTION_KEY',
        'NEO4J_HOST',
        'NEO4J_PASSWORD',
        'LOCAL_DATA_PATH',
        'YAML_OUTPUT_PATH'
    )
    
    $missingVars = @()
    foreach ($var in $requiredVars) {
        $found = $envContent | Where-Object { $_ -match "^$var=" }
        if (-not $found) {
            $missingVars += $var
        }
    }
    
    if ($missingVars.Count -gt 0) {
        Write-Warning "   ⚠ Variables faltantes:"
        $missingVars | ForEach-Object { Write-Warning "      - $_" }
    } else {
        Write-Success "   ✓ Todas las variables requeridas presentes"
    }
} else {
    Write-Error "   ✗ Archivo .env no existe"
    Write-Warning "   → Ejecutar: .\n8n_setup\deploy-n8n-complete.ps1"
    exit 1
}

Write-Host ""

# ===================================================================
# 4. VERIFICAR DIRECTORIOS
# ===================================================================

Write-Info "📂 PASO 4/5: Verificando directorios de trabajo..."

# Extraer rutas del .env
$localDataPath = ($envContent | Where-Object { $_ -match '^LOCAL_DATA_PATH=(.+)$' }) -replace '^LOCAL_DATA_PATH=', ''
$yamlOutputPath = ($envContent | Where-Object { $_ -match '^YAML_OUTPUT_PATH=(.+)$' }) -replace '^YAML_OUTPUT_PATH=', ''

if ($localDataPath) {
    if (Test-Path $localDataPath) {
        Write-Success "   ✓ LOCAL_DATA_PATH existe: $localDataPath"
    } else {
        Write-Warning "   ⚠ LOCAL_DATA_PATH no existe. Creando..."
        New-Item -ItemType Directory -Path $localDataPath -Force | Out-Null
        Write-Success "   ✓ Directorio creado: $localDataPath"
    }
}

if ($yamlOutputPath) {
    if (Test-Path $yamlOutputPath) {
        Write-Success "   ✓ YAML_OUTPUT_PATH existe: $yamlOutputPath"
    } else {
        Write-Warning "   ⚠ YAML_OUTPUT_PATH no existe. Creando..."
        New-Item -ItemType Directory -Path $yamlOutputPath -Force | Out-Null
        Write-Success "   ✓ Directorio creado: $yamlOutputPath"
    }
}

Write-Host ""

# ===================================================================
# 5. INICIAR N8N
# ===================================================================

Write-Info "🚀 PASO 5/5: Iniciando n8n..."

# Verificar si ya está corriendo
$n8nProcess = Get-Process -Name "node" -ErrorAction SilentlyContinue | Where-Object { $_.Path -match "n8n" }

if ($n8nProcess) {
    Write-Warning "   ⚠ n8n ya está corriendo (PID: $($n8nProcess.Id))"
    $restart = Read-Host "   ¿Reiniciar? (s/N)"
    
    if ($restart -eq "s" -or $restart -eq "S") {
        Write-Host "   Deteniendo n8n..."
        Stop-Process -Id $n8nProcess.Id -Force
        Start-Sleep -Seconds 3
    } else {
        Write-Info "   Usando instancia existente."
        $skipStart = $true
    }
}

if (-not $skipStart) {
    Write-Host "   Iniciando n8n en nueva ventana de PowerShell..."
    
    $n8nCommand = "cd '$PSScriptRoot'; Write-Host '🤖 n8n corriendo...' -ForegroundColor Green; n8n start --env-file $envPath"
    
    Start-Process powershell -ArgumentList "-NoExit", "-Command", $n8nCommand
    
    Write-Host "   Esperando a que n8n inicie (15 segundos)..."
    Start-Sleep -Seconds 15
    
    # Verificar que está corriendo
    $n8nPort = ($envContent | Where-Object { $_ -match '^N8N_PORT=(.+)$' }) -replace '^N8N_PORT=', ''
    if (-not $n8nPort) { $n8nPort = "5678" }
    
    $n8nTest = Test-NetConnection -ComputerName localhost -Port $n8nPort -InformationLevel Quiet -WarningAction SilentlyContinue
    
    if ($n8nTest) {
        Write-Success "   ✓ n8n iniciado correctamente en puerto $n8nPort"
    } else {
        Write-Error "   ✗ n8n NO respondió en puerto $n8nPort"
        Write-Warning "   → Revisar logs en la ventana de PowerShell abierta"
    }
}

Write-Host ""

# ===================================================================
# RESUMEN Y ACCESOS
# ===================================================================

Write-Info "╔════════════════════════════════════════════════════════════╗"
Write-Info "║               ✅ SISTEMA INICIADO CORRECTAMENTE            ║"
Write-Info "╚════════════════════════════════════════════════════════════╝"
Write-Host ""

Write-Success "🌐 ACCESOS:"
Write-Host "   • n8n UI:      http://localhost:$n8nPort" -ForegroundColor White
Write-Host "   • Neo4j Browser: http://$($neo4jHost):7474" -ForegroundColor White
Write-Host ""

Write-Success "📂 RUTAS MONITOREADAS:"
Write-Host "   • Entrada:     $localDataPath" -ForegroundColor White
Write-Host "   • YAML Output: $yamlOutputPath" -ForegroundColor White
Write-Host ""

Write-Success "📊 WORKFLOWS ACTIVOS:"
Write-Host "   1. Monitor Archivos (LOCAL_DATA_PATH)" -ForegroundColor White
Write-Host "   2. Sync Neo4j (Webhook /sync-neo4j)" -ForegroundColor White
Write-Host "   3. Text Processing (Webhook /process-text)" -ForegroundColor White
Write-Host "   4. Google Drive Multimodal (Polling cada 1 min)" -ForegroundColor White
Write-Host ""

Write-Success "🔧 COMANDOS ÚTILES:"
Write-Host "   • Ver workflows:   n8n list:workflows" -ForegroundColor Yellow
Write-Host "   • Activar workflow: n8n activate:workflow --name='nombre'" -ForegroundColor Yellow
Write-Host "   • Ver logs:        Get-Content `$env:USERPROFILE\.n8n\logs\* -Wait" -ForegroundColor Yellow
Write-Host "   • Detener n8n:     Stop-Process -Name 'node' -Force" -ForegroundColor Yellow
Write-Host ""

# Abrir browser (opcional)
if (-not $SkipBrowser) {
    Write-Info "🌐 Abriendo interfaz web en 3 segundos..."
    Start-Sleep -Seconds 3
    Start-Process "http://localhost:$n8nPort"
}

Write-Info "═══════════════════════════════════════════════════════════════"
Write-Success "✨ YO Estructural v3.0 está listo para procesar fenomenología"
Write-Info "═══════════════════════════════════════════════════════════════"
Write-Host ""

if ($Verbose) {
    Write-Host "Presiona cualquier tecla para salir..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
