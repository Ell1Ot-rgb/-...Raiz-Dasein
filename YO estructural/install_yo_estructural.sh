#!/bin/bash

# ============================================================================
# 🚀 SCRIPT DE INSTALACIÓN AUTOMÁTICA - YO ESTRUCTURAL
# ============================================================================
# 
# Uso:
#   ./install_yo_estructural.sh [pc1|pc2] [python_version]
#
# Ejemplos:
#   ./install_yo_estructural.sh pc1 3.8
#   ./install_yo_estructural.sh pc2 3.10
#   ./install_yo_estructural.sh pc1        # usa Python default
#
# ============================================================================

set -e  # Exit on error

# ─────────────────────────────────────────────────────────────────────────
# COLORES PARA OUTPUT
# ─────────────────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ─────────────────────────────────────────────────────────────────────────
# FUNCIONES AUXILIARES
# ─────────────────────────────────────────────────────────────────────────

print_header() {
    echo -e "${BLUE}╔════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${NC}  $1"
    echo -e "${BLUE}╚════════════════════════════════════════════════════════════════╝${NC}"
}

print_step() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗ ERROR:${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# ─────────────────────────────────────────────────────────────────────────
# VALIDACIÓN DE PARÁMETROS
# ─────────────────────────────────────────────────────────────────────────

if [ $# -eq 0 ]; then
    print_error "Se requiere parámetro: pc1 o pc2"
    echo "Uso: $0 [pc1|pc2] [python_version]"
    exit 1
fi

PC_TYPE=$1
PYTHON_VERSION=${2:-3.8}

if [[ "$PC_TYPE" != "pc1" && "$PC_TYPE" != "pc2" ]]; then
    print_error "Tipo de PC inválido. Use 'pc1' o 'pc2'"
    exit 1
fi

# ─────────────────────────────────────────────────────────────────────────
# DETECTAR SISTEMA OPERATIVO
# ─────────────────────────────────────────────────────────────────────────

OS_TYPE=$(uname -s)
if [[ "$OS_TYPE" == "Linux" ]]; then
    DISTRO=$(lsb_release -si 2>/dev/null || echo "Linux")
elif [[ "$OS_TYPE" == "Darwin" ]]; then
    DISTRO="macOS"
else
    DISTRO="Unknown"
fi

print_header "INSTALACIÓN YO ESTRUCTURAL - $PC_TYPE"
echo -e "Sistema operativo: ${GREEN}$DISTRO${NC}"
echo -e "Versión Python: ${GREEN}$PYTHON_VERSION${NC}"
echo ""

# ─────────────────────────────────────────────────────────────────────────
# VERIFICAR PYTHON
# ─────────────────────────────────────────────────────────────────────────

print_info "Verificando Python $PYTHON_VERSION..."
if ! command -v python$PYTHON_VERSION &> /dev/null; then
    print_warning "Python $PYTHON_VERSION no encontrado. Intentando con 'python3'..."
    PYTHON_CMD="python3"
    if ! command -v $PYTHON_CMD &> /dev/null; then
        print_error "Python no está instalado"
        exit 1
    fi
else
    PYTHON_CMD="python$PYTHON_VERSION"
fi

PYTHON_ACTUAL=$($PYTHON_CMD --version)
print_step "Python encontrado: $PYTHON_ACTUAL"

# ─────────────────────────────────────────────────────────────────────────
# CREAR ENTORNO VIRTUAL
# ─────────────────────────────────────────────────────────────────────────

if [ "$PC_TYPE" = "pc1" ]; then
    VENV_DIR="venv_pc1"
    VENV_NAME="YO Estructural - PC1 (Dual-Core AMD)"
else
    VENV_DIR="venv_neo4j"
    VENV_NAME="YO Estructural - PC2 (Neo4j + FCA)"
fi

print_info "Creando entorno virtual: $VENV_DIR"
$PYTHON_CMD -m venv $VENV_DIR
print_step "Entorno virtual creado"

# Activar entorno
source $VENV_DIR/bin/activate
print_step "Entorno activado"

# ─────────────────────────────────────────────────────────────────────────
# ACTUALIZAR PIP
# ─────────────────────────────────────────────────────────────────────────

print_info "Actualizando pip, setuptools y wheel..."
pip install --upgrade pip setuptools wheel -q
print_step "pip actualizado"

# ─────────────────────────────────────────────────────────────────────────
# INSTALACIÓN ESPECÍFICA POR PC
# ─────────────────────────────────────────────────────────────────────────

if [ "$PC_TYPE" = "pc1" ]; then
    print_header "INSTALANDO LIBRERÍAS PC1 (DUAL-CORE AMD)"
    
    # Verificar espacio en disco
    SPACE_AVAILABLE=$(df -BG . | awk 'NR==2 {print $4}' | sed 's/G//')
    if [ "$SPACE_AVAILABLE" -lt 2 ]; then
        print_warning "Poco espacio disponible (~${SPACE_AVAILABLE}GB). Necesitas ~2GB"
    fi
    
    print_info "Instalando dependencias base..."
    pip install --upgrade \
        python-dotenv==1.0.0 \
        PyYAML==6.0.1 \
        toml==0.10.2 \
        -q
    print_step "Dependencias base instaladas"
    
    print_info "Instalando librerías NLP y embeddings..."
    pip install --upgrade \
        spacy==3.7.2 \
        nltk==3.8.1 \
        sentence-transformers==2.2.2 \
        -q
    print_step "NLP instalado"
    
    print_info "Descargando modelo spaCy es_core_news_sm (~50 MB)..."
    $PYTHON_CMD -m spacy download es_core_news_sm -q
    print_step "Modelo spaCy descargado"
    
    print_info "Instalando librerías de computación científica..."
    pip install --upgrade \
        numpy==1.26.4 \
        scipy==1.11.4 \
        pandas==2.1.4 \
        scikit-learn==1.3.2 \
        -q
    print_step "Computación científica instalada"
    
    print_info "Instalando librerías de networking..."
    pip install --upgrade \
        requests==2.31.0 \
        httpx==0.24.1 \
        aiohttp==3.9.1 \
        websockets==12.0 \
        neo4j==5.15.0 \
        psycopg2-binary==2.9.9 \
        -q
    print_step "Networking instalado"
    
    print_info "Instalando utilidades..."
    pip install --upgrade \
        python-dateutil==2.8.2 \
        pytz==2023.3 \
        loguru==0.7.2 \
        psutil==5.9.6 \
        tqdm==4.66.1 \
        click==8.1.7 \
        rich==13.7.0 \
        typer==0.9.0 \
        -q
    print_step "Utilidades instaladas"
    
    print_info "Instalando validación y formato..."
    pip install --upgrade \
        pydantic==2.5.0 \
        jsonschema==4.20.0 \
        marshmallow==3.20.1 \
        cachetools==5.3.2 \
        zstandard==0.22.0 \
        redis==5.0.1 \
        -q
    print_step "Validación instalada"
    
    print_info "Instalando integraciones..."
    pip install --upgrade \
        Pillow==10.1.0 \
        python-multipart==0.0.6 \
        python-magic==0.4.27 \
        openpyxl==3.1.2 \
        librosa==0.10.1 \
        SpeechRecognition==3.10.0 \
        -q
    print_step "Integraciones instaladas"
    
    print_info "Instalando Google APIs..."
    pip install --upgrade \
        google-api-python-client==2.108.0 \
        google-auth==2.23.4 \
        google-auth-oauthlib==1.1.0 \
        google-auth-httplib2==0.1.1 \
        -q
    print_step "Google APIs instaladas"
    
    print_info "Instalando Supabase..."
    pip install --upgrade \
        supabase==2.1.1 \
        -q
    print_step "Supabase instalada"
    
    print_info "Instalando herramientas de desarrollo (opcional)..."
    pip install --upgrade \
        pytest==7.4.3 \
        pytest-asyncio==0.21.1 \
        black==23.11.0 \
        flake8==6.1.0 \
        mypy==1.7.1 \
        -q
    print_step "Herramientas de desarrollo instaladas"
    
    # Verificación
    print_info "Verificando instalación..."
    $PYTHON_CMD -c "
import dotenv
import yaml
import spacy
from sentence_transformers import SentenceTransformer
import numpy
import scipy
import pandas
from sklearn.cluster import DBSCAN
import neo4j
import requests
import pydantic
print('✅ Todas las dependencias verificadas')
" && print_step "Verificación exitosa" || print_error "Falta instalar algunas librerías"

elif [ "$PC_TYPE" = "pc2" ]; then
    print_header "INSTALANDO LIBRERÍAS PC2 (NEO4J + FCA)"
    
    print_info "Instalando dependencias base..."
    pip install --upgrade \
        python-dotenv==1.0.0 \
        PyYAML==6.0.1 \
        -q
    print_step "Dependencias base instaladas"
    
    print_info "Instalando librerías de computación..."
    pip install --upgrade \
        numpy==1.26.4 \
        scipy==1.11.4 \
        pandas==2.1.4 \
        scikit-learn==1.3.2 \
        -q
    print_step "Librerías de computación instaladas"
    
    print_info "Instalando Neo4j driver..."
    pip install --upgrade neo4j==5.15.0 -q
    print_step "Neo4j driver instalado"
    
    print_info "Instalando FCA..."
    pip install --upgrade concepts==0.9.2 -q || pip install fcapy==0.1.0 -q
    print_step "FCA instalado"
    
    print_info "Instalando fuzzy matching..."
    pip install --upgrade \
        thefuzz==0.20.0 \
        python-Levenshtein==0.21.1 \
        -q
    print_step "Fuzzy matching instalado"
    
    print_info "Instalando visualización..."
    pip install --upgrade \
        networkx \
        matplotlib==3.8.2 \
        plotly==5.17.0 \
        seaborn==0.13.0 \
        -q
    print_step "Visualización instalada"
    
    print_info "Instalando utilidades..."
    pip install --upgrade \
        tqdm==4.66.1 \
        loguru==0.7.2 \
        psutil==5.9.6 \
        -q
    print_step "Utilidades instaladas"
    
    print_info "Instalando testing (opcional)..."
    pip install --upgrade \
        pytest==7.4.3 \
        pytest-asyncio==0.21.1 \
        -q
    print_step "Testing instalado"
    
    # Verificación
    print_info "Verificando instalación..."
    $PYTHON_CMD -c "
import neo4j
import concepts
import networkx
import matplotlib
from sklearn.cluster import DBSCAN
from thefuzz import fuzz
print('✅ Todas las dependencias verificadas')
" && print_step "Verificación exitosa" || print_error "Falta instalar algunas librerías"
    
    # Verificar Neo4j
    print_info "Verificando Neo4j..."
    if command -v neo4j &> /dev/null; then
        print_step "Neo4j command-line encontrado"
        neo4j --version
    else
        print_warning "Neo4j CLI no está instalado. Instálalo con: sudo apt install neo4j"
    fi
fi

# ─────────────────────────────────────────────────────────────────────────
# CREAR ARCHIVOS DE CONFIGURACIÓN
# ─────────────────────────────────────────────────────────────────────────

print_header "CONFIGURACIÓN"

# Crear .env si no existe
if [ ! -f .env ]; then
    print_info "Creando archivo .env..."
    cat > .env << 'EOF'
# Configuración YO Estructural
# ============================================

# NEO4J
NEO4J_URI=bolt://192.168.1.100:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=tu_password_segura

# SUPABASE (opcional)
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=xxxxxx

# GOOGLE DRIVE (opcional)
GOOGLE_DRIVE_CREDENTIALS_PATH=/ruta/a/credentials.json

# N8N (opcional)
N8N_URL=http://192.168.1.200:5678

# MODO DIAGNOSTICO
DEBUG=false
EOF
    print_step ".env creado (editar con tus credenciales)"
else
    print_step ".env ya existe"
fi

# ─────────────────────────────────────────────────────────────────────────
# CREAR SCRIPTS DE ACTIVACIÓN
# ─────────────────────────────────────────────────────────────────────────

print_info "Creando scripts de activación..."

if [ "$PC_TYPE" = "pc1" ]; then
    cat > activate_pc1.sh << EOF
#!/bin/bash
source $VENV_DIR/bin/activate
echo "✅ Entorno PC1 activado"
EOF
    chmod +x activate_pc1.sh
    print_step "activate_pc1.sh creado"
else
    cat > activate_pc2.sh << EOF
#!/bin/bash
source $VENV_DIR/bin/activate
echo "✅ Entorno PC2 activado"
EOF
    chmod +x activate_pc2.sh
    print_step "activate_pc2.sh creado"
fi

# ─────────────────────────────────────────────────────────────────────────
# RESUMEN FINAL
# ─────────────────────────────────────────────────────────────────────────

print_header "✅ INSTALACIÓN COMPLETADA"

echo -e "${GREEN}Próximos pasos:${NC}"
echo ""

if [ "$PC_TYPE" = "pc1" ]; then
    echo "1. Activar entorno:"
    echo "   source activate_pc1.sh"
    echo ""
    echo "2. Verificar instalación:"
    echo "   python -c 'import spacy; print(spacy.load(\"es_core_news_sm\"))'  # spaCy"
    echo "   python -c 'from sentence_transformers import SentenceTransformer; print(SentenceTransformer(\"all-MiniLM-L6-v2\"))'  # Embeddings"
    echo ""
    echo "3. Editar .env con credenciales (especialmente NEO4J_URI)"
    echo ""
else
    echo "1. Activar entorno:"
    echo "   source activate_pc2.sh"
    echo ""
    echo "2. Verificar Neo4j:"
    echo "   neo4j status  # si está instalado localmente"
    echo "   docker ps | grep neo4j  # si está en Docker"
    echo ""
    echo "3. Verificar FCA:"
    echo "   python -c 'import concepts; print(\"✅ FCA OK\")'  "
    echo ""
    echo "4. Editar .env con IP de PC1"
    echo ""
fi

echo -e "${YELLOW}⚠ IMPORTANTE:${NC}"
echo "  - Editar .env con tus credenciales específicas"
echo "  - Para PC1: Actualizar NEO4J_URI con IP de PC2"
echo "  - Para PC2: Instalar Neo4j Server si aún no lo has hecho"
echo ""

echo -e "${BLUE}Información de instalación:${NC}"
echo "  Entorno: $VENV_DIR"
echo "  Python: $($PYTHON_CMD --version)"
echo "  Sistema: $DISTRO"
echo ""

deactivate  # Desactivar venv
echo -e "${GREEN}✨ ¡Listo para usar!${NC}"
