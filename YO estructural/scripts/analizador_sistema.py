import os
import pandas as pd
from clasificador import ClasificadorFenomenologico, cargar_config

# Importar el gestor del modelo semántico
from gestor_modelo_semantico import GestorModeloSemantico

def analizar_sistema():
    # Crear archivo de reporte
    reporte_path = os.path.join(os.path.dirname(__file__), '..', 'logs_sistema', 'reporte_analisis.txt')
    
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write("=== REPORTE DE ANÁLISIS DEL SISTEMA ===\n\n")
        
        # Verificar estructura de directorios
        directorios = ['entrada_bruta', 'features_extraidas', 'clasificados', 'logs_sistema']
        f.write("1. Verificación de directorios:\n")
        for dir in directorios:
            path = os.path.join(os.path.dirname(__file__), '..', dir)
            existe = os.path.exists(path)
            f.write(f"   - {dir}: {'✓' if existe else 'X'}\n")
        
        # Verificar archivos necesarios
        f.write("\n2. Verificación de archivos:\n")
        archivos = {
            'features_tfidf.csv': os.path.join('features_extraidas', 'features_tfidf.csv'),
            'etiquetas.csv': os.path.join('features_extraidas', 'etiquetas.csv'),
            'config.yaml': os.path.join('configuracion', 'config.yaml')
        }
        
        for nombre, ruta in archivos.items():
            path = os.path.join(os.path.dirname(__file__), '..', ruta)
            existe = os.path.exists(path)
            f.write(f"   - {nombre}: {'✓' if existe else 'X'}\n")
        
        # Intentar cargar y procesar datos
        try:
            config = cargar_config()
            df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'features_extraidas', 'features_tfidf.csv'))
            etiquetas = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'features_extraidas', 'etiquetas.csv'))
            y = etiquetas['clase'].tolist()
            
            f.write(f"\n3. Análisis de datos:\n")
            f.write(f"   - Número de textos: {len(df)}\n")
            f.write(f"   - Número de features: {df.shape[1]}\n")
            f.write(f"   - Número de etiquetas: {len(y)}\n")
            f.write(f"   - Categorías únicas: {len(set(y))}\n")
            
            # Verificar que cada categoría tenga al menos 2 ejemplos
            from collections import Counter
            conteo = Counter(y)
            f.write("\n4. Distribución de categorías:\n")
            for categoria, count in conteo.items():
                f.write(f"   - {categoria}: {count} ejemplos\n")
                if count < 2:
                    f.write(f"     ¡ADVERTENCIA! La categoría {categoria} tiene menos de 2 ejemplos\n")
            
            # Análisis del modelo semántico
            f.write("\n5. Análisis del modelo semántico:\n")
            try:
                gestor = GestorModeloSemantico(config)
                
                # Verificar directorios del modelo semántico
                for nivel, ruta in config['modelo_semantico']['rutas'].items():
                    ruta_completa = os.path.join(os.path.dirname(__file__), '..', ruta)
                    existe = os.path.exists(ruta_completa)
                    f.write(f"   - Directorio {nivel}: {'✓' if existe else 'X'}\n")
                
                # Estadísticas del ontosistema
                gestor.ontosistema.actualizar_estadisticas()
                stats = gestor.ontosistema.estadisticas
                
                f.write("\n6. Estadísticas del modelo semántico:\n")
                f.write(f"   - Fenómenos: {stats['fenomenos']}\n")
                f.write(f"   - Contextos: {stats['contextos']}\n")
                f.write(f"   - Macrocontextos: {stats['macrocontextos']}\n")
                f.write(f"   - Redes: {stats['redes']}\n")
                f.write(f"   - Conceptos emergentes: {stats['conceptos_emergentes']}\n")
                f.write(f"   - Apariciones del YO: {stats['apariciones_yo']}\n")
                
                # Análisis de escalabilidad
                f.write("\n7. Análisis de escalabilidad:\n")
                total_elementos = sum(stats.values())
                f.write(f"   - Total de elementos: {total_elementos}\n")
                
                if total_elementos > 0:
                    porcentaje_yo = (stats['apariciones_yo'] / total_elementos) * 100
                    f.write(f"   - Porcentaje de emergencia del YO: {porcentaje_yo:.1f}%\n")
                    
                    # Calcular densidad de red
                    if stats['contextos'] > 0 and stats['redes'] > 0:
                        densidad = stats['contextos'] / stats['redes']
                        f.write(f"   - Densidad de red (contextos/red): {densidad:.1f}\n")
                
                # Verificar integridad de datos
                f.write("\n8. Verificación de integridad:\n")
                integridad_ok = True
                
                # Verificar que existan archivos para las estadísticas reportadas
                for tipo, cantidad in stats.items():
                    if tipo in config['modelo_semantico']['rutas']:
                        ruta = config['modelo_semantico']['rutas'][tipo]
                        ruta_completa = os.path.join(os.path.dirname(__file__), '..', ruta)
                        if os.path.exists(ruta_completa):
                            archivos = [f for f in os.listdir(ruta_completa) if f.endswith('.yaml')]
                            if len(archivos) != cantidad:
                                f.write(f"   - ERROR: {tipo} reporta {cantidad} pero hay {len(archivos)} archivos\n")
                                integridad_ok = False
                        else:
                            if cantidad > 0:
                                f.write(f"   - ERROR: {tipo} reporta {cantidad} pero no existe el directorio\n")
                                integridad_ok = False
                
                if integridad_ok:
                    f.write("   - Integridad de datos: ✓\n")
                
            except Exception as e:
                f.write(f"   - ERROR en análisis del modelo semántico: {str(e)}\n")
            
            # Intentar clasificar
            f.write("\n9. Prueba de clasificación:\n")
            try:
                clasificador = ClasificadorFenomenologico(config)
                X = df.values
                
                # Verificar si hay suficientes datos para entrenar
                if len(set(y)) < 2:
                    f.write("   - ERROR: Se necesitan al menos 2 categorías diferentes para entrenar\n")
                else:
                    clasificador.entrenar(X, y)
                    f.write("   - Entrenamiento: ✓\n")
                    
                    # Hacer una predicción de prueba
                    prediccion = clasificador.predecir([X[0]])
                    probabilidades = clasificador.predecir_probabilidades([X[0]])
                    f.write(f"   - Predicción de prueba: {prediccion[0]}\n")
                    f.write(f"   - Probabilidad máxima: {max(probabilidades[0]):.3f}\n")
                    
            except Exception as e:
                f.write(f"   - ERROR en clasificación: {str(e)}\n")
            
        except FileNotFoundError as e:
            f.write(f"\n3. ERROR: No se pudo cargar {e.filename}\n")
        except Exception as e:
            f.write(f"\n3. ERROR general: {str(e)}\n")
        
        # Recomendaciones
        f.write("\n10. Recomendaciones:\n")
        f.write("   - Ejecutar extractor_features.py si faltan archivos de características\n")
        f.write("   - Verificar que config.yaml tenga la configuración del modelo semántico\n")
        f.write("   - Asegurar que cada categoría tenga al menos 2 ejemplos\n")
        f.write("   - Revisar logs_sistema/ para errores específicos\n")
        f.write("   - Ejecutar gestor_modelo_semantico.py para inicializar estructuras\n")
        
        f.write(f"\n=== FIN DEL REPORTE ===\n")
    
    print(f"Reporte generado en: {reporte_path}")
    return reporte_path

if __name__ == "__main__":
    analizar_sistema()
    print("Análisis completado. Revisa el archivo 'reporte_analisis.txt' en la carpeta logs_sistema.")
    
    # Añadir después de la sección de clasificación
    f.write("\n10. Análisis de calidad del modelo:\n")
    try:
        from sklearn.metrics import confusion_matrix, f1_score
        import numpy as np
        
        # Calcular métricas adicionales
        y_pred = clasificador.predecir(X)
        f1 = f1_score(y, y_pred, average='weighted')
        f.write(f"   - F1-Score ponderado: {f1:.3f}\n")
        
        # Matriz de confusión
        cm = confusion_matrix(y, y_pred)
        f.write(f"   - Clases balanceadas: {'Sí' if np.std(np.bincount(y)) < 2 else 'No'}\n")
        
        # Detectar overfitting
        train_score = clasificador.modelo.score(X, y)
        if train_score - score > 0.2:
            f.write("   - ⚠️ Posible overfitting detectado\n")
        
    except Exception as e:
        f.write(f"   - Error en análisis avanzado: {str(e)}\n")