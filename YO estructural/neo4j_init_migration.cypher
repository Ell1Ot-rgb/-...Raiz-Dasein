// ═══════════════════════════════════════════════════════════════════════════
// Script de Inicialización Neo4j para Migración Óptima
// Usuario: neo4j
// Password: fenomenologia2024
// ═══════════════════════════════════════════════════════════════════════════

// 1. CREAR ÍNDICES PARA MÁXIMOS RELACIONALES
// ─────────────────────────────────────────────────────────────────────────
CREATE INDEX maximo_concepto IF NOT EXISTS FOR (m:MAXIMO_RELACIONAL) ON (m.concepto);
CREATE INDEX maximo_certeza IF NOT EXISTS FOR (m:MAXIMO_RELACIONAL) ON (m.certeza_combinada);
CREATE INDEX maximo_timestamp IF NOT EXISTS FOR (m:MAXIMO_RELACIONAL) ON (m.timestamp_creacion);

// 2. CREAR ÍNDICES PARA NODOS DE INSTANCIAS
// ─────────────────────────────────────────────────────────────────────────
CREATE INDEX instancia_id IF NOT EXISTS FOR (i:INSTANCIA) ON (i.id);
CREATE INDEX instancia_tipo IF NOT EXISTS FOR (i:INSTANCIA) ON (i.tipo);
CREATE INDEX instancia_timestamp IF NOT EXISTS FOR (i:INSTANCIA) ON (i.timestamp);

// 3. CREAR ÍNDICES PARA CONTENIDOS FENOMENOLÓGICOS
// ─────────────────────────────────────────────────────────────────────────
CREATE INDEX contenido_id IF NOT EXISTS FOR (c:CONTENIDO) ON (c.id);
CREATE INDEX contenido_tipo IF NOT EXISTS FOR (c:CONTENIDO) ON (c.tipo);
CREATE INDEX contenido_timestamp IF NOT EXISTS FOR (c:CONTENIDO) ON (c.timestamp_creacion);

// 4. CREAR ÍNDICES PARA CONCEPTOS DERIVADOS
// ─────────────────────────────────────────────────────────────────────────
CREATE INDEX concepto_nombre IF NOT EXISTS FOR (c:CONCEPTO) ON (c.nombre);
CREATE INDEX concepto_categoria IF NOT EXISTS FOR (c:CONCEPTO) ON (c.categoria);

// 5. CREAR ÍNDICES PARA RUTAS FENOMENOLÓGICAS
// ─────────────────────────────────────────────────────────────────────────
CREATE INDEX ruta_tipo IF NOT EXISTS FOR (r:RUTA_FENOMENOLOGICA) ON (r.tipo_ruta);
CREATE INDEX ruta_certeza IF NOT EXISTS FOR (r:RUTA_FENOMENOLOGICA) ON (r.certeza);

// 6. CREAR CONSTRAINTS (UNICIDAD)
// ─────────────────────────────────────────────────────────────────────────
CREATE CONSTRAINT maximo_unique IF NOT EXISTS FOR (m:MAXIMO_RELACIONAL) REQUIRE m.concepto IS UNIQUE;
CREATE CONSTRAINT instancia_unique IF NOT EXISTS FOR (i:INSTANCIA) REQUIRE i.id IS UNIQUE;
CREATE CONSTRAINT contenido_unique IF NOT EXISTS FOR (c:CONTENIDO) REQUIRE c.id IS UNIQUE;

// 7. CREAR NODOS INICIALES DEL SISTEMA
// ─────────────────────────────────────────────────────────────────────────

// Sistema YO Estructural (nodo raíz)
MERGE (sistema:SISTEMA {nombre: "YO_Estructural"})
ON CREATE SET 
  sistema.version = "3.0",
  sistema.timestamp_creacion = datetime(),
  sistema.descripcion = "Sistema Fenomenológico con Generador de Máximos Relacionales",
  sistema.estado = "activo",
  sistema.migracion_preparada = true,
  sistema.servidor_destino = "remoto"
RETURN sistema;

// Configuración del sistema
MERGE (config:CONFIGURACION {tipo: "sistema"})
ON CREATE SET
  config.ram_total = "4GB",
  config.optimizado_para = "4GB_DDR3",
  config.batch_size = 16,
  config.gc_interval = 3,
  config.embedding_cache_size = 200,
  config.timestamp_config = datetime()
RETURN config;

// Conectar sistema con configuración
MATCH (s:SISTEMA {nombre: "YO_Estructural"})
MATCH (c:CONFIGURACION {tipo: "sistema"})
MERGE (s)-[:USA_CONFIGURACION]->(c);

// 8. CREAR NODOS PARA MIGRACIÓN
// ─────────────────────────────────────────────────────────────────────────

// Información de migración
CREATE (m:MIGRACION {
  id: "migration_" + toString(datetime()),
  origen: "GitHub_Codespaces",
  destino: "Servidor_Remoto",
  estado: "preparada",
  timestamp_preparacion: datetime(),
  credenciales_neo4j_user: "neo4j",
  credenciales_neo4j_pass: "fenomenologia2024",
  url_neo4j_origen: "bolt://localhost:7687",
  url_neo4j_destino: "bolt://192.168.1.37:7687",
  notas: "Migración desde Codespaces a servidor remoto con n8n + Gemini integrado"
})
RETURN m;

// 9. CREAR ESTADÍSTICAS INICIALES
// ─────────────────────────────────────────────────────────────────────────

CREATE (stats:ESTADISTICAS {
  tipo: "sistema",
  total_maximos_relacionales: 0,
  total_instancias: 0,
  total_contenidos: 0,
  total_rutas_generadas: 0,
  timestamp_inicio: datetime(),
  ultima_actualizacion: datetime()
})
RETURN stats;

// 10. PROCEDIMIENTOS ALMACENADOS (si APOC está disponible)
// ─────────────────────────────────────────────────────────────────────────

// Verificar si APOC está instalado
CALL dbms.procedures() YIELD name
WHERE name STARTS WITH 'apoc'
RETURN count(*) AS apoc_procedures;

// Si APOC está disponible, crear procedimiento de respaldo
// (Este comando fallará si APOC no está instalado, pero no afectará el resto)
CALL apoc.export.cypher.all("backup_neo4j_migration.cypher", {
  format: "cypher-shell",
  useOptimizations: {type: "UNWIND_BATCH", unwindBatchSize: 20}
}) YIELD file, batches, source, format, nodes, relationships, properties, time
RETURN file, batches, nodes, relationships, time;

// 11. CONSULTAS DE VERIFICACIÓN
// ─────────────────────────────────────────────────────────────────────────

// Listar todos los índices creados
SHOW INDEXES;

// Listar todas las constraints
SHOW CONSTRAINTS;

// Contar nodos por tipo
MATCH (n)
RETURN labels(n) AS tipo, count(*) AS cantidad
ORDER BY cantidad DESC;

// Verificar estado del sistema
MATCH (s:SISTEMA)
RETURN s.nombre, s.version, s.estado, s.migracion_preparada;

// 12. MENSAJE DE CONFIRMACIÓN
// ─────────────────────────────────────────────────────────────────────────

RETURN "✅ Neo4j inicializado correctamente para migración óptima" AS status,
       "Usuario: neo4j | Password: fenomenologia2024" AS credenciales,
       "Listo para sincronizar con servidor remoto" AS siguiente_paso;
