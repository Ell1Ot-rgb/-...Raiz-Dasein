# 📦 DISTRIBUCIÓN DE LIBRERÍAS - YO Estructural

## 📋 Resumen Ejecutivo

**Total de librerías:** 80+ paquetes Python + servicios externos

**Distribución:**
- **PC 1 (Dual-Core AMD):** 45 librerías (procesamiento ligero)
- **PC 2 (Potente):** 35+ librerías (Neo4j, FCA, análisis pesado)
- **Servicios Externos:** Google Cloud, Supabase, n8n

---

## 🖥️ PC 1: Dual-Core AMD (Procesadores Ligeros)

### ⚙️ Librerías de Configuración y Variables de Entorno
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `python-dotenv` | 1.0.0 | Cargar variables de entorno desde `.env` | 10 KB |
| `PyYAML` | 6.0.1 | Parsear archivos `.yaml` de configuración | 300 KB |
| `toml` | 0.10.2 | Parsear archivos `.toml` | 50 KB |

### 📝 Librerías de Procesamiento de Texto (NLP)
| Librería | Versión | Propósito | Tamaño | Instalación |
|:---|:---:|:---|:---:|:---|
| `spacy` | 3.7.2 | Análisis lingüístico, parsing, NER | 50 MB | `pip install spacy` + `python -m spacy download es_core_news_sm` |
| `nltk` | 3.8.1 | Tokenización, corpus, stopwords | 100 MB | `pip install nltk` |
| `transformers` | 4.36.0 | Modelos de Hugging Face (pero ligeramente pesado) | 200 MB | `pip install transformers` |
| `sentence-transformers` | (propuesto 2.2.2) | Embeddings semánticos ligeros (all-MiniLM-L6-v2) | 80 MB | `pip install sentence-transformers` |

### 🔢 Librerías de Computación Científica
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `numpy` | 1.26.4 | Arrays multidimensionales, operaciones numéricas | 15 MB |
| `scipy` | 1.11.4 | Funciones científicas avanzadas (clustering, estadística) | 30 MB |
| `pandas` | 2.1.4 | Manipulación y análisis de DataFrames | 50 MB |
| `scikit-learn` | 1.3.2 | ML: clustering (DBSCAN), clasificación, regresión | 20 MB |

### 🧠 Librería de Deep Learning (CUIDADO: Solo necesaria si usas modelos grandes)
| Librería | Versión | Propósito | Tamaño | Notas |
|:---|:---:|:---|:---:|:---|
| `torch` | 2.2.2 | Backend para transformers | **500 MB** | ⚠️ **Evitar en dual-core** - usar CPU + versión ligera |

**RECOMENDACIÓN PARA DUAL-CORE:** NO instalar `torch` en PC 1. Si necesitas embeddings, usa `sentence-transformers` que carga modelos optimizados sin torch.

### 📡 Librerías de Red e HTTP
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `requests` | 2.31.0 | HTTP requests síncronos (APIs REST) | 100 KB |
| `httpx` | 0.24.1 | HTTP cliente async/sync moderno | 200 KB |
| `aiohttp` | 3.9.1 | HTTP client/server asincrónico | 500 KB |
| `websockets` | 12.0 | WebSockets para comunicación real-time | 100 KB |

### 🔗 Base de Datos (Conectores)
| Librería | Versión | Propósito | Tamaño | Ubicación |
|:---|:---:|:---|:---:|:---|
| `neo4j` | 5.15.0 | Driver Python para Neo4j | 500 KB | **PC 1 (cliente remoto)** |
| `psycopg2-binary` | 2.9.9 | Conector PostgreSQL | 2 MB | Si integras Supabase |

### 📊 Visualización y Gráficos
| Librería | Versión | Propósito | Tamaño | Notas |
|:---|:---:|:---|:---:|:---|
| `matplotlib` | 3.8.2 | Gráficos 2D estáticos | 50 MB | Ligero para dual-core |
| `seaborn` | 0.13.0 | Gráficos estadísticos sobre matplotlib | 10 MB | Depende de matplotlib |
| `plotly` | 5.17.0 | Gráficos interactivos (webGL) | 30 MB | Alternativa moderna |
| `networkx` | (mencionado en código) | Análisis de grafos | 5 MB | Para análisis local |

### 🔐 Criptografía y Seguridad
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `cryptography` | 42.0.8 | Cifrado, hashing criptográfico | 5 MB |
| `bcrypt` | 4.1.2 | Hashing de contraseñas | 200 KB |
| `PyJWT` | 2.8.0 | Manejo de JWT tokens | 50 KB |

### ⚡ Procesamiento Asincrónico
| Librería | Versión | Propósito | Tamaño | Notas |
|:---|:---:|:---|:---:|:---|
| `aiofiles` | 23.2.1 | I/O asincrónico de archivos | 50 KB | Ligero |
| `asyncio` | (builtin en Python 3.7+) | Async/await framework | - | Incluido en Python |

### 🗂️ Manejo de Archivos
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `Pillow` | 10.1.0 | Procesamiento de imágenes | 10 MB |
| `python-multipart` | 0.0.6 | Parsing de form data multipart | 50 KB |
| `openpyxl` | 3.1.2 | Lectura/escritura de Excel | 2 MB |
| `python-magic` | 0.4.27 | Detección de tipos de archivo | 100 KB |

### 📹 Audio y Multimedia
| Librería | Versión | Propósito | Tamaño | Notas |
|:---|:---:|:---|:---:|:---|
| `librosa` | 0.10.1 | Análisis de audio (musicales features) | 30 MB | Opcional |
| `SpeechRecognition` | 3.10.0 | Reconocimiento de voz | 2 MB | Opcional |
| `opencv-python` | 4.8.1.78 | Procesamiento de video/imágenes | 100 MB | Bastante pesado para dual-core |

### 🎨 Imagen (Visión Computadora)
| Librería | Versión | Propósito | Tamaño | Notas |
|:---|:---:|:---|:---:|:---|
| `opencv-python` | 4.8.1.78 | Computer vision | 100 MB | ⚠️ Evitar si espacio es crítico |

### ⏱️ Utilidades de Fecha y Tiempo
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `python-dateutil` | 2.8.2 | Extensiones avanzadas para datetime | 200 KB |
| `pytz` | 2023.3 | Manejo de zonas horarias | 100 KB |

### 📈 Monitoreo y Logging
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `loguru` | 0.7.2 | Logging mejorado y colorido | 100 KB |
| `prometheus-client` | 0.19.0 | Métricas Prometheus (opcional) | 500 KB |
| `psutil` | 5.9.6 | Monitoreo de recursos (CPU, RAM, disco) | 200 KB |

### 🛠️ Utilidades CLI y Formato
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `tqdm` | 4.66.1 | Barras de progreso en terminal | 50 KB |
| `click` | 8.1.7 | Framework para crear CLIs | 200 KB |
| `rich` | 13.7.0 | Terminal output formateado (tablas, colores) | 200 KB |
| `typer` | 0.9.0 | Crear CLIs con tipado automático | 100 KB |

### 📋 Validación y Esquemas
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `pydantic` | 2.5.0 | Validación de datos con schemas | 500 KB |
| `jsonschema` | 4.20.0 | Validar JSON contra schema | 100 KB |
| `marshmallow` | 3.20.1 | Serialización/deserialización de datos | 200 KB |

### 💾 Compresión y Cache
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `cachetools` | 5.3.2 | Decoradores para caching | 50 KB |
| `zstandard` | 0.22.0 | Compresión Zstandard | 1 MB |
| `redis` | 5.0.1 | Cliente Redis (opcional para cache) | 200 KB |

### 🧪 Testing (SOLO EN DESARROLLO)
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `pytest` | 7.4.3 | Framework de testing | 1 MB |
| `pytest-asyncio` | 0.21.1 | Soporte async en pytest | 100 KB |
| `pytest-cov` | 4.1.0 | Coverage de tests | 500 KB |

### 🎨 Desarrollo (SOLO EN DESARROLLO)
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `black` | 23.11.0 | Formateador de código Python | 2 MB |
| `flake8` | 6.1.0 | Linter de código | 500 KB |
| `mypy` | 1.7.1 | Type checking estático | 2 MB |

### 📓 Jupyter (OPCIONAL, SOLO para desarrollo/notebooks)
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `jupyter` | 1.0.0 | Ambiente Jupyter completo | 5 MB |
| `ipykernel` | 6.27.1 | Kernel de IPython para Jupyter | 2 MB |

### 🌐 Google Cloud APIs
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `google-api-python-client` | 2.108.0 | Cliente de Google APIs (Drive, Sheets, etc.) | 2 MB |
| `google-auth-httplib2` | 0.1.1 | Autenticación HTTP para Google | 50 KB |
| `google-auth-oauthlib` | 1.1.0 | OAuth flow para Google | 100 KB |
| `google-auth` | 2.23.4 | Core de autenticación Google | 500 KB |

---

## 🖥️ PC 2: Computador Potente (Neo4j + Análisis Pesado)

### 🗄️ Neo4j y Graph Database
| Librería | Versión | Propósito | Tamaño | Instalación |
|:---|:---:|:---|:---:|:---|
| `neo4j` | 5.15.0 | Driver Python (también instalado en PC1) | 500 KB | `pip install neo4j` |

### 🔬 Análisis Formal de Conceptos (FCA)
| Librería | Versión | Propósito | Tamaño | Instalación |
|:---|:---:|:---|:---:|:---|
| `concepts` | 0.9.2 | Formal Concept Analysis | 2 MB | `pip install concepts` |
| `fcapy` | 0.1.0 | Alternativa FCA (si falla concepts) | 1 MB | `pip install fcapy` |

### 🔗 Neo4j Graph Data Science (GDS)
| Librería | APOC | Propósito | Notas |
|:---|:---:|:---|:---|
| Neo4j GDS Plugin | (builtin) | Algoritmos de grafos (PageRank, Louvain, etc.) | Se instala en servidor Neo4j, NO via pip |
| Neo4j APOC Plugin | (builtin) | Batch operations, stored procedures | Incluido en Neo4j Enterprise/Community 5.x |

**Instalación en Neo4j Server (PC 2):**
```bash
# Copiar JAR a plugins/ de Neo4j
cp apoc-5.x.x-all.jar /var/lib/neo4j/plugins/
cp neo4j-graph-data-science-2.x.x.jar /var/lib/neo4j/plugins/

# Editar neo4j.conf
dbms.security.procedures.unrestricted=apoc.*,gds.*

# Reiniciar Neo4j
systemctl restart neo4j
```

### 🔤 Fuzzy Matching (Consolidación de Identidades)
| Librería | Versión | Propósito | Tamaño |
|:---|:---:|:---|:---:|
| `thefuzz` | 0.20.0 | Fuzzy string matching para co-reference | 100 KB |
| `python-Levenshtein` | 0.21.1 | Acelerador compilado para thefuzz | 200 KB |

---

## ☁️ Servicios Externos (NO requieren instalación de librerías locales)

### 📱 Supabase (PostgreSQL + Auth + Storage)
| Servicio | Librería Cliente | Propósito |
|:---|:---:|:---|
| **Supabase** | `supabase==2.1.1` | Backend as a Service (PostgreSQL + Auth) |
| PostgreSQL | `psycopg2-binary==2.9.9` | Driver PostgreSQL |

**Instalación:**
```bash
pip install supabase psycopg2-binary
```

### 🚀 n8n (Workflow Automation)
| Herramienta | Puerto | Propósito | Acceso |
|:---|:---:|:---|:---|
| **n8n** | 5678 | Automatización de workflows, integraciones REST | HTTP via `requests` |

**No requiere librería especial** - comunica via HTTP REST

### 🗂️ Google Drive (APIs)
Librerías ya listadas en PC 1:
- `google-api-python-client`
- `google-auth-oauthlib`
- `google-auth`

---

## 📦 Archivos `requirements.txt` Recomendados

### PC 1: Dual-Core AMD - `requirements_dualcore.txt`
```txt
# ===========================================
# LIBRERÍAS OPTIMIZADAS PARA DUAL-CORE AMD
# ===========================================

# Core
neo4j==5.15.0
python-dotenv==1.0.0
PyYAML==6.0.1
toml==0.10.2

# NLP - SOLO MODELO PEQUEÑO
spacy==3.7.2
# Descargar: python -m spacy download es_core_news_sm

# Embeddings - MODELO LIGERO
sentence-transformers==2.2.2
# Usará: all-MiniLM-L6-v2 (80MB)

# Computación científica
numpy==1.26.4
scipy==1.11.4
pandas==2.1.4
scikit-learn==1.3.2

# Red e HTTP
requests==2.31.0
httpx==0.24.1
aiohttp==3.9.1
websockets==12.0

# Utilidades
python-dateutil==2.8.2
pytz==2023.3
tqdm==4.66.1
click==8.1.7
rich==13.7.0
typer==0.9.0

# Validación
pydantic==2.5.0
jsonschema==4.20.0
marshmallow==3.20.1

# Logging
loguru==0.7.2
psutil==5.9.6

# Cache y compresión
cachetools==5.3.2
zstandard==0.22.0
redis==5.0.1

# Testing (opcional)
pytest==7.4.3
pytest-asyncio==0.21.1

# Desarrollo (opcional)
black==23.11.0
flake8==6.1.0
mypy==1.7.1

# Integraciones
supabase==2.1.1
psycopg2-binary==2.9.9

# Google APIs
google-api-python-client==2.108.0
google-auth==2.23.4
google-auth-oauthlib==1.1.0

# Multimedia (opcional)
Pillow==10.1.0
librosa==0.10.1
SpeechRecognition==3.10.0

# NO incluir (demasiado pesado):
# torch
# tensorflow
# es_core_news_lg
# opencv-python
```

### PC 2: Potente - `requirements_neo4j_fca.txt`
```txt
# ===========================================
# LIBRERÍAS PARA PC POTENTE (NEO4J + FCA)
# ===========================================

neo4j==5.15.0
numpy==1.26.4
scipy==1.11.4
pandas==2.1.4
scikit-learn==1.3.2

# FCA
concepts==0.9.2

# Fuzzy matching
thefuzz==0.20.0
python-Levenshtein==0.21.1

# Utilidades
PyYAML==6.0.1
python-dotenv==1.0.0
tqdm==4.66.1
loguru==0.7.2
psutil==5.9.6

# Visualización
networkx>=2.6
matplotlib==3.8.2
plotly==5.17.0

# Testing
pytest==7.4.3
pytest-asyncio==0.21.1
```

---

## 🔄 Arquitectura de Instalación Completa

```
┌─────────────────────────────────────────────────────────────┐
│                    PROYECTO YO ESTRUCTURAL                  │
└─────────────────────────────────────────────────────────────┘

┌──────────────────────────────┐      ┌──────────────────────────────┐
│    PC 1: DUAL-CORE AMD       │      │    PC 2: POTENTE             │
│  (Procesadores Ligeros)      │      │  (Neo4j + FCA + Análisis)    │
├──────────────────────────────┤      ├──────────────────────────────┤
│                              │      │                              │
│ ✅ spacy (sm) 50MB           │      │ ✅ Neo4j 5.15 (server)       │
│ ✅ sentence-transformers 80MB│      │ ✅ concepts (FCA) 2MB        │
│ ✅ scikit-learn 20MB         │      │ ✅ GDS Plugin (APOC)         │
│ ✅ numpy, scipy, pandas      │      │ ✅ thefuzz 100KB             │
│ ✅ requests, httpx, aiohttp  │      │ ✅ Visualización (nx, mpl)   │
│ ✅ Google APIs               │      │                              │
│ ✅ Supabase connector        │      │ 🔌 PostgreSQL (Supabase)     │
│                              │      │                              │
│ ❌ torch (demasiado pesado)  │      │                              │
│ ❌ es_core_news_lg (500MB)   │      │                              │
│ ❌ opencv-python (100MB)     │      │                              │
│                              │      │                              │
│ Total: ~450MB (sin modelos)  │      │ Total: ~200MB                │
│        + 80MB (embeddings)   │      │                              │
│        + 50MB (spacy)        │      │                              │
│ ─────────────────────────    │      │                              │
│ ≈ 580MB final               │      │                              │
│                              │      │                              │
└──────────────────────────────┘      └──────────────────────────────┘
         ⬇️ REST + bolt://               ⬇️ GraphQL + Supabase
      (red LAN 1Gbps)                  (cloud)
         
    ☁️ SERVICIOS EXTERNOS
    ├── Supabase (PostgreSQL)
    ├── Google Drive (OAuth)
    └── n8n (Workflows)
```

---

## 🚀 Pasos de Instalación

### PASO 1: PC 1 (Dual-Core AMD)

```bash
# 1. Crear entorno virtual
python3.8 -m venv venv_pc1
source venv_pc1/bin/activate

# 2. Instalar dependencias optimizadas
pip install -r requirements_dualcore.txt

# 3. Descargar modelo spaCy pequeño
python -m spacy download es_core_news_sm

# 4. Verificar instalación
python -c "import spacy; import sentence_transformers; print('✅ OK')"
```

### PASO 2: PC 2 (Potente)

```bash
# 1. Instalar Neo4j (OS package manager o Docker)
# Ubuntu/Debian:
sudo apt install neo4j

# O con Docker:
docker run -d \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password \
  neo4j:5.15

# 2. Crear entorno virtual
python3.8 -m venv venv_neo4j
source venv_neo4j/bin/activate

# 3. Instalar dependencias
pip install -r requirements_neo4j_fca.txt

# 4. Verificar conexión Neo4j
python -c "from neo4j import GraphDatabase; print('✅ OK')"
```

### PASO 3: Variables de Entorno (.env)

```bash
# .env
NEO4J_URI=bolt://192.168.1.100:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=tu_password_segura

SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=xxxxxx

GOOGLE_DRIVE_CREDENTIALS_PATH=/ruta/a/credentials.json

N8N_URL=http://192.168.1.200:5678
```

---

## 📊 Comparativa de Tamaños

| Componente | Tamaño | Ubicación |
|:---|:---:|:---|
| spacy (sm) | 50 MB | PC 1 |
| spacy (lg) | 500 MB | ❌ Evitar |
| sentence-transformers (MiniLM) | 80 MB | PC 1 |
| sentence-transformers (mpnet-base) | 420 MB | ❌ Evitar |
| torch + transformers | 500+ MB | ❌ Evitar en dual-core |
| scikit-learn + scipy | 50 MB | PC 1 |
| Neo4j Server | 300 MB | PC 2 |
| concepts (FCA) | 2 MB | PC 2 |
| **PC 1 Total (optimizado)** | **~650 MB** | - |
| **PC 2 Total (base)** | **~500 MB** | - |

---

## ⚠️ Advertencias Críticas para Dual-Core

### ❌ NO instalar en PC 1:
1. `torch` (500 MB) - Usar `sentence-transformers` instead
2. `tensorflow` (300 MB+) - Usar `scikit-learn` instead
3. `es_core_news_lg` (500 MB) - Usar `es_core_news_sm` (50 MB)
4. `opencv-python` (100 MB) - Opcional, usar solo si necesario
5. `transformers` con modelos grandes

### ✅ Alternativas ligeras recomendadas:
- `sentence-transformers` en lugar de `transformers` + `torch`
- `spacy-sm` en lugar de `spacy-lg`
- `scikit-learn` en lugar de `xgboost` o `lightgbm`
- `fastapi` + `uvicorn` en lugar de `flask` (más eficiente)

---

## 📝 Notas Adicionales

### Sincronización entre PCs
- Usar `rsync` para sincronizar configuraciones:
  ```bash
  rsync -av config/ usuario@pc2:/ruta/config/
  ```

### Monitoreo de consumo
```bash
# En PC 1, monitorear durante ejecución:
watch -n 1 'ps aux | grep python | grep -v grep | awk "{sum+=\$6} END {print \"RAM: \" sum \" KB\"}"'

# O usar psutil:
python -c "import psutil; print(f'RAM: {psutil.virtual_memory().percent}%')"
```

### Actualización de librerías
```bash
# Verificar dependencias desactualizadas
pip list --outdated

# Actualizar todos (cuidadoso)
pip install --upgrade -r requirements_dualcore.txt
```

---

**Última actualización:** 2025-11-06
**Versión del sistema:** YO Estructural v2.3-optimized
**Estado:** ✅ Listo para implementación
