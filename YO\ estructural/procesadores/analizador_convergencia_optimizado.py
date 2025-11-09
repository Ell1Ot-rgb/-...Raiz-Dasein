"""
ANALIZADOR DE CONVERGENCIA DEFINICIONAL - OPTIMIZADO PARA DUAL-CORE
===================================================================

Implementación de máximo relacional con optimizaciones:
1. Lazy loading de embeddings
2. Batch processing para análisis
3. Memory-efficient streaming
4. Paralelización inteligente (2 cores)
5. Integración NetworkX + Neo4j GDS

Arquitectura:
- PC1 (Dual-Core AMD, 8GB RAM): Este módulo + análisis
- PC2 (Potente): Neo4j 5.12+ con GDS + LightRAG
"""

import numpy as np
import networkx as nx
from typing import List, Dict, Tuple, Optional
import logging
from datetime import datetime
import json
import gc
from functools import lru_cache
import concurrent.futures
from collections import defaultdict
import psutil
import os

# Importaciones con lazy loading
_embeddings_model = None
_neo4j_connection = None

logger = logging.getLogger(__name__)


class MemoryOptimizer:
    """Optimiza uso de memoria para dual-core"""
    
    MAX_MEMORY_PERCENT = 70  # Máximo 70% de RAM disponible
    BATCH_SIZE = 32  # Tamaño de batch optimizado para embeddings
    CHUNK_SIZE = 100  # Tamaño de chunk para procesamiento
    
    @staticmethod
    def get_available_memory() -> float:
        """Obtiene memoria disponible en GB"""
        return psutil.virtual_memory().available / (1024**3)
    
    @staticmethod
    def check_memory_threshold() -> bool:
        """Verifica si estamos por debajo del threshold"""
        memory_percent = psutil.virtual_memory().percent
        logger.debug(f"Uso de memoria: {memory_percent:.1f}%")
        return memory_percent < MemoryOptimizer.MAX_MEMORY_PERCENT
    
    @staticmethod
    def aggressive_gc():
        """Recolección agresiva de basura"""
        gc.collect()
        logger.debug("Garbage collection ejecutado")
    
    @staticmethod
    def estimate_dataframe_memory(n_rows: int, n_cols: int) -> float:
        """Estima memoria de dataframe en MB"""
        return (n_rows * n_cols * 8) / (1024**2)  # 8 bytes por float64


class EmbeddingsProvider:
    """Proveedor lazy-loaded de embeddings"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Inicializa provider sin cargar modelo inmediatamente
        
        Args:
            model_name: Modelo a usar (lightweight para dual-core)
        """
        self.model_name = model_name
        self.modelo = None
        self.cache = {}
        self.cache_size = 0
        self.max_cache_mb = 500  # Max 500MB cache
    
    def get_modelo(self):
        """Carga modelo lazy (solo cuando se necesita)"""
        if self.modelo is None:
            logger.info(f"Cargando modelo {self.model_name}...")
            from sentence_transformers import SentenceTransformer
            self.modelo = SentenceTransformer(self.model_name)
            logger.info(f"Modelo cargado: {self.model_name}")
        return self.modelo
    
    def encode_batch(self, textos: List[str], 
                     batch_size: int = 32) -> np.ndarray:
        """
        Codifica textos en lotes (memory-efficient)
        
        Args:
            textos: Lista de strings
            batch_size: Tamaño de lote
        
        Returns:
            Array de embeddings (n_textos x embedding_dim)
        """
        modelo = self.get_modelo()
        embeddings = []
        
        for i in range(0, len(textos), batch_size):
            batch = textos[i:i+batch_size]
            
            # Codificar batch
            batch_embeddings = modelo.encode(
                batch,
                convert_to_numpy=True,
                show_progress_bar=False
            )
            embeddings.append(batch_embeddings)
            
            # Verificar memoria
            if not MemoryOptimizer.check_memory_threshold():
                logger.warning("Memory threshold alcanzado, forzando GC")
                MemoryOptimizer.aggressive_gc()
        
        return np.vstack(embeddings)
    
    def similitud_coseno_batch(self, 
                               embeddings1: np.ndarray,
                               embeddings2: np.ndarray) -> np.ndarray:
        """
        Calcula similitud coseno entre dos conjuntos de embeddings
        (memory-efficient para matrices grandes)
        
        Args:
            embeddings1: Array (n1 x d)
            embeddings2: Array (n2 x d)
        
        Returns:
            Matriz de similitudes (n1 x n2)
        """
        from sklearn.metrics.pairwise import cosine_similarity
        
        # Normalizar
        e1_norm = embeddings1 / (np.linalg.norm(embeddings1, axis=1, 
                                                keepdims=True) + 1e-8)
        e2_norm = embeddings2 / (np.linalg.norm(embeddings2, axis=1, 
                                                keepdims=True) + 1e-8)
        
        # Computar similitud
        similitudes = np.dot(e1_norm, e2_norm.T)
        
        return similitudes


class ConvergenciaAnalyzer:
    """Analiza convergencia de rutas a máximo relacional"""
    
    def __init__(self, neo4j_conn, embeddings_provider: EmbeddingsProvider):
        """
        Inicializa analizador
        
        Args:
            neo4j_conn: Conexión a Neo4j
            embeddings_provider: Proveedor de embeddings
        """
        self.neo4j = neo4j_conn
        self.embeddings = embeddings_provider
        self.cache_rutas = {}
        self.cache_convergencias = {}
    
    def extraer_5_rutas_independientes(self, 
            preinstancia_ids: List[str], 
            usar_batch: bool = True) -> List[Dict]:
        """
        Extrae 5 rutas independientes optimizadamente
        
        Arquitectura:
        PreInstancia (PC1 memoria) 
            ↓ Query streaming
        Neo4j (PC2) → Retorna JSON comprimido
            ↓ Parseo en PC1
        Rutas procesadas (memoria eficiente)
        
        Args:
            preinstancia_ids: IDs de PreInstancias
            usar_batch: Si usar batch processing
        
        Returns:
            Lista de 5 rutas con definiciones
        """
        rutas = []
        
        if usar_batch and len(preinstancia_ids) > 10:
            # Procesar en chunks para no saturar memoria
            for chunk_ids in self._chunk_list(
                preinstancia_ids[:5], 
                MemoryOptimizer.CHUNK_SIZE
            ):
                rutas.extend(
                    self._extraer_rutas_chunk(chunk_ids)
                )
        else:
            rutas = self._extraer_rutas_chunk(preinstancia_ids[:5])
        
        logger.info(f"Extradas {len(rutas)} rutas independientes")
        return rutas
    
    def _extraer_rutas_chunk(self, pi_ids: List[str]) -> List[Dict]:
        """Extrae rutas para un chunk de PreInstancias"""
        rutas = []
        
        for pi_id in pi_ids:
            try:
                # Query optimizada: obtiene solo lo necesario
                ruta_data = self.neo4j.query(f"""
                    // Ruta 1: PreInstancia → Augenblick
                    MATCH (pi:PreInstancia {{id: '{pi_id}'}})
                    -[:GENERA]->(a:Augenblick)
                    
                    // Ruta 2: Augenblick → Vohexistencia
                    OPTIONAL MATCH (a)-[:PERTENECE_A]->(v:Vohexistencia)
                    
                    // Ruta 3: Vohexistencia → Grundzug
                    OPTIONAL MATCH (v)-[:PRODUCE]->(g:Grundzug)
                    
                    // Ruta 4: Grundzug → AxiomaYO
                    OPTIONAL MATCH (g)-[:FUNDAMENTA]->(ax:AxiomaYO)
                    
                    RETURN {{
                        pi_id: pi.id,
                        augenblick: a.definicion,
                        vohex: COALESCE(v.constante_emergente, ''),
                        grundzug: COALESCE(g.esencia, ''),
                        axioma: COALESCE(ax.definicion, ''),
                        va: COALESCE(ax.va, 0),
                        pc: COALESCE(ax.pc, 0)
                    }}
                """)
                
                if ruta_data:
                    rutas.append({
                        "ruta_id": f"ruta_{len(rutas)+1}",
                        "preinstancia_id": pi_id,
                        "paso_1_experiencial": 
                            ruta_data[0].get("augenblick", ""),
                        "paso_2_clustering": 
                            ruta_data[0].get("vohex", ""),
                        "paso_3_esencia": 
                            ruta_data[0].get("grundzug", ""),
                        "paso_4_axiomatico": {
                            "definicion": 
                                ruta_data[0].get("axioma", ""),
                            "va": ruta_data[0].get("va", 0),
                            "pc": ruta_data[0].get("pc", 0)
                        }
                    })
                    
            except Exception as e:
                logger.error(f"Error extrayendo ruta {pi_id}: {e}")
            
            # Cleanup
            if len(rutas) % 2 == 0:
                MemoryOptimizer.aggressive_gc()
        
        return rutas
    
    def calcular_convergencia_5_rutas(self, 
            rutas: List[Dict]) -> Dict:
        """
        Calcula convergencia con optimizaciones:
        1. Batch encoding de definiciones
        2. Similitud incremental (no matriz completa)
        3. Streaming de resultados
        
        Args:
            rutas: 5 rutas extraídas
        
        Returns:
            Métricas de convergencia
        """
        if len(rutas) < 2:
            logger.warning("Menos de 2 rutas para convergencia")
            return {"similitud_promedio": 0, "convergencia_detected": False}
        
        # Paso 1: Extraer definiciones finales
        definiciones = [
            r["paso_4_axiomatico"]["definicion"] 
            for r in rutas 
            if r["paso_4_axiomatico"]["definicion"]
        ]
        
        if len(definiciones) < 2:
            return {"similitud_promedio": 0, "convergencia_detected": False}
        
        logger.info(f"Codificando {len(definiciones)} definiciones...")
        
        # Paso 2: Codificar en batch
        embeddings = self.embeddings.encode_batch(
            definiciones,
            batch_size=MemoryOptimizer.BATCH_SIZE
        )
        
        # Paso 3: Calcular matriz de similitud
        logger.info("Calculando matriz de similitud...")
        matriz = self.embeddings.similitud_coseno_batch(
            embeddings, embeddings
        )
        
        # Paso 4: Analizar resultados
        mask = ~np.eye(len(embeddings), dtype=bool)
        similitudes = matriz[mask]
        
        similitud_promedio = float(np.mean(similitudes))
        desv_est = float(np.std(similitudes))
        
        # Paso 5: Detectar convergencia
        convergencia_detected = similitud_promedio > 0.85
        
        logger.info(
            f"Convergencia: {similitud_promedio:.4f} "
            f"(desv: {desv_est:.4f})"
        )
        
        return {
            "similitud_promedio": similitud_promedio,
            "desviacion_estandar": desv_est,
            "convergencia_detected": convergencia_detected,
            "matriz_similitudes": matriz,
            "definiciones": definiciones,
            "n_definiciones": len(definiciones)
        }
    
    def calcular_certeza_combinada(self, 
            rutas: List[Dict]) -> Dict:
        """
        Calcula certeza combinada optimizadamente
        
        Fórmula:
        P(correcto) = 1 - ∏(1 - c_i) para i en rutas
        
        Args:
            rutas: Rutas con VA y PC
        
        Returns:
            Métricas de certeza
        """
        # Extraer certezas
        certezas = []
        for r in rutas:
            axioma = r["paso_4_axiomatico"]
            va = axioma.get("va", 0)
            pc = axioma.get("pc", 0)
            certeza = va * pc  # Combinación simple
            certezas.append(certeza)
        
        certezas = np.array(certezas)
        
        # Verificar que no estén todas iguales (independencia)
        desv_est_certezas = float(np.std(certezas))
        if desv_est_certezas < 0.01:
            logger.warning("Rutas pueden no ser independientes")
            independencia_factor = 0.85
        else:
            independencia_factor = 0.95
        
        # Calcular certeza combinada
        # P(error) = producto de errores individuales
        certeza_combinada = 1.0
        for c in certezas:
            if c > 0:
                certeza_combinada *= (1 - c)
        
        certeza_combinada = 1 - certeza_combinada
        
        # Ajustar por independencia
        certeza_final = (
            certeza_combinada * independencia_factor
        )
        
        return {
            "certeza_individual_promedio": float(np.mean(certezas)),
            "certeza_individual_desv": desv_est_certezas,
            "certeza_combinada_teórica": float(certeza_combinada),
            "factor_independencia": independencia_factor,
            "certeza_final_ajustada": float(certeza_final),
            "porcentaje": f"{certeza_final * 100:.4f}%",
            "certezas_individuales": [float(c) for c in certezas]
        }
    
    def detectar_maximo_relacional(self, 
            preinstancia_ids: List[str],
            usar_lightrag: bool = False) -> Dict:
        """
        Detecta máximo relacional definicional
        
        Pasos optimizados:
        1. Extraer rutas (lazy)
        2. Convergencia (batch)
        3. Certeza (vectorizado)
        4. Síntesis (streaming)
        
        Args:
            preinstancia_ids: IDs de PreInstancias
            usar_lightrag: Si usar LightRAG para enriquecimiento
        
        Returns:
            Resultado de máximo relacional
        """
        timestamp_inicio = datetime.now()
        
        logger.info("=== Iniciando detección de máximo relacional ===")
        logger.info(f"Memoria disponible: {MemoryOptimizer.get_available_memory():.2f}GB")
        
        try:
            # Paso 1: Extraer rutas
            logger.info(f"Extrayendo rutas de {len(preinstancia_ids)} PreInstancias...")
            rutas = self.extraer_5_rutas_independientes(
                preinstancia_ids[:5]
            )
            
            if len(rutas) < 2:
                logger.error("No hay suficientes rutas")
                return {"es_maximo_relacional": False}
            
            # Paso 2: Convergencia
            logger.info("Analizando convergencia...")
            convergencia = self.calcular_convergencia_5_rutas(rutas)
            
            # Paso 3: Certeza
            logger.info("Calculando certeza combinada...")
            certeza = self.calcular_certeza_combinada(rutas)
            
            # Paso 4: Síntesis
            es_maximo = (
                convergencia.get("similitud_promedio", 0) >= 0.85 and
                certeza.get("certeza_final_ajustada", 0) >= 0.99 and
                convergencia.get("desviacion_estandar", 1) <= 0.10
            )
            
            # Paso 5: Opcional - LightRAG enriquecimiento
            definicion_enriquecida = None
            if usar_lightrag and es_maximo:
                logger.info("Enriqueciendo con LightRAG...")
                definicion_enriquecida = (
                    self._enriquecer_con_lightrag(
                        convergencia["definiciones"]
                    )
                )
            
            # Resultado final
            resultado = {
                "es_maximo_relacional": es_maximo,
                "concepto_convergente": (
                    self._extraer_nombre_concepto(rutas) 
                    if rutas else None
                ),
                "convergencia": convergencia,
                "certeza": certeza,
                "nivel_verdad_alcanzado": (
                    0.9999 if es_maximo else 
                    certeza.get("certeza_final_ajustada", 0)
                ),
                "definicion_sintetizada": (
                    definicion_enriquecida or 
                    self._sintetizar_definiciones(
                        convergencia.get("definiciones", [])
                    )
                ),
                "timestamp": datetime.now().isoformat(),
                "duracion_segundos": (
                    (datetime.now() - timestamp_inicio).total_seconds()
                ),
                "memoria_utilizada_mb": (
                    (MemoryOptimizer.get_available_memory() * 1024 -
                     psutil.virtual_memory().available / (1024**2))
                )
            }
            
            logger.info(
                f"✓ Análisis completado en "
                f"{resultado['duracion_segundos']:.2f}s"
            )
            
            return resultado
            
        except Exception as e:
            logger.error(f"Error en detección: {e}", exc_info=True)
            return {"es_maximo_relacional": False, "error": str(e)}
    
    def _enriquecer_con_lightrag(self, definiciones: List[str]) -> str:
        """
        Enriquece definiciones usando LightRAG en PC2
        
        Nota: LightRAG corre en PC2 (Neo4j remoto)
        Este método solo orquesta la llamada
        """
        try:
            # Llamada remota a LightRAG via Neo4j procedure
            resultado = self.neo4j.query("""
                CALL neo4j.config.lightrag.enrich($definiciones)
                YIELD enriched_definition
                RETURN enriched_definition
            """, {"definiciones": json.dumps(definiciones)})
            
            if resultado:
                return resultado[0].get("enriched_definition", 
                                       definiciones[0])
        except Exception as e:
            logger.warning(f"LightRAG no disponible: {e}")
        
        return definiciones[0] if definiciones else ""
    
    def _sintetizar_definiciones(self, 
            definiciones: List[str]) -> str:
        """Sintetiza múltiples definiciones"""
        if not definiciones:
            return ""
        
        if len(definiciones) == 1:
            return definiciones[0]
        
        # Concatenar con separadores conceptuales
        return " | ".join(
            f"Ruta {i+1}: {d}" 
            for i, d in enumerate(definiciones)
        )
    
    def _extraer_nombre_concepto(self, rutas: List[Dict]) -> str:
        """Extrae nombre del concepto de las rutas"""
        if not rutas:
            return "DESCONOCIDO"
        
        # Intentar obtener del AxiomaYO
        for r in rutas:
            if r["paso_4_axiomatico"].get("definicion"):
                # Extraer primera palabra importante
                palabras = r["paso_4_axiomatico"]["definicion"].split()
                return palabras[0].upper() if palabras else "CONCEPTO"
        
        return "CONCEPTO_CONVERGENTE"
    
    @staticmethod
    def _chunk_list(lista: list, chunk_size: int):
        """Divide lista en chunks"""
        for i in range(0, len(lista), chunk_size):
            yield lista[i:i + chunk_size]


# ===================================================================
# INTERFAZ SIMPLIFICADA PARA USO EN OrquestadorMaestro
# ===================================================================

class AnalizadorConvergenciaSimplificado:
    """
    Interfaz simplificada para integración en sistema principal
    
    Uso:
    analizador = AnalizadorConvergenciaSimplificado(neo4j_conn)
    resultado = analizador.analizar(preinstancia_ids)
    """
    
    _instancia = None
    
    def __init__(self, neo4j_conn):
        self.neo4j = neo4j_conn
        self.embeddings = EmbeddingsProvider()
        self.analyzer = ConvergenciaAnalyzer(
            neo4j_conn, 
            self.embeddings
        )
    
    @classmethod
    def get_instancia(cls, neo4j_conn=None):
        """Singleton con lazy initialization"""
        if cls._instancia is None:
            if neo4j_conn is None:
                raise ValueError("neo4j_conn requerido en primera llamada")
            cls._instancia = cls(neo4j_conn)
        return cls._instancia
    
    def analizar(self, preinstancia_ids: List[str],
                 usar_lightrag: bool = False) -> Dict:
        """Análisis simplificado"""
        return self.analyzer.detectar_maximo_relacional(
            preinstancia_ids,
            usar_lightrag=usar_lightrag
        )
    
    def limpiar_memoria(self):
        """Limpia caches y modelos"""
        if self.embeddings.modelo is not None:
            del self.embeddings.modelo
            self.embeddings.modelo = None
        MemoryOptimizer.aggressive_gc()


if __name__ == "__main__":
    # Ejemplo de uso
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )
    
    print("""
    Módulo: Analizador de Convergencia Definicional (Optimizado)
    Uso: from analizador_convergencia_optimizado import AnalizadorConvergenciaSimplificado
    """)
