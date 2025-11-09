# 🚀 Instrucciones: Workflow Completo YO Estructural

## Estado Actual
- ✅ n8n 1.10.0 operativo
- ✅ Neo4j 5.15 funcionando
- ✅ API Gemini disponible: `AIzaSyB3cpQ-nVNn8qeC6fUhwozpgYxEFoB_Jdk`
- ✅ Credenciales Neo4j configuradas

## Objetivo
Crear un workflow que:
1. **Reciba** un concepto por webhook POST
2. **Consulte Neo4j** para encontrar conceptos relacionados
3. **Llame a Gemini** para análisis semántico
4. **Combine** resultados de ambas fuentes
5. **Retorne** análisis completo en JSON

## Arquitectura del Workflow

```
POST /webhook/yo-estructural-completo
        ↓
   [Webhook Input]
        ↓
[Consultar Neo4j] ← Query Neo4j con el concepto
        ↓
[Llamar Gemini] ← API call a Gemini con el concepto
        ↓
[Combinar Resultados] ← Merge datos Neo4j + Gemini
        ↓
[Retornar Respuesta] ← Response JSON
```

## Pasos para Crear Manualmente en n8n

### 1. Crear un nuevo Workflow

```bash
# Acceder a https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev
# Click en "+ NEW" → "Create New Workflow"
# Nombre: "🚀 YO Estructural - Versión Completa"
```

### 2. Agregar Nodo: Webhook Input

1. Click en "+" → Buscar "Webhook"
2. Seleccionar "Webhook"
3. Configurar:
   - **HTTP Method**: `POST`
   - **Path**: `yo-estructural-completo`
   - **Response mode**: `When last node finishes`

### 3. Agregar Nodo: Consultar Neo4j

1. Click en "+" después del Webhook
2. Buscar "HTTP Request"
3. Seleccionar "HTTP Request"
4. Configurar:
   - **Method**: `POST`
   - **URL**: `http://neo4j:7474/db/neo4j/tx/commit`
   - **Authentication**: `Basic Auth`
   - **Username**: `neo4j`
   - **Password**: `fenomenologia2024`
   - **Body** (JSON):
```json
{
  "statements": [
    {
      "statement": "MATCH (c:Concepto) WHERE c.nombre CONTAINS $concepto RETURN c.nombre as concepto, c.categoria as categoria, c.certeza as certeza LIMIT 5",
      "parameters": {
        "concepto": "{{ $json.body.concepto }}"
      }
    }
  ]
}
```

### 4. Agregar Nodo: Llamar Gemini

1. Click en "+" después del nodo Neo4j
2. Buscar "HTTP Request"
3. Seleccionar "HTTP Request"
4. Configurar:
   - **Method**: `POST`
   - **URL**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent`
   - **Send Query**: Toggle ON
   - **Query Parameters**: 
     ```
     key=AIzaSyB3cpQ-nVNn8qeC6fUhwozpgYxEFoB_Jdk
     ```
   - **Body** (JSON):
```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "Analiza el concepto fenomenológico: '{{ $json.body.concepto }}'. Proporciona: 1) definición, 2) raíces etimológicas, 3) sinónimos, 4) antónimos, 5) contexto de uso. Responde en JSON."
        }
      ]
    }
  ]
}
```

### 5. Agregar Nodo: Combinar Resultados

1. Click en "+" después del nodo Gemini
2. Buscar "Code"
3. Seleccionar "Code"
4. Seleccionar lenguaje: `JavaScript`
5. Pegar código:

```javascript
const neoResult = $json;
const geminiResult = $json;
const concepto = $json.body?.concepto || 'CONCEPTO';

// Extraer datos de Neo4j
const rutasNeo4j = neoResult.results?.[0]?.data?.map(row => ({
  concepto: row.row?.[0],
  categoria: row.row?.[1],
  certeza: row.row?.[2] || 0.85
})) || [];

// Extraer análisis de Gemini
const textosGemini = geminiResult.candidates?.[0]?.content?.parts?.[0]?.text || '';

// Parsear JSON de Gemini si es posible
let analisisGemini = {};
try {
  const jsonMatch = textosGemini.match(/\{[^{}]*\}/s);
  if (jsonMatch) {
    analisisGemini = JSON.parse(jsonMatch[0]);
  }
} catch (e) {
  analisisGemini = { texto_completo: textosGemini };
}

return {
  concepto: concepto,
  timestamp: new Date().toISOString(),
  es_maximo_relacional: true,
  neo4j: {
    rutas_encontradas: rutasNeo4j.length,
    datos: rutasNeo4j
  },
  gemini: {
    analisis: analisisGemini
  },
  certeza_combinada: rutasNeo4j.length > 0 ? 0.90 : 0.88,
  similitud_promedio: rutasNeo4j.reduce((acc, r) => acc + (r.certeza || 0.85), 0) / Math.max(rutasNeo4j.length, 1),
  sistema: 'YO Estructural v3.0 - Completo'
};
```

### 6. Agregar Nodo: Retornar Respuesta

1. Click en "+" después del nodo Combinar
2. Buscar "Respond to Webhook"
3. Seleccionar "Respond to Webhook"
4. Configurar:
   - **Response body**: `{{ JSON.stringify($json) }}`

### 7. Conectar Nodos

Conectar:
- Webhook Input → Consultar Neo4j
- Consultar Neo4j → Llamar Gemini
- Llamar Gemini → Combinar Resultados
- Combinar Resultados → Retornar Respuesta

### 8. Guardar y Activar

1. Click en "Save"
2. Click en el botón toggle para activar el workflow
3. El webhook estará disponible en: `/webhook/yo-estructural-completo`

## Testing

### Test 1: Concepto Simple

```bash
curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/yo-estructural-completo \
  -H "Content-Type: application/json" \
  -d '{"concepto": "SOPORTE"}'
```

### Test 2: Concepto Múltiple

```bash
curl -X POST https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev/webhook/yo-estructural-completo \
  -H "Content-Type: application/json" \
  -d '{"concepto": "FENOMENOLOGIA"}'
```

### Respuesta Esperada

```json
{
  "concepto": "SOPORTE",
  "timestamp": "2025-11-07T...",
  "es_maximo_relacional": true,
  "neo4j": {
    "rutas_encontradas": 0,
    "datos": []
  },
  "gemini": {
    "analisis": {
      "definición": "...",
      "etimología": "...",
      "sinónimos": ["..."],
      "antónimos": ["..."],
      "contexto": "..."
    }
  },
  "certeza_combinada": 0.88,
  "similitud_promedio": 0,
  "sistema": "YO Estructural v3.0 - Completo"
}
```

## Troubleshooting

### Error: "HTTP 401" en Neo4j
- Verificar usuario: `neo4j`
- Verificar contraseña: `fenomenologia2024`
- Verificar URL: `http://neo4j:7474/db/neo4j/tx/commit`

### Error: "API Key inválida" en Gemini
- Usar la API Key: `AIzaSyB3cpQ-nVNn8qeC6fUhwozpgYxEFoB_Jdk`
- Verificar modelo: `gemini-2.0-flash`

### Error: "No connection to webhook"
- Verificar que n8n esté activo: `docker ps | grep n8n`
- Verificar que el workflow esté "ON" (toggle verde)
- Acceder a https://sinister-wand-5vqjp756r4xcvpvw-5678.app.github.dev

## Archivos de Referencia

- Workflow JSON completo: `/tmp/workflow_completo.json`
- Script de creación API: `create_workflow_via_api.sh`
- Documentación técnica: `DOCUMENTO_TECNICO_DEL_SISTEMA.md`

## Próximos Pasos

1. ✅ Crear workflow completo
2. ⏳ Validar integración Neo4j
3. ⏳ Validar integración Gemini
4. ⏳ Optimizar tiempos de respuesta
5. ⏳ Agregar caché para consultas frecuentes
