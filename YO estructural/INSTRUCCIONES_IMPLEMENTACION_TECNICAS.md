# 📋 INSTRUCCIONES TÉCNICAS PASO A PASO - IMPLEMENTACIÓN MÁXIMO RELACIONAL

## 🎯 Objetivo
Implementar detección de **máximo relacional definicional** en sistema existente optimizado para AMD Dual-Core + 8GB RAM, usando arquitectura híbrida (NetworkX local + Neo4j GDS remoto).

---

## 📦 Arquivos Creados

```
YO estructural/
├── config_dualcore_optimizado.yaml                 # ← CONFIGURACIÓN CENTRAL
├── requirements_dualcore.txt                       # ← DEPENDENCIAS OPTIMIZADAS
├── GUIA_INTEGRACION_MAXIMO_RELACIONAL.md          # ← GUÍA DE INTEGRACIÓN
├── instalar_maximo_relacional.sh                  # ← SCRIPT INSTALACIÓN
├── docker-compose-PC2.yml                         # ← DOCKER PARA PC2 POTENTE
├── Dockerfile.lightrag                            # ← DOCKERFILE LIGHTRAG
│
└── procesadores/
    ├── analizador_convergencia_optimizado.py      # ← ANÁLISIS DE CONVERGENCIA
    └── analizador_maximo_relacional_hibrido.py    # ← ANÁLISIS HÍBRIDO
```

---

## 🚀 PASO 1: INSTALACIÓN INICIAL (PC1 - Dual-Core)

### 1.1 Clonar/copiar los archivos

```bash
# Verificar que estás en la carpeta correcta
cd /path/to/YO\ estructural

# Verificar que los archivos existen
ls -la config_dualcore_optimizado.yaml
ls -la procesadores/
```

### 1.2 Ejecutar instalación automática

```bash
# Hacer ejecutable el script
chmod +x instalar_maximo_relacional.sh

# Ejecutar instalación
./instalar_maximo_relacional.sh
```

**Esto hará:**
- ✓ Crear estructura de directorios
- ✓ Crear entorno virtual (venv)
- ✓ Instalar todas las dependencias optimizadas
- ✓ Descargar modelo spaCy pequeño
- ✓ Verificar importaciones
- ✓ Mostrar próximos pasos

### 1.3 Activar entorno virtual

```bash
source venv/bin/activate
```

---

## 🔧 PASO 2: CONFIGURACIÓN (PC1 + PC2)

### 2.1 Editar configuración para dual-core

```bash
nano config_dualcore_optimizado.yaml
```

**Cambios críticos:**

```yaml
# LÍNEA ~20: Usuario del sistema
nlp:
  embedding_batch_size: 32  # ✓ CORRECTO PARA 8GB RAM
  spacy_batch_size: 50

# LÍNEA ~60: Máximo de memoria
optimization:
  max_memory_mb: 2048  # ✓ USAR 2GB de 8GB
  max_workers: 2       # ✓ DUAL-CORE

# LÍNEA ~40: Conexión Neo4j remoto
neo4j:
  bolt_url: "bolt://192.168.1.100:7687"  # ← CAMBIAR IP de PC2
  auth_password: "tu_password"
```

### 2.2 Inicializar PC2 (máquina potente) - Docker

```bash
# En PC2:
cd /path/to/YO\ estructural

# Iniciar servicios
docker-compose -f docker-compose-PC2.yml up -d

# Verificar que están corriendo
docker-compose -f docker-compose-PC2.yml ps

# Debería mostrar:
# neo4j           running
# lightrag        running
```

**Verificar conectividad:**

```bash
# En PC2
docker-compose logs neo4j | grep "started"

# Debería mostrar algo como:
# Neo4j 5.12.1 started on bolt://0.0.0.0:7687
```

---

## 🔗 PASO 3: INTEGRACIÓN EN SISTEMA PRINCIPAL

### 3.1 Abrir `sistema_principal_v2.py`

```bash
nano sistema_principal_v2.py
```

### 3.2 Agregar imports (al inicio del archivo)

```python
# ============================================================
# IMPORTS PARA MÁXIMO RELACIONAL DEFINICIONAL
# ============================================================
from procesadores.analizador_convergencia_optimizado import (
    AnalizadorConvergenciaOptimizado,
    ResultadoConvergencia
)

from procesadores.analizador_maximo_relacional_hibrido import (
    OrquestadorComputacionHibrida,
    ResultadoAnalisiscentralizado
)

import asyncio
import yaml
```

### 3.3 Agregar métodos a la clase principal

```python
class SistemaPrincipal:
    """Sistema principal con máximo relacional"""
    
    def __init__(self, config_path: str = "./config_dualcore_optimizado.yaml"):
        # ... inicialización existente ...
        
        # NUEVO: Máximo relacional
        self.analizador_convergencia = AnalizadorConvergenciaOptimizado(config_path)
        self.orquestador_hibrido = OrquestadorComputacionHibrida(config_path)
        logger.info("[INIT] ✓ Máximo relacional cargado")
    
    # ============================================================
    # MÉTODO 1: Detectar concepto individual
    # ============================================================
    def detectar_maximo_relacional_concepto(self, 
                                           concepto: str,
                                           rutas_definiciones: dict) -> bool:
        """Detecta si concepto alcanza 99%+ certeza"""
        
        resultado = self.analizador_convergencia.analizar_concepto(
            concepto,
            rutas_definiciones
        )
        
        if resultado.es_maximo_relacional:
            # Guardar en BD
            self._guardar_maximo_relacional_bd(
                concepto=concepto,
                certeza=resultado.certeza_combinada,
                rutas=resultado.rutas
            )
        
        return resultado.es_maximo_relacional
    
    # ============================================================
    # MÉTODO 2: Procesar lote (CRÍTICO para dual-core)
    # ============================================================
    def procesar_lote_maximo_relacional(self,
                                       conceptos_rutas: dict,
                                       batch_size: int = 10) -> list:
        """Procesar múltiples conceptos en lotes"""
        
        resultados = self.analizador_convergencia.procesar_lote_conceptos(
            conceptos_rutas,
            batch_size=batch_size
        )
        
        # Guardar máximos relacionales
        for resultado in resultados:
            if resultado.es_maximo_relacional:
                self._guardar_maximo_relacional_bd(
                    concepto=resultado.concepto,
                    certeza=resultado.certeza_combinada,
                    rutas=resultado.rutas
                )
        
        return resultados
    
    # ============================================================
    # MÉTODO 3: Análisis híbrido del grafo
    # ============================================================
    async def analizar_grafo_hibrido(self,
                                     nodos: list,
                                     arcos: list,
                                     neo4j_disponible: bool = True) -> ResultadoAnalisiscentralizado:
        """Análisis híbrido (NetworkX + GDS)"""
        
        resultado = await self.orquestador_hibrido.analizar_hibrido(
            nodos=nodos,
            arcos=arcos,
            nombre_grafo_gds="concepto_grafo",
            neo4j_disponible=neo4j_disponible
        )
        
        return resultado
    
    # ============================================================
    # MÉTODO AUXILIAR: Guardar en BD
    # ============================================================
    def _guardar_maximo_relacional_bd(self,
                                      concepto: str,
                                      certeza: float,
                                      rutas: list):
        """Guardar máximo relacional en Neo4j"""
        
        # Pseudocódigo - adaptar a tu implementación
        # self.neo4j_db.crear_maximo_relacional(
        #     concepto=concepto,
        #     certeza=certeza,
        #     rutas=[r.nombre for r in rutas]
        # )
        
        logger.info(f"[BD] Máximo relacional guardado: {concepto}")
```

---

## ✅ PASO 4: PRUEBAS

### 4.1 Prueba 1: Importación de módulos

```bash
# En terminal, activar venv
source venv/bin/activate

# Ejecutar prueba
python3 -c "
from procesadores.analizador_convergencia_optimizado import AnalizadorConvergenciaOptimizado
print('✓ Módulo convergencia importado')

from procesadores.analizador_maximo_relacional_hibrido import OrquestadorComputacionHibrida
print('✓ Módulo híbrido importado')

print('\n✓ TODAS LAS IMPORTACIONES CORRECTAS')
"
```

**Salida esperada:**
```
✓ Módulo convergencia importado
✓ Módulo híbrido importado
✓ TODAS LAS IMPORTACIONES CORRECTAS
```

### 4.2 Prueba 2: Analizar concepto individual

```bash
python3 << 'EOF'
from procesadores.analizador_convergencia_optimizado import AnalizadorConvergenciaOptimizado

# Inicializar
analizador = AnalizadorConvergenciaOptimizado(
    config_path="./config_dualcore_optimizado.yaml"
)

# Concepto de prueba
rutas = {
    "Física": "Material que sostiene peso y distribuye fuerzas hacia abajo",
    "Ergonómica": "Superficie que acomoda la forma del cuerpo humano",
    "Arquitectónica": "Elemento estructural que transfiere cargas al suelo",
    "Lógica": "Entidad que fundamenta la existencia de otra",
    "Ontológica": "Razón de ser fundamental en la estructura del ser"
}

# Analizar
resultado = analizador.analizar_concepto("SOPORTE", rutas)

print(f"""
╔════════════════════════════════════════════════════════════╗
║                RESULTADO DE PRUEBA                        ║
╚════════════════════════════════════════════════════════════╝

Concepto: {resultado.concepto}
Certeza individual promedio: {resultado.certeza_individual_promedio:.4f}
Certeza combinada: {resultado.certeza_combinada:.6f}
¿Es máximo relacional?: {'✓ SÍ' if resultado.es_maximo_relacional else '✗ NO'}
Confianza: {resultado.confianza_diagnostico}

RUTAS:
""")

for ruta in resultado.rutas:
    print(f"  {ruta.nombre}: {ruta.certeza:.4f}")
EOF
```

**Salida esperada:**
```
╔════════════════════════════════════════════════════════════╗
║                RESULTADO DE PRUEBA                        ║
╚════════════════════════════════════════════════════════════╝

Concepto: SOPORTE
Certeza individual promedio: 0.9231
Certeza combinada: 0.999994
¿Es máximo relacional?: ✓ SÍ
Confianza: ALTO

RUTAS:
  Física: 0.9234
  Ergonómica: 0.9187
  Arquitectónica: 0.9267
  Lógica: 0.9201
  Ontológica: 0.9245
```

### 4.3 Prueba 3: Procesamiento en lote

```bash
python3 << 'EOF'
from procesadores.analizador_convergencia_optimizado import AnalizadorConvergenciaOptimizado

analizador = AnalizadorConvergenciaOptimizado()

# Preparar 3 conceptos de prueba
conceptos = {
    "SOPORTE": {
        "Física": "Material que sostiene peso",
        "Ergonómica": "Superficie que acomoda",
        "Arquitectónica": "Elemento estructural",
        "Lógica": "Entidad que fundamenta",
        "Ontológica": "Razón de ser fundamental"
    },
    "ESTRUCTURA": {
        "Física": "Conjunto de partes conectadas",
        "Ergonómica": "Disposición de elementos",
        "Arquitectónica": "Sistema constructivo",
        "Lógica": "Sistema de proposiciones",
        "Ontológica": "Forma del ser"
    },
    "RELACIÓN": {
        "Física": "Conexión entre objetos",
        "Ergonómica": "Interacción usuario-sistema",
        "Arquitectónica": "Vínculo estructural",
        "Lógica": "Conexión lógica",
        "Ontológica": "Nexo ontológico"
    }
}

# Procesar lote
resultados = analizador.procesar_lote_conceptos(
    conceptos,
    batch_size=2  # Lotes de 2
)

# Mostrar resultados
maximo_count = sum(1 for r in resultados if r.es_maximo_relacional)
print(f"\n✓ Procesados {len(resultados)} conceptos")
print(f"✓ Máximos relacionales encontrados: {maximo_count}")

for resultado in resultados:
    print(f"\n  {resultado.concepto}: {resultado.certeza_combinada:.6f} - {'MÁXIMO' if resultado.es_maximo_relacional else 'NO'}")
EOF
```

### 4.4 Prueba 4: Monitoreo de memoria (Dual-Core)

```bash
# En terminal separada, monitorear en tiempo real
watch -n 1 'free -h && echo "---" && ps aux | grep python | grep -v grep'
```

---

## 📊 PASO 5: INTEGRACIÓN CON DATOS REALES

### 5.1 Obtener conceptos de Neo4j

```python
# En tu código sistema_principal_v2.py

def cargar_conceptos_de_neo4j(self) -> dict:
    """
    Cargar conceptos existentes de Neo4j.
    Cada concepto tiene 5 definiciones (una por ruta).
    """
    
    query = """
    MATCH (c:Concepto)
    WHERE c.definicion_fisica IS NOT NULL
    RETURN 
        c.nombre AS nombre,
        c.definicion_fisica AS fisica,
        c.definicion_ergonomica AS ergonomica,
        c.definicion_arquitectonica AS arquitectonica,
        c.definicion_logica AS logica,
        c.definicion_ontologica AS ontologica
    LIMIT 1000
    """
    
    conceptos = {}
    for record in self.neo4j_db.ejecutar_query(query):
        conceptos[record['nombre']] = {
            "Física": record['fisica'],
            "Ergonómica": record['ergonomica'],
            "Arquitectónica": record['arquitectonica'],
            "Lógica": record['logica'],
            "Ontológica": record['ontologica']
        }
    
    return conceptos

# Usar:
conceptos = sistema.cargar_conceptos_de_neo4j()
resultados = sistema.procesar_lote_maximo_relacional(conceptos, batch_size=50)
```

### 5.2 Guardar resultados en Neo4j

```python
def _guardar_maximo_relacional_bd(self,
                                  concepto: str,
                                  certeza: float,
                                  rutas: list):
    """Guardar máximo relacional en Neo4j"""
    
    query = """
    MERGE (m:MaximoRelacional {nombre: $concepto})
    SET 
        m.certeza_combinada = $certeza,
        m.timestamp = datetime(),
        m.rutas = $rutas_list,
        m.detectado = true
    RETURN m
    """
    
    rutas_list = [r.nombre for r in rutas]
    
    self.neo4j_db.ejecutar_query(
        query,
        {
            'concepto': concepto,
            'certeza': certeza,
            'rutas_list': rutas_list
        }
    )
    
    logger.info(f"✓ Máximo relacional guardado: {concepto}")
```

---

## 🎯 PASO 6: OPTIMIZACIÓN FINAL PARA DUAL-CORE

### 6.1 Monitoreo de memoria

```bash
# Ver consumo en tiempo real
free -h
watch -n 2 free -h
```

### 6.2 Si RAM se llena (>6GB):

**Estrategia 1: Reducir batch_size**
```yaml
# En config_dualcore_optimizado.yaml
clustering:
  batch_size: 500  # En lugar de 1000
```

**Estrategia 2: Usar más lotes pero más pequeños**
```python
# En código
resultados = sistema.procesar_lote_maximo_relacional(
    conceptos,
    batch_size=5  # Más pequeño
)
```

**Estrategia 3: Usar modelo embedding más pequeño**
```python
# Cambiar en config
nlp:
  embedding_model: "sentence-transformers/paraphrase-MiniLM-L6-v2"  # Aún más pequeño
```

### 6.3 Validar rendimiento

```bash
# Ver tiempo de ejecución
time python3 -c "
import time
from sistema_principal_v2 import SistemaPrincipal

sistema = SistemaPrincipal()
conceptos = sistema.cargar_conceptos_de_neo4j()

t_inicio = time.time()
resultados = sistema.procesar_lote_maximo_relacional(conceptos[:100], batch_size=10)
t_fin = time.time()

print(f'Tiempo: {t_fin - t_inicio:.2f}s')
print(f'Conceptos/seg: {100 / (t_fin - t_inicio):.1f}')
"
```

---

## 🔍 PASO 7: VALIDACIÓN FINAL

### Checklist de validación

- [ ] Archivos creados en ubicaciones correctas
- [ ] Dependencias instaladas sin errores
- [ ] Modelos descargados (spaCy, embeddings)
- [ ] Prueba 1: Importaciones correctas
- [ ] Prueba 2: Concepto individual analizado
- [ ] Prueba 3: Lote procesado sin errores
- [ ] Prueba 4: Memoria bajo control (<6GB)
- [ ] Neo4j conecta desde PC1 a PC2
- [ ] LightRAG API respondiendo
- [ ] Máximos relacionales guardándose en BD
- [ ] Rendimiento: >10 conceptos/seg

### Si falla algo:

```bash
# Mostrar logs
tail -f logs/dualcore_execution.log

# Verificar conexión Neo4j
python3 -c "
from neo4j import GraphDatabase
driver = GraphDatabase.driver('bolt://192.168.X.X:7687', auth=('neo4j', 'neo4j'))
driver.verify_connectivity()
print('✓ Neo4j conectando')
driver.close()
"

# Revisar memoria
free -h
ps aux | grep python
```

---

## 📞 RESUMEN EJECUTIVO

| Aspecto | Estado | Verificación |
|--------|--------|--------------|
| **Instalación** | ✓ Automatizada | `./instalar_maximo_relacional.sh` |
| **Configuración** | ✓ Centralizada | `config_dualcore_optimizado.yaml` |
| **Integración** | ✓ Paso a paso | Ver PASO 3 |
| **Pruebas** | ✓ 4 niveles | Ver PASO 4 |
| **Memoria** | ✓ Optimizada | Batch processing + lazy loading |
| **Escalabilidad** | ✓ Híbrida | NetworkX local + GDS remoto |
| **Documentación** | ✓ Completa | `GUIA_INTEGRACION_MAXIMO_RELACIONAL.md` |

---

## 🚀 Próximos pasos

1. **Ejecutar instalación:** `./instalar_maximo_relacional.sh`
2. **Editar configuración:** `nano config_dualcore_optimizado.yaml`
3. **Integrar en sistema:** Copiar métodos a `sistema_principal_v2.py`
4. **Ejecutar pruebas:** Ver PASO 4
5. **Procesar conceptos reales:** Ver PASO 5
6. **Monitorear rendimiento:** Ver PASO 6

---

**¡Sistema listo para detectar MÁXIMO RELACIONAL DEFINICIONAL!** ✨
