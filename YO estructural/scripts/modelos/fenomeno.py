import uuid
import datetime

class Fenomeno:
    """Representa un fenómeno discreto (visual, sensorial, emocional)"""
    
    def __init__(self, contenido, tipo="general", propiedades=None):
        self.id = str(uuid.uuid4())[:8]  # ID único abreviado
        self.contenido = contenido  # El contenido del fenómeno
        self.tipo = tipo  # Tipo: visual, sensorial, emocional, etc.
        self.timestamp = datetime.datetime.now().isoformat()
        self.propiedades = propiedades or {}
    
    def to_dict(self):
        return {
            "id": self.id,
            "contenido": self.contenido,
            "tipo": self.tipo,
            "timestamp": self.timestamp,
            "propiedades": self.propiedades
        }
    
    @classmethod
    def from_dict(cls, data):
        fenomeno = cls(data["contenido"], data["tipo"])
        fenomeno.id = data["id"]
        fenomeno.timestamp = data["timestamp"]
        fenomeno.propiedades = data["propiedades"]
        return fenomeno