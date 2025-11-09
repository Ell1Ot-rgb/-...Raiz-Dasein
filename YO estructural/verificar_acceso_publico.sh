#!/bin/bash
# Script para verificar que los puertos sean accesibles públicamente

echo "🔍 Verificando acceso público a los servicios..."
echo ""

CODESPACE_NAME="sinister-wand-5vqjp756r4xcvpvw"

# URLs esperadas
N8N_URL="https://${CODESPACE_NAME}-5678.app.github.dev"
NEO4J_URL="https://${CODESPACE_NAME}-7474.app.github.dev"
API_URL="https://${CODESPACE_NAME}-8000.app.github.dev"

echo "📍 URLs de tus servicios:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "n8n:      $N8N_URL"
echo "Neo4j:    $NEO4J_URL"
echo "API:      $API_URL"
echo ""

# Verificar n8n
echo "🧪 Probando acceso a n8n..."
if curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$N8N_URL" | grep -q "200\|401\|403"; then
    echo "✅ n8n es accesible públicamente"
    echo "   URL: $N8N_URL"
else
    echo "❌ n8n NO es accesible públicamente"
    echo "   Haz el puerto 5678 público en el panel PORTS"
fi

echo ""

# Verificar Neo4j
echo "🧪 Probando acceso a Neo4j..."
if curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$NEO4J_URL" | grep -q "200\|401\|403"; then
    echo "✅ Neo4j es accesible públicamente"
    echo "   URL: $NEO4J_URL"
else
    echo "❌ Neo4j NO es accesible públicamente"
    echo "   Haz el puerto 7474 público en el panel PORTS"
fi

echo ""

# Verificar API
echo "🧪 Probando acceso a API..."
if curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$API_URL" | grep -q "200\|401\|403\|404"; then
    echo "✅ API es accesible públicamente"
    echo "   URL: $API_URL"
else
    echo "⚠️  API no responde (contenedor unhealthy)"
    echo "   Haz el puerto 8000 público cuando se arregle"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 Workflow n8n:"
echo "   $N8N_URL/workflow/bRzrHvbsZ8H5fxcQ"
echo ""
echo "🔗 Webhook para probar:"
echo "   curl -X POST $N8N_URL/webhook/generar-maximo \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"concepto\": \"SOPORTE\"}'"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
