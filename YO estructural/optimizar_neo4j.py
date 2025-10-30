#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para optimizar la base de datos Neo4j
Crea índices y constraints necesarios para mejorar el rendimiento
"""

import yaml
from database import Neo4jConnection

def crear_indices_y_constraints(db_connection):
    """Crea todos los índices y constraints necesarios para optimizar Neo4j"""
    
    print("🔧 Optimizando base de datos Neo4j...")
    print("=" * 60)
    
    # Lista de comandos para crear índices y constraints
    comandos = [
        # Constraint único para nodos YO
        ("CREATE CONSTRAINT yo_id_unique IF NOT EXISTS FOR (y:YO) REQUIRE y.id IS UNIQUE", 
         "Constraint único para YO.id"),
        
        # Constraint único para nodos Contexto
        ("CREATE CONSTRAINT contexto_id_unique IF NOT EXISTS FOR (c:Contexto) REQUIRE c.id IS UNIQUE",
         "Constraint único para Contexto.id"),
        
        # Constraint único para nodos Reflexion
        ("CREATE CONSTRAINT reflexion_id_unique IF NOT EXISTS FOR (r:Reflexion) REQUIRE r.id IS UNIQUE",
         "Constraint único para Reflexion.id"),
        
        # Constraint único para nodos Contradiccion
        ("CREATE CONSTRAINT contradiccion_id_unique IF NOT EXISTS FOR (cont:Contradiccion) REQUIRE cont.id IS UNIQUE",
         "Constraint único para Contradiccion.id"),
        
        # Índices adicionales para mejorar búsquedas
        ("CREATE INDEX yo_tipo_idx IF NOT EXISTS FOR (y:YO) ON (y.tipo)",
         "Índice para YO.tipo"),
        
        ("CREATE INDEX yo_timestamp_idx IF NOT EXISTS FOR (y:YO) ON (y.timestamp)",
         "Índice para YO.timestamp"),
        
        ("CREATE INDEX reflexion_timestamp_idx IF NOT EXISTS FOR (r:Reflexion) ON (r.timestamp)",
         "Índice para Reflexion.timestamp"),
    ]
    
    exitos = 0
    errores = 0
    
    for comando, descripcion in comandos:
        try:
            print(f"\n📌 Creando: {descripcion}")
            db_connection.query(comando)
            print(f"   ✅ Creado exitosamente")
            exitos += 1
        except Exception as e:
            if "already exists" in str(e).lower() or "equivalent" in str(e).lower():
                print(f"   ℹ️  Ya existe")
                exitos += 1
            else:
                print(f"   ❌ Error: {str(e)}")
                errores += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Optimización completada:")
    print(f"   • Éxitos: {exitos}")
    print(f"   • Errores: {errores}")
    print("=" * 60)
    
    return exitos, errores

def verificar_indices(db_connection):
    """Verifica los índices y constraints existentes"""
    
    print("\n🔍 Verificando índices y constraints existentes...")
    print("=" * 60)
    
    try:
        # Listar constraints
        print("\n📋 Constraints:")
        constraints = db_connection.query("SHOW CONSTRAINTS")
        if constraints:
            for c in constraints:
                print(f"   • {c.get('name', 'N/A')}: {c.get('type', 'N/A')}")
        else:
            print("   ⚠️  No se encontraron constraints")
        
        # Listar índices
        print("\n📋 Índices:")
        indices = db_connection.query("SHOW INDEXES")
        if indices:
            for idx in indices:
                print(f"   • {idx.get('name', 'N/A')}: {idx.get('type', 'N/A')} - Estado: {idx.get('state', 'N/A')}")
        else:
            print("   ⚠️  No se encontraron índices")
            
    except Exception as e:
        print(f"   ❌ Error al verificar: {str(e)}")
    
    print("=" * 60)

def main():
    """Función principal"""
    
    print("\n🧠 OPTIMIZACIÓN DE BASE DE DATOS NEO4J")
    print("=" * 60)
    
    # Cargar configuración
    try:
        with open('configuracion/config.yaml', 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo de configuración")
        print("   Asegúrate de tener configuracion/config.yaml")
        return False
    
    # Conectar a Neo4j
    neo4j_config = config.get('neo4j', {})
    
    # Construir URI desde host y puerto
    host = neo4j_config.get('host', 'localhost')
    port = neo4j_config.get('port', 7687)
    uri = neo4j_config.get('uri', f'bolt://{host}:{port}')
    
    try:
        connection = Neo4jConnection(
            uri,
            neo4j_config.get('username', 'neo4j'),
            neo4j_config.get('password', 'password'),
            database=neo4j_config.get('database'),
            timeout=neo4j_config.get('timeout', 30),
            max_retry=neo4j_config.get('max_retry', 3),
            pool_size=neo4j_config.get('pool_size', 50)
        )
        
        print("✅ Conectado a Neo4j exitosamente\n")
        
        # Verificar índices existentes (antes)
        verificar_indices(connection)
        
        # Crear índices y constraints
        exitos, errores = crear_indices_y_constraints(connection)
        
        # Verificar índices existentes (después)
        verificar_indices(connection)
        
        # Cerrar conexión
        connection.close()
        
        print("\n✅ Optimización completada exitosamente")
        return errores == 0
        
    except Exception as e:
        print(f"\n❌ Error crítico: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import sys
    exito = main()
    sys.exit(0 if exito else 1)
