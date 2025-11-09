# 🧠 N8N + YO ESTRUCTURAL v3.0

## Instalación Rápida (Copiar y Pegar)

### En PowerShell como Administrador:

```powershell
# Paso 1: Permitir ejecución de scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Paso 2: Navegar a la carpeta del proyecto
cd "C:\ruta\a\YO estructural"

# Paso 3: Ejecutar instalación automática
.\n8n_setup\install-n8n-complete.ps1
```

**Eso es todo.** El script se encarga de:
- ✅ Descargar e instalar Node.js 18 LTS
- ✅ Instalar n8n globalmente
- ✅ Crear archivo `.env` seguro con tus credenciales
- ✅ Importar 3 workflows optimizados
- ✅ Validar conectividad (Neo4j, webhooks)
- ✅ (Opcional) Crear servicio Windows para autoarranque

---

## Lo que necesitas saber

### **3 Workflows incluidos:**

| Workflow | Función | Entrada | Salida |
|----------|---------|---------|--------|
| **1. Monitor Archivos** | Vigila carpeta local, detecta tipos | Archivos en disco | Webhooks routeados |
| **2. Sync Neo4j** | Crea/actualiza nodos y relaciones | Webhook JSON | Nodos en Neo4j + logs |
| **3. Text Processing** | Analiza, extrae keywords, genera embeddings | Webhook texto | YAML enriquecido + Neo4j |

### **Dónde van los archivos:**

```
%USERPROFILE%\.n8n\
├── .env                      ← Credenciales (¡secreto!)
├── n8n.db                    ← Base de datos local (SQLite)
├── workflows/                ← Workflows ejecutándose
├── credentials.json          ← Credenciales cifradas
└── logs/                     ← Logs de ejecución
```

---

## Primeros pasos después de la instalación

### 1. **Iniciar n8n**
```powershell
n8n start --env-file $env:USERPROFILE\.n8n\.env
```

Luego abre: **http://localhost:5678**  
Usuario: `admin`  
Contraseña: (se muestra en la instalación)

### 2. **Ver workflows activos**
```powershell
n8n list:workflows
n8n list:executions
```

### 3. **Disparar un test manualmente**
```powershell
$body = @{
  contenido = "Texto de prueba"
  id = "test_001"
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:5678/webhook/process-text `
  -Method Post -Body $body -ContentType application/json
```

---

## Integración con tu código Python

```python
from integraciones.n8n_config import N8nIntegrator

n8n = N8nIntegrator()

# Enviar datos a procesar
resultado = n8n.enviar_datos_webhook(
    datos={"contenido": "Mi nota de Obsidian", "id": "nota_001"},
    origen="motor_yo"
)

if resultado['success']:
    print("✓ Procesamiento iniciado")
else:
    print(f"✗ Error: {resultado['error']}")
```

---

## Variables de entorno principales

```env
# Neo4j
NEO4J_HOST=192.168.1.37
NEO4J_PORT=7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=fenomenologia2024

# n8n
N8N_PORT=5678
N8N_ENCRYPTION_KEY=...
N8N_API_KEY=...

# Rutas locales
LOCAL_DATA_PATH=C:\yo_estructural\datos
OBSIDIAN_VAULT_PATH=C:\Users\usuario\Obsidian\vault
YAML_OUTPUT_PATH=C:\yo_estructural\datos\yaml_procesados
```

---

## Troubleshooting rápido

| Problema | Solución |
|----------|----------|
| `node` no se encuentra | Cierra PowerShell, abre nueva ventana |
| Puerto 5678 en uso | Cambia `N8N_PORT=5679` en `.env` |
| No conecta a Neo4j | `Test-NetConnection -ComputerName 192.168.1.37 -Port 7687` |
| Webhooks no funcionan | Verifica workflow esté ACTIVE (no pausado) |
| Credenciales corruptas | `rm $env:USERPROFILE\.n8n\n8n.db` y regenera |

---

## Documentación completa

Ver archivo: **`SETUP_GUIDE.md`** (guía detallada con diagramas y ejemplos)

---

## Comandos útiles

```powershell
# Iniciar n8n
n8n start

# Con túnel para webhooks públicos (sin firewall)
n8n start --tunnel

# Exportar workflows (backup)
n8n export:workflow --all --output backup_$(Get-Date -f yyyyMMdd).json

# Importar workflows
n8n import:workflow --input workflow.json

# Ver logs en tiempo real
tail -f $env:USERPROFILE\.n8n\logs\*

# Testear conectividad
Invoke-RestMethod http://localhost:5678/healthz
```

---

## Próximos pasos

1. ✅ Ejecutar el script de instalación
2. ✅ Iniciar n8n (`n8n start`)
3. ✅ Visitar http://localhost:5678
4. ✅ Verificar que los 3 workflows estén activos
5. ✅ Probar con un archivo en tu carpeta monitoreada
6. ✅ Integrar con tu código Python (`motor_yo/sistema_yo_emergente.py`)

---

## Soporte

**¿Problemas?** Revisa:
- Logs: `$env:USERPROFILE\.n8n\logs\`
- Guía completa: `SETUP_GUIDE.md`
- Código: `integraciones/n8n_config.py`

