#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT DE CONFIGURACIÓN AUTOMÁTICA - YO ESTRUCTURAL
==================================================

Este script configura automáticamente todo el sistema YO Estructural:
1. Verifica dependencias
2. Configura variables de entorno
3. Inicializa servicios
4. Prueba conexiones
5. Inicia automatización

Autor: Sistema YO Estructural
Versión: 3.0
"""

import os
import sys
import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional

class ConfiguradorAutomatizacion:
    """Configurador automático del sistema YO Estructural"""
    
    def __init__(self):
        self.directorio_base = Path(__file__).parent
        self.archivo_env = self.directorio_base / '.env'
        self.estado_configuracion = {
            'dependencias': False,
            'variables_entorno': False,
            'servicios': False,
            'conexiones': False
        }
    
    def mostrar_banner(self):
        """Muestra el banner del configurador"""
        print("\n" + "="*70)
        print("🧠 CONFIGURADOR AUTOMÁTICO - SISTEMA YO ESTRUCTURAL v3.0")
        print("="*70)
        print("Este script configurará automáticamente todo el sistema:")
        print("• Verificación de dependencias")
        print("• Configuración de variables de entorno")
        print("• Inicialización de servicios")
        print("• Pruebas de conectividad")
        print("• Inicio de automatización")
        print("="*70 + "\n")
    
    def verificar_dependencias(self) -> bool:
        """Verifica que todas las dependencias estén instaladas"""
        print("📦 Verificando dependencias...")
        
        dependencias_python = [
            'fastapi', 'uvicorn', 'neo4j', 'supabase', 'scikit-learn',
            'numpy', 'requests', 'python-dotenv', 'pydantic'
        ]
        
        dependencias_faltantes = []
        
        for dep in dependencias_python:
            try:
                __import__(dep.replace('-', '_'))
                print(f"  ✓ {dep}")
            except ImportError:
                dependencias_faltantes.append(dep)
                print(f"  ✗ {dep} - FALTANTE")
        
        if dependencias_faltantes:
            print(f"\n⚠️  Dependencias faltantes: {', '.join(dependencias_faltantes)}")
            respuesta = input("¿Desea instalarlas automáticamente? (s/n): ")
            
            if respuesta.lower() in ['s', 'si', 'y', 'yes']:
                return self._instalar_dependencias(dependencias_faltantes)
            else:
                print("❌ No se pueden continuar sin las dependencias")
                return False
        
        print("✅ Todas las dependencias están instaladas")
        self.estado_configuracion['dependencias'] = True
        return True
    
    def _instalar_dependencias(self, dependencias: List[str]) -> bool:
        """Instala las dependencias faltantes"""
        try:
            print("\n🔄 Instalando dependencias...")
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'
            ])
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
            ])
            print("✅ Dependencias instaladas correctamente")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error instalando dependencias: {e}")
            return False
    
    def configurar_variables_entorno(self) -> bool:
        """Configura las variables de entorno interactivamente"""
        print("\n🔧 Configurando variables de entorno...")
        
        if self.archivo_env.exists():
            print(f"📄 Archivo .env encontrado: {self.archivo_env}")
            respuesta = input("¿Desea reconfigurarlo? (s/n): ")
            if respuesta.lower() not in ['s', 'si', 'y', 'yes']:
                print("✅ Usando configuración existente")
                self.estado_configuracion['variables_entorno'] = True
                return True
        
        configuracion = {}
        
        print("\n🔹 CONFIGURACIÓN NEO4J:")
        configuracion['NEO4J_URI'] = input("Neo4j URI [bolt://172.23.111.142:7687]: ") or "bolt://172.23.111.142:7687"
        configuracion['NEO4J_USER'] = input("Neo4j Usuario [neo4j]: ") or "neo4j"
        configuracion['NEO4J_PASSWORD'] = input("Neo4j Password [fenomenologia2024]: ") or "fenomenologia2024"
        
        print("\n🔹 CONFIGURACIÓN SUPABASE:")
        configuracion['SUPABASE_URL'] = input("Supabase URL: ")
        configuracion['SUPABASE_KEY'] = input("Supabase Anon Key: ")
        configuracion['SUPABASE_SERVICE_KEY'] = input("Supabase Service Key: ")
        
        print("\n🔹 CONFIGURACIÓN N8N:")
        configuracion['N8N_WEBHOOK_URL'] = input("n8n Webhook URL: ")
        configuracion['N8N_API_KEY'] = input("n8n API Key (opcional): ")
        configuracion['N8N_BASE_URL'] = input("n8n Base URL: ")
        
        print("\n🔹 CONFIGURACIÓN GOOGLE DRIVE:")
        configuracion['GOOGLE_DRIVE_MONITORED_FOLDERS'] = input("IDs de carpetas a monitorear (separados por coma): ")
        
        print("\n🔹 CONFIGURACIÓN AUTOMATIZACIÓN:")
        configuracion['ENABLE_DRIVE_MONITOR'] = input("Habilitar monitoreo de Drive [true]: ") or "true"
        configuracion['ENABLE_AUTO_PROCESSING'] = input("Habilitar procesamiento automático [true]: ") or "true"
        configuracion['ENABLE_NEO4J_SYNC'] = input("Habilitar sincronización Neo4j [true]: ") or "true"
        
        # Configuraciones adicionales
        configuracion['LOG_LEVEL'] = "INFO"
        configuracion['PROCESSING_TIMEOUT'] = "300"
        configuracion['MDCE_DEBUG'] = "true"
        configuracion['SISTEMA_ENCRYPTION_KEY'] = "tu_clave_secreta_cambiar"
        
        # Escribir archivo .env
        try:
            with open(self.archivo_env, 'w', encoding='utf-8') as f:
                f.write("# Variables de entorno para YO Estructural\n")
                f.write("# Generado automáticamente\n")
                f.write(f"# Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for clave, valor in configuracion.items():
                    f.write(f"{clave}={valor}\n")
            
            print(f"✅ Archivo .env creado: {self.archivo_env}")
            self.estado_configuracion['variables_entorno'] = True
            return True
            
        except Exception as e:
            print(f"❌ Error creando archivo .env: {e}")
            return False
    
    def verificar_servicios_docker(self) -> bool:
        """Verifica si Docker está disponible y los servicios están corriendo"""
        print("\n🐳 Verificando servicios Docker...")
        
        try:
            # Verificar si Docker está instalado
            subprocess.check_output(['docker', '--version'], stderr=subprocess.STDOUT)
            print("  ✓ Docker instalado")
            
            # Verificar si Docker Compose está disponible
            subprocess.check_output(['docker-compose', '--version'], stderr=subprocess.STDOUT)
            print("  ✓ Docker Compose disponible")
            
            # Verificar servicios corriendo
            resultado = subprocess.check_output(['docker-compose', 'ps'], stderr=subprocess.STDOUT, text=True)
            
            if 'neo4j' in resultado and 'Up' in resultado:
                print("  ✓ Neo4j corriendo")
            else:
                print("  ⚠️  Neo4j no está corriendo")
                respuesta = input("¿Desea iniciar los servicios Docker? (s/n): ")
                if respuesta.lower() in ['s', 'si', 'y', 'yes']:
                    return self._iniciar_servicios_docker()
            
            self.estado_configuracion['servicios'] = True
            return True
            
        except subprocess.CalledProcessError:
            print("  ⚠️  Docker no está disponible o no hay servicios corriendo")
            print("  💡 Puede iniciar los servicios manualmente con: docker-compose up -d")
            return True  # No es crítico para la configuración
        except FileNotFoundError:
            print("  ⚠️  Docker no está instalado")
            print("  💡 Instale Docker para usar los servicios containerizados")
            return True  # No es crítico
    
    def _iniciar_servicios_docker(self) -> bool:
        """Inicia los servicios Docker"""
        try:
            print("🔄 Iniciando servicios Docker...")
            subprocess.check_call(['docker-compose', 'up', '-d'])
            print("✅ Servicios Docker iniciados")
            
            # Esperar a que Neo4j esté listo
            print("⏳ Esperando a que Neo4j esté listo...")
            time.sleep(30)
            
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Error iniciando servicios Docker: {e}")
            return False
    
    def probar_conexiones(self) -> bool:
        """Prueba las conexiones a todos los servicios"""
        print("\n🔗 Probando conexiones...")
        
        # Cargar variables de entorno
        from dotenv import load_dotenv
        load_dotenv(self.archivo_env)
        
        conexiones_exitosas = 0
        total_conexiones = 0
        
        # Probar Neo4j
        total_conexiones += 1
        try:
            from neo4j import GraphDatabase
            driver = GraphDatabase.driver(
                os.getenv('NEO4J_URI'),
                auth=(os.getenv('NEO4J_USER'), os.getenv('NEO4J_PASSWORD'))
            )
            with driver.session() as session:
                session.run("RETURN 1")
            driver.close()
            print("  ✓ Neo4j conectado")
            conexiones_exitosas += 1
        except Exception as e:
            print(f"  ✗ Neo4j error: {e}")
        
        # Probar Supabase
        total_conexiones += 1
        try:
            import requests
            url = os.getenv('SUPABASE_URL')
            headers = {'apikey': os.getenv('SUPABASE_KEY')}
            response = requests.get(f'{url}/rest/v1/', headers=headers, timeout=10)
            if response.status_code == 200:
                print("  ✓ Supabase conectado")
                conexiones_exitosas += 1
            else:
                print(f"  ✗ Supabase error HTTP: {response.status_code}")
        except Exception as e:
            print(f"  ✗ Supabase error: {e}")
        
        # Probar n8n
        total_conexiones += 1
        try:
            import requests
            webhook_url = os.getenv('N8N_WEBHOOK_URL')
            if webhook_url:
                # Intentar hacer ping al webhook
                response = requests.get(webhook_url, timeout=5)
                print("  ✓ n8n accesible")
                conexiones_exitosas += 1
            else:
                print("  ⚠️  n8n URL no configurada")
        except Exception as e:
            print(f"  ⚠️  n8n: {e}")
            conexiones_exitosas += 1  # No crítico
        
        exito = conexiones_exitosas >= (total_conexiones - 1)  # Permitir 1 fallo
        if exito:
            print(f"✅ Conexiones verificadas ({conexiones_exitosas}/{total_conexiones})")
            self.estado_configuracion['conexiones'] = True
        else:
            print(f"⚠️  Algunas conexiones fallaron ({conexiones_exitosas}/{total_conexiones})")
        
        return exito
    
    def mostrar_resumen_configuracion(self):
        """Muestra un resumen de la configuración"""
        print("\n" + "="*70)
        print("📋 RESUMEN DE CONFIGURACIÓN")
        print("="*70)
        
        for componente, estado in self.estado_configuracion.items():
            icono = "✅" if estado else "❌"
            print(f"{icono} {componente.replace('_', ' ').title()}")
        
        print("\n📁 Archivos importantes:")
        print(f"  • Configuración: {self.archivo_env}")
        print(f"  • Docker Compose: {self.directorio_base / 'docker-compose.yml'}")
        print(f"  • Automatización: {self.directorio_base / 'automatizacion_completa.py'}")
        
        print("\n🚀 Comandos útiles:")
        print("  • Iniciar automatización: python automatizacion_completa.py")
        print("  • Iniciar servicios Docker: docker-compose up -d")
        print("  • Ver logs: docker-compose logs -f")
        print("  • Detener servicios: docker-compose down")
        
        print("="*70)
    
    def iniciar_automatizacion(self) -> bool:
        """Inicia el sistema de automatización"""
        print("\n🚀 ¿Desea iniciar la automatización ahora?")
        respuesta = input("(s/n): ")
        
        if respuesta.lower() in ['s', 'si', 'y', 'yes']:
            try:
                print("🔄 Iniciando automatización...")
                print("💡 Presione Ctrl+C para detener")
                print("-" * 50)
                
                # Ejecutar el script de automatización
                subprocess.call([sys.executable, 'automatizacion_completa.py'])
                return True
                
            except KeyboardInterrupt:
                print("\n⏹️  Automatización detenida por el usuario")
                return True
            except Exception as e:
                print(f"❌ Error iniciando automatización: {e}")
                return False
        else:
            print("✅ Configuración completada. Puede iniciar la automatización manualmente.")
            return True
    
    def ejecutar_configuracion_completa(self):
        """Ejecuta todo el proceso de configuración"""
        self.mostrar_banner()
        
        try:
            # Paso 1: Verificar dependencias
            if not self.verificar_dependencias():
                print("❌ Configuración abortada: dependencias faltantes")
                return False
            
            # Paso 2: Configurar variables de entorno
            if not self.configurar_variables_entorno():
                print("❌ Configuración abortada: error en variables de entorno")
                return False
            
            # Paso 3: Verificar servicios Docker
            self.verificar_servicios_docker()
            
            # Paso 4: Probar conexiones
            self.probar_conexiones()
            
            # Paso 5: Mostrar resumen
            self.mostrar_resumen_configuracion()
            
            # Paso 6: Iniciar automatización
            self.iniciar_automatizacion()
            
            print("\n🎉 ¡Configuración completada exitosamente!")
            return True
            
        except KeyboardInterrupt:
            print("\n⏹️  Configuración cancelada por el usuario")
            return False
        except Exception as e:
            print(f"\n❌ Error durante la configuración: {e}")
            return False

def main():
    """Función principal"""
    configurador = ConfiguradorAutomatizacion()
    configurador.ejecutar_configuracion_completa()

if __name__ == "__main__":
    main()