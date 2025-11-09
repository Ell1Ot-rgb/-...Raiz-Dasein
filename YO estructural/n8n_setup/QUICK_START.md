# QUICK START: Copia y pega esto en PowerShell

## 🚀 Instalación (OPCIÓN A: Automática)

**Abre PowerShell como Administrador y copia esta línea completa:**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force; $dir = "C:\YO_ESTRUCTURAL"; if (-not (Test-Path $dir)) { mkdir $dir } else { cd $dir\`"YO estructural\`" }; .\n8n_setup\deploy-n8n-complete.ps1
```

**O paso a paso (más seguro):**

```powershell
# 1. Permitir scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 2. Ir a la carpeta
cd "C:\ruta\a\YO estructural"

# 3. Ejecutar
.\n8n_setup\deploy-n8n-complete.ps1
```

---

## ⚡ Iniciar n8n

Después de que termine la instalación:

```powershell
# Simple
n8n start

# O con .env explícito
n8n start --env-file $env:USERPROFILE\.n8n\.env
```

Luego abre: **http://localhost:5678**

---

## ✅ Verificar que funciona

```powershell
# Terminal 1: Ver si n8n está arriba
Invoke-RestMethod http://localhost:5678/healthz

# Terminal 2: Ver los workflows
n8n list:workflows

# Terminal 3: Ver logs
tail -f $env:USERPROFILE\.n8n\logs\*
```

---

## 🎯 Próximos 10 minutos

1. ✅ Ejecuta el script arriba (5 min)
2. ✅ `n8n start` (2 min)
3. ✅ Abre http://localhost:5678 (1 min)
4. ✅ Verifica que ves los 3 workflows en la UI (2 min)

---

## 📚 Documentación

- **README.md** → Inicio rápido
- **SETUP_GUIDE.md** → Guía completa
- **RESUMEN_EJECUTIVO.md** → Visión general

---

## 🆘 Si algo falla

```powershell
# Ver logs de error
Get-Content $env:USERPROFILE\.n8n\logs\* -Tail 50

# Validar instalación
.\n8n_setup\validate-installation.ps1

# Regenerar .env
.\n8n_setup\install-n8n-complete.ps1 -GenerateEnvOnly
```

---

¡Eso es todo! Comienza con: `.\n8n_setup\deploy-n8n-complete.ps1`
