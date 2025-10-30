import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import yaml
import os
import nltk
from nltk.corpus import stopwords
import csv
import re

# Asegura recursos NLTK para español
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

def cargar_config():
    ruta = os.path.join(os.path.dirname(__file__), '..', 'configuracion', 'config.yaml')
    with open(ruta, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

class ExtractorFeatures:
    def __init__(self, config):
        self.config = config
        self.idioma = self.config['procesamiento'].get('idioma', 'spanish')
        try:
            self.stopwords = set(stopwords.words(self.idioma))
        except Exception:
            self.stopwords = set(stopwords.words('english'))
        self.vectorizador = None

    def limpiar_texto(self, texto):
        import unicodedata
        
        # Normalizar unicode
        texto = unicodedata.normalize('NFKD', texto)
        texto = texto.lower()
        
        # Mejorar regex para español
        texto = re.sub(r'[^a-záéíóúñü\s]', ' ', texto)
        texto = re.sub(r'\s+', ' ', texto)
        
        palabras = texto.split()
        if self.config['procesamiento']['eliminar_stopwords']:
            # Añadir stopwords personalizadas
            stopwords_extra = {'ser', 'estar', 'tener', 'hacer', 'decir', 'muy', 'más', 'todo'}
            self.stopwords.update(stopwords_extra)
            palabras = [p for p in palabras if p not in self.stopwords and len(p) > 2]
        
        return ' '.join(palabras).strip()

    def crear_vectorizador_tfidf(self):
        self.vectorizador = TfidfVectorizer(
            max_features=self.config['procesamiento']['max_features_tfidf'],
            ngram_range=tuple(self.config['procesamiento']['ngram_range']),
            min_df=2,  # Cambiar de 1 a 2 para reducir ruido
            max_df=0.85,  # Reducir de 0.95 a 0.85
            sublinear_tf=True,  # Añadir escalado sublineal
            use_idf=True
        )
        return self.vectorizador

    def extraer_features_tfidf(self, textos):
        textos_limpios = [self.limpiar_texto(t) for t in textos]
        if self.vectorizador is None:
            self.crear_vectorizador_tfidf()
        matriz = self.vectorizador.fit_transform(textos_limpios)
        nombres = self.vectorizador.get_feature_names_out()
        return pd.DataFrame(matriz.toarray(), columns=nombres)
    
    def clasificar_texto_automaticamente(self, texto, nombre_archivo, tfidf_vocab=None):
        categorias_base = self.config['fenomenologia']['categorias_base']
        # Diccionario ampliado de palabras/frases clave y sinónimos
        palabras_clave = {
            "experiencia_vivida": ["experiencia", "vivencia", "fenomenológico", "vivido", "estructura esencial"],
            "conciencia_temporal": ["tiempo", "temporal", "momento", "duración", "pasado", "futuro", "presente", "retención", "protención", "flujo"],
            "intersubjetividad": ["otro", "alter ego", "empatía", "relación", "encuentro", "diálogo", "intersubjetivo", "compartida"],
            "corporalidad": ["cuerpo", "corporal", "físico", "sensación", "tacto", "leib", "movimiento", "vivido"],
            "espacialidad": ["espacio", "espacial", "lugar", "orientación", "dirección", "arriba", "abajo", "derecha", "izquierda", "centro"],
            "mundaneidad": ["mundo", "mundano", "cotidiano", "diario", "rutina", "habitual", "ordinario", "lebenswelt", "vida cotidiana"],
            "afectividad": ["afecto", "emoción", "sentimiento", "tristeza", "alegría", "temple", "ánimo", "angustia", "afectiva"],
            "intencionalidad": ["intención", "intencional", "dirigido", "noesis", "noema", "correlación", "objeto", "sentido"]
        }
        texto_lower = texto.lower()
        scores = {cat: 0 for cat in categorias_base}
        # 1. Coincidencia directa y frases exactas
        for cat, palabras in palabras_clave.items():
            for palabra in palabras:
                if palabra in texto_lower:
                    scores[cat] += 2 if " " in palabra else 1
        # 2. TF-IDF (si se pasa el vocabulario)
        if tfidf_vocab:
            for cat, palabras in palabras_clave.items():
                for palabra in palabras:
                    if palabra in tfidf_vocab:
                        scores[cat] += tfidf_vocab[palabra]
        # 3. Coincidencia de contexto (palabras cercanas)
        for cat, palabras in palabras_clave.items():
            for palabra in palabras:
                if any(p in texto_lower for p in palabra.split()):
                    scores[cat] += 0.5
        # 4. Etiquetas múltiples si hay empate o ambigüedad
        max_score = max(scores.values())
        etiquetas = [cat for cat, score in scores.items() if score == max_score and score > 0]
        # Si ninguna categoría destaca, asignar por hash
        if not etiquetas:
            etiquetas = [categorias_base[hash(nombre_archivo) % len(categorias_base)]]
        return etiquetas if len(etiquetas) > 1 else etiquetas[0]

if __name__ == "__main__":
    config = cargar_config()
    
    # Leer todos los archivos de texto de entrada
    dir_entrada = os.path.join(os.path.dirname(__file__), '..', 'entrada_bruta')
    textos = []
    archivos_txt = []
    
    for archivo in sorted(os.listdir(dir_entrada)):
        if archivo.endswith('.txt'):
            ruta = os.path.join(dir_entrada, archivo)
            with open(ruta, 'r', encoding='utf-8') as f:
                contenido = f.read()
                textos.append(contenido)
                archivos_txt.append(archivo)
    
    print(f"Procesando {len(textos)} archivos de texto...")
    
    # Extraer características
    extractor = ExtractorFeatures(config)
    df = extractor.extraer_features_tfidf(textos)
    
    # Guardar features
    ruta_salida = os.path.join(os.path.dirname(__file__), '..', 'features_extraidas', 'features_tfidf.csv')
    df.to_csv(ruta_salida, index=False)
    print(f"Features guardadas en {ruta_salida}")

    # Generar etiquetas automáticamente
    # Después de guardar features_tfidf.csv, añade esto:
    etiquetas = []
    for i, nombre_archivo in enumerate(archivos_txt):
        categoria = extractor.clasificar_texto_automaticamente(textos[i], nombre_archivo)
        etiquetas.append(categoria)
    
    # Crear DataFrame de etiquetas con la estructura correcta
    etiquetas_df = pd.DataFrame({
        "archivo": archivos_txt,
        "clase": etiquetas
    })
    
    # Guardar etiquetas
    ruta_etiquetas = os.path.join(os.path.dirname(__file__), '..', 'features_extraidas', 'etiquetas.csv')
    etiquetas_df.to_csv(ruta_etiquetas, index=False)
    print(f"Etiquetas guardadas en {ruta_etiquetas}")
    
    # Mostrar resumen
    print(f"\nResumen del procesamiento:")
    print(f"- Archivos procesados: {len(textos)}")
    print(f"- Características extraídas: {df.shape[1]}")
    print(f"- Distribución de categorías:")
    for categoria, count in etiquetas_df['clase'].value_counts().items():
        print(f"  * {categoria}: {count} archivos")
     