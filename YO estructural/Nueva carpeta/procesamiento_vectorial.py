#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROCESAMIENTO VECTORIAL Y GRADIENTES - YO ESTRUCTURAL
====================================================

Este módulo maneja el procesamiento vectorial y de gradientes para el sistema YO Estructural:
1. Extracción de embeddings vectoriales
2. Cálculo de gradientes fenomenológicos
3. Análisis de similitudes y relaciones
4. Generación de representaciones para Neo4j

Autor: Sistema YO Estructural
Versión: 3.0
"""

import os
import sys
import json
import numpy as np
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path

# Importaciones para procesamiento de texto y vectores
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.decomposition import PCA
    import hashlib
except ImportError as e:
    print(f"Error importando librerías de ML: {e}")
    print("Instale las dependencias con: pip install scikit-learn numpy")
    sys.exit(1)

# Configurar logging
logger = logging.getLogger(__name__)

class ProcesadorVectorial:
    """Procesador vectorial para análisis fenomenológico"""
    
    def __init__(self, config: Optional[Dict] = None):
        """Inicializa el procesador vectorial"""
        self.config = config or self._cargar_configuracion_default()
        
        # Inicializar vectorizador TF-IDF
        self.tfidf_vectorizer = TfidfVectorizer(
            max_features=self.config.get('max_features_tfidf', 3000),
            ngram_range=tuple(self.config.get('ngram_range', [1, 3])),
            stop_words='spanish' if self.config.get('eliminar_stopwords', True) else None,
            min_df=self.config.get('min_df', 2),
            max_df=self.config.get('max_df', 0.85)
        )
        
        # Cache para vectores
        self.cache_vectores = {}
        self.cache_gradientes = {}
        
        logger.info("Procesador vectorial inicializado")
    
    def _cargar_configuracion_default(self) -> Dict:
        """Carga configuración por defecto"""
        return {
            'max_features_tfidf': 3000,
            'ngram_range': [1, 3],
            'eliminar_stopwords': True,
            'min_df': 2,
            'max_df': 0.85,
            'umbral_similitud': 0.3,
            'dimensiones_pca': 50
        }
    
    def extraer_vectores_texto(self, texto: str, id_documento: str = None) -> Dict[str, Any]:
        """Extrae vectores TF-IDF de un texto"""
        try:
            if not texto or len(texto.strip()) < 10:
                return {
                    'success': False,
                    'error': 'Texto demasiado corto para vectorización'
                }
            
            # Generar ID si no se proporciona
            if not id_documento:
                id_documento = hashlib.md5(texto.encode()).hexdigest()[:12]
            
            # Verificar cache
            if id_documento in self.cache_vectores:
                logger.debug(f"Vector recuperado del cache: {id_documento}")
                return self.cache_vectores[id_documento]
            
            # Vectorizar texto
            vector_tfidf = self.tfidf_vectorizer.fit_transform([texto])
            vector_denso = vector_tfidf.toarray()[0]
            
            # Obtener características más importantes
            feature_names = self.tfidf_vectorizer.get_feature_names_out()
            indices_importantes = np.argsort(vector_denso)[-20:][::-1]  # Top 20
            
            caracteristicas_importantes = [
                {
                    'termino': feature_names[i],
                    'peso': float(vector_denso[i]),
                    'importancia': float(vector_denso[i] / np.max(vector_denso))
                }
                for i in indices_importantes if vector_denso[i] > 0
            ]
            
            resultado = {
                'success': True,
                'id_documento': id_documento,
                'vector_tfidf': vector_denso.tolist(),
                'dimensiones': len(vector_denso),
                'caracteristicas_importantes': caracteristicas_importantes,
                'norma_vector': float(np.linalg.norm(vector_denso)),
                'timestamp': datetime.now().isoformat()
            }
            
            # Guardar en cache
            self.cache_vectores[id_documento] = resultado
            
            logger.info(f"Vector extraído para documento {id_documento}: {len(caracteristicas_importantes)} características")
            return resultado
            
        except Exception as e:
            logger.error(f"Error extrayendo vectores: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def calcular_gradientes_fenomenologicos(self, datos: Dict[str, Any]) -> Dict[str, Any]:
        """Calcula gradientes fenomenológicos basados en los datos"""
        try:
            gradientes = {
                'intensidad_emocional': self._calcular_gradiente_emocional(datos),
                'coherencia_narrativa': self._calcular_gradiente_coherencia(datos),
                'peso_existencial': self._calcular_gradiente_existencial(datos),
                'complejidad_semantica': self._calcular_gradiente_complejidad(datos),
                'conectividad_relacional': self._calcular_gradiente_conectividad(datos)
            }
            
            # Calcular gradiente compuesto
            gradiente_compuesto = np.mean(list(gradientes.values()))
            
            resultado = {
                'success': True,
                'gradientes_individuales': gradientes,
                'gradiente_compuesto': float(gradiente_compuesto),
                'interpretacion': self._interpretar_gradientes(gradientes),
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"Gradientes calculados: compuesto={gradiente_compuesto:.3f}")
            return resultado
            
        except Exception as e:
            logger.error(f"Error calculando gradientes: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _calcular_gradiente_emocional(self, datos: Dict) -> float:
        """Calcula gradiente de intensidad emocional"""
        emociones = datos.get('propiedades', {}).get('emociones_detectadas', [])
        if not emociones:
            return 0.5  # Neutral
        
        # Pesos emocionales (ejemplo)
        pesos_emociones = {
            'alegria': 0.8, 'tristeza': 0.7, 'miedo': 0.9,
            'ira': 0.85, 'sorpresa': 0.6, 'disgusto': 0.75
        }
        
        intensidad_total = sum(pesos_emociones.get(emocion.lower(), 0.5) for emocion in emociones)
        return min(intensidad_total / len(emociones), 1.0)
    
    def _calcular_gradiente_coherencia(self, datos: Dict) -> float:
        """Calcula gradiente de coherencia narrativa"""
        coherencia = datos.get('propiedades', {}).get('coherencia_narrativa', 0.5)
        if isinstance(coherencia, (int, float)):
            return float(coherencia)
        return 0.5
    
    def _calcular_gradiente_existencial(self, datos: Dict) -> float:
        """Calcula gradiente de peso existencial"""
        peso = datos.get('propiedades', {}).get('peso_existencial', 0.5)
        if isinstance(peso, (int, float)):
            return float(peso)
        return 0.5
    
    def _calcular_gradiente_complejidad(self, datos: Dict) -> float:
        """Calcula gradiente de complejidad semántica"""
        # Basado en la longitud del texto y diversidad de conceptos
        descripcion = datos.get('propiedades', {}).get('descripcion', '')
        if not descripcion:
            return 0.3
        
        # Factores de complejidad
        longitud_factor = min(len(descripcion) / 1000, 1.0)
        palabras_unicas = len(set(descripcion.lower().split()))
        diversidad_factor = min(palabras_unicas / 100, 1.0)
        
        return (longitud_factor + diversidad_factor) / 2
    
    def _calcular_gradiente_conectividad(self, datos: Dict) -> float:
        """Calcula gradiente de conectividad relacional"""
        relaciones = datos.get('relaciones', [])
        if not relaciones:
            return 0.2
        
        # Más relaciones = mayor conectividad
        return min(len(relaciones) / 10, 1.0)
    
    def _interpretar_gradientes(self, gradientes: Dict[str, float]) -> Dict[str, str]:
        """Interpreta los gradientes calculados"""
        interpretaciones = {}
        
        for nombre, valor in gradientes.items():
            if valor < 0.3:
                nivel = "bajo"
            elif valor < 0.7:
                nivel = "medio"
            else:
                nivel = "alto"
            
            interpretaciones[nombre] = f"{nivel} ({valor:.3f})"
        
        return interpretaciones
    
    def calcular_similitudes(self, vectores: List[np.ndarray], ids: List[str] = None) -> Dict[str, Any]:
        """Calcula matriz de similitudes entre vectores"""
        try:
            if len(vectores) < 2:
                return {
                    'success': False,
                    'error': 'Se necesitan al menos 2 vectores para calcular similitudes'
                }
            
            # Convertir a matriz numpy
            matriz_vectores = np.array(vectores)
            
            # Calcular similitudes coseno
            matriz_similitudes = cosine_similarity(matriz_vectores)
            
            # Generar IDs si no se proporcionan
            if not ids:
                ids = [f"doc_{i}" for i in range(len(vectores))]
            
            # Encontrar pares más similares
            pares_similares = []
            for i in range(len(matriz_similitudes)):
                for j in range(i + 1, len(matriz_similitudes)):
                    similitud = matriz_similitudes[i][j]
                    if similitud > self.config.get('umbral_similitud', 0.3):
                        pares_similares.append({
                            'doc1': ids[i],
                            'doc2': ids[j],
                            'similitud': float(similitud)
                        })
            
            # Ordenar por similitud descendente
            pares_similares.sort(key=lambda x: x['similitud'], reverse=True)
            
            resultado = {
                'success': True,
                'matriz_similitudes': matriz_similitudes.tolist(),
                'pares_similares': pares_similares[:20],  # Top 20
                'estadisticas': {
                    'similitud_promedio': float(np.mean(matriz_similitudes)),
                    'similitud_maxima': float(np.max(matriz_similitudes[matriz_similitudes < 1.0])),
                    'similitud_minima': float(np.min(matriz_similitudes)),
                    'pares_sobre_umbral': len(pares_similares)
                },
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"Similitudes calculadas: {len(pares_similares)} pares sobre umbral")
            return resultado
            
        except Exception as e:
            logger.error(f"Error calculando similitudes: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def reducir_dimensionalidad(self, vectores: List[np.ndarray], n_componentes: int = None) -> Dict[str, Any]:
        """Reduce la dimensionalidad de los vectores usando PCA"""
        try:
            if not n_componentes:
                n_componentes = self.config.get('dimensiones_pca', 50)
            
            matriz_vectores = np.array(vectores)
            
            if matriz_vectores.shape[1] <= n_componentes:
                return {
                    'success': False,
                    'error': f'Los vectores ya tienen {matriz_vectores.shape[1]} dimensiones, menor que {n_componentes}'
                }
            
            # Aplicar PCA
            pca = PCA(n_components=n_componentes)
            vectores_reducidos = pca.fit_transform(matriz_vectores)
            
            resultado = {
                'success': True,
                'vectores_reducidos': vectores_reducidos.tolist(),
                'dimensiones_originales': matriz_vectores.shape[1],
                'dimensiones_reducidas': n_componentes,
                'varianza_explicada': pca.explained_variance_ratio_.tolist(),
                'varianza_total_explicada': float(np.sum(pca.explained_variance_ratio_)),
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"Dimensionalidad reducida: {matriz_vectores.shape[1]} -> {n_componentes} (varianza: {resultado['varianza_total_explicada']:.3f})")
            return resultado
            
        except Exception as e:
            logger.error(f"Error reduciendo dimensionalidad: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def generar_representacion_neo4j(self, datos_procesados: Dict[str, Any]) -> Dict[str, Any]:
        """Genera representación optimizada para Neo4j"""
        try:
            # Extraer información clave
            id_unico = datos_procesados.get('id_unico', 'unknown')
            propiedades = datos_procesados.get('propiedades', {})
            relaciones = datos_procesados.get('relaciones', [])
            
            # Crear nodo principal
            nodo_principal = {
                'id': id_unico,
                'tipo': 'Fenomeno',
                'propiedades': {
                    'descripcion': propiedades.get('descripcion', ''),
                    'timestamp': datos_procesados.get('timestamp_sistema'),
                    'peso_existencial': propiedades.get('peso_existencial', 0.5),
                    'intensidad_fenomenologica': propiedades.get('intensidad_fenomenologica', 0.5)
                }
            }
            
            # Crear nodos de características vectoriales
            nodos_caracteristicas = []
            if 'features_tfidf' in propiedades:
                features = propiedades['features_tfidf']
                if isinstance(features, list):
                    for i, feature in enumerate(features[:10]):  # Top 10
                        nodos_caracteristicas.append({
                            'id': f"{id_unico}_feature_{i}",
                            'tipo': 'Caracteristica',
                            'propiedades': {
                                'termino': feature.get('termino', ''),
                                'peso': feature.get('peso', 0),
                                'importancia': feature.get('importancia', 0)
                            }
                        })
            
            # Crear relaciones
            relaciones_neo4j = []
            
            # Relaciones con características
            for nodo_car in nodos_caracteristicas:
                relaciones_neo4j.append({
                    'desde': id_unico,
                    'hacia': nodo_car['id'],
                    'tipo': 'TIENE_CARACTERISTICA',
                    'propiedades': {
                        'peso': nodo_car['propiedades']['peso']
                    }
                })
            
            # Relaciones originales
            for relacion in relaciones:
                relaciones_neo4j.append({
                    'desde': id_unico,
                    'hacia': relacion.get('id_destino', 'unknown'),
                    'tipo': relacion.get('tipo', 'RELACIONADO_CON'),
                    'propiedades': relacion.get('propiedades', {})
                })
            
            resultado = {
                'success': True,
                'nodos': [nodo_principal] + nodos_caracteristicas,
                'relaciones': relaciones_neo4j,
                'estadisticas': {
                    'total_nodos': 1 + len(nodos_caracteristicas),
                    'total_relaciones': len(relaciones_neo4j)
                },
                'timestamp': datetime.now().isoformat()
            }
            
            logger.info(f"Representación Neo4j generada: {resultado['estadisticas']['total_nodos']} nodos, {resultado['estadisticas']['total_relaciones']} relaciones")
            return resultado
            
        except Exception as e:
            logger.error(f"Error generando representación Neo4j: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def procesar_completo(self, datos: Dict[str, Any]) -> Dict[str, Any]:
        """Procesa completamente los datos: vectores + gradientes + Neo4j"""
        try:
            resultado_completo = {
                'id_procesamiento': datos.get('id_unico', 'unknown'),
                'timestamp_inicio': datetime.now().isoformat(),
                'pasos_completados': [],
                'resultados': {},
                'errores': []
            }
            
            # PASO 1: Extraer vectores si hay texto
            descripcion = datos.get('propiedades', {}).get('descripcion', '')
            if descripcion:
                resultado_vectores = self.extraer_vectores_texto(
                    descripcion, 
                    datos.get('id_unico')
                )
                if resultado_vectores.get('success'):
                    resultado_completo['resultados']['vectores'] = resultado_vectores
                    resultado_completo['pasos_completados'].append('extraccion_vectores')
                    
                    # Agregar características al objeto de datos
                    if 'propiedades' not in datos:
                        datos['propiedades'] = {}
                    datos['propiedades']['features_tfidf'] = resultado_vectores['caracteristicas_importantes']
                else:
                    resultado_completo['errores'].append(f"Error en vectores: {resultado_vectores.get('error')}")
            
            # PASO 2: Calcular gradientes
            resultado_gradientes = self.calcular_gradientes_fenomenologicos(datos)
            if resultado_gradientes.get('success'):
                resultado_completo['resultados']['gradientes'] = resultado_gradientes
                resultado_completo['pasos_completados'].append('calculo_gradientes')
                
                # Agregar gradientes al objeto de datos
                if 'propiedades' not in datos:
                    datos['propiedades'] = {}
                datos['propiedades']['gradientes'] = resultado_gradientes['gradientes_individuales']
                datos['propiedades']['gradiente_compuesto'] = resultado_gradientes['gradiente_compuesto']
            else:
                resultado_completo['errores'].append(f"Error en gradientes: {resultado_gradientes.get('error')}")
            
            # PASO 3: Generar representación Neo4j
            resultado_neo4j = self.generar_representacion_neo4j(datos)
            if resultado_neo4j.get('success'):
                resultado_completo['resultados']['neo4j'] = resultado_neo4j
                resultado_completo['pasos_completados'].append('representacion_neo4j')
            else:
                resultado_completo['errores'].append(f"Error en Neo4j: {resultado_neo4j.get('error')}")
            
            resultado_completo['timestamp_fin'] = datetime.now().isoformat()
            resultado_completo['success'] = len(resultado_completo['pasos_completados']) > 0
            
            logger.info(f"Procesamiento completo finalizado: {len(resultado_completo['pasos_completados'])} pasos completados")
            return resultado_completo
            
        except Exception as e:
            logger.error(f"Error en procesamiento completo: {e}")
            return {
                'success': False,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

# Función de utilidad para testing
def test_procesador():
    """Función de prueba del procesador vectorial"""
    procesador = ProcesadorVectorial()
    
    # Datos de prueba
    datos_prueba = {
        'id_unico': 'test_001',
        'timestamp_sistema': datetime.now().isoformat(),
        'propiedades': {
            'descripcion': 'Este es un texto de prueba para el procesamiento vectorial y análisis fenomenológico del sistema YO Estructural.',
            'emociones_detectadas': ['alegria', 'curiosidad'],
            'peso_existencial': 0.7,
            'coherencia_narrativa': 0.8
        },
        'relaciones': [
            {'id_destino': 'test_002', 'tipo': 'SE_RELACIONA_CON'}
        ]
    }
    
    # Procesar
    resultado = procesador.procesar_completo(datos_prueba)
    
    print("\n" + "="*50)
    print("PRUEBA DEL PROCESADOR VECTORIAL")
    print("="*50)
    print(f"Éxito: {resultado.get('success')}")
    print(f"Pasos completados: {resultado.get('pasos_completados')}")
    print(f"Errores: {resultado.get('errores')}")
    
    if resultado.get('success'):
        if 'vectores' in resultado['resultados']:
            vectores = resultado['resultados']['vectores']
            print(f"\nVectores: {vectores['dimensiones']} dimensiones")
            print(f"Características importantes: {len(vectores['caracteristicas_importantes'])}")
        
        if 'gradientes' in resultado['resultados']:
            gradientes = resultado['resultados']['gradientes']
            print(f"\nGradiente compuesto: {gradientes['gradiente_compuesto']:.3f}")
            print("Gradientes individuales:")
            for nombre, valor in gradientes['gradientes_individuales'].items():
                print(f"  - {nombre}: {valor:.3f}")
        
        if 'neo4j' in resultado['resultados']:
            neo4j = resultado['resultados']['neo4j']
            print(f"\nNeo4j: {neo4j['estadisticas']['total_nodos']} nodos, {neo4j['estadisticas']['total_relaciones']} relaciones")
    
    print("="*50)
    return resultado

if __name__ == "__main__":
    test_procesador()