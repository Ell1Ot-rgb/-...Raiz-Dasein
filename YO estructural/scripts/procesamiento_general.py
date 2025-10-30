from extractor_features import ExtractorFeatures
from clasificador import ClasificadorFenomenologico, cargar_config

def pipeline_demo():
    config = cargar_config()
    textos = ["Texto ejemplo fenomenológico.", "Otra vivencia relatada aquí."]
    extractor = ExtractorFeatures(config)
    X = extractor.extraer_features_tfidf(textos)
    y = ['experiencia_vivida', 'afectividad']
    clf = ClasificadorFenomenologico(config)
    clf.entrenar(X, y)

if __name__ == "__main__":
    pipeline_demo()