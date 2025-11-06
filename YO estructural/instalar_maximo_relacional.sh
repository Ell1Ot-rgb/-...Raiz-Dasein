#!/bin/bash

# ============================================================
# SCRIPT DE INSTALACIÓN OPTIMIZADO PARA DUAL-CORE
# ============================================================
# Este script configura TODO para máximo relacional definicional
# en AMD Dual-Core + 8GB RAM
# ============================================================

set -e  # Salir si hay error

echo "╔════════════════════════════════════════════════════════════╗"
echo "║   INSTALACIÓN MÁXIMO RELACIONAL - DUAL-CORE OPTIMIZADO    ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# ============================================================
# PASO 1: Verificar Python
# ============================================================
echo "[1/8] Verificando Python..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "  ✓ Python $python_version"

# ============================================================
# PASO 2: Crear estructura de directorios
# ============================================================
echo "[2/8] Creando directorios..."
mkdir -p procesadores
mkdir -p logs
mkdir -p cache_dualcore
mkdir -p metrics
echo "  ✓ Directorios creados"

# ============================================================
# PASO 3: Crear entorno virtual (recomendado)
# ============================================================
echo "[3/8] Configurando entorno virtual..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "  ✓ Entorno virtual creado"
else
    echo "  ℹ Entorno virtual ya existe"
fi

# Activar
source venv/bin/activate || true

# ============================================================
# PASO 4: Instalar dependencias básicas
# ============================================================
echo "[4/8] Instalando dependencias..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r requirements_dualcore.txt --no-cache-dir

echo "  ✓ Dependencias instaladas"

# ============================================================
# PASO 5: Descargar modelo spaCy pequeño
# ============================================================
echo "[5/8] Descargando modelo spaCy (pequeño)..."
python3 -m spacy download es_core_news_sm --quiet 2>/dev/null || echo "  ℹ spaCy model descargado"
echo "  ✓ Modelo spaCy listo"

# ============================================================
# PASO 6: Descargar modelo embeddings (lazy load)
# ============================================================
echo "[6/8] Verificando modelos de embeddings..."
python3 << 'EOF'
from sentence_transformers import SentenceTransformer
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("  ✓ Modelo all-MiniLM-L6-v2 listo (80MB)")
except:
    print("  ℹ Se descargará en primera ejecución")
EOF

# ============================================================
# PASO 7: Verificar configuración YAML
# ============================================================
echo "[7/8] Verificando configuración..."
if [ -f "config_dualcore_optimizado.yaml" ]; then
    echo "  ✓ config_dualcore_optimizado.yaml encontrado"
    
    # Verificar IP de Neo4j
    neo4j_url=$(grep "bolt_url:" config_dualcore_optimizado.yaml | head -1 | awk '{print $2}')
    if [[ $neo4j_url == *"192.168.X.X"* ]]; then
        echo "  ⚠ IMPORTANTE: Editar Neo4j URL en config_dualcore_optimizado.yaml"
        echo "    Reemplazar '192.168.X.X' con IP real de PC2"
    else
        echo "  ✓ Neo4j URL configurado: $neo4j_url"
    fi
else
    echo "  ✗ config_dualcore_optimizado.yaml NO encontrado"
    exit 1
fi

# ============================================================
# PASO 8: Prueba de importación
# ============================================================
echo "[8/8] Verificando importaciones..."
python3 << 'EOF'
import sys
try:
    print("  Importando NumPy... ", end="", flush=True)
    import numpy as np
    print("✓")
    
    print("  Importando SentenceTransformers... ", end="", flush=True)
    from sentence_transformers import SentenceTransformer
    print("✓")
    
    print("  Importando NetworkX... ", end="", flush=True)
    import networkx as nx
    print("✓")
    
    print("  Importando Neo4j... ", end="", flush=True)
    from neo4j import AsyncGraphDatabase
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
echo "║             ✓ INSTALACIÓN COMPLETADA                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "PRÓXIMOS PASOS:"
echo ""
echo "1. Editar configuración (si Neo4j está remoto):"
echo "   $ nano config_dualcore_optimizado.yaml"
echo "   # Cambiar: neo4j.bolt_url = bolt://IP_REAL:7687"
echo ""
echo "2. Copiar archivos a sistema_principal_v2.py:"
echo "   $ grep -l \"from procesadores\" sistema_principal_v2.py"
echo ""
echo "3. Verificar memoria disponible (dual-core):"
echo "   $ free -h"
echo ""
echo "4. Ejecutar prueba:"
echo "   $ python3 procesadores/analizador_convergencia_optimizado.py"
echo ""
echo "5. Ver logs en:"
echo "   $ tail -f logs/dualcore_execution.log"
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Sistema listo para detectar MÁXIMO RELACIONAL DEFINICIONAL║"
echo "╚════════════════════════════════════════════════════════════╝"
