#!/bin/bash
# Script de inicio para el servicio de automatización YO Estructural
# ==================================================================

set -e

echo "[$(date)] Iniciando servicio de automatización YO Estructural..."

# Verificar variables de entorno críticas
required_vars=("NEO4J_URI" "SUPABASE_URL" "N8N_WEBHOOK_URL")
for var in "${required_vars[@]}"; do
    if [ -z "${!var}" ]; then
        echo "[$(date)] ERROR: Variable de entorno $var no está configurada"
        exit 1
    fi
done

echo "[$(date)] Variables de entorno verificadas"

# Crear directorios si no existen
mkdir -p logs_sistema procesado entrada_bruta

# Verificar conectividad con servicios externos
echo "[$(date)] Verificando conectividad..."

# Verificar Neo4j
echo "[$(date)] Verificando conexión a Neo4j..."
python3 -c "
import os
from neo4j import GraphDatabase
try:
    driver = GraphDatabase.driver(os.getenv('NEO4J_URI'), auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASSWORD')))
    with driver.session() as session:
        result = session.run('RETURN 1')
        print('[{}] Neo4j: Conexión exitosa'.format('$(date)'))
    driver.close()
except Exception as e:
    print('[{}] Neo4j: Error de conexión - {}'.format('$(date)', str(e)))
    exit(1)
"

# Verificar Supabase
echo "[$(date)] Verificando conexión a Supabase..."
python3 -c "
import os
import requests
try:
    url = os.getenv('SUPABASE_URL')
    headers = {'apikey': os.getenv('SUPABASE_KEY')}
    response = requests.get(f'{url}/rest/v1/', headers=headers, timeout=10)
    if response.status_code == 200:
        print('[{}] Supabase: Conexión exitosa'.format('$(date)'))
    else:
        print('[{}] Supabase: Error HTTP {}'.format('$(date)', response.status_code))
        exit(1)
except Exception as e:
    print('[{}] Supabase: Error de conexión - {}'.format('$(date)', str(e)))
    exit(1)
"

# Verificar n8n
echo "[$(date)] Verificando conexión a n8n..."
python3 -c "
import os
import requests
try:
    webhook_url = os.getenv('N8N_WEBHOOK_URL')
    # Solo verificar que la URL sea accesible
    response = requests.get(webhook_url.replace('/webhook/', '/healthz'), timeout=10)
    print('[{}] n8n: Servicio accesible'.format('$(date)'))
except Exception as e:
    print('[{}] n8n: Advertencia - {}'.format('$(date)', str(e)))
    # No salir con error, n8n puede estar configurado diferente
"

echo "[$(date)] Verificaciones completadas"

# Función para manejar señales
cleanup() {
    echo "[$(date)] Recibida señal de terminación, cerrando servicios..."
    if [ ! -z "$AUTOMATION_PID" ]; then
        kill $AUTOMATION_PID 2>/dev/null || true
        wait $AUTOMATION_PID 2>/dev/null || true
    fi
    echo "[$(date)] Servicios cerrados correctamente"
    exit 0
}

# Configurar manejo de señales
trap cleanup SIGTERM SIGINT

# Iniciar el servicio de automatización
echo "[$(date)] Iniciando automatización completa..."
python3 automatizacion_completa.py &
AUTOMATION_PID=$!

echo "[$(date)] Servicio de automatización iniciado (PID: $AUTOMATION_PID)"
echo "[$(date)] Logs disponibles en logs_sistema/automatizacion_completa.log"

# Monitorear el proceso
while true; do
    if ! kill -0 $AUTOMATION_PID 2>/dev/null; then
        echo "[$(date)] ERROR: El proceso de automatización ha terminado inesperadamente"
        echo "[$(date)] Reiniciando en 10 segundos..."
        sleep 10
        
        # Reiniciar el proceso
        python3 automatizacion_completa.py &
        AUTOMATION_PID=$!
        echo "[$(date)] Proceso reiniciado (PID: $AUTOMATION_PID)"
    fi
    
    sleep 30  # Verificar cada 30 segundos
done