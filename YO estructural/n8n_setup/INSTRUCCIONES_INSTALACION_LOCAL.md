# 🖥️ INSTRUCCIONES DE INSTALACIÓN LOCAL DUAL

**Proyecto:** YO Estructural v3.0 - Configuración de Dos Computadoras  
**Fecha:** 31/10/2025  
**Infraestructura:** Dual Core (n8n + Python) + i5 Core (Neo4j)

---

## 📋 ÍNDICE RÁPIDO

1. [Preparación de la Red Local](#1-preparación-de-la-red-local)
2. [Instalación en i5 Core (Neo4j)](#2-instalación-en-i5-core-neo4j)
3. [Instalación en Dual Core (n8n + Python)](#3-instalación-en-dual-core-n8n--python)
4. [Configuración de Google Drive y Gemini](#4-configuración-de-google-drive-y-gemini)
5. [Validación del Sistema Completo](#5-validación-del-sistema-completo)
6. [Operación Diaria](#6-operación-diaria)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. PREPARACIÓN DE LA RED LOCAL

### 1.1 Verificar Conectividad entre Computadoras

**En la Dual Core** (PowerShell):
```powershell
# Obtener IP de la i5 Core
# Ejemplo: 192.168.1.37

# Verificar conexión
Test-NetConnection -ComputerName 192.168.1.37 -Port 7687

# Debe responder: TcpTestSucceeded: True
```

**En la i5 Core** (Terminal/PowerShell):
```bash
# Verificar tu IP local
ipconfig  # Windows
ifconfig  # Linux/Mac

# Anotar la IP (ejemplo: 192.168.1.37)
```

### 1.2 Configurar Firewall

**En la i5 Core** (donde corre Neo4j):
```powershell
# Abrir puerto 7687 (Bolt Protocol)
New-NetFirewallRule -DisplayName "Neo4j Bolt" -Direction Inbound -Protocol TCP -LocalPort 7687 -Action Allow

# Abrir puerto 7474 (HTTP Browser)
New-NetFirewallRule -DisplayName "Neo4j HTTP" -Direction Inbound -Protocol TCP -LocalPort 7474 -Action Allow
```

---

## 2. INSTALACIÓN EN i5 CORE (Neo4j)

### 2.1 Opción A: Neo4j con Docker (RECOMENDADO)

```bash
# Instalar Docker Desktop (si no está instalado)
# Descargar desde: https://www.docker.com/products/docker-desktop/

# Crear directorio para datos persistentes
mkdir -p ~/neo4j/data
mkdir -p ~/neo4j/logs

# Ejecutar Neo4j
docker run -d \
  --name neo4j-yo-estructural \
  -p 7474:7474 \
  -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/fenomenologia2024 \
  -v ~/neo4j/data:/data \
  -v ~/neo4j/logs:/logs \
  neo4j:latest

# Verificar que está corriendo
docker ps

# Acceder al browser
# http://localhost:7474
# Usuario: neo4j
# Contraseña: fenomenologia2024
```

### 2.2 Opción B: Neo4j Nativo (Windows/Linux)

**Windows:**
```powershell
# Descargar Neo4j Community Edition
# https://neo4j.com/download/

# Ejecutar instalador
# Configurar durante instalación:
# - Puerto Bolt: 7687
# - Puerto HTTP: 7474
# - Contraseña: fenomenologia2024

# Iniciar servicio
neo4j console
```

**Linux:**
```bash
# Instalar Neo4j
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt-get update
sudo apt-get install neo4j

# Configurar
sudo nano /etc/neo4j/neo4j.conf
# Descomentar y modificar:
# dbms.default_listen_address=0.0.0.0

# Iniciar
sudo systemctl start neo4j
sudo systemctl enable neo4j

# Cambiar contraseña
cypher-shell
ALTER USER neo4j SET PASSWORD 'fenomenologia2024';
```

### 2.3 Verificar Acceso Remoto

**Desde la Dual Core:**
```powershell
# Probar conexión
Test-NetConnection -ComputerName 192.168.1.37 -Port 7687

# Instalar neo4j driver (si tienes Python para testing)
pip install neo4j

# Test rápido
python -c "from neo4j import GraphDatabase; driver = GraphDatabase.driver('bolt://192.168.1.37:7687', auth=('neo4j', 'fenomenologia2024')); print('✓ Conexión exitosa'); driver.close()"
```

---

## 3. INSTALACIÓN EN DUAL CORE (n8n + Python)

### 3.1 Instalar n8n con PowerShell

**Abrir PowerShell como ADMINISTRADOR:**

```powershell
# 1. Permitir ejecución de scripts
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# 2. Navegar al proyecto
cd "C:\ruta\a\YO estructural"

# 3. Ejecutar instalador
.\n8n_setup\deploy-n8n-complete.ps1
```

**Durante la instalación se pedirá:**
- IP de Neo4j (ejemplo: `192.168.1.37`)
- Puerto de Neo4j (ejemplo: `7687`)
- Usuario Neo4j (ejemplo: `neo4j`)
- Contraseña Neo4j (ejemplo: `fenomenologia2024`)
- Ruta local de datos (ejemplo: `C:\YO_Estructural\data`)
- Ruta de salida YAML (ejemplo: `C:\YO_Estructural\yaml_output`)

### 3.2 Configurar Variables de Entorno Adicionales

**Editar el archivo `.env` generado:**

```powershell
# Abrir el archivo
notepad $env:USERPROFILE\.n8n\.env
```

**Agregar estas variables NUEVAS:**

```env
# === CONFIGURACIÓN ESPECÍFICA MULTICOMPUTADORA ===

# Neo4j (ya están, verificar que tengan la IP correcta)
NEO4J_HOST=192.168.1.37
NEO4J_PORT=7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=fenomenologia2024
NEO4J_DATABASE=neo4j

# Google Drive
GOOGLE_DRIVE_FOLDER_ID=tu_folder_id_aqui
# Para obtener el ID: abre la carpeta en Drive, copia el ID de la URL
# https://drive.google.com/drive/folders/ESTE_ES_EL_ID

# Gemini API
GEMINI_API_KEY=tu_api_key_de_gemini
# Obtener en: https://aistudio.google.com/app/apikey

# Rutas locales (ajustar según tu estructura)
LOCAL_DATA_PATH=C:\YO_Estructural\entrada_bruta
YAML_OUTPUT_PATH=C:\YO_Estructural\procesado\yaml_automaticos
```

**Guardar y cerrar.**

### 3.3 Instalar Python y Dependencias

```powershell
# Verificar Python (3.8+)
python --version

# Si no está instalado, descargar desde:
# https://www.python.org/downloads/

# Instalar dependencias del proyecto
cd "C:\ruta\a\YO estructural"
pip install -r requirements.txt

# Verificar que neo4j driver está instalado
pip install neo4j python-dotenv pyyaml fastapi uvicorn
```

### 3.4 Importar Workflow 4 (Google Drive Multimodal)

```powershell
# Con n8n corriendo, importar el nuevo workflow
n8n import:workflow --input=".\n8n_setup\workflow_4_google_drive_multimodal.json"

# Verificar workflows importados
n8n list:workflows
```

---

## 4. CONFIGURACIÓN DE GOOGLE DRIVE Y GEMINI

### 4.1 Configurar Credenciales de Google Drive en n8n

1. **Iniciar n8n:**
   ```powershell
   n8n start --env-file $env:USERPROFILE\.n8n\.env
   ```

2. **Abrir interfaz:** `http://localhost:5678`

3. **Agregar credenciales:**
   - Ir a: `Settings` → `Credentials` → `New`
   - Tipo: `Google OAuth2 API`
   - Nombre: `Google Drive YO Estructural`
   - Seguir wizard de autenticación
   - Scopes necesarios: `https://www.googleapis.com/auth/drive.readonly`

4. **Configurar Workflow 4:**
   - Abrir workflow `Google Drive Multimodal Processing`
   - Nodo `Google Drive Trigger` → asignar credencial creada
   - Nodo `Download File` → asignar misma credencial
   - Guardar (`Ctrl+S`)

### 4.2 Obtener API Key de Gemini

1. Ir a: https://aistudio.google.com/app/apikey
2. Crear nuevo proyecto (si no tienes)
3. Generar API Key
4. Copiar y pegar en `.env` (variable `GEMINI_API_KEY`)

**Reiniciar n8n para cargar nueva variable:**
```powershell
# Detener n8n (Ctrl+C)
# Reiniciar
n8n start --env-file $env:USERPROFILE\.n8n\.env
```

---

## 5. VALIDACIÓN DEL SISTEMA COMPLETO

### 5.1 Test de Conectividad

```powershell
# Ejecutar validador
cd "C:\ruta\a\YO estructural"
.\n8n_setup\validate-installation.ps1

# Debe mostrar:
# ✓ Node.js instalado
# ✓ n8n instalado
# ✓ .env configurado
# ✓ Neo4j accesible (192.168.1.37:7687)
# ✓ Workflows importados (4 workflows)
```

### 5.2 Test Manual del Flujo Completo

**Paso 1: Crear archivo de prueba en Google Drive**

1. Subir un PDF o imagen a la carpeta monitoreada
2. Esperar 1 minuto (polling de n8n)

**Paso 2: Verificar logs de n8n**

```powershell
# Ver logs en tiempo real
Get-Content $env:USERPROFILE\.n8n\logs\* -Wait
```

Deberías ver:
- `[Workflow 4] Archivo detectado: test.pdf`
- `[Gemini] Procesando con Vision API`
- `[Workflow 3] Texto recibido para procesamiento`
- `[Workflow 2] Sincronizando con Neo4j`

**Paso 3: Verificar en Neo4j**

```cypher
// En Neo4j Browser (http://192.168.1.37:7474)
MATCH (n) 
WHERE n.fuente = 'google_drive_gemini'
RETURN n
LIMIT 10
```

Deberías ver nodos creados con el contenido extraído.

**Paso 4: Verificar archivos generados**

```powershell
# Verificar YAML generado
dir "C:\YO_Estructural\procesado\yaml_automaticos"

# Verificar texto fenomenológico
dir "C:\YO_Estructural\entrada_bruta"
```

---

## 6. OPERACIÓN DIARIA

### 6.1 Iniciar el Sistema (Dual Core)

**Script de inicio rápido** (`iniciar_sistema.ps1`):

```powershell
# === SCRIPT DE INICIO ===
# Guardar como: C:\YO_Estructural\iniciar_sistema.ps1

Write-Host "🚀 Iniciando YO Estructural v3.0..." -ForegroundColor Cyan

# 1. Verificar Neo4j (i5 Core)
Write-Host "`n📊 Verificando Neo4j en i5 Core..."
$neo4j = Test-NetConnection -ComputerName 192.168.1.37 -Port 7687 -InformationLevel Quiet
if ($neo4j) {
    Write-Host "✓ Neo4j accesible" -ForegroundColor Green
} else {
    Write-Host "✗ Neo4j NO accesible. Verificar i5 Core." -ForegroundColor Red
    exit
}

# 2. Iniciar n8n
Write-Host "`n🤖 Iniciando n8n..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot'; n8n start --env-file $env:USERPROFILE\.n8n\.env"

Start-Sleep -Seconds 5

# 3. Verificar n8n
$n8n = Test-NetConnection -ComputerName localhost -Port 5678 -InformationLevel Quiet
if ($n8n) {
    Write-Host "✓ n8n iniciado correctamente" -ForegroundColor Green
} else {
    Write-Host "✗ n8n NO respondió en puerto 5678" -ForegroundColor Red
}

# 4. Abrir browser (opcional)
Write-Host "`n🌐 Abriendo interfaz web..."
Start-Process "http://localhost:5678"

Write-Host "`n✅ Sistema listo. Monitorea los logs en la otra ventana de PowerShell." -ForegroundColor Green
Write-Host "📂 Carpeta monitoreada: $env:LOCAL_DATA_PATH"
Write-Host "📊 Neo4j Browser: http://192.168.1.37:7474"
```

**Ejecutar:**
```powershell
.\iniciar_sistema.ps1
```

### 6.2 Detener el Sistema

```powershell
# Detener n8n (Ctrl+C en la ventana donde corre)

# O matar proceso
Stop-Process -Name "node" -Force
```

---

## 7. TROUBLESHOOTING

### ❌ Error: "No se puede conectar a Neo4j"

**Solución:**
```powershell
# Verificar que Neo4j corre en i5 Core
Test-NetConnection -ComputerName 192.168.1.37 -Port 7687

# Si falla, en i5 Core:
docker ps  # Verificar contenedor corriendo
docker logs neo4j-yo-estructural  # Ver logs

# O si es nativo:
sudo systemctl status neo4j
```

### ❌ Error: "Gemini API Key inválida"

**Solución:**
```powershell
# Verificar .env
notepad $env:USERPROFILE\.n8n\.env

# Debe tener:
# GEMINI_API_KEY=AIza...tu_key_completa

# Reiniciar n8n después de cambios
```

### ❌ Error: "Google Drive Trigger no detecta archivos"

**Solución:**
1. Verificar credenciales OAuth2 en n8n UI
2. Verificar `GOOGLE_DRIVE_FOLDER_ID` en `.env`
3. Verificar permisos de la carpeta (debe ser accesible con la cuenta OAuth)
4. Activar workflow manualmente:
   ```powershell
   n8n activate:workflow --id=google-drive-multimodal
   ```

### ❌ Error: "Workflow 3 no recibe datos"

**Solución:**
```powershell
# Verificar que Workflow 3 está activo
n8n list:workflows

# Activar manualmente
n8n activate:workflow --name="Text Processing"

# Test directo con curl
curl -X POST http://localhost:5678/webhook/process-text `
  -H "Content-Type: application/json" `
  -d '{"id_documento":"test","contenido":"Texto de prueba","fuente":"manual"}'
```

### ❌ Error: "Python no encuentra módulos"

**Solución:**
```powershell
# Reinstalar dependencias
cd "C:\ruta\a\YO estructural"
pip install -r requirements.txt --upgrade

# Verificar instalación
pip list | Select-String "neo4j|fastapi|yaml"
```

---

## 📊 CHECKLIST FINAL

### En i5 Core:
- [ ] Neo4j instalado y corriendo
- [ ] Puerto 7687 abierto en firewall
- [ ] Contraseña configurada: `fenomenologia2024`
- [ ] Accesible desde Dual Core (test con `Test-NetConnection`)

### En Dual Core:
- [ ] Node.js 18 LTS instalado
- [ ] n8n instalado globalmente
- [ ] `.env` configurado con IP correcta de Neo4j
- [ ] 4 workflows importados
- [ ] Google Drive OAuth configurado
- [ ] Gemini API Key configurada
- [ ] Python 3.8+ con dependencias instaladas
- [ ] Rutas `LOCAL_DATA_PATH` y `YAML_OUTPUT_PATH` creadas

### Validación:
- [ ] `validate-installation.ps1` ejecutado exitosamente
- [ ] Test manual con archivo en Google Drive
- [ ] Nodos aparecen en Neo4j Browser
- [ ] Archivos YAML generados en `YAML_OUTPUT_PATH`

---

## 🎉 SISTEMA OPERATIVO

Si todos los checks están ✓, tu sistema YO Estructural está completamente funcional en las dos computadoras.

**Próximos pasos:**
1. Subir documentos fenomenológicos a Google Drive
2. Observar el procesamiento automático
3. Consultar el grafo en Neo4j
4. Ejecutar análisis con `sistema_yo_emergente.py`

---

**Última actualización:** 31/10/2025  
**Soporte:** Ver `START_HERE.txt` y `SETUP_GUIDE.md` para más detalles
