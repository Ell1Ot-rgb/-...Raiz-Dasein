# 🔧 INSTRUCCIONES PARA CONFIGURAR NEO4J

## 📋 Problema Detectado

La base de datos **`yo_estructural`** no existe en tu servidor Neo4j.

---

## ✅ SOLUCIÓN 1: Crear la BD automáticamente (Recomendado)

### Paso 1: Ejecutar el script de creación

```bash
py crear_bd_neo4j.py
```

Este script:
- Se conecta a Neo4j usando las credenciales de `config.yaml`
- Verifica si la base de datos existe
- La crea automáticamente si no existe
- Verifica que se creó correctamente

### Paso 2: Optimizar la base de datos

Una vez creada la BD, ejecuta:

```bash
py optimizar_neo4j.py
```

Esto creará todos los índices y constraints necesarios para mejorar el rendimiento.

---

## ✅ SOLUCIÓN 2: Crear la BD manualmente

Si el script automático falla por permisos, créala manualmente:

### Opción A: Desde Neo4j Browser

1. Abre Neo4j Browser en: http://192.168.1.37:7474
2. Conéctate con:
   - Usuario: `neo4j`
   - Contraseña: `fenomenologia2024`
3. Ejecuta este comando:

```cypher
CREATE DATABASE yo_estructural IF NOT EXISTS
```

4. Verifica que se creó:

```cypher
SHOW DATABASES
```

### Opción B: Desde la línea de comandos (en el servidor Neo4j)

```bash
cypher-shell -u neo4j -p fenomenologia2024 -d system "CREATE DATABASE yo_estructural IF NOT EXISTS"
```

---

## 🔍 Verificación

Para verificar que la base de datos existe:

```cypher
SHOW DATABASES
```

Deberías ver `yo_estructural` en la lista con estado `online`.

---

## 📊 Después de crear la BD

1. **Ejecuta el optimizador**:
   ```bash
   py optimizar_neo4j.py
   ```

2. **Ejecuta el verificador**:
   ```bash
   py verificar.py
   ```

---

## ⚠️ Troubleshooting

### Error: "Permission denied" o "Insufficient privilege"

Tu usuario no tiene permisos de administrador. Opciones:

1. **Usar el usuario `neo4j`** (administrador por defecto)
   - Actualiza `config.yaml` con las credenciales correctas

2. **Otorgar permisos al usuario actual**:
   ```cypher
   GRANT CREATE DATABASE ON DBMS TO tu_usuario
   ```

### Error: "Connection refused"

Verifica que Neo4j esté corriendo en `192.168.1.37:7687`:

```bash
# Windows
netstat -an | findstr 7687

# Linux/Mac
netstat -tuln | grep 7687
```

### Error: "Authentication failed"

Verifica las credenciales en `configuracion/config.yaml`:
- Usuario: `neo4j`
- Contraseña: `fenomenologia2024`

---

## 📝 Configuración Actual

Según tu `config.yaml`:

```yaml
neo4j:
  host: 192.168.1.37
  port: 7687
  database: yo_estructural
  username: neo4j
  password: fenomenologia2024
```

---

## 🚀 Flujo Completo de Instalación

```bash
# 1. Crear la base de datos
py crear_bd_neo4j.py

# 2. Optimizar (crear índices y constraints)
py optimizar_neo4j.py

# 3. Verificar todo el sistema
py verificar.py
```

---

## 📞 Ayuda Adicional

Si sigues teniendo problemas:

1. Verifica que Neo4j esté corriendo
2. Verifica que puedas conectarte con Neo4j Browser
3. Verifica las credenciales en el archivo de configuración
4. Revisa los logs de Neo4j en el servidor

---

**Última actualización**: 30 de octubre de 2025
