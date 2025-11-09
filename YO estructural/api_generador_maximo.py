"""
API REST para el Generador de Rutas Fenomenológicas con soporte para Gemini y n8n
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
import sys
import os
from datetime import datetime

# Agregar directorio padre al path para imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from procesadores.generador_rutas_fenomenologicas import GeneradorRutasFenomenologicas
from procesadores.gemini_integration import GeminiEnriquecedor, verificar_gemini_disponible
from integraciones.n8n_config import N8nIntegrator

app = FastAPI(
    title="API Generador Máximo Relacional",
    description="API para generar rutas fenomenológicas y detectar máximos relacionales",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar componentes globales
generador = None
gemini_enriquecedor = None
n8n_integrator = None

@app.on_event("startup")
async def startup_event():
    """Inicializar componentes al arrancar"""
    global generador, gemini_enriquecedor, n8n_integrator
    
    print("🚀 Inicializando API Generador Máximo Relacional...")
    
    # Inicializar generador
    try:
        generador = GeneradorRutasFenomenologicas(
            modelo_embeddings="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            usar_neo4j=True,
            neo4j_uri=os.getenv('NEO4J_URI', 'bolt://localhost:7687'),
            neo4j_user=os.getenv('NEO4J_USER', 'neo4j'),
            neo4j_password=os.getenv('NEO4J_PASSWORD', 'fenomenologia2024')
        )
        print("✅ Generador de rutas inicializado")
    except Exception as e:
        print(f"⚠️ Error inicializando generador: {e}")
        generador = None
    
    # Inicializar Gemini (opcional)
    if verificar_gemini_disponible():
        try:
            gemini_enriquecedor = GeminiEnriquecedor()
            print("✅ Gemini disponible para enriquecimiento")
        except Exception as e:
            print(f"⚠️ Gemini no disponible: {e}")
            gemini_enriquecedor = None
    else:
        print("⚠️ Gemini no configurado (opcional)")
    
    # Inicializar n8n (opcional)
    try:
        n8n_integrator = N8nIntegrator()
        print("✅ Integración n8n configurada")
    except Exception as e:
        print(f"⚠️ n8n no disponible: {e}")
        n8n_integrator = None
    
    print("🎯 API lista para recibir solicitudes")


class ConceptoRequest(BaseModel):
    """Request para generar rutas de un concepto"""
    concepto: str = Field(..., description="Concepto a analizar (ej: 'SOPORTE')")
    usar_neo4j: bool = Field(True, description="Guardar en Neo4j")
    usar_gemini: bool = Field(False, description="Enriquecer con Gemini")
    enviar_a_n8n: bool = Field(False, description="Enviar resultado a n8n webhook")


class MaximoRelacionalResponse(BaseModel):
    """Response con el resultado del análisis"""
    concepto: str
    es_maximo_relacional: bool
    certeza_combinada: float
    similitud_promedio: float
    rutas: List[Dict]
    gemini_analisis: Optional[Dict] = None
    neo4j_guardado: bool = False
    n8n_enviado: bool = False
    timestamp: str
    tiempo_procesamiento_ms: int


@app.get("/")
async def root():
    """Endpoint raíz con información de la API"""
    return {
        "api": "Generador Máximo Relacional",
        "version": "1.0.0",
        "estado": {
            "generador": generador is not None,
            "gemini": gemini_enriquecedor is not None,
            "n8n": n8n_integrator is not None
        },
        "endpoints": {
            "generar_rutas": "/api/generador/rutas",
            "verificar_maximo": "/api/generador/verificar-maximo",
            "health": "/health",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health():
    """Health check del servicio"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "componentes": {
            "generador": "ok" if generador else "error",
            "gemini": "ok" if gemini_enriquecedor else "no_configurado",
            "n8n": "ok" if n8n_integrator else "no_configurado"
        }
    }


@app.post("/api/generador/rutas", response_model=MaximoRelacionalResponse)
async def generar_rutas(request: ConceptoRequest, background_tasks: BackgroundTasks):
    """
    Genera las 5 rutas fenomenológicas para un concepto y determina si es máximo relacional
    
    Args:
        request: Datos del concepto a analizar
        background_tasks: Para tareas asíncronas (ej: enviar a n8n)
    
    Returns:
        MaximoRelacionalResponse con análisis completo
    """
    tiempo_inicio = datetime.now()
    
    if not generador:
        raise HTTPException(
            status_code=503, 
            detail="Generador no disponible. Verificar configuración."
        )
    
    concepto = request.concepto.strip().upper()
    
    if not concepto:
        raise HTTPException(status_code=400, detail="Concepto vacío")
    
    try:
        # 1. Generar rutas con el generador
        print(f"📊 Generando rutas para: {concepto}")
        resultado = generador.generar_maximo_relacional(concepto)
        
        # 2. Enriquecer con Gemini si está disponible y solicitado
        gemini_analisis = None
        if request.usar_gemini and gemini_enriquecedor:
            print(f"🤖 Enriqueciendo con Gemini...")
            try:
                gemini_analisis = gemini_enriquecedor.analizar_convergencia(
                    concepto, 
                    resultado['rutas']
                )
                
                # Actualizar resultado con análisis de Gemini
                resultado['gemini_analisis'] = gemini_analisis
                
                # Si Gemini dice que NO convergen, ajustar resultado
                if not gemini_analisis.get('convergen', True):
                    resultado['es_maximo_relacional'] = False
                    resultado['razon_gemini'] = gemini_analisis.get('razon', '')
                
            except Exception as e:
                print(f"⚠️ Error en Gemini: {e}")
                gemini_analisis = {"error": str(e)}
        
        # 3. Guardar en Neo4j si está habilitado
        neo4j_guardado = False
        if request.usar_neo4j and resultado['es_maximo_relacional']:
            try:
                generador.guardar_maximo_en_neo4j(resultado)
                neo4j_guardado = True
                print(f"✅ Guardado en Neo4j: {concepto}")
            except Exception as e:
                print(f"⚠️ Error guardando en Neo4j: {e}")
        
        # 4. Enviar a n8n en background si está solicitado
        n8n_enviado = False
        if request.enviar_a_n8n and n8n_integrator:
            def enviar_a_n8n_task():
                try:
                    response = n8n_integrator.enviar_datos_webhook(
                        datos={
                            "concepto": concepto,
                            "es_maximo_relacional": resultado['es_maximo_relacional'],
                            "certeza_combinada": resultado['certeza_combinada'],
                            "rutas": resultado['rutas'],
                            "gemini_analisis": gemini_analisis
                        },
                        origen="api_generador"
                    )
                    if response['success']:
                        print(f"✅ Enviado a n8n: {concepto}")
                    else:
                        print(f"⚠️ Error enviando a n8n: {response.get('error')}")
                except Exception as e:
                    print(f"⚠️ Error en tarea n8n: {e}")
            
            background_tasks.add_task(enviar_a_n8n_task)
            n8n_enviado = True
        
        # Calcular tiempo de procesamiento
        tiempo_fin = datetime.now()
        tiempo_ms = int((tiempo_fin - tiempo_inicio).total_seconds() * 1000)
        
        # Construir response
        return MaximoRelacionalResponse(
            concepto=concepto,
            es_maximo_relacional=resultado['es_maximo_relacional'],
            certeza_combinada=resultado['certeza_combinada'],
            similitud_promedio=resultado['similitud_promedio'],
            rutas=resultado['rutas'],
            gemini_analisis=gemini_analisis,
            neo4j_guardado=neo4j_guardado,
            n8n_enviado=n8n_enviado,
            timestamp=tiempo_fin.isoformat(),
            tiempo_procesamiento_ms=tiempo_ms
        )
        
    except Exception as e:
        print(f"❌ Error procesando concepto '{concepto}': {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/generador/verificar-maximo/{concepto}")
async def verificar_maximo(concepto: str):
    """
    Verifica rápidamente si un concepto es máximo relacional (sin generar rutas)
    Solo consulta Neo4j
    """
    if not generador or not generador.driver_neo4j:
        raise HTTPException(
            status_code=503,
            detail="Neo4j no disponible"
        )
    
    concepto_upper = concepto.strip().upper()
    
    try:
        with generador.driver_neo4j.session() as session:
            resultado = session.run(
                """
                MATCH (m:MAXIMO_RELACIONAL {concepto: $concepto})
                RETURN m.certeza_combinada AS certeza,
                       m.similitud_promedio AS similitud,
                       m.timestamp_creacion AS creacion,
                       m.timestamp_actualizacion AS actualizacion
                """,
                concepto=concepto_upper
            )
            
            record = resultado.single()
            
            if record:
                return {
                    "concepto": concepto_upper,
                    "es_maximo_relacional": True,
                    "certeza_combinada": record['certeza'],
                    "similitud_promedio": record['similitud'],
                    "timestamp_creacion": str(record['creacion']),
                    "timestamp_actualizacion": str(record['actualizacion']) if record['actualizacion'] else None,
                    "origen": "neo4j_cache"
                }
            else:
                return {
                    "concepto": concepto_upper,
                    "es_maximo_relacional": False,
                    "mensaje": "No encontrado en caché. Use POST /api/generador/rutas para generar."
                }
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/generador/estadisticas")
async def obtener_estadisticas():
    """Obtiene estadísticas de máximos relacionales en Neo4j"""
    if not generador or not generador.driver_neo4j:
        raise HTTPException(status_code=503, detail="Neo4j no disponible")
    
    try:
        with generador.driver_neo4j.session() as session:
            resultado = session.run(
                """
                MATCH (m:MAXIMO_RELACIONAL)
                RETURN count(m) AS total_maximos,
                       avg(m.certeza_combinada) AS certeza_promedio,
                       max(m.certeza_combinada) AS certeza_maxima,
                       min(m.certeza_combinada) AS certeza_minima
                """
            )
            
            record = resultado.single()
            
            return {
                "total_maximos_relacionales": record['total_maximos'],
                "certeza_promedio": record['certeza_promedio'],
                "certeza_maxima": record['certeza_maxima'],
                "certeza_minima": record['certeza_minima'],
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    
    print("🚀 Iniciando API Generador Máximo Relacional...")
    print("📍 Documentación interactiva: http://localhost:8000/docs")
    print("📍 Endpoint principal: http://localhost:8000/api/generador/rutas")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
