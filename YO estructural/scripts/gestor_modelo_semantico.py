import os
import yaml
import datetime
from modelos.fenomeno import Fenomeno
from modelos.contexto import Contexto
from modelos.macrocontexto import Macrocontexto
from modelos.red_contextos import RedContextos
from modelos.ontosistema import Ontosistema
from modelos.metacampo import Metacampo

def cargar_config():
    ruta = os.path.join(os.path.dirname(__file__), '..', 'configuracion', 'config.yaml')
    with open(ruta, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

class GestorModeloSemantico:
    """Gestor principal del modelo semántico"""
    
    def __init__(self, config=None):
        self.config = config or cargar_config()
        self.inicializar_config_modelo()
        self.ontosistema = Ontosistema(self.config)
        self.crear_directorios()
    
    def inicializar_config_modelo(self):
        """Inicializa la configuración del modelo semántico si no existe"""
        if 'modelo_semantico' not in self.config:
            self.config['modelo_semantico'] = {
                'rutas': {
                    'fenomenos': 'procesado/nodos_fenomenologicos/v1/fenomenos',
                    'contextos': 'procesado/nodos_fenomenologicos/v1/contextos',
                    'macrocontextos': 'procesado/nodos_fenomenologicos/v1/macrocontextos',
                    'redes': 'procesado/nodos_fenomenologicos/v1/redes',
                    'conceptos_emergentes': 'procesado/nodos_fenomenologicos/v1/conceptos',
                    'metacampos': 'procesado/nodos_fenomenologicos/v1/metacampos'
                },
                'umbrales': {
                    'agrupacion_contextos': 0.7,  # Similitud mínima para agrupar contextos
                    'emergencia_yo': 0.6,  # Umbral para considerar emergencia del YO
                    'creacion_concepto': 0.5  # Umbral para crear un nuevo concepto
                },
                'neo4j': {
                    'enabled': False,
                    'uri': 'bolt://localhost:7687',
                    'user': 'neo4j',
                    'password': 'password'
                }
            }
            # Guardar la configuración actualizada
            self.guardar_config()
    
    def guardar_config(self):
        """Guarda la configuración actualizada"""
        ruta = os.path.join(os.path.dirname(__file__), '..', 'configuracion', 'config.yaml')
        with open(ruta, 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, default_flow_style=False, allow_unicode=True)
    
    def crear_directorios(self):
        """Crea los directorios necesarios para el modelo semántico"""
        for tipo, ruta in self.config['modelo_semantico']['rutas'].items():
            ruta_completa = os.path.join(os.path.dirname(__file__), '..', ruta)
            os.makedirs(ruta_completa, exist_ok=True)
    
    def crear_fenomeno(self, contenido, tipo="general", propiedades=None):
        """Crea un nuevo fenómeno"""
        fenomeno = Fenomeno(contenido, tipo, propiedades)
        ruta_base = os.path.join(os.path.dirname(__file__), '..', 
                               self.config['modelo_semantico']['rutas']['fenomenos'])
        ruta_completa = os.path.join(ruta_base, f"fenomeno_{fenomeno.id}.yaml")
        
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            yaml.dump(fenomeno.to_dict(), f, default_flow_style=False, allow_unicode=True)
        
        return fenomeno
    
    def crear_contexto(self, descripcion="", fenomenos=None, flujos=None, yo_presente=False, proyeccion=""):
        """Crea un nuevo contexto"""
        contexto = Contexto(descripcion)
        
        # Agregar fenómenos
        if fenomenos:
            for f in fenomenos:
                contexto.agregar_fenomeno(f)
        
        # Agregar flujos
        if flujos:
            for flujo in flujos:
                contexto.agregar_flujo(flujo)
        
        # Configurar YO y proyección
        if yo_presente:
            contexto.activar_yo()
        
        if proyeccion:
            contexto.establecer_proyeccion(proyeccion)
        
        # Guardar contexto
        ruta_base = os.path.join(os.path.dirname(__file__), '..', 
                               self.config['modelo_semantico']['rutas']['contextos'])
        contexto.guardar(ruta_base)
        
        return contexto
    
    def crear_macrocontexto(self, nombre, descripcion, contextos_ids, patron="", reflexion=""):
        """Crea un nuevo macrocontexto"""
        macrocontexto = Macrocontexto(nombre, descripcion)
        
        # Agregar contextos
        for ctx_id in contextos_ids:
            macrocontexto.agregar_contexto(ctx_id)
        
        # Establecer patrón y reflexión
        if patron:
            macrocontexto.establecer_patron(patron)
        
        if reflexion:
            macrocontexto.establecer_reflexion(reflexion)
        
        # Guardar macrocontexto
        ruta_base = os.path.join(os.path.dirname(__file__), '..', 
                               self.config['modelo_semantico']['rutas']['macrocontextos'])
        macrocontexto.guardar(ruta_base)
        
        return macrocontexto
    
    def actualizar_estadisticas(self):
        """Actualiza las estadísticas del ontosistema"""
        self.ontosistema.actualizar_estadisticas()
        ruta_logs = os.path.join(os.path.dirname(__file__), '..', 'logs_sistema')
        self.ontosistema.guardar_estadisticas(ruta_logs)
        return self.ontosistema.estadisticas

if __name__ == "__main__":
    # Ejemplo de uso
    gestor = GestorModeloSemantico()
    gestor.crear_directorios()
    
    # Crear algunos fenómenos de ejemplo
    fenomeno1 = gestor.crear_fenomeno("Sensación de extrañeza al caminar por la calle", "emocional")
    fenomeno2 = gestor.crear_fenomeno("Ruido de tráfico", "sensorial")
    fenomeno3 = gestor.crear_fenomeno("Edificio alto a la derecha", "visual")
    
    # Crear un contexto con esos fenómenos
    contexto = gestor.crear_contexto(
        descripcion="Caminando por el centro de la ciudad",
        fenomenos=[fenomeno1, fenomeno2, fenomeno3],
        flujos=["Movimiento hacia adelante", "Desvío a la izquierda"],
        yo_presente=True,
        proyeccion="Posible llegada a la plaza central"
    )
    
    # Actualizar estadísticas
    stats = gestor.actualizar_estadisticas()
    print("Estadísticas actualizadas:")
    for k, v in stats.items():
        print(f"  - {k}: {v}")