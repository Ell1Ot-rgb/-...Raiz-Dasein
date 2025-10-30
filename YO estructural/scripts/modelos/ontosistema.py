import os
import yaml
import datetime
import json

class Ontosistema:
    """Representa el sistema ontológico completo (base de datos total)"""
    
    def __init__(self, config):
        self.config = config
        self.rutas = config.get('modelo_semantico', {}).get('rutas', {})
        self.estadisticas = {
            "fenomenos": 0,
            "contextos": 0,
            "macrocontextos": 0,
            "redes": 0,
            "conceptos_emergentes": 0,
            "apariciones_yo": 0
        }
        self.ultima_actualizacion = datetime.datetime.now().isoformat()
    
    def actualizar_estadisticas(self):
        """Actualiza las estadísticas contando archivos en las rutas configuradas"""
        for tipo, ruta in self.rutas.items():
            ruta_completa = os.path.join(os.path.dirname(__file__), '../..', ruta)
            if os.path.exists(ruta_completa):
                # Contar archivos YAML en el directorio
                archivos = [f for f in os.listdir(ruta_completa) if f.endswith('.yaml')]
                self.estadisticas[tipo] = len(archivos)
        
        # Contar apariciones del YO
        self.contar_apariciones_yo()
        
        self.ultima_actualizacion = datetime.datetime.now().isoformat()
        return self.estadisticas
    
    def contar_apariciones_yo(self):
        """Cuenta las apariciones del YO en los contextos"""
        ruta_contextos = os.path.join(os.path.dirname(__file__), '../..', self.rutas.get('contextos', ''))
        if os.path.exists(ruta_contextos):
            contador = 0
            for archivo in os.listdir(ruta_contextos):
                if archivo.endswith('.yaml'):
                    try:
                        with open(os.path.join(ruta_contextos, archivo), 'r', encoding='utf-8') as f:
                            data = yaml.safe_load(f)
                            if data.get('yo_presente', False):
                                contador += 1
                    except Exception:
                        pass
            self.estadisticas["apariciones_yo"] = contador
    
    def guardar_estadisticas(self, ruta_logs):
        """Guarda las estadísticas en un archivo JSON"""
        ruta_completa = os.path.join(ruta_logs, 'metricas.json')
        datos = {
            "estadisticas": self.estadisticas,
            "timestamp": self.ultima_actualizacion
        }
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        return ruta_completa
    
    def cargar_estadisticas(self, ruta_logs):
        """Carga estadísticas desde un archivo JSON"""
        ruta_completa = os.path.join(ruta_logs, 'metricas.json')
        if os.path.exists(ruta_completa):
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                self.estadisticas = datos.get("estadisticas", self.estadisticas)
                self.ultima_actualizacion = datos.get("timestamp", self.ultima_actualizacion)
        return self.estadisticas