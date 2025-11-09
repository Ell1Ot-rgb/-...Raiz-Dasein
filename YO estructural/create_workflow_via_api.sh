#!/bin/bash

# Script para crear el workflow completo YO Estructural en n8n
# Uso: ./create_workflow_via_api.sh

set -e

API_KEY="n8n_api_fcd1ede386b72b3cb67f2f7e46d0882f2a000eeeb48214741ec32910330024a57e60d6fc97bb3c7a"
BASE_URL="http://localhost:5678/api/v1"
GEMINI_KEY="AIzaSyB3cpQ-nVNn8qeC6fUhwozpgYxEFoB_Jdk"

echo "🔧 Creando workflow completo YO Estructural..."
echo ""

# Crear el workflow
echo "📝 Enviando definición del workflow..."

# Usar jq para construir el JSON de forma más robusta
jq -n \
  --arg name "🚀 YO Estructural - Versión Completa" \
  --arg gemini_key "$GEMINI_KEY" \
  '{
    name: $name,
    settings: {},
    nodes: [
      {
        parameters: {
          httpMethod: "POST",
          path: "yo-estructural-completo",
          responseMode: "responseNode"
        },
        name: "Webhook Input",
        type: "n8n-nodes-base.webhook",
        typeVersion: 1,
        position: [100, 100],
        webhookId: "yo-estructural-completo",
        id: "webhook-node"
      },
      {
        parameters: {
          method: "POST",
          url: "http://neo4j:7474/db/neo4j/tx/commit",
          authentication: "basicAuth",
          basicAuth: "{\"username\": \"neo4j\", \"password\": \"fenomenologia2024\"}",
          bodyType: "json",
          body: "{\"statements\": [{\"statement\": \"MATCH (c:Concepto) WHERE c.nombre CONTAINS $concepto RETURN c.nombre as concepto, c.categoria as categoria, c.certeza as certeza LIMIT 5\", \"parameters\": {\"concepto\": \"{{ $json.body.concepto }}\"}}]}"
        },
        name: "Consultar Neo4j",
        type: "n8n-nodes-base.httpRequest",
        typeVersion: 3,
        position: [350, 50],
        id: "neo4j-node"
      },
      {
        parameters: {
          method: "POST",
          url: "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
          authentication: "custom",
          sendQuery: true,
          queryParameters: ("key=" + $gemini_key),
          bodyType: "json",
          body: "{\"contents\": [{\"parts\": [{\"text\": \"Analiza el concepto fenomenológico: {{ $json.body.concepto }}. Proporciona: 1) definición, 2) raíces etimológicas, 3) sinónimos, 4) antónimos, 5) contexto. Responde en JSON.\"}]}]}"
        },
        name: "Llamar Gemini",
        type: "n8n-nodes-base.httpRequest",
        typeVersion: 3,
        position: [350, 200],
        id: "gemini-node"
      },
      {
        parameters: {
          jsCode: "const concepto = $json.body?.concepto || \"CONCEPTO\";\nconst timestamp = new Date().toISOString();\n\nreturn {\n  concepto: concepto,\n  timestamp: timestamp,\n  es_maximo_relacional: true,\n  neo4j: $json || {},\n  gemini: $json || {},\n  sistema: \"YO Estructural v3.0 - Completo\"\n};"
        },
        name: "Combinar Resultados",
        type: "n8n-nodes-base.code",
        typeVersion: 1,
        position: [600, 120],
        id: "combine-node"
      },
      {
        parameters: {
          responseBody: "={{ JSON.stringify($json) }}"
        },
        name: "Retornar Respuesta",
        type: "n8n-nodes-base.respondToWebhook",
        typeVersion: 1,
        position: [800, 120],
        id: "response-node"
      }
    ],
    connections: {
      "Webhook Input": {
        main: [[{node: "Consultar Neo4j", type: "main", index: 0}]]
      },
      "Consultar Neo4j": {
        main: [[{node: "Llamar Gemini", type: "main", index: 0}]]
      },
      "Llamar Gemini": {
        main: [[{node: "Combinar Resultados", type: "main", index: 0}]]
      },
      "Combinar Resultados": {
        main: [[{node: "Retornar Respuesta", type: "main", index: 0}]]
      }
    }
  }' > /tmp/workflow_payload.json

echo "✓ JSON creado"

# Enviar a n8n
RESPONSE=$(curl -s -X POST "$BASE_URL/workflows" \
  -H "X-N8N-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d @/tmp/workflow_payload.json)

WORKFLOW_ID=$(echo "$RESPONSE" | jq -r '.id // empty')

if [ -z "$WORKFLOW_ID" ]; then
  echo "❌ Error al crear el workflow:"
  echo "$RESPONSE" | jq '.'
  exit 1
fi

echo "✅ Workflow creado: $WORKFLOW_ID"
echo ""

# Activar el workflow
echo "🔄 Activando workflow..."

ACTIVATE_RESPONSE=$(curl -s -X POST "$BASE_URL/workflows/$WORKFLOW_ID/activate" \
  -H "X-N8N-API-KEY: $API_KEY")

IS_ACTIVE=$(echo "$ACTIVATE_RESPONSE" | jq -r '.active // false')

if [ "$IS_ACTIVE" = "true" ]; then
  echo "✅ Workflow activado"
else
  echo "⚠️ No se pudo activar automáticamente, activar manualmente en la UI"
fi

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║ 🎉 WORKFLOW COMPLETADO EXITOSAMENTE 🎉        ║"
echo "╠════════════════════════════════════════════════╣"
echo "║ Workflow ID: $WORKFLOW_ID"
echo "║ Webhook: /webhook/yo-estructural-completo"
echo "║ URL: https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/yo-estructural-completo"
echo "║"
echo "║ 📝 TESTING:"
echo "║ curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/yo-estructural-completo \\"
echo "║   -H 'Content-Type: application/json' \\"
echo "║   -d '{\"concepto\": \"SOPORTE\"}'"
echo "╚════════════════════════════════════════════════╝"
echo ""
