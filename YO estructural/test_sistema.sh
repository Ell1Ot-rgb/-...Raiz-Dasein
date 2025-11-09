#!/bin/bash
# Script de prueba del sistema n8n + Gemini + Neo4j

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🧪 PRUEBA DEL SISTEMA COMPLETO"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 1. Verificar que los contenedores estén corriendo
echo "1️⃣ Verificando contenedores..."
echo ""
docker ps --format "table {{.Names}}\t{{.Status}}" | grep -E "yo_estructural"
echo ""

# 2. Probar Neo4j
echo "2️⃣ Probando conexión a Neo4j..."
echo ""
docker exec yo_estructural_neo4j cypher-shell -u neo4j -p fenomenologia2024 "RETURN 'Neo4j OK' as status" 2>/dev/null || echo "❌ Error en Neo4j"
echo ""

# 3. Probar n8n
echo "3️⃣ Probando n8n..."
echo ""
curl -s -o /dev/null -w "Status: %{http_code}\n" http://localhost:5678
echo ""

# 4. Probar API
echo "4️⃣ Probando API YO Estructural..."
echo ""
curl -s http://localhost:8000/health | python3 -m json.tool 2>/dev/null || echo "⚠️ API no responde correctamente"
echo ""

# 5. Obtener URL del webhook de n8n
echo "5️⃣ URL del webhook n8n:"
echo ""
echo "https://${CODESPACE_NAME}-5678.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}/webhook/generar-maximo"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 COMANDO DE PRUEBA:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "curl -X POST https://${CODESPACE_NAME}-5678.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}/webhook/generar-maximo \\"
echo "  -H \"Content-Type: application/json\" \\"
echo "  -d '{\"concepto\": \"SOPORTE\"}'"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 NOTAS:"
echo "   • Asegúrate de haber importado el workflow en n8n"
echo "   • Verifica que las credenciales estén configuradas"
echo "   • El workflow debe estar ACTIVO (switch verde)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
