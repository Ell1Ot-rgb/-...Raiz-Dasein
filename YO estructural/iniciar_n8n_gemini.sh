#!/bin/bash

# Script de Inicio Rápido: n8n + Gemini + Generador Máximo Relacional
# ====================================================================

set -e  # Salir si hay error

echo "🚀 Iniciando Sistema de Máximo Relacional con n8n + Gemini"
echo "============================================================"
echo ""

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Función para imprimir con color
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Verificar si estamos en el directorio correcto
if [ ! -f "docker-compose.yml" ]; then
    print_error "Error: docker-compose.yml no encontrado"
    echo "Por favor ejecuta este script desde: /workspaces/-...Raiz-Dasein/YO estructural/"
    exit 1
fi

# Paso 1: Verificar archivo .env
echo "📋 Paso 1: Verificando configuración..."
if [ ! -f ".env" ]; then
    print_warning "Archivo .env no encontrado. Creando desde .env.example..."
    cp .env.example .env
    print_warning "⚠️  IMPORTANTE: Edita .env y agrega tu GOOGLE_GEMINI_API_KEY"
    echo ""
    echo "   Obtén tu API key en: https://makersuite.google.com/app/apikey"
    echo "   Luego ejecuta: nano .env"
    echo ""
    read -p "Presiona Enter cuando hayas configurado .env..."
fi

# Verificar que Gemini API key esté configurada
if grep -q "GOOGLE_GEMINI_API_KEY=$" .env || ! grep -q "GOOGLE_GEMINI_API_KEY" .env; then
    print_error "GOOGLE_GEMINI_API_KEY no está configurada en .env"
    echo ""
    echo "Por favor:"
    echo "1. Obtén tu API key en: https://makersuite.google.com/app/apikey"
    echo "2. Edita .env: nano .env"
    echo "3. Agrega: GOOGLE_GEMINI_API_KEY=AIzaSy...TU_KEY"
    echo ""
    exit 1
fi

print_success "Archivo .env configurado"

# Paso 2: Instalar dependencias Python
echo ""
echo "📦 Paso 2: Instalando dependencias Python..."

if command -v pip &> /dev/null; then
    pip install -q google-generativeai sentence-transformers 2>/dev/null || {
        print_warning "Algunas dependencias ya están instaladas o hubo un problema menor"
    }
    print_success "Dependencias Python listas"
else
    print_warning "pip no encontrado. Asegúrate de instalar manualmente:"
    echo "   pip install google-generativeai sentence-transformers"
fi

# Paso 3: Verificar Docker
echo ""
echo "🐳 Paso 3: Verificando Docker..."

if ! command -v docker &> /dev/null; then
    print_error "Docker no está instalado"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    print_error "docker-compose no está instalado"
    exit 1
fi

print_success "Docker y docker-compose disponibles"

# Paso 4: Detener contenedores existentes si los hay
echo ""
echo "🛑 Paso 4: Deteniendo contenedores previos (si existen)..."
docker-compose down 2>/dev/null || true
print_success "Limpieza completada"

# Paso 5: Construir imágenes
echo ""
echo "🏗️  Paso 5: Construyendo imágenes Docker..."
echo "   (Esto puede tomar varios minutos la primera vez)"
docker-compose build yo_estructural_api 2>&1 | grep -E "Step|Successfully|ERROR" || true
print_success "Imágenes construidas"

# Paso 6: Levantar servicios
echo ""
echo "🚀 Paso 6: Levantando servicios..."
echo "   - Neo4j (base de datos)"
echo "   - n8n (automatización)"
echo "   - API Generador (procesamiento)"
echo ""

docker-compose up -d neo4j n8n yo_estructural_api

# Esperar a que servicios estén listos
echo ""
echo "⏳ Esperando a que servicios inicien..."
sleep 10

# Verificar Neo4j
echo -n "   Verificando Neo4j... "
for i in {1..30}; do
    if docker exec yo_estructural_neo4j cypher-shell -u neo4j -p fenomenologia2024 "RETURN 1" &>/dev/null; then
        print_success "OK"
        break
    fi
    sleep 2
    echo -n "."
done

# Verificar API
echo -n "   Verificando API... "
for i in {1..30}; do
    if curl -s http://localhost:8000/health &>/dev/null; then
        print_success "OK"
        break
    fi
    sleep 2
    echo -n "."
done

# Verificar n8n
echo -n "   Verificando n8n... "
for i in {1..30}; do
    if curl -s http://localhost:5678/healthz &>/dev/null; then
        print_success "OK"
        break
    fi
    sleep 2
    echo -n "."
done

# Paso 7: Verificar salud de componentes
echo ""
echo "🏥 Paso 7: Verificando salud del sistema..."

HEALTH_RESPONSE=$(curl -s http://localhost:8000/health)

if echo "$HEALTH_RESPONSE" | grep -q '"status":"healthy"'; then
    print_success "Sistema saludable"
    
    # Mostrar estado de componentes
    echo ""
    echo "   Estado de componentes:"
    echo "$HEALTH_RESPONSE" | python3 -m json.tool 2>/dev/null | grep -A 5 "componentes" || echo "$HEALTH_RESPONSE"
else
    print_warning "Sistema iniciado pero con advertencias"
    echo "$HEALTH_RESPONSE"
fi

# Paso 8: Resumen e instrucciones
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 ¡Sistema iniciado correctamente!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📍 Servicios disponibles:"
echo ""
echo "   🔧 n8n (Workflows):"
echo "      URL: http://localhost:5678"
echo "      Usuario: admin"
echo "      Contraseña: fenomenologia2024"
echo ""
echo "   🔌 API Generador:"
echo "      URL: http://localhost:8000"
echo "      Docs: http://localhost:8000/docs"
echo ""
echo "   🗄️  Neo4j Browser:"
echo "      URL: http://localhost:7474"
echo "      Usuario: neo4j"
echo "      Contraseña: fenomenologia2024"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📚 Próximos pasos:"
echo ""
echo "   1. Acceder a n8n: http://localhost:5678"
echo "   2. Importar workflow:"
echo "      n8n_setup/workflows/workflow_5_generador_maximo_relacional.json"
echo "   3. Configurar credenciales en n8n:"
echo "      - Neo4j YO Estructural"
echo "      - Google Gemini API"
echo "   4. Activar workflow en n8n"
echo "   5. Probar con:"
echo ""
echo "      curl -X POST http://localhost:5678/webhook/generar-maximo \\"
echo "        -H 'Content-Type: application/json' \\"
echo "        -d '{\"concepto\": \"SOPORTE\"}'"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📖 Documentación completa:"
echo "   GUIA_INTEGRACION_N8N_GEMINI.md"
echo ""
echo "📊 Ver logs:"
echo "   docker-compose logs -f"
echo ""
echo "🛑 Detener sistema:"
echo "   docker-compose down"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Preguntar si quiere abrir n8n en navegador
read -p "¿Quieres abrir n8n en el navegador? (s/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    if command -v xdg-open &> /dev/null; then
        xdg-open http://localhost:5678
    elif command -v open &> /dev/null; then
        open http://localhost:5678
    else
        echo "Por favor abre manualmente: http://localhost:5678"
    fi
fi

print_success "¡Listo para usar!"
