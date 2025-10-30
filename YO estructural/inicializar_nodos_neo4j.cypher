// ============================================================
// INICIALIZACIÓN DEL SISTEMA YO ESTRUCTURAL v3.0 EN NEO4J
// Copiar y pegar en Neo4j Browser o cypher-shell
// ============================================================

// 1️⃣ CONFIRMAR BASE DE DATOS ACTIVA
:use yo_estructural

// 2️⃣ LIMPIAR DATOS ANTERIORES (OPCIONAL - DESCOMENTAR SI QUIERES EMPEZAR LIMPIO)
// MATCH (n) DETACH DELETE n;

// ============================================================
// 3️⃣ CREAR NODO PRINCIPAL DEL SISTEMA
// ============================================================
CREATE (:Sistema {
  id: 'sistema_yo_estructural_001',
  nombre: 'YO estructural',
  version: '3.0',
  estado: 'activo',
  tipo: 'fenomenologia_computacional',
  descripcion: 'Sistema fenomenológico de procesamiento y emergencia del YO',
  timestamp_creacion: datetime(),
  autor: 'Elliot',
  niveles_jerarquicos: [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
  fases_totales: 9
});

// ============================================================
// 4️⃣ CREAR MÓDULOS Y SUBSISTEMAS PRINCIPALES
// ============================================================

// MÓDULO MDCE - Metaestabilizador Dinámico de Coherencia Estructural
CREATE (:Modulo {
  id: 'modulo_mdce_001',
  nombre: 'MDCE',
  tipo: 'Metaestabilizador Dinámico de Coherencia Estructural',
  funcion: 'Detectar y resolver contradicciones narrativas',
  descripcion: 'Sistema de coherencia que detecta contradicciones nivel 1-5 y activa reconfiguraciones',
  estado: 'activo',
  niveles_contradiccion: [1, 2, 3, 4, 5],
  umbral_reconfig: 4,
  timestamp_creacion: datetime()
});

// MÓDULO YO REFLEXIVO
CREATE (:Modulo {
  id: 'modulo_yo_reflexivo_001',
  nombre: 'YO_Reflexivo',
  tipo: 'Subsistema YO Emergente',
  funcion: 'Observación y auto-reflexión del sistema',
  descripcion: 'Sistema que emerge de los contextos y mantiene coherencia narrativa',
  tipos_yo: ['NARRATIVO', 'REFLEXIVO', 'CONTEXTUAL', 'FRACTURADO'],
  coherencia_minima: 0.6,
  estado: 'activo',
  timestamp_creacion: datetime()
});

// MÓDULO PROCESADOR FENOMENOLÓGICO
CREATE (:Modulo {
  id: 'modulo_procesador_fenomenologico_001',
  nombre: 'Procesador_Fenomenologico',
  tipo: 'Motor de Procesamiento',
  funcion: 'Procesar datos crudos y clasificarlos en fases 0-8',
  descripcion: 'Procesa archivos y genera instancias, gradientes, fenómenos, contextos',
  fases_procesamiento: ['preinstancia', 'instancia', 'gradiente', 'vohexistencia', 'fenomeno', 'contexto', 'metacontexto', 'yo', 'voluntad'],
  estado: 'activo',
  timestamp_creacion: datetime()
});

// MÓDULO SISTEMA VECTORIAL
CREATE (:Modulo {
  id: 'modulo_vectorial_001',
  nombre: 'Sistema_Vectorial',
  tipo: 'Procesamiento Semántico',
  funcion: 'Generar embeddings y calcular similitudes',
  descripcion: 'Sistema de vectorización TF-IDF y embeddings para similitud semántica',
  algoritmos: ['TF-IDF', 'Word2Vec', 'Cosine Similarity'],
  umbral_similitud: 0.3,
  estado: 'activo',
  timestamp_creacion: datetime()
});

// MÓDULO DETECTOR DE CONTRADICCIONES
CREATE (:Modulo {
  id: 'modulo_detector_contradicciones_001',
  nombre: 'Detector_Contradicciones',
  tipo: 'Análisis de Coherencia',
  funcion: 'Detectar incoherencias narrativas y temporales',
  descripcion: 'Analiza coherencia interna y detecta contradicciones de nivel 1-5',
  niveles: ['superficial', 'semantica', 'narrativa', 'estructural', 'existencial'],
  estado: 'activo',
  timestamp_creacion: datetime()
});

// ============================================================
// 5️⃣ CREAR FASES FENOMENOLÓGICAS (0-8)
// ============================================================

// FASE 0: PREINSTANCIA
CREATE (:Fase {
  id: 'fase_0_preinstancia',
  numero: 0,
  nombre: 'PreInstancia',
  nivel_jerarquico: -4,
  descripcion: 'Registro de existencia sin concepto - dato crudo',
  etiqueta_neo4j: 'PreInstancia',
  propiedades_requeridas: ['dato_crudo', 'origen', 'timestamp'],
  color: '#1a1a1a',
  estado: 'activo'
});

// FASE 1: INSTANCIA
CREATE (:Fase {
  id: 'fase_1_instancia',
  numero: 1,
  nombre: 'Instancia',
  nivel_jerarquico: -3,
  descripcion: 'Instancia con propiedades fenomenológicas',
  etiqueta_neo4j: 'Instancia',
  propiedades_requeridas: ['activacion', 'tipo', 'peso_existencial'],
  color: '#2d2d2d',
  estado: 'activo'
});

// FASE 2: GRADIENTE
CREATE (:Fase {
  id: 'fase_2_gradiente',
  numero: 2,
  nombre: 'Gradiente',
  nivel_jerarquico: -2,
  descripcion: 'Gradientes relacionales acumulativos',
  etiqueta_neo4j: 'Gradiente',
  propiedades_requeridas: ['valor_gradiente', 'direccion'],
  color: '#404040',
  estado: 'activo'
});

// FASE 3: VOHEXISTENCIA
CREATE (:Fase {
  id: 'fase_3_vohexistencia',
  numero: 3,
  nombre: 'Vohexistencia',
  nivel_jerarquico: -1,
  descripcion: 'Agrupaciones por propiedades compartidas',
  etiqueta_neo4j: 'Vohexistencia',
  propiedades_requeridas: ['peso_coexistencial', 'constante_emergente'],
  color: '#595959',
  estado: 'activo'
});

// FASE 4: FENÓMENO (NÚCLEO)
CREATE (:Fase {
  id: 'fase_4_fenomeno',
  numero: 4,
  nombre: 'Fenomeno',
  nivel_jerarquico: 0,
  descripcion: 'Núcleos conceptuales por frecuencia - nivel fundamental',
  etiqueta_neo4j: 'Fenomeno',
  propiedades_requeridas: ['contenido', 'tipo', 'intensidad', 'es_nucleo'],
  color: '#ff6b35',
  estado: 'activo'
});

// FASE 5: CONTEXTO
CREATE (:Fase {
  id: 'fase_5_contexto',
  numero: 5,
  nombre: 'Contexto',
  nivel_jerarquico: 1,
  descripcion: 'Estructuras narrativas y temporales',
  etiqueta_neo4j: 'Contexto',
  propiedades_requeridas: ['estructura', 'nivel', 'yo_emergente'],
  color: '#4ecdc4',
  estado: 'activo'
});

// FASE 6: METACONTEXTO
CREATE (:Fase {
  id: 'fase_6_metacontexto',
  numero: 6,
  nombre: 'Metacontexto',
  nivel_jerarquico: 2,
  descripcion: 'Agrupaciones de contextos por fenómenos compartidos',
  etiqueta_neo4j: 'Metacontexto',
  propiedades_requeridas: ['patron_emergente', 'contextos_incluidos'],
  color: '#45b7d1',
  estado: 'activo'
});

// FASE 7: YO
CREATE (:Fase {
  id: 'fase_7_yo',
  numero: 7,
  nombre: 'YO',
  nivel_jerarquico: 3,
  descripcion: 'Emergencia del YO observador - punto de auto-reflexión',
  etiqueta_neo4j: 'YO',
  propiedades_requeridas: ['tipo', 'coherencia_narrativa', 'version'],
  color: '#f7b731',
  estado: 'activo'
});

// FASE 8: VOLUNTAD
CREATE (:Fase {
  id: 'fase_8_voluntad',
  numero: 8,
  nombre: 'Voluntad',
  nivel_jerarquico: 4,
  descripcion: 'Predicción de efectos y sugerencia de acciones',
  etiqueta_neo4j: 'Voluntad',
  propiedades_requeridas: ['direccion', 'intensidad', 'prediccion'],
  color: '#5f27cd',
  estado: 'activo'
});

// ============================================================
// 6️⃣ CREAR TIPOS DE RELACIONES FENOMENOLÓGICAS
// ============================================================

CREATE (:TipoRelacion {
  id: 'rel_se_parece_a',
  nombre: 'SE_PARECE_A',
  descripcion: 'Similitud semántica entre instancias',
  peso_minimo: 0.3,
  direccion: 'bidireccional',
  nivel_aplicable: [-3, -2, -1, 0]
});

CREATE (:TipoRelacion {
  id: 'rel_agrupa',
  nombre: 'AGRUPA',
  descripcion: 'Agrupación en vohexistencias',
  peso_minimo: 0.5,
  direccion: 'unidireccional',
  nivel_aplicable: [-1, 0]
});

CREATE (:TipoRelacion {
  id: 'rel_incluye',
  nombre: 'INCLUYE',
  descripcion: 'Inclusión en contextos',
  peso_minimo: 0.4,
  direccion: 'unidireccional',
  nivel_aplicable: [0, 1, 2]
});

CREATE (:TipoRelacion {
  id: 'rel_surge_de',
  nombre: 'SURGE_DE',
  descripcion: 'Emergencia desde contextos',
  peso_minimo: 0.6,
  direccion: 'unidireccional',
  nivel_aplicable: [1, 2, 3]
});

CREATE (:TipoRelacion {
  id: 'rel_observa',
  nombre: 'OBSERVA',
  descripcion: 'Observación del YO',
  peso_minimo: 0.7,
  direccion: 'unidireccional',
  nivel_aplicable: [3]
});

CREATE (:TipoRelacion {
  id: 'rel_contradice',
  nombre: 'CONTRADICE',
  descripcion: 'Contradicción consciente',
  peso_minimo: 0.5,
  direccion: 'bidireccional',
  nivel_aplicable: [0, 1, 2, 3]
});

CREATE (:TipoRelacion {
  id: 'rel_actua_en',
  nombre: 'ACTUA_EN',
  descripcion: 'Acción de la voluntad',
  peso_minimo: 0.6,
  direccion: 'unidireccional',
  nivel_aplicable: [4]
});

// ============================================================
// 7️⃣ CREAR RELACIONES ENTRE MÓDULOS Y SISTEMA
// ============================================================

MATCH (s:Sistema {nombre: 'YO estructural'}),
      (m:Modulo {nombre: 'MDCE'})
CREATE (m)-[:PERTENECE_A {
  rol: 'metaestabilizador',
  prioridad: 1,
  timestamp: datetime()
}]->(s);

MATCH (s:Sistema {nombre: 'YO estructural'}),
      (m:Modulo {nombre: 'YO_Reflexivo'})
CREATE (m)-[:EMERGE_DE {
  proceso: 'emergencia_contextual',
  nivel_emergencia: 3,
  timestamp: datetime()
}]->(s);

MATCH (s:Sistema {nombre: 'YO estructural'}),
      (m:Modulo {nombre: 'Procesador_Fenomenologico'})
CREATE (m)-[:PERTENECE_A {
  rol: 'motor_procesamiento',
  prioridad: 2,
  timestamp: datetime()
}]->(s);

MATCH (s:Sistema {nombre: 'YO estructural'}),
      (m:Modulo {nombre: 'Sistema_Vectorial'})
CREATE (m)-[:PERTENECE_A {
  rol: 'procesamiento_semantico',
  prioridad: 3,
  timestamp: datetime()
}]->(s);

MATCH (s:Sistema {nombre: 'YO estructural'}),
      (m:Modulo {nombre: 'Detector_Contradicciones'})
CREATE (m)-[:PERTENECE_A {
  rol: 'analisis_coherencia',
  prioridad: 1,
  timestamp: datetime()
}]->(s);

// ============================================================
// 8️⃣ RELACIONAR MÓDULOS ENTRE SÍ
// ============================================================

MATCH (mdce:Modulo {nombre: 'MDCE'}),
      (detector:Modulo {nombre: 'Detector_Contradicciones'})
CREATE (detector)-[:ALIMENTA_A {
  tipo: 'deteccion_contradicciones',
  timestamp: datetime()
}]->(mdce);

MATCH (yo:Modulo {nombre: 'YO_Reflexivo'}),
      (mdce:Modulo {nombre: 'MDCE'})
CREATE (mdce)-[:MANTIENE_COHERENCIA_DE {
  proceso: 'reconfiguracion',
  timestamp: datetime()
}]->(yo);

MATCH (procesador:Modulo {nombre: 'Procesador_Fenomenologico'}),
      (vectorial:Modulo {nombre: 'Sistema_Vectorial'})
CREATE (procesador)-[:UTILIZA {
  para: 'similitud_semantica',
  timestamp: datetime()
}]->(vectorial);

// ============================================================
// 9️⃣ RELACIONAR FASES EN JERARQUÍA
// ============================================================

MATCH (f0:Fase {numero: 0}), (f1:Fase {numero: 1})
CREATE (f0)-[:TRANSFORMA_EN {nivel: 'ascendente'}]->(f1);

MATCH (f1:Fase {numero: 1}), (f2:Fase {numero: 2})
CREATE (f1)-[:TRANSFORMA_EN {nivel: 'ascendente'}]->(f2);

MATCH (f2:Fase {numero: 2}), (f3:Fase {numero: 3})
CREATE (f2)-[:TRANSFORMA_EN {nivel: 'ascendente'}]->(f3);

MATCH (f3:Fase {numero: 3}), (f4:Fase {numero: 4})
CREATE (f3)-[:TRANSFORMA_EN {nivel: 'ascendente'}]->(f4);

MATCH (f4:Fase {numero: 4}), (f5:Fase {numero: 5})
CREATE (f4)-[:TRANSFORMA_IN {nivel: 'ascendente'}]->(f5);

MATCH (f5:Fase {numero: 5}), (f6:Fase {numero: 6})
CREATE (f5)-[:TRANSFORMA_EN {nivel: 'ascendente'}]->(f6);

MATCH (f6:Fase {numero: 6}), (f7:Fase {numero: 7})
CREATE (f6)-[:TRANSFORMA_EN {nivel: 'emergente'}]->(f7);

MATCH (f7:Fase {numero: 7}), (f8:Fase {numero: 8})
CREATE (f7)-[:TRANSFORMA_EN {nivel: 'volitivo'}]->(f8);

// ============================================================
// 🔟 CREAR CONFIGURACIÓN GLOBAL DEL SISTEMA
// ============================================================

CREATE (:Configuracion {
  id: 'config_sistema_001',
  nombre: 'Configuracion_Global',
  version: '3.0',
  neo4j_host: '192.168.1.37',
  neo4j_port: 7687,
  database: 'yo_estructural',
  idioma: 'spanish',
  umbral_similitud: 0.3,
  umbral_coherencia: 0.6,
  umbral_reconfig: 4,
  max_contextos_activos: 50,
  timestamp_creacion: datetime()
});

// ============================================================
// ✅ VERIFICAR CREACIÓN
// ============================================================

// Contar nodos creados
MATCH (n) 
RETURN labels(n)[0] as TipoNodo, count(n) as Cantidad 
ORDER BY Cantidad DESC;

// Ver estructura del sistema
MATCH (s:Sistema)-[r]->(m) 
RETURN s.nombre, type(r), m.nombre;

// Ver jerarquía de fases
MATCH (f1:Fase)-[r:TRANSFORMA_EN]->(f2:Fase) 
RETURN f1.nombre, f1.nivel_jerarquico, f2.nombre, f2.nivel_jerarquico 
ORDER BY f1.numero;

// ============================================================
// 🎉 SISTEMA INICIALIZADO
// ============================================================
// Total de nodos: ~25
// - 1 Sistema
// - 5 Módulos
// - 9 Fases
// - 7 TiposRelacion
// - 1 Configuración
// - Relaciones de jerarquía y dependencia
// ============================================================
