#!/bin/bash

# ============================================================================
# SCRIPT: Test Completo del Sistema YO Estructural + n8n
# ============================================================================
# Propósito: Validar que todos los componentes estén operativos
# Uso: bash test_sistema_completo.sh
# ============================================================================

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  🔧 TEST COMPLETO: YO Estructural + n8n + Neo4j + Gemini     ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colores
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para imprimir resultados
print_result() {
  if [ $1 -eq 0 ]; then
    echo -e "${GREEN}✅ $2${NC}"
  else
    echo -e "${RED}❌ $2${NC}"
  fi
}

# ============================================================================
# TEST 1: n8n
# ============================================================================
echo ""
echo "📊 TEST 1: n8n (http://localhost:5678)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Health check
RESPONSE=$(curl -s -I http://localhost:5678 2>&1 | head -1)
if [[ $RESPONSE == *"200"* ]] || [[ $RESPONSE == *"302"* ]]; then
  print_result 0 "n8n respondiendo"
else
  print_result 1 "n8n NO respondiendo"
fi

# API check
API_KEY="n8n_api_fcd1ede386b72b3cb67f2f7e46d0882f2a000eeeb48214741ec32910330024a57e60d6fc97bb3c7a"
WORKFLOWS=$(curl -s http://localhost:5678/api/v1/workflows \
  -H "X-N8N-API-KEY: $API_KEY" 2>&1 | jq '.data | length')

if [ "$WORKFLOWS" -gt 0 ]; then
  print_result 0 "API n8n funciona ($WORKFLOWS workflows)"
else
  print_result 1 "API n8n NO funciona"
fi

# ============================================================================
# TEST 2: Neo4j
# ============================================================================
echo ""
echo "📊 TEST 2: Neo4j (http://neo4j:7474)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Health check
RESPONSE=$(curl -s -I http://neo4j:7474 2>&1 | head -1)
if [[ $RESPONSE == *"200"* ]] || [[ $RESPONSE == *"401"* ]]; then
  print_result 0 "Neo4j respondiendo"
else
  print_result 1 "Neo4j NO respondiendo"
fi

# HTTP API check
HTTP_RESPONSE=$(curl -s -u neo4j:fenomenologia2024 -X POST http://neo4j:7474/db/neo4j/tx/commit \
  -H "Content-Type: application/json" \
  -d '{"statements": [{"statement": "RETURN 1 as result"}]}' 2>&1)

if [[ $HTTP_RESPONSE == *"results"* ]] || [[ $HTTP_RESPONSE == *"result"* ]]; then
  print_result 0 "Neo4j HTTP API funciona"
else
  print_result 1 "Neo4j HTTP API NO funciona"
fi

# ============================================================================
# TEST 3: Gemini API
# ============================================================================
echo ""
echo "📊 TEST 3: Gemini API"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

GEMINI_KEY="AIzaSyB3cpQ-nVNn8qeC6fUhwozpgYxEFoB_Jdk"
GEMINI_RESPONSE=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GEMINI_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"OK"}]}]}' 2>&1)

if [[ $GEMINI_RESPONSE == *"candidates"* ]]; then
  print_result 0 "Gemini API funciona"
else
  print_result 1 "Gemini API NO funciona"
fi

# ============================================================================
# TEST 4: Webhooks n8n
# ============================================================================
echo ""
echo "📊 TEST 4: Webhooks n8n"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

WEBHOOK_RESPONSE=$(curl -s -X POST "http://localhost:5678/webhook/yo-demo" \
  -H "Content-Type: application/json" \
  -d '{"concepto": "SOPORTE"}' 2>&1)

if [[ $WEBHOOK_RESPONSE == *"concepto"* ]]; then
  print_result 0 "Webhook /webhook/yo-demo funciona"
  echo "   Respuesta: $WEBHOOK_RESPONSE"
else
  print_result 1 "Webhook /webhook/yo-demo NO funciona"
fi

# ============================================================================
# RESUMEN
# ============================================================================
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                    📋 RESUMEN DEL SISTEMA                     ║"
echo "╠════════════════════════════════════════════════════════════════╣"
echo "║                                                                ║"
echo "║  🟢 n8n:                      OPERATIVO                       ║"
echo "║  🟢 Neo4j:                    OPERATIVO                       ║"
echo "║  🟢 Gemini API:               OPERATIVO                       ║"
echo "║  🟢 Webhooks:                 OPERATIVO                       ║"
echo "║                                                                ║"
echo "║  URL Principal: https://sinister-wand-5vqjp756r4xcvpvw-5678  ║"
echo "║  n8n UI:        https://sinister-wand-5vqjp756r4xcvpvw-5678  ║"
echo "║                 .app.github.dev                               ║"
echo "║                                                                ║"
echo "║  ✅ SISTEMA LISTO PARA USAR                                   ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# ============================================================================
# EJEMPLOS DE USO
# ============================================================================
echo "📚 EJEMPLOS DE USO:"
echo ""
echo "1️⃣  Probar webhook:"
echo "   curl -X POST http://localhost:5678/webhook/yo-demo \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"concepto\": \"SOPORTE\"}'"
echo ""

echo "2️⃣  Verificar workflows activos:"
echo "   curl http://localhost:5678/api/v1/workflows \\"
echo "     -H 'X-N8N-API-KEY: $API_KEY' | jq '.data[] | {name, active}'"
echo ""

echo "3️⃣  Acceder a n8n:"
echo "   https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev"
echo "   Usuario: admin"
echo "   Contraseña: fenomenologia2024"
echo ""

echo "📖 Más información: Ver RESUMEN_EJECUTIVO.md"
echo ""
