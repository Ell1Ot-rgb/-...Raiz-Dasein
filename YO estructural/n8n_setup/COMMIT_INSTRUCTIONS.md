# Instrucciones para Commit del Setup de N8N al Repositorio

## 📋 Resumen de archivos creados

```
YO estructural/n8n_setup/
├── deploy-n8n-complete.ps1          ← Script maestro de despliegue
├── install-n8n-complete.ps1         ← Instalador completo
├── validate-installation.ps1        ← Validador post-instalación
├── README.md                         ← Guía rápida
├── SETUP_GUIDE.md                    ← Documentación completa
├── workflows/
│   ├── workflow_1_monitor_archivos.json
│   ├── workflow_2_sync_neo4j.json
│   └── workflow_3_text_processing.json
└── credentials/
    └── credentials_template.json
```

## 🔐 Archivos que NO deben versionarse

Agrega esto a `.gitignore`:

```gitignore
# N8N - NO VERSIONAR (datos sensibles)
%USERPROFILE%/.n8n/
.n8n/
n8n/
*.db
credentials.json
.env
.env.local
.env.*.local

# Logs
logs/
*.log

# Node modules (si aplica)
node_modules/
npm-debug.log*
```

## 📝 Comandos para hacer commit

### 1. Verificar estado actual

```powershell
cd "C:\ruta\a\YO estructural"
git status
```

### 2. Agregar los nuevos archivos

```powershell
# Agregar solo la carpeta n8n_setup
git add n8n_setup/

# O agregar específicamente (sin archivos sensibles)
git add n8n_setup/*.ps1
git add n8n_setup/*.md
git add n8n_setup/workflows/
git add n8n_setup/credentials/credentials_template.json
```

### 3. Verificar cambios

```powershell
git diff --cached
```

### 4. Hacer commit

```powershell
git commit -m "Feat: Sistema de instalación n8n automatizado desde PowerShell

- Agregado script maestro: deploy-n8n-complete.ps1
- Instalador completo: install-n8n-complete.ps1
- Validador post-instalación: validate-installation.ps1
- 3 workflows JSON optimizados para YO Estructural:
  • Workflow 1: Monitor de archivos locales
  • Workflow 2: Sincronización con Neo4j
  • Workflow 3: Procesamiento de texto + embeddings
- Plantilla de credenciales
- Documentación completa (README.md + SETUP_GUIDE.md)

Características:
✓ Instalación 100% desde PowerShell
✓ Gestión automática de variables de entorno
✓ Sin interfaz gráfica necesaria
✓ Validación post-instalación
✓ Integración con motor_yo/sistema_yo_emergente.py

Uso:
  .\n8n_setup\deploy-n8n-complete.ps1"
```

### 5. Ver el commit

```powershell
git log -1 --stat
```

### 6. Hacer push

```powershell
git push origin main
```

## ✅ Checklist de commit

- [ ] `deploy-n8n-complete.ps1` incluido
- [ ] `install-n8n-complete.ps1` incluido
- [ ] `validate-installation.ps1` incluido
- [ ] Archivos de workflows JSON incluidos
- [ ] Documentación (README.md, SETUP_GUIDE.md) incluida
- [ ] `.gitignore` actualizado (sin .env, n8n.db, logs, etc.)
- [ ] **NO incluir** archivo `.env` real
- [ ] **NO incluir** `n8n.db` o credenciales
- [ ] **NO incluir** carpeta `node_modules` si existe
- [ ] Mensaje de commit descriptivo
- [ ] Verificado con `git status` antes de push

## 📋 Mensaje de commit recomendado

Si prefieres un formato alternativo:

```
Feat: Automatización completa de n8n desde PowerShell

Add n8n setup system:
- Master deployment script (deploy-n8n-complete.ps1)
- Full installer with Node.js + n8n (install-n8n-complete.ps1)
- Post-installation validator (validate-installation.ps1)
- 3 optimized n8n workflows for YO Estructural
- Complete documentation (README + SETUP_GUIDE)
- Credentials template for Neo4j integration

Features:
- 100% PowerShell-based installation
- Headless operation (no GUI required)
- Automatic environment variable management
- File monitoring and local processing
- Neo4j synchronization
- Text enrichment with embeddings

Usage: .\n8n_setup\deploy-n8n-complete.ps1
```

## 🔄 Después del commit

### Para otros usuarios del proyecto

```powershell
# Obtener los cambios
git pull origin main

# Ejecutar instalación
cd "YO estructural"
.\n8n_setup\deploy-n8n-complete.ps1

# Iniciar n8n
n8n start --env-file $env:USERPROFILE\.n8n\.env
```

### Para actualizar workflows después

```powershell
# Exportar workflows actualizados
n8n export:workflow --all --output .\n8n_setup\workflows\backup_$(Get-Date -f yyyyMMdd).json

# Luego actualizar los JSON en el repo
# y hacer commit de cambios

git add n8n_setup/workflows/
git commit -m "Update: Workflows n8n actualizados"
git push origin main
```

## 📊 Estructura de commits futuros

Si necesitas actualizar workflows:

```powershell
git add n8n_setup/workflows/workflow_*.json
git commit -m "Update: Workflows n8n - Agrega procesamiento de X"
git push origin main
```

Para cambios en documentación:

```powershell
git add n8n_setup/*.md
git commit -m "Docs: Actualiza SETUP_GUIDE con ejemplos de uso"
git push origin main
```

## ⚠️ Consideraciones de seguridad

**NUNCA hacer commit de:**
- `.env` (contiene credenciales)
- `n8n.db` (base de datos)
- `credentials.json` (credenciales cifradas)
- Logs personales

**SÍ hacer commit de:**
- Scripts PowerShell (sin credenciales hardcodeadas)
- Workflows JSON (sin datos sensibles)
- Documentación
- Templates (.env.template, credentials_template.json)

## 🎯 Próximos pasos

1. ✅ Ejecutar: `git add n8n_setup/`
2. ✅ Verificar: `git status`
3. ✅ Commit: `git commit -m "..."`
4. ✅ Push: `git push origin main`
5. ✅ Verificar en GitHub: `https://github.com/Ell1Ot-rgb/-...Raiz-Dasein`

---

**¿Preguntas?** Revisa:
- `n8n_setup/README.md` - Guía rápida
- `n8n_setup/SETUP_GUIDE.md` - Documentación completa
