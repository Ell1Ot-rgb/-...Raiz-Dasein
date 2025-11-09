#!/bin/bash

# Script para probar el webhook del workflow YO Estructural

WEBHOOK_URL="http://localhost:5678/webhook/generador-maximo"
API_KEY="n8n_api_6e5908f5bc7b1d7db57554be72e9c61b104b13562ac4f41f1344f2727a7f189431e402a9684421cf"

echo "🚀 Probando Workflow YO Estructural..."
echo "URL: $WEBHOOK_URL"
echo ""

# Test 1: Concepto SOPORTE
echo "Test 1: Concepto 'SOPORTE'"
curl -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "concepto": "SOPORTE",
    "timestamp": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
  }' 2>&1 | jq '.' || echo "Error en la respuesta"

echo ""
echo "✅ Test completado"
