import uuid
import datetime
import yaml
import os

class Contexto:
    """Representa un contexto completo con la estructura ': - . . . YO ...'"""
    
    def __init__(self, descripcion=""):
        self.id = str(uuid.uuid4())[:8]  # ID único abreviado
        self.descripcion = descripcion
        self.fenomenos = []  # Lista de objetos Fenomeno
        self.flujos = []  # Lista de eventos/flujos
        self.yo_presente = False  # Indica si hay un observador activo
        self.proyeccion_futura = ""  # Contenido de la proyección
        self.timestamp = datetime.datetime.now().isoformat()
    
    def agregar_fenomeno(self, fenomeno):
        self.fenomenos.append(fenomeno)
    
    def agregar_flujo(self, flujo):
        self.flujos.append(flujo)
    
    def activar_yo(self):
        self.yo_presente = True
    
    def establecer_proyeccion(self, proyeccion):
        self.proyeccion_futura = proyeccion
    
    def to_dict(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "fenomenos": [f.to_dict() for f in self.fenomenos],
            "flujos": self.flujos,
            "yo_presente": self.yo_presente,
            "proyeccion_futura": self.proyeccion_futura,
            "timestamp": self.timestamp
        }
    
    def guardar(self, ruta_base):
        """Guarda el contexto en formato YAML"""
        ruta_completa = os.path.join(ruta_base, f"contexto_{self.id}.yaml")
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            yaml.dump(self.to_dict(), f, default_flow_style=False, allow_unicode=True)
        return ruta_completa
    
    @classmethod
    def from_dict(cls, data):
        from .fenomeno import Fenomeno  # Importación local para evitar circular imports
        
        contexto = cls(data["descripcion"])
        contexto.id = data["id"]
        contexto.timestamp = data["timestamp"]
        contexto.yo_presente = data["yo_presente"]
        contexto.proyeccion_futura = data["proyeccion_futura"]
        contexto.flujos = data["flujos"]
        
        # Reconstruir fenómenos
        for f_data in data["fenomenos"]:
            fenomeno = Fenomeno.from_dict(f_data)
            contexto.fenomenos.append(fenomeno)
            
        return contexto
    
    @classmethod
    def cargar(cls, ruta_archivo):
        """Carga un contexto desde un archivo YAML"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls.from_dict(data)