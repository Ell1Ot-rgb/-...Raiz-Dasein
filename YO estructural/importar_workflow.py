#!/usr/bin/env python3
"""
Script para importar workflows a n8n usando la API
Limpia el JSON y envía solo los campos permitidos
"""

import json
import requests
import os
import sys

# Configuración
N8N_URL = "http://localhost:5678"
N8N_API_KEY = os.getenv("N8N_API_KEY")
WORKFLOW_FILE = "n8n_setup/workflows/workflow_5_generador_maximo_relacional.json"

def clean_workflow_json(workflow_data):
    """
    Limpia el JSON del workflow para que solo tenga los campos permitidos por la API
    """
    # Campos permitidos por la API de n8n
    allowed_fields = {
        "name", "nodes", "connections", "active", "settings", 
        "staticData", "tags", "pinData", "versionId"
    }
    
    # Crear nuevo diccionario solo con campos permitidos
    cleaned = {k: v for k, v in workflow_data.items() if k in allowed_fields}
    
    # Asegurar que active sea False inicialmente
    cleaned["active"] = False
    
    return cleaned

def import_workflow():
    """Importa el workflow a n8n"""
    
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🔄 IMPORTADOR AUTOMÁTICO DE WORKFLOWS N8N")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()
    
    # Verificar API key
    if not N8N_API_KEY:
        print("❌ Error: N8N_API_KEY no está configurada")
        print("   Ejecuta: export N8N_API_KEY='tu-api-key'")
        return False
    
    # Leer workflow
    print(f"📂 Leyendo workflow: {WORKFLOW_FILE}")
    try:
        with open(WORKFLOW_FILE, 'r', encoding='utf-8') as f:
            workflow_data = json.load(f)
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {WORKFLOW_FILE}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error parseando JSON: {e}")
        return False
    
    workflow_name = workflow_data.get("name", "Workflow Importado")
    print(f"📝 Nombre del workflow: {workflow_name}")
    print()
    
    # Limpiar JSON
    print("🧹 Limpiando JSON para la API...")
    cleaned_workflow = clean_workflow_json(workflow_data)
    
    # Importar a n8n
    print("🔄 Importando a n8n...")
    headers = {
        "X-N8N-API-KEY": N8N_API_KEY,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(
            f"{N8N_URL}/api/v1/workflows",
            headers=headers,
            json=cleaned_workflow,
            timeout=30
        )
        
        if response.status_code in [200, 201]:
            print("✅ Workflow importado exitosamente!")
            print()
            result = response.json()
            workflow_id = result.get("id", "N/A")
            print(f"   ID del workflow: {workflow_id}")
            print()
            
            # Ahora activar el workflow
            print("🔄 Activando workflow...")
            activate_response = requests.patch(
                f"{N8N_URL}/api/v1/workflows/{workflow_id}",
                headers=headers,
                json={"active": True},
                timeout=30
            )
            
            if activate_response.status_code == 200:
                print("✅ Workflow activado correctamente!")
                print()
                print(f"🌐 Webhook disponible en:")
                print(f"   https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/generar-maximo")
            else:
                print(f"⚠️  No se pudo activar automáticamente (status {activate_response.status_code})")
                print("   Actívalo manualmente desde la UI de n8n")
            
            print()
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("🎉 IMPORTACIÓN COMPLETADA")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print()
            print("📋 PRÓXIMOS PASOS:")
            print()
            print("1. Abre n8n: https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev")
            print()
            print("2. Ve a 'Workflows' y abre el workflow importado")
            print()
            print("3. Configura las credenciales en los nodos:")
            print("   • Nodo 'Neo4j: Guardar Máximo' → Credencial Neo4j")
            print("   • Nodo 'Gemini: Analizar Convergencia' → Credencial Gemini")
            print("   • Nodo 'Neo4j: Conectar Similares' → Credencial Neo4j")
            print()
            print("4. Si no está activo, actívalo con el switch arriba")
            print()
            print("5. Prueba con:")
            print("   curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/generar-maximo \\")
            print("     -H 'Content-Type: application/json' \\")
            print("     -d '{\"concepto\": \"SOPORTE\"}'")
            print()
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            
            return True
            
        elif response.status_code == 409:
            print("ℹ️  El workflow ya existe en n8n")
            print()
            print("   Opciones:")
            print("   1. Usa el workflow existente en n8n")
            print("   2. Elimínalo desde n8n UI y vuelve a ejecutar este script")
            print("   3. Renómbralo en el JSON y vuelve a importar")
            return False
            
        else:
            print(f"⚠️  Respuesta HTTP: {response.status_code}")
            print()
            print("❌ Error al importar:")
            try:
                error_data = response.json()
                print(json.dumps(error_data, indent=2))
            except:
                print(response.text)
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        print()
        print("   Verifica que n8n esté corriendo:")
        print("   docker ps | grep n8n")
        return False

if __name__ == "__main__":
    success = import_workflow()
    sys.exit(0 if success else 1)
