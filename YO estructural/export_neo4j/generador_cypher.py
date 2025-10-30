import os
import yaml
from typing import List, Dict

class GeneradorCypher:
    """Genera scripts Cypher para exportar a Neo4j"""
    
    def __init__(self, ruta_datos: str):
        self.ruta_datos = ruta_datos
    
    def generar_script_completo(self, ruta_salida: str) -> str:
        """Genera script Cypher completo del sistema"""
        script_lines = [
            "// Script de exportación completa del Sistema Fenomenológico",
            "// Generado automáticamente\n",
            "// Limpiar base de datos",
            "MATCH (n) DETACH DELETE n;\n"
        ]
        
        # Crear nodos por nivel
        script_lines.extend(self._generar_nodos_preinstancias())
        script_lines.extend(self._generar_nodos_instancias())
        script_lines.extend(self._generar_nodos_vohexistencias())
        script_lines.extend(self._generar_nodos_fenomenos())
        script_lines.extend(self._generar_nodos_contextos())
        
        # Crear relaciones
        script_lines.extend(self._generar_relaciones())
        
        # Crear nodos del YO
        script_lines.extend(self._generar_nodos_yo())
        
        # Guardar script
        ruta_script = os.path.join(ruta_salida, "sistema_completo.cypher")
        with open(ruta_script, 'w', encoding='utf-8') as f:
            f.write('\n'.join(script_lines))
        
        return ruta_script
    
    def _generar_nodos_instancias(self) -> List[str]:
        """Genera comandos Cypher para nodos de instancias"""
        comandos = ["// Crear nodos de Instancias"]
        
        ruta_instancias = os.path.join(self.ruta_datos, "instancias")
        if os.path.exists(ruta_instancias):
            for archivo in os.listdir(ruta_instancias):
                if archivo.endswith('.yaml'):
                    with open(os.path.join(ruta_instancias, archivo), 'r', encoding='utf-8') as f:
                        data = yaml.safe_load(f)
                    
                    propiedades = ", ".join([f"{k}: '{v}'" for k, v in data.get('propiedades', {}).items()])
                    comando = f"CREATE (:{data['id']}:Instancia {{id: '{data['id']}', {propiedades}, activacion: {data.get('activacion_actual', 0.0)}}});"
                    comandos.append(comando)
        
        comandos.append("")  # Línea vacía
        return comandos
    
    def _generar_nodos_yo(self) -> List[str]:
        """Genera nodos del sistema YO con métricas extendidas"""
        comandos = ["// Crear nodos del Sistema YO"]
        
        # Nodos base del YO
        niveles_yo = [
            ("ProtoYO", "proto_yo", 0),
            ("YoSensorial", "yo_sensorial", 1),
            ("YoAfectivo", "yo_afectivo", 2),
            ("YoReflexivo", "yo_reflexivo", 3),
            ("YoSimbolico", "yo_simbolico", 4),
            ("YoNarrativo", "yo_narrativo", 5)
        ]
        
        for label, tipo, nivel in niveles_yo:
            comandos.append(
                f"CREATE (:YO:{label} {{"
                f"tipo: '{tipo}', "
                f"nivel: {nivel}, "
                f"coherencia_narrativa: 0.0, "
                f"estabilidad_contextual: 0.0, "
                f"integracion_afectiva: 0.0, "
                f"ultima_actualizacion: datetime()}});"
            )
        
        # Nodos para tensiones estructurales
        comandos.extend([
            "// Crear nodos de tensiones estructurales",
            "CREATE (:TensionEstructural:Temporal {tipo: 'temporal'});",
            "CREATE (:TensionEstructural:Contextual {tipo: 'contextual'});",
            "CREATE (:TensionEstructural:Afectiva {tipo: 'afectiva'});"
        ])
        
        comandos.append("")
        return comandos
    
    def _generar_relaciones_yo(self) -> List[str]:
        """Genera relaciones del sistema YO"""
        return [
            "// Crear relaciones jerárquicas del YO",
            "MATCH (y1:YO), (y2:YO) ",
            "WHERE y1.nivel + 1 = y2.nivel",
            "CREATE (y1)-[:EMERGE_EN]->(y2);",
            "",
            "// Crear relaciones con tensiones",
            "MATCH (y:YO), (t:TensionEstructural)",
            "WHERE exists(y.ultima_actualizacion)",
            "CREATE (y)-[:PRESENTA_TENSION {timestamp: datetime()}]->(t);",
            ""
        ]
    
    def generar_nodos_estado_yo(self, estado: Dict) -> List[str]:
        """Genera nodos para el estado actual del YO"""
        comandos = ["// Crear nodos de Estado YO actual"]
        
        # Nodo principal del estado
        timestamp = estado.get('timestamp', datetime.now().isoformat())
        comandos.append(f"""
            CREATE (e:EstadoYO {{
                timestamp: datetime('{timestamp}'),
                version: {estado.get('version', 0)},
                tipo_yo: '{estado.get('tipo_yo', 'proto_yo')}'
            }});
        """)
        
        # Nodos de reflexiones
        for i, reflexion in enumerate(estado.get('reflexiones', [])):
            comandos.append(f"""
            CREATE (r:Reflexion {{
                id: 'reflexion_{i}',
                contenido: '{reflexion.get('contenido', '')}',
                timestamp: datetime('{reflexion.get('timestamp', timestamp)}')
            }});
            MATCH (e:EstadoYO), (r:Reflexion {{id: 'reflexion_{i}'}}) 
            WHERE e.timestamp = datetime('{timestamp}')
            CREATE (e)-[:CONTIENE]->(r);
        """)
        
        # Nodos de contextos activos
        for contexto in estado.get('contextos_activos', []):
            comandos.append(f"""
            MERGE (c:Contexto {{id: '{contexto}'}});
            MATCH (e:EstadoYO), (c:Contexto {{id: '{contexto}'}}) 
            WHERE e.timestamp = datetime('{timestamp}')
            CREATE (e)-[:ACTIVA]->(c);
        """)
        
        return comandos
    
    def generar_nodos_tensiones(self, historial: List[Dict]) -> List[str]:
        """Genera nodos para las tensiones estructurales"""
        comandos = ["// Crear nodos de Tensiones Estructurales"]
        
        for registro in historial:
            timestamp = registro.get('timestamp', datetime.now().isoformat())
            for tension in registro.get('tensiones_activas', []):
                comandos.append(f"""
                CREATE (t:Tension {{
                    tipo: '{tension.get('tipo', 'indefinida')}',
                    descripcion: '{tension.get('descripcion', '')}',
                    timestamp: datetime('{timestamp}')
                }});
                MATCH (e:EstadoYO) 
                WHERE e.timestamp <= datetime('{timestamp}')
                WITH e, t ORDER BY e.timestamp DESC LIMIT 1
                CREATE (e)-[:PRESENTA]->(t);
                """)
        
        return comandos
    
    def exportar_metricas_yo(self, estado: Dict, metricas: Dict) -> List[str]:
        """Exporta métricas actuales del YO a Neo4j"""
        comandos = ["// Actualizar métricas del YO"]
        
        # Actualizar métricas del nivel actual
        tipo_yo = estado.get('tipo_yo', 'yo_narrativo')
        comandos.append(f"""
            MATCH (y:YO {{tipo: '{tipo_yo}'}}) 
            SET 
                y.coherencia_narrativa = {metricas['coherencia_narrativa']},
                y.estabilidad_contextual = {metricas['estabilidad_contextual']},
                y.integracion_afectiva = {metricas['coherencia_afectiva']},
                y.ultima_actualizacion = datetime()
            RETURN y;
        """)
        
        # Registrar tensiones activas
        if estado.get('tensiones_activas'):
            for tension in estado['tensiones_activas']:
                comandos.append(f"""
                    MATCH (y:YO {{tipo: '{tipo_yo}'}}), (t:TensionEstructural {{tipo: '{tension['tipo']}'}}) 
                    CREATE (y)-[:PRESENTA_TENSION {{
                        timestamp: datetime(),
                        intensidad: {tension.get('intensidad', 0.5)},
                        descripcion: '{tension.get('descripcion', 'Tensión detectada')}'
                    }}]->(t);
                """)
        
        return comandos