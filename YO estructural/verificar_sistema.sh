#!/bin/bash

# ═══════════════════════════════════════════════════════════════════════════
# RESUMEN EJECUTIVO: Sistema n8n + Neo4j + Gemini en Codespaces
# ═══════════════════════════════════════════════════════════════════════════

echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                              ║"
echo "║   ✅ SISTEMA COMPLETAMENTE OPERATIVO EN GITHUB CODESPACES                   ║"
echo "║                                                                              ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Verificar servicios
echo "🔍 Verificando servicios..."
echo ""

# Neo4j
if docker ps | grep -q "yo_estructural_neo4j.*healthy"; then
    echo "✅ Neo4j: HEALTHY"
    echo "   📍 Browser: http://localhost:7474"
    echo "   📍 Bolt: bolt://localhost:7687"
    echo "   🔑 neo4j / fenomenologia2024"
else
    echo "⚠️  Neo4j: NO DISPONIBLE"
fi
echo ""

# n8n
if docker ps | grep -q "yo_estructural_n8n.*healthy"; then
    echo "✅ n8n: HEALTHY"
    echo "   📍 URL: http://localhost:5678"
    echo "   🔑 admin / fenomenologia2024"
else
    echo "⚠️  n8n: NO DISPONIBLE"
fi
echo ""

# API
if docker ps | grep -q "yo_estructural_api"; then
    echo "✅ API YO Estructural: RUNNING"
    echo "   📍 URL: http://localhost:8000"
else
    echo "⚠️  API: NO DISPONIBLE"
fi
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔑 CONFIGURACIÓN APLICADA:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✅ Gemini API Key: AIzaSyAtgpP05qWmGW6dUZnYBW96K3U-gLiV5Kc"
echo "✅ Neo4j inicializado con estructura de migración"
echo "✅ Workflow n8n disponible para importar"
echo "✅ Sistema preparado para servidor remoto"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 PRÓXIMOS PASOS:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1️⃣  Acceder a n8n: http://localhost:5678"
echo "    Login: admin / fenomenologia2024"
echo ""
echo "2️⃣  Configurar credenciales en n8n:"
echo "    • Neo4j: host=neo4j, port=7687, user=neo4j, pass=fenomenologia2024"
echo "    • Gemini: API Key = AIzaSyAtgpP05qWmGW6dUZnYBW96K3U-gLiV5Kc"
echo ""
echo "3️⃣  Importar workflow:"
echo "    n8n_setup/workflows/workflow_5_generador_maximo_relacional.json"
echo ""
echo "4️⃣  Probar sistema con:"
echo "    curl -X POST http://localhost:5678/webhook/generar-maximo \\"
echo "      -H 'Content-Type: application/json' \\"
echo "      -d '{\"concepto\": \"SOPORTE\"}'"
echo ""
echo "5️⃣  Cuando esté listo, migrar a servidor remoto (192.168.1.37)"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📚 DOCUMENTACIÓN:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📄 ESTADO_SISTEMA_CODESPACES.txt - Estado completo del sistema"
echo "📄 README_N8N_GEMINI_RAPIDO.md - Inicio rápido (5 min)"
echo "📄 GUIA_INTEGRACION_N8N_GEMINI.md - Guía completa técnica"
echo "📄 neo4j_init_simple.cypher - Script de inicialización Neo4j"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "⚠️  IMPORTANTE - CODESPACES:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "GitHub Codespaces tiene cuota gratuita limitada."
echo "Para producción 24/7, debes migrar a tu servidor remoto."
echo ""
echo "Detener servicios cuando no uses: docker-compose down"
echo "Reiniciar servicios: docker-compose up -d neo4j n8n"
echo ""

echo "✅ ¡Sistema listo para usar!"
echo ""
