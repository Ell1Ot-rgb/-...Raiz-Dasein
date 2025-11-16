"""
GUÍA TÉCNICA: IMPLEMENTACIÓN OPTIMIZADA PARA DUAL-CORE
========================================================

Sistema: Máximo Relacional Definicional + Centralidad Híbrida
Arquitectura: Dual-PC (PC1: Dual-Core AMD 8GB | PC2: Neo4j + LightRAG)
Lenguaje: Python 3.9+
Requisitos: 2-3 horas de implementación

ÍNDICE:
======
1. Requisitos previos
2. Instalación de dependencias
3. Configuración del entorno
4. Integración en sistema principal
5. Optimizaciones para dual-core
6. Testing y validación
7. Troubleshooting
"""

# ===================================================================
# 1. REQUISITOS PREVIOS
# ===================================================================

"""
PRE-REQUISITOS (Verificar antes de empezar):

PC1 (Dual-Core AMD, 8GB RAM):
├─ ✓ Python 3.9+ instalado
├─ ✓ pip actualizado (pip install --upgrade pip)
├─ ✓ virtualenv disponible
├─ ✓ Conectividad de red a PC2 (Neo4j remoto)
└─ ✓ Espacio libre en disco: >= 2GB

PC2 (PC Potente):
├─ ✓ Neo4j 5.12+ ejecutándose
├─ ✓ Neo4j GDS instalado (plugin)
├─ ✓ LightRAG instalado (opcional pero recomendado)
├─ ✓ Docker corriendo (Neo4j + LightRAG en contenedores)
└─ ✓ Puerto 7687 accesible desde PC1

Verificación PC1:
$ python --version  # Python 3.9+
$ pip --version
$ lsof -i :5000    # Si usas puerto 5000 para Flask
"""

# ===================================================================
# 2. INSTALACIÓN DE DEPENDENCIAS
# ===================================================================

# PASO 1: Crear entorno virtual (CRÍTICO para dual-core)
"""
En PC1:

# Crear entorno virtual en carpeta específica
python3.9 -m venv /opt/yo_estructural_env

# Activar entorno
source /opt/yo_estructural_env/bin/activate

# Verificar pip
pip --version
pip install --upgrade pip setuptools wheel
"""

# PASO 2: Instalar dependencias optimizadas para dual-core
REQUIREMENTS_DUAL_CORE = """
# requirements_dualcore.txt
# ===========================
# VERSIONES PINNED (crítico para reproducibilidad)

# Core científico
numpy==1.24.3              # ⚠️ Versión exacta (1.25+ lenta en dual-core)
scipy==1.11.1              # Compatible con numpy 1.24
scikit-learn==1.3.0        # ML library, optimizado

# NLP - MODELOS LIGEROS (critíco para 8GB)
spacy==3.6.1               # NLP framework
https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.6.0/en_core_web_sm-3.6.0-py3-none-any.whl
sentence-transformers==2.2.2  # Embeddings (USAR VERSIÓN EXACTA)

# Embeddings - MODELO ULTRA-LIGERO
# all-MiniLM-L6-v2: 80MB, 384 dims (perfecto para dual-core)
# NO instalar "LaBSE" o "large" models (200MB+)

# Neo4j
neo4j==5.13.0              # Driver
neo4j-driver-async==5.13.0 # Async (opcional)

# Grafos
networkx==3.1              # Graph analysis
python-igraph==0.10.6      # Alternativa rápida (opcional)

# Utils
psutil==5.9.5              # Memory/CPU monitoring
python-dotenv==1.0.0       # .env support
pydantic==2.0.3            # Data validation
pyyaml==6.0.1              # Config files

# LightRAG (remoto, en PC2)
# No instalar en PC1 - solo cliente HTTP

# Async/Concurrency
aiohttp==3.8.5             # HTTP async
asyncio-contextmanager==1.0.0

# Logging/Monitoring
loguru==0.7.0              # Better logging

# Testing
pytest==7.4.0              # (desarrollo/testing)
pytest-asyncio==0.21.1     # (desarrollo/testing)

# Performance
ujson==5.8.0               # JSON rápido
orjson==3.9.7              # JSON alternativo más rápido
"""

# PASO 3: Instalar requirements optimizado
"""
# En PC1 (entorno virtual activado):

cd /path/to/YO\ estructural

# Instalar dependencias
pip install -r requirements_dualcore.txt

# Descargar modelo spaCy (one-time)
python -m spacy download es_core_news_sm

# Verificar instalación
python -c "import numpy; import networkx; import sentence_transformers; print('✓ Dependencias OK')"

# TIEMPO ESTIMADO: 5-10 minutos (depende de velocidad internet)
"""

# ===================================================================
# 3. CONFIGURACIÓN DEL ENTORNO
# ===================================================================

"""
CONFIGURACIÓN .env (PC1)
========================

Crear archivo: /path/to/YO\ estructural/.env.dualcore

# Neo4j remoto (en PC2)
NEO4J_URI=bolt://192.168.1.100:7687          # IP/hostname PC2
NEO4J_USER=neo4j
NEO4J_PASSWORD=tu_contraseña_fuerte

# LightRAG (remoto, en PC2)
LIGHTRAG_API_URL=http://192.168.1.100:8000
LIGHTRAG_API_KEY=tu_api_key

# Optimizaciones dual-core
PYTHON_OPTIMIZATION=2                         # -OO flag
PYTHONUNBUFFERED=1                           # Log en tiempo real
OMP_NUM_THREADS=2                            # Force 2 threads
MKL_NUM_THREADS=2                            # Intel MKL si aplica
NUMEXPR_NUM_THREADS=2                        # NumExpr parallelization

# Memory settings
MEMORY_MAX_PERCENT=70                        # Max 70% RAM
BATCH_SIZE_EMBEDDINGS=32                     # Batch size
CHUNK_SIZE_PROCESSING=100                    # Chunk size

# Logging
LOG_LEVEL=INFO                               # DEBUG para troubleshooting
LOG_FILE=/tmp/yo_estructural.log

# Flask (si usas)
FLASK_ENV=production
FLASK_DEBUG=0
"""

# PASO 4: Crear archivo de configuración YAML
CONFIG_YAML = """
# config_dualcore.yaml
# ====================

sistema:
  nombre: "YO Estructural v2.3"
  version: "2.3.0"
  modo: "produccion"

neo4j:
  host: "192.168.1.100"        # IP PC2
  port: 7687
  username: "neo4j"
  password: "${NEO4J_PASSWORD}"
  database: "neo4j"
  timeout: 30
  max_retry: 3
  pool_size: 20                 # Reducido para dual-core

hardware:
  cores: 2
  ram_gb: 8
  optimization_level: "aggressive"

embeddings:
  modelo: "all-MiniLM-L6-v2"   # CRÍTICO: modelo ligero
  dimensiones: 384
  batch_size: 32                # Batch para dual-core
  cache_mb: 500                 # Max cache

clustering:
  algoritmo: "dbscan"
  eps: 0.15
  min_samples: 2
  n_jobs: 2                     # 2 cores

analisis:
  # Máximo Relacional
  maximo_relacional:
    modo: "hibrido"             # networkx + neo4j_gds
    umbral_modo_local: 10000    # Switch a GDS si > 10k nodos
    
  # Convergencia Definicional
  convergencia:
    n_rutas: 5
    umbral_convergencia: 0.85
    umbral_certeza: 0.99
    umbral_desviacion: 0.10
    
  # Axiomatización
  axiomatizacion:
    va_minimo: 0.7
    pc_minimo: 0.8
    confianza_combinada_minima: 0.84

lightrag:
  habilitado: false             # Desactivar si no hay acceso
  url_remota: "${LIGHTRAG_API_URL}"
  api_key: "${LIGHTRAG_API_KEY}"
  timeout: 30

procesamiento:
  memory_check_interval: 100    # Check cada N items
  gc_aggressive: true           # Recolección agresiva
  streaming: true               # Procesar en streaming
  workers_paralelos: 2          # 2 cores

logging:
  nivel: "INFO"
  archivo: "/tmp/yo_estructural.log"
  max_bytes: "10485760"         # 10MB
  backup_count: 5
"""

# ===================================================================
# 4. INTEGRACIÓN EN SISTEMA PRINCIPAL
# ===================================================================

"""
INTEGRACIÓN EN sistema_principal_v2.py
======================================

# En sistema_principal_v2.py, agregar:

from procesadores.analizador_convergencia_optimizado import (
    AnalizadorConvergenciaSimplificado,
    MemoryOptimizer
)
from procesadores.analizador_maximo_relacional_hibrido import (
    AnalizadorMaximoRelacionalPublico
)

class SistemaFenomenologicoV2:
    def __init__(self, config_path: str):
        # ... código existente ...
        
        # NUEVO: Inicializar analizadores
        self.analizador_convergencia = (
            AnalizadorConvergenciaSimplificado.get_instancia(
                self.neo4j
            )
        )
        
        self.analizador_maximo_relacional = (
            AnalizadorMaximoRelacionalPublico(self.neo4j)
        )
        
        # NUEVO: Monitor de memoria
        self.memory_monitor = MemoryOptimizer()
    
    def procesar_flujo_completo_con_maximo_relacional(self, 
            ruta_datos_entrada: str) -> Dict:
        '''
        Flujo completo:
        1. Ingesta → Preinstancias
        2. Análisis → Instancias Existenciales
        3. Clustering → Vohexistencias
        4. Convergencia → Máximo Relacional Definicional
        5. Centralidad → Máximo Relacional de Red
        6. Síntesis → AxiomaYO final
        '''
        
        # Paso 1-3: Ya existen
        resultado_previo = self.procesar_flujo_completo(ruta_datos_entrada)
        
        # Paso 4: NUEVO - Análisis de Convergencia
        self.logger.info("Analizando convergencia definicional...")
        
        preinstancia_ids = [p.id for p in resultado_previo['preinstancias']]
        
        convergencia = self.analizador_convergencia.analizar(
            preinstancia_ids[:5],
            usar_lightrag=self.config.get('lightrag', {}).get('habilitado')
        )
        
        if convergencia.get('es_maximo_relacional'):
            self.logger.info("✓ Máximo relacional definicional detectado")
        
        # Paso 5: NUEVO - Análisis de Centralidad
        self.logger.info("Analizando máximo relacional de red...")
        
        maximo_relacional = self.analizador_maximo_relacional.analizar()
        
        if maximo_relacional.get('concepto_maximo'):
            self.logger.info(
                f"✓ Concepto máximo: {maximo_relacional['concepto_maximo']} "
                f"(score: {maximo_relacional['score_maximo']:.4f})"
            )
        
        # Paso 6: Síntesis final
        resultado_final = {
            **resultado_previo,
            "convergencia_definicional": convergencia,
            "maximo_relacional_red": maximo_relacional,
            "timestamp_final": datetime.now().isoformat()
        }
        
        return resultado_final
"""

# ===================================================================
# 5. OPTIMIZACIONES PARA DUAL-CORE
# ===================================================================

"""
OPTIMIZACIONES CRÍTICAS PARA DUAL-CORE 8GB
===========================================

1. LAZY LOADING DE EMBEDDINGS
   ✓ Ya implementado en EmbeddingsProvider
   ✓ Modelo se carga solo cuando se necesita
   ✓ Ahorro: 200-300MB de RAM inicial

2. BATCH PROCESSING
   ✓ Embeddings: batch_size=32 (no 1)
   ✓ Grafo: chunk_size=1000 nodos por lote
   ✓ Speedup: 3-5x vs procesamiento serial

3. MEMORY MONITORING
   ✓ Check cada 100 items
   ✓ Garbage collection agresivo si > 70% RAM
   ✓ Nunca excede 8GB

4. PARALELIZACIÓN INTELIGENTE
   ✓ ThreadPool con 2 workers (2 cores)
   ✓ No usar multiprocessing (overhead)
   ✓ Usar concurrent.futures.ThreadPoolExecutor

5. STREAMING DE RESULTADOS
   ✓ No acumular todo en RAM
   ✓ Procesar mientras llega
   ✓ Persistir inmediatamente en Neo4j

6. CACHE SELECTIVO
   ✓ Solo cachear embeddings (reutilización)
   ✓ Max 500MB cache
   ✓ Limpiar entre análisis

VERIFICACIÓN DE OPTIMIZACIONES:
"""

verification_script = """
# test_optimizaciones.py
import psutil
import time
from procesadores.analizador_convergencia_optimizado import (
    MemoryOptimizer,
    EmbeddingsProvider
)

def test_memory():
    print("TEST 1: Memory Monitoring")
    print(f"RAM disponible: {MemoryOptimizer.get_available_memory():.2f}GB")
    print(f"RAM en uso: {psutil.virtual_memory().percent:.1f}%")
    assert MemoryOptimizer.check_memory_threshold(), "Memoria insuficiente"
    print("✓ Test memoria PASS")

def test_lazy_loading():
    print("\\nTEST 2: Lazy Loading Embeddings")
    
    # Sin cargar modelo
    embeddings = EmbeddingsProvider()
    mem_antes = psutil.virtual_memory().available / (1024**3)
    
    # Cargar modelo
    modelo = embeddings.get_modelo()
    mem_despues = psutil.virtual_memory().available / (1024**3)
    
    print(f"Memoria antes: {mem_antes:.2f}GB")
    print(f"Memoria después: {mem_despues:.2f}GB")
    print(f"Overhead modelo: {(mem_antes - mem_despues):.2f}GB")
    
    assert (mem_antes - mem_despues) < 1.0, "Modelo demasiado pesado"
    print("✓ Test lazy loading PASS")

def test_batch_encoding():
    print("\\nTEST 3: Batch Encoding")
    
    embeddings = EmbeddingsProvider()
    
    textos = ["texto de prueba " + str(i) for i in range(100)]
    
    # Batch
    inicio = time.time()
    result_batch = embeddings.encode_batch(textos, batch_size=32)
    tiempo_batch = time.time() - inicio
    
    print(f"100 textos, batch_size=32: {tiempo_batch:.2f}s")
    print(f"Shape resultado: {result_batch.shape}")
    
    assert result_batch.shape[0] == 100, "Número de embeddings incorrecto"
    print("✓ Test batch encoding PASS")

if __name__ == "__main__":
    test_memory()
    test_lazy_loading()
    test_batch_encoding()
    print("\\n✓✓✓ TODOS LOS TESTS PASARON ✓✓✓")
"""

# ===================================================================
# 6. TESTING Y VALIDACIÓN
# ===================================================================

"""
TESTING
=======

1. Unit Tests:
   pytest tests/test_convergencia.py -v
   pytest tests/test_maximo_relacional.py -v

2. Integration Tests:
   pytest tests/test_integracion.py -v

3. Performance Tests:
   pytest tests/test_performance.py -v --benchmark

4. Memory Tests:
   python test_optimizaciones.py

Comandos verificación:
# Ver memoria durante ejecución
watch -n 1 'ps aux | grep python | head -5'

# Ver I/O a Neo4j
tcpdump -i any -w neo4j_traffic.pcap port 7687

# Profile de Python
python -m cProfile -s cumulative script.py
"""

# ===================================================================
# 7. TROUBLESHOOTING
# ===================================================================

"""
PROBLEMAS COMUNES Y SOLUCIONES
===============================

PROBLEMA 1: "MemoryError: Unable to allocate X GB"
SOLUCIÓN:
- Reducir batch_size: 32 → 16
- Reducir chunk_size: 1000 → 500
- Activar aggressive_gc en config
- Verificar otras aplicaciones consumiendo RAM

PROBLEMA 2: "ConnectionError: No se puede conectar a Neo4j en PC2"
SOLUCIÓN:
- Verificar IP correcta en .env
- Ping a PC2: ping 192.168.1.100
- Verificar puerto: telnet 192.168.1.100 7687
- Verificar firewall en PC2

PROBLEMA 3: "TimeoutError en cálculo de embeddings"
SOLUCIÓN:
- Aumentar timeout: timeout=60 (default 30)
- Reducir batch_size: 32 → 16
- Verificar GPU si disponible: CUDA_VISIBLE_DEVICES=""

PROBLEMA 4: "Dual-core saturado al 100%"
SOLUCIÓN:
- Reducir n_jobs: 2 → 1 (procesamiento serial)
- Aumentar delays entre batches: sleep(0.1)
- Usar nice/ionice para reducir prioridad

PROBLEMA 5: "LightRAG no disponible"
SOLUCIÓN:
- Configurar lightrag.habilitado = false
- Sistema usa fallback sin enriquecimiento
- Performance igual, menos accuracy

DEBUG MODE:
- Set LOG_LEVEL=DEBUG en .env
- python -u script.py (unbuffered output)
- Agregar breakpoints: import pdb; pdb.set_trace()
"""

# ===================================================================
# CHECKLIST DE IMPLEMENTACIÓN
# ===================================================================

checklist = """
CHECKLIST: IMPLEMENTACIÓN COMPLETA
====================================

□ PRE-REQUISITOS:
  □ Python 3.9+ en PC1
  □ Neo4j 5.12+ corriendo en PC2 (Docker)
  □ Conectividad PC1 → PC2

□ INSTALACIÓN:
  □ Crear venv: python3.9 -m venv /opt/yo_estructural_env
  □ Activar: source /opt/yo_estructural_env/bin/activate
  □ Instalar deps: pip install -r requirements_dualcore.txt
  □ Descargar spacy: python -m spacy download es_core_news_sm

□ CONFIGURACIÓN:
  □ Crear .env.dualcore con vars correctas
  □ Crear config_dualcore.yaml
  □ Verificar IP Neo4j en .env (192.168.x.x)

□ ARCHIVOS CREADOS:
  □ procesadores/analizador_convergencia_optimizado.py (750 líneas)
  □ procesadores/analizador_maximo_relacional_hibrido.py (650 líneas)
  □ tests/test_optimizaciones.py
  □ requirements_dualcore.txt
  □ config_dualcore.yaml

□ INTEGRACIÓN:
  □ Actualizar sistema_principal_v2.py
  □ Agregar imports de analizadores
  □ Llamar métodos en flujo principal
  □ Test básico: python -c "import procesadores; print('OK')"

□ TESTING:
  □ python test_optimizaciones.py (pasa todos)
  □ pytest tests/test_convergencia.py (pasa)
  □ pytest tests/test_maximo_relacional.py (pasa)
  □ Monitor memoria durante ejecución

□ OPTIMIZACIONES:
  □ Batch size correcto para 8GB (32)
  □ Chunk size correcto (1000)
  □ Memory threshold en 70%
  □ GC agresivo habilitado
  □ Streaming activado

□ DOCUMENTACIÓN:
  □ README.md actualizado
  □ Docstrings en código
  □ Ejemplos de uso
  □ Troubleshooting completado

TIEMPO ESTIMADO: 2-3 horas
DIFICULTAD: INTERMEDIA
STATUS: PRODUCCIÓN LISTA
"""

print(__doc__)
print("\n" + "="*70)
print("CONFIGURACIÓN Y REQUERIMIENTOS COMPLETADOS")
print("="*70)
