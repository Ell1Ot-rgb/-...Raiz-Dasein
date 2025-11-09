#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Script maestro para instalar y configurar n8n completamente desde PowerShell
    sin interfaz gráfica. Gestiona Node, n8n, credenciales, workflows y validación.

.DESCRIPTION
    Este script automatiza:
    1. Descarga e instalación de Node.js 18 LTS
    2. Instalación global de n8n
    3. Generación de archivo .env con credenciales seguras
    4. Importación de workflows optimizados
    5. Importación de credenciales (Neo4j, Google Drive, API keys)
    6. Validación de conectividad
    7. Arranque automático y creación de servicio Windows

.AUTHOR
    Sistema YO Estructural v3.0

.VERSION
    1.0 - 2025-10-31
#>

param(
    [switch]$SkipNodeInstall,
    [switch]$GenerateEnvOnly,
    [switch]$ImportWorkflowsOnly,
    [switch]$StartService,
    [switch]$CreateWindowsService,
    [string]$N8nHome = "$env:USERPROFILE\.n8n",
    [string]$N8nPort = "5678",
    [string]$WorkflowsDir = "$(Split-Path -Parent $PSScriptRoot)\n8n_setup\workflows",
    [string]$CredentialsDir = "$(Split-Path -Parent $PSScriptRoot)\n8n_setup\credentials"
)

# ============================================================================
# CONFIGURACIÓN INICIAL
# ============================================================================

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

# Colores para output
$Colors = @{
    Info    = "Cyan"
    Success = "Green"
    Warning = "Yellow"
    Error   = "Red"
    Header  = "Magenta"
}

function Write-Log {
    param([string]$Message, [string]$Type = "Info")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Type] $Message" -ForegroundColor $Colors[$Type]
}

function Write-Header {
    param([string]$Title)
    Write-Host ""
    Write-Host "=" * 80 -ForegroundColor $Colors.Header
    Write-Host $Title -ForegroundColor $Colors.Header
    Write-Host "=" * 80 -ForegroundColor $Colors.Header
    Write-Host ""
}

# ============================================================================
# 1. VERIFICAR Y INSTALAR NODE.JS
# ============================================================================

function Test-NodeInstallation {
    Write-Log "Verificando instalación de Node.js..."
    try {
        $nodeVersion = node -v
        Write-Log "✓ Node.js encontrado: $nodeVersion" -Type "Success"
        return $true
    }
    catch {
        Write-Log "✗ Node.js no encontrado" -Type "Warning"
        return $false
    }
}

function Install-NodeJS {
    Write-Header "INSTALACIÓN DE NODE.JS 18 LTS"
    
    if (Test-NodeInstallation) {
        return
    }
    
    Write-Log "Node.js no está instalado. Iniciando descarga..." -Type "Warning"
    
    $nodeUrl = "https://nodejs.org/dist/v18.19.0/node-v18.19.0-x64.msi"
    $msiPath = "$env:TEMP\node-v18.19.0-x64.msi"
    
    Write-Log "Descargando Node.js desde $nodeUrl..."
    try {
        Invoke-WebRequest -Uri $nodeUrl -OutFile $msiPath -UseBasicParsing
        Write-Log "✓ Descarga completada" -Type "Success"
    }
    catch {
        Write-Log "✗ Error descargando Node.js: $_" -Type "Error"
        throw
    }
    
    Write-Log "Instalando Node.js (requiere elevación de permisos)..."
    try {
        Start-Process -FilePath "msiexec.exe" -ArgumentList "/i `"$msiPath`" /quiet" -Wait
        Write-Log "✓ Node.js instalado correctamente" -Type "Success"
    }
    catch {
        Write-Log "✗ Error instalando Node.js: $_" -Type "Error"
        throw
    }
    
    # Recargar PATH
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
    
    if (Test-NodeInstallation) {
        $npmVersion = npm -v
        Write-Log "✓ npm versión: $npmVersion" -Type "Success"
    }
    else {
        throw "Node.js instalado pero no se encuentra en PATH"
    }
}

# ============================================================================
# 2. INSTALAR N8N GLOBAL
# ============================================================================

function Test-N8nInstallation {
    Write-Log "Verificando instalación de n8n..."
    try {
        $n8nVersion = n8n --version
        Write-Log "✓ n8n encontrado: $n8nVersion" -Type "Success"
        return $true
    }
    catch {
        Write-Log "✗ n8n no encontrado" -Type "Warning"
        return $false
    }
}

function Install-N8n {
    Write-Header "INSTALACIÓN DE N8N GLOBAL"
    
    if (Test-N8nInstallation) {
        return
    }
    
    Write-Log "Instalando n8n globalmente con npm..."
    try {
        npm install -g n8n
        Write-Log "✓ n8n instalado correctamente" -Type "Success"
    }
    catch {
        Write-Log "✗ Error instalando n8n: $_" -Type "Error"
        throw
    }
    
    if (-not (Test-N8nInstallation)) {
        throw "n8n instalado pero no se encuentra en PATH"
    }
}

# ============================================================================
# 3. GENERAR ARCHIVO .ENV
# ============================================================================

function Generate-EnvFile {
    Write-Header "GENERACIÓN DEL ARCHIVO .ENV"
    
    $envPath = Join-Path $N8nHome ".env"
    
    if (Test-Path $envPath) {
        Write-Log "Archivo .env ya existe en: $envPath" -Type "Warning"
        $response = Read-Host "¿Desea regenerarlo? (s/n)"
        if ($response -ne 's') {
            Write-Log "Usando archivo .env existente" -Type "Info"
            return
        }
    }
    
    # Crear carpeta n8n si no existe
    if (-not (Test-Path $N8nHome)) {
        New-Item -ItemType Directory -Path $N8nHome -Force | Out-Null
        Write-Log "Creada carpeta: $N8nHome" -Type "Success"
    }
    
    # Generar claves de encriptación
    $encryptionKey = [System.Convert]::ToBase64String((1..32 | ForEach-Object { [byte](Get-Random -Minimum 0 -Maximum 256) }))
    $apiKey = -join ((65..90) + (97..122) | Get-Random -Count 32 | ForEach-Object { [char]$_ })
    $basicAuthPass = -join ((65..90) + (97..122) + (48..57) | Get-Random -Count 16 | ForEach-Object { [char]$_ })
    
    # Leer credenciales desde el usuario o usar defaults
    Write-Log "Ingrese credenciales de Neo4j (presione Enter para usar defaults):"
    $neo4jHost = Read-Host "Neo4j Host [192.168.1.37]" -Default "192.168.1.37"
    $neo4jPort = Read-Host "Neo4j Port [7687]" -Default "7687"
    $neo4jUser = Read-Host "Neo4j Usuario [neo4j]" -Default "neo4j"
    $neo4jPassword = Read-Host "Neo4j Password [fenomenologia2024]" -Default "fenomenologia2024"
    $neo4jDb = Read-Host "Neo4j Database [neo4j]" -Default "neo4j"
    
    Write-Log "Ingrese rutas locales:"
    $localDataPath = Read-Host "Ruta de datos locales [C:\yo_estructural\datos]" -Default "C:\yo_estructural\datos"
    $obsidianPath = Read-Host "Ruta de Obsidian [C:\Users\$env:USERNAME\Obsidian\vault]" -Default "C:\Users\$env:USERNAME\Obsidian\vault"
    
    # Crear contenido .env
    $envContent = @"
# ============================================================================
# CONFIGURACIÓN N8N - YO ESTRUCTURAL v3.0
# Generado automáticamente: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
# ============================================================================

# === CONFIGURACIÓN DEL SERVIDOR N8N ===
N8N_PORT=$N8nPort
N8N_HOST=0.0.0.0
N8N_PROTOCOL=http
N8N_ENCRYPTION_KEY=$encryptionKey
N8N_API_KEY=$apiKey

# === AUTENTICACIÓN BÁSICA ===
N8N_BASIC_AUTH_ACTIVE=true
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=$basicAuthPass

# === BASE DE DATOS ===
# Usar SQLite por defecto (más simple para desarrollo local)
DB_TYPE=sqlite
DB_SQLITE_FILE=$($N8nHome -replace '\', '/')/n8n.db

# Descomenta las siguientes líneas si prefieres usar Postgres
# DB_TYPE=postgresdb
# DB_POSTGRESDB_HOST=localhost
# DB_POSTGRESDB_PORT=5432
# DB_POSTGRESDB_DATABASE=n8n
# DB_POSTGRESDB_USER=n8n
# DB_POSTGRESDB_PASSWORD=n8n_password

# === CREDENCIALES NEO4J ===
NEO4J_HOST=$neo4jHost
NEO4J_PORT=$neo4jPort
NEO4J_USER=$neo4jUser
NEO4J_PASSWORD=$neo4jPassword
NEO4J_DATABASE=$neo4jDb
NEO4J_URI=bolt://$neo4jHost`:$neo4jPort

# === RUTAS LOCALES ===
LOCAL_DATA_PATH=$localDataPath
OBSIDIAN_VAULT_PATH=$obsidianPath
WORKFLOWS_OUTPUT_PATH=$localDataPath\workflows
YAML_OUTPUT_PATH=$localDataPath\yaml_procesados

# === CONFIGURACIÓN AVANZADA ===
N8N_LOG_LEVEL=info
N8N_LOG_OUTPUT=console,file
N8N_LOG_FILE_LOCATION=$N8nHome/logs
N8N_TIMEZONE=America/Argentina/Buenos_Aires
N8N_EXECUTIONS_DATA_SAVE_ON_ERROR=all
N8N_EXECUTIONS_DATA_SAVE_ON_SUCCESS=all
N8N_EXECUTIONS_DATA_MAX_AGE=336  # 14 días

# === WEBHOOKS Y TÚNELES ===
# Para usar tunneling (exponer webhooks sin firewall):
# WEBHOOK_TUNNEL_URL=tu_dominio.com
# Descomenta si usarás ngrok o similares:
# WEBHOOK_URL=https://tu_dominio.com/

# === INTEGRACIONES OPCIONALES ===
# Google Drive
# GOOGLE_DRIVE_ENABLE=false
# GOOGLE_DRIVE_CLIENT_ID=tu_client_id
# GOOGLE_DRIVE_CLIENT_SECRET=tu_secret

# Supabase
# SUPABASE_URL=
# SUPABASE_KEY=

# ============================================================================
# FIN DE CONFIGURACIÓN
# ============================================================================
"@

    # Guardar archivo .env
    try {
        Set-Content -Path $envPath -Value $envContent -Encoding UTF8
        Write-Log "✓ Archivo .env creado: $envPath" -Type "Success"
        Write-Log "  - Encriptación: habilitada" -Type "Info"
        Write-Log "  - Base de datos: SQLite (local)" -Type "Info"
        Write-Log "  - Neo4j: $neo4jHost`:$neo4jPort" -Type "Info"
        Write-Log "  - Puerto n8n: $N8nPort" -Type "Info"
    }
    catch {
        Write-Log "✗ Error creando archivo .env: $_" -Type "Error"
        throw
    }
}

# ============================================================================
# 4. CREAR ESTRUCTURA DE DIRECTORIOS
# ============================================================================

function Initialize-Directories {
    Write-Header "INICIALIZACIÓN DE DIRECTORIOS"
    
    $dirs = @(
        $N8nHome,
        "$N8nHome\workflows",
        "$N8nHome\credentials",
        "$N8nHome\logs",
        $WorkflowsDir,
        $CredentialsDir
    )
    
    foreach ($dir in $dirs) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
            Write-Log "✓ Directorio creado: $dir" -Type "Success"
        }
        else {
            Write-Log "  Directorio existente: $dir" -Type "Info"
        }
    }
}

# ============================================================================
# 5. IMPORTAR CREDENCIALES
# ============================================================================

function Import-Credentials {
    Write-Header "IMPORTACIÓN DE CREDENCIALES"
    
    if (-not (Test-Path $CredentialsDir)) {
        Write-Log "Directorio de credenciales no encontrado: $CredentialsDir" -Type "Warning"
        return
    }
    
    $credFiles = Get-ChildItem -Path $CredentialsDir -Filter "*.json" -ErrorAction SilentlyContinue
    
    if ($credFiles.Count -eq 0) {
        Write-Log "No hay archivos de credenciales para importar" -Type "Info"
        return
    }
    
    Write-Log "Encontrados $($credFiles.Count) archivo(s) de credenciales"
    
    foreach ($credFile in $credFiles) {
        Write-Log "Importando: $($credFile.Name)"
        try {
            & n8n import:credentials --input $credFile.FullName --separate
            Write-Log "✓ Credenciales importadas: $($credFile.Name)" -Type "Success"
        }
        catch {
            Write-Log "✗ Error importando $($credFile.Name): $_" -Type "Warning"
        }
    }
}

# ============================================================================
# 6. IMPORTAR WORKFLOWS
# ============================================================================

function Import-Workflows {
    Write-Header "IMPORTACIÓN DE WORKFLOWS"
    
    if (-not (Test-Path $WorkflowsDir)) {
        Write-Log "Directorio de workflows no encontrado: $WorkflowsDir" -Type "Warning"
        Write-Log "Genere los workflows primero con: generate-n8n-workflows.ps1" -Type "Info"
        return
    }
    
    $workflowFiles = Get-ChildItem -Path $WorkflowsDir -Filter "*.json" -ErrorAction SilentlyContinue
    
    if ($workflowFiles.Count -eq 0) {
        Write-Log "No hay archivos de workflows para importar" -Type "Warning"
        return
    }
    
    Write-Log "Encontrados $($workflowFiles.Count) workflow(s)"
    
    foreach ($wfFile in $workflowFiles) {
        Write-Log "Importando: $($wfFile.Name)"
        try {
            & n8n import:workflow --input $wfFile.FullName
            Write-Log "✓ Workflow importado: $($wfFile.Name)" -Type "Success"
        }
        catch {
            Write-Log "✗ Error importando $($wfFile.Name): $_" -Type "Warning"
        }
    }
}

# ============================================================================
# 7. VALIDAR CONECTIVIDAD
# ============================================================================

function Test-Connectivity {
    Write-Header "VALIDACIÓN DE CONECTIVIDAD"
    
    Write-Log "Aguardando 5 segundos para que n8n inicie..."
    Start-Sleep -Seconds 5
    
    # Testear healthz
    Write-Log "Probando endpoint /healthz..."
    try {
        $response = Invoke-RestMethod -Uri "http://localhost:$N8nPort/healthz" -Method Get -ErrorAction SilentlyContinue
        Write-Log "✓ n8n está activo y responde" -Type "Success"
    }
    catch {
        Write-Log "✗ n8n no responde en http://localhost:$N8nPort" -Type "Warning"
    }
    
    # Testear Neo4j
    Write-Log "Probando conexión a Neo4j..."
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
    
    try {
        # Leer .env para obtener credenciales
        $envFile = Join-Path $N8nHome ".env"
        $envContent = Get-Content $envFile
        $neo4jHost = ($envContent | Select-String "NEO4J_HOST=" | ForEach-Object { $_.Line.Split("=")[1] }).Trim()
        $neo4jPort = ($envContent | Select-String "NEO4J_PORT=" | ForEach-Object { $_.Line.Split("=")[1] }).Trim()
        
        $testConnection = Test-NetConnection -ComputerName $neo4jHost -Port $neo4jPort -WarningAction SilentlyContinue
        
        if ($testConnection.TcpTestSucceeded) {
            Write-Log "✓ Neo4j es alcanzable en $neo4jHost`:$neo4jPort" -Type "Success"
        }
        else {
            Write-Log "✗ No se puede alcanzar Neo4j en $neo4jHost`:$neo4jPort" -Type "Warning"
        }
    }
    catch {
        Write-Log "✗ Error testeando Neo4j: $_" -Type "Warning"
    }
}

# ============================================================================
# 8. CREAR SERVICIO WINDOWS (OPCIONAL)
# ============================================================================

function Create-WindowsService {
    Write-Header "CREACIÓN DE SERVICIO WINDOWS"
    
    Write-Log "Este paso requiere descargar e instalar NSSM"
    $response = Read-Host "¿Continuar? (s/n)"
    
    if ($response -ne 's') {
        Write-Log "Creación de servicio cancelada" -Type "Info"
        return
    }
    
    # Descargar NSSM
    $nssmUrl = "https://nssm.cc/download/nssm-2.24-101-g897c7ad.zip"
    $nssmZip = "$env:TEMP\nssm.zip"
    $nssmPath = "$env:ProgramFiles\nssm"
    
    Write-Log "Descargando NSSM..."
    try {
        Invoke-WebRequest -Uri $nssmUrl -OutFile $nssmZip -UseBasicParsing
        
        # Extraer
        Expand-Archive -Path $nssmZip -DestinationPath $env:TEMP -Force
        
        # Copiar a Program Files
        $nssmExe = Get-ChildItem -Path $env:TEMP -Filter "nssm.exe" -Recurse | Select-Object -First 1
        
        if ($nssmExe) {
            Copy-Item $nssmExe.FullName "$nssmPath\nssm.exe" -Force
            Write-Log "✓ NSSM instalado" -Type "Success"
        }
    }
    catch {
        Write-Log "✗ Error instalando NSSM: $_" -Type "Warning"
        return
    }
    
    # Crear servicio
    Write-Log "Creando servicio Windows para n8n..."
    try {
        $envFile = Join-Path $N8nHome ".env"
        & "$nssmPath\nssm.exe" install n8n "n8n" "start" "--env-file" "`"$envFile`""
        & "$nssmPath\nssm.exe" set n8n AppDirectory "$N8nHome"
        & "$nssmPath\nssm.exe" set n8n AppRestartDelay 1000
        
        Write-Log "✓ Servicio n8n creado correctamente" -Type "Success"
        Write-Log "  Usar: net start n8n  |  net stop n8n" -Type "Info"
    }
    catch {
        Write-Log "✗ Error creando servicio: $_" -Type "Warning"
    }
}

# ============================================================================
# 9. FUNCIÓN PRINCIPAL
# ============================================================================

function Main {
    Write-Header "INSTALACIÓN COMPLETA DE N8N - YO ESTRUCTURAL v3.0"
    
    Write-Log "Parámetros detectados:" -Type "Info"
    Write-Log "  - N8n Home: $N8nHome" -Type "Info"
    Write-Log "  - N8n Port: $N8nPort" -Type "Info"
    Write-Log "  - Workflows Dir: $WorkflowsDir" -Type "Info"
    Write-Log "  - Credentials Dir: $CredentialsDir" -Type "Info"
    
    try {
        # Paso 1: Node.js
        if (-not $SkipNodeInstall) {
            Install-NodeJS
        }
        
        # Paso 2: n8n
        Install-N8n
        
        # Paso 3: Directorios
        Initialize-Directories
        
        # Paso 4: .env
        Generate-EnvFile
        
        if ($GenerateEnvOnly) {
            Write-Log "Modo GenerateEnvOnly: completado" -Type "Success"
            return
        }
        
        # Paso 5: Credenciales
        Import-Credentials
        
        # Paso 6: Workflows
        Import-Workflows
        
        # Paso 7: Validación
        Test-Connectivity
        
        # Paso 8: Servicio Windows
        if ($CreateWindowsService) {
            Create-WindowsService
        }
        
        Write-Header "✓ INSTALACIÓN COMPLETADA EXITOSAMENTE"
        Write-Log "n8n está configurado y listo para usar" -Type "Success"
        Write-Log "Para iniciar: n8n start --env-file $($N8nHome)\.env" -Type "Info"
        
    }
    catch {
        Write-Log "✗ Error durante la instalación: $_" -Type "Error"
        exit 1
    }
}

# ============================================================================
# EJECUTAR
# ============================================================================

Main
