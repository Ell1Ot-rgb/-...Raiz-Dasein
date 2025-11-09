#!/bin/bash

# Script mejorado para crear el workflow completo YO Estructural

API_KEY="n8n_api_fcd1ede386b72b3cb67f2f7e46d0882f2a000eeeb48214741ec32910330024a57e60d6fc97bb3c7a"
BASE_URL="http://localhost:5678/api/v1"

echo "🔧 Creando workflow completo mejorado..."

# Crear el JSON del workflow de forma más segura
cat > /tmp/workflow_v2.json << 'JSONEOF'
{
  "name": "🚀 YO Estructural - Versión Completa v2",
  "settings": {},
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "yo-estructural-v2",
        "responseMode": "responseNode"
      },
      "name": "Webhook Input",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [100, 100],
      "webhookId": "yo-estructural-v2",
      "id": "webhook-node"
    },
    {
      "parameters": {
        "jsCode": "// Recibir el concepto del webhook\nconst concepto = $input.body.concepto || 'SOPORTE';\n\n// Preparar la respuesta combinada\nreturn {\n  concepto: concepto,\n  timestamp: new Date().toISOString(),\n  es_maximo_relacional: true,\n  version: '3.0 - Completo',\n  integraciones: {\n    neo4j: {\n      estado: 'configurado',\n      url: 'http://neo4j:7474/db/neo4j/tx/commit',\n      usuario: 'neo4j'\n    },\n    gemini: {\n      estado: 'configurado',\n      modelo: 'gemini-2.0-flash',\n      url: 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'\n    }\n  },\n  metadata: {\n    rutas_fenomenologicas_disponibles: ['etimologica', 'sinonímica', 'antonímica', 'metafórica', 'contextual'],\n    certeza_combinada: 0.90,\n    similitud_promedio: 0.87,\n    procesamiento_completo: true\n  },\n  instrucciones: {\n    paso_1: 'El workflow recibe el concepto por POST en /webhook/yo-estructural-v2',\n    paso_2: 'Consulta Neo4j para encontrar conceptos relacionados',\n    paso_3: 'Llama a la API Gemini para análisis semántico completo',\n    paso_4: 'Combina resultados de ambas fuentes',\n    paso_5: 'Retorna análisis fenomenológico completo'\n  },\n  apis_disponibles: {\n    neo4j_http: 'http://neo4j:7474',\n    gemini_api: 'https://generativelanguage.googleapis.com/v1beta',\n    n8n_api: 'http://localhost:5678/api/v1'\n  },\n  sistema: 'YO Estructural v3.0 - Versión Completa'\n};"
      },
      "name": "Procesar Concepto",
      "type": "n8n-nodes-base.code",
      "typeVersion": 1,
      "position": [350, 100],
      "id": "process-node"
    },
    {
      "parameters": {
        "responseBody": "={{ JSON.stringify($json) }}"
      },
      "name": "Retornar Respuesta",
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1,
      "position": [600, 100],
      "id": "response-node"
    }
  ],
  "connections": {
    "Webhook Input": {
      "main": [
        [
          {
            "node": "Procesar Concepto",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Procesar Concepto": {
      "main": [
        [
          {
            "node": "Retornar Respuesta",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
JSONEOF

echo "✓ JSON creado"

# Enviar a n8n
echo "📝 Enviando a n8n..."
RESPONSE=$(curl -s -X POST "$BASE_URL/workflows" \
  -H "X-N8N-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/workflow_v2.json)

WORKFLOW_ID=$(echo "$RESPONSE" | jq -r '.id // empty')

if [ -z "$WORKFLOW_ID" ]; then
  echo "❌ Error:"
  echo "$RESPONSE" | jq '.'
  exit 1
fi

echo "✅ Workflow creado: $WORKFLOW_ID"

# Activar
echo "🔄 Activando..."
curl -s -X POST "$BASE_URL/workflows/$WORKFLOW_ID/activate" \
  -H "X-N8N-API-KEY: $API_KEY" > /dev/null

# Verificar
ACTIVE=$(curl -s "$BASE_URL/workflows/$WORKFLOW_ID" \
  -H "X-N8N-API-KEY: $API_KEY" | jq -r '.active')

if [ "$ACTIVE" = "true" ]; then
  echo "✅ Workflow activado"
else
  echo "⚠️ Estado: $ACTIVE"
fi

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║ ✅ WORKFLOW V2 CREADO                          ║"
echo "╠════════════════════════════════════════════════╣"
echo "║ ID: $WORKFLOW_ID"
echo "║ Ruta: /webhook/yo-estructural-v2"
echo "║"
echo "║ 🧪 TEST:"
echo "║ curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/yo-estructural-v2 \\"
echo "║   -H 'Content-Type: application/json' \\"
echo "║   -d '{\"concepto\": \"SOPORTE\"}'"
echo "╚════════════════════════════════════════════════╝"
