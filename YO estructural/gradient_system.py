# Extensión del sistema existente
import sqlite3
import json
from typing import List, Dict, Tuple
from datetime import datetime

class ConceptVector:
    def __init__(self, concept_id: str, vector: List[float]):
        self.concept_id = concept_id
        self.vector = vector

class UltraPrecisionGradientSystem:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.initialize_db()
    
    def initialize_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS concepts (
                    id TEXT PRIMARY KEY,
                    vector TEXT,  -- JSON array
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.execute('''
                CREATE TABLE IF NOT EXISTS gradients (
                    concept1 TEXT,
                    concept2 TEXT,
                    value REAL,
                    confidence REAL,
                    algorithm TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (concept1, concept2, algorithm)
                )
            ''')
    
    def add_concept(self, concept_vector: ConceptVector):
        """Añade un nuevo concepto al sistema"""
        pass  # Implementar según necesidades

class VohexGradientSystem(UltraPrecisionGradientSystem):
    """Sistema de gradientes extendido para vohexistencias"""
    
    def __init__(self, db_path: str = "gradients_vohex.db"):
        super().__init__(db_path)
        self._init_vohex_tables()
    
    def _init_vohex_tables(self):
        """Inicializa tablas para vohexistencias"""
        with sqlite3.connect(self.db.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS vohexistencias (
                    id TEXT PRIMARY KEY,
                    instancias TEXT,  -- JSON array de IDs
                    constante_emergente TEXT,
                    peso_coexistencial REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
    
    def get_all_gradients_for_node(self, concept_id: str) -> Dict:
        """Implementación requerida: obtiene todos los gradientes para un nodo"""
        gradientes = []
        proximidad_promedio = 0.0
        
        with sqlite3.connect(self.db.db_path) as conn:
            # Obtener todos los otros conceptos
            cursor = conn.execute('SELECT id FROM concepts WHERE id != ?', (concept_id,))
            otros_conceptos = [row[0] for row in cursor.fetchall()]
            
            valores_gradiente = []
            for otro_id in otros_conceptos:
                # Obtener gradiente más reciente
                cursor = conn.execute('''
                    SELECT value, confidence, algorithm, created_at
                    FROM gradients 
                    WHERE (concept1 = ? AND concept2 = ?) OR (concept1 = ? AND concept2 = ?)
                    AND algorithm = 'ultra_precision_combined'
                    ORDER BY created_at DESC LIMIT 1
                ''', (concept_id, otro_id, otro_id, concept_id))
                
                row = cursor.fetchone()
                if row:
                    gradiente_info = {
                        "nodo_destino": otro_id,
                        "valor_gradiente": row[0],
                        "confianza": row[1],
                        "algoritmo": row[2],
                        "timestamp": row[3]
                    }
                    gradientes.append(gradiente_info)
                    valores_gradiente.append(row[0])
            
            # Calcular proximidad promedio (centralidad relacional)
            if valores_gradiente:
                proximidad_promedio = sum(valores_gradiente) / len(valores_gradiente)
        
        return {
            "nodo_origen": concept_id,
            "gradientes": gradientes,
            "proximidad_promedio": proximidad_promedio,
            "total_relaciones": len(gradientes),
            "timestamp_consulta": datetime.now().isoformat()
        }
    
    def calcular_nodo_central_vohex(self, nodos_vohex: List[str]) -> Dict:
        """Calcula el nodo más central dentro de una vohexistencia"""
        centralidades = {}
        
        for nodo in nodos_vohex:
            info_gradientes = self.get_all_gradients_for_node(nodo)
            # Filtrar solo gradientes con otros nodos del vohex
            gradientes_internos = [
                g for g in info_gradientes["gradientes"] 
                if g["nodo_destino"] in nodos_vohex
            ]
            
            if gradientes_internos:
                centralidad = sum(g["valor_gradiente"] for g in gradientes_internos) / len(gradientes_internos)
            else:
                centralidad = 0.0
            
            centralidades[nodo] = {
                "centralidad": centralidad,
                "relaciones_internas": len(gradientes_internos),
                "gradientes_internos": gradientes_internos
            }
        
        # Encontrar nodo más central
        nodo_central = max(centralidades.keys(), key=lambda x: centralidades[x]["centralidad"])
        
        return {
            "nodo_central": nodo_central,
            "centralidad_maxima": centralidades[nodo_central]["centralidad"],
            "analisis_completo": centralidades,
            "cohesion_vohex": sum(c["centralidad"] for c in centralidades.values()) / len(centralidades)
        }
    
    def add_concept(self, concept_vector: ConceptVector):
        """Sobrescribe para recalcular automáticamente vohexistencias"""
        super().add_concept(concept_vector)
        self._actualizar_vohexistencias_automatico(concept_vector.concept_id)
    
    def _actualizar_vohexistencias_automatico(self, nuevo_concepto_id: str):
        """Actualiza automáticamente las vohexistencias cuando se agrega un concepto"""
        # Obtener gradientes del nuevo concepto
        info_gradientes = self.get_all_gradients_for_node(nuevo_concepto_id)
        
        # Buscar conceptos con alta similitud (candidatos a vohexistencia)
        candidatos_vohex = [
            g["nodo_destino"] for g in info_gradientes["gradientes"]
            if g["valor_gradiente"] >= 0.7 and g["confianza"] >= 0.8
        ]
        
        if len(candidatos_vohex) >= 2:  # Mínimo 3 nodos para vohexistencia
            candidatos_vohex.append(nuevo_concepto_id)
            self._crear_vohexistencia_automatica(candidatos_vohex)
    
    def _crear_vohexistencia_automatica(self, nodos: List[str]):
        """Crea automáticamente una vohexistencia"""
        vohex_id = f"auto_vohex_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Calcular constante emergente basada en propiedades comunes
        constante = self._detectar_constante_emergente(nodos)
        
        # Calcular peso coexistencial
        analisis_central = self.calcular_nodo_central_vohex(nodos)
        peso = analisis_central["cohesion_vohex"]
        
        # Guardar en base de datos
        with sqlite3.connect(self.db.db_path) as conn:
            conn.execute('''
                INSERT INTO vohexistencias (id, instancias, constante_emergente, peso_coexistencial)
                VALUES (?, ?, ?, ?)
            ''', (vohex_id, json.dumps(nodos), constante, peso))
        
        print(f"🔗 Vohexistencia automática creada: {vohex_id} (peso: {peso:.2f})")
        return vohex_id