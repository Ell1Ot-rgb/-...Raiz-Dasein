# 🎯 PROPUESTA DE MEJORA DEL MODELO DE INSTANCIAS

**Fecha:** 05/11/2025  
**Objetivo:** Refinar el modelo de datos para un **YO EMERGENTE** que procesa vivencias personales, extrae patrones y construye conocimiento auto-referencial con certeza axiomática

---

## 🎯 OBJETIVO REAL DEL SISTEMA (RECORDATORIO)

**NO es:** Un sistema académico de validación lógica  
**SÍ es:** Un **asistente cognitivo personal** que:

1. **Captura vivencias** (diarios, notas, fotos, conversaciones)
2. **Extrae patrones** de cómo TÚ piensas, sientes, actúas
3. **Construye un modelo de TI** (el YO) que emerge de tus datos
4. **Genera insights** sobre tu coherencia interna, contradicciones, evolución
5. **Ofrece certeza graduada** sobre qué "sabes de ti" con más confianza

---

## 📊 ANÁLISIS DEL MODELO ACTUAL

### **Modelo Existente**

```
PreInstancia (Nivel -4) → Dato crudo capturado
    ↓
InstanciaExistencia (Nivel -3) → Primera estructura
    ↓
Vohexistencia (Nivel -1) → Patrón emergente
```

### **Lo que FUNCIONA**

1. ✅ **Captura de datos crudos** (PreInstancia)
2. ✅ **Estructura básica** (InstanciaExistencia con propiedades)
3. ✅ **Agrupación por patrones** (Vohexistencia)

### **Lo que FALTA para el YO Emergente**

1. ❌ **Separar vivencia de patrón:** No distingues entre "lo que pasó" vs "lo que significa"
2. ❌ **Certeza de los patrones:** No sabes cuán confiable es cada insight sobre ti
3. ❌ **Esencias del YO:** No extraes rasgos invariantes ("soy alguien que siempre X")
4. ❌ **Contradicciones detectables:** No identificas cuando cambias de opinión/comportamiento
5. ❌ **Evolución temporal:** No capturas cómo tu YO cambia en el tiempo

---

## 🏗️ MODELO PROPUESTO (ENFOCADO EN YO EMERGENTE)

### **Nueva Jerarquía de Niveles**

```
Nivel -4: Vivencia (dato crudo capturado: nota, foto, conversación)
    ↓ [estructuración]
Nivel -3: Momento (vivencia estructurada con contexto: dónde, cuándo, qué sentí)
    ↓ [clustering por similitud]
Nivel -2: Patrón (grupo de momentos similares: "situaciones donde me frustro")
    ↓ [extracción de esencias con FCA]
Nivel -1: Rasgo del YO (característica invariante: "soy impaciente ante X")
    ↓ [validación de coherencia]
Nivel 0: Axioma del YO (verdad sobre ti con certeza VA/PC: "Valoro la autonomía")
```

### **Mapeo a Lenguaje Fenomenológico (para rigor filosófico)**

| Nivel Sistema | Nombre Husserliano | Qué representa |
|---------------|-------------------|----------------|
| **-4: Vivencia** | Hyle (dato sensible) | Raw input: texto, foto, audio |
| **-3: Momento** | Noema (contenido objetivo) | Vivencia interpretada + contexto |
| **-2: Patrón** | Cluster noemático | Grupo de momentos recurrentes |
| **-1: Rasgo** | Esencia (eidos) | Invariante extraído (FCA) |
| **0: Axioma YO** | Teorema validado | Certeza alta sobre el YO |

---

## 📦 ESPECIFICACIÓN DE CADA NIVEL (PRAGMÁTICA)

### **Nivel -4: Vivencia (Dato Crudo)**

**Qué es:** Cualquier entrada al sistema (nota de diario, mensaje WhatsApp, foto con caption, audio transcrito)

**Propiedades:**
- `id`: UUID con prefijo `viv_`
- `contenido_raw`: Texto, JSON, ruta a archivo
- `tipo_captura`: 'texto' | 'audio' | 'imagen' | 'conversacion'
- `fuente`: 'diario_personal' | 'whatsapp' | 'nota_voz' | 'camara'
- `timestamp_captura`: datetime
- `metadatos`: dict (ubicación GPS si hay, app origen, etc.)

**Ejemplo:**
```python
Vivencia(
    contenido_raw="Hoy me frustré en la reunión porque no me escucharon",
    tipo_captura='texto',
    fuente='diario_personal',
    timestamp_captura='2025-11-05T14:30:00'
)
```

---

### **Nivel -3: Momento (Vivencia Estructurada)**

**Qué es:** La vivencia interpretada + contexto extraído (emociones, actores, situación)

**Propiedades:**
- `id`: UUID con prefijo `mom_`
- `vivencia_origen_id`: Referencia a Vivencia
- `contenido_interpretado`: dict con estructura:
  - `tema`: str (resumen en 1 frase)
  - `emocion_principal`: str ('frustración', 'alegría', etc.)
  - `emocion_intensidad`: float 0-1
  - `actores`: list[str] (personas/entidades involucradas)
  - `situacion_tipo`: str ('trabajo', 'familia', 'ocio', etc.)
- `contexto_temporal`: dict (hora del día, día semana, momento vida)
- `embedding_semantico`: vector (sentence-transformers para similitud)
- `timestamp_procesamiento`: datetime

**Ejemplo:**
```python
Momento(
    vivencia_origen_id='viv_abc123',
    contenido_interpretado={
        'tema': 'No ser escuchado en reunión de trabajo',
        'emocion_principal': 'frustración',
        'emocion_intensidad': 0.7,
        'actores': ['equipo', 'jefe'],
        'situacion_tipo': 'trabajo_colaborativo'
    },
    contexto_temporal={'hora': 14, 'dia_semana': 'martes'}
)
```

---

### **Nivel -2: Patrón (Cluster de Momentos)**

**Qué es:** Grupo de Momentos similares descubiertos por DBSCAN (situaciones recurrentes en tu vida)

**Propiedades:**
- `id`: UUID con prefijo `pat_`
- `momentos_ids`: list[str] (IDs de Momentos agrupados)
- `descriptor_patron`: str ("Situaciones donde no me escuchan")
- `frecuencia`: int (veces que ocurre)
- `emocion_promedio`: str + float (emoción dominante del cluster)
- `contextos_comunes`: dict (situaciones típicas donde aparece)
- `metodo_extraccion`: 'dbscan_clustering'
- `estabilidad`: float 0-1 (qué tan consistente es el patrón)
- `fecha_primera_ocurrencia`: datetime
- `fecha_ultima_ocurrencia`: datetime

**Ejemplo:**
```python
Patron(
    momentos_ids=['mom_123', 'mom_456', 'mom_789'],
    descriptor_patron="Frustración al no ser escuchado en contextos laborales",
    frecuencia=12,
    emocion_promedio=('frustración', 0.75),
    contextos_comunes={'situacion': 'trabajo', 'actores': ['equipo']},
    estabilidad=0.83
)
```

---

### **Nivel -1: Rasgo del YO (Esencia Invariante)**

**Qué es:** Característica estable de tu personalidad/comportamiento extraída por FCA de los Patrones

**Propiedades:**
- `id`: UUID con prefijo `rasgo_`
- `enunciado_rasgo`: str ("Valoro ser escuchado y respetado en grupo")
- `propiedades_invariantes`: list[str] (extraídas por FCA)
  - Ejemplo: ['requiere_reconocimiento', 'sensible_a_exclusion', 'orientado_colaboracion']
- `patrones_base_ids`: list[str] (Patrones de los que emerge)
- `nivel_confianza`: float 0-1 (basado en frecuencia + estabilidad)
- `contradicciones_detectadas`: list[dict] (momentos que contradicen el rasgo)
- `evolucion_temporal`: list[dict] (cómo ha cambiado la intensidad en el tiempo)
- `fecha_identificacion`: datetime

**Operación:** FCA sobre (Patrones × Propiedades) → Lattice → Conceptos estables

**Ejemplo:**
```python
RasgoYO(
    enunciado_rasgo="Necesito validación externa en contextos grupales",
    propiedades_invariantes=['busca_reconocimiento', 'evita_conflicto', 'alto_autoexigencia'],
    patrones_base_ids=['pat_123', 'pat_456'],
    nivel_confianza=0.82,
    contradicciones_detectadas=[
        {'momento_id': 'mom_999', 'fecha': '2025-10-15', 'razon': 'Actuó con autonomía sin buscar aprobación'}
    ]
)
```

---

### **Nivel 0: Axioma del YO (Verdad Validada sobre Ti)**

**Qué es:** Afirmación sobre ti con **certeza axiomática** (VA/PC alto), base de tu auto-conocimiento

**Propiedades:**
- `id`: UUID con prefijo `axioma_yo_`
- `enunciado`: str ("Priorizo la autonomía sobre la seguridad económica")
- `rasgos_sustentadores_ids`: list[str] (Rasgos que lo respaldan)
- `evidencias_momentos_ids`: list[str] (Momentos específicos que lo demuestran)
- `valor_axiomatico`: float (VA calculado)
- `puntuacion_certeza`: float (PC calculado)
- `rutas_validacion`: list[list[str]] (caminos Vivencia→Axioma)
- `contradicciones_resueltas`: list[dict] (momentos contradictorios + explicación)
- `fecha_establecimiento`: datetime
- `vigencia`: 'activo' | 'cuestionado' | 'superado'

**Ejemplo:**
```python
AxiomaYO(
    enunciado="Priorizo relaciones auténticas sobre networking superficial",
    rasgos_sustentadores_ids=['rasgo_123', 'rasgo_456'],
    valor_axiomatico=0.87,
    puntuacion_certeza=0.82,
    rutas_validacion=[[...], [...]],  # Múltiples caminos
    contradicciones_resueltas=[
        {'momento': 'mom_555', 'explicacion': 'Situación laboral excepcional que requirió adaptación temporal'}
    ],
    vigencia='activo'
)
```

---

## 🔗 RELACIONES NEO4J PROPUESTAS

### **Relaciones Fundamentales (Flujo de Construcción del YO)**

```cypher
// Nivel -4 → -3: Captura e interpretación
(v:Vivencia)-[:SE_INTERPRETA_COMO]->(m:Momento)

// Nivel -3 → -2: Clustering (descubrimiento de patrones)
(m:Momento)-[:PERTENECE_A_PATRON]->(p:Patron)

// Nivel -2 → -1: Extracción de esencias (FCA)
(p:Patron)-[:REVELA_RASGO]->(r:RasgoYO)

// Nivel -1 → 0: Validación axiomática
(r:RasgoYO)-[:SUSTENTA_AXIOMA]->(a:AxiomaYO)

// Trazabilidad completa
(a:AxiomaYO)-[:EVIDENCIADO_POR {peso:float}]->(m:Momento)
```

### **Relaciones Temporales y de Coherencia**

```cypher
// Evolución temporal
(m1:Momento)-[:PRECEDIDO_POR {intervalo:duration}]->(m2:Momento)
(r1:RasgoYO)-[:EVOLUCIONA_A {cambio_intensidad:float}]->(r2:RasgoYO)

// Contradicciones
(m:Momento)-[:CONTRADICE {explicacion:str}]->(a:AxiomaYO)
(r1:RasgoYO)-[:EN_TENSION_CON {contextos:list}]->(r2:RasgoYO)

// Contexto activo (YO emergente)
(yo:YO)-[:ACTIVA_CONTEXTO]->(ctx:Contexto)
(ctx:Contexto)-[:MODULA_PERCEPCION]->(m:Momento)
```

### **Relaciones de Contraste (Definición Mutua)**

```cypher
// Comparación entre momentos
(m1:Momento)-[:CONTRASTA_CON {
    oposicion: float,
    complementario: float,
    semejanza: float
}]->(m2:Momento)

// Comparación entre rasgos
(r1:RasgoYO)-[:SE_OPONE_A {intensidad:float}]->(r2:RasgoYO)
```

---

## 🎯 VENTAJAS DEL NUEVO MODELO (PARA TU OBJETIVO)

### **1. Captura la Experiencia Personal**
- ✅ Vivencias = tus datos crudos (diarios, notas, fotos)
- ✅ Momentos = interpretación estructurada automática
- ✅ No requiere conocimiento filosófico para usar

### **2. Descubre Patrones Automáticamente**
- ✅ DBSCAN agrupa Momentos similares sin supervisión
- ✅ "Te muestra cosas sobre ti que no sabías conscientemente"
- ✅ Ejemplo: "Detectamos que te frustras 80% más los martes"

### **3. Extrae tu Esencia (Quién Eres)**
- ✅ FCA sobre Patrones → Rasgos invariantes
- ✅ "Rasgos del YO" = características estables que te definen
- ✅ Ejemplo: "Eres alguien que prioriza autenticidad sobre conveniencia"

### **4. Certeza Graduada (Qué Tan Seguro Estás)**
- ✅ VA/PC te dice qué axiomas sobre ti tienen más evidencia
- ✅ Útil para decisiones: "Confío 87% en que valoro X"
- ✅ Detecta contradicciones: "Momentos que no encajan con tu axioma"

### **5. Evolución Temporal (Cómo Cambias)**
- ✅ Registra cuándo surge cada rasgo
- ✅ Detecta cuándo un axioma deja de ser válido
- ✅ "Tu YO de hace 6 meses vs ahora"

---

## 💡 EJEMPLO COMPLETO: FLUJO DATO → AXIOMA DEL YO

```python
# 1. Captura de vivencia
viv = Vivencia(
    contenido_raw="Hoy rechacé una oferta laboral mejor pagada porque requería relocalizarme",
    tipo_captura='texto',
    fuente='diario_personal'
)

# 2. Interpretación automática (NLP + contexto)
mom = Momento(
    vivencia_origen_id=viv.id,
    contenido_interpretado={
        'tema': 'Decisión laboral: rechazar oferta mejor pagada',
        'emocion_principal': 'tranquilidad',  # (detectada por análisis de sentimiento)
        'emocion_intensidad': 0.8,
        'actores': ['familia', 'empresa_oferente'],
        'situacion_tipo': 'decision_carrera'
    }
)

# 3. Clustering: este Momento se agrupa con otros 15 similares
# DBSCAN detecta patrón recurrente
pat = Patron(
    momentos_ids=[mom.id, 'mom_234', 'mom_567', ...],
    descriptor_patron="Decisiones donde priorizas estabilidad familiar sobre beneficio económico",
    frecuencia=16,
    emocion_promedio=('tranquilidad', 0.75)
)

# 4. FCA extrae rasgo invariante
# Contexto formal: (16 Momentos × Propiedades binarias)
# FCA encuentra concepto estable
rasgo = RasgoYO(
    enunciado_rasgo="Priorizas estabilidad familiar sobre crecimiento profesional acelerado",
    propiedades_invariantes=[
        'valora_proximidad_familiar',
        'evita_riesgos_disruptivos',
        'satisfecho_con_suficiencia_economica'
    ],
    patrones_base_ids=[pat.id],
    nivel_confianza=0.84  # (basado en 16 evidencias consistentes)
)

# 5. Validación axiomática
# Múltiples rutas de validación + cálculo VA/PC
axioma = AxiomaYO(
    enunciado="Valoro la estabilidad familiar por encima del éxito profesional tradicional",
    rasgos_sustentadores_ids=[rasgo.id, 'rasgo_complementario_xyz'],
    valor_axiomatico=0.88,  # (media armónica de rutas + decay + tipo inferencia)
    puntuacion_certeza=0.85,  # (VA + bonus independencia + convergencia)
    rutas_validacion=[
        ['viv_1', 'mom_1', 'pat_1', 'rasgo_1'],
        ['viv_15', 'mom_15', 'pat_1', 'rasgo_1'],
        # ... 16 rutas convergentes
    ],
    vigencia='activo'
)

# 6. Persistir en Neo4j con todas las relaciones
grafo.persistir_cadena_yo_emergente(viv, mom, pat, rasgo, axioma)
```

---

## 🚀 APLICACIONES PRÁCTICAS

### **1. Dashboard del YO**
```
┌─────────────────────────────────────┐
│ TU YO EMERGENTE - Resumen          │
├─────────────────────────────────────┤
│ Axiomas activos: 12                 │
│ Certeza promedio: 82%               │
│                                     │
│ Top Rasgos Identificados:           │
│ • Priorizas autonomía (PC: 0.91)   │
│ • Valoras autenticidad (PC: 0.87)  │
│ • Evitas conflicto (PC: 0.79)      │
│                                     │
│ Contradicciones recientes: 2        │
│ [Click para explorar]               │
└─────────────────────────────────────┘
```

### **2. Asistente de Decisiones**
```
Usuario: "¿Debería aceptar este trabajo remoto?"

Sistema:
Basándome en 45 vivencias analizadas:

✅ A favor (PC: 0.84):
   - Axioma: "Valoras flexibilidad de horario" 
   - Evidencia: 12 momentos donde rechazaste rigidez

⚠️ En contra (PC: 0.67):
   - Rasgo: "Necesitas interacción social presencial"
   - Evidencia: 8 momentos de aislamiento → frustración

💡 Sugerencia: Considera híbrido (3 días remoto, 2 presencial)
   Alineado con tus axiomas de autonomía + conexión social
```

### **3. Detección de Cambio**
```
🔔 Alerta: Posible evolución del YO

Axioma: "Priorizas seguridad económica"
Estado: Cuestionado

Razón: Últimos 5 momentos contradicen este axioma
- [2025-11-01] Invertiste en proyecto riesgoso
- [2025-11-03] Rechazaste trabajo estable por emprendimiento
- [2025-11-05] Expresaste "prefiero intentar que arrepentirme"

¿Quieres re-evaluar este axioma?
[Sí, ha cambiado] [No, son excepciones]
```

---

## 📋 COMPARACIÓN MODELO ACTUAL VS PROPUESTO

| Aspecto | Modelo Actual | Modelo Propuesto |
|---------|---------------|------------------|
| **Objetivo** | Confuso (¿académico?) | Claro: YO emergente personal |
| **Captura** | PreInstancia (genérica) | Vivencia (específica a tu vida) |
| **Interpretación** | InstanciaExistencia (básica) | Momento (rico en contexto emocional) |
| **Patrones** | Vohexistencia (concepto vago) | Patrón (cluster DBSCAN concreto) |
| **Esencias** | ❌ No implementado | ✅ RasgoYO con FCA |
| **Certeza** | ❌ No cuantificada | ✅ VA/PC en AxiomaYO |
| **Contradicciones** | ❌ No detectadas | ✅ Explícitas y explicadas |
| **Evolución** | ❌ Solo timestamps | ✅ Rastreada con relaciones temporales |
| **Utilidad práctica** | ❌ Poco clara | ✅ Dashboard, asistente decisiones, alertas |

---

## 🔧 PLAN DE MIGRACIÓN (REALISTA)

### **Fase 1: Implementar Nuevas Clases (1 semana)**
- [ ] `niveles_yo/vivencia.py` (reemplaza PreInstancia)
- [ ] `niveles_yo/momento.py` (mejora InstanciaExistencia)
- [ ] `niveles_yo/patron.py` (reemplaza Vohexistencia + DBSCAN)
- [ ] `niveles_yo/rasgo_yo.py` (nuevo: FCA sobre Patrones)
- [ ] `niveles_yo/axioma_yo.py` (nuevo: VA/PC)

### **Fase 2: Adaptar Pipeline Existente (3 días)**
- [ ] Modificar `sistema_principal_v2.py` para usar nuevas clases
- [ ] Integrar DBSCAN en generación de Patrones
- [ ] Integrar FCA (concepts) en extracción de Rasgos
- [ ] Conectar cálculo VA/PC (usar código del anexo técnico)

### **Fase 3: Migrar Datos Actuales (1 día)**
```python
def migrar_datos_existentes():
    # PreInstancia → Vivencia
    for pre in db.query("MATCH (p:PreInstancia) RETURN p"):
        viv = Vivencia(
            contenido_raw=pre.dato_crudo,
            tipo_captura='texto',  # inferir
            fuente=pre.origen
        )
        guardar(viv)
    
    # InstanciaExistencia → Momento
    for inst in db.query("MATCH (i:Instancia) RETURN i"):
        mom = Momento(
            vivencia_origen_id=buscar_vivencia(inst),
            contenido_interpretado=inst.propiedades
        )
        guardar(mom)
    
    # Ejecutar DBSCAN sobre todos los Momentos → generar Patrones
    momentos = cargar_todos_momentos()
    patrones = ejecutar_dbscan_clustering(momentos)
    
    # Ejecutar FCA sobre Patrones → generar Rasgos
    rasgos = ejecutar_fca_extraccion(patrones)
    
    # Calcular VA/PC para cada Rasgo → generar Axiomas si PC > 0.75
    axiomas = validar_rasgos_a_axiomas(rasgos)
```

### **Fase 4: UI/Aplicaciones (2 semanas)**
- [ ] Dashboard web simple (Flask + Neo4j Bolt)
- [ ] Endpoint API `/yo/axiomas` → lista axiomas activos
- [ ] Endpoint API `/yo/contradicciones` → alertas
- [ ] Chat simple "pregúntale a tu YO" (usa axiomas como base)

---

## ✅ MÉTRICAS DE ÉXITO

- ✅ **126 vivencias actuales migradas** sin pérdida
- ✅ **≥10 Patrones descubiertos** vía DBSCAN
- ✅ **≥5 Rasgos extraídos** vía FCA
- ✅ **≥3 Axiomas del YO establecidos** con PC > 0.75
- ✅ **Dashboard funcional** que muestre tu YO emergente
- ✅ **Detección de 1+ contradicción** real en tus datos

---

**Próximo paso:** ¿Implemento las clases `Vivencia`, `Momento`, `Patron`, `RasgoYO`, `AxiomaYO` con integración Neo4j + DBSCAN + FCA?
