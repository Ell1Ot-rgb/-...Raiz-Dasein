#!/bin/bash
# Script para probar la conectividad pública a n8n

URL="https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev"

echo "🧪 Probando acceso a n8n..."
echo "URL: $URL"
echo ""

# Probar desde dentro del Codespace
echo "📡 Probando desde Codespace (localhost)..."
if curl -s -o /dev/null -w "%{http_code}" http://localhost:5678 | grep -q "200\|401"; then
    echo "✅ n8n responde en localhost:5678"
else
    echo "❌ n8n NO responde en localhost:5678"
fi

echo ""
echo "📡 Probando URL pública..."
echo "   Intentando: $URL"
echo ""

RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$URL" 2>&1)

if echo "$RESPONSE" | grep -q "200\|401\|403"; then
    echo "✅✅✅ ¡ÉXITO! n8n es accesible públicamente"
    echo ""
    echo "🎉 Abre esta URL en tu navegador:"
    echo "   $URL"
    echo ""
    echo "🔐 Credenciales:"
    echo "   Usuario: admin"
    echo "   Password: fenomenologia2024"
    echo ""
    echo "📋 Workflow directo:"
    echo "   $URL/workflow/bRzrHvbsZ8H5fxcQ"
elif echo "$RESPONSE" | grep -q "404"; then
    echo "⚠️  El puerto está público pero n8n devuelve 404"
    echo "   Esto puede ser normal si intentas acceder a una ruta inexistente"
    echo "   Prueba la URL principal: $URL"
else
    echo "❌ n8n NO es accesible públicamente"
    echo "   Código HTTP: $RESPONSE"
    echo ""
    echo "🔧 SOLUCIÓN:"
    echo "   1. Ve al panel PORTS en la parte inferior de VS Code"
    echo "   2. Busca el puerto 5678"
    echo "   3. Clic derecho → Port Visibility → Public"
    echo ""
    echo "   Después de hacerlo público, ejecuta este script de nuevo:"
    echo "   ./probar_acceso_n8n.sh"
fi

echo ""
echo "════════════════════════════════════════════════════════════"
