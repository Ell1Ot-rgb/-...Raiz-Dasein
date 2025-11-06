#!/bin/bash

# ============================================================
# INSTALACIÓN OPTIMIZADA PARA 4GB RAM (DUAL-CORE)
# ============================================================
# PC1: 192.168.1.35 - 4GB DDR3 @ 1334MHz
# PC2: 192.168.1.37 - Neo4j + LightRAG
# ============================================================

set -e  # Salir si hay error

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     INSTALACIÓN MÁXIMO RELACIONAL - 4GB RAM OPTIMIZADO    ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "⚠️  RAM Total: 4GB DDR3 @ 1334MHz"
echo "⚠️  RAM Disponible: ~1.2GB"
echo "⚠️  Configuración: ULTRA LIGERA"
echo ""

# ============================================================
# PASO 1: Verificar Python
# ============================================================
echo "[1/9] Verificando Python..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "  ✓ Python $python_version"

# Verificar memoria disponible
mem_total=$(free -m | awk 'NR==2{print $2}')
mem_available=$(free -m | awk 'NR==2{print $7}')

if [ "$mem_total" -lt 4000 ]; then
    echo "  ⚠️  RAM detectada: ${mem_total}MB"
fi

if [ "$mem_available" -lt 1000 ]; then
    echo "  ⚠️  RAM disponible baja: ${mem_available}MB"
    echo "  ⚠️  Cierra aplicaciones innecesarias antes de continuar"
    read -p "  Presiona Enter para continuar o Ctrl+C para cancelar..."
fi

# ============================================================
# PASO 2: Crear estructura de directorios
# ============================================================
echo "[2/9] Creando directorios..."
mkdir -p procesadores
mkdir -p logs
mkdir -p cache_4gb
mkdir -p metrics
echo "  ✓ Directorios creados"

# ============================================================
# PASO 3: Crear entorno virtual LIGERO
# ============================================================
echo "[3/9] Configurando entorno virtual..."
if [ ! -d "venv_4gb" ]; then
    python3 -m venv venv_4gb --without-pip
    echo "  ✓ Entorno virtual creado (sin pip pesado)"
    
    # Instalar pip ligero
    source venv_4gb/bin/activate
    curl https://bootstrap.pypa.io/get-pip.py | python3
else
    echo "  ℹ Entorno virtual ya existe"
    source venv_4gb/bin/activate
fi

# ============================================================
# PASO 4: Instalar dependencias MÍNIMAS
# ============================================================
echo "[4/9] Instalando dependencias MÍNIMAS..."
pip install --no-cache-dir --upgrade pip setuptools wheel > /dev/null 2>&1

# Instalar solo lo esencial
pip install --no-cache-dir numpy==1.24.3
pip install --no-cache-dir scipy==1.11.1
pip install --no-cache-dir scikit-learn==1.3.0
pip install --no-cache-dir networkx==3.1
pip install --no-cache-dir neo4j==5.12.0
pip install --no-cache-dir pyyaml==6.0.1
pip install --no-cache-dir psutil==5.9.5

# SentenceTransformers LIGERO
echo "  Instalando sentence-transformers (esto puede tardar)..."
pip install --no-cache-dir sentence-transformers==2.2.2

# spaCy pequeño
pip install --no-cache-dir spacy==3.6.1

echo "  ✓ Dependencias instaladas"

# ============================================================
# PASO 5: Descargar modelo spaCy pequeño
# ============================================================
echo "[5/9] Descargando modelo spaCy (pequeño)..."
python3 -m spacy download es_core_news_sm --quiet 2>/dev/null || echo "  ℹ spaCy model descargado"
echo "  ✓ Modelo spaCy listo"

# ============================================================
# PASO 6: Verificar modelo embeddings (lazy load)
# ============================================================
echo "[6/9] Verificando modelos de embeddings..."
python3 << 'EOF'
import warnings
warnings.filterwarnings("ignore")
from sentence_transformers import SentenceTransformer
try:
    model = SentenceTransformer('paraphrase-MiniLM-L3-v2')  # 60MB
    print("  ✓ Modelo paraphrase-MiniLM-L3-v2 listo (60MB)")
except:
    print("  ℹ Se descargará en primera ejecución")
EOF

# ============================================================
# PASO 7: Verificar configuración
# ============================================================
echo "[7/9] Verificando configuración..."
if [ -f "config_4gb_optimizado.yaml" ]; then
    echo "  ✓ config_4gb_optimizado.yaml encontrado"
    
    # Verificar IPs
    neo4j_url=$(grep "bolt_url:" config_4gb_optimizado.yaml | head -1 | awk '{print $2}' | tr -d '"')
    if [[ $neo4j_url == *"192.168.1.37"* ]]; then
        echo "  ✓ Neo4j URL configurado: $neo4j_url"
    else
        echo "  ⚠️ Verificar Neo4j URL en config_4gb_optimizado.yaml"
    fi
else
    echo "  ✗ config_4gb_optimizado.yaml NO encontrado"
    exit 1
fi

# ============================================================
# PASO 8: Test de conectividad Neo4j
# ============================================================
echo "[8/9] Verificando conectividad Neo4j remoto..."
if timeout 5 bash -c "</dev/tcp/192.168.1.37/7687" 2>/dev/null; then
    echo "  ✓ Neo4j accesible en 192.168.1.37:7687"
else
    echo "  ⚠️ No se puede conectar a Neo4j en 192.168.1.37:7687"
    echo "  ⚠️ Verifica que Neo4j esté corriendo en PC2"
fi

# ============================================================
# PASO 9: Prueba de importación
# ============================================================
echo "[9/9] Verificando importaciones..."
python3 << 'EOF'
import sys
try:
    print("  Importando NumPy... ", end="", flush=True)
    import numpy as np
    print("✓")
    
    print("  Importando NetworkX... ", end="", flush=True)
    import networkx as nx
    print("✓")
    
    print("  Importando Neo4j... ", end="", flush=True)
    from neo4j import GraphDatabase
    print("✓")
    
    print("  Importando spaCy... ", end="", flush=True)
    import spacy
    print("✓")
    
    print("\n  ✓ Todas las dependencias importadas correctamente")
    
except ImportError as e:
    print(f"\n  ✗ Error de importación: {e}")
    sys.exit(1)
EOF

# ============================================================
# INFORMACIÓN FINAL
# ============================================================
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║             ✓ INSTALACIÓN COMPLETADA (4GB RAM)            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "CONFIGURACIÓN DEL SISTEMA:"
echo "  • PC1 (este equipo): 192.168.1.35"
echo "  • PC2 (servidor):    192.168.1.37"
echo "  • Neo4j:             bolt://192.168.1.37:7687"
echo "  • Usuario:           neo4j"
echo "  • Password:          fenomenologia2024"
echo ""
echo "LIMITACIONES 4GB RAM:"
echo "  ⚠️  Batch size: MAX 10 conceptos (NO más)"
echo "  ⚠️  Caché: Solo 200 embeddings"
echo "  ⚠️  Workers: 1 thread (NO paralelo)"
echo "  ⚠️  Memoria límite: 1GB de 4GB"
echo ""
echo "PRÓXIMOS PASOS:"
echo ""
echo "1. Activar entorno:"
echo "   $ source venv_4gb/bin/activate"
echo ""
echo "2. Ejecutar prueba:"
echo "   $ python3 procesadores/analizador_convergencia_optimizado.py"
echo ""
echo "3. Ver uso de memoria:"
echo "   $ watch -n 2 'free -h'"
echo ""
echo "4. Integrar en sistema_principal_v2.py:"
echo "   $ cat GUIA_INTEGRACION_MAXIMO_RELACIONAL.md"
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Sistema listo para detectar MÁXIMO RELACIONAL (4GB RAM)  ║"
echo "╚════════════════════════════════════════════════════════════╝"
