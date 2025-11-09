#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Guía completa de instalación y despliegue de n8n con workflows para YO Estructural
    
.DESCRIPTION
    Este documento describe paso a paso cómo instalar y configurar n8n desde PowerShell
    sin interfaz gráfica, con 3 workflows optimizados para el sistema fenomenológico.
#>

Write-Host "
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║           🧠 GUÍA COMPLETA: N8N + YO ESTRUCTURAL v3.0                         ║
║                                                                                ║
║                    Instalación 100% desde PowerShell                           ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
" -ForegroundColor Magenta

Write-Host @"

# ============================================================================
# ÍNDICE DE CONTENIDOS
# ============================================================================

1. PREREQUISITOS
2. INSTALACIÓN RÁPIDA (3 comandos)
3. ESTRUCTURA DE DIRECTORIOS
4. WORKFLOWS EXPLICADOS
5. IMPORTACIÓN DE CREDENCIALES
6. VALIDACIÓN Y TESTING
7. OPERACIÓN Y MANTENIMIENTO
8. TROUBLESHOOTING
9. INTEGRACIÓN CON TU STACK

# ============================================================================
# 1. PREREQUISITOS
# ============================================================================

✓ Windows 10 / Windows 11
✓ PowerShell 5.1 o superior (Get-Host | Select-Object Version)
✓ Permisos administrativos en la máquina
✓ Conexión a Internet (para descargas)
✓ Mínimo 2GB de RAM disponible
✓ Neo4j corriendo en la red (192.168.1.37:7687 por defecto)

# ============================================================================
# 2. INSTALACIÓN RÁPIDA
# ============================================================================

OPCIÓN A: Instalación automática (recomendada)
----------------------------------------------

Paso 1: Abrir PowerShell como Administrador
Paso 2: Ejecutar este script

  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  
Paso 3: Navegar a la carpeta del proyecto y ejecutar

  .\n8n_setup\install-n8n-complete.ps1

El script automáticamente:
✓ Descarga e instala Node.js 18 LTS
✓ Instala n8n globalmente
✓ Crea archivo .env con tus credenciales
✓ Importa 3 workflows optimizados
✓ Importa credenciales
✓ Valida conectividad (Neo4j, webhooks)
✓ Crea un servicio Windows (opcional)


OPCIÓN B: Instalación manual paso a paso
-----------------------------------------

  # 1. Instalar Node.js
  iwr https://aka.ms/getwinget | iex
  winget install OpenJS.NodeJS.LTS
  
  # 2. Instalar n8n
  npm install -g n8n
  
  # 3. Generar .env (ver sección 3)
  
  # 4. Crear directorios
  mkdir $env:USERPROFILE\.n8n
  mkdir $env:USERPROFILE\.n8n\workflows
  mkdir $env:USERPROFILE\.n8n\credentials
  
  # 5. Copiar workflows y credenciales
  Copy-Item .\n8n_setup\workflows\* $env:USERPROFILE\.n8n\workflows\
  
  # 6. Iniciar n8n
  n8n start --env-file $env:USERPROFILE\.n8n\.env

# ============================================================================
# 3. ESTRUCTURA DE DIRECTORIOS
# ============================================================================

Tu proyecto estructura:
  
  YO estructural/
  ├── n8n_setup/
  │   ├── install-n8n-complete.ps1           ← SCRIPT MAESTRO
  │   ├── SETUP_GUIDE.md                     ← ESTE ARCHIVO
  │   ├── workflows/
  │   │   ├── workflow_1_monitor_archivos.json
  │   │   ├── workflow_2_sync_neo4j.json
  │   │   └── workflow_3_text_processing.json
  │   └── credentials/
  │       └── credentials_template.json
  │
  ├── configuracion/
  │   └── config.yaml                        ← CONFIGURACIÓN PRINCIPAL
  │
  └── motor_yo/
      └── sistema_yo_emergente.py            ← INTEGRACIÓN CON N8N

Después de la instalación, encontrarás:

  %USERPROFILE%\.n8n/
  ├── .env                                   ← CREDENCIALES (¡SECRETO!)
  ├── n8n.db                                 ← BASE DE DATOS (SQLite)
  ├── workflows/                             ← WORKFLOWS IMPORTADOS
  ├── credentials.json                       ← CREDENCIALES CIFRADAS
  └── logs/                                  ← LOGS DE EJECUCIÓN


# ============================================================================
# 4. WORKFLOWS EXPLICADOS
# ============================================================================

WORKFLOW 1: Monitor Archivos Locales
═════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────┐
│  [Watch Folder] → [Read File Content] → [Detect Type] → [Route]        │
│       ↓                                                      ↓           │
│     ├── [Log to Neo4j]                        ┌──────────────┘          │
│     │                                         │                         │
│     └─→ [Route by Type]  ┬────────────────────┼──→ [Send to Obsidian]  │
│                          ├──────────────────────→ [Send to JSON]        │
│                          └──────────────────────→ [Send to Text]        │
└─────────────────────────────────────────────────────────────────────────┘

Función:
  • Monitorea carpeta LOCAL_DATA_PATH continuamente
  • Detecta nuevos archivos (markdown, JSON, YAML, texto)
  • Registra metadatos en Neo4j
  • Routea a procesadores específicos según tipo
  
Variables de entorno usadas:
  LOCAL_DATA_PATH = Ruta a monitorear
  NEO4J_* = Credenciales Neo4j

Entrada: Carpeta en el disco local
Salida: Webhooks a otros workflows


WORKFLOW 2: Sync Neo4j
═════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────┐
│ [Webhook] → [Prepare Data] → [Create Node] → [Create Relations] →      │
│   /sync-neo4j                                   [Log Sync]              │
│                                                    ↓                     │
│                                            [Response Node]              │
└─────────────────────────────────────────────────────────────────────────┘

Función:
  • Recibe datos vía webhook POST
  • Valida y prepara datos para inserción
  • Ejecuta MERGE en Neo4j (crea o actualiza nodos)
  • Crea relaciones automáticas
  • Registra operación en log CSV
  
Variables:
  NEO4J_HOST, NEO4J_PORT, NEO4J_USER, NEO4J_PASSWORD
  LOCAL_DATA_PATH (para guardar logs)

Entrada: JSON vía webhook
Salida: Nodos/relaciones en Neo4j + log local


WORKFLOW 3: Text Processing & Embeddings
═════════════════════════════════════════════════════════════════════════════

┌──────────────────────────────────────────────────────────────────────────┐
│ [Webhook] → [Analyze] → [Keywords] → [Embeddings] ┬─→ [Save YAML]      │
│ /process-text                                      ├─→ [Send Neo4j]     │
│                                                    └─→ [Response]       │
└──────────────────────────────────────────────────────────────────────────┘

Función:
  • Recibe texto vía webhook
  • Analiza estadísticas (palabras, caracteres, líneas)
  • Extrae palabras clave (top 10)
  • Genera embeddings (mock o real)
  • Guarda JSON enriquecido localmente
  • Envía a Neo4j para sincronización
  
Variables:
  YAML_OUTPUT_PATH = Ubicación de YAML enriquecidos
  NEO4J_* = Para sincronización

Entrada: JSON con texto y metadatos
Salida: Archivos JSON enriquecidos + nodos en Neo4j


# ============================================================================
# 5. IMPORTACIÓN DE CREDENCIALES
# ============================================================================

Las credenciales se manejan de forma segura y automática.
Todas las variables de entorno se cifran en la base de datos de n8n.

Gestión manual (si necesitas agregar más tarde):

  # Listar credenciales
  n8n export:credentials --output .\credenciales_backup.json
  
  # Importar nuevas credenciales
  n8n import:credentials --input .\nuevas_credenciales.json --separate
  
  # Ver credenciales (cuidado: datos sensibles)
  n8n list:credentials

Ubicación de variables sensibles en .env:

  NEO4J_PASSWORD=fenomenologia2024       ← CAMBIAR EN PRODUCCIÓN
  N8N_ENCRYPTION_KEY=...                 ← GENERADO AUTOMÁTICAMENTE
  N8N_API_KEY=...                        ← GENERADO AUTOMÁTICAMENTE
  N8N_BASIC_AUTH_PASSWORD=...            ← GENERADO AUTOMÁTICAMENTE


# ============================================================================
# 6. VALIDACIÓN Y TESTING
# ============================================================================

Verificar instalación:

  # Comprobar Node.js
  node -v
  npm -v
  
  # Comprobar n8n
  n8n --version
  
  # Verificar archivo .env
  cat $env:USERPROFILE\.n8n\.env
  
  # Ver logs
  Get-Content $env:USERPROFILE\.n8n\logs\* -Tail 50

Testear conectividad:

  # Neo4j
  Test-NetConnection -ComputerName 192.168.1.37 -Port 7687
  
  # n8n (cuando está corriendo)
  Invoke-RestMethod http://localhost:5678/healthz
  
  # Verificar API key
  $headers = @{ "X-N8N-API-KEY" = "tu_api_key_aqui" }
  Invoke-RestMethod http://localhost:5678/rest/workflows -Headers $headers

Ejecutar workflow de prueba:

  # Usar Invoke-RestMethod para disparar webhook
  $body = @{
    contenido = "Este es un texto de prueba"
    id = "test_001"
    fuente = "manual_test"
  } | ConvertTo-Json
  
  Invoke-RestMethod -Uri http://localhost:5678/webhook/process-text \
    -Method Post \
    -Body $body \
    -ContentType application/json


# ============================================================================
# 7. OPERACIÓN Y MANTENIMIENTO
# ============================================================================

Iniciar n8n:

  # Inicio simple
  n8n start
  
  # Con variables de entorno
  n8n start --env-file $env:USERPROFILE\.n8n\.env
  
  # Con túnel (webhooks públicos sin firewall)
  n8n start --tunnel
  
  # Como servicio Windows (si instalaste NSSM)
  net start n8n
  net stop n8n

Operaciones cotidianas:

  # Ver workflows disponibles
  n8n list:workflows
  
  # Ver ejecuciones recientes
  n8n list:executions
  
  # Exportar workflows (backup)
  n8n export:workflow --all --output .\backup_workflows.json
  
  # Exportar credenciales (backup)
  n8n export:credentials --output .\backup_credentials.json

Monitoreo:

  # Ver logs en tiempo real
  tail -f $env:USERPROFILE\.n8n\logs\*
  
  # Ver uso de CPU/Memoria (Windows)
  Get-Process n8n | Format-Table ProcessName, CPU, Memory
  
  # Ver puerto 5678
  netstat -ano | findstr :5678


# ============================================================================
# 8. TROUBLESHOOTING
# ============================================================================

Problema: Node.js no se encuentra
─────────────────────────────────────────────────────────────────────────
Solución:
  1. Cierra PowerShell completamente
  2. Abre una nueva ventana como Administrador
  3. Ejecuta: refreshenv
  4. Verifica: node -v


Problema: npm no reconoce n8n
─────────────────────────────────────────────────────────────────────────
Solución:
  1. Reinstala n8n: npm install -g n8n --force
  2. Comprueba: npm list -g n8n
  3. Agrega a PATH manualmente si es necesario


Problema: No se puede conectar a Neo4j
─────────────────────────────────────────────────────────────────────────
Solución:
  1. Verifica que Neo4j está corriendo: Test-NetConnection -ComputerName 192.168.1.37 -Port 7687
  2. Comprueba credenciales en .env
  3. Revisa logs: docker logs neo4j (si usas Docker)
  4. Confirma firewall no bloquea puerto 7687


Problema: Webhooks no disparan
─────────────────────────────────────────────────────────────────────────
Solución:
  1. Verifica que n8n está corriendo: Invoke-RestMethod http://localhost:5678/healthz
  2. Chequea que el workflow está ACTIVE (not paused)
  3. Verifica la ruta exacta del webhook en la configuración
  4. Usa n8n con --tunnel si necesitas acceso desde Internet


Problema: Errores de encriptación o credenciales
─────────────────────────────────────────────────────────────────────────
Solución:
  1. Elimina base de datos corrupta: rm $env:USERPROFILE\.n8n\n8n.db
  2. Regenera .env: .\n8n_setup\install-n8n-complete.ps1 -GenerateEnvOnly
  3. Reimporta credenciales: n8n import:credentials --input ...


Problema: Puerto 5678 ya está en uso
─────────────────────────────────────────────────────────────────────────
Solución:
  1. Encuentra qué proceso ocupa el puerto: netstat -ano | findstr :5678
  2. Mata el proceso: taskkill /PID <pid> /F
  3. O cambia puerto en .env: N8N_PORT=5679


# ============================================================================
# 9. INTEGRACIÓN CON TU STACK
# ============================================================================

Conexión con motor_yo/sistema_yo_emergente.py:
───────────────────────────────────────────────────────────────────────────

Tu código Python puede disparar workflows de n8n:

  from integraciones.n8n_config import N8nIntegrator
  
  n8n_client = N8nIntegrator()
  
  # Disparar workflow de procesamiento de texto
  resultado = n8n_client.enviar_datos_webhook(
    datos={
      "contenido": "Aquí va el texto a procesar",
      "id": "mi_documento_001",
      "fuente": "motor_yo"
    },
    origen="sistema_fenomenologico"
  )
  
  if resultado['success']:
    print("✓ Procesamiento iniciado en n8n")
  else:
    print(f"✗ Error: {resultado['error']}")


Flujo completo de datos:
───────────────────────────────────────────────────────────────────────────

Obsidian (.md)
    ↓
[Workflow 1: Monitor] 
    ↓
[Workflow 3: Text Processing] 
    ↓ (enriquecido + embeddings)
[Workflow 2: Sync Neo4j]
    ↓
Neo4j (nodos + relaciones + vectores)
    ↓
motor_yo (consulta y analiza)
    ↓
YO emergente (síntesis fenomenológica)


Variables de entorno para integración:
───────────────────────────────────────────────────────────────────────────

En tu código Python, accede a:

  import os
  
  n8n_webhook_url = os.getenv('N8N_WEBHOOK_URL')  # Base para webhooks
  neo4j_uri = os.getenv('NEO4J_URI')              # Conexión a Neo4j
  local_data_path = os.getenv('LOCAL_DATA_PATH')  # Archivos locales


# ============================================================================
# COMANDOS RÁPIDOS (COPY-PASTE)
# ============================================================================

# Instalación completa automática
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser; `
.\n8n_setup\install-n8n-complete.ps1

# Instalar solo si necesitas Node.js
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser; `
.\n8n_setup\install-n8n-complete.ps1 -SkipNodeInstall

# Generar .env sin instalar todo
.\n8n_setup\install-n8n-complete.ps1 -GenerateEnvOnly

# Crear servicio Windows
.\n8n_setup\install-n8n-complete.ps1 -CreateWindowsService

# Iniciar n8n
n8n start --env-file `$env:USERPROFILE\.n8n\.env

# Exportar todos los workflows (backup)
n8n export:workflow --all --output workflows_backup_$(Get-Date -f yyyyMMdd).json

# Ver ejecuciones recientes
n8n list:executions | head -20

# Testear conectividad a Neo4j
Test-NetConnection -ComputerName 192.168.1.37 -Port 7687

# Ver logs en tiempo real
Get-Content -Path $env:USERPROFILE\.n8n\logs\* -Wait


# ============================================================================
# SOPORTE Y DOCUMENTACIÓN
# ============================================================================

Recursos oficiales:
  • n8n docs: https://docs.n8n.io/
  • n8n Community: https://community.n8n.io/
  • Neo4j Cypher: https://neo4j.com/docs/cypher-manual/

Documentación del proyecto:
  • ANALISIS_CONFIGURACION_PROYECTO.md
  • INSTRUCCIONES_NEO4J.md
  • Código fuente: integraciones/n8n_config.py

Para preguntas técnicas:
  • Revisar logs: $env:USERPROFILE\.n8n\logs\
  • Activar debug: N8N_LOG_LEVEL=debug en .env
  • Exportar configuración para análisis: n8n export:credentials + workflows

" -ForegroundColor Cyan

Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════════════════════╗" -ForegroundColor Magenta
Write-Host "║  ✓ Guía completada. ¡Listo para instalar!                                      ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════════════════════════════════════════════╝" -ForegroundColor Magenta
