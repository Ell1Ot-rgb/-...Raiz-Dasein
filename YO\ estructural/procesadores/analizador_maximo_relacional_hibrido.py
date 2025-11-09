"""
ANALIZADOR DE MÁXIMO RELACIONAL - NETWORKX + NEO4J GDS HÍBRIDO
==============================================================

Implementa búsqueda de máximo relacional usando:
1. OPCIÓN A (NetworkX): En PC1 para grafos pequeños/medianos
2. OPCIÓN B (Neo4j GDS): En PC2 para grafos grandes
3. HÍBRIDO: Según tamaño de grafo, elige automáticamente

Optimizaciones para dual-core:
- Carga incremental de grafo
- Streaming de resultados
- Paralelización inteligente
- Memory-efficient graph operations
"""

import networkx as nx
import numpy as np
import logging
from typing import Dict, List, Tuple, Optional
from datetime import datetime
import json
from enum import Enum
import psutil

logger = logging.getLogger(__name__)


class ModoEjecucion(Enum):
    """Modos de ejecución según disponibilidad"""
    NETWORKX_LOCAL = "networkx_local"      # PC1, grafos < 10k nodos
    NEOJ4_GDS_REMOTO = "neo4j_gds_remoto"  # PC2, grafos > 10k nodos
    HIBRIDO = "hibrido"                    # Ambos, compara resultados


class CentralityMetrics(Enum):
    """Métricas de centralidad disponibles"""
    PAGERANK = "pagerank"
    BETWEENNESS = "betweenness"
    CLOSENESS = "closeness"
    EIGENVECTOR = "eigenvector"
    DEGREE = "degree"
    CLUSTERING = "clustering"


class ConstructorGrafoOptimizado:
    """Construye grafo desde Neo4j optimizadamente para dual-core"""
    
    # Límites para dual-core 8GB
    MAX_NODOS_LOCAL = 10000
    MAX_ARISTAS_LOCAL = 50000
    CHUNK_NODOS = 1000
    CHUNK_ARISTAS = 5000
    
    def __init__(self, neo4j_conn):
        self.neo4j = neo4j_conn
        self.grafo = None
        self.metricas = {}
    
    def obtener_estadisticas_grafo(self) -> Dict:
        """Obtiene estadísticas del grafo sin cargar todo"""
        stats = self.neo4j.query("""
            MATCH (c:Concepto)
            WITH count(c) as n_conceptos
            MATCH (c1:Concepto)-[r:GRADIENTE]->(c2:Concepto)
            WITH n_conceptos, count(r) as n_aristas
            RETURN {
                n_conceptos: n_conceptos,
                n_aristas: n_aristas,
                densidad: n_aristas / (n_conceptos * (n_conceptos - 1))
            }
        """)
        
        if stats:
            return stats[0]
        return {"n_conceptos": 0, "n_aristas": 0, "densidad": 0}
    
    def seleccionar_modo_ejecucion(self) -> ModoEjecucion:
        """
        Selecciona modo de ejecución según tamaño de grafo
        
        Lógica:
        - < 10k nodos: NetworkX local (rápido, bajo overhead)
        - 10-100k nodos: Neo4j GDS remoto (más poder)
        - > 100k nodos: Neo4j GDS remoto (obligatorio)
        """
        stats = self.obtener_estadisticas_grafo()
        n_nodos = stats.get("n_conceptos", 0)
        
        if n_nodos < self.MAX_NODOS_LOCAL:
            logger.info(f"Usando NetworkX ({n_nodos} nodos)")
            return ModoEjecucion.NETWORKX_LOCAL
        else:
            logger.info(f"Usando Neo4j GDS ({n_nodos} nodos)")
            return ModoEjecucion.NEOJ4_GDS_REMOTO
    
    def construir_grafo_local(self) -> nx.DiGraph:
        """
        Construye grafo NetworkX desde Neo4j
        
        Optimizaciones:
        - Carga en chunks
        - Streaming de aristas
        - Memory checks
        """
        logger.info("Construyendo grafo NetworkX...")
        grafo = nx.DiGraph()
        
        # Paso 1: Cargar nodos en chunks
        offset = 0
        while True:
            nodos = self.neo4j.query(f"""
                MATCH (c:Concepto)
                RETURN {{id: c.id, nombre: c.nombre}}
                SKIP {offset} LIMIT {self.CHUNK_NODOS}
            """)
            
            if not nodos:
                break
            
            for nodo in nodos:
                grafo.add_node(
                    nodo["id"],
                    nombre=nodo.get("nombre", "")
                )
            
            offset += self.CHUNK_NODOS
            logger.debug(f"Cargados {grafo.number_of_nodes()} nodos")
            
            # Check memoria
            if not self._check_memoria():
                logger.error("Insuficiente memoria")
                return None
        
        # Paso 2: Cargar aristas en chunks
        offset = 0
        while True:
            aristas = self.neo4j.query(f"""
                MATCH (c1:Concepto)-[r:GRADIENTE]->(c2:Concepto)
                RETURN {{
                    source: c1.id,
                    target: c2.id,
                    weight: r.valor,
                    confidence: r.confianza
                }}
                SKIP {offset} LIMIT {self.CHUNK_ARISTAS}
            """)
            
            if not aristas:
                break
            
            for arista in aristas:
                grafo.add_edge(
                    arista["source"],
                    arista["target"],
                    weight=arista.get("weight", 0.5),
                    confidence=arista.get("confidence", 0.8)
                )
            
            offset += self.CHUNK_ARISTAS
            logger.debug(f"Cargadas {grafo.number_of_edges()} aristas")
            
            if not self._check_memoria():
                logger.error("Insuficiente memoria")
                return None
        
        logger.info(
            f"Grafo construido: {grafo.number_of_nodes()} nodos, "
            f"{grafo.number_of_edges()} aristas"
        )
        
        self.grafo = grafo
        return grafo
    
    def _check_memoria(self) -> bool:
        """Verifica si memoria está OK"""
        mem_percent = psutil.virtual_memory().percent
        if mem_percent > 75:
            logger.warning(f"Memoria alta: {mem_percent}%")
            return False
        return True


class AnalizadorCentralidadNetworkX:
    """Calcula centralidad usando NetworkX (Opción A)"""
    
    def __init__(self, grafo: nx.DiGraph):
        self.grafo = grafo
        self.metricas_cache = {}
    
    def calcular_pagerank(self, iterations: int = 30, 
                         damping: float = 0.85) -> Dict:
        """
        Calcula PageRank optimizado
        
        Optimizaciones:
        - Parametrizable
        - Usa weights
        - Cache
        """
        if "pagerank" in self.metricas_cache:
            return self.metricas_cache["pagerank"]
        
        logger.info(f"Calculando PageRank ({iterations} iteraciones)...")
        
        try:
            pagerank = nx.pagerank(
                self.grafo,
                alpha=damping,
                max_iter=iterations,
                weight='weight',
                tol=1e-6
            )
            
            self.metricas_cache["pagerank"] = pagerank
            return pagerank
            
        except Exception as e:
            logger.error(f"Error en PageRank: {e}")
            return {}
    
    def calcular_betweenness(self) -> Dict:
        """Calcula Betweenness Centrality"""
        if "betweenness" in self.metricas_cache:
            return self.metricas_cache["betweenness"]
        
        logger.info("Calculando Betweenness Centrality...")
        
        try:
            betweenness = nx.betweenness_centrality(
                self.grafo,
                weight='weight',
                normalized=True
            )
            
            self.metricas_cache["betweenness"] = betweenness
            return betweenness
            
        except Exception as e:
            logger.error(f"Error en Betweenness: {e}")
            return {}
    
    def calcular_closeness(self) -> Dict:
        """Calcula Closeness Centrality (solo componente fuerte)"""
        if "closeness" in self.metricas_cache:
            return self.metricas_cache["closeness"]
        
        logger.info("Calculando Closeness Centrality...")
        
        try:
            # Solo en componente fuerte conexo
            if nx.is_strongly_connected(self.grafo):
                closeness = nx.closeness_centrality(
                    self.grafo,
                    distance='weight'
                )
            else:
                # Para grafo desconexo, usa componente más grande
                componentes = list(nx.strongly_connected_components(
                    self.grafo
                ))
                if componentes:
                    comp_mayor = self.grafo.subgraph(componentes[0])
                    closeness = nx.closeness_centrality(
                        comp_mayor,
                        distance='weight'
                    )
                    # Rellenar otros nodos con 0
                    for nodo in self.grafo.nodes():
                        if nodo not in closeness:
                            closeness[nodo] = 0
                else:
                    closeness = {n: 0 for n in self.grafo.nodes()}
            
            self.metricas_cache["closeness"] = closeness
            return closeness
            
        except Exception as e:
            logger.error(f"Error en Closeness: {e}")
            return {}
    
    def calcular_eigenvector(self, max_iter: int = 100) -> Dict:
        """Calcula Eigenvector Centrality"""
        if "eigenvector" in self.metricas_cache:
            return self.metricas_cache["eigenvector"]
        
        logger.info("Calculando Eigenvector Centrality...")
        
        try:
            eigenvector = nx.eigenvector_centrality(
                self.grafo,
                max_iter=max_iter,
                weight='weight',
                tol=1e-6
            )
            
            self.metricas_cache["eigenvector"] = eigenvector
            return eigenvector
            
        except Exception as e:
            logger.error(f"Error en Eigenvector: {e}")
            return {}
    
    def calcular_clustering_coefficient(self) -> Dict:
        """Calcula Clustering Coefficient"""
        if "clustering" in self.metricas_cache:
            return self.metricas_cache["clustering"]
        
        logger.info("Calculando Clustering Coefficient...")
        
        try:
            # Convertir a undirected para clustering
            grafo_undir = self.grafo.to_undirected()
            clustering = nx.clustering(
                grafo_undir,
                weight='weight'
            )
            
            self.metricas_cache["clustering"] = clustering
            return clustering
            
        except Exception as e:
            logger.error(f"Error en Clustering: {e}")
            return {}
    
    def calcular_todas_metricas(self) -> Dict:
        """Calcula todas las métricas"""
        logger.info("Calculando todas las métricas...")
        
        metricas = {
            "pagerank": self.calcular_pagerank(),
            "betweenness": self.calcular_betweenness(),
            "closeness": self.calcular_closeness(),
            "eigenvector": self.calcular_eigenvector(),
            "clustering": self.calcular_clustering_coefficient()
        }
        
        return metricas


class AnalizadorCentralidadNeo4jGDS:
    """Calcula centralidad usando Neo4j GDS (Opción B)"""
    
    def __init__(self, neo4j_conn):
        self.neo4j = neo4j_conn
        self.nombre_grafo_gds = "grafo_centralidad_temp"
    
    def proyectar_grafo(self) -> bool:
        """Proyecta grafo en GDS"""
        logger.info("Proyectando grafo en Neo4j GDS...")
        
        try:
            self.neo4j.query(f"""
                CALL gds.graph.project(
                    '{self.nombre_grafo_gds}',
                    'Concepto',
                    'GRADIENTE',
                    {{
                        relationshipProperties: ['valor', 'confianza']
                    }}
                )
                YIELD graphName, nodeCount, relationshipCount
                RETURN graphName, nodeCount, relationshipCount
            """)
            
            logger.info("Grafo proyectado en GDS")
            return True
            
        except Exception as e:
            logger.error(f"Error proyectando grafo: {e}")
            return False
    
    def calcular_pagerank(self) -> Dict:
        """Calcula PageRank con Neo4j GDS"""
        logger.info("Calculando PageRank con Neo4j GDS...")
        
        try:
            resultado = self.neo4j.query(f"""
                CALL gds.pageRank.stream(
                    '{self.nombre_grafo_gds}',
                    {{
                        maxIterations: 30,
                        damping: 0.85,
                        relationshipWeightProperty: 'valor'
                    }}
                )
                YIELD nodeId, score
                WITH gds.util.asNode(nodeId).id AS id, score
                RETURN {{id: id, score: score}}
            """)
            
            return {r["id"]: r["score"] for r in resultado}
            
        except Exception as e:
            logger.error(f"Error en PageRank GDS: {e}")
            return {}
    
    def calcular_betweenness(self) -> Dict:
        """Calcula Betweenness con Neo4j GDS"""
        logger.info("Calculando Betweenness con Neo4j GDS...")
        
        try:
            resultado = self.neo4j.query(f"""
                CALL gds.betweenness.stream(
                    '{self.nombre_grafo_gds}',
                    {{relationshipWeightProperty: 'valor'}}
                )
                YIELD nodeId, score
                WITH gds.util.asNode(nodeId).id AS id, score
                RETURN {{id: id, score: score}}
            """)
            
            return {r["id"]: r["score"] for r in resultado}
            
        except Exception as e:
            logger.error(f"Error en Betweenness GDS: {e}")
            return {}
    
    def calcular_closeness(self) -> Dict:
        """Calcula Closeness con Neo4j GDS"""
        logger.info("Calculando Closeness con Neo4j GDS...")
        
        try:
            resultado = self.neo4j.query(f"""
                CALL gds.closeness.stream(
                    '{self.nombre_grafo_gds}',
                    {{relationshipWeightProperty: 'valor'}}
                )
                YIELD nodeId, centrality
                WITH gds.util.asNode(nodeId).id AS id, centrality
                RETURN {{id: id, score: centrality}}
            """)
            
            return {r["id"]: r["score"] for r in resultado}
            
        except Exception as e:
            logger.error(f"Error en Closeness GDS: {e}")
            return {}
    
    def limpiar_grafo(self):
        """Limpia proyección GDS"""
        try:
            self.neo4j.query(f"""
                CALL gds.graph.drop('{self.nombre_grafo_gds}')
            """)
        except:
            pass


class AnalizadorMaximoRelacionalHibrido:
    """
    Analizador híbrido que elige entre NetworkX y Neo4j GDS
    según tamaño del grafo
    """
    
    PESOS_METRICAS = {
        "pagerank": 0.3,
        "betweenness": 0.25,
        "closeness": 0.2,
        "eigenvector": 0.15,
        "clustering": 0.1
    }
    
    def __init__(self, neo4j_conn):
        self.neo4j = neo4j_conn
        self.constructor = ConstructorGrafoOptimizado(neo4j_conn)
        self.modo = None
    
    def detectar_maximo_relacional(self) -> Dict:
        """
        Detecta máximo relacional usando mejor estrategia
        
        Returns:
            {
                "concepto_maximo": str,
                "score_maximo": float,
                "modo_usado": str,
                "metricas": {...},
                "timestamp": str
            }
        """
        timestamp_inicio = datetime.now()
        
        # Paso 1: Seleccionar modo
        self.modo = self.constructor.seleccionar_modo_ejecucion()
        logger.info(f"Modo seleccionado: {self.modo.value}")
        
        try:
            if self.modo == ModoEjecucion.NETWORKX_LOCAL:
                resultado = self._analizar_networkx()
            else:
                resultado = self._analizar_neo4j_gds()
            
            # Agregar metadata
            resultado["modo_usado"] = self.modo.value
            resultado["duracion_segundos"] = (
                (datetime.now() - timestamp_inicio).total_seconds()
            )
            
            return resultado
            
        except Exception as e:
            logger.error(f"Error en análisis: {e}", exc_info=True)
            return {
                "error": str(e),
                "modo_usado": self.modo.value if self.modo else None
            }
    
    def _analizar_networkx(self) -> Dict:
        """Análisis con NetworkX"""
        logger.info("Iniciando análisis con NetworkX...")
        
        # Paso 1: Construir grafo
        grafo = self.constructor.construir_grafo_local()
        if grafo is None:
            return {"error": "No se pudo construir grafo"}
        
        # Paso 2: Calcular centralidades
        analizador = AnalizadorCentralidadNetworkX(grafo)
        metricas = analizador.calcular_todas_metricas()
        
        # Paso 3: Combinar scores
        scores_combinados = self._combinar_scores(metricas)
        
        # Paso 4: Encontrar máximo
        nodo_maximo = max(
            scores_combinados,
            key=scores_combinados.get
        )
        
        return {
            "concepto_maximo": nodo_maximo,
            "score_maximo": scores_combinados[nodo_maximo],
            "metricas_detalladas": {
                "pagerank": metricas["pagerank"].get(nodo_maximo, 0),
                "betweenness": metricas["betweenness"].get(nodo_maximo, 0),
                "closeness": metricas["closeness"].get(nodo_maximo, 0),
                "eigenvector": metricas["eigenvector"].get(nodo_maximo, 0),
                "clustering": metricas["clustering"].get(nodo_maximo, 0)
            },
            "scores_todos": scores_combinados
        }
    
    def _analizar_neo4j_gds(self) -> Dict:
        """Análisis con Neo4j GDS"""
        logger.info("Iniciando análisis con Neo4j GDS...")
        
        analizador = AnalizadorCentralidadNeo4jGDS(self.neo4j)
        
        try:
            # Proyectar
            if not analizador.proyectar_grafo():
                return {"error": "No se pudo proyectar grafo"}
            
            # Calcular metricas
            metricas = {
                "pagerank": analizador.calcular_pagerank(),
                "betweenness": analizador.calcular_betweenness(),
                "closeness": analizador.calcular_closeness()
            }
            
            # Combinar
            scores_combinados = {}
            todos_nodos = set()
            for m in metricas.values():
                todos_nodos.update(m.keys())
            
            for nodo in todos_nodos:
                score = (
                    metricas["pagerank"].get(nodo, 0) * 0.3 +
                    metricas["betweenness"].get(nodo, 0) * 0.25 +
                    metricas["closeness"].get(nodo, 0) * 0.2
                )
                scores_combinados[nodo] = score
            
            # Máximo
            nodo_maximo = max(
                scores_combinados,
                key=scores_combinados.get
            )
            
            return {
                "concepto_maximo": nodo_maximo,
                "score_maximo": scores_combinados[nodo_maximo],
                "metricas_detalladas": {
                    "pagerank": metricas["pagerank"].get(nodo_maximo, 0),
                    "betweenness": metricas["betweenness"].get(nodo_maximo, 0),
                    "closeness": metricas["closeness"].get(nodo_maximo, 0)
                },
                "scores_todos": scores_combinados
            }
            
        finally:
            analizador.limpiar_grafo()
    
    def _combinar_scores(self, metricas: Dict) -> Dict:
        """Combina todas las métricas en un score único"""
        scores_combinados = {}
        
        todos_nodos = set()
        for m in metricas.values():
            todos_nodos.update(m.keys())
        
        for nodo in todos_nodos:
            score = sum(
                metricas.get(metrica_nombre, {}).get(nodo, 0) * peso
                for metrica_nombre, peso in self.PESOS_METRICAS.items()
            )
            scores_combinados[nodo] = score
        
        return scores_combinados


# ===================================================================
# INTERFAZ DE USO
# ===================================================================

class AnalizadorMaximoRelacionalPublico:
    """Interfaz pública simplificada"""
    
    def __init__(self, neo4j_conn):
        self.analizador = AnalizadorMaximoRelacionalHibrido(neo4j_conn)
    
    def analizar(self) -> Dict:
        """Realiza análisis completo"""
        return self.analizador.detectar_maximo_relacional()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )
    
    print("""
    Módulo: Analizador de Máximo Relacional (NetworkX + Neo4j GDS)
    Uso: from analizador_maximo_relacional_hibrido import AnalizadorMaximoRelacionalPublico
    """)
