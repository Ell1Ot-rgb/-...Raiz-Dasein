# 🧠 Sistema YO Estructural - Implementación Completa

## 📋 Estructura del Proyecto

```
YO_estructural/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── fenomeno.py
│   │   ├── contexto.py
│   │   └── concepto.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── procesador_fenomenologico.py
│   │   ├── clasificador.py
│   │   ├── extractor_features.py
│   │   └── generador_conceptos.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── webhooks.py
│   └── utils/
│       ├── __init__.py
│       ├── neo4j_client.py
│       └── supabase_client.py
├── scripts/
│   ├── init_db.py
│   └── setup_neo4j.py
└── data/
    ├── entrada_bruta/
    ├── procesado/
    └── logs/
```

## 🐳 Configuración Docker

### Dockerfile

```dockerfile
FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    software-properties-common \
    openjdk-11-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Instalar Neo4j
RUN wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add - && \
    echo 'deb https://debian.neo4j.com stable 4.4' | tee -a /etc/apt/sources.list.d/neo4j.list && \
    apt-get update && \
    apt-get install -y neo4j=1:4.4.* && \
    rm -rf /var/lib/apt/lists/*

# Configurar Neo4j
ENV NEO4J_AUTH=neo4j/fenomenologia2024
ENV NEO4J_dbms_connector_bolt_listen__address=0.0.0.0:7687
ENV NEO4J_dbms_connector_http_listen__address=0.0.0.0:7474

# Configurar directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY app/ ./app/
COPY scripts/ ./scripts/
COPY data/ ./data/

# Crear directorios necesarios
RUN mkdir -p data/entrada_bruta data/procesado data/logs

# Script de inicio
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 8000 7474 7687

CMD ["./start.sh"]
```

### start.sh

```bash
#!/bin/bash

# Iniciar Neo4j en background
neo4j start

# Esperar a que Neo4j esté listo
sleep 30

# Inicializar base de datos
python scripts/init_db.py

# Iniciar aplicación Python
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### requirements.txt

```txt
fastapi==0.104.1
uvicorn==0.24.0
neo4j==5.15.0
supabase==2.1.1
pydantic==2.5.0
python-multipart==0.0.6
python-dotenv==1.0.0
pandas==2.1.4
numpy==1.25.2
scikit-learn==1.3.2
nltk==3.8.1
textblob==0.17.1
requests==2.31.0
aiofiles==0.24.0
```

## ⚙️ Configuración

### .env.example

```env
# Supabase
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=tu_supabase_anon_key
SUPABASE_SERVICE_KEY=tu_supabase_service_key

# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=fenomenologia2024

# API
API_HOST=0.0.0.0
API_PORT=8000
SECRET_KEY=tu_secret_key_super_seguro

# n8n Webhook
N8N_WEBHOOK_URL=https://tu-n8n.render.com/webhook/fenomenologia
```

## 🔧 Código de la Aplicación

### app/config/settings.py

```python
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Supabase
    supabase_url: str
    supabase_key: str
    supabase_service_key: str
    
    # Neo4j
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "fenomenologia2024"
    
    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    secret_key: str
    
    # n8n
    n8n_webhook_url: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### app/models/fenomeno.py

```python
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class FenomenoBase(BaseModel):
    contenido: str
    tipo: str  # texto, imagen, audio, video
    timestamp: datetime
    propiedades: Dict[str, Any] = {}

class Fenomeno(FenomenoBase):
    id: Optional[str] = None
    vector_semantico: Optional[List[float]] = None
    etiquetas: List[str] = []
    
class ContextoFenomenologico(BaseModel):
    id: Optional[str] = None
    estructura: str  # ": - . . . YO ..."
    fenomenos: List[Fenomeno] = []
    yo_emergente: bool = False
    timestamp: datetime
    nivel: int = 1  # 0=fenómeno, 1=contexto, 2=macro, etc.
    
class ConceptoEmergente(BaseModel):
    id: Optional[str] = None
    nombre: str
    nivel: int
    tags: List[str] = []
    origen: str
    parecido_a: List[str] = []
    emergencia_yo: bool = False
    vector_conceptual: Optional[List[float]] = None
```

### app/services/procesador_fenomenologico.py

```python
import re
from typing import List, Dict, Any, Tuple
from datetime import datetime
from app.models.fenomeno import Fenomeno, ContextoFenomenologico, ConceptoEmergente
from app.utils.neo4j_client import Neo4jClient
from app.utils.supabase_client import SupabaseClient

class ProcesadorFenomenologico:
    def __init__(self):
        self.neo4j = Neo4jClient()
        self.supabase = SupabaseClient()
        
    def procesar_entrada_bruta(self, contenido: str, tipo: str = "texto") -> ContextoFenomenologico:
        """
        Procesa entrada bruta y la convierte en estructura : - . . . YO ...
        """
        # Extraer estructura fenomenológica
        estructura = self._extraer_estructura(contenido)
        
        # Crear fenómenos individuales
        fenomenos = self._segmentar_fenomenos(contenido, tipo)
        
        # Detectar emergencia de YO
        yo_emergente = self._detectar_yo_emergente(contenido, fenomenos)
        
        contexto = ContextoFenomenologico(
            estructura=estructura,
            fenomenos=fenomenos,
            yo_emergente=yo_emergente,
            timestamp=datetime.now(),
            nivel=1
        )
        
        return contexto
    
    def _extraer_estructura(self, contenido: str) -> str:
        """
        Convierte texto libre a estructura : - . . . YO ...
        """
        # Detectar inicio de contexto
        inicio = ": -"
        
        # Segmentar fenómenos discretos
        fenomenos_detectados = self._detectar_fenomenos_discretos(contenido)
        fenomenos_str = " ".join([f".{f}" for f in fenomenos_detectados])
        
        # Detectar observador activo
        yo_presente = "YO" if self._hay_autoobservacion(contenido) else ""
        
        # Proyección futura
        proyeccion = "..." if self._hay_incertidumbre(contenido) else ""
        
        return f"{inicio} {fenomenos_str} {yo_presente} {proyeccion}".strip()
    
    def _detectar_fenomenos_discretos(self, contenido: str) -> List[str]:
        """
        Identifica fenómenos discretos en el contenido
        """
        # Palabras clave que indican fenómenos
        palabras_fenomeno = []
        
        # Emociones
        if re.search(r'\b(miedo|alegría|tristeza|ansiedad|calma)\b', contenido, re.IGNORECASE):
            palabras_fenomeno.append("emoción")
            
        # Movimientos
        if re.search(r'\b(correr|caminar|saltar|moverse)\b', contenido, re.IGNORECASE):
            palabras_fenomeno.append("movimiento")
            
        # Sensaciones
        if re.search(r'\b(frío|calor|dolor|placer)\b', contenido, re.IGNORECASE):
            palabras_fenomeno.append("sensación")
            
        # Pensamientos
        if re.search(r'\b(pienso|creo|imagino|recuerdo)\b', contenido, re.IGNORECASE):
            palabras_fenomeno.append("pensamiento")
        
        return palabras_fenomeno if palabras_fenomeno else ["experiencia"]
    
    def _hay_autoobservacion(self, contenido: str) -> bool:
        """
        Detecta si hay autoobservación (emergencia de YO)
        """
        patrones_yo = [
            r'\byo\b',
            r'\bme doy cuenta\b',
            r'\bobservo\b',
            r'\bsiento que\b',
            r'\breflexiono\b'
        ]
        
        return any(re.search(patron, contenido, re.IGNORECASE) for patron in patrones_yo)
    
    def _hay_incertidumbre(self, contenido: str) -> bool:
        """
        Detecta proyección futura o incertidumbre
        """
        patrones_incertidumbre = [
            r'\bquizás\b',
            r'\btal vez\b',
            r'\bpodría\b',
            r'\bno sé\b',
            r'\b\?\b'
        ]
        
        return any(re.search(patron, contenido, re.IGNORECASE) for patron in patrones_incertidumbre)
    
    def _segmentar_fenomenos(self, contenido: str, tipo: str) -> List[Fenomeno]:
        """
        Segmenta el contenido en fenómenos individuales
        """
        fenomenos = []
        
        # Dividir por oraciones o párrafos
        segmentos = re.split(r'[.!?]\s+', contenido)
        
        for i, segmento in enumerate(segmentos):
            if segmento.strip():
                fenomeno = Fenomeno(
                    contenido=segmento.strip(),
                    tipo=tipo,
                    timestamp=datetime.now(),
                    propiedades={
                        "posicion": i,
                        "longitud": len(segmento)
                    }
                )
                fenomenos.append(fenomeno)
        
        return fenomenos
    
    def _detectar_yo_emergente(self, contenido: str, fenomenos: List[Fenomeno]) -> bool:
        """
        Detecta si emerge un YO observador
        """
        # Criterios para emergencia de YO
        tiene_autoobservacion = self._hay_autoobservacion(contenido)
        tiene_reflexion = len(fenomenos) > 2  # Mínimo de fenómenos para reflexión
        tiene_temporalidad = any(palabra in contenido.lower() 
                               for palabra in ['antes', 'después', 'ahora', 'entonces'])
        
        return tiene_autoobservacion and (tiene_reflexion or tiene_temporalidad)
    
    async def guardar_contexto(self, contexto: ContextoFenomenologico) -> str:
        """
        Guarda contexto en Supabase y Neo4j
        """
        # Guardar en Supabase
        contexto_id = await self.supabase.crear_contexto(contexto)
        contexto.id = contexto_id
        
        # Crear nodos en Neo4j
        await self.neo4j.crear_contexto_grafo(contexto)
        
        return contexto_id
    
    async def detectar_patrones(self, contexto: ContextoFenomenologico) -> List[ConceptoEmergente]:
        """
        Detecta patrones y genera conceptos emergentes
        """
        conceptos = []
        
        # Obtener contextos similares
        contextos_similares = await self.supabase.buscar_contextos_similares(contexto)
        
        # Detectar agrupaciones
        if len(contextos_similares) >= 3:
            concepto_agrupacion = ConceptoEmergente(
                nombre=f"patrón_{datetime.now().strftime('%Y%m%d_%H%M')}",
                nivel=1,
                tags=self._extraer_tags_comunes(contextos_similares),
                origen=contexto.id,
                emergencia_yo=contexto.yo_emergente
            )
            conceptos.append(concepto_agrupacion)
        
        # Detectar rupturas
        ruptura = await self._detectar_ruptura(contexto, contextos_similares)
        if ruptura:
            conceptos.append(ruptura)
        
        return conceptos
    
    def _extraer_tags_comunes(self, contextos: List[ContextoFenomenologico]) -> List[str]:
        """
        Extrae tags comunes de un grupo de contextos
        """
        # Implementar lógica de extracción de tags
        tags_comunes = []
        
        # Análisis simple de palabras frecuentes
        todas_palabras = []
        for contexto in contextos:
            for fenomeno in contexto.fenomenos:
                palabras = fenomeno.contenido.lower().split()
                todas_palabras.extend(palabras)
        
        # Contar frecuencias
        from collections import Counter
        contador = Counter(todas_palabras)
        
        # Seleccionar las más frecuentes (excluyendo stop words)
        stop_words = {'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'es', 'se', 'no', 'te', 'lo', 'le', 'da', 'su', 'por', 'son', 'con', 'para', 'al', 'del', 'los', 'las', 'una', 'como', 'pero', 'sus', 'ese', 'esta', 'han', 'si', 'más', 'me', 'ya', 'muy', 'hay', 'estar', 'ser', 'hacer', 'todo', 'este', 'puede', 'mi', 'hasta', 'ver', 'ir', 'dos', 'bien', 'tiempo', 'años', 'año', 'día', 'vez', 'parte', 'cada', 'casa', 'estado', 'vida', 'mundo', 'país', 'agua', 'tierra', 'fuego', 'aire'}
        
        for palabra, freq in contador.most_common(5):
            if palabra not in stop_words and len(palabra) > 3:
                tags_comunes.append(palabra)
        
        return tags_comunes
    
    async def _detectar_ruptura(self, contexto: ContextoFenomenologico, contextos_similares: List[ContextoFenomenologico]) -> ConceptoEmergente:
        """
        Detecta si el contexto actual representa una ruptura de patrón
        """
        if not contextos_similares:
            return None
            
        # Comparar estructura
        estructura_actual = contexto.estructura
        estructuras_previas = [c.estructura for c in contextos_similares]
        
        # Si la estructura es muy diferente, puede ser una ruptura
        similitud_promedio = self._calcular_similitud_estructura(estructura_actual, estructuras_previas)
        
        if similitud_promedio < 0.3:  # Umbral de ruptura
            ruptura = ConceptoEmergente(
                nombre=f"ruptura_{datetime.now().strftime('%Y%m%d_%H%M')}",
                nivel=1,
                tags=["ruptura", "cambio", "emergencia"],
                origen=contexto.id,
                emergencia_yo=True  # Las rupturas suelen generar autoobservación
            )
            return ruptura
        
        return None
    
    def _calcular_similitud_estructura(self, estructura_actual: str, estructuras_previas: List[str]) -> float:
        """
        Calcula similitud promedio entre estructuras
        """
        if not estructuras_previas:
            return 0.0
        
        from difflib import SequenceMatcher
        
        similitudes = []
        for estructura_previa in estructuras_previas:
            similitud = SequenceMatcher(None, estructura_actual, estructura_previa).ratio()
            similitudes.append(similitud)
        
        return sum(similitudes) / len(similitudes)
```

### app/utils/neo4j_client.py

```python
from neo4j import GraphDatabase
from typing import List, Dict, Any
from app.config.settings import settings
from app.models.fenomeno import ContextoFenomenologico, Fenomeno, ConceptoEmergente

class Neo4jClient:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            settings.neo4j_uri,
            auth=(settings.neo4j_user, settings.neo4j_password)
        )
    
    def close(self):
        self.driver.close()
    
    async def crear_contexto_grafo(self, contexto: ContextoFenomenologico):
        """
        Crea el contexto y sus relaciones en Neo4j
        """
        with self.driver.session() as session:
            # Crear nodo Contexto
            session.run(
                """
                CREATE (c:Contexto {
                    id: $id,
                    estructura: $estructura,
                    timestamp: $timestamp,
                    nivel: $nivel,
                    yo_emergente: $yo_emergente
                })
                """,
                id=contexto.id,
                estructura=contexto.estructura,
                timestamp=contexto.timestamp.isoformat(),
                nivel=contexto.nivel,
                yo_emergente=contexto.yo_emergente
            )
            
            # Crear nodos Fenómeno y relaciones
            for i, fenomeno in enumerate(contexto.fenomenos):
                fenomeno_id = f"{contexto.id}_fenomeno_{i}"
                
                # Crear nodo Fenómeno
                session.run(
                    """
                    CREATE (f:Fenomeno {
                        id: $id,
                        contenido: $contenido,
                        tipo: $tipo,
                        timestamp: $timestamp,
                        posicion: $posicion
                    })
                    """,
                    id=fenomeno_id,
                    contenido=fenomeno.contenido,
                    tipo=fenomeno.tipo,
                    timestamp=fenomeno.timestamp.isoformat(),
                    posicion=i
                )
                
                # Crear relación CONTIENE
                session.run(
                    """
                    MATCH (c:Contexto {id: $contexto_id})
                    MATCH (f:Fenomeno {id: $fenomeno_id})
                    CREATE (c)-[:CONTIENE {posicion: $posicion}]->(f)
                    """,
                    contexto_id=contexto.id,
                    fenomeno_id=fenomeno_id,
                    posicion=i
                )
            
            # Si hay YO emergente, crear nodo YO
            if contexto.yo_emergente:
                yo_id = f"{contexto.id}_yo"
                session.run(
                    """
                    CREATE (y:YO {
                        id: $id,
                        contexto_origen: $contexto_id,
                        timestamp: $timestamp
                    })
                    """,
                    id=yo_id,
                    contexto_id=contexto.id,
                    timestamp=contexto.timestamp.isoformat()
                )
                
                # Crear relación OBSERVA
                session.run(
                    """
                    MATCH (y:YO {id: $yo_id})
                    MATCH (c:Contexto {id: $contexto_id})
                    CREATE (y)-[:OBSERVA]->(c)
                    """,
                    yo_id=yo_id,
                    contexto_id=contexto.id
                )
    
    async def crear_concepto_grafo(self, concepto: ConceptoEmergente):
        """
        Crea concepto emergente en Neo4j
        """
        with self.driver.session() as session:
            # Crear nodo Concepto
            session.run(
                """
                CREATE (c:Concepto {
                    id: $id,
                    nombre: $nombre,
                    nivel: $nivel,
                    tags: $tags,
                    origen: $origen,
                    emergencia_yo: $emergencia_yo
                })
                """,
                id=concepto.id,
                nombre=concepto.nombre,
                nivel=concepto.nivel,
                tags=concepto.tags,
                origen=concepto.origen,
                emergencia_yo=concepto.emergencia_yo
            )
            
            # Crear relación EMERGE_DE
            session.run(
                """
                MATCH (c:Concepto {id: $concepto_id})
                MATCH (ctx:Contexto {id: $contexto_id})
                CREATE (c)-[:EMERGE_DE]->(ctx)
                """,
                concepto_id=concepto.id,
                contexto_id=concepto.origen
            )
    
    async def buscar_contextos_relacionados(self, contexto_id: str) -> List[Dict]:
        """
        Busca contextos relacionados en el grafo
        """
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (c1:Contexto {id: $contexto_id})
                MATCH (c2:Contexto)
                WHERE c1 <> c2
                OPTIONAL MATCH path = (c1)-[*1..2]-(c2)
                WITH c2, length(path) as distancia
                ORDER BY distancia ASC
                LIMIT 10
                RETURN c2.id as id, c2.estructura as estructura, 
                       c2.yo_emergente as yo_emergente, distancia
                """,
                contexto_id=contexto_id
            )
            
            return [record.data() for record in result]
    
    async def obtener_estadisticas_grafo(self) -> Dict[str, int]:
        """
        Obtiene estadísticas del grafo
        """
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (c:Contexto) 
                OPTIONAL MATCH (f:Fenomeno)
                OPTIONAL MATCH (y:YO)
                OPTIONAL MATCH (con:Concepto)
                RETURN 
                    count(DISTINCT c) as contextos,
                    count(DISTINCT f) as fenomenos,
                    count(DISTINCT y) as yos,
                    count(DISTINCT con) as conceptos
                """
            )
            
            record = result.single()
            return {
                "contextos": record["contextos"],
                "fenomenos": record["fenomenos"],
                "yos": record["yos"],
                "conceptos": record["conceptos"]
            }
```

### app/utils/supabase_client.py

```python
from supabase import create_client, Client
from typing import List, Dict, Any, Optional
from app.config.settings import settings
from app.models.fenomeno import ContextoFenomenologico, ConceptoEmergente
from datetime import datetime

class SupabaseClient:
    def __init__(self):
        self.client: Client = create_client(
            settings.supabase_url,
            settings.supabase_key
        )
    
    async def crear_contexto(self, contexto: ContextoFenomenologico) -> str:
        """
        Crea un contexto en Supabase
        """
        data = {
            "estructura": contexto.estructura,
            "nivel": contexto.nivel,
            "yo_emergente": contexto.yo_emergente,
            "timestamp": contexto.timestamp.isoformat(),
            "fenomenos_count": len(contexto.fenomenos),
            "metadata": {
                "fenomenos": [
                    {
                        "contenido": f.contenido,
                        "tipo": f.tipo,
                        "propiedades": f.propiedades
                    } for f in contexto.fenomenos
                ]
            }
        }
        
        result = self.client.table("contextos").insert(data).execute()
        return result.data[0]["id"]
    
    async def crear_concepto(self, concepto: ConceptoEmergente) -> str:
        """
        Crea un concepto emergente en Supabase
        """
        data = {
            "nombre": concepto.nombre,
            "nivel": concepto.nivel,
            "tags": concepto.tags,
            "origen": concepto.origen,
            "parecido_a": concepto.parecido_a,
            "emergencia_yo": concepto.emergencia_yo,
            "timestamp": datetime.now().isoformat()
        }
        
        result = self.client.table("conceptos").insert(data).execute()
        return result.data[0]["id"]
    
    async def buscar_contextos_similares(self, contexto: ContextoFenomenologico, limite: int = 5) -> List[ContextoFenomenologico]:
        """
        Busca contextos similares basándose en la estructura
        """
        # Búsqueda por similitud de estructura
        result = self.client.table("contextos")\
            .select("*")\
            .eq("nivel", contexto.nivel)\
            .limit(limite)\
            .execute()
        
        contextos_similares = []
        for record in result.data:
            # Reconstruir objeto ContextoFenomenologico
            ctx = ContextoFenomenologico(
                id=record["id"],
                estructura=record["estructura"],
                nivel=record["nivel"],
                yo_emergente=record["yo_emergente"],
                timestamp=datetime.fromisoformat(record["timestamp"]),
                fenomenos=[]  # Simplificado para búsqueda
            )
            contextos_similares.append(ctx)
        
        return contextos_similares
    
    async def obtener_contexto(self, contexto_id: str) -> Optional[ContextoFenomenologico]:
        """
        Obtiene un contexto por ID
        """
        result = self.client.table("contextos")\
            .select("*")\
            .eq("id", contexto_id)\
            .single()\
            .execute()
        
        if result.data:
            record = result.data
            return ContextoFenomenologico(
                id=record["id"],
                estructura=record["estructura"],
                nivel=record["nivel"],
                yo_emergente=record["yo_emergente"],
                timestamp=datetime.fromisoformat(record["timestamp"]),
                fenomenos=[]  # Reconstruir si es necesario
            )
        
        return None
    
    async def obtener_estadisticas(self) -> Dict[str, int]:
        """
        Obtiene estadísticas de Supabase
        """
        # Contar contextos
        contextos_result = self.client.table("contextos").select("id", count="exact").execute()
        contextos_count = contextos_result.count
        
        # Contar conceptos
        conceptos_result = self.client.table("conceptos").select("id", count="exact").execute()
        conceptos_count = conceptos_result.count
        
        # Contar contextos con YO emergente
        yo_result = self.client.table("contextos")\
            .select("id", count="exact")\
            .eq("yo_emergente", True)\
            .execute()
        yo_count = yo_result.count
        
        return {
            "contextos_totales": contextos_count,
            "conceptos_emergentes": conceptos_count,
            "yo_emergentes": yo_count,
            "tasa_emergencia_yo": yo_count / contextos_count if contextos_count > 0 else 0
        }
```

### app/api/webhooks.py

```python
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from app.services.procesador_fenomenologico import ProcesadorFenomenologico
from app.utils.neo4j_client import Neo4jClient
from app.utils.supabase_client import SupabaseClient
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

class WebhookData(BaseModel):
    contenido: str
    tipo: str = "texto"
    metadata: Optional[Dict[str, Any]] = {}
    fuente: str = "n8n"

class ResponseWebhook(BaseModel):
    status: str
    contexto_id: str
    estructura: str
    conceptos_emergentes: List[str] = []
    yo_emergente: bool = False

@router.post("/webhook/fenomenologia", response_model=ResponseWebhook)
async def procesar_fenomenologia(
    data: WebhookData,
    background_tasks: BackgroundTasks
):
    """
    Webhook principal para recibir datos fenomenológicos desde n8n
    """
    try:
        logger.info(f"Recibiendo datos de {data.fuente}: {data.tipo}")
        
        # Inicializar procesador
        procesador = ProcesadorFenomenologico()
        
        # Procesar entrada bruta
        contexto = procesador.procesar_entrada_bruta(data.contenido, data.tipo)
        
        # Guardar contexto
        contexto_id = await procesador.guardar_contexto(contexto)
        
        # Detectar patrones en background
        background_tasks.add_task(
            procesar_patrones_background,
            contexto_id,
            contexto
        )
        
        # Respuesta inmediata
        return ResponseWebhook(
            status="procesado",
            contexto_id=contexto_id,
            estructura=contexto.estructura,
            yo_emergente=contexto.yo_emergente
        )
        
    except Exception as e:
        logger.error(f"Error procesando webhook: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/webhook/batch")
async def procesar_batch_fenomenologia(
    datos: List[WebhookData],
    background_tasks: BackgroundTasks
):
    """
    Procesa múltiples entradas fenomenológicas en batch
    """
    try:
        procesador = ProcesadorFenomenologico()
        resultados = []
        
        for data in datos:
            contexto = procesador.procesar_entrada_bruta(data.contenido, data.tipo)
            contexto_id = await procesador.guardar_contexto(contexto)
            
            resultados.append({
                "contexto_id": contexto_id,
                "estructura": contexto.estructura,
                "yo_emergente": contexto.yo_emergente
            })
        
        # Procesar patrones globales en background
        background_tasks.add_task(
            analizar_patrones_globales,
            [r["contexto_id"] for r in resultados]
        )
        
        return {
            "status": "batch_procesado",
            "total": len(resultados),
            "resultados": resultados
        }
        
    except Exception as e:
        logger.error(f"Error procesando batch: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
async def obtener_status():
    """
    Obtiene el estado actual del sistema
    """
    try:
        supabase = SupabaseClient()
        neo4j = Neo4jClient()
        
        # Estadísticas de Supabase
        stats_supabase = await supabase.obtener_estadisticas()
        
        # Estadísticas de Neo4j
        stats_neo4j = await neo4j.obtener_estadisticas_grafo()
        
        return {
            "status": "activo",
            "supabase": stats_supabase,
            "neo4j": stats_neo4j,
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"Error obteniendo status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/contexto/{contexto_id}")
async def obtener_contexto(contexto_id: str):
    """
    Obtiene un contexto específico con sus relaciones
    """
    try:
        supabase = SupabaseClient()
        neo4j = Neo4jClient()
        
        # Obtener contexto de Supabase
        contexto = await supabase.obtener_contexto(contexto_id)
        if not contexto:
            raise HTTPException(status_code=404, detail="Contexto no encontrado")
        
        # Obtener relaciones de Neo4j
        relaciones = await neo4j.buscar_contextos_relacionados(contexto_id)
        
        return {
            "contexto": contexto.dict(),
            "relaciones": relaciones
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error obteniendo contexto: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

async def procesar_patrones_background(contexto_id: str, contexto):
    """
    Procesa patrones y conceptos emergentes en background
    """
    try:
        procesador = ProcesadorFenomenologico()
        
        # Detectar patrones
        conceptos = await procesador.detectar_patrones(contexto)
        
        # Guardar conceptos emergentes
        for concepto in conceptos:
            concepto_id = await procesador.supabase.crear_concepto(concepto)
            concepto.id = concepto_id
            await procesador.neo4j.crear_concepto_grafo(concepto)
        
        logger.info(f"Procesados {len(conceptos)} conceptos para contexto {contexto_id}")
        
    except Exception as e:
        logger.error(f"Error procesando patrones background: {str(e)}")

async def analizar_patrones_globales(contextos_ids: List[str]):
    """
    Analiza patrones globales entre múltiples contextos
    """
    try:
        # Implementar análisis de patrones globales
        logger.info(f"Analizando patrones globales para {len(contextos_ids)} contextos")
        
        # Aquí iría la lógica de análisis de macrocontextos
        # y detección de ontosistemas emergentes
        
    except Exception as e:
        logger.error(f"Error analizando patrones globales: {str(e)}")
```

### app/main.py

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
from datetime import datetime
from app.api.webhooks import router as webhooks_router
from app.config.settings import settings

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Crear aplicación FastAPI
app = FastAPI(
    title="Sistema YO Estructural",
    description="Sistema fenomenológico estructural para procesamiento de datos",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(webhooks_router, prefix="/api/v1")

@app.get("/")
async def root():
    """
    Endpoint raíz con información del sistema
    """
    return {
        "sistema": "YO Estructural",
        "version": "1.0.0",
        "descripcion": "Sistema fenomenológico estructural",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "webhook_principal": "/api/v1/webhook/fenomenologia",
            "webhook_batch": "/api/v1/webhook/batch",
            "status": "/api/v1/status",
            "contexto": "/api/v1/contexto/{contexto_id}"
        }
    }

@app.get("/health")
async def health_check():
    """
    Health check para monitoreo
    """
    try:
        # Verificar conexiones
        from app.utils.supabase_client import SupabaseClient
        from app.utils.neo4j_client import Neo4jClient
        
        supabase = SupabaseClient()
        neo4j = Neo4jClient()
        
        # Test básico de conexiones
        supabase_ok = True
        neo4j_ok = True
        
        try:
            await supabase.obtener_estadisticas()
        except:
            supabase_ok = False
            
        try:
            await neo4j.obtener_estadisticas_grafo()
        except:
            neo4j_ok = False
        
        status = "healthy" if (supabase_ok and neo4j_ok) else "degraded"
        
        return {
            "status": status,
            "timestamp": datetime.now().isoformat(),
            "services": {
                "supabase": "ok" if supabase_ok else "error",
                "neo4j": "ok" if neo4j_ok else "error"
            }
        }
        
    except Exception as e:
        logger.error(f"Error en health check: {str(e)}")
        return JSONResponse(
            status_code=503,
            content={
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
        )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """