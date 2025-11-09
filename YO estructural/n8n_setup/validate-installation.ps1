#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Script de validación post-instalación para n8n + YO Estructural
    
.DESCRIPTION
    Verifica que toda la instalación se completó correctamente,
    valida conectividad, workflows y credenciales.
#>

param(
    [switch]$QuickTest,
    [string]$N8nPort = "5678"
)

$ErrorActionPreference = "SilentlyContinue"
$ProgressPreference = "SilentlyContinue"

$Colors = @{
    Success = "Green"
    Error   = "Red"
    Warning = "Yellow"
    Info    = "Cyan"
    Header  = "Magenta"
}

function Write-Log { param([string]$Msg, [string]$Type = "Info")
    Write-Host "[$Type] $Msg" -ForegroundColor $Colors[$Type]
}

function Write-Header { param([string]$Title)
    Write-Host ""
    Write-Host "=" * 80 -ForegroundColor $Colors.Header
    Write-Host $Title -ForegroundColor $Colors.Header
    Write-Host "=" * 80 -ForegroundColor $Colors.Header
}

Write-Header "✓ VALIDACIÓN POST-INSTALACIÓN N8N + YO ESTRUCTURAL"

# ============================================================================
# 1. VALIDAR NODE.JS Y NPM
# ============================================================================

Write-Header "1. VALIDACIÓN DE NODE.JS Y NPM"

try {
    $nodeVersion = node -v
    Write-Log "Node.js: $nodeVersion" -Type "Success"
} catch {
    Write-Log "✗ Node.js no encontrado" -Type "Error"
    exit 1
}

try {
    $npmVersion = npm -v
    Write-Log "npm: $npmVersion" -Type "Success"
} catch {
    Write-Log "✗ npm no encontrado" -Type "Error"
    exit 1
}

# ============================================================================
# 2. VALIDAR N8N
# ============================================================================

Write-Header "2. VALIDACIÓN DE N8N"

try {
    $n8nVersion = n8n --version
    Write-Log "n8n: $n8nVersion" -Type "Success"
} catch {
    Write-Log "✗ n8n no instalado" -Type "Error"
    Write-Log "Ejecuta: npm install -g n8n" -Type "Warning"
    exit 1
}

# ============================================================================
# 3. VALIDAR ARCHIVO .ENV
# ============================================================================

Write-Header "3. VALIDACIÓN DE ARCHIVO .ENV"

$envFile = Join-Path $env:USERPROFILE ".n8n\.env"

if (Test-Path $envFile) {
    Write-Log ".env encontrado: $envFile" -Type "Success"
    
    # Verificar variables clave
    $content = Get-Content $envFile
    $vars = @(
        "N8N_PORT",
        "N8N_ENCRYPTION_KEY",
        "NEO4J_HOST",
        "NEO4J_PORT",
        "NEO4J_USER"
    )
    
    foreach ($var in $vars) {
        if ($content | Select-String "^$var=" -Quiet) {
            Write-Log "  ✓ $var definido" -Type "Info"
        } else {
            Write-Log "  ✗ $var no definido" -Type "Warning"
        }
    }
} else {
    Write-Log "✗ Archivo .env no encontrado" -Type "Error"
    Write-Log "Regenera con: .\n8n_setup\install-n8n-complete.ps1 -GenerateEnvOnly" -Type "Warning"
}

# ============================================================================
# 4. VALIDAR DIRECTORIOS
# ============================================================================

Write-Header "4. VALIDACIÓN DE DIRECTORIOS"

$dirs = @(
    "$env:USERPROFILE\.n8n",
    "$env:USERPROFILE\.n8n\workflows",
    "$env:USERPROFILE\.n8n\credentials",
    "$env:USERPROFILE\.n8n\logs"
)

foreach ($dir in $dirs) {
    if (Test-Path $dir) {
        Write-Log "  ✓ $dir" -Type "Success"
    } else {
        Write-Log "  ✗ $dir no existe" -Type "Warning"
    }
}

# ============================================================================
# 5. VALIDAR BASE DE DATOS
# ============================================================================

Write-Header "5. VALIDACIÓN DE BASE DE DATOS"

$dbFile = Join-Path $env:USERPROFILE ".n8n\n8n.db"

if (Test-Path $dbFile) {
    $dbSize = (Get-Item $dbFile).Length / 1MB
    Write-Log "Base de datos SQLite: $([Math]::Round($dbSize, 2)) MB" -Type "Success"
} else {
    Write-Log "Base de datos no encontrada (se creará al iniciar n8n)" -Type "Info"
}

# ============================================================================
# 6. VALIDAR CONECTIVIDAD (SI N8N ESTÁ CORRIENDO)
# ============================================================================

Write-Header "6. VALIDACIÓN DE CONECTIVIDAD"

$n8nRunning = $false
try {
    $response = Invoke-RestMethod -Uri "http://localhost:$N8nPort/healthz" -ErrorAction SilentlyContinue -TimeoutSec 3
    if ($response) {
        Write-Log "n8n responde en http://localhost:$N8nPort" -Type "Success"
        $n8nRunning = $true
    }
} catch {
    Write-Log "n8n no está corriendo en puerto $N8nPort" -Type "Warning"
    Write-Log "Inicia con: n8n start --env-file `$env:USERPROFILE\.n8n\.env" -Type "Info"
}

# Si n8n está corriendo, hacer más pruebas
if ($n8nRunning) {
    
    # Intentar obtener workflows
    try {
        $envContent = Get-Content $envFile
        $apiKey = ($envContent | Select-String "N8N_API_KEY=" | ForEach-Object { $_.Line.Split("=")[1] }).Trim()
        
        if ($apiKey) {
            $headers = @{ "X-N8N-API-KEY" = $apiKey }
            $workflows = Invoke-RestMethod -Uri "http://localhost:$N8nPort/rest/workflows" `
                -Headers $headers -ErrorAction SilentlyContinue -TimeoutSec 5
            
            Write-Log "Workflows activos: $($workflows.data.Count)" -Type "Success"
            
            foreach ($wf in $workflows.data | Select-Object -First 3) {
                $status = if ($wf.active) { "ACTIVE" } else { "PAUSED" }
                Write-Log "  • $($wf.name) [$status]" -Type "Info"
            }
        }
    } catch {
        Write-Log "No se pudieron leer workflows" -Type "Warning"
    }
    
    # Validar Neo4j desde n8n
    try {
        $neo4jHost = ($envContent | Select-String "NEO4J_HOST=" | ForEach-Object { $_.Line.Split("=")[1] }).Trim()
        $neo4jPort = ($envContent | Select-String "NEO4J_PORT=" | ForEach-Object { $_.Line.Split("=")[1] }).Trim()
        
        if ($neo4jHost -and $neo4jPort) {
            $tcpTest = Test-NetConnection -ComputerName $neo4jHost -Port $neo4jPort -WarningAction SilentlyContinue
            
            if ($tcpTest.TcpTestSucceeded) {
                Write-Log "Neo4j alcanzable en $neo4jHost`:$neo4jPort" -Type "Success"
            } else {
                Write-Log "No se alcanza Neo4j en $neo4jHost`:$neo4jPort" -Type "Warning"
            }
        }
    } catch {
        Write-Log "Error validando Neo4j" -Type "Warning"
    }
}

# ============================================================================
# 7. TEST RÁPIDO (OPCIONAL)
# ============================================================================

if ($QuickTest -and $n8nRunning) {
    Write-Header "7. TEST RÁPIDO DE WEBHOOK"
    
    try {
        $testBody = @{
            contenido = "Test desde PowerShell"
            id = "test_$(Get-Date -Format yyyyMMddHHmmss)"
            timestamp = Get-Date -Format o
        } | ConvertTo-Json
        
        $response = Invoke-RestMethod -Uri "http://localhost:$N8nPort/webhook/process-text" `
            -Method Post -Body $testBody -ContentType "application/json" `
            -ErrorAction SilentlyContinue -TimeoutSec 10
        
        Write-Log "✓ Webhook respondió correctamente" -Type "Success"
        Write-Log "  Respuesta: $($response | ConvertTo-Json -Depth 2)" -Type "Info"
    } catch {
        Write-Log "✗ Error en webhook: $_" -Type "Warning"
    }
}

# ============================================================================
# 8. RESUMEN
# ============================================================================

Write-Header "8. RESUMEN DE VALIDACIÓN"

Write-Host @"

✓ PASOS COMPLETADOS:
  1. Verificación de Node.js y npm
  2. Verificación de n8n
  3. Validación de archivo .env
  4. Validación de directorios
  5. Validación de base de datos

$(if ($n8nRunning) { "✓ n8n está CORRIENDO y responde" } else { "⚠ n8n no está en ejecución (inicia manualmente)" })

PRÓXIMOS PASOS:
  1. Iniciar n8n:
     n8n start --env-file `$env:USERPROFILE\.n8n\.env
  
  2. Abrir interfaz web:
     http://localhost:5678
  
  3. Verificar workflows en la UI
  
  4. Monitorear archivos en:
     $($([System.Environment]::GetEnvironmentVariable('LOCAL_DATA_PATH', 'User')) ?? 'C:\yo_estructural\datos')
  
  5. Consultar logs:
     tail -f `$env:USERPROFILE\.n8n\logs\*

DOCUMENTACIÓN:
  • Lee: .\n8n_setup\README.md
  • Guía completa: .\n8n_setup\SETUP_GUIDE.md

" -ForegroundColor Cyan

Write-Host ""
Write-Host "✓ Validación completada $(if ($n8nRunning) { "- Sistema LISTO" } else { "- Iniciando n8n..." })" -ForegroundColor Green
Write-Host ""

# Ofrecer iniciar n8n si no está corriendo
if (-not $n8nRunning) {
    $response = Read-Host "¿Desea iniciar n8n ahora? (s/n)"
    if ($response -eq 's') {
        Write-Log "Iniciando n8n..." -Type "Info"
        & n8n start --env-file $env:USERPROFILE\.n8n\.env
    }
}
