# 🌐 Cómo Acceder a los Servicios en GitHub Codespaces

## ⚠️ IMPORTANTE: No Uses `localhost` Directamente

En GitHub Codespaces, **NO** puedes acceder a `http://localhost:5678` desde tu navegador local.

Codespaces corre en la nube, no en tu computadora. Necesitas usar las URLs generadas automáticamente por Codespaces.

---

## ✅ Método 1: Usar la Pestaña PORTS (Recomendado)

### Paso a Paso:

1. **Abre la pestaña PORTS** en VS Code:
   - Mira en la parte inferior de VS Code
   - Al lado de "TERMINAL" verás "PORTS"
   - Click en "PORTS"

2. **Verás una lista de puertos activos:**
   ```
   Puerto    | Servicio          | Acción
   ---------|-------------------|--------
   5678     | n8n               | 🌐 Click aquí
   7474     | Neo4j Browser     | 🌐 Click aquí
   7687     | Neo4j Bolt        | (solo para conexiones)
   8000     | API YO            | 🌐 Click aquí
   ```

3. **Para abrir n8n:**
   - Busca la fila con el puerto **5678**
   - Haz click en el **ícono de globo 🌐** en esa fila
   - O haz click derecho → **"Open in Browser"**

4. **Login en n8n:**
   ```
   Usuario: admin
   Password: fenomenologia2024
   ```

---

## ✅ Método 2: URLs Directas

Si la pestaña PORTS no funciona, las URLs siguen este patrón:

```
https://<CODESPACE_NAME>-<PUERTO>.app.github.dev
```

Por ejemplo, si tu Codespace se llama `fuzzy-space-adventure-xyz123`:

- **n8n:** `https://fuzzy-space-adventure-xyz123-5678.app.github.dev`
- **Neo4j:** `https://fuzzy-space-adventure-xyz123-7474.app.github.dev`
- **API:** `https://fuzzy-space-adventure-xyz123-8000.app.github.dev`

### Cómo obtener tu URL exacta:

Ejecuta en la terminal:
```bash
echo "n8n: https://${CODESPACE_NAME}-5678.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
echo "Neo4j: https://${CODESPACE_NAME}-7474.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
```

---

## ✅ Método 3: Simple Browser de VS Code

Dentro de VS Code, puedes abrir un navegador interno:

1. Presiona `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac)
2. Escribe: `Simple Browser: Show`
3. Ingresa la URL del puerto que quieres abrir

---

## 🔧 Verificar que los Servicios Estén Corriendo

```bash
# Ver contenedores activos:
docker ps

# Ver logs de n8n:
docker logs -f yo_estructural_n8n

# Verificar conectividad desde dentro del Codespace:
curl -I http://localhost:5678
```

---

## 🎯 Servicios Disponibles

### 1. **n8n** (Automatización de Workflows)
- **Puerto:** 5678
- **Usuario:** admin
- **Password:** fenomenologia2024
- **Qué hacer:**
  1. Login
  2. Importar workflow: `n8n_setup/workflows/workflow_5_generador_maximo_relacional.json`
  3. Configurar credenciales (Neo4j, Gemini)
  4. Activar workflow

### 2. **Neo4j Browser** (Base de Datos)
- **Puerto:** 7474
- **Connect URL:** `bolt://localhost:7687`
- **Usuario:** neo4j
- **Password:** fenomenologia2024
- **Qué hacer:**
  1. Login
  2. Ejecutar queries Cypher
  3. Visualizar nodos `MAXIMO_RELACIONAL`

### 3. **API YO Estructural** (REST API)
- **Puerto:** 8000
- **Documentación:** `/docs`
- **Endpoints:**
  - `POST /api/generador/rutas` - Generar máximo relacional
  - `GET /health` - Estado del sistema

---

## ❓ Troubleshooting

### Problema: "localhost refused to connect"

**Causa:** Estás intentando acceder desde tu navegador local, pero el servicio está en la nube.

**Solución:** Usa la pestaña PORTS de VS Code.

---

### Problema: "No veo la pestaña PORTS"

**Solución:**
1. Ve a: View → Command Palette (`Ctrl+Shift+P`)
2. Escribe: "Ports: Focus on Ports View"
3. O presiona: `Ctrl+Shift+P` → `View: Show Ports`

---

### Problema: "El puerto dice 'Private'"

**Solución:**
```bash
gh codespace ports visibility 5678:public -c $CODESPACE_NAME
gh codespace ports visibility 7474:public -c $CODESPACE_NAME
gh codespace ports visibility 8000:public -c $CODESPACE_NAME
```

---

### Problema: "La página carga pero da error 502/504"

**Causa:** El contenedor aún no terminó de iniciar.

**Solución:**
```bash
# Ver logs:
docker logs yo_estructural_n8n

# Esperar hasta ver: "Editor is now accessible via"
```

---

## 📊 Estado Actual de tus Servicios

```bash
# Verificar:
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

Deberías ver:
- `yo_estructural_n8n` - **Up** (healthy)
- `yo_estructural_neo4j` - **Up** (healthy)
- `yo_estructural_api` - **Up**

---

## 🔑 Credenciales Configuradas

```bash
# Gemini API Key (ya configurada en .env):
AIzaSyAtgpP05qWmGW6dUZnYBW96K3U-gLiV5Kc

# Neo4j:
Usuario: neo4j
Password: fenomenologia2024

# n8n:
Usuario: admin
Password: fenomenologia2024
```

---

## 🚀 Próximos Pasos

1. ✅ Servicios corriendo
2. ✅ Puertos públicos
3. ✅ Gemini API configurada
4. ⏳ **Acceder a n8n** (usa pestaña PORTS)
5. ⏳ Importar workflow
6. ⏳ Configurar credenciales en n8n
7. ⏳ Probar generación de máximo relacional

---

**¡Todo está listo! Solo necesitas abrir n8n desde la pestaña PORTS.** 🎉
