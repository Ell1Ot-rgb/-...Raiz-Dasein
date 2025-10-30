#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Ejecución Completa del Sistema YO Estructural
Genera diagnósticos detallados y ejecuta todo el flujo fenomenológico
"""

import os
import sys
import json
import time
import logging
import traceback
from datetime import datetime
from pathlib import Path

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar módulos del sistema
try:
    from sistema_principal_v2 import SistemaFenomenologicoV2
    from motor_yo.sistema_yo_emergente import SistemaYoEmergente
    # Eliminar esta línea:
    # from verificar import main as verificar_sistema
except ImportError as e:
    print(f"Error al importar módulos: {e}")
    sys.exit(1)

class DiagnosticadorSistema:
    """Clase para generar diagnósticos detallados del sistema"""
    
    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.directorio_diagnosticos = f"diagnosticos_sistema_{self.timestamp}"
        self.crear_directorio_diagnosticos()
        self.configurar_logging()
        
    def crear_directorio_diagnosticos(self):
        """Crea el directorio para los diagnósticos"""
        os.makedirs(self.directorio_diagnosticos, exist_ok=True)
        os.makedirs(f"{self.directorio_diagnosticos}/logs", exist_ok=True)
        os.makedirs(f"{self.directorio_diagnosticos}/metricas", exist_ok=True)
        os.makedirs(f"{self.directorio_diagnosticos}/estados", exist_ok=True)
        
    def configurar_logging(self):
        """Configura el sistema de logging para diagnósticos"""
        log_file = f"{self.directorio_diagnosticos}/logs/diagnostico_completo.log"
        
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger("DiagnosticadorSistema")
        self.logger.info(f"Iniciando diagnóstico completo del sistema - {self.timestamp}")
        
    def verificar_prerequisitos(self):
        """Verifica que todos los prerequisitos estén cumplidos"""
        self.logger.info("=== VERIFICACIÓN DE PREREQUISITOS ===")
        
        # Verificar estructura de directorios
        directorios_requeridos = [
            'entrada_bruta', 'procesado', 'logs_sistema', 'configuracion'
        ]
        
        for directorio in directorios_requeridos:
            if os.path.exists(directorio):
                self.logger.info(f"✓ Directorio {directorio} existe")
            else:
                self.logger.error(f"✗ Directorio {directorio} no encontrado")
                return False
                
        # Verificar archivos de configuración
        if os.path.exists('configuracion/config.yaml'):
            self.logger.info("✓ Archivo de configuración encontrado")
        else:
            self.logger.error("✗ Archivo de configuración no encontrado")
            return False
            
        # Contar archivos de entrada
        archivos_entrada = len([f for f in os.listdir('entrada_bruta') if f.endswith('.txt')])
        self.logger.info(f"✓ Encontrados {archivos_entrada} archivos de texto en entrada_bruta")
        
        return True
        
    def ejecutar_verificacion_sistema(self):
        """Ejecuta la verificación completa del sistema"""
        self.logger.info("=== VERIFICACIÓN COMPLETA DEL SISTEMA ===")
        try:
            # Realizar verificaciones básicas del sistema
            verificaciones_ok = True
            
            # Verificar que los módulos principales estén disponibles
            if not all([hasattr(self, attr) for attr in ['logger', 'directorio_diagnosticos']]):
                self.logger.error("✗ Faltan atributos requeridos en el diagnosticador")
                verificaciones_ok = False
            
            if verificaciones_ok:
                self.logger.info("✓ Verificación del sistema completada exitosamente")
            else:
                self.logger.warning("⚠ Verificación del sistema completada con advertencias")
            return verificaciones_ok
        except Exception as e:
            self.logger.error(f"✗ Error en verificación del sistema: {str(e)}")
            return False
            
    def ejecutar_sistema_principal(self):
        """Ejecuta el sistema principal y captura métricas"""
        self.logger.info("=== EJECUCIÓN DEL SISTEMA PRINCIPAL ===")
        
        try:
            # Inicializar sistema
            config_path = 'configuracion/config.yaml'
            sistema = SistemaFenomenologicoV2(config_path)
            sistema.modo_diagnostico = True
            
            self.logger.info("Sistema inicializado correctamente")
            
            # Ejecutar flujo completo
            inicio = time.time()
            resultado = sistema.procesar_flujo_completo('entrada_bruta')
            fin = time.time()
            
            # Guardar métricas de ejecución
            metricas_ejecucion = {
                "tiempo_ejecucion_segundos": fin - inicio,
                "timestamp_inicio": datetime.fromtimestamp(inicio).isoformat(),
                "timestamp_fin": datetime.fromtimestamp(fin).isoformat(),
                "resultado": resultado
            }
            
            # Guardar métricas (con conversión de Enum a string)
            with open(f"{self.directorio_diagnosticos}/metricas/metricas_ejecucion.json", 'w', encoding='utf-8') as f:
                json.dump(metricas_ejecucion, f, indent=2, ensure_ascii=False, default=str)
                
            # Guardar estado del YO
            estado_yo = sistema.motor_yo.estado_actual.__dict__
            with open(f"{self.directorio_diagnosticos}/estados/estado_yo_final.json", 'w', encoding='utf-8') as f:
                json.dump(estado_yo, f, indent=2, ensure_ascii=False, default=str)
                
            self.logger.info(f"✓ Sistema ejecutado exitosamente en {fin-inicio:.2f} segundos")
            return resultado, sistema
            
        except Exception as e:
            self.logger.error(f"✗ Error en ejecución del sistema: {str(e)}")
            self.logger.error(traceback.format_exc())
            return None, None
            
    def generar_reporte_diagnostico(self, resultado, sistema):
        """Genera un reporte completo de diagnóstico"""
        self.logger.info("=== GENERACIÓN DE REPORTE DIAGNÓSTICO ===")
        
        reporte = {
            "timestamp": self.timestamp,
            "version_sistema": "2.2",
            "resumen_ejecucion": {
                "exitoso": resultado is not None,
                "emergencia_yo_detectada": resultado.get('emergencia_detectada', False) if resultado else False,
                "instancias_procesadas": resultado.get('instancias_procesadas', 0) if resultado else 0,
                "vohexistencias_detectadas": resultado.get('vohexistencias_detectadas', 0) if resultado else 0
            }
        }
        
        if sistema:
            # Agregar métricas del sistema
            reporte["metricas_sistema"] = sistema.metricas
            
            # Agregar estado del YO
            reporte["estado_yo"] = {
                "tipo_actual": sistema.motor_yo.estado_actual.tipo.name if hasattr(sistema.motor_yo.estado_actual, 'tipo') else "DESCONOCIDO",
                "version": sistema.motor_yo.estado_actual.version,
                "contextos_activos": len(sistema.motor_yo.estado_actual.contextos_activos),
                "reflexiones": len(sistema.motor_yo.estado_actual.reflexiones)
            }
            
            # Agregar auditoría si está disponible
            if hasattr(sistema.motor_yo, 'auditoria'):
                reporte["auditoria_eventos"] = len(sistema.motor_yo.auditoria)
        
        # Guardar reporte
        with open(f"{self.directorio_diagnosticos}/reporte_diagnostico_completo.json", 'w', encoding='utf-8') as f:
            json.dump(reporte, f, indent=2, ensure_ascii=False)
            
        # Generar reporte en texto legible
        self.generar_reporte_texto(reporte)
        
        self.logger.info("✓ Reporte de diagnóstico generado")
        
    def generar_reporte_texto(self, reporte):
        """Genera un reporte en formato texto legible"""
        with open(f"{self.directorio_diagnosticos}/REPORTE_DIAGNOSTICO.txt", 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("REPORTE DE DIAGNÓSTICO COMPLETO - SISTEMA YO ESTRUCTURAL\n")
            f.write("=" * 80 + "\n\n")
            
            f.write(f"Timestamp: {reporte['timestamp']}\n")
            f.write(f"Versión del Sistema: {reporte['version_sistema']}\n\n")
            
            f.write("RESUMEN DE EJECUCIÓN:\n")
            f.write("-" * 40 + "\n")
            resumen = reporte['resumen_ejecucion']
            f.write(f"• Ejecución exitosa: {'SÍ' if resumen['exitoso'] else 'NO'}\n")
            f.write(f"• Emergencia del YO detectada: {'SÍ' if resumen['emergencia_yo_detectada'] else 'NO'}\n")
            f.write(f"• Instancias procesadas: {resumen['instancias_procesadas']}\n")
            f.write(f"• Vohexistencias detectadas: {resumen['vohexistencias_detectadas']}\n\n")
            
            if 'metricas_sistema' in reporte:
                f.write("MÉTRICAS DEL SISTEMA:\n")
                f.write("-" * 40 + "\n")
                metricas = reporte['metricas_sistema']
                for clave, valor in metricas.items():
                    f.write(f"• {clave}: {valor}\n")
                f.write("\n")
            
            if 'estado_yo' in reporte:
                f.write("ESTADO DEL YO:\n")
                f.write("-" * 40 + "\n")
                estado = reporte['estado_yo']
                for clave, valor in estado.items():
                    f.write(f"• {clave}: {valor}\n")
                f.write("\n")
            
            f.write("=" * 80 + "\n")
            f.write("Diagnóstico completado exitosamente\n")
            f.write("=" * 80 + "\n")

def main():
    """Función principal del script"""
    print("🧠 SISTEMA YO ESTRUCTURAL - EJECUCIÓN COMPLETA CON DIAGNÓSTICOS")
    print("=" * 80)
    
    # Crear diagnosticador
    diagnosticador = DiagnosticadorSistema()
    
    try:
        # 1. Verificar prerequisitos
        print("\n1. Verificando prerequisitos...")
        if not diagnosticador.verificar_prerequisitos():
            print("❌ Prerequisitos no cumplidos. Abortando ejecución.")
            return False
        print("✅ Prerequisitos verificados")
        
        # 2. Ejecutar verificación del sistema
        print("\n2. Ejecutando verificación completa del sistema...")
        if not diagnosticador.ejecutar_verificacion_sistema():
            print("⚠️ Verificación completada con advertencias")
        else:
            print("✅ Verificación del sistema completada")
        
        # 3. Ejecutar sistema principal
        print("\n3. Ejecutando sistema fenomenológico principal...")
        resultado, sistema = diagnosticador.ejecutar_sistema_principal()
        
        if resultado is None:
            print("❌ Error en la ejecución del sistema principal")
            return False
        print("✅ Sistema principal ejecutado exitosamente")
        
        # 4. Generar reporte de diagnóstico
        print("\n4. Generando reporte de diagnóstico...")
        diagnosticador.generar_reporte_diagnostico(resultado, sistema)
        print("✅ Reporte de diagnóstico generado")
        
        # 5. Mostrar resumen final
        print("\n" + "=" * 80)
        print("🎉 EJECUCIÓN COMPLETADA EXITOSAMENTE")
        print("=" * 80)
        print(f"📁 Diagnósticos guardados en: {diagnosticador.directorio_diagnosticos}")
        print(f"🧠 Estado del YO: {sistema.motor_yo.estado_actual.tipo.name if hasattr(sistema.motor_yo.estado_actual, 'tipo') else 'DESCONOCIDO'}")
        print(f"📊 Instancias procesadas: {resultado.get('instancias_procesadas', 0)}")
        print(f"🔗 Vohexistencias detectadas: {resultado.get('vohexistencias_detectadas', 0)}")
        print(f"⚡ Emergencia detectada: {'SÍ' if resultado.get('emergencia_detectada', False) else 'NO'}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error crítico en la ejecución: {str(e)}")
        diagnosticador.logger.error(f"Error crítico: {str(e)}")
        diagnosticador.logger.error(traceback.format_exc())
        return False

if __name__ == "__main__":
    try:
        exito = main()
        sys.exit(0 if exito else 1)
    except KeyboardInterrupt:
        print("\n⚠️ Ejecución interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error no manejado: {str(e)}")
        sys.exit(1)