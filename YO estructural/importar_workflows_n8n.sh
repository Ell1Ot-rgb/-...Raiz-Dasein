#!/bin/bash

# Script para importar workflows a n8n automáticamente
# Usa la API de n8n con autenticación básica

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔄 IMPORTADOR AUTOMÁTICO DE WORKFLOWS N8N"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

N8N_URL="http://localhost:5678"
N8N_API_KEY="${N8N_API_KEY:-}"
WORKFLOW_FILE="n8n_setup/workflows/workflow_5_generador_maximo_relacional.json"

# Cargar variables de entorno
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Función para importar workflow
import_workflow() {
    local workflow_json=$(cat "$WORKFLOW_FILE")
    
    echo "📂 Leyendo workflow: $WORKFLOW_FILE"
    
    # Extraer información del workflow
    local workflow_name=$(echo "$workflow_json" | python3 -c "import sys, json; print(json.load(sys.stdin).get('name', 'Workflow Importado'))")
    
    echo "📝 Nombre del workflow: $workflow_name"
    echo ""
    echo "🔄 Importando a n8n..."
    
    # Importar workflow usando la API de n8n con API Key
    response=$(curl -s -w "\n%{http_code}" \
        -X POST "$N8N_URL/api/v1/workflows" \
        -H "X-N8N-API-KEY: $N8N_API_KEY" \
        -H "Content-Type: application/json" \
        -d "$workflow_json")
    
    http_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n-1)
    
    if [ "$http_code" = "200" ] || [ "$http_code" = "201" ]; then
        echo "✅ Workflow importado exitosamente!"
        echo ""
        workflow_id=$(echo "$body" | python3 -c "import sys, json; print(json.load(sys.stdin).get('id', 'N/A'))" 2>/dev/null || echo "N/A")
        echo "   ID del workflow: $workflow_id"
        echo ""
    else
        echo "⚠️  Respuesta HTTP: $http_code"
        echo ""
        
        # Verificar si es porque ya existe
        if echo "$body" | grep -q "already exists" || echo "$body" | grep -q "duplicate"; then
            echo "ℹ️  El workflow ya existe en n8n"
            echo ""
            echo "   Opciones:"
            echo "   1. Usa el workflow existente"
            echo "   2. Elimínalo desde n8n UI y vuelve a importar"
            echo ""
        else
            echo "❌ Error al importar:"
            echo "$body" | python3 -m json.tool 2>/dev/null || echo "$body"
            echo ""
        fi
    fi
}

# Verificar que n8n esté corriendo
echo "🔍 Verificando que n8n esté disponible..."
if ! curl -s -f -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_URL/api/v1/workflows" > /dev/null 2>&1; then
    echo "⚠️  n8n API no responde. Verificando con curl básico..."
    if ! curl -s -f "$N8N_URL" > /dev/null 2>&1; then
        echo "❌ n8n no está disponible en $N8N_URL"
        echo "   Asegúrate de que el contenedor esté corriendo:"
        echo "   docker ps | grep n8n"
        exit 1
    fi
fi

echo "✅ n8n está disponible"
echo ""

# Verificar que el archivo de workflow existe
if [ ! -f "$WORKFLOW_FILE" ]; then
    echo "❌ Archivo de workflow no encontrado: $WORKFLOW_FILE"
    exit 1
fi

# Importar workflow
import_workflow

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 PRÓXIMOS PASOS:"
echo ""
echo "1. Abre n8n: https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev"
echo ""
echo "2. Ve a 'Workflows' y busca: 'Generador Máximo Relacional + Gemini'"
echo ""
echo "3. Configura las credenciales en los nodos:"
echo "   • Nodo 'Neo4j: Guardar Máximo' → Credencial Neo4j"
echo "   • Nodo 'Gemini: Analizar Convergencia' → Credencial Gemini"
echo ""
echo "4. Activa el workflow (switch arriba a la derecha)"
echo ""
echo "5. Prueba con:"
echo "   curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/generar-maximo \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"concepto\": \"SOPORTE\"}'"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
