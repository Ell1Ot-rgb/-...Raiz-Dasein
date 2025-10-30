#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear la base de datos yo_estructural en Neo4j
Ejecutar ANTES de optimizar_neo4j.py
"""

import yaml
from neo4j import GraphDatabase

def crear_base_datos():
    """Crea la base de datos yo_estructural en Neo4j"""
    
    print("\n🔨 CREACIÓN DE BASE DE DATOS NEO4J")
    print("=" * 60)
    
    # Cargar configuración
    try:
        with open('configuracion/config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("❌ Error: No se encontró configuracion/config.yaml")
        return False
    
    neo4j_config = config.get('neo4j', {})
    
    # Construir URI
    host = neo4j_config.get('host', 'localhost')
    port = neo4j_config.get('port', 7687)
    uri = f'bolt://{host}:{port}'
    username = neo4j_config.get('username', 'neo4j')
    password = neo4j_config.get('password', 'password')
    database_name = neo4j_config.get('database', 'yo_estructural')
    
    print(f"📡 Conectando a Neo4j en {uri}...")
    print(f"👤 Usuario: {username}")
    print(f"🗄️  Base de datos a crear: {database_name}\n")
    
    driver = None
    
    try:
        # Conectar a Neo4j con la base de datos 'system'
        driver = GraphDatabase.driver(uri, auth=(username, password))
        
        # Verificar conexión
        driver.verify_connectivity()
        print("✅ Conexión exitosa a Neo4j\n")
        
        # Listar bases de datos existentes
        print("📋 Bases de datos existentes:")
        with driver.session(database='system') as session:
            result = session.run("SHOW DATABASES")
            databases = [record['name'] for record in result]
            
            for db in databases:
                print(f"   • {db}")
        
        # Verificar si ya existe
        if database_name in databases:
            print(f"\n✅ La base de datos '{database_name}' ya existe")
            print("   No es necesario crearla nuevamente")
            return True
        
        # Crear la base de datos
        print(f"\n🔨 Creando base de datos '{database_name}'...")
        
        with driver.session(database='system') as session:
            session.run(f"CREATE DATABASE `{database_name}` IF NOT EXISTS")
        
        print(f"✅ Base de datos '{database_name}' creada exitosamente")
        
        # Esperar un momento para que se inicialice
        import time
        print("\n⏳ Esperando inicialización de la base de datos...")
        time.sleep(2)
        
        # Verificar que se creó correctamente
        print("\n🔍 Verificando creación...")
        with driver.session(database='system') as session:
            result = session.run("SHOW DATABASES")
            databases_new = [record['name'] for record in result]
            
            if database_name in databases_new:
                print(f"✅ Verificación exitosa: '{database_name}' está disponible")
                
                # Mostrar estado
                for record in session.run("SHOW DATABASE `" + database_name + "`"):
                    estado = record.get('currentStatus', 'unknown')
                    print(f"   Estado: {estado}")
                
                return True
            else:
                print(f"❌ Error: La base de datos no se creó correctamente")
                return False
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        
        # Verificar si es un problema de permisos
        if "permission" in str(e).lower() or "privilege" in str(e).lower():
            print("\n⚠️  SOLUCIÓN: Tu usuario no tiene permisos de administrador")
            print("\n📝 Opciones:")
            print("   1. Ejecutar este comando en Neo4j Browser como administrador:")
            print(f"      CREATE DATABASE `{database_name}` IF NOT EXISTS")
            print("\n   2. O conectar con el usuario 'neo4j' que tiene privilegios")
            print("\n   3. O otorgar permisos al usuario actual:")
            print(f"      GRANT CREATE DATABASE ON DBMS TO {username}")
        
        return False
        
    finally:
        if driver:
            driver.close()
            print("\n🔌 Conexión cerrada")

def main():
    """Función principal"""
    
    exito = crear_base_datos()
    
    if exito:
        print("\n" + "=" * 60)
        print("✅ PROCESO COMPLETADO")
        print("=" * 60)
        print("\n📌 Siguiente paso: Ejecutar 'py optimizar_neo4j.py'")
        print("   para crear índices y constraints\n")
    else:
        print("\n" + "=" * 60)
        print("❌ PROCESO FALLIDO")
        print("=" * 60)
        print("\n📌 Revisa los errores anteriores y vuelve a intentar\n")
    
    return exito

if __name__ == "__main__":
    import sys
    exito = main()
    sys.exit(0 if exito else 1)
