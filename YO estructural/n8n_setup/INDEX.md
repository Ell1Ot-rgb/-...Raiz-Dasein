# 📑 ÍNDICE COMPLETO: Sistema N8N + YO Estructural v3.0

## 📁 Estructura de carpetas

```
YO estructural/n8n_setup/
│
├── 🚀 SCRIPTS PRINCIPALES (Ejecutables)
│   ├── deploy-n8n-complete.ps1         ← ¡EJECUTA ESTE PRIMERO!
│   ├── install-n8n-complete.ps1        ← Instalador detallado
│   └── validate-installation.ps1       ← Validador post-instalación
│
├── 📖 DOCUMENTACIÓN
│   ├── INDEX.md                        ← Este archivo
│   ├── QUICK_START.md                  ← Copia y pega (5 min)
│   ├── README.md                       ← Intro rápida (10 min)
│   ├── SETUP_GUIDE.md                  ← Guía completa (30 min)
│   ├── RESUMEN_EJECUTIVO.md            ← Visión general
│   └── COMMIT_INSTRUCTIONS.md          ← Para hacer push a git
│
├── 🔄 WORKFLOWS (JSON)
│   └── workflows/
│       ├── workflow_1_monitor_archivos.json
│       ├── workflow_2_sync_neo4j.json
│       └── workflow_3_text_processing.json
│
└── 🔐 CREDENCIALES
    └── credentials/
        └── credentials_template.json
```

---

## 📊 Tabla de contenidos por tipo

### 🎯 Por qué viniste aquí

| Necesito... | Leer esto... | Tiempo |
|-------------|------------|--------|
| Empezar YA | QUICK_START.md | 5 min |
| Entender qué hay | README.md | 10 min |
| Tutorial paso a paso | SETUP_GUIDE.md | 30 min |
| Visión general | RESUMEN_EJECUTIVO.md | 15 min |
| Hacer commit a git | COMMIT_INSTRUCTIONS.md | 10 min |
| Instalar manualmente | Ver dentro de install-n8n-complete.ps1 | 20 min |

---

## 🚀 QUICK LINKS

### Instalación rápida (3 comandos)

```powershell
# Copiar en PowerShell como Administrador:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

cd "C:\ruta\a\YO estructural"

.\n8n_setup\deploy-n8n-complete.ps1
```

### Iniciar n8n

```powershell
n8n start --env-file $env:USERPROFILE\.n8n\.env
```

### Interfaz web

```
http://localhost:5678
Usuario: admin
Contraseña: (se muestra en instalación)
```

---

## 📋 Descripción de cada archivo

### 🟢 SCRIPTS PowerShell

#### `deploy-n8n-complete.ps1` ⭐ PRINCIPAL
- **Propósito**: Orquestador maestro que automatiza TODO
- **Uso**: `.\deploy-n8n-complete.ps1`
- **Hace**:
  - Descarga e instala Node.js 18 LTS
  - Instala n8n globalmente
  - Genera archivo `.env` seguro
  - Importa 3 workflows
  - Valida conectividad
  - (Opcional) Crea servicio Windows
- **Tiempo**: 10-15 minutos
- **Salida**: Sistema listo para usar

#### `install-n8n-complete.ps1`
- **Propósito**: Instalador parametrizado con control granular
- **Uso**: `.\install-n8n-complete.ps1 [-SkipNodeInstall] [-GenerateEnvOnly] [-CreateWindowsService]`
- **Flags útiles**:
  - `-SkipNodeInstall`: Si ya tienes Node
  - `-GenerateEnvOnly`: Solo generar .env
  - `-CreateWindowsService`: Agregar servicio Windows
- **Tiempo**: Depende de flags (5-15 min)

#### `validate-installation.ps1`
- **Propósito**: Verificar post-instalación
- **Uso**: `.\validate-installation.ps1 [-QuickTest]`
- **Valida**:
  - Node.js y npm
  - n8n está instalado
  - Archivo .env existe
  - Directorios creados
  - Base de datos
  - Conectividad (si n8n corre)
  - Webhooks funcionan (si `-QuickTest`)
- **Tiempo**: 2-5 min

---

### 📖 DOCUMENTACIÓN

#### `QUICK_START.md` ⭐ INICIO
- **Para**: Usuarios impacientes (5 min)
- **Contiene**: Un comando de una línea
- **Salida**: Sistema instalado

#### `README.md` ⭐ INICIO
- **Para**: Primer contacto (10 min)
- **Contiene**:
  - Instalación rápida paso a paso
  - 3 workflows en tabla
  - Variables de entorno
  - Primeros pasos
  - Troubleshooting rápido

#### `SETUP_GUIDE.md` ⭐ COMPLETA
- **Para**: Aprendizaje profundo (30 min lectura)
- **Contiene**:
  - Prerequisitos
  - Instalación manual
  - Estructura de directorios
  - Explicación detallada de workflows (con diagramas ASCII)
  - Importación de credenciales
  - Validación y testing
  - Operación y mantenimiento
  - Troubleshooting completo
  - Integración con tu stack

#### `RESUMEN_EJECUTIVO.md`
- **Para**: Visión general ejecutiva (15 min)
- **Contiene**:
  - Qué se creó
  - Flujo de datos completo
  - Componentes
  - Casos de uso
  - Checklist de verificación
  - Operación diaria
  - Integración con Python

#### `COMMIT_INSTRUCTIONS.md`
- **Para**: Versionar el setup en git (10 min)
- **Contiene**:
  - Qué versionar y qué no
  - Comandos git paso a paso
  - Mensajes de commit recomendados
  - Checklist de seguridad
  - Procedimientos para actualizaciones futuras

---

### 🔄 WORKFLOWS (JSON)

Estos son archivos listos para importar en n8n. Se copian automáticamente durante la instalación.

#### `workflows/workflow_1_monitor_archivos.json`
```
Watch Folder → Read → Detect Type → Log Neo4j → Route
                                        ├→ Obsidian
                                        ├→ JSON
                                        └→ Text
```
- **Entrada**: Carpeta en disco
- **Salida**: Webhooks a otros workflows
- **Función**: Monitorear archivos locales continuamente

#### `workflows/workflow_2_sync_neo4j.json`
```
Webhook → Prepare → Create Node → Create Relations → Log → Response
```
- **Entrada**: Webhook JSON
- **Salida**: Nodos en Neo4j + log CSV
- **Función**: Sincronizar datos con grafos

#### `workflows/workflow_3_text_processing.json`
```
Webhook → Analyze → Keywords → Embeddings → Save YAML
                                      ├→ Neo4j
                                      └→ Response
```
- **Entrada**: Webhook con texto
- **Salida**: YAML enriquecido + nodos Neo4j
- **Función**: Procesar texto y enriquecer

---

### 🔐 CREDENCIALES

#### `credentials/credentials_template.json`
- **Propósito**: Template de credenciales (para referencia)
- **Contiene**: Estructura de Neo4j, Basic Auth, API Key
- **Nota**: Los valores reales se generan en `.env` durante instalación

---

## 🎯 Flujos de trabajo típicos

### Escenario 1: Instalación limpia (Nuevo usuario)

```
1. Leer: QUICK_START.md (5 min)
2. Ejecutar: deploy-n8n-complete.ps1
3. Esperar a que termine (10-15 min)
4. Ejecutar: n8n start
5. Abrir: http://localhost:5678
6. ¡Listo!
```

### Escenario 2: Instalación manual con control

```
1. Leer: SETUP_GUIDE.md (30 min)
2. Ejecutar: install-n8n-complete.ps1 paso a paso
3. Ejecutar scripts de validación
4. Leer: Integración con motor_yo
5. Configurar credenciales manuales si es necesario
```

### Escenario 3: Actualizar workflows

```
1. Editar workflow en UI de n8n
2. Exportar: n8n export:workflow --all --output backup.json
3. Copiar JSON a: workflows/
4. Hacer commit: git add workflows/ && git commit ...
5. Push: git push
```

### Escenario 4: Troubleshooting

```
1. Ejecutar: validate-installation.ps1
2. Revisar logs: tail -f $env:USERPROFILE\.n8n\logs\*
3. Buscar solución en SETUP_GUIDE.md (Troubleshooting)
4. Si no funciona: ir a n8n community o crear issue
```

---

## 🔗 Referencias cruzadas

```
QUICK_START.md
  └─ Remite a: README.md
      └─ Remite a: SETUP_GUIDE.md
          ├─ Explica: Workflows
          ├─ Explica: Credenciales
          └─ Remite a: COMMIT_INSTRUCTIONS.md

RESUMEN_EJECUTIVO.md
  ├─ Resumen de: Todo lo anterior
  ├─ Incluye: Casos de uso
  └─ Casos de uso integran con: motor_yo (Python)
```

---

## 📦 Lo que se instala

```
Mínimo requerido:
  • Node.js 18 LTS
  • npm
  • n8n (global)
  
Se crea en tu máquina:
  %USERPROFILE%\.n8n\
  ├── .env (credenciales)
  ├── n8n.db (SQLite)
  ├── workflows/ (los 3 JSON)
  ├── credentials.json (cifrado)
  └── logs/ (ejecución)

Se descarga/genera:
  • SQLite database (local)
  • Workflows JSON (3 archivos)
  • Credenciales (desde plantilla)
  
NO se descarga:
  • Docker (opcional)
  • Postgres (opcional, SQLite es suficiente)
  • Dependencias Node (solo n8n que es 1 paquete global)
```

---

## ⚡ Comandos de referencia rápida

```powershell
# INSTALACIÓN
.\deploy-n8n-complete.ps1                  # Todo automatizado
.\install-n8n-complete.ps1                # Instalación manual
.\validate-installation.ps1               # Validar

# OPERACIÓN
n8n start                                  # Iniciar
n8n start --tunnel                         # Con webhooks públicos
n8n list:workflows                         # Ver workflows
n8n list:executions                        # Ver ejecuciones
n8n export:workflow --all                  # Backup

# MONITOREO
tail -f $env:USERPROFILE\.n8n\logs\*     # Logs en vivo
Invoke-RestMethod http://localhost:5678/healthz  # Health check

# MANTENIMIENTO
Get-Process n8n                            # Ver proceso
Stop-Process -Name n8n                     # Matar proceso
```

---

## 🚨 Archivos que NO deben versionar

```gitignore
# N8N - ¡SECRETO!
.env                      # Credenciales
.env.local
n8n.db                    # Base de datos
credentials.json          # Credenciales cifradas
%USERPROFILE%\.n8n\

# Logs
logs/
*.log

# Node
node_modules/
npm-debug.log
```

---

## ✅ Checklist de instalación

- [ ] PowerShell abierto como Administrador
- [ ] Navego a carpeta del proyecto
- [ ] Ejecuto `deploy-n8n-complete.ps1`
- [ ] El script termina sin errores
- [ ] Ejecuto `n8n start`
- [ ] Abro http://localhost:5678
- [ ] Veo 3 workflows en la UI (ACTIVE)
- [ ] Veo logs sin errores críticos
- [ ] Puedo validar con `validate-installation.ps1`

---

## 🎓 Orden recomendado de lectura

### Para aprender rápido (30 min total)
1. Este archivo (INDEX.md) - 5 min
2. QUICK_START.md - 3 min
3. README.md - 10 min
4. RESUMEN_EJECUTIVO.md - 12 min

### Para aprender completo (90 min total)
1. Este archivo (INDEX.md) - 5 min
2. QUICK_START.md - 3 min
3. README.md - 10 min
4. SETUP_GUIDE.md - 40 min
5. RESUMEN_EJECUTIVO.md - 15 min
6. COMMIT_INSTRUCTIONS.md - 10 min
7. Revisar workflows JSON - 7 min

---

## 🆘 Si necesitas ayuda

```
Problema: No sé por dónde empezar
Solución: Lee QUICK_START.md (5 min)

Problema: Necesito instalación manual
Solución: Lee SETUP_GUIDE.md (30 min)

Problema: No funciona algo
Solución: Ejecuta validate-installation.ps1

Problema: Quiero entender todo
Solución: Lee RESUMEN_EJECUTIVO.md

Problema: Quiero versionar en git
Solución: Lee COMMIT_INSTRUCTIONS.md

Problema: Workflow no ejecuta
Solución: SETUP_GUIDE.md → Troubleshooting

Problema: Neo4j no conecta
Solución: SETUP_GUIDE.md → Troubleshooting → Conectividad
```

---

## 📞 Contacto y referencias

**Documentación oficial:**
- n8n: https://docs.n8n.io/
- Neo4j: https://neo4j.com/docs/
- PowerShell: https://learn.microsoft.com/en-us/powershell/

**En este proyecto:**
- motor_yo/sistema_yo_emergente.py (integración Python)
- configuracion/config.yaml (config principal)
- integraciones/n8n_config.py (cliente n8n en Python)

---

## 📅 Historial

| Fecha | Versión | Cambios |
|-------|---------|---------|
| 2025-10-31 | 3.0 | Creación inicial - Setup completo desde PowerShell |

---

## 📝 Notas finales

Este setup fue creado para ser:
- ✅ Completamente automatizado
- ✅ Sin interfaz gráfica necesaria
- ✅ Versionable en git
- ✅ Reproducible en cualquier máquina Windows
- ✅ Integrable con tu stack de Python

**Principio**: Máxima automatización, mínima fricción.

---

**🎉 ¡Bienvenido a n8n + YO Estructural v3.0!**

**Comienza aquí:** Lee QUICK_START.md (5 minutos)

