import uuid
import datetime
import yaml
import os
import networkx as nx

class RedContextos:
    """Representa una red de contextos como un grafo experiencial"""
    
    def __init__(self, nombre="", descripcion=""):
        self.id = str(uuid.uuid4())[:8]  # ID único abreviado
        self.nombre = nombre
        self.descripcion = descripcion
        self.grafo = nx.DiGraph()  # Grafo dirigido para representar relaciones
        self.timestamp = datetime.datetime.now().isoformat()
        self.propiedades_emergentes = {}  # Propiedades que emergen de la red
    
    def agregar_nodo(self, id_nodo, tipo="contexto", atributos=None):
        """Agrega un nodo a la red (contexto, macrocontexto, etc.)"""
        self.grafo.add_node(id_nodo, tipo=tipo, **(atributos or {}))
    
    def agregar_relacion(self, id_origen, id_destino, tipo="contiene", peso=1.0, atributos=None):
        """Agrega una relación entre nodos"""
        self.grafo.add_edge(id_origen, id_destino, tipo=tipo, peso=peso, **(atributos or {}))
    
    def calcular_metricas(self):
        """Calcula métricas básicas del grafo"""
        return {
            "num_nodos": self.grafo.number_of_nodes(),
            "num_relaciones": self.grafo.number_of_edges(),
            "densidad": nx.density(self.grafo),
            "componentes_conectados": nx.number_connected_components(self.grafo.to_undirected()),
            "centralidad": {node: score for node, score in nx.degree_centrality(self.grafo).items()}
        }
    
    def to_dict(self):
        # Convertir el grafo a un formato serializable
        nodos = []
        for nodo, attrs in self.grafo.nodes(data=True):
            nodos.append({"id": nodo, **attrs})
            
        relaciones = []
        for origen, destino, attrs in self.grafo.edges(data=True):
            relaciones.append({"origen": origen, "destino": destino, **attrs})
        
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "nodos": nodos,
            "relaciones": relaciones,
            "propiedades_emergentes": self.propiedades_emergentes,
            "timestamp": self.timestamp
        }
    
    def guardar(self, ruta_base):
        """Guarda la red en formato YAML"""
        ruta_completa = os.path.join(ruta_base, f"red_{self.id}.yaml")
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            yaml.dump(self.to_dict(), f, default_flow_style=False, allow_unicode=True)
        return ruta_completa
    
    @classmethod
    def from_dict(cls, data):
        red = cls(data["nombre"], data["descripcion"])
        red.id = data["id"]
        red.timestamp = data["timestamp"]
        red.propiedades_emergentes = data["propiedades_emergentes"]
        
        # Reconstruir el grafo
        for nodo in data["nodos"]:
            nodo_id = nodo.pop("id")
            red.grafo.add_node(nodo_id, **nodo)
            
        for rel in data["relaciones"]:
            origen = rel.pop("origen")
            destino = rel.pop("destino")
            red.grafo.add_edge(origen, destino, **rel)
            
        return red
    
    @classmethod
    def cargar(cls, ruta_archivo):
        """Carga una red desde un archivo YAML"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls.from_dict(data)