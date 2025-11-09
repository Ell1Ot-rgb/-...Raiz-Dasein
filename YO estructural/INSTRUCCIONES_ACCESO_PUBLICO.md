# 🌐 Cómo Hacer Públicos los Puertos en GitHub Codespaces

## ⚠️ PROBLEMA
Los puertos están configurados como **privados** por defecto, por lo que las URLs no son accesibles públicamente.

## ✅ SOLUCIÓN (Método Visual)

### Opción 1: Desde VS Code (MÁS FÁCIL)

1. **Abre el panel de PUERTOS**:
   - Presiona `Ctrl+` ` (backtick) para abrir el terminal
   - Haz clic en la pestaña **"PORTS"** (al lado de "TERMINAL")

2. **Cambia la visibilidad de los puertos**:
   
   Para cada puerto que necesites hacer público:
   
   | Puerto | Servicio | Acción |
   |--------|----------|--------|
   | **5678** | n8n | Clic derecho → **Port Visibility** → **Public** |
   | **7474** | Neo4j Browser | Clic derecho → **Port Visibility** → **Public** |
   | **7687** | Neo4j Bolt | Clic derecho → **Port Visibility** → **Public** |
   | **8000** | API | Clic derecho → **Port Visibility** → **Public** |

3. **Verifica las URLs públicas**:
   Después de hacerlos públicos, las URLs estarán disponibles en la columna "Forwarded Address"

### Opción 2: Desde devcontainer.json (Permanente)

Edita el archivo `.devcontainer/devcontainer.json` y agrega:

```json
{
  "forwardPorts": [5678, 7474, 7687, 8000],
  "portsAttributes": {
    "5678": {
      "label": "n8n",
      "onAutoForward": "notify",
      "visibility": "public"
    },
    "7474": {
      "label": "Neo4j Browser",
      "onAutoForward": "notify",
      "visibility": "public"
    },
    "7687": {
      "label": "Neo4j Bolt",
      "onAutoForward": "notify",
      "visibility": "public"
    },
    "8000": {
      "label": "API",
      "onAutoForward": "notify",
      "visibility": "public"
    }
  }
}
```

Luego reconstruye el contenedor: `Ctrl+Shift+P` → "Rebuild Container"

### Opción 3: Desde GitHub CLI (Automático)

Si tienes `gh` instalado y autenticado:

```bash
gh codespace ports visibility 5678:public -c $CODESPACE_NAME
gh codespace ports visibility 7474:public -c $CODESPACE_NAME
gh codespace ports visibility 7687:public -c $CODESPACE_NAME
gh codespace ports visibility 8000:public -c $CODESPACE_NAME
```

## 📋 URLs Públicas Esperadas

Una vez configurados como públicos, las URLs serán:

```
n8n:         https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev
Neo4j UI:    https://sinister-wand-5vqjp756r4xcvpvw-7474.app.github.dev
Neo4j Bolt:  https://sinister-wand-5vqjp756r4vcvpvw-7687.app.github.dev
API:         https://sinister-wand-5vqjp756r4xcvpvw-8000.app.github.dev
```

## 🔐 Workflow URL

Después de hacer público el puerto 5678:

```
https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/workflow/bRzrHvbsZ8H5fxcQ
```

## 🧪 Webhook URL (para probar)

```bash
curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/generar-maximo \
  -H 'Content-Type: application/json' \
  -d '{"concepto": "SOPORTE"}'
```

## ⚡ Inicio Rápido

**SI ESTÁS VIENDO ESTO, HAZ ESTO AHORA:**

1. Ve al panel **PORTS** en la parte inferior de VS Code
2. Encuentra el puerto **5678** (n8n)
3. Clic derecho → **Port Visibility** → **Public**
4. ✅ ¡Listo! Ya puedes acceder a la URL

---

**Nota**: Los puertos privados solo son accesibles cuando estás autenticado en GitHub. Los puertos públicos son accesibles sin autenticación (útil para webhooks externos).
