from dotenv import load_dotenv
import os
import yaml
from pathlib import Path
from motor_yo.sistema_yo_emergente import SistemaYoEmergente
from analizador_textos.procesador_fenomenologico import ProcesadorFenomenologico
from gradient_system_enhanced import VohexGradientSystem
from niveles.preinstancia import PreInstancia
from niveles.instancia_existencia import InstanciaExistencia
from niveles.vohexistencia import Vohexistencia
import logging
from datetime import datetime
from typing import Dict
from database import Neo4jConnection

class SistemaFenomenologicoV2:
    """Sistema principal integrado v2.2"""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = self._cargar_config(config_path)  # <-- Primero cargar config
        self.modo_diagnostico = self.config.get("modo_diagnostico", False)
        self.procesador_textos = ProcesadorFenomenologico()
        self.sistema_gradientes = VohexGradientSystem()
        self.metricas = {
            "diversidad_contextual": 0.0,
            "profundidad_narrativa": 0,
            "coherencia_temporal": 0.0,
            "emergencia_yo_narrativo": False
        }
        
        # Inicializar conexión Neo4j y componentes que la necesitan
        self._configurar_credenciales()
        self._configurar_logging()
        self.motor_yo.registrar_callback("mdce", self._manejar_evento_mdce)
    
    def _configurar_logging(self):
        """Configura sistema de logging estructurado"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"logs_sistema/sistema_principal_{timestamp}.log"
        
        logging.basicConfig(
            level=logging.DEBUG if self.config.get("modo_diagnostico") else logging.INFO,
            format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger("SistemaFenomenologico")
        self.logger.info("Sistema inicializado con configuración cargada")
    
    def _configurar_logging_detallado(self):
        """Configura logging detallado para modo diagnóstico"""
        import logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s',
            handlers=[
                logging.FileHandler('logs_sistema/diagnostico_detallado.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def _debug_print(self, mensaje: str, nivel: str = "INFO"):
        """Imprime mensajes de diagnóstico si está activado"""
        if self.modo_diagnostico:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] [DIAGNÓSTICO-{nivel}] {mensaje}")
            
            if hasattr(self, 'logger'):
                getattr(self.logger, nivel.lower())(mensaje)
    
    def _configurar_credenciales(self):
        """Configura credenciales desde variables de entorno"""
        if "neo4j" in self.config:
            self.config["neo4j"].update({
                "uri": os.getenv("NEO4J_URI", self.config["neo4j"].get("uri")),
                "user": os.getenv("NEO4J_USER", self.config["neo4j"].get("user")),
                "password": os.getenv("NEO4J_PASSWORD", self.config["neo4j"].get("password"))
            })
        
        # Inicializar conexión Neo4j con parámetros avanzados
        neo4j_config = self.config["neo4j"]
        self.neo4j = Neo4jConnection(
            f"bolt://{neo4j_config['host']}:{neo4j_config['port']}",
            neo4j_config["username"],
            neo4j_config["password"],
            database=neo4j_config.get("database"),
            timeout=neo4j_config.get("timeout", 30),
            max_retry=neo4j_config.get("max_retry", 3),
            pool_size=neo4j_config.get("pool_size", 50)
        )
        
        # Inicializar el motor YO con la conexión Neo4j
        self.motor_yo = SistemaYoEmergente(self.config_path, self.neo4j._driver)
    
    def _configurar_logging_detallado(self):
        """Configura logging detallado para modo diagnóstico"""
        import logging
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s',
            handlers=[
                logging.FileHandler('logs_sistema/diagnostico_detallado.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def _debug_print(self, mensaje: str, nivel: str = "INFO"):
        """Imprime mensajes de diagnóstico si está activado"""
        if self.modo_diagnostico:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"[{timestamp}] [DIAGNÓSTICO-{nivel}] {mensaje}")
            
            if hasattr(self, 'logger'):
                getattr(self.logger, nivel.lower())(mensaje)
    
    def _manejar_evento_mdce(self, evento: Dict):
        """Maneja eventos del MDCE"""
        if self.config.get("modo_diagnostico"):
            self.logger.debug(f"Evento MDCE recibido: {evento['tipo']}")
        
        if evento["tipo"] == "reconfiguracion_completada":
            self.logger.info(
                f"Reconfiguración exitosa - Nueva coherencia: "
                f"{evento['datos']['coherencia_nueva']:.2f}"
            )
            self._actualizar_metricas_post_reconfiguracion(evento["datos"])
        
        elif evento["tipo"] == "error_reconfiguracion":
            self.logger.warning(
                f"Error en reconfiguración: {evento['datos']['error']}"
            )
    
    def procesar_flujo_completo(self, ruta_datos_entrada: str) -> Dict:
        """Ejecuta el flujo completo del sistema con diagnóstico"""
        self._debug_print("Iniciando flujo completo del sistema")
        
        print("🚀 Iniciando Sistema Fenomenológico v2.2")
        
        # 1. Procesar textos automáticamente
        print("📖 Procesando textos fenomenológicos...")
        # Asegurarse de que ruta_datos_entrada esté definido
        ruta_entrada = ruta_datos_entrada  # Crear una variable local para evitar problemas
        analisis_textos = self.procesador_textos.procesar_directorio(
            ruta_entrada, 
            self.config['rutas']['logs']
        )
        
        # 2. Generar preinstancias
        print("🔸 Generando preinstancias...")
        preinstancias = self._generar_preinstancias_desde_analisis(analisis_textos)
        self._debug_print(f"Generadas {len(preinstancias)} preinstancias")
        
        # 3. Crear instancias de existencia
        print("🔹 Creando instancias de existencia...")
        instancias = self._crear_instancias_desde_preinstancias(preinstancias)
        self.instancias = instancias  # Guardar las instancias como atributo de la clase
        self._debug_print(f"Creadas {len(instancias)} instancias de existencia")
        
        # 4. Activar MDCE si hay contradicciones
        self._debug_print("Evaluando necesidad de activación MDCE")
        if self._detectar_contradicciones_nivel_4(instancias):
            self._debug_print("[MDCE] Contradicciones de 4º orden detectadas", "WARNING")
            resultado_mdce = self._activar_ciclo_mdce(instancias)
            self._debug_print(f"[MDCE] Resultado del ciclo: {resultado_mdce}")
        
        # 4. Calcular gradientes relacionales
        print("📊 Calculando gradientes relacionales...")
        self._calcular_gradientes_instancias(instancias)
        
        # 5. Detectar vohexistencias
        print("🔗 Detectando vohexistencias...")
        vohexistencias = self._detectar_vohexistencias(instancias)
        self.vohexistencias = vohexistencias  # Guardar las vohexistencias como atributo de la clase
        
        # 6. Evaluar emergencia del YO
        print("🧠 Evaluando emergencia del YO...")
        contextos_activos = self._extraer_contextos_activos()
        fenomenos_activos = self._extraer_fenomenos_activos()
        
        emergencia_detectada = self.motor_yo.evaluar_emergencia(contextos_activos, fenomenos_activos)
        
        # 7. Calcular métricas finales
        print("📈 Calculando métricas de éxito...")
        self._calcular_metricas_finales()
        
        # 8. Generar exportación Neo4j
        print("🗄️ Generando exportación Neo4j...")
        self._generar_exportacion_neo4j()
        
        resultado = {
            "estado_yo": self.motor_yo.estado_actual.__dict__,
            "metricas": self.metricas,
            "vohexistencias_detectadas": len(vohexistencias),
            "instancias_procesadas": len(instancias),
            "emergencia_detectada": emergencia_detectada,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        print(f"✅ Sistema completado. YO emergente: {self.motor_yo.estado_actual.tipo.name}")
        return resultado
    
    def _calcular_metricas_finales(self):
        """Calcula las métricas de éxito del sistema"""
        # Diversidad contextual
        contextos = self._contar_archivos_yaml('contextos')
        macrocontextos = self._contar_archivos_yaml('macrocontextos')
        self.metricas["diversidad_contextual"] = min(1.0, (contextos + macrocontextos) / 20.0)
        
        # Profundidad narrativa
        self.metricas["profundidad_narrativa"] = self.motor_yo.estado_actual.tipo.value
        
        # Coherencia temporal
        self.metricas["coherencia_temporal"] = self.motor_yo.estado_actual.activacion
        
        # Emergencia YO Narrativo
        self.metricas["emergencia_yo_narrativo"] = (
            self.motor_yo.estado_actual.tipo.value >= 5
        )
        
        print(f"📊 Métricas calculadas: {self.metricas}")
        
        # Evaluar contradicciones de 4° orden
        self.logger.info("Evaluando contradicciones de 4° orden...")
        estado_actual = self._preparar_estado_evaluacion()
        
        resultado_contradicciones = self.motor_yo.evaluar_contradicciones(estado_actual)
        
        if resultado_contradicciones["requiere_reconfig"]:
            self.logger.warning("Iniciando reconfiguración estructural")
            resultado_reconfig = self.motor_yo.activar_reconfiguracion(resultado_contradicciones)
            
            if resultado_reconfig.get("exito", False):
                self.logger.info("Reconfiguración completada exitosamente")
            else:
                self.logger.error("Falló la reconfiguración estructural")
                self._registrar_pendientes_reanalisis(resultado_contradicciones)
    
    def _preparar_estado_evaluacion(self) -> dict:
        """Prepara el estado actual del sistema para evaluación de contradicciones.
        
        Returns:
            dict: Estado del sistema con métricas relevantes para evaluación
        """
        return {
            'nivel_yo': self.motor_yo.estado_actual.tipo.value if hasattr(self.motor_yo.estado_actual, 'tipo') else 0,
            'coherencia_interna': self.motor_yo.estado_actual.activacion if hasattr(self.motor_yo.estado_actual, 'activacion') else 0.0,
            'contextos_activos': self.motor_yo.estado_actual.contextos_activos if hasattr(self.motor_yo.estado_actual, 'contextos_activos') else [],
            'reflexiones': self.motor_yo.estado_actual.reflexiones if hasattr(self.motor_yo.estado_actual, 'reflexiones') else [],
            'timestamp': self.motor_yo.estado_actual.timestamp if hasattr(self.motor_yo.estado_actual, 'timestamp') else '',
            'version': self.motor_yo.estado_actual.version if hasattr(self.motor_yo.estado_actual, 'version') else 0
        }
    
    def _registrar_pendientes_reanalisis(self, contradicciones: dict):
        """Registra contradicciones pendientes de reanálisis.
        
        Args:
            contradicciones: Diccionario con información de contradicciones detectadas
        """
        self.logger.warning(f"Contradicciones pendientes de reanálisis: {contradicciones.get('tensiones', {})}")
        # TODO: Implementar sistema de seguimiento de contradicciones pendientes
        # Podría guardar en archivo, base de datos o cola de procesamiento
    
    def _contar_archivos_yaml(self, subcarpeta: str) -> int:
        """Cuenta los archivos YAML en una subcarpeta específica del modelo semántico"""
        try:
            ruta_base = self.config.get('modelo_semantico', {}).get('rutas', {}).get(subcarpeta, '')
            if not ruta_base:
                return 0
            
            ruta_completa = Path(ruta_base)
            if not ruta_completa.exists():
                return 0
            
            # Contar archivos .yaml y .yml
            return len(list(ruta_completa.glob('*.yaml'))) + len(list(ruta_completa.glob('*.yml')))
        except Exception as e:
            self.logger.warning(f"Error al contar archivos YAML en {subcarpeta}: {e}")
            return 0
    
    def _cargar_config(self, config_path: str) -> dict:
        """Carga la configuración desde un archivo YAML."""
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def __del__(self):
        """Cleanup connections"""
        if hasattr(self, 'neo4j'):
            self.neo4j.close()
    
    def persistir_instancia(self, instancia):
        """Persiste una instancia en Neo4j"""
        query = """
        MERGE (i:InstanciaExistencia {id: $id})
        SET i.tipo = $tipo,
            i.valor = $valor,
            i.timestamp = $timestamp
        """
        self.neo4j.query(query, {
            "id": instancia.id,
            "tipo": instancia.tipo,
            "valor": instancia.valor,
            "timestamp": datetime.now().isoformat()
        })
    
    def persistir_vohexistencia(self, vohex):
        """Persiste una vohexistencia y sus relaciones"""
        query = """
        MERGE (v:Vohexistencia {id: $id})
        SET v.peso = $peso,
            v.coherencia = $coherencia,
            v.timestamp = $timestamp
        """
        self.neo4j.query(query, {
            "id": vohex.id,
            "peso": vohex.peso,
            "coherencia": vohex.coherencia,
            "timestamp": datetime.now().isoformat()
        })

    def _generar_preinstancias_desde_analisis(self, analisis_textos: Dict) -> List[PreInstancia]:
        """Genera preinstancias a partir del análisis de textos fenomenológicos"""
        preinstancias = []
        
        for resultado in analisis_textos['resultados']:
            # Extraer patrones detectados y clasificación
            patrones = resultado['patrones_detectados']
            clasificacion = resultado['clasificacion_estructurada']
            
            # Crear preinstancia para cada patrón significativo
            for patron in patrones:
                # Crear el dato crudo como un diccionario con toda la información
                dato_crudo = {
                    'nivel_jerarquico': patron['nivel_jerarquico'],
                    'contenido': patron['contenido'],
                    'confianza': patron['confianza'],
                    'clasificacion': clasificacion
                }
                
                # Crear preinstancia con el dato crudo estructurado
                preinstancia = PreInstancia(
                    dato_crudo=dato_crudo,
                    origen=resultado.get('archivo_origen', 'analisis_fenomenologico')
                )
                preinstancias.append(preinstancia)
        
        self._debug_print(f"Generadas {len(preinstancias)} preinstancias desde análisis")
        return preinstancias

    def _crear_instancias_desde_preinstancias(self, preinstancias: List[PreInstancia]) -> List[InstanciaExistencia]:
        """Crea instancias de existencia a partir de preinstancias"""
        instancias = []
        
        for preinstancia in preinstancias:
            # Extraer datos estructurados de la preinstancia
            datos_crudos = preinstancia.dato_crudo
            
            # Crear propiedades para la instancia
            propiedades = {
                'nivel_jerarquico': datos_crudos['nivel_jerarquico'],
                'contenido': datos_crudos['contenido'],
                'confianza': datos_crudos['confianza'],
                'clasificacion': datos_crudos['clasificacion']
            }
            
            # Crear nueva instancia de existencia
            instancia = InstanciaExistencia(
                propiedades=propiedades,
                proto_origen=preinstancia.origen
            )
            
            instancias.append(instancia)
        
        self._debug_print(f"Creadas {len(instancias)} instancias de existencia")
        return instancias

    def _detectar_contradicciones_nivel_4(self, instancias: List[InstanciaExistencia]) -> bool:
        """Detecta contradicciones de 4º orden entre instancias de existencia"""
        self._debug_print("Analizando contradicciones de 4º orden")
        
        # Verificar si hay suficientes instancias para análisis
        if len(instancias) < 2:
            return False
            
        # Analizar contradicciones estructurales
        contradicciones = []
        
        for i, inst1 in enumerate(instancias):
            for inst2 in instancias[i+1:]:
                # Verificar contradicciones temporales
                if self._hay_contradiccion_temporal(inst1, inst2):
                    contradicciones.append({
                        'tipo': 'temporal',
                        'instancias': [inst1.id, inst2.id]
                    })
                    
                # Verificar contradicciones de coherencia
                if self._hay_contradiccion_coherencia(inst1, inst2):
                    contradicciones.append({
                        'tipo': 'coherencia',
                        'instancias': [inst1.id, inst2.id]
                    })
        
        # Registrar contradicciones encontradas
        if contradicciones:
            self._debug_print(
                f"Detectadas {len(contradicciones)} contradicciones de 4º orden",
                "WARNING"
            )
            return True
            
        self._debug_print("No se detectaron contradicciones de 4º orden")
        return False
    
    def _hay_contradiccion_temporal(self, inst1: InstanciaExistencia, inst2: InstanciaExistencia) -> bool:
        """Verifica si hay contradicción temporal entre dos instancias"""
        # Contradicción si tienen el mismo nivel jerárquico pero timestamps incompatibles
        if inst1.propiedades.get('nivel_jerarquico') == inst2.propiedades.get('nivel_jerarquico'):
            t1 = datetime.fromisoformat(inst1.timestamp)
            t2 = datetime.fromisoformat(inst2.timestamp)
            return abs((t2 - t1).total_seconds()) > 3600  # Más de 1 hora de diferencia
        return False
    
    def _hay_contradiccion_coherencia(self, inst1: InstanciaExistencia, inst2: InstanciaExistencia) -> bool:
        """Verifica si hay contradicción de coherencia entre dos instancias"""
        # Contradicción si tienen alta confianza pero clasificaciones incompatibles
        if (inst1.propiedades.get('confianza', 0) > 0.8 and 
            inst2.propiedades.get('confianza', 0) > 0.8):
            return inst1.propiedades.get('clasificacion') != inst2.propiedades.get('clasificacion')
        return False
    
    def _son_contradictorias(self, props1: Dict, props2: Dict) -> bool:
        """Evalúa si dos conjuntos de propiedades son contradictorios"""
        # Verificar contradicciones en nivel jerárquico
        if props1.get('nivel_jerarquico') == props2.get('nivel_jerarquico'):
            # Verificar contradicciones en clasificación
            if props1.get('clasificacion') != props2.get('clasificacion'):
                # Si tienen el mismo nivel pero clasificación diferente,
                # verificar si la confianza es alta en ambos casos
                return (props1.get('confianza', 0) > 0.8 and 
                        props2.get('confianza', 0) > 0.8)

    def _calcular_gradientes_instancias(self, instancias: list[InstanciaExistencia]) -> None:
        """Calcula los gradientes relacionales entre instancias de existencia"""
        if not instancias:
            self._debug_print("No hay instancias para calcular gradientes", "WARNING")
            return
            
        self._debug_print(f"Calculando gradientes para {len(instancias)} instancias")
        
        # Procesar cada instancia con el sistema de gradientes
        for instancia in instancias:
            gradientes = self.sistema_gradientes.calcular_gradientes(
                instancia.propiedades,
                instancia.timestamp
            )
            
            # Actualizar propiedades de la instancia con los gradientes
            instancia.propiedades.update({
                'gradiente_temporal': gradientes.get('temporal', 0.0),
                'gradiente_coherencia': gradientes.get('coherencia', 0.0),
                'gradiente_estructural': gradientes.get('estructural', 0.0)
            })
        
        self._debug_print("Gradientes relacionales calculados exitosamente")

    def _detectar_vohexistencias(self, instancias: List[InstanciaExistencia]) -> List[Vohexistencia]:
        """Detecta y crea vohexistencias a partir de instancias relacionadas"""
        self._debug_print(f"Iniciando detección de vohexistencias para {len(instancias)} instancias")
        vohexistencias = []
        instancias_procesadas = set()

        for instancia in instancias:
            if instancia.id in instancias_procesadas:
                continue

            # Obtener gradientes relacionales para la instancia actual
            gradientes = self.sistema_gradientes.get_all_gradients_for_node(instancia.id)
            instancias_relacionadas = []

            # Identificar instancias altamente relacionadas
            for otra_instancia in instancias:
                if otra_instancia.id == instancia.id:
                    continue
                    
                # Buscar en los gradientes la relación con la otra instancia
                for gradiente in gradientes["gradientes"]:
                    if gradiente["nodo_destino"] == otra_instancia.id:
                        if gradiente["valor_gradiente"] > self.config.get("umbral_vohexistencia", 0.7):
                            instancias_relacionadas.append(otra_instancia)
                            break

            # Si hay suficientes instancias relacionadas, crear una vohexistencia
            if len(instancias_relacionadas) >= self.config.get("min_instancias_vohex", 2):
                nueva_vohex = Vohexistencia(
                    nombre=f"Vohex_{instancia.id[:6]}",
                    descripcion=f"Vohexistencia generada desde {instancia.id}"
                )
                
                # Agregar instancias a la vohexistencia
                nueva_vohex.agregar_instancia(instancia.id)
                for inst_rel in instancias_relacionadas:
                    nueva_vohex.agregar_instancia(inst_rel.id)
                
                # Establecer constante emergente basada en propiedades comunes
                propiedades_comunes = self._identificar_propiedades_comunes(
                    [instancia] + instancias_relacionadas
                )
                nueva_vohex.establecer_constante_emergente(
                    f"Patrón: {', '.join(propiedades_comunes)}"
                )
                
                vohexistencias.append(nueva_vohex)
                
                # Marcar todas las instancias como procesadas
                instancias_procesadas.add(instancia.id)
                for inst in instancias_relacionadas:
                    instancias_procesadas.add(inst.id)

        self._debug_print(f"Detectadas {len(vohexistencias)} vohexistencias")
        return vohexistencias
        
    def _identificar_propiedades_comunes(self, instancias: List[InstanciaExistencia]) -> List[str]:
        """Identifica propiedades comunes entre un grupo de instancias"""
        if not instancias:
            return []
            
        # Obtener todas las propiedades de la primera instancia
        propiedades_comunes = set(instancias[0].propiedades.keys())
        
        # Intersectar con las propiedades de las demás instancias
        for instancia in instancias[1:]:
            propiedades_comunes.intersection_update(instancia.propiedades.keys())
            
            # Si ya no hay propiedades comunes, terminar
            if not propiedades_comunes:
                break
                
        return list(propiedades_comunes)

    def _extraer_contextos_activos(self):
        """Extrae los contextos activos del sistema actual para evaluación de emergencia.
        
        Returns:
            list: Lista de contextos activos con sus propiedades relevantes
        """
        contextos = []
        
        # Función auxiliar para convertir claves numéricas a strings en diccionarios anidados
        def convertir_claves_a_strings(obj):
            if isinstance(obj, dict):
                return {str(k): convertir_claves_a_strings(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convertir_claves_a_strings(item) for item in obj]
            else:
                return obj
        
        # Extraer contextos de instancias activas
        for instancia in self.instancias:
            # Convertir claves numéricas a strings en propiedades
            propiedades_convertidas = convertir_claves_a_strings(instancia.propiedades)
            gradientes_convertidos = convertir_claves_a_strings(instancia.gradientes if hasattr(instancia, 'gradientes') else {})
            
            contexto = {
                'id': instancia.id,
                'tipo': 'instancia',
                'propiedades': propiedades_convertidas,
                'gradientes': gradientes_convertidos,
                'timestamp': instancia.timestamp
            }
            contextos.append(contexto)
        
        # Extraer contextos de vohexistencias
        for vohex in self.vohexistencias:
            # Convertir claves numéricas a strings en propiedades
            propiedades_convertidas = convertir_claves_a_strings(vohex.propiedades)
            
            contexto = {
                'id': vohex.id,
                'tipo': 'vohexistencia',
                'propiedades': propiedades_convertidas,
                'constante_emergente': vohex.constante_emergente,
                'peso_coexistencial': vohex.peso_coexistencial,
                'timestamp': vohex.timestamp
            }
            contextos.append(contexto)
        
        # Ordenar contextos por timestamp para mantener coherencia temporal
        contextos.sort(key=lambda x: x['timestamp'])
        
        self.logger.debug(f"Extraídos {len(contextos)} contextos activos con claves convertidas a strings")
        return contextos
    
    def _extraer_fenomenos_activos(self):
        """Extrae los fenómenos activos del sistema actual para evaluación de emergencia.
        
        Returns:
            list: Lista de fenómenos activos con sus propiedades relevantes
        """
        fenomenos = []
        
        # Reutilizamos la función auxiliar definida en _extraer_contextos_activos
        def convertir_claves_a_strings(obj):
            if isinstance(obj, dict):
                return {str(k): convertir_claves_a_strings(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convertir_claves_a_strings(item) for item in obj]
            else:
                return obj
        
        # Si no hay fenómenos explícitos, podemos derivarlos de las instancias y vohexistencias
        # Extraer fenómenos de instancias activas
        for instancia in self.instancias:
            # Convertir claves numéricas a strings en propiedades
            propiedades_convertidas = convertir_claves_a_strings(instancia.propiedades)
            
            fenomeno = {
                'id': f"fenomeno_{instancia.id}",
                'tipo': 'derivado_instancia',
                'propiedades': propiedades_convertidas,
                'timestamp': instancia.timestamp
            }
            fenomenos.append(fenomeno)
        
        # Extraer fenómenos de vohexistencias (si existen)
        for vohex in self.vohexistencias:
            # Convertir claves numéricas a strings en propiedades
            propiedades_convertidas = convertir_claves_a_strings(vohex.propiedades)
            
            fenomeno = {
                'id': f"fenomeno_{vohex.id}",
                'tipo': 'derivado_vohexistencia',
                'propiedades': propiedades_convertidas,
                'constante_emergente': vohex.constante_emergente if hasattr(vohex, 'constante_emergente') else None,
                'timestamp': vohex.timestamp
            }
            fenomenos.append(fenomeno)
        
        # Ordenar fenómenos por timestamp para mantener coherencia temporal
        fenomenos.sort(key=lambda x: x['timestamp'])
        
        self.logger.debug(f"Extraídos {len(fenomenos)} fenómenos activos con claves convertidas a strings")
        return fenomenos