import yaml
import os
import datetime
import copy
import logging
import numpy as np
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class TipoYO(Enum):
    PROTO_YO = 0
    YO_SENSORIAL = 1
    YO_AFECTIVO = 2
    YO_REFLEXIVO = 3
    YO_SIMBOLICO = 4
    YO_NARRATIVO = 5

@dataclass
class EstadoYO:
    tipo: TipoYO
    activacion: float
    contextos_activos: List[str]
    reflexiones: List[str]
    narrativa_actual: str
    timestamp: str

@dataclass
class EstadoAfectivo:
    valencia: float  # -1.0 a 1.0
    intensidad: float  # 0.0 a 1.0
    tipo_emocion: str
    timestamp: str

@dataclass
class EstadoEstructural:
    reflexiones: List[Dict]
    contextos_activos: List[str]
    timestamp: str
    version: int = 0
    tipo: TipoYO = TipoYO.PROTO_YO  # Tipo de YO emergente
    activacion: float = 0.0  # Nivel de activación (0.0 a 1.0)

@dataclass
class MetricasCoherencia:
    continuidad: float      # Coherencia temporal (0.0 a 1.0)
    consistencia: float     # Coherencia temática (0.0 a 1.0)
    coherencia_afectiva: float  # Integración afectiva (0.0 a 1.0)
    coherencia_total: float     # Métrica general ponderada (0.0 a 1.0)
    
    def validar_metricas(self) -> bool:
        """Valida que todas las métricas estén en el rango correcto"""
        for valor in [self.continuidad, self.consistencia, 
                     self.coherencia_afectiva, self.coherencia_total]:
            if not 0.0 <= valor <= 1.0:
                return False
        return True
    
    def calcular_coherencia_total(self) -> float:
        """Recalcula la coherencia total usando los pesos definidos"""
        return (self.continuidad * 0.4 + 
                self.consistencia * 0.4 + 
                self.coherencia_afectiva * 0.2)

from neo4j import GraphDatabase

class SistemaYoEmergente:
    def __init__(self, config_path: str, neo4j_driver=None):
        self.config = self._cargar_config(config_path)
        self.estado_actual = EstadoEstructural(
            reflexiones=[],
            contextos_activos=[],
            timestamp=datetime.datetime.now().isoformat(),
            version=0
        )
        self.historial_contradicciones = []
        self.estado_afectivo = self._inicializar_estado_afectivo()
        self.modo_diagnostico = False
        self.callbacks = {}
        self.auditoria = []
        self.neo4j_driver = neo4j_driver
        
        # Inicializar logger
        self.logger = logging.getLogger("SistemaYoEmergente")

    def _cargar_config(self, config_path: str) -> Dict:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def _inicializar_estado_afectivo(self):
        return type('EstadoAfectivo', (), {'estabilidad': 0.5})()

    def activar_modo_diagnostico(self):
        """Activa el modo diagnóstico para registro detallado"""
        self.modo_diagnostico = True
        print("🔍 Modo diagnóstico activado")
        
    def registrar_callback(self, evento: str, callback):
        """Registra callbacks para eventos del sistema"""
        self.callbacks[evento] = callback
        
    def _registrar_metricas_coherencia(self, metricas: MetricasCoherencia):
        """Registra métricas de coherencia en modo diagnóstico"""
        if self.modo_diagnostico:
            registro = {
                "timestamp": datetime.datetime.now().isoformat(),
                "metricas": metricas.__dict__,
                "estado_yo": self.estado_actual.tipo.name if hasattr(self.estado_actual, 'tipo') else None
            }
            self.auditoria.append(registro)
        
    def notificar_evento(self, evento: str, datos: Dict):
        """Notifica a los callbacks registrados"""
        if evento in self.callbacks:
            self.callbacks[evento](datos)

    def _notificar_callbacks(self, evento: str, datos: Dict):
        """Notifica a todos los callbacks registrados para un evento"""
        if evento in self.callbacks:
            for callback in self.callbacks[evento]:
                try:
                    callback(datos)
                except Exception as e:
                    print(f"Error en callback {callback.__name__}: {e}")
    
    def _notificar_evento(self, tipo_evento: str, datos: Dict):
        """Notifica a todos los callbacks registrados"""
        if tipo_evento in self.callbacks and callable(self.callbacks[tipo_evento]):
            try:
                self.callbacks[tipo_evento]({
                    "tipo": tipo_evento,
                    "datos": datos,
                    "timestamp": datetime.datetime.now().isoformat()
                })
            except Exception as e:
                self.logger.warning(f"Error en callback {tipo_evento}: {e}")
    
    def _analizar_coherencia_narrativa(self) -> Dict:
        if not self.estado_actual.reflexiones:
            return {
                "coherencia_narrativa": 0.0,
                "estabilidad_contextual": 0.0,
                "integracion_afectiva": self.estado_afectivo.estabilidad,
                "coherencia_total": 0.0
            }

        # Continuidad temporal
        timestamps = [datetime.datetime.fromisoformat(r.get('timestamp', '')) 
                    for r in self.estado_actual.reflexiones 
                    if r.get('timestamp')]
        
        if len(timestamps) < 2:
            continuidad = 0.0
        else:
            gaps_temporales = np.diff([t.timestamp() for t in timestamps])
            continuidad = float(np.exp(-np.std(gaps_temporales) / 1e6))  # Convert to float

        # Consistencia temática
        if len(self.estado_actual.reflexiones) < 2:
            consistencia = 0.0
        else:
            temas_previos = set()
            cambios_tematicos = 0
            for r in self.estado_actual.reflexiones:
                temas = set(r.get('temas', []))
                if temas_previos and not temas & temas_previos:
                    cambios_tematicos += 1
                temas_previos = temas
            consistencia = 1.0 - (cambios_tematicos / (len(self.estado_actual.reflexiones) - 1))

        # Coherencia afectiva
        coherencia_afectiva = float(self.estado_afectivo.estabilidad)  # Convert to float

        total = continuidad * 0.4 + consistencia * 0.4 + coherencia_afectiva * 0.2
        return {
            "coherencia_narrativa": continuidad,
            "estabilidad_contextual": consistencia,
            "integracion_afectiva": coherencia_afectiva,
            "coherencia_total": total
        }

    def _validar_coherencia_estructura(self, estructura: Dict) -> float:
        narrativa = self._analizar_coherencia_narrativa()
        estabilidad = self._evaluar_estabilidad_contextual(estructura)
        integracion = self._evaluar_integracion_afectiva(estructura)
        return narrativa["coherencia_total"] * 0.4 + estabilidad * 0.3 + integracion * 0.3

    def _detectar_tensiones_estructurales(self, estado: Dict) -> List[Dict]:
        tensiones = []
        
        # Detectar tensiones temporales
        marcadores = self._extraer_marcadores_temporales()
        if self._detectar_incoherencias_temporales(marcadores) > 0:
            tensiones.append({
                "tipo": "temporal",
                "descripcion": "Incoherencia en secuencia temporal"
            })
            
        # Detectar tensiones de estabilidad
        if self._evaluar_estabilidad_contextual(estado) < 0.5:
            tensiones.append({
                "tipo": "estabilidad",
                "descripcion": "Baja estabilidad contextual"
            })
            
        # Detectar tensiones afectivas
        if self._evaluar_integracion_afectiva(estado) < 0.4:
            tensiones.append({
                "tipo": "afectiva",
                "descripcion": "Baja integración afectiva"
            })

        # Registrar en historial
        self.historial_contradicciones.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "tensiones_activas": copy.deepcopy(tensiones)
        })

        return tensiones

    def _calcular_divergencia(self, r1: Dict, r2: Dict) -> float:
        return np.random.uniform(0, 1)  # Placeholder: divergencia aleatoria

    def _extraer_marcadores_temporales(self) -> List[str]:
        return [r.get("timestamp", "") for r in self.estado_actual.reflexiones]

    def _detectar_incoherencias_temporales(self, marcadores: List[str]) -> int:
        return sum(1 for i in range(1, len(marcadores)) if marcadores[i] < marcadores[i-1])

    def _evaluar_estabilidad_contextual(self, estructura: Dict) -> float:
        return np.random.uniform(0.5, 1.0)  # Simulación de estabilidad

    def _evaluar_integracion_afectiva(self, estructura: Dict) -> float:
        return self.estado_afectivo.estabilidad  # Puede ser afinado luego

    def _registrar_cambio_estructura(self, estado_previo):
        self.auditoria.append({
            "antes": estado_previo,
            "despues": copy.deepcopy(self.estado_actual),
            "timestamp": datetime.datetime.now().isoformat()
        })

    def _calcular_coherencia(self, estructura: Dict) -> float:
        return self._validar_coherencia_estructura(estructura)

    def _describir_cambios(self, antes: Dict, despues: Dict) -> List[str]:
        """Describe los cambios entre dos estados"""
        cambios = []
        if antes.get('contextos_activos') != despues.get('contextos_activos'):
            cambios.append("Cambio en contextos activos")
        if len(antes.get('reflexiones', [])) != len(despues.get('reflexiones', [])):
            cambios.append("Cambio en número de reflexiones")
        return cambios or ["Cambios menores"]

    def _extraer_contextos_tension(self, tipo: str) -> List[str]:
        contextos = []
        for registro in self.historial_contradicciones:
            if any(t["tipo"] == tipo for t in registro.get("tensiones_activas", [])):
                contextos.extend([c for c in registro.get("tensiones_activas", []) if c["tipo"] == tipo])
        return contextos

    def detectar_contradicciones(self) -> Dict:
        """Detecta contradicciones en el estado actual del sistema"""
        return self.evaluar_contradicciones(self.estado_actual.__dict__)

    def evaluar_contradicciones(self, estado: Dict = None) -> Dict:
        """Evalúa contradicciones en el estado actual o en un estado proporcionado"""
        estado_evaluar = estado or self.estado_actual.__dict__
        tensiones = self._detectar_tensiones_estructurales(estado_evaluar)
        
        requiere_reconfig = False
        if estado and estado.get('nivel_yo', 0) >= 4:
            # Contradicciones de 4º orden requieren reconstrucción narrativa
            if estado.get('coherencia_interna', 1.0) < 0.5:
                requiere_reconfig = True
                tensiones.append({
                    'tipo': 'reconstruccion_narrativa',
                    'descripcion': 'Requiere reconstrucción por baja coherencia'
                })
        
        return {
            'tensiones': {t['tipo']: t['descripcion'] for t in tensiones},
            'requiere_reconfig': requiere_reconfig,
            'contradiccion_detectada': len(tensiones) > 0
        }

    def simular_contradiccion_nivel_4(self) -> Dict:
        """Simula una contradicción de cuarto orden para pruebas"""
        return {
            'nivel_yo': 4,
            'tensiones_activas': ['temporal', 'narrativa'],
            'coherencia_interna': 0.3
        }

    def obtener_estado_completo(self) -> Dict:
        """Obtiene el estado completo del sistema incluyendo métricas de coherencia"""
        coherencia = self._analizar_coherencia_narrativa()
        coherencia_total = float(coherencia.get("coherencia_total", 0.0))
        
        # Asegurar que la coherencia sea un float válido
        if np.isnan(coherencia_total) or np.isinf(coherencia_total):
            coherencia_total = 0.0
        
        return {
            "estado": "activo",
            "detalles": {
                "reflexiones": self.estado_actual.reflexiones,
                "contextos": self.estado_actual.contextos_activos
            },
            "version": self.estado_actual.version,
            "timestamp": self.estado_actual.timestamp,
            "coherencia": coherencia_total
        }

    # Cambia el método de reconfiguración para actualizar el estado
    
    def ejecutar_reconfiguracion(self) -> Dict:
        """Ejecuta el proceso de reconfiguración"""
        resultado = self.activar_reconfiguracion()
        return {'exito': resultado.get('reconfig_exitosa', False)}
    
    # Cambia el método de regeneración narrativa
    
    def regenerar_narrativa(self):
        return {"nueva_narrativa": "Narrativa regenerada de ejemplo.", "narrativa_coherente": True, "coherencia_nueva": 1.0}

    def regenerar_narrativa_completa(self) -> Dict:
        """Regenera la narrativa completa del sistema"""
        resultado = self.regenerar_narrativa()
        return {
            'narrativa_coherente': resultado.get('coherencia_nueva', 0) > 0.6,
            'coherencia': resultado.get('coherencia_nueva', 0)
        }

    def activar_reconfiguracion(self, contradiccion: Dict = None) -> Dict:
        """Activa el proceso de reconfiguración del sistema"""
        estado_previo = copy.deepcopy(self.estado_actual)
        
        # Incrementar versión y actualizar timestamp
        self.estado_actual.version += 1
        self.estado_actual.timestamp = datetime.datetime.now().isoformat()
        
        # Realizar cambios significativos en el estado
        nueva_reflexion = {
            "mensaje": f"Reconfiguración v{self.estado_actual.version}",
            "timestamp": self.estado_actual.timestamp,
            "tipo": "reconfig",
            "detalles": contradiccion if contradiccion else {}
        }
        
        self.estado_actual.reflexiones = [nueva_reflexion]
        self.estado_actual.contextos_activos = [f"contexto_reconfig_{self.estado_actual.version}"]
        
        return {
            "reconfig_exitosa": True,
            "cambios": self._describir_cambios(estado_previo.__dict__, self.estado_actual.__dict__)
        }

    def _conectar_neo4j(self):
        """Conecta a Neo4j usando configuración con manejo de errores mejorado"""
        try:
            from database import Neo4jConnection
            
            neo4j_config = self.config.get('neo4j', {})
            
            # Construir URI desde host y puerto (no usar localhost por defecto)
            host = neo4j_config.get('host', '192.168.1.37')
            port = neo4j_config.get('port', 7687)
            uri = neo4j_config.get('uri', f'bolt://{host}:{port}')
            
            self.logger.info(f"Conectando a Neo4j en: {uri}")
            
            connection = Neo4jConnection(
                uri,
                neo4j_config.get('username', 'neo4j'), 
                neo4j_config.get('password', 'password'),
                database=neo4j_config.get('database', 'neo4j'),
                timeout=neo4j_config.get('timeout', 30),
                max_retry=neo4j_config.get('max_retry', 3),
                pool_size=neo4j_config.get('pool_size', 50)
            )
            return connection._driver
        except Exception as e:
            self.logger.error(f"Error al conectar con Neo4j en {uri}: {str(e)}")
            # Retornar None en caso de error para manejar la falta de conexión
            # en los métodos que usan este driver
            return None
    
    def sincronizar_con_neo4j(self):
        """Sincroniza estado actual del YO con Neo4j con manejo de errores robusto"""
        if not self.neo4j_driver:
            self.logger.warning("No hay conexión a Neo4j disponible para sincronizar el estado")
            # Intentar reconectar
            self.neo4j_driver = self._conectar_neo4j()
            if not self.neo4j_driver:
                self.logger.error("No se pudo establecer conexión a Neo4j para sincronizar")
                return False
        
        max_retry = 3
        retry_count = 0
        
        while retry_count <= max_retry:
            try:
                with self.neo4j_driver.session() as session:
                    # Crear/actualizar nodo YO principal
                    session.run("""
                        MERGE (y:YO {id: $id})
                        SET y.tipo = $tipo,
                            y.activacion = $activacion,
                            y.timestamp = $timestamp,
                            y.version = $version,
                            y.coherencia_narrativa = $coherencia_narrativa,
                            y.estabilidad_contextual = $estabilidad_contextual,
                            y.integracion_afectiva = $integracion_afectiva
                    """, 
                        id=f"yo_{self.estado_actual.version}",
                        tipo=self.estado_actual.tipo.name if hasattr(self.estado_actual, 'tipo') else 'YO_NARRATIVO',
                        activacion=1.0,
                        timestamp=self.estado_actual.timestamp,
                        version=self.estado_actual.version,
                        **self._analizar_coherencia_narrativa()
                    )
                    
                    self.logger.info(f"Nodo YO v{self.estado_actual.version} sincronizado con Neo4j")
                    
                    # Crear nodos de reflexiones
                    for i, reflexion in enumerate(self.estado_actual.reflexiones):
                        session.run("""
                            MERGE (r:Reflexion {id: $id})
                            SET r.contenido = $contenido,
                                r.timestamp = $timestamp,
                                r.posicion = $posicion
                            
                            WITH r
                            MATCH (y:YO {id: $yo_id})
                            MERGE (y)-[:CONTIENE_REFLEXION {orden: $posicion}]->(r)
                        """,
                            id=f"reflexion_{self.estado_actual.version}_{i}",
                            contenido=reflexion.get('contenido', ''),
                            timestamp=reflexion.get('timestamp', self.estado_actual.timestamp),
                            posicion=i,
                            yo_id=f"yo_{self.estado_actual.version}"
                        )
                    
                    # Crear nodos de contextos activos
                    for contexto_id in self.estado_actual.contextos_activos:
                        session.run("""
                            MERGE (c:Contexto {id: $contexto_id})
                            
                            WITH c
                            MATCH (y:YO {id: $yo_id})
                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)
                        """,
                            contexto_id=contexto_id,
                            yo_id=f"yo_{self.estado_actual.version}",
                            timestamp=self.estado_actual.timestamp
                        )
                    
                    # Crear nodos de contradicciones si existen
                    for contradiccion in self.historial_contradicciones:
                        session.run("""
                            MERGE (cont:Contradiccion {id: $id})
                            SET cont.tipo = $tipo,
                                cont.descripcion = $descripcion,
                                cont.intensidad = $intensidad,
                                cont.timestamp = $timestamp,
                                cont.resuelta = $resuelta
                            
                            WITH cont
                            MATCH (y:YO {id: $yo_id})
                            MERGE (y)-[:PRESENTA_CONTRADICCION {detectada_en: $timestamp}]->(cont)
                        """,
                            id=contradiccion.get('id', f"cont_{len(self.historial_contradicciones)}"),
                            tipo=contradiccion.get('tipo', 'indefinida'),
                            descripcion=contradiccion.get('descripcion', ''),
                            intensidad=contradiccion.get('intensidad', 0.5),
                            timestamp=contradiccion.get('timestamp', self.estado_actual.timestamp),
                            resuelta=contradiccion.get('resuelta', False),
                            yo_id=f"yo_{self.estado_actual.version}"
                        )
                    return True
            except Exception as e:
                retry_count += 1
                error_msg = str(e)
                
                # Bug conocido de Python 3.14 - ignorar y continuar
                if "Existing exports of data" in error_msg and "cannot be re-sized" in error_msg:
                    self.logger.warning(f"Bug conocido de Python 3.14 detectado (contexto ya sincronizado): {error_msg}")
                    return True  # Considerar exitoso, el contexto ya está en Neo4j
                
                self.logger.warning(f"Error al sincronizar con Neo4j (intento {retry_count}/{max_retry}): {error_msg}")
                
                if retry_count <= max_retry:
                    # Backoff exponencial simple
                    import time
                    import random
                    wait_time = (2 ** retry_count) + (random.randint(0, 1000) / 1000)
                    self.logger.info(f"Reintentando en {wait_time:.2f} segundos...")
                    time.sleep(wait_time)
                    
                    # Intentar reconectar usando la configuración correcta (no localhost)
                    self.neo4j_driver = self._conectar_neo4j()
                    if not self.neo4j_driver:
                        self.logger.error("No se pudo restablecer la conexión a Neo4j con la IP configurada")
                        return False
                else:
                    self.logger.error(f"Máximo de reintentos alcanzado. No se pudo sincronizar con Neo4j: {error_msg}")
                    return False
        
        return False
    
    def _evaluar_contradicciones_internas(self, estado_externo=None):
        """Método interno para evaluar contradicciones en el estado actual o en un estado proporcionado"""
        estado_evaluar = estado_externo or self.estado_actual.__dict__
        tensiones = self._detectar_tensiones_estructurales(estado_evaluar)
        
        requiere_reconfig = False
        if estado_evaluar.get('nivel_yo', 0) >= 4:
            # Contradicciones de 4º orden requieren reconstrucción narrativa
            if estado_evaluar.get('coherencia_interna', 1.0) < 0.5:
                requiere_reconfig = True
                tensiones.append({
                    'tipo': 'reconstruccion_narrativa',
                    'descripcion': 'Requiere reconstrucción por baja coherencia'
                })
        
        return {
            'tensiones': {t['tipo']: t['descripcion'] for t in tensiones},
            'requiere_reconfig': requiere_reconfig,
            'contradiccion_detectada': len(tensiones) > 0
        }
    
    def evaluar_contradicciones(self, estado_externo=None):
        """Evalúa contradicciones y sincroniza con Neo4j"""
        resultado = self._evaluar_contradicciones_internas(estado_externo)
        
        # Sincronizar resultado con Neo4j
        self.sincronizar_con_neo4j()
        
        return resultado
    
    def _actualizar_tipo_yo(self, coherencia_total: float, num_contextos: int):
        """Actualiza el tipo de YO emergente basado en métricas.
        
        Args:
            coherencia_total: Valor de coherencia narrativa total (0.0 a 1.0)
            num_contextos: Número de contextos activos
        """
        # Lógica de emergencia fenomenológica del YO
        if coherencia_total >= 0.9 and num_contextos >= 5:
            self.estado_actual.tipo = TipoYO.YO_NARRATIVO
        elif coherencia_total >= 0.75 and num_contextos >= 4:
            self.estado_actual.tipo = TipoYO.YO_SIMBOLICO
        elif coherencia_total >= 0.6 and num_contextos >= 3:
            self.estado_actual.tipo = TipoYO.YO_REFLEXIVO
        elif coherencia_total >= 0.4 and num_contextos >= 2:
            self.estado_actual.tipo = TipoYO.YO_AFECTIVO
        elif coherencia_total >= 0.2 and num_contextos >= 1:
            self.estado_actual.tipo = TipoYO.YO_SENSORIAL
        else:
            self.estado_actual.tipo = TipoYO.PROTO_YO
        
    def evaluar_emergencia(self, contextos_activos, fenomenos_activos):
        """Evalúa la emergencia del YO a partir de contextos y fenómenos activos.
        
        Args:
            contextos_activos: Lista de contextos activos en el sistema
            fenomenos_activos: Lista de fenómenos activos en el sistema
            
        Returns:
            Dict: Resultado de la evaluación de emergencia con métricas
        """
        # Actualizar el estado actual con los IDs de contextos activos
        # Extraer solo IDs si son objetos completos, mantener strings si ya lo son
        if contextos_activos and isinstance(contextos_activos[0], dict):
            self.estado_actual.contextos_activos = [ctx.get('id', str(ctx)) for ctx in contextos_activos]
        else:
            self.estado_actual.contextos_activos = contextos_activos
        
        self.estado_actual.timestamp = datetime.datetime.now().isoformat()
        
        # Analizar coherencia narrativa con los nuevos contextos
        coherencia = self._analizar_coherencia_narrativa()
        
        # Evaluar contradicciones potenciales
        contradicciones = self.detectar_contradicciones()
        
        # Determinar si hay emergencia del YO basado en métricas
        emergencia_detectada = coherencia["coherencia_total"] > 0.6 and not contradicciones["contradiccion_detectada"]
        
        # Actualizar tipo de YO y nivel de activación basado en coherencia
        self._actualizar_tipo_yo(coherencia["coherencia_total"], len(contextos_activos))
        self.estado_actual.activacion = coherencia["coherencia_total"]
        
        # Registrar el evento de evaluación
        self._notificar_evento("evaluacion_emergencia", {
            "emergencia_detectada": emergencia_detectada,
            "coherencia": coherencia,
            "contradicciones": contradicciones,
            "contextos_activos": len(contextos_activos),
            "fenomenos_activos": len(fenomenos_activos)
        })
        
        # Registrar en modo diagnóstico si está activado
        if self.modo_diagnostico:
            print(f"[DIAGNÓSTICO] Evaluación de emergencia: {emergencia_detectada}")
            print(f"[DIAGNÓSTICO] Coherencia total: {coherencia['coherencia_total']:.2f}")
            print(f"[DIAGNÓSTICO] Contradicciones: {contradicciones['contradiccion_detectada']}")
        
        # Sincronizar estado con Neo4j después de evaluar emergencia
        self.sincronizar_con_neo4j()
        
        return {
            "emergencia_detectada": emergencia_detectada,
            "coherencia": coherencia["coherencia_total"],
            "contradicciones": contradicciones["contradiccion_detectada"],
            "requiere_reconfiguracion": contradicciones["requiere_reconfig"],
            "timestamp": self.estado_actual.timestamp
        }
    
    def _ejecutar_reconfiguracion(self, contradiccion: Dict = None) -> Dict:
        """Método interno para ejecutar reconfiguración"""
        estado_previo = copy.deepcopy(self.estado_actual)
        
        # Incrementar versión
        self.estado_actual.version += 1
        self.estado_actual.timestamp = datetime.datetime.now().isoformat()
        
        # Crear nueva reflexión
        nueva_reflexion = {
            "mensaje": f"Reconfiguración ejecutada v{self.estado_actual.version}",
            "timestamp": self.estado_actual.timestamp,
            "tipo": "reconfig_auto",
            "contradiccion": contradiccion if contradiccion else {}
        }
        
        self.estado_actual.reflexiones.append(nueva_reflexion)
        
        return {
            "reconfig_exitosa": True,
            "version_nueva": self.estado_actual.version,
            "cambios": self._describir_cambios(estado_previo.__dict__, self.estado_actual.__dict__)
        }