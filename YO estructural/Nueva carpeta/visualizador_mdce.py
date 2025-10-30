import matplotlib.pyplot as plt
import networkx as nx
from datetime import datetime
import json

class VisualizadorMDCE:
    def __init__(self, sistema_yo):
        self.sistema = sistema_yo
        self.historial_metricas = []
        
    def actualizar_metricas(self):
        """Actualiza el historial de métricas"""
        self.historial_metricas.append({
            "timestamp": datetime.now().isoformat(),
            "activacion": self.sistema.estado_actual.activacion,
            "tipo_yo": self.sistema.estado_actual.tipo.name,
            "contradicciones": len(self.sistema.historial_contradicciones),
            "contextos_activos": len(self.sistema.estado_actual.contextos_activos)
        })
    
    def visualizar_estado_actual(self):
        """Genera visualización del estado actual del sistema"""
        plt.figure(figsize=(15, 8))
        
        # 1. Gráfico de Activación
        plt.subplot(2, 2, 1)
        activaciones = [m["activacion"] for m in self.historial_metricas[-20:]]
        plt.plot(activaciones, marker='o')
        plt.title("Nivel de Activación")
        plt.ylim(0, 1)
        
        # 2. Evolución del YO
        plt.subplot(2, 2, 2)
        tipos_yo = [m["tipo_yo"] for m in self.historial_metricas[-20:]]
        plt.plot(range(len(tipos_yo)), [TipoYO[t].value for t in tipos_yo], marker='s')
        plt.title("Evolución del YO")
        plt.ylim(-1, 6)
        
        # 3. Contradicciones Detectadas
        plt.subplot(2, 2, 3)
        contradicciones = [m["contradicciones"] for m in self.historial_metricas[-20:]]
        plt.bar(range(len(contradicciones)), contradicciones)
        plt.title("Contradicciones Acumuladas")
        
        # 4. Contextos Activos
        plt.subplot(2, 2, 4)
        contextos = [m["contextos_activos"] for m in self.historial_metricas[-20:]]
        plt.plot(contextos, marker='v')
        plt.title("Contextos Activos")
        
        plt.tight_layout()
        plt.savefig(f"logs_sistema/estado_mdce_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        plt.close()