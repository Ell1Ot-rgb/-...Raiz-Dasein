# 🚀 INICIO RÁPIDO - SISTEMA 4GB RAM

## ⚡ PASOS PARA EJECUTAR AHORA MISMO

### 📍 PASO 1: INICIAR SERVICIOS EN PC2 (192.168.1.37)

```bash
# 1. Conectar a PC2
ssh usuario@192.168.1.37

# 2. Ir al directorio del proyecto
cd ~/fenomenologia

# 3. Copiar archivos de configuración desde PC1
# (Ejecutar esto en PC1)
scp "/workspaces/-...Raiz-Dasein/YO estructural/docker-compose-PC2.yml" usuario@192.168.1.37:~/fenomenologia/docker-compose.yml
scp "/workspaces/-...Raiz-Dasein/YO estructural/Dockerfile.lightrag" usuario@192.168.1.37:~/fenomenologia/

# 4. De vuelta en PC2, iniciar servicios
docker-compose up -d

# 5. Verificar que estén corriendo
docker-compose ps

# Deberías ver:
# neo4j_fenomenologia         running   0.0.0.0:7474->7474/tcp, 0.0.0.0:7687->7687/tcp
# lightrag_semantic_refinement running   0.0.0.0:8000->8000/tcp

# 6. Ver logs en tiempo real
docker-compose logs -f
```

**✅ Verificación:**
- Neo4j HTTP: http://192.168.1.37:7474 (navegador)
- Neo4j Bolt: bolt://192.168.1.37:7687
- LightRAG: http://192.168.1.37:8000/health

---

### 📍 PASO 2: INSTALAR DEPENDENCIAS EN PC1 (192.168.1.35)

```bash
# 1. Ir al directorio del proyecto
cd "/workspaces/-...Raiz-Dasein/YO estructural"

# 2. Verificar RAM disponible
free -h
# Deberías tener al menos 1GB disponible
# Si tienes menos, cierra aplicaciones

# 3. Ejecutar instalación automática
chmod +x instalar_4gb_optimizado.sh
./instalar_4gb_optimizado.sh

# Esto tomará 5-10 minutos
# Descarga ~100MB de modelos
```

**✅ Verificación:**
Al final del script verás:
```
╔════════════════════════════════════════════════════════════╗
║             ✓ INSTALACIÓN COMPLETADA (4GB RAM)            ║
╚════════════════════════════════════════════════════════════╝
```

---

### 📍 PASO 3: PROBAR CONECTIVIDAD

```bash
# 1. Activar entorno virtual
source venv_4gb/bin/activate

# 2. Test Neo4j
python3 << 'EOF'
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://192.168.1.37:7687",
    auth=("neo4j", "fenomenologia2024")
)

try:
    driver.verify_connectivity()
    print("✅ Conexión a Neo4j: OK")
    
    with driver.session() as session:
        result = session.run("RETURN 'Conexión exitosa' AS msg")
        print(f"✅ Query test: {result.single()['msg']}")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    driver.close()
EOF

# 3. Test LightRAG
curl http://192.168.1.37:8000/health

# 4. Test ping
ping -c 3 192.168.1.37
```

**✅ Verificación:**
Deberías ver:
```
✅ Conexión a Neo4j: OK
✅ Query test: Conexión exitosa
{"status": "ok"}
```

---

### 📍 PASO 4: EJECUTAR ANÁLISIS DE PRUEBA

```bash
# Ejecutar analizador de convergencia
python3 procesadores/analizador_convergencia_optimizado.py
```

**✅ Salida esperada:**
```
=== Analizador de Convergencia Fenomenológica (Optimizado para 4GB RAM) ===
Cargando analizador para 4GB RAM...
RAM disponible: ~1.2GB de 4GB total
Configuración cargada desde: config_4gb_optimizado.yaml

Procesando 10 conceptos de prueba...
Batch 1/10: [====================] 100%
Batch 2/10: [====================] 100%
...
✓ Convergencia detectada en concepto: "fenomenología"
  - Certeza definitoria: 99.2%
  - Rutas convergentes: 5/5
  - Tiempo: 2.3s
```

---

### 📍 PASO 5: MONITOREAR RECURSOS

Abre **3 terminales** en PC1:

**Terminal 1: Sistema principal**
```bash
source venv_4gb/bin/activate
python3 procesadores/analizador_convergencia_optimizado.py
```

**Terminal 2: Monitor de RAM**
```bash
watch -n 2 'free -h'
```

**Terminal 3: Procesos Python**
```bash
watch -n 2 'ps aux | grep python | grep -v grep'
```

**✅ Verificación:**
En Terminal 2 deberías ver:
```
              total        used        free      shared  buff/cache   available
Mem:           4.0G        2.5G        800M        100M        700M        1.2G
```

---

## 🎯 INTEGRACIÓN CON SISTEMA PRINCIPAL

Una vez que todo funcione, integra en `sistema_principal_v2.py`:

```python
# ============================================================
# AGREGAR AL INICIO DEL ARCHIVO
# ============================================================
import sys
sys.path.append('./procesadores')

from analizador_convergencia_optimizado import AnalizadorConvergenciaOptimizado
import psutil
import resource

# ============================================================
# CONFIGURAR LÍMITE DE MEMORIA
# ============================================================
def configurar_limites():
    """Limita proceso a 1GB (de 4GB total)"""
    try:
        soft = 1024 * 1024 * 1024  # 1GB
        hard = int(1.2 * 1024 * 1024 * 1024)  # 1.2GB
        resource.setrlimit(resource.RLIMIT_AS, (soft, hard))
        print("✓ Límite de memoria: 1GB")
    except:
        print("⚠ No se pudo limitar memoria")

configurar_limites()

# ============================================================
# INICIALIZAR ANALIZADOR
# ============================================================
analizador_convergencia = AnalizadorConvergenciaOptimizado(
    config_path="./config_4gb_optimizado.yaml"
)

# ============================================================
# USAR EN CICLO PRINCIPAL
# ============================================================
def procesar_texto_fenomenologico(texto):
    """Analiza texto y detecta máximo relacional"""
    
    # ... tu código existente de procesamiento ...
    
    # DETECTAR CONVERGENCIA
    resultado = analizador_convergencia.analizar_convergencia(
        conceptos=conceptos_extraidos,
        rutas=rutas_fenomenologicas,
        batch_size=10  # MAX 10 en 4GB
    )
    
    if resultado['convergencia_detectada']:
        print(f"✅ MÁXIMO RELACIONAL: {resultado['concepto_central']}")
        print(f"   Certeza: {resultado['certeza_definicion']:.1f}%")
        
        # Guardar en Neo4j remoto
        analizador_convergencia.guardar_resultado_neo4j(resultado)
    
    return resultado

# ============================================================
# EJEMPLO DE USO
# ============================================================
if __name__ == "__main__":
    texto = """
    El concepto de fenomenología converge a través de múltiples rutas:
    física, ergonómica, arquitectónica, lógica y ontológica...
    """
    
    resultado = procesar_texto_fenomenologico(texto)
```

---

## 🔍 VERIFICAR QUE TODO FUNCIONA

### Checklist completo:

```bash
# 1. PC2 corriendo servicios
ssh usuario@192.168.1.37 "docker-compose ps"
# ✅ Debe mostrar neo4j y lightrag como "running"

# 2. PC1 puede conectar a Neo4j
python3 -c "from neo4j import GraphDatabase; GraphDatabase.driver('bolt://192.168.1.37:7687', auth=('neo4j', 'fenomenologia2024')).verify_connectivity(); print('OK')"
# ✅ Debe imprimir "OK"

# 3. PC1 puede conectar a LightRAG
curl -s http://192.168.1.37:8000/health | grep -q "ok" && echo "OK" || echo "FAIL"
# ✅ Debe imprimir "OK"

# 4. Configuración cargada correctamente
python3 -c "import yaml; c=yaml.safe_load(open('config_4gb_optimizado.yaml')); print(f\"Batch: {c['clustering']['batch_size']}, RAM: {c['optimization']['max_memory_mb']}MB\")"
# ✅ Debe imprimir "Batch: 100, RAM: 1024MB"

# 5. RAM disponible suficiente
free -m | awk 'NR==2{if($7>1000) print "OK"; else print "WARN: Solo", $7, "MB disponibles"}'
# ✅ Debe imprimir "OK" o advertencia si hay poca RAM
```

---

## 🚨 TROUBLESHOOTING RÁPIDO

### Problema 1: "Cannot connect to Neo4j"

**Solución:**
```bash
# En PC2, verificar que esté corriendo
docker ps | grep neo4j

# Si no está corriendo
docker-compose up -d neo4j

# Verificar logs
docker logs neo4j_fenomenologia
```

### Problema 2: "Out of Memory"

**Solución:**
```bash
# Cerrar aplicaciones en PC1
# Reducir batch size en config_4gb_optimizado.yaml

# Cambiar de:
clustering:
  batch_size: 100

# A:
clustering:
  batch_size: 50  # Mitad del tamaño
```

### Problema 3: "Module not found"

**Solución:**
```bash
# Reactivar entorno
source venv_4gb/bin/activate

# Reinstalar dependencia faltante
pip install --no-cache-dir <paquete>
```

### Problema 4: LightRAG no responde

**Solución:**
```bash
# En PC2, reiniciar servicio
docker-compose restart lightrag

# Ver logs
docker logs -f lightrag_semantic_refinement
```

---

## 📊 MÉTRICAS NORMALES

### Uso de RAM en PC1 durante ejecución:

```
Inicialización:
├─ Python base: 50MB
├─ spaCy model: 15MB
├─ Embeddings model: 60MB
└─ TOTAL: ~125MB

Durante procesamiento (batch 10):
├─ Base: 125MB
├─ Embeddings cache: 80MB
├─ NetworkX graph: 50MB
├─ Procesamiento: 50MB
└─ TOTAL: ~305MB

Pico máximo (convergencia completa):
├─ Base + cache: 205MB
├─ Clusters activos: 200MB
├─ Resultados: 100MB
├─ Buffer: 295MB
└─ TOTAL: ~800MB (80% de límite 1GB)
```

### Tiempos normales:

- Inicialización: 10-15s
- Batch 10 conceptos: 2-3s
- Convergencia 100 conceptos: 30-60s
- Guardado Neo4j: 1-2s

---

## ✅ ARCHIVOS CLAVE

```
/workspaces/-...Raiz-Dasein/YO estructural/
├── config_4gb_optimizado.yaml          ← Configuración principal
├── instalar_4gb_optimizado.sh          ← Script de instalación
├── docker-compose-PC2.yml              ← Para PC2 (servidor)
├── GUIA_DESPLIEGUE_4GB_COMPLETA.md     ← Guía detallada
├── RESUMEN_IMPLEMENTACION_4GB.md       ← Resumen técnico
├── INICIO_RAPIDO_4GB.md                ← Este archivo
└── procesadores/
    └── analizador_convergencia_optimizado.py  ← Analizador principal
```

---

## 🎯 COMANDOS MÁS USADOS

```bash
# Activar entorno
source venv_4gb/bin/activate

# Ejecutar análisis
python3 procesadores/analizador_convergencia_optimizado.py

# Ver RAM
free -h

# Monitor continuo
watch -n 2 'free -h && echo "---" && ps aux | grep python | head -3'

# Test Neo4j
python3 -c "from neo4j import GraphDatabase; GraphDatabase.driver('bolt://192.168.1.37:7687', auth=('neo4j', 'fenomenologia2024')).verify_connectivity(); print('OK')"

# Estado servicios PC2
ssh usuario@192.168.1.37 "docker-compose ps"
```

---

**SISTEMA LISTO PARA USAR** ✅  
**Configurado para:** 4GB RAM DDR3 @ 1334MHz  
**Red:** PC1 (192.168.1.35) ↔ PC2 (192.168.1.37)  
**Credenciales:** neo4j / fenomenologia2024
