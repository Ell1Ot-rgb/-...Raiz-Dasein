import os
import pandas as pd
from datetime import datetime
from extractor_features import ExtractorFeatures
from clasificador import ClasificadorFenomenologico
from gestor_modelo_semantico import GestorModeloSemantico

def analizar_sistema_local():
    # Crear directorio para reportes si no existe
    reporte_dir = os.path.join('logs_sistema')
    os.makedirs(reporte_dir, exist_ok=True)
    
    # Nombre del archivo de reporte
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    reporte_path = os.path.join(reporte_dir, f'reporte_analisis_{timestamp}.txt')
    
    with open(reporte_path, 'w', encoding='utf-8') as f:
        f.write('=== REPORTE DE ANÁLISIS DEL SISTEMA ===\n\n')
        
        # 1. Análisis de textos de entrada
        ruta_textos = os.path.join('entrada_bruta')
        textos = []
        for archivo in sorted(os.listdir(ruta_textos)):
            if archivo.endswith('.txt'):
                with open(os.path.join(ruta_textos, archivo), 'r', encoding='utf-8') as txt:
                    textos.append(txt.read())
        
        f.write(f'Textos procesados: {len(textos)}\n')
        
        # 2. Extracción de características
        extractor = ExtractorFeatures()
        features_df = extractor.extraer_features_tfidf(textos)
        f.write(f'Características extraídas: {features_df.shape[1]}\n')
        
        # 3. Análisis de gradientes
        ruta_gradientes = os.path.join('features_extraidas', 'features_tfidf.csv')
        if os.path.exists(ruta_gradientes):
            gradientes_df = pd.read_csv(ruta_gradientes)
            f.write(f'Gradientes almacenados: {gradientes_df.shape[0]}\n')
        
        # 4. Análisis de preinstancias
        ruta_preinstancias = os.path.join('procesado', 'nodos_fenomenologicos')
        if os.path.exists(ruta_preinstancias):
            num_preinstancias = len(os.listdir(ruta_preinstancias))
            f.write(f'Preinstancias generadas: {num_preinstancias}\n')
        
        # 5. Estado del modelo semántico
        gestor = GestorModeloSemantico()
        estado_modelo = gestor.obtener_estado()
        f.write('\nEstado del modelo semántico:\n')
        f.write(f'- Conceptos totales: {estado_modelo.get("total_conceptos", 0)}\n')
        f.write(f'- Relaciones: {estado_modelo.get("total_relaciones", 0)}\n')
        
    print(f'Reporte generado en: {reporte_path}')
    return reporte_path

if __name__ == '__main__':
    analizar_sistema_local()