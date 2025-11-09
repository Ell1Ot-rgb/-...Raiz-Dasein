#!/usr/bin/env python3
"""
Script para configurar credenciales en n8n automáticamente
"""
import requests
import json
import os
from base64 import b64encode

# Configuración
N8N_URL = "http://localhost:5678"
N8N_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhYWY1NGI2ZS0wNmM3LTRiNTEtYjI3Mi04NTlkNDA2NzBhYTYiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzYyNDYxNzUxfQ.-xCWquOwqPLbnFvl02yiSLv2pWO_jDnO86SaaiEnBlw"

# Credenciales
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "fenomenologia2024"
GEMINI_API_KEY = "AIzaSyAtgpP05qWmGW6dUZnYBW96K3U-gLiV5Kc"

headers = {
    "X-N8N-API-KEY": N8N_API_KEY,
    "Content-Type": "application/json"
}

def crear_credencial_neo4j():
    """Crea credencial HTTP Basic Auth para Neo4j"""
    credential = {
        "name": "Neo4j Basic Auth",
        "type": "httpBasicAuth",
        "data": {
            "user": NEO4J_USER,
            "password": NEO4J_PASSWORD
        }
    }
    
    try:
        response = requests.post(
            f"{N8N_URL}/api/v1/credentials",
            headers=headers,
            json=credential
        )
        
        if response.status_code in [200, 201]:
            data = response.json()
            print(f"✅ Credencial Neo4j creada con ID: {data.get('id')}")
            return data.get('id')
        else:
            print(f"❌ Error creando credencial Neo4j: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def crear_credencial_gemini():
    """Crea credencial Header Auth para Gemini (como query param)"""
    credential = {
        "name": "Gemini API Key",
        "type": "httpQueryAuth",
        "data": {
            "name": "key",
            "value": GEMINI_API_KEY
        }
    }
    
    try:
        response = requests.post(
            f"{N8N_URL}/api/v1/credentials",
            headers=headers,
            json=credential
        )
        
        if response.status_code in [200, 201]:
            data = response.json()
            print(f"✅ Credencial Gemini creada con ID: {data.get('id')}")
            return data.get('id')
        else:
            print(f"❌ Error creando credencial Gemini: {response.status_code}")
            print(f"   Respuesta: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def listar_credenciales():
    """Lista todas las credenciales existentes"""
    try:
        response = requests.get(
            f"{N8N_URL}/api/v1/credentials",
            headers=headers
        )
        
        if response.status_code == 200:
            credentials = response.json()
            print(f"\n📋 Credenciales existentes ({len(credentials.get('data', []))} total):")
            for cred in credentials.get('data', []):
                print(f"   - {cred.get('name')} (ID: {cred.get('id')}, Tipo: {cred.get('type')})")
            return credentials.get('data', [])
        else:
            print(f"❌ Error listando credenciales: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def main():
    print("🔧 Configurando credenciales en n8n...\n")
    
    # Listar credenciales existentes
    existing = listar_credenciales()
    
    # Verificar si ya existen
    neo4j_exists = any(c.get('name') == 'Neo4j Basic Auth' for c in existing)
    gemini_exists = any(c.get('name') == 'Gemini API Key' for c in existing)
    
    print()
    
    # Crear credenciales si no existen
    if not neo4j_exists:
        print("📝 Creando credencial Neo4j...")
        neo4j_id = crear_credencial_neo4j()
    else:
        print("ℹ️  Credencial Neo4j ya existe")
    
    if not gemini_exists:
        print("📝 Creando credencial Gemini...")
        gemini_id = crear_credencial_gemini()
    else:
        print("ℹ️  Credencial Gemini ya existe")
    
    print("\n" + "="*60)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("="*60)
    print("\n📌 Próximos pasos:")
    print("1. Abre n8n: https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/workflow/fGVYk91OaTo9DAti")
    print("2. Haz clic en el nodo 'Neo4j Guardar'")
    print("3. En 'Credential for Basic Auth', selecciona 'Neo4j Basic Auth'")
    print("4. Haz clic en el nodo 'Gemini API'")
    print("5. En 'Credential for Query Auth', selecciona 'Gemini API Key'")
    print("6. Activa el workflow (switch arriba a la derecha)")
    print("7. Prueba con:")
    print("   curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/generar-maximo \\")
    print("     -H 'Content-Type: application/json' \\")
    print("     -d '{\"concepto\": \"SOPORTE\"}'")

if __name__ == "__main__":
    main()
