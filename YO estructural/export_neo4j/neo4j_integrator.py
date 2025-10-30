import yaml
import json
import csv
import logging
from datetime import datetime
from neo4j import GraphDatabase

class Neo4jIntegrator:
    def __init__(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        # Configurar logging
        self._configurar_logging()
        
        # Conectar a Neo4j
        conf = self.config['neo4j']
        uri = f"bolt://{conf['host']}:{conf['port']}"
        self.driver = GraphDatabase.driver(uri, auth=(conf['username'], conf['password']))
        self.nodos_def = self.config['nodos_neo4j']
        self.relaciones_def = self.config.get('relaciones_neo4j', [])
    
    def _configurar_logging(self):
        """Configura el sistema de logging"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"logs_sistema/neo4j_sync_{timestamp}.log"
        
        self.logger = logging.getLogger("Neo4jIntegrator")
        self.logger.setLevel(logging.DEBUG)
        
        # Handler para archivo
        fh = logging.FileHandler(log_file, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        
        # Handler para consola
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # Formato
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def close(self):
        self.logger.info("Cerrando conexión con Neo4j")
        self.driver.close()
    
    def importar_json(self, path):
        self.logger.info(f"Importando datos desde JSON: {path}")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            self._crear_nodos_y_relaciones(datos)
            self.logger.info(f"Importación JSON completada: {len(datos)} registros procesados")
        except Exception as e:
            self.logger.error(f"Error importando JSON: {str(e)}")
            raise
    
    def importar_csv(self, path):
        self.logger.info(f"Importando datos desde CSV: {path}")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                datos = list(reader)
            self._crear_nodos_y_relaciones(datos)
            self.logger.info(f"Importación CSV completada: {len(datos)} registros procesados")
        except Exception as e:
            self.logger.error(f"Error importando CSV: {str(e)}")
            raise
    
    def _crear_nodos_y_relaciones(self, datos):
        self.logger.info("Iniciando creación de nodos y relaciones")
        with self.driver.session(database=self.config['neo4j']['database']) as session:
            # Crear nodos
            for item in datos:
                try:
                    tipo = item['tipo'].capitalize()
                    if tipo not in self.nodos_def:
                        self.logger.warning(f"Tipo de nodo no definido: {tipo}")
                        continue
                        
                    etiqueta = self.nodos_def[tipo]['etiqueta_neo4j']
                    props = {k: item[k] for k in self.nodos_def[tipo]['propiedades'] if k in item}
                    props['id'] = int(item['id'])
                    
                    set_clause = ', '.join([f'n.{k} = ${k}' for k in props])
                    session.run(f"""
                        MERGE (n:{etiqueta} {{id: $id}})
                        SET {set_clause}
                    """, **props)
                    
                    self.logger.debug(f"Nodo creado: {etiqueta} (id: {props['id']})")
                except Exception as e:
                    self.logger.error(f"Error creando nodo: {str(e)}")
                    continue
            
            # Crear relaciones
            for item in datos:
                try:
                    origen_tipo = item['tipo'].capitalize()
                    rel_id = item.get('relacion_con')
                    if not rel_id:
                        continue
                        
                    for rel in self.relaciones_def:
                        if rel['origen'].lower() == origen_tipo.lower():
                            tipo_rel = rel['tipo']
                            session.run(f"""
                                MATCH (a:{self.nodos_def[rel['origen']]['etiqueta_neo4j']} {{id: $ida}})
                                MATCH (b:{self.nodos_def[rel['destino']]['etiqueta_neo4j']} {{id: $idb}})
                                MERGE (a)-[:{tipo_rel}]->(b)
                            """, ida=int(item['id']), idb=int(rel_id))
                            
                            self.logger.debug(f"Relación creada: ({item['id']})-[{tipo_rel}]->({rel_id})")
                except Exception as e:
                    self.logger.error(f"Error creando relación: {str(e)}")
                    continue
            
            self.logger.info("Creación de nodos y relaciones completada")