import uuid
import datetime
import yaml
import os

class Metacampo:
    """Representa un metacampo (redes entre sistemas)"""
    
    def __init__(self, nombre="", descripcion=""):
        self.id = str(uuid.uuid4())[:8]  # ID único abreviado
        self.nombre = nombre
        self.descripcion = descripcion
        self.sistemas_relacionados = []  # IDs de los sistemas relacionados
        self.patrones_intersistema = []  # Patrones que emergen entre sistemas
        self.timestamp = datetime.datetime.now().isoformat()
        self.nivel_abstraccion = 5  # Nivel más alto de abstracción
    
    def agregar_sistema(self, sistema_id, tipo="ontosistema"):
        """Agrega un sistema relacionado al metacampo"""
        if sistema_id not in [s["id"] for s in self.sistemas_relacionados]:
            self.sistemas_relacionados.append({"id": sistema_id, "tipo": tipo})
    
    def agregar_patron(self, nombre, descripcion, propiedades=None):
        """Agrega un patrón intersistema"""
        self.patrones_intersistema.append({
            "nombre": nombre,
            "descripcion": descripcion,
            "propiedades": propiedades or {}
        })
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "sistemas_relacionados": self.sistemas_relacionados,
            "patrones_intersistema": self.patrones_intersistema,
            "nivel_abstraccion": self.nivel_abstraccion,
            "timestamp": self.timestamp
        }
    
    def guardar(self, ruta_base):
        """Guarda el metacampo en formato YAML"""
        ruta_completa = os.path.join(ruta_base, f"metacampo_{self.id}.yaml")
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            yaml.dump(self.to_dict(), f, default_flow_style=False, allow_unicode=True)
        return ruta_completa
    
    @classmethod
    def from_dict(cls, data):
        metacampo = cls(data["nombre"], data["descripcion"])
        metacampo.id = data["id"]
        metacampo.sistemas_relacionados = data["sistemas_relacionados"]
        metacampo.patrones_intersistema = data["patrones_intersistema"]
        metacampo.nivel_abstraccion = data["nivel_abstraccion"]
        metacampo.timestamp = data["timestamp"]
        return metacampo
    
    @classmethod
    def cargar(cls, ruta_archivo):
        """Carga un metacampo desde un archivo YAML"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls.from_dict(data)