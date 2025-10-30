import uuid
import datetime
import yaml
import os

class Macrocontexto:
    """Representa un macrocontexto (conjunto de contextos relacionados)"""
    
    def __init__(self, nombre="", descripcion=""):
        self.id = str(uuid.uuid4())[:8]  # ID único abreviado
        self.nombre = nombre
        self.descripcion = descripcion
        self.contextos_ids = []  # IDs de los contextos incluidos
        self.patron_emergente = ""  # Patrón que emerge de los contextos
        self.timestamp = datetime.datetime.now().isoformat()
        self.reflexion_yo = ""  # Reflexión del YO sobre este macrocontexto
    
    def agregar_contexto(self, contexto_id):
        if contexto_id not in self.contextos_ids:
            self.contextos_ids.append(contexto_id)
    
    def establecer_patron(self, patron):
        self.patron_emergente = patron
    
    def establecer_reflexion(self, reflexion):
        self.reflexion_yo = reflexion
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "contextos_ids": self.contextos_ids,
            "patron_emergente": self.patron_emergente,
            "reflexion_yo": self.reflexion_yo,
            "timestamp": self.timestamp
        }
    
    def guardar(self, ruta_base):
        """Guarda el macrocontexto en formato YAML"""
        ruta_completa = os.path.join(ruta_base, f"macrocontexto_{self.id}.yaml")
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            yaml.dump(self.to_dict(), f, default_flow_style=False, allow_unicode=True)
        return ruta_completa
    
    @classmethod
    def from_dict(cls, data):
        macrocontexto = cls(data["nombre"], data["descripcion"])
        macrocontexto.id = data["id"]
        macrocontexto.contextos_ids = data["contextos_ids"]
        macrocontexto.patron_emergente = data["patron_emergente"]
        macrocontexto.reflexion_yo = data["reflexion_yo"]
        macrocontexto.timestamp = data["timestamp"]
        return macrocontexto
    
    @classmethod
    def cargar(cls, ruta_archivo):
        """Carga un macrocontexto desde un archivo YAML"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return cls.from_dict(data)