// Inicialización Simple de Neo4j para Migración
// ═══════════════════════════════════════════════════════════════

// Limpiar constraints existentes si hay conflictos
DROP CONSTRAINT maximo_unique IF EXISTS;
DROP CONSTRAINT instancia_unique IF EXISTS;
DROP CONSTRAINT contenido_unique IF EXISTS;

// Crear índices básicos (si no existen)
CREATE INDEX maximo_concepto IF NOT EXISTS FOR (m:MAXIMO_RELACIONAL) ON (m.concepto);
CREATE INDEX maximo_certeza IF NOT EXISTS FOR (m:MAXIMO_RELACIONAL) ON (m.certeza_combinada);
CREATE INDEX instancia_id IF NOT EXISTS FOR (i:INSTANCIA) ON (i.id);
CREATE INDEX contenido_id IF NOT EXISTS FOR (c:CONTENIDO) ON (c.id);

// Crear nodo del sistema
MERGE (sistema:SISTEMA {nombre: "YO_Estructural"})
ON CREATE SET 
  sistema.version = "3.0_Codespaces",
  sistema.timestamp_creacion = datetime(),
  sistema.gemini_api_configurada = true,
  sistema.n8n_activo = true,
  sistema.migracion_preparada = true;

// Crear nodo de migración
CREATE (m:MIGRACION {
  id: "codespaces_to_remote_" + toString(timestamp()),
  origen: "GitHub_Codespaces",
  destino: "Servidor_Remoto_192.168.1.37",
  estado: "preparada",
  timestamp: datetime(),
  neo4j_user: "neo4j",
  neo4j_pass: "fenomenologia2024",
  gemini_api: "configurada",
  n8n_url: "http://localhost:5678"
});

RETURN "✅ Neo4j inicializado para migración" AS status;
