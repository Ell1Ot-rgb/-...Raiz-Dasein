# ⚡ GENERADOR DE RUTAS - EJECUCIÓN INMEDIATA

## 🚀 COMENZAR AHORA MISMO

### Opción 1: Prueba Rápida (30 segundos)

```bash
cd "/workspaces/-...Raiz-Dasein/YO estructural"

# Ejecutar demostración
python3 procesadores/generador_rutas_fenomenologicas.py
```

**Salida esperada:**
```
Concepto: SOPORTE
Certeza individual promedio: 0.9412
Certeza combinada: 0.9999941
¿Máximo relacional?: True
Confianza: ALTO
Tiempo: 2.3ms

RUTAS GENERADAS:

1. Física
   Definición: Desde una perspectiva física, SOPORTE se refiere a...
   Confianza: 0.9412

2. Ergonómica
   Definición: Desde una perspectiva ergonómica, SOPORTE se define por...
   Confianza: 0.9356

... (más rutas)
```

---

### Opción 2: Procesar Múltiples Conceptos

```python
#!/usr/bin/env python3
# archivo: procesar_conceptos.py

from procesadores.generador_rutas_fenomenologicas import GeneradorRutasFenomenologicas

gen = GeneradorRutasFenomenologicas()

# Conceptos para procesar
conceptos = [
    "SOPORTE",
    "TIEMPO",
    "ESPACIO",
    "CONSCIENCIA",
    "EMERGENCIA",
    "IDENTIDAD"
]

# Procesar
resultados = gen.generar_rutas_batch(conceptos, batch_size=2)

# Mostrar reporte
print(gen.generar_reporte(resultados))

# Guardar resultados
for resultado in resultados:
    gen.guardar_resultado(resultado)

print("\n✓ Resultados guardados en ./resultados_rutas/")
```

**Ejecutar:**
```bash
python3 procesar_conceptos.py
```

---

### Opción 3: Con Neo4j (Si PC2 está corriendo)

```python
#!/usr/bin/env python3
# archivo: procesar_con_neo4j.py

from procesadores.extensiones_neo4j_lightrag import GeneradorRutasConExtensiones

# Inicializar con Neo4j
gen = GeneradorRutasConExtensiones(
    usar_neo4j=True,
    usar_lightrag=False
)

# Procesar concepto
resultado = gen.generar_rutas_mejorado("SOPORTE")

# Resultado ahora está en Neo4j
print(f"✓ Guardado en Neo4j")
print(f"  Concepto: {resultado['concepto']}")
print(f"  Máximo relacional: {resultado['es_maximo_relacional']}")
print(f"  Guardado: {resultado['metadatos'].get('neo4j_guardado', False)}")
```

---

### Opción 4: Con LightRAG (Si PC2 está corriendo)

```python
#!/usr/bin/env python3
# archivo: procesar_con_lightrag.py

from procesadores.extensiones_neo4j_lightrag import GeneradorRutasConExtensiones

# Inicializar con LightRAG
gen = GeneradorRutasConExtensiones(
    usar_neo4j=False,
    usar_lightrag=True
)

# Procesar concepto
resultado = gen.generar_rutas_mejorado("SOPORTE")

# Resultado con definiciones refinadas
for ruta in resultado['rutas']:
    print(f"\n{ruta['nombre']}:")
    print(f"  Original: {ruta['definicion'][:80]}...")
    if 'definicion_refinada' in ruta:
        print(f"  Refinada: {ruta['definicion_refinada'][:80]}...")
```

---

### Opción 5: Completa (Con todo)

```python
#!/usr/bin/env python3
# archivo: procesar_completo.py

from procesadores.extensiones_neo4j_lightrag import GeneradorRutasConExtensiones

# Inicializar con TODO
gen = GeneradorRutasConExtensiones(
    usar_neo4j=True,
    usar_lightrag=True
)

# Procesar
resultado = gen.generar_rutas_mejorado("SOPORTE")

print(f"""
✓ PROCESAMIENTO COMPLETO:

Concepto: {resultado['concepto']}
Rutas: {len(resultado['rutas'])}
Máximo: {resultado['es_maximo_relacional']}
Certeza: {resultado['certeza_combinada']:.4f}

Metadatos:
- LightRAG: {resultado['metadatos'].get('lightrag_aplicado', False)}
- Neo4j: {resultado['metadatos'].get('neo4j_guardado', False)}

""")

# Ver una ruta refinada
if resultado['rutas']:
    r = resultado['rutas'][0]
    print(f"Ejemplo ruta refinada ({r['nombre']}):")
    if 'definicion_refinada' in r:
        print(f"  {r['definicion_refinada'][:200]}...")
```

---

## 📊 RENDIMIENTO ESPERADO

### En PC1 (4GB RAM, dual-core):

```
Concepto simple:
  Tiempo: 2-3ms
  RAM: +50MB
  
Batch 10 conceptos:
  Tiempo: 20-30ms
  RAM: +100MB
  
Batch 100 conceptos:
  Tiempo: 200-300ms
  RAM: +300MB (pico)
  
Máximos encontrados:
  Esperado: 30-40% de conceptos
```

---

## 🔍 QÚÉVER EN LOS RESULTADOS

### Archivo YAML generado (`resultados_rutas/soporte_rutas.yaml`):

```yaml
concepto: SOPORTE
certeza_individual_promedio: 0.9412
certeza_combinada: 0.9999941
es_maximo_relacional: true
confianza_diagnostico: ALTO
tiempo_procesamiento_ms: 2.34
rutas:
  - nombre: Física
    definicion: "Desde una perspectiva física, SOPORTE se refiere..."
    similitud_promedio: 0.9412
    confianza: 0.9412
  - nombre: Ergonómica
    definicion: "Desde una perspectiva ergonómica, SOPORTE se define..."
    similitud_promedio: 0.9356
    confianza: 0.9356
  # ... más rutas
```

---

## 🎯 FLUJO RECOMENDADO

### 1️⃣ COMENZAR (Ahora)
```bash
python3 procesadores/generador_rutas_fenomenologicas.py
# ✓ Verifica que funciona
```

### 2️⃣ PROCESAR (Cuando tengas conceptos)
```bash
python3 procesar_conceptos.py
# ✓ Genera múltiples máximos
# ✓ Guarda en YAML/JSON
```

### 3️⃣ MEJORAR (Opcional - Cuando necesites)
```bash
# Si quieres escalabilidad:
# docker-compose -f docker-compose-PC2.yml up -d
python3 procesar_con_neo4j.py

# Si quieres mejor calidad:
python3 procesar_con_lightrag.py
```

### 4️⃣ ANALIZAR (Opcional - Para insights)
```bash
# Con Neo4j corriendo, hacer queries
# Ver comunidades de máximos
# Analizar temporal
```

---

## 📁 ARCHIVOS GENERADOS

```
resultados_rutas/
├── soporte_rutas.yaml      ← Formato legible
├── soporte_rutas.json      ← Formato máquina
├── tiempo_rutas.yaml
├── tiempo_rutas.json
├── espacio_rutas.yaml
├── espacio_rutas.json
└── ...
```

Cada archivo contiene:
- 5 rutas de definición
- Certeza individual y combinada
- ¿Es máximo relacional?
- Metadatos de procesamiento

---

## 🔧 TROUBLESHOOTING

### Error: "ModuleNotFoundError: No module named 'sentence_transformers'"

```bash
# Instalar dependencias
pip install sentence-transformers numpy scikit-learn

# O ejecutar el script de instalación
./instalar_4gb_optimizado.sh
```

### Error: "No such file or directory: './config_4gb_optimizado.yaml'"

```bash
# El generador usa configuración por defecto si no existe
# Pero puedes crear archivo:
cp config_4gb_optimizado.yaml config_4gb_optimizado.yaml
```

### RAM se agota durante procesamiento

```python
# Reducir batch_size en tu código
resultados = gen.generar_rutas_batch(
    conceptos,
    batch_size=3  # Reducir de 10 a 3
)
```

---

## ✅ CHECKLIST

- [ ] ¿Tengo 1GB+ RAM disponible? (`free -h`)
- [ ] ¿Tengo Python 3.8+? (`python3 --version`)
- [ ] ¿Ejecuté `instalar_4gb_optimizado.sh`? (O instalé dependencias)
- [ ] ¿Puedo importar SentenceTransformer? (`python3 -c "from sentence_transformers import SentenceTransformer"`)
- [ ] ¿Tengo PC2 para Neo4j? (Opcional)
- [ ] ¿Tengo PC2 para LightRAG? (Opcional)

---

## 🎓 PRÓXIMOS PASOS

1. **Ejecutar demostración:**
   ```bash
   python3 procesadores/generador_rutas_fenomenologicas.py
   ```

2. **Procesar conceptos propios:**
   - Crear archivo `procesar_conceptos.py`
   - Listar tus conceptos
   - Ejecutar

3. **Agregar Neo4j** (cuando tengas volumen)
   - Iniciar PC2
   - Usar `GeneradorRutasConExtensiones(usar_neo4j=True)`

4. **Agregar LightRAG** (para mejor calidad)
   - Usar `GeneradorRutasConExtensiones(usar_lightrag=True)`

---

## 📞 AYUDA

- **¿Cómo uso Python puro?** → Ver Opción 1-2 arriba
- **¿Cómo integro Neo4j?** → Ver Opción 3 arriba
- **¿Cómo integro LightRAG?** → Ver Opción 4 arriba
- **¿Cómo uso ambos?** → Ver Opción 5 arriba
- **¿Qué es máximo relacional?** → Lee `ANALISIS_CAPACIDADES_GENERADOR_RUTAS.md`
- **¿Qué mejoran Neo4j/LightRAG?** → Lee `GUIA_INTEGRACION_GENERADOR_RUTAS.md`

---

**¡LISTO PARA USAR! 🚀**

Ejecuta ahora: `python3 procesadores/generador_rutas_fenomenologicas.py`
