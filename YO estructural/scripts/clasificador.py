import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import yaml
import os
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

def cargar_config():
    ruta = os.path.join(os.path.dirname(__file__), '..', 'configuracion', 'config.yaml')
    with open(ruta, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

class ClasificadorFenomenologico:
    def __init__(self, config):
        self.config = config
        # Mejorar parámetros del RandomForest
        self.modelo = RandomForestClassifier(
            n_estimators=200,  # Aumentar de 100 a 200
            max_depth=10,      # Limitar profundidad
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=config['clasificacion']['random_state'],
            n_jobs=-1,
            class_weight='balanced'  # Balancear clases automáticamente
        )
        self.esta_entrenado = False

    def entrenar(self, X, y):
        from collections import Counter
        
        # Verificar si hay suficientes muestras para estratificar
        conteo_clases = Counter(y)
        clases_insuficientes = [clase for clase, count in conteo_clases.items() if count < 2]
        
        if clases_insuficientes:
            # Sin estratificación si hay clases con pocas muestras
            X_train, X_test, y_train, y_test = train_test_split(
                X, y,
                test_size=self.config['clasificacion']['test_size'],
                random_state=self.config['clasificacion']['random_state']
            )
            print(f"Advertencia: Clases con pocas muestras detectadas: {clases_insuficientes}")
            print("Entrenamiento sin estratificación.")
        else:
            # Con estratificación normal
            X_train, X_test, y_train, y_test = train_test_split(
                X, y,
                test_size=self.config['clasificacion']['test_size'],
                random_state=self.config['clasificacion']['random_state'],
                stratify=y
            )
        
        self.modelo.fit(X_train, y_train)
        
        # Añadir validación cruzada
        cv_scores = cross_val_score(self.modelo, X, y, cv=3, scoring='accuracy')
        print(f"Validación cruzada: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")
        
        # Reporte detallado
        y_pred = self.modelo.predict(X_test)
        print("\nReporte de clasificación:")
        print(classification_report(y_test, y_pred))
        
        score = self.modelo.score(X_test, y_test)
        print(f"Precisión en test: {score:.2f}")
        self.esta_entrenado = True

    def predecir(self, X):
        return self.modelo.predict(X)

    def predecir_probabilidades(self, X):
        return self.modelo.predict_proba(X)

if __name__ == "__main__":
    config = cargar_config()
    # Cargar features
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'features_extraidas', 'features_tfidf.csv'))
    
    # Cargar etiquetas
    etiquetas = pd.read_csv(os.path.join(os.path.dirname(__file__), '..', 'features_extraidas', 'etiquetas.csv'))
    y = etiquetas['clase'].tolist()
    
    # Verificar que el número de muestras coincida
    if len(df) != len(y):
        raise ValueError(f"Número de muestras no coincide: {len(df)} features vs {len(y)} etiquetas")
    
    clf = ClasificadorFenomenologico(config)
    clf.entrenar(df, y)
    
    # Corregir las llamadas - solo pasar las características (df)
    predicciones = clf.predecir(df)
    probabilidades = clf.predecir_probabilidades(df)
    
    print(f"Predicciones: {predicciones}")
    print(f"Probabilidades (primeras 3): {probabilidades[:3]}")
    # Eliminar estas líneas incorrectas:
    # clf.predecir(df, y)
    # clf.predecir_probabilidades(df, y)
