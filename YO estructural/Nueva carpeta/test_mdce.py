import unittest
import yaml
import json
from neo4j import GraphDatabase
from motor_yo.sistema_yo_emergente import SistemaYoEmergente
from main import SistemaYoAutomatizado

class TestMDCEAvanzado(unittest.TestCase):
    """Suite de pruebas avanzadas para MDCE con validación Neo4j"""
    
    def setUp(self):
        self.sistema = SistemaYoAutomatizado()
        self.neo4j_driver = GraphDatabase.driver(
            "bolt://localhost:7687",
            auth=("neo4j", "password")
        )
        
    def tearDown(self):
        # Limpiar base de datos después de cada test
        with self.neo4j_driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        self.neo4j_driver.close()
    
    def test_ciclo_completo_automatizado(self):
        """Prueba el ciclo fenomenológico completo automático"""
        # Ejecutar ciclo completo
        resultado = self.sistema.ejecutar_ciclo_completo()
        
        # Validar que todos los nodos están en Neo4j
        with self.neo4j_driver.session() as session:
            # Verificar PreInstancias
            result = session.run("MATCH (p:PreInstancia) RETURN count(p) as count")
            preinstancias_count = result.single()["count"]
            self.assertGreater(preinstancias_count, 0, "Deben existir PreInstancias en Neo4j")
            
            # Verificar Instancias
            result = session.run("MATCH (i:Instancia) RETURN count(i) as count")
            instancias_count = result.single()["count"]
            self.assertGreater(instancias_count, 0, "Deben existir Instancias en Neo4j")
            
            # Verificar Fenómenos
            result = session.run("MATCH (f:Fenomeno) RETURN count(f) as count")
            fenomenos_count = result.single()["count"]
            self.assertGreater(fenomenos_count, 0, "Deben existir Fenómenos en Neo4j")
            
            # Verificar YO
            result = session.run("MATCH (y:YO) RETURN count(y) as count")
            yo_count = result.single()["count"]
            self.assertGreater(yo_count, 0, "Debe existir al menos un nodo YO en Neo4j")
            
            # Verificar Voluntad
            result = session.run("MATCH (v:Voluntad) RETURN count(v) as count")
            voluntad_count = result.single()["count"]
            self.assertGreater(voluntad_count, 0, "Debe existir nodo Voluntad en Neo4j")
    
    def test_rutas_semanticas_decision(self):
        """Prueba que las rutas semánticas hacia decisiones estén formadas correctamente"""
        self.sistema.ejecutar_ciclo_completo()
        
        with self.neo4j_driver.session() as session:
            # Verificar ruta completa: PreInstancia -> ... -> Voluntad -> Decisión
            result = session.run("""
                MATCH path = (p:PreInstancia)-[*]->(d:Decision)
                RETURN length(path) as ruta_longitud, count(path) as rutas_count
            """)
            
            record = result.single()
            if record:
                self.assertGreater(record["rutas_count"], 0, "Debe existir al menos una ruta completa")
                self.assertGreaterEqual(record["ruta_longitud"], 8, "La ruta debe tener al menos 8 niveles")
    
    def test_auto_reestructuracion_contradicciones(self):
        """Prueba que la auto-reestructuración se active con contradicciones"""
        # Inyectar contradicción de alto nivel
        contradiccion_critica = {
            "tipo": "narrativa_fragmentada",
            "intensidad": 0.9,
            "nivel": 4,
            "contextos_afectados": ["temporal", "identitario", "existencial"]
        }
        
        # Ejecutar con contradicción
        self.sistema.sistema_yo.historial_contradicciones.append(contradiccion_critica)
        resultado = self.sistema.ejecutar_ciclo_completo()
        
        # Verificar en Neo4j que se creó la contradicción y la reconfiguración
        with self.neo4j_driver.session() as session:
            result = session.run("""
                MATCH (y:YO)-[:PRESENTA_CONTRADICCION]->(c:Contradiccion)
                WHERE c.intensidad > 0.8
                RETURN c.tipo as tipo, c.intensidad as intensidad
            """)
            
            contradiccion = result.single()
            self.assertIsNotNone(contradiccion, "Debe existir contradicción de alta intensidad")
            self.assertEqual(contradiccion["tipo"], "narrativa_fragmentada")
            
            # Verificar que se activó reconfiguración
            result = session.run("""
                MATCH (y:YO)
                WHERE y.version > 0
                RETURN y.version as version
            """)
            
            yo_reconfigurado = result.single()
            self.assertIsNotNone(yo_reconfigurado, "El YO debe haberse reconfigurado")
            self.assertGreater(yo_reconfigurado["version"], 0)
    
    def test_coherencia_estado_neo4j(self):
        """Prueba que el estado en Neo4j sea coherente con el sistema"""
        self.sistema.ejecutar_ciclo_completo()
        
        # Obtener estado del sistema
        estado_sistema = self.sistema.sistema_yo.obtener_estado_completo()
        
        # Obtener estado de Neo4j
        with self.neo4j_driver.session() as session:
            result = session.run("""
                MATCH (y:YO)
                RETURN y.coherencia_narrativa as coherencia,
                       y.estabilidad_contextual as estabilidad,
                       y.integracion_afectiva as integracion,
                       y.version as version
                ORDER BY y.version DESC
                LIMIT 1
            """)
            
            estado_neo4j = result.single()
            
            # Comparar coherencias
            self.assertAlmostEqual(
                estado_sistema["coherencia"],
                estado_neo4j["coherencia"],
                places=2,
                msg="La coherencia debe coincidir entre sistema y Neo4j"
            )
            
            # Verificar que las métricas están en rango válido
            self.assertGreaterEqual(estado_neo4j["coherencia"], 0.0)
            self.assertLessEqual(estado_neo4j["coherencia"], 1.0)
    
    def test_navegabilidad_grafo_completo(self):
        """Prueba que el grafo completo sea navegable desde raíz hasta metaYO"""
        self.sistema.ejecutar_ciclo_completo()
        
        with self.neo4j_driver.session() as session:
            # Verificar navegabilidad completa
            result = session.run("""
                MATCH (inicio:PreInstancia)
                MATCH (fin:YO)
                MATCH path = shortestPath((inicio)-[*]->(fin))
                RETURN length(path) as longitud_ruta, count(path) as rutas_disponibles
            """)
            
            navegabilidad = result.single()
            self.assertIsNotNone(navegabilidad, "Debe existir ruta navegable")
            self.assertGreater(navegabilidad["rutas_disponibles"], 0)
            self.assertGreaterEqual(navegabilidad["longitud_ruta"], 5)

if __name__ == '__main__':
    unittest.main()