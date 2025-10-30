import os
import re
import yaml
from typing import List, Dict, Tuple
from dataclasses import dataclass
import datetime

@dataclass
class PatronDetectado:
    tipo: str
    contenido: str
    nivel_jerarquico: int
    confianza: float
    posicion: Tuple[int, int]  # línea inicio, línea fin

class ProcesadorFenomenologico:
    """Analizador automático de textos fenomenológicos"""
    
    def __init__(self):
        self.patrones_nivel = {
            -4: [r'\b(?:dato|crudo|sin\s+contexto|aparición)\b'],
            -3: [r'\b(?:temperatura|rugosidad|vibración|textura)\b'],
            -2: [r'\b(?:similar|diferente|gradiente|relación)\b'],
            -1: [r'\b(?:grupo|conjunto|patrón|coexisten)\b'],
            0: [r'\b(?:lluvia|viento|dolor|fenómeno)\b'],
            1: [r'\b(?:contexto|situación|YO|testigo)\b'],
            2: [r'\b(?:macrocontexto|patrón\s+general)\b']
        }
        
        self.patrones_yo = {
            'proto_yo': [r'\b(?:reactividad|sin\s+conciencia)\b'],
            'yo_sensorial': [r'\b(?:registro|estímulo|percibo)\b'],
            'yo_afectivo': [r'\b(?:siento|emoción|afecto)\b'],
            'yo_reflexivo': [r'\b(?:observo|reflexiono|pienso)\b'],
            'yo_simbolico': [r'\b(?:símbolo|significado|estructura)\b'],
            'yo_narrativo': [r'\b(?:relato|historia|continuidad)\b']
        }
    
    def procesar_archivo(self, ruta_archivo: str) -> Dict:
        """Procesa un archivo de texto y detecta estructuras fenomenológicas"""
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            lineas = contenido.split('\n')
        
        patrones_detectados = []
        apariciones_yo = []
        
        # Detectar patrones por nivel
        for nivel, patrones in self.patrones_nivel.items():
            for patron in patrones:
                matches = list(re.finditer(patron, contenido, re.IGNORECASE))
                for match in matches:
                    linea_num = contenido[:match.start()].count('\n') + 1
                    patrones_detectados.append(PatronDetectado(
                        tipo=f"nivel_{nivel}",
                        contenido=match.group(),
                        nivel_jerarquico=nivel,
                        confianza=0.8,
                        posicion=(linea_num, linea_num)
                    ))
        
        # Detectar apariciones del YO
        for tipo_yo, patrones in self.patrones_yo.items():
            for patron in patrones:
                matches = list(re.finditer(patron, contenido, re.IGNORECASE))
                for match in matches:
                    linea_num = contenido[:match.start()].count('\n') + 1
                    apariciones_yo.append({
                        "tipo": tipo_yo,
                        "contenido": match.group(),
                        "linea": linea_num,
                        "confianza": 0.7
                    })
        
        # Generar clasificación estructurada
        clasificacion = self._generar_clasificacion(patrones_detectados, apariciones_yo)
        
        return {
            "archivo_origen": ruta_archivo,
            "timestamp_procesamiento": datetime.datetime.now().isoformat(),
            "patrones_detectados": [p.__dict__ for p in patrones_detectados],
            "apariciones_yo": apariciones_yo,
            "clasificacion_estructurada": clasificacion,
            "metricas": self._calcular_metricas(patrones_detectados, apariciones_yo)
        }
    
    def _generar_clasificacion(self, patrones: List[PatronDetectado], apariciones_yo: List[Dict]) -> Dict:
        """Genera clasificación jerárquica estructurada"""
        clasificacion = {
            "niveles_detectados": {},
            "emergencia_yo": {},
            "coherencia_narrativa": 0.0
        }
        
        # Agrupar por niveles
        for patron in patrones:
            nivel = patron.nivel_jerarquico
            if nivel not in clasificacion["niveles_detectados"]:
                clasificacion["niveles_detectados"][nivel] = []
            clasificacion["niveles_detectados"][nivel].append(patron.contenido)
        
        # Analizar emergencia del YO
        tipos_yo_detectados = set(ap["tipo"] for ap in apariciones_yo)
        clasificacion["emergencia_yo"] = {
            "tipos_detectados": list(tipos_yo_detectados),
            "nivel_maximo": self._determinar_nivel_yo_maximo(tipos_yo_detectados),
            "coherencia_yo": len(tipos_yo_detectados) / 6.0  # 6 tipos posibles
        }
        
        # Calcular coherencia narrativa
        clasificacion["coherencia_narrativa"] = self._calcular_coherencia_narrativa(patrones)
        
        return clasificacion
    
    def _determinar_nivel_yo_maximo(self, tipos_detectados: set) -> int:
        """Determina el nivel máximo del YO detectado"""
        jerarquia_yo = {
            'proto_yo': 0,
            'yo_sensorial': 1,
            'yo_afectivo': 2,
            'yo_reflexivo': 3,
            'yo_simbolico': 4,
            'yo_narrativo': 5
        }
        
        if not tipos_detectados:
            return 0
        
        return max(jerarquia_yo.get(tipo, 0) for tipo in tipos_detectados)
    
    def procesar_directorio(self, ruta_directorio: str, ruta_salida: str) -> Dict:
        """Procesa todos los archivos .txt de un directorio"""
        resultados = []
        
        for archivo in os.listdir(ruta_directorio):
            if archivo.endswith('.txt'):
                ruta_completa = os.path.join(ruta_directorio, archivo)
                resultado = self.procesar_archivo(ruta_completa)
                resultados.append(resultado)
        
        # Crear el diccionario de resultados
        analisis_completo = {
            "timestamp": datetime.datetime.now().isoformat(),
            "archivos_procesados": len(resultados),
            "resultados": resultados
        }
        
        # Guardar resultados consolidados
        ruta_resultado = os.path.join(ruta_salida, 'analisis_fenomenologico.yaml')
        with open(ruta_resultado, 'w', encoding='utf-8') as f:
            yaml.dump(analisis_completo, f, default_flow_style=False, allow_unicode=True)
        
        return analisis_completo
    
    def _calcular_coherencia_narrativa(self, patrones: List[PatronDetectado]) -> float:
        """Calcula la coherencia narrativa basada en los patrones detectados"""
        if not patrones:
            return 0.0
            
        # Ordenar patrones por posición
        patrones_ordenados = sorted(patrones, key=lambda p: p.posicion[0])
        
        # Calcular coherencia basada en la progresión de niveles
        coherencia = 0.0
        niveles_consecutivos = 0
        ultimo_nivel = None
        
        for patron in patrones_ordenados:
            if ultimo_nivel is not None:
                # Premiar progresión gradual de niveles
                if abs(patron.nivel_jerarquico - ultimo_nivel) <= 1:
                    niveles_consecutivos += 1
            ultimo_nivel = patron.nivel_jerarquico
        
        if len(patrones) > 1:
            coherencia = niveles_consecutivos / (len(patrones) - 1)
        
        return min(1.0, coherencia)
    
    def _calcular_metricas(self, patrones: List[PatronDetectado], apariciones_yo: List[Dict]) -> Dict:
        """Calcula métricas del análisis fenomenológico"""
        if not patrones:
            return {
                "densidad_patrones": 0.0,
                "diversidad_niveles": 0.0,
                "presencia_yo": 0.0
            }
        
        # Calcular densidad de patrones
        densidad = len(patrones) / max(p.posicion[1] for p in patrones)
        
        # Calcular diversidad de niveles
        niveles_unicos = len(set(p.nivel_jerarquico for p in patrones))
        diversidad = niveles_unicos / len(self.patrones_nivel)
        
        # Calcular presencia del YO
        presencia_yo = len(apariciones_yo) / len(patrones) if patrones else 0.0
        
        return {
            "densidad_patrones": min(1.0, densidad),
            "diversidad_niveles": min(1.0, diversidad),
            "presencia_yo": min(1.0, presencia_yo)
        }