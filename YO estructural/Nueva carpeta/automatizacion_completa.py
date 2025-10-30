#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SISTEMA DE AUTOMATIZACIÓN COMPLETA YO ESTRUCTURAL
=================================================

Este script automatiza el flujo completo desde Google Drive hasta Neo4j:
1. Monitorea archivos en Google Drive
2. Procesa datos vectoriales y gradientes
3. Envía a n8n para procesamiento
4. Almacena en Supabase
5. Visualiza en Neo4j

Autor: Sistema YO Estructural
Versión: 3.0
"""

import os
import sys
import json
import time
import asyncio
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Agregar el directorio de integraciones al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'integraciones'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'analizador_textos'))

# Importar componentes del sistema
try:
    from n8n_config import N8nIntegrator
    from google_drive_connector import GoogleDriveConnector
    from supabase_connector import SupabaseConnector
    from procesador_fenomenologico import ProcesadorFenomenologico
except ImportError as e:
    print(f"Error importando módulos: {e}")
    sys.exit(1)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('logs_sistema/automatizacion_completa.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AutomatizacionCompletaYO:
    """Sistema de automatización completa para YO Estructural"""
    
    def __init__(self):
        """Inicializa todos los componentes del sistema"""
        logger.info("Inicializando Sistema de Automatización Completa YO Estructural")
        
        # Cargar variables de entorno
        self._cargar_variables_entorno()
        
        # Inicializar componentes
        self.n8n = None
        self.supabase = None
        self.google_drive = None
        self.procesador = None
        
        self._inicializar_componentes()
        
        # Estado del sistema
        self.estado_sistema = {
            "iniciado": datetime.now().isoformat(),
            "archivos_procesados": 0,
            "errores": 0,
            "ultimo_procesamiento": None
        }
    
    def _cargar_variables_entorno(self):
        """Carga y valida variables de entorno"""
        variables_requeridas = [
            'NEO4J_URI', 'NEO4J_USER', 'NEO4J_PASSWORD',
            'SUPABASE_URL', 'SUPABASE_KEY',
            'N8N_WEBHOOK_URL'
        ]
        
        variables_faltantes = []
        for var in variables_requeridas:
            if not os.getenv(var):
                variables_faltantes.append(var)
        
        if variables_faltantes:
            logger.error(f"Variables de entorno faltantes: {variables_faltantes}")
            raise ValueError(f"Variables requeridas no configuradas: {variables_faltantes}")
        
        logger.info("Variables de entorno cargadas correctamente")
    
    def _inicializar_componentes(self):
        """Inicializa todos los componentes del sistema"""
        
        # Inicializar N8N
        try:
            self.n8n = N8nIntegrator()
            logger.info("N8N integrator inicializado")
        except Exception as e:
            logger.error(f"Error inicializando N8N: {e}")
        
        # Inicializar Supabase
        try:
            self.supabase = SupabaseConnector()
            logger.info("Supabase connector inicializado")
        except Exception as e:
            logger.error(f"Error inicializando Supabase: {e}")
        
        # Inicializar Google Drive
        try:
            self.google_drive = GoogleDriveConnector()
            logger.info("Google Drive connector inicializado")
        except Exception as e:
            logger.error(f"Error inicializando Google Drive: {e}")
        
        # Inicializar Procesador Fenomenológico
        try:
            self.procesador = ProcesadorFenomenologico()
            logger.info("Procesador fenomenológico inicializado")
        except Exception as e:
            logger.error(f"Error inicializando procesador: {e}")
    
    async def procesar_archivo_completo(self, archivo_info: Dict[str, Any]) -> Dict[str, Any]:
        """Procesa un archivo completamente desde Drive hasta Neo4j"""
        try:
            logger.info(f"Iniciando procesamiento completo de: {archivo_info.get('name', 'archivo')}")
            
            resultado = {
                "archivo": archivo_info.get('name'),
                "id_archivo": archivo_info.get('id'),
                "timestamp": datetime.now().isoformat(),
                "pasos_completados": [],
                "errores": [],
                "datos_procesados": None
            }
            
            # PASO 1: Procesar datos con el procesador fenomenológico
            if self.procesador:
                try:
                    # Obtener contenido del archivo
                    contenido = self.google_drive.descargar_archivo_como_bytes(archivo_info['id'])
                    
                    # Procesar según el tipo de archivo
                    if archivo_info.get('mimeType', '').startswith('text/'):
                        texto = contenido.decode('utf-8')
                        contexto = await self.procesador.procesar_entrada_bruta(texto)
                        resultado["datos_procesados"] = contexto
                        resultado["pasos_completados"].append("procesamiento_fenomenologico")
                    else:
                        # Para archivos no texto, crear estructura básica
                        datos_basicos = {
                            "id_unico": archivo_info['id'],
                            "timestamp_sistema": datetime.now().isoformat(),
                            "origen": {
                                "tipo_archivo": self._detectar_tipo_archivo(archivo_info),
                                "nombre_archivo": archivo_info['name'],
                                "fuente": "Google Drive",
                                "tamaño_bytes": archivo_info.get('size', 0)
                            },
                            "propiedades": {
                                "descripcion": f"Archivo {archivo_info['name']} desde Google Drive",
                                "metadatos_especificos": archivo_info
                            }
                        }
                        resultado["datos_procesados"] = datos_basicos
                        resultado["pasos_completados"].append("procesamiento_basico")
                        
                except Exception as e:
                    error_msg = f"Error en procesamiento fenomenológico: {str(e)}"
                    logger.error(error_msg)
                    resultado["errores"].append(error_msg)
            
            # PASO 2: Guardar en Supabase
            if self.supabase and resultado["datos_procesados"]:
                try:
                    resultado_supabase = self.supabase.guardar_preinstancia(resultado["datos_procesados"])
                    if resultado_supabase.get('success'):
                        resultado["pasos_completados"].append("guardado_supabase")
                        resultado["supabase_id"] = resultado_supabase.get('id')
                    else:
                        resultado["errores"].append(f"Error guardando en Supabase: {resultado_supabase.get('error')}")
                except Exception as e:
                    error_msg = f"Error guardando en Supabase: {str(e)}"
                    logger.error(error_msg)
                    resultado["errores"].append(error_msg)
            
            # PASO 3: Enviar a N8N para procesamiento avanzado
            if self.n8n and resultado["datos_procesados"]:
                try:
                    resultado_n8n = self.n8n.enviar_datos_webhook(
                        resultado["datos_procesados"], 
                        origen="automatizacion_completa"
                    )
                    if resultado_n8n.get('success'):
                        resultado["pasos_completados"].append("enviado_n8n")
                        resultado["n8n_response"] = resultado_n8n
                    else:
                        resultado["errores"].append(f"Error enviando a N8N: {resultado_n8n.get('error')}")
                except Exception as e:
                    error_msg = f"Error enviando a N8N: {str(e)}"
                    logger.error(error_msg)
                    resultado["errores"].append(error_msg)
            
            # Actualizar estadísticas
            self.estado_sistema["archivos_procesados"] += 1
            self.estado_sistema["ultimo_procesamiento"] = datetime.now().isoformat()
            
            if resultado["errores"]:
                self.estado_sistema["errores"] += len(resultado["errores"])
            
            logger.info(f"Procesamiento completo finalizado para {archivo_info.get('name')}. Pasos: {resultado['pasos_completados']}")
            return resultado
            
        except Exception as e:
            error_msg = f"Error crítico procesando archivo {archivo_info.get('name', 'desconocido')}: {str(e)}"
            logger.error(error_msg)
            return {
                "archivo": archivo_info.get('name'),
                "error_critico": error_msg,
                "timestamp": datetime.now().isoformat()
            }
    
    def _detectar_tipo_archivo(self, archivo_info: Dict[str, Any]) -> str:
        """Detecta el tipo de archivo basado en mimeType y extensión"""
        mime_type = archivo_info.get('mimeType', '')
        nombre = archivo_info.get('name', '')
        
        if mime_type.startswith('image/'):
            return 'imagen'
        elif mime_type.startswith('text/'):
            return 'texto'
        elif mime_type.startswith('audio/'):
            return 'audio'
        elif mime_type.startswith('video/'):
            return 'video'
        elif nombre.endswith('.md'):
            return 'markdown'
        elif nombre.endswith(('.json', '.yaml', '.yml')):
            return 'configuracion'
        else:
            return 'otro'
    
    def iniciar_monitoreo_automatico(self):
        """Inicia el monitoreo automático de Google Drive"""
        if not self.google_drive:
            logger.error("Google Drive no está disponible")
            return
        
        if not self.google_drive.monitored_folders:
            logger.warning("No hay carpetas configuradas para monitorear")
            # Listar carpetas disponibles
            try:
                carpetas = self.google_drive.listar_carpetas()
                logger.info(f"Carpetas disponibles en Google Drive: {len(carpetas)}")
                for carpeta in carpetas[:5]:  # Mostrar solo las primeras 5
                    logger.info(f"  - {carpeta['name']} (ID: {carpeta['id']})")
            except Exception as e:
                logger.error(f"Error listando carpetas: {e}")
            return
        
        logger.info(f"Iniciando monitoreo de {len(self.google_drive.monitored_folders)} carpetas")
        
        # Callback para procesar archivos
        def callback_procesamiento(archivo_info):
            try:
                # Ejecutar procesamiento asíncrono
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                resultado = loop.run_until_complete(self.procesar_archivo_completo(archivo_info))
                loop.close()
                
                logger.info(f"Archivo procesado: {archivo_info['name']} - Resultado: {len(resultado.get('pasos_completados', []))} pasos completados")
                
            except Exception as e:
                logger.error(f"Error en callback de procesamiento: {e}")
        
        # Iniciar monitoreo
        try:
            self.google_drive.monitorear_cambios(
                callback=callback_procesamiento,
                intervalo=30  # Revisar cada 30 segundos
            )
        except KeyboardInterrupt:
            logger.info("Monitoreo detenido por el usuario")
        except Exception as e:
            logger.error(f"Error en monitoreo: {e}")
    
    def obtener_estado_sistema(self) -> Dict[str, Any]:
        """Obtiene el estado actual del sistema"""
        estado = {
            "sistema": self.estado_sistema.copy(),
            "componentes": {
                "n8n": {
                    "disponible": self.n8n is not None,
                    "webhook_url": self.n8n.n8n_webhook_url if self.n8n else None
                },
                "supabase": {
                    "disponible": self.supabase is not None,
                    "url": self.supabase.supabase_url if self.supabase else None
                },
                "google_drive": {
                    "disponible": self.google_drive is not None,
                    "carpetas_monitoreadas": len(self.google_drive.monitored_folders) if self.google_drive else 0
                },
                "procesador": {
                    "disponible": self.procesador is not None
                }
            }
        }
        
        # Obtener estadísticas de Supabase si está disponible
        if self.supabase:
            try:
                estadisticas = self.supabase.obtener_estadisticas()
                estado["componentes"]["supabase"]["estadisticas"] = estadisticas.get("estadisticas")
            except Exception as e:
                logger.error(f"Error obteniendo estadísticas de Supabase: {e}")
        
        return estado

def main():
    """Función principal"""
    try:
        # Crear instancia del sistema
        sistema = AutomatizacionCompletaYO()
        
        # Mostrar estado del sistema
        estado = sistema.obtener_estado_sistema()
        logger.info(f"Estado del sistema: {json.dumps(estado, indent=2, ensure_ascii=False)}")
        
        # Verificar si el monitoreo está habilitado
        if os.getenv('ENABLE_DRIVE_MONITOR', 'false').lower() == 'true':
            logger.info("Iniciando monitoreo automático de Google Drive...")
            sistema.iniciar_monitoreo_automatico()
        else:
            logger.info("Monitoreo automático deshabilitado. Para habilitarlo, configure ENABLE_DRIVE_MONITOR=true")
            
            # Mostrar información del sistema
            print("\n" + "="*60)
            print("SISTEMA DE AUTOMATIZACIÓN YO ESTRUCTURAL")
            print("="*60)
            print(f"Archivos procesados: {estado['sistema']['archivos_procesados']}")
            print(f"Errores: {estado['sistema']['errores']}")
            print(f"Componentes disponibles:")
            for comp, info in estado['componentes'].items():
                status = "✓" if info['disponible'] else "✗"
                print(f"  {status} {comp.upper()}")
            print("\nPara iniciar el monitoreo automático, configure ENABLE_DRIVE_MONITOR=true en .env")
            print("="*60)
    
    except KeyboardInterrupt:
        logger.info("Sistema detenido por el usuario")
    except Exception as e:
        logger.error(f"Error crítico en el sistema: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()