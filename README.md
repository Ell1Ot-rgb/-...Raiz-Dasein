# Raiz Dasein
C:\Users\Public\#...Raíz Dasein\YO estructural>py verificar.py
🧠 SISTEMA YO ESTRUCTURAL - EJECUCIÓN COMPLETA CON DIAGNÓSTICOS
================================================================================
2025-10-30 11:57:01,192 [INFO] DiagnosticadorSistema: Iniciando diagnóstico completo del sistema - 20251030_115701

1. Verificando prerequisitos...
2025-10-30 11:57:01,197 [INFO] DiagnosticadorSistema: === VERIFICACIÓN DE PREREQUISITOS ===
2025-10-30 11:57:01,199 [INFO] DiagnosticadorSistema: ✓ Directorio entrada_bruta existe
2025-10-30 11:57:01,201 [INFO] DiagnosticadorSistema: ✓ Directorio procesado existe
2025-10-30 11:57:01,212 [INFO] DiagnosticadorSistema: ✓ Directorio logs_sistema existe
2025-10-30 11:57:01,213 [INFO] DiagnosticadorSistema: ✓ Directorio configuracion existe
2025-10-30 11:57:01,215 [INFO] DiagnosticadorSistema: ✓ Archivo de configuración encontrado
2025-10-30 11:57:01,218 [INFO] DiagnosticadorSistema: ✓ Encontrados 44 archivos de texto en entrada_bruta
✅ Prerequisitos verificados

2. Ejecutando verificación completa del sistema...
2025-10-30 11:57:01,227 [INFO] DiagnosticadorSistema: === VERIFICACIÓN COMPLETA DEL SISTEMA ===
2025-10-30 11:57:01,234 [INFO] DiagnosticadorSistema: ✓ Verificación del sistema completada exitosamente
✅ Verificación del sistema completada

3. Ejecutando sistema fenomenológico principal...
2025-10-30 11:57:01,241 [INFO] DiagnosticadorSistema: === EJECUCIÓN DEL SISTEMA PRINCIPAL ===
2025-10-30 11:57:01,345 [DEBUG] neo4j.pool: [#0000]  _: <POOL> created, direct address IPv4Address(('192.168.1.37', 7687))
2025-10-30 11:57:01,347 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: yo_estructural
2025-10-30 11:57:01,351 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> pinning database: 'yo_estructural'
2025-10-30 11:57:01,353 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name='yo_estructural', guessed=False)
2025-10-30 11:57:01,355 [DEBUG] neo4j.pool: [#0000]  _: <POOL> trying to hand out new connection
2025-10-30 11:57:01,356 [DEBUG] neo4j.io: [#0000]  _: <RESOLVE> in: 192.168.1.37:7687
2025-10-30 11:57:01,378 [DEBUG] neo4j.io: [#0000]  _: <RESOLVE> dns resolver out: 192.168.1.37:7687
2025-10-30 11:57:01,379 [DEBUG] neo4j.io: [#0000]  C: <OPEN> 192.168.1.37:7687
2025-10-30 11:57:01,384 [DEBUG] neo4j.io: [#DB1C]  C: <MAGIC> 0x6060B017
2025-10-30 11:57:01,386 [DEBUG] neo4j.io: [#DB1C]  C: <HANDSHAKE> 0x000001FF 0x00080805 0x00020404 0x00000003
2025-10-30 11:57:01,433 [DEBUG] neo4j.io: [#DB1C]  S: <HANDSHAKE> 0x00000305
2025-10-30 11:57:01,435 [DEBUG] neo4j.io: [#DB1C]  C: HELLO {'user_agent': 'neo4j-python/6.0.2 Python/3.14.0-final-0 (win32)', 'bolt_agent': {'product': 'neo4j-python/6.0.2', 'platform': 'Windows 10; AMD64', 'language': 'Python/3.14.0-final-0', 'language_details': 'CPython; 3.14.0-final-0 (tags/v3.14.0:ebf955d, Oct  7 2025 10:15:03) [MSC v.1944 64 bit (AMD64)]'}}
2025-10-30 11:57:01,437 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> client state: CONNECTED > AUTHENTICATION
2025-10-30 11:57:01,439 [DEBUG] neo4j.io: [#DB1C]  C: LOGON {'scheme': 'basic', 'principal': 'neo4j', 'credentials': '*******'}
2025-10-30 11:57:01,622 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> client state: AUTHENTICATION > READY
2025-10-30 11:57:01,654 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'server': 'Neo4j/5.12.0', 'connection_id': 'bolt-27', 'hints': {'connection.recv_timeout_seconds': 120}}
2025-10-30 11:57:01,661 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: CONNECTED > AUTHENTICATION
2025-10-30 11:57:01,707 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {}
2025-10-30 11:57:01,709 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: AUTHENTICATION > READY
2025-10-30 11:57:01,716 [DEBUG] neo4j.io: [#DB1C]  C: RUN 'RETURN 1 AS num' {} {'db': 'yo_estructural'}
2025-10-30 11:57:01,717 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> client state: READY > STREAMING
2025-10-30 11:57:01,719 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:01,743 [DEBUG] neo4j.io: [#DB1C]  S: FAILURE {'code': 'Neo.ClientError.Database.DatabaseNotFound', 'message': "Database does not exist. Database name: 'yo_estructural'."}
2025-10-30 11:57:01,763 [DEBUG] neo4j.io: [#DB1C]  C: RESET
2025-10-30 11:57:01,766 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> client state: STREAMING > READY
2025-10-30 11:57:01,777 [DEBUG] neo4j.io: [#DB1C]  S: IGNORED
2025-10-30 11:57:01,778 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {}
2025-10-30 11:57:01,780 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: FAILED > READY
2025-10-30 11:57:01,781 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:01,783 [ERROR] Neo4jConnection: Error al verificar conexión a Neo4j: {neo4j_code: Neo.ClientError.Database.DatabaseNotFound} {message: Database does not exist. Database name: 'yo_estructural'.} {gql_status: 50N42} {gql_status_description: error: general processing exception - unexpected error. Database does not exist. Database name: 'yo_estructural'.}
2025-10-30 11:57:01,791 [INFO] Neo4jConnection: Conexión a Neo4j establecida exitosamente: bolt://192.168.1.37:7687
2025-10-30 11:57:01,906 [INFO] SistemaFenomenologico: Sistema inicializado con configuración cargada
2025-10-30 11:57:01,908 [INFO] DiagnosticadorSistema: Sistema inicializado correctamente
[11:57:01.909] [DIAGNÓSTICO-INFO] Iniciando flujo completo del sistema
2025-10-30 11:57:01,911 [INFO] SistemaFenomenologico: Iniciando flujo completo del sistema
🚀 Iniciando Sistema Fenomenológico v2.2
📖 Procesando textos fenomenológicos...
🔸 Generando preinstancias...
[11:57:02.239] [DIAGNÓSTICO-INFO] Generadas 126 preinstancias desde análisis
2025-10-30 11:57:02,240 [INFO] SistemaFenomenologico: Generadas 126 preinstancias desde análisis
[11:57:02.241] [DIAGNÓSTICO-INFO] Generadas 126 preinstancias
2025-10-30 11:57:02,243 [INFO] SistemaFenomenologico: Generadas 126 preinstancias
🔹 Creando instancias de existencia...
[11:57:02.251] [DIAGNÓSTICO-INFO] Creadas 126 instancias de existencia
2025-10-30 11:57:02,252 [INFO] SistemaFenomenologico: Creadas 126 instancias de existencia
[11:57:02.258] [DIAGNÓSTICO-INFO] Creadas 126 instancias de existencia
2025-10-30 11:57:02,259 [INFO] SistemaFenomenologico: Creadas 126 instancias de existencia
[11:57:02.260] [DIAGNÓSTICO-INFO] Evaluando necesidad de activación MDCE
2025-10-30 11:57:02,261 [INFO] SistemaFenomenologico: Evaluando necesidad de activación MDCE
[11:57:02.263] [DIAGNÓSTICO-INFO] Analizando contradicciones de 4º orden
2025-10-30 11:57:02,264 [INFO] SistemaFenomenologico: Analizando contradicciones de 4º orden
[11:57:02.285] [DIAGNÓSTICO-INFO] No se detectaron contradicciones de 4º orden
2025-10-30 11:57:02,285 [INFO] SistemaFenomenologico: No se detectaron contradicciones de 4º orden
📊 Calculando gradientes relacionales...
[11:57:02.292] [DIAGNÓSTICO-INFO] Calculando gradientes para 126 instancias
2025-10-30 11:57:02,304 [INFO] SistemaFenomenologico: Calculando gradientes para 126 instancias
[11:57:02.414] [DIAGNÓSTICO-INFO] Gradientes relacionales calculados exitosamente
2025-10-30 11:57:02,414 [INFO] SistemaFenomenologico: Gradientes relacionales calculados exitosamente
🔗 Detectando vohexistencias...
[11:57:02.418] [DIAGNÓSTICO-INFO] Iniciando detección de vohexistencias para 126 instancias
2025-10-30 11:57:02,421 [INFO] SistemaFenomenologico: Iniciando detección de vohexistencias para 126 instancias
[11:57:02.588] [DIAGNÓSTICO-INFO] Detectadas 0 vohexistencias
2025-10-30 11:57:02,590 [INFO] SistemaFenomenologico: Detectadas 0 vohexistencias
🧠 Evaluando emergencia del YO...
2025-10-30 11:57:02,615 [DEBUG] SistemaFenomenologico: Extraídos 126 contextos activos con claves convertidas a strings
2025-10-30 11:57:02,622 [DEBUG] SistemaFenomenologico: Extraídos 126 fenómenos activos con claves convertidas a strings
2025-10-30 11:57:02,668 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:02,670 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> pinning database: None
2025-10-30 11:57:02,672 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:02,674 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:02,675 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:02,676 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:02,680 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                        MERGE (y:YO {id: $id})\n                        SET y.tipo = $tipo,\n                            y.activacion = $activacion,\n                            y.timestamp = $timestamp,\n                            y.version = $version,\n                            y.coherencia_narrativa = $coherencia_narrativa,\n                            y.estabilidad_contextual = $estabilidad_contextual,\n                            y.integracion_afectiva = $integracion_afectiva\n                    ' {'id': 'yo_0', 'tipo': 'PROTO_YO', 'activacion': 1.0, 'timestamp': '2025-10-30T11:57:02.642985', 'version': 0, 'coherencia_narrativa': 0.0, 'estabilidad_contextual': 0.0, 'integracion_afectiva': 0.5, 'coherencia_total': 0.0} {}
2025-10-30 11:57:02,681 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> client state: READY > STREAMING
2025-10-30 11:57:02,683 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:04,498 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 1801, 'fields': []}
2025-10-30 11:57:04,499 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:04,503 [INFO] SistemaYoEmergente: Nodo YO v0 sincronizado con Neo4j
2025-10-30 11:57:04,586 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBWpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'nodes-created': 1, 'properties-set': 8}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:04,587 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:04,590 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:04,591 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:04,592 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:04,593 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:04,594 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:04,598 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:04,600 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1a5544df', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBWpA=']}
2025-10-30 11:57:04,609 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:05,443 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 826, 'fields': []}
2025-10-30 11:57:05,444 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:05,611 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBW5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:05,612 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:05,614 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:05,616 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:05,616 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:05,620 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:05,621 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:05,622 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:05,627 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ca8ebf5d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBW5A=']}
2025-10-30 11:57:05,636 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:05,657 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 18, 'fields': []}
2025-10-30 11:57:05,658 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:05,710 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBXJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:05,711 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:05,715 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:05,716 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:05,717 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:05,718 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:05,719 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:05,719 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:05,721 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3e0bedfe', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBXJA=']}
2025-10-30 11:57:05,722 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:05,733 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:05,733 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:05,782 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBXZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:05,798 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:05,800 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:05,801 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:05,803 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:05,804 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:05,805 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:05,809 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:05,811 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6ef62480', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBXZA=']}
2025-10-30 11:57:05,812 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:05,822 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:05,822 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:05,878 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBXpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:05,879 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:05,883 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:05,884 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:05,886 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:05,887 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:05,891 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:05,892 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:05,910 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5fdb4646', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBXpA=']}
2025-10-30 11:57:05,915 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:05,925 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:05,932 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,004 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBX5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,004 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,009 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,011 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,012 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,014 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,015 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,016 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,022 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a649d13c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBX5A=']}
2025-10-30 11:57:06,025 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,033 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:06,034 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,082 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBYJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,085 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,087 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,092 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,093 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,095 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,097 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,097 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,104 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_94908ba1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBYJA=']}
2025-10-30 11:57:06,106 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,115 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:06,115 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,206 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBYZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,209 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,210 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,212 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,212 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,214 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,216 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,216 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,220 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8c563a97', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBYZA=']}
2025-10-30 11:57:06,221 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,235 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:06,235 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,329 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBYpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,332 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,339 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,340 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,341 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,342 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,344 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,345 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,346 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_0f50dc4e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBYpA=']}
2025-10-30 11:57:06,349 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,368 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:06,373 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,417 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBY5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,424 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,425 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,426 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,427 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,428 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,433 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,433 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,435 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5c2eaa92', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBY5A=']}
2025-10-30 11:57:06,436 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,447 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:06,448 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,492 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,496 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,498 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,502 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,509 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,516 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,517 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,518 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,519 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_490cb68d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZJA=']}
2025-10-30 11:57:06,520 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,551 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 26, 'fields': []}
2025-10-30 11:57:06,551 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,602 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,603 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,612 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,614 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,616 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,620 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,623 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,625 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,626 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a8a9dcfd', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZZA=']}
2025-10-30 11:57:06,628 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,645 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:06,645 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,697 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,698 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,702 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,704 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,704 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,705 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,706 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,707 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,709 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_da3870af', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZpA=']}
2025-10-30 11:57:06,710 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,719 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:06,719 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,805 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZ5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,806 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,816 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,821 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,822 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,826 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,832 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,837 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,863 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_64a4db11', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBZ5A=']}
2025-10-30 11:57:06,869 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,883 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:06,884 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:06,934 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBaJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:06,935 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:06,939 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:06,940 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:06,941 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:06,942 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:06,942 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:06,943 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:06,945 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b9404783', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBaJA=']}
2025-10-30 11:57:06,946 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:06,960 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:06,962 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,012 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBaZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,013 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,016 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,021 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,023 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,036 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,037 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,038 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,039 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b10e8b9a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBaZA=']}
2025-10-30 11:57:07,040 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,052 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:07,057 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,107 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBapA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,108 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,110 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,112 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,115 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,115 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,116 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,117 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,119 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_e367f159', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBapA=']}
2025-10-30 11:57:07,120 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,129 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:07,129 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,171 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBa5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,175 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,176 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,177 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,179 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,180 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,181 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,184 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,186 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3da9414e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBa5A=']}
2025-10-30 11:57:07,189 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,203 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:07,203 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,249 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBbJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,250 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,255 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,259 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,259 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,260 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,261 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,262 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,264 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6f69981d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBbJA=']}
2025-10-30 11:57:07,269 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,279 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:07,280 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,384 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBbZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,385 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,388 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,389 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,390 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,391 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,393 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,403 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,412 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6888362b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBbZA=']}
2025-10-30 11:57:07,425 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,451 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 10, 'fields': []}
2025-10-30 11:57:07,452 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,503 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBbpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,504 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,507 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,508 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,509 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,510 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,515 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,515 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,517 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6e8e35e4', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBbpA=']}
2025-10-30 11:57:07,521 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,544 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 11, 'fields': []}
2025-10-30 11:57:07,545 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,599 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBb5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,600 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,602 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,604 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,605 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,608 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,610 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,611 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,613 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d320c9fc', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBb5A=']}
2025-10-30 11:57:07,620 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,639 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:07,639 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,697 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBcJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,697 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,702 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,704 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,706 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,707 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,710 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,714 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,716 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9c603674', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBcJA=']}
2025-10-30 11:57:07,717 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,727 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:07,730 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,773 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBcZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,774 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,780 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,784 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,787 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,788 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,801 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,803 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,804 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_14483803', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBcZA=']}
2025-10-30 11:57:07,810 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,821 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:07,821 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,868 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBcpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,869 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,872 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,873 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,878 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,879 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,880 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,880 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,891 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c0936ee6', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBcpA=']}
2025-10-30 11:57:07,894 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:07,912 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 11, 'fields': []}
2025-10-30 11:57:07,922 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:07,967 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBc5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:07,974 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:07,977 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:07,979 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:07,981 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:07,987 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:07,988 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:07,989 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:07,991 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6f810470', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBc5A=']}
2025-10-30 11:57:07,993 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,011 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:08,011 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,103 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBdJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,104 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,106 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,108 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,109 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,110 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,113 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,114 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,115 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_bbb805c6', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBdJA=']}
2025-10-30 11:57:08,122 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,139 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 10, 'fields': []}
2025-10-30 11:57:08,139 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,186 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBdZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,186 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,190 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,191 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,194 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,198 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,200 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,201 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,208 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_e6ec60ba', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBdZA=']}
2025-10-30 11:57:08,210 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,228 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 10, 'fields': []}
2025-10-30 11:57:08,235 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,277 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBdpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,281 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,282 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,283 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,284 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,285 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,286 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,289 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,291 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6728f0ac', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBdpA=']}
2025-10-30 11:57:08,294 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,305 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:08,306 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,362 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBd5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,363 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,366 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,367 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,368 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,369 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,372 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,374 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,375 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7cbc0996', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBd5A=']}
2025-10-30 11:57:08,378 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,387 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:08,388 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,434 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBeJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,435 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,438 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,439 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,441 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,444 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,446 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,447 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,450 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_fd572082', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBeJA=']}
2025-10-30 11:57:08,456 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,491 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 11, 'fields': []}
2025-10-30 11:57:08,498 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,520 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBeZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,521 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,527 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,530 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,533 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,538 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,540 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,542 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,544 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_74e22928', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBeZA=']}
2025-10-30 11:57:08,550 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,564 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:08,565 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,659 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBepA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,659 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,662 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,666 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,667 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,668 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,673 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,674 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,680 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_27503275', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBepA=']}
2025-10-30 11:57:08,683 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,694 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:08,694 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:08,921 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBe5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:08,927 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:08,930 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:08,931 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:08,932 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:08,933 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:08,938 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:08,940 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:08,941 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9caa679e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBe5A=']}
2025-10-30 11:57:08,944 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:08,954 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:08,955 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,000 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBfJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,001 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,003 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,007 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,008 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,010 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,013 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,015 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,037 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_072c2fba', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBfJA=']}
2025-10-30 11:57:09,061 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,074 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:09,076 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,131 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBfZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,132 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,135 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,135 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,138 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,139 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,140 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,141 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,142 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5ec1a3c9', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBfZA=']}
2025-10-30 11:57:09,143 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,152 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:09,152 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,207 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBfpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,208 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,210 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,211 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,213 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,214 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,215 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,216 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,217 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5773da8c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBfpA=']}
2025-10-30 11:57:09,223 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,249 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 11, 'fields': []}
2025-10-30 11:57:09,250 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,298 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBf5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,300 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,305 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,306 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,307 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,308 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,309 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,310 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,315 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ac4fa241', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBf5A=']}
2025-10-30 11:57:09,317 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,344 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:09,344 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,434 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBgJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,435 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,438 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,439 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,446 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,447 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,449 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,467 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,471 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b4348eb9', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBgJA=']}
2025-10-30 11:57:09,479 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,489 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:09,490 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,533 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBgZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,534 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,540 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,541 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,542 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,543 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,544 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,545 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,551 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_29006d34', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBgZA=']}
2025-10-30 11:57:09,554 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,574 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:09,598 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,613 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBgpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,614 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,615 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,619 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,620 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,621 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,624 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,626 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,627 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5b2f4651', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBgpA=']}
2025-10-30 11:57:09,633 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,650 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 10, 'fields': []}
2025-10-30 11:57:09,650 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,692 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBg5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,693 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,696 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,696 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,698 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,700 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,701 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,703 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,704 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_aab3a550', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBg5A=']}
2025-10-30 11:57:09,707 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,729 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 13, 'fields': []}
2025-10-30 11:57:09,730 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,772 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBhJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,773 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,777 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,778 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,779 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,781 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,785 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,786 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,790 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b65a4016', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBhJA=']}
2025-10-30 11:57:09,802 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,815 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:09,816 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,865 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBhZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,866 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,869 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,870 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,871 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,872 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,874 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,874 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,877 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4393cbcd', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBhZA=']}
2025-10-30 11:57:09,879 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:09,887 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:09,892 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:09,967 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBhpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:09,978 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:09,979 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:09,980 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:09,984 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:09,985 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:09,986 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:09,989 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:09,991 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4bdec510', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBhpA=']}
2025-10-30 11:57:09,999 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,012 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:10,012 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:10,056 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBh5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:10,057 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:10,059 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:10,061 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:10,062 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:10,063 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:10,066 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:10,067 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:10,069 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a7042cf7', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBh5A=']}
2025-10-30 11:57:10,079 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,094 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 10, 'fields': []}
2025-10-30 11:57:10,097 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:10,149 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBiJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:10,150 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:10,152 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:10,154 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:10,155 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:10,156 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:10,160 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:10,160 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:10,162 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f1120c02', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBiJA=']}
2025-10-30 11:57:10,168 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,187 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 10, 'fields': []}
2025-10-30 11:57:10,188 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:10,230 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBiZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:10,231 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:10,236 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:10,237 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:10,238 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:10,239 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:10,240 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:10,242 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:10,246 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d3a960b1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBiZA=']}
2025-10-30 11:57:10,257 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,272 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:10,273 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:10,588 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBipA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:10,589 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:10,591 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:10,595 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:10,596 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:10,597 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:10,600 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:10,602 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:10,604 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f33ff624', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBipA=']}
2025-10-30 11:57:10,611 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,623 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:10,624 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:10,673 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBi5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:10,678 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:10,680 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:10,681 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:10,683 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:10,684 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:10,685 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:10,689 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:10,692 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f2a5b15d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBi5A=']}
2025-10-30 11:57:10,694 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,704 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:10,704 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:10,787 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBjJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:10,788 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:10,791 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:10,795 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:10,797 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:10,798 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:10,799 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:10,812 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:10,813 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_46b4b89b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBjJA=']}
2025-10-30 11:57:10,815 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,826 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:10,827 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:10,925 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBjZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:10,925 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:10,930 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:10,931 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:10,932 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:10,934 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:10,938 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:10,940 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:10,941 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8970d81c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBjZA=']}
2025-10-30 11:57:10,956 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:10,979 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:10,990 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,055 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBjpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,056 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,059 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,060 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,062 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,065 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,066 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,067 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,073 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9c756c42', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBjpA=']}
2025-10-30 11:57:11,076 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,095 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 11, 'fields': []}
2025-10-30 11:57:11,096 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,147 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBj5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,148 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,150 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,152 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,153 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,154 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,155 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,156 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,159 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f711da9d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBj5A=']}
2025-10-30 11:57:11,161 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,170 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:11,172 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,225 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBkJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,226 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,230 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,231 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,232 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,233 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,234 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,235 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,236 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_93c2483b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBkJA=']}
2025-10-30 11:57:11,237 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,247 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:11,247 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,302 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBkZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,303 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,305 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,307 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,307 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,309 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,311 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,313 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,314 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_0b1ba81e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBkZA=']}
2025-10-30 11:57:11,315 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,332 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:11,333 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,381 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBkpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,383 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,387 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,388 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,389 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,390 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,391 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,395 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,396 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9142a93a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBkpA=']}
2025-10-30 11:57:11,398 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,411 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:11,412 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,502 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBk5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,503 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,506 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,507 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,508 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,509 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,512 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,513 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,515 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7b3551be', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBk5A=']}
2025-10-30 11:57:11,518 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,526 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:11,527 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,582 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBlJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,583 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,585 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,587 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,587 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,589 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,590 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,591 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,595 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_16f2f3b1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBlJA=']}
2025-10-30 11:57:11,596 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,607 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:11,608 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,653 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBlZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,654 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,657 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,659 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,660 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,661 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,662 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,665 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,668 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_be5f6195', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBlZA=']}
2025-10-30 11:57:11,672 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,683 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:11,689 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,738 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBlpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,741 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,749 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,753 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,754 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,759 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,760 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,761 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,766 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_499c79cf', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBlpA=']}
2025-10-30 11:57:11,768 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,785 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:11,786 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,841 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBl5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,842 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,844 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,846 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,846 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,848 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,849 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,849 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,853 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_eae14cfd', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBl5A=']}
2025-10-30 11:57:11,855 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,864 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:11,870 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:11,925 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBmJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:11,925 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:11,928 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:11,929 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:11,930 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:11,931 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:11,932 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:11,935 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:11,940 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8000e45d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBmJA=']}
2025-10-30 11:57:11,954 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:11,967 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:11,967 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,079 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBmZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,081 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,084 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:12,088 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:12,089 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:12,091 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:12,095 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:12,106 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:12,107 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7eca164b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBmZA=']}
2025-10-30 11:57:12,108 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:12,124 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:12,125 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,178 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBmpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,178 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,182 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:12,184 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:12,185 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:12,186 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:12,187 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:12,187 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:12,190 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d8b6264b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBmpA=']}
2025-10-30 11:57:12,195 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:12,202 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:12,203 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,254 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBm5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,269 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,271 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:12,276 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:12,278 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:12,282 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:12,285 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:12,291 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:12,292 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7bce724b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBm5A=']}
2025-10-30 11:57:12,294 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:12,312 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:12,312 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,361 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBnJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,362 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,365 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:12,367 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:12,369 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:12,372 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:12,374 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:12,375 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:12,391 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4793eb94', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBnJA=']}
2025-10-30 11:57:12,396 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:12,405 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:12,418 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,456 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBnZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,504 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,508 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:12,512 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:12,515 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:12,517 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:12,518 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:12,533 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:12,538 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8fe83ecb', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBnZA=']}
2025-10-30 11:57:12,560 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:12,571 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:12,574 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,663 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBnpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,666 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,668 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:12,669 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:12,670 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:12,672 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:12,673 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:12,675 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:12,682 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_aca1f831', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBnpA=']}
2025-10-30 11:57:12,690 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:12,710 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:12,713 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,758 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBn5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,759 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,763 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:12,765 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:12,776 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:12,779 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:12,779 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:12,781 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:12,786 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_54200f42', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBn5A=']}
2025-10-30 11:57:12,787 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:12,798 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:12,798 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:12,851 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBoJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:12,853 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:12,943 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,002 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,021 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,032 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,047 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,060 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,073 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a8f1f060', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBoJA=']}
2025-10-30 11:57:13,079 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,089 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:13,100 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,200 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBoZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,201 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,205 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,206 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,207 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,208 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,209 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,210 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,212 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9fd8df73', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBoZA=']}
2025-10-30 11:57:13,214 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,223 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:13,223 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,307 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBopA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,308 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,313 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,315 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,316 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,317 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,319 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,320 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,326 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3db6ac02', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBopA=']}
2025-10-30 11:57:13,328 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,336 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:13,337 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,440 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBo5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,441 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,443 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,445 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,446 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,448 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,448 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,450 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,453 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1c420cb6', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBo5A=']}
2025-10-30 11:57:13,455 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,464 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:13,479 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,513 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBpJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,527 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,529 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,530 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,531 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,535 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,537 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,538 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,541 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8409d0d1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBpJA=']}
2025-10-30 11:57:13,548 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,560 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:13,563 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,608 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBpZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,609 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,611 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,614 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,614 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,617 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,619 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,620 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,624 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4873c9a1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBpZA=']}
2025-10-30 11:57:13,630 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,646 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:13,647 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,703 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBppA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,703 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,707 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,713 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,715 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,717 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,719 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,724 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,726 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_79a8849b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBppA=']}
2025-10-30 11:57:13,731 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,743 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:13,744 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,796 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBp5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,797 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,799 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,801 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,802 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,803 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,807 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,808 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,809 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d683c928', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBp5A=']}
2025-10-30 11:57:13,821 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:13,835 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:13,836 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:13,889 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBqJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:13,890 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:13,904 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:13,927 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:13,931 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:13,942 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:13,953 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:13,957 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:13,964 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c563d3f2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBqJA=']}
2025-10-30 11:57:13,966 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:14,020 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:14,021 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:14,121 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBqZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:14,124 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:14,126 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:14,127 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:14,131 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:14,137 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:14,140 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:14,143 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:14,144 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4a8b6b0e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBqZA=']}
2025-10-30 11:57:14,152 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:14,172 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:14,176 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:14,218 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBqpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:14,223 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:14,224 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:14,226 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:14,227 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:14,235 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:14,241 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:14,243 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:14,245 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b62c7e25', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBqpA=']}
2025-10-30 11:57:14,247 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:14,269 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:14,269 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:14,664 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBq5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:14,665 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:14,668 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:14,669 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:14,670 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:14,671 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:14,672 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:14,676 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:14,678 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8b7d204e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBq5A=']}
2025-10-30 11:57:14,679 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:14,688 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:14,689 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:14,748 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBrJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:14,749 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:14,752 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:14,753 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:14,755 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:14,759 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:14,760 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:14,761 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:14,764 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_577e4de9', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBrJA=']}
2025-10-30 11:57:14,766 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:14,781 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:14,783 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:14,864 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBrZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:14,865 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:14,904 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:14,913 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:14,918 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:14,920 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:14,920 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:14,925 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:14,938 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c4dfa53b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBrZA=']}
2025-10-30 11:57:14,940 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:14,952 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:14,955 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:15,048 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBrpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:15,049 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:15,066 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:15,066 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:15,067 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:15,068 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:15,069 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:15,070 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:15,071 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_488385b1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBrpA=']}
2025-10-30 11:57:15,078 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:15,242 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 158, 'fields': []}
2025-10-30 11:57:15,242 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:15,295 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBr5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:15,296 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:15,303 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:15,304 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:15,305 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:15,306 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:15,307 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:15,307 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:15,313 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d4cbb836', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBr5A=']}
2025-10-30 11:57:15,315 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:15,336 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 17, 'fields': []}
2025-10-30 11:57:15,337 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:15,426 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBsJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:15,426 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:15,430 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:15,432 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:15,432 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:15,434 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:15,434 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:15,435 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:15,437 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_2d624729', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBsJA=']}
2025-10-30 11:57:15,442 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:15,455 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:15,468 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:15,604 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBsZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:15,605 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:15,607 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:15,609 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:15,609 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:15,610 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:15,612 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:15,614 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:15,617 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_968e54ed', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBsZA=']}
2025-10-30 11:57:15,619 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:15,640 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 13, 'fields': []}
2025-10-30 11:57:15,642 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:15,692 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBspA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:15,693 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:15,696 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:15,699 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:15,701 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:15,702 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:15,705 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:15,706 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:15,712 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_30c55234', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBspA=']}
2025-10-30 11:57:15,718 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:15,731 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:15,731 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:15,907 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBs5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:15,908 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:15,912 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:15,913 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:15,914 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:15,915 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:15,916 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:15,917 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:15,918 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c2cd5283', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBs5A=']}
2025-10-30 11:57:15,919 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:15,937 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 12, 'fields': []}
2025-10-30 11:57:15,937 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:16,093 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBtJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:16,120 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:16,124 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:16,126 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:16,127 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:16,130 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:16,142 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:16,147 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:16,152 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d0416f7c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBtJA=']}
2025-10-30 11:57:16,157 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:16,169 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:16,170 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:16,226 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBtZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:16,226 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:16,232 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:16,233 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:16,234 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:16,237 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:16,241 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:16,242 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:16,244 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d9e69b04', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBtZA=']}
2025-10-30 11:57:16,248 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:16,267 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:16,267 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:16,322 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBtpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:16,323 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:16,326 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:16,327 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:16,327 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:16,329 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:16,329 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:16,331 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:16,332 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_12b83d62', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBtpA=']}
2025-10-30 11:57:16,336 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:16,345 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:16,350 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:16,401 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBt5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:16,401 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:16,406 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:16,407 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:16,408 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:16,409 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:16,410 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:16,410 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:16,412 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ebf4430a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBt5A=']}
2025-10-30 11:57:16,413 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:16,423 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:16,424 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:16,479 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBuJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:16,483 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:16,487 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:16,488 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:16,489 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:16,490 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:16,492 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:16,493 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:16,494 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c56abe0f', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBuJA=']}
2025-10-30 11:57:16,495 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:16,512 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 14, 'fields': []}
2025-10-30 11:57:16,512 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:16,941 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBuZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:16,941 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:16,944 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:16,946 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:16,947 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:16,948 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:16,950 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:16,951 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:16,952 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_dfe7a876', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBuZA=']}
2025-10-30 11:57:16,966 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:16,981 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:16,984 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,098 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBupA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,102 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,104 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,106 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,109 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,113 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,122 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,126 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,170 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d4a31de2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBupA=']}
2025-10-30 11:57:17,189 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,207 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:17,208 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,252 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBu5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,253 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,259 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,260 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,263 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,266 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,270 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,276 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,277 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_09cd393a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBu5A=']}
2025-10-30 11:57:17,279 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,287 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:17,288 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,330 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBvJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,331 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,338 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,339 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,340 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,341 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,342 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,344 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,350 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ae826386', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBvJA=']}
2025-10-30 11:57:17,352 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,360 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:17,360 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,408 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBvZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,409 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,411 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,413 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,416 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,417 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,419 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,422 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,423 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_2ee15309', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBvZA=']}
2025-10-30 11:57:17,433 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,446 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:17,446 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,550 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBvpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,551 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,554 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,557 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,560 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,561 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,562 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,565 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,570 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7d0c2982', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBvpA=']}
2025-10-30 11:57:17,575 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,587 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:17,588 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,645 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBv5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,646 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,649 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,650 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,652 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,653 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,655 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,656 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,657 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1ac713d4', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBv5A=']}
2025-10-30 11:57:17,658 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,666 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:17,666 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,709 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBwJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,718 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,723 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,726 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,728 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,730 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,733 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,735 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,737 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b96f91f2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBwJA=']}
2025-10-30 11:57:17,739 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,749 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:17,749 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,803 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBwZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,804 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,807 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,808 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,809 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,810 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,811 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,812 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,813 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_30a18fbe', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBwZA=']}
2025-10-30 11:57:17,816 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,825 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:17,825 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,866 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBwpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,867 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,870 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,871 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,873 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,875 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,877 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,878 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,880 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_fa56b6b4', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBwpA=']}
2025-10-30 11:57:17,887 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,903 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:17,904 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:17,947 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBw5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:17,948 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:17,951 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:17,952 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:17,953 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:17,955 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:17,958 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:17,959 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:17,974 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1f15d628', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBw5A=']}
2025-10-30 11:57:17,978 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:17,991 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:17,994 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,084 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBxJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,085 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,099 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,123 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,136 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,141 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,143 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,147 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,149 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_0a8cf5f1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBxJA=']}
2025-10-30 11:57:18,152 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,160 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:18,161 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,210 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBxZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,211 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,216 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,217 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,219 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,221 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,223 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,224 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,230 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_891d11a2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBxZA=']}
2025-10-30 11:57:18,234 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,247 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:18,264 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,299 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBxpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,301 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,303 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,309 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,323 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,326 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,334 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,337 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,347 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_36b6f2eb', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBxpA=']}
2025-10-30 11:57:18,351 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,370 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:18,371 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,422 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBx5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,427 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,431 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,432 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,433 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,435 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,436 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,439 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,441 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_be14dda5', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBx5A=']}
2025-10-30 11:57:18,442 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,470 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:18,471 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,522 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkByJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,523 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,525 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,527 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,527 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,528 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,529 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,531 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,534 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6d840716', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkByJA=']}
2025-10-30 11:57:18,536 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,547 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:18,549 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,629 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkByZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,630 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,632 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,634 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,635 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,636 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,639 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,640 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,642 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a2eb1dbf', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkByZA=']}
2025-10-30 11:57:18,645 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,653 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:18,654 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,706 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBypA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,707 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,711 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,713 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,714 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,715 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,716 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,716 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,718 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_62e62040', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBypA=']}
2025-10-30 11:57:18,720 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,804 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 20, 'fields': []}
2025-10-30 11:57:18,808 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:18,937 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBy5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:18,938 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:18,940 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:18,941 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:18,942 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:18,946 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:18,947 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:18,949 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:18,951 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b025c524', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBy5A=']}
2025-10-30 11:57:18,953 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:18,983 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 15, 'fields': []}
2025-10-30 11:57:18,984 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:19,596 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBzJA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 1, 'db': 'neo4j'}
2025-10-30 11:57:19,597 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:19,600 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:19,601 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:19,604 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:19,605 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:19,607 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:19,609 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:19,613 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_05c56100', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBzJA=']}
2025-10-30 11:57:19,620 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:19,634 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 9, 'fields': []}
2025-10-30 11:57:19,635 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:19,752 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBzZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:19,752 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:19,756 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:19,758 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:19,759 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:19,760 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:19,761 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:19,762 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:19,763 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8685c80c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBzZA=']}
2025-10-30 11:57:19,765 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:19,772 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:19,772 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:19,817 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBzpA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:19,818 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:19,821 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:19,822 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:19,823 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:19,824 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:19,828 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:19,828 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:19,830 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_07992148', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBzpA=']}
2025-10-30 11:57:19,838 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:19,851 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:19,853 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,039 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBz5A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,039 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,043 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,044 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,046 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,047 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,050 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,052 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,056 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_31e9cb9b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkBz5A=']}
2025-10-30 11:57:20,059 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,069 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:20,069 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,118 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB0JA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,123 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,127 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,128 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,137 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,139 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,141 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,147 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,148 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a7bebb58', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB0JA=']}
2025-10-30 11:57:20,158 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,166 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:20,171 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,211 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB0ZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,212 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,217 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,219 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,220 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,222 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,223 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,226 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,231 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5eb8c3f7', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB0ZA=']}
2025-10-30 11:57:20,234 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,242 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:20,242 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,291 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB0pA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,292 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,295 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,299 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,300 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,301 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,303 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,304 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,306 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4843255e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB0pA=']}
2025-10-30 11:57:20,311 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,321 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:20,322 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,374 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB05A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,374 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,375 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,376 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,376 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,377 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,378 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,380 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,380 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3f3e0fc7', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB05A=']}
2025-10-30 11:57:20,381 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,388 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:20,388 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,484 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB1JA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,486 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,487 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,487 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,488 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,488 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,489 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,489 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,489 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1303c59b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB1JA=']}
2025-10-30 11:57:20,490 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,499 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:20,500 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,547 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB1ZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,547 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,549 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,549 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,550 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,550 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,551 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,551 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,552 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9ec1d7cf', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB1ZA=']}
2025-10-30 11:57:20,552 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,561 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:20,563 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,608 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB1pA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,608 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,610 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,610 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,610 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,611 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,611 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,611 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,612 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4b7709a0', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB1pA=']}
2025-10-30 11:57:20,612 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,623 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:20,624 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,669 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB15A=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,670 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,672 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,674 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,677 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,677 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,678 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,678 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,679 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_44286e77', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB15A=']}
2025-10-30 11:57:20,680 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:20,691 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 8, 'fields': []}
2025-10-30 11:57:20,691 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:20,747 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2JA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 2}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:20,748 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:20,749 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:20,750 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:20,750 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:20,751 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:20,751 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:20,752 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:20,752 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (cont:Contradiccion {id: $id})\n                            SET cont.tipo = $tipo,\n                                cont.descripcion = $descripcion,\n                                cont.intensidad = $intensidad,\n                                cont.timestamp = $timestamp,\n                                cont.resuelta = $resuelta\n                            \n                            WITH cont\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:PRESENTA_CONTRADICCION {detectada_en: $timestamp}]->(cont)\n                        ' {'id': 'cont_1', 'tipo': 'indefinida', 'descripcion': '', 'intensidad': 0.5, 'timestamp': '2025-10-30T11:57:02.668518', 'resuelta': False, 'yo_id': 'yo_0'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2JA=']}
2025-10-30 11:57:20,753 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,139 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 382, 'fields': []}
2025-10-30 11:57:21,140 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,263 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 7}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,264 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,265 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
📈 Calculando métricas de éxito...
📊 Métricas calculadas: {'diversidad_contextual': 0.0, 'profundidad_narrativa': 0, 'coherencia_temporal': 0.0, 'emergencia_yo_narrativo': False}
2025-10-30 11:57:21,267 [INFO] SistemaFenomenologico: Evaluando contradicciones de 4° orden...
2025-10-30 11:57:21,268 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,268 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> pinning database: None
2025-10-30 11:57:21,269 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,270 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,270 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,271 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,273 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                        MERGE (y:YO {id: $id})\n                        SET y.tipo = $tipo,\n                            y.activacion = $activacion,\n                            y.timestamp = $timestamp,\n                            y.version = $version,\n                            y.coherencia_narrativa = $coherencia_narrativa,\n                            y.estabilidad_contextual = $estabilidad_contextual,\n                            y.integracion_afectiva = $integracion_afectiva\n                    ' {'id': 'yo_0', 'tipo': 'PROTO_YO', 'activacion': 1.0, 'timestamp': '2025-10-30T11:57:02.642985', 'version': 0, 'coherencia_narrativa': 0.0, 'estabilidad_contextual': 0.0, 'integracion_afectiva': 0.5, 'coherencia_total': 0.0} {}
2025-10-30 11:57:21,275 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,350 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 71, 'fields': []}
2025-10-30 11:57:21,350 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,352 [INFO] SistemaYoEmergente: Nodo YO v0 sincronizado con Neo4j
2025-10-30 11:57:21,396 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'stats': {'contains-updates': True, 'properties-set': 7}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,397 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,398 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,399 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,399 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,400 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,400 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,403 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,403 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1a5544df', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,404 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,426 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 10, 'fields': []}
2025-10-30 11:57:21,431 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,479 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,482 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,483 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,487 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,487 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,488 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,488 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,488 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,488 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ca8ebf5d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,489 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,506 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 13, 'fields': []}
2025-10-30 11:57:21,515 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,516 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,516 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,516 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,517 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,518 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,518 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,521 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,522 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,524 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3e0bedfe', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,525 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,533 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:21,534 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,585 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,586 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,587 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,587 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,588 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,588 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,588 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,588 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,588 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6ef62480', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,591 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,597 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:21,597 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,648 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,650 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,650 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,651 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,651 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,652 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,652 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,653 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,653 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5fdb4646', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,654 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,661 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:21,662 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,712 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,713 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,714 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,714 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,715 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,715 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,716 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,716 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,717 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a649d13c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,718 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,725 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:21,726 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,776 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,777 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,780 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,781 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,781 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,781 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,782 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,782 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,783 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_94908ba1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,783 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,789 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:21,792 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,839 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,840 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,841 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,841 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,842 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,842 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,842 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,842 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,843 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8c563a97', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,844 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,850 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:21,851 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,901 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,902 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,903 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,904 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,904 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,904 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,905 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,905 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,906 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_0f50dc4e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,908 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,914 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:21,915 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:21,966 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:21,970 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:21,970 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:21,970 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:21,970 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:21,971 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:21,972 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:21,972 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:21,973 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5c2eaa92', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:21,973 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:21,979 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:21,980 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,027 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,029 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,030 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,030 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,030 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,030 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,031 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,031 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,031 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_490cb68d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,032 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,038 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:22,042 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,091 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,094 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,100 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,101 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,101 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,102 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,102 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,102 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,102 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a8a9dcfd', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,103 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,110 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:22,111 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,156 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,157 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,158 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,159 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,159 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,160 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,160 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,161 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,161 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_da3870af', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,162 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,173 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:22,174 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,219 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,220 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,221 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,221 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,222 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,222 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,222 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,222 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,223 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_64a4db11', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,227 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,235 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:22,239 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,280 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,281 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,282 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,282 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,286 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,286 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,287 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,287 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,287 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b9404783', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,288 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,294 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:22,295 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,344 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,346 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,347 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,347 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,348 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,348 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,348 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,348 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,348 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b10e8b9a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,350 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,362 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:22,363 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,408 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,409 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,410 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,410 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,411 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,415 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,416 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,419 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,421 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_e367f159', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,422 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,428 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:22,429 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,474 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,477 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,478 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,478 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,479 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,480 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,480 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,480 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,481 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3da9414e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,481 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,488 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:22,490 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,534 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,535 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,536 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,536 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,537 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,537 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,537 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,538 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,538 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6f69981d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,540 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,548 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:22,548 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,597 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,604 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,605 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,605 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,605 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,606 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,606 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,606 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,606 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6888362b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,607 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,613 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:22,617 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,660 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,662 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,662 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,663 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,663 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,663 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,664 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,664 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,665 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6e8e35e4', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,666 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,679 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:22,680 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,723 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,724 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,725 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,725 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,726 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,726 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,727 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,727 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,728 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d320c9fc', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,729 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,739 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:22,741 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,786 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,787 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,795 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,795 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,795 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,796 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,796 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,796 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,796 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9c603674', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,797 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,807 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:22,807 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,849 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,850 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,852 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,852 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,852 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,853 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,853 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,853 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,854 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_14483803', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,854 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,860 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:22,861 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,912 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,913 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,914 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,914 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,915 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,915 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,916 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,916 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,917 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c0936ee6', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,918 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,925 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:22,925 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:22,975 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:22,976 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:22,978 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:22,981 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:22,981 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:22,981 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:22,982 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:22,982 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:22,983 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6f810470', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:22,984 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:22,992 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:22,995 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,038 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,039 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,040 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,041 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,041 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,041 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,041 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,043 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,044 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_bbb805c6', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,045 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,055 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:23,055 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,101 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,102 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,112 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,113 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,113 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,114 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,114 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,115 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,115 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_e6ec60ba', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,116 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,126 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:23,143 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,180 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,181 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,182 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,183 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,183 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,184 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,184 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,184 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,185 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6728f0ac', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,186 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,192 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:23,192 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,244 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,245 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,246 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,246 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,247 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,249 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,250 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,250 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,251 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7cbc0996', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,252 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,257 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:23,258 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,308 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,309 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,310 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,310 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,311 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,312 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,312 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,312 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,313 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_fd572082', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,314 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,320 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:23,321 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,372 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,373 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,374 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,374 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,375 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,375 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,376 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,378 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,379 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_74e22928', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,380 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,385 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:23,385 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,435 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,436 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,438 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,439 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,439 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,440 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,440 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,441 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,441 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_27503275', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,442 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,449 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:23,449 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,499 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,500 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,501 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,501 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,501 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,502 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,502 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,502 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,502 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9caa679e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,503 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,508 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:23,509 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,563 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,564 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,566 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,567 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,568 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,568 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,569 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,569 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,570 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_072c2fba', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,570 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,575 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:23,576 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,626 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,627 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,628 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,629 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,629 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,630 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,630 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,631 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,631 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5ec1a3c9', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,632 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,638 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:23,638 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,689 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,691 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,692 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,692 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,692 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,692 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,693 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,693 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,693 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5773da8c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,694 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,701 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:23,701 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,752 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,753 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,755 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,756 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,756 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,757 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,757 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,758 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,759 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ac4fa241', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,759 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,765 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:23,766 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,815 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,816 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,817 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,818 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,818 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,819 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,819 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,819 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,820 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b4348eb9', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,821 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,828 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:23,828 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,878 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,879 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,880 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,881 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,881 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,882 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,882 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,884 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,885 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_29006d34', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,886 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,893 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:23,893 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:23,942 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:23,944 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:23,945 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:23,945 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:23,946 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:23,946 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:23,947 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:23,947 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:23,948 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5b2f4651', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:23,949 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:23,955 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:23,955 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,006 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,007 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,008 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,008 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,008 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,009 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,010 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,010 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,010 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_aab3a550', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,011 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,016 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:24,017 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,069 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,070 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,073 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,073 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,074 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,074 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,074 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,074 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,074 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b65a4016', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,076 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,083 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:24,090 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,130 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,134 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,135 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,135 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,136 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,136 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,137 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,137 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,138 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4393cbcd', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,139 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,148 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:24,149 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,201 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,236 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,238 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,238 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,239 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,239 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,239 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,239 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,240 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4bdec510', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,240 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,251 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:24,251 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,305 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,306 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,307 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,308 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,308 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,309 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,309 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,310 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,310 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a7042cf7', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,311 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,323 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:24,324 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,368 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,369 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,370 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,371 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,371 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,371 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,371 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,372 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,372 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f1120c02', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,373 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,391 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:24,391 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,432 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,433 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,434 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,434 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,435 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,435 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,439 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,440 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,441 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d3a960b1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,442 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,462 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:24,462 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,463 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,463 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,463 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,463 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,468 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,468 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,468 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,468 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,470 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f33ff624', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,475 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,484 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:24,487 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,528 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,529 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,535 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,535 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,536 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,536 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,537 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,537 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,538 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f2a5b15d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,539 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,548 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:24,548 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,591 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,592 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,594 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,595 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,595 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,595 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,597 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,598 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,598 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_46b4b89b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,599 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,609 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:24,610 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,654 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,655 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,656 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,657 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,657 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,658 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,658 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,659 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,660 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8970d81c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,661 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,670 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:24,674 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,718 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,723 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,724 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,724 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,725 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,725 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,726 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,726 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,727 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9c756c42', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,728 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,736 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:24,737 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,780 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,781 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,782 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,783 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,783 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,784 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,784 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,785 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,785 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_f711da9d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,786 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,792 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:24,793 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,844 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,845 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,846 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,847 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,848 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,848 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,849 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,849 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,850 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_93c2483b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,851 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,856 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:24,856 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,908 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,908 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,909 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,910 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,911 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,911 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,912 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,912 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,913 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_0b1ba81e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,914 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,920 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:24,920 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:24,970 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:24,971 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:24,971 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:24,974 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:24,974 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:24,975 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:24,975 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:24,976 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:24,977 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9142a93a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:24,979 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:24,984 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:24,985 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,034 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,035 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,038 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,038 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,038 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,039 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,039 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,040 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,040 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7b3551be', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,041 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,046 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:25,046 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,098 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,099 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,100 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,101 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,101 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,101 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,101 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,101 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,102 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_16f2f3b1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,102 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,107 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:25,108 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,162 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,163 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,164 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,165 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,166 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,166 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,167 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,168 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,168 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_be5f6195', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,169 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,174 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:25,175 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,228 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 1, 'db': 'neo4j'}
2025-10-30 11:57:25,231 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,232 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,232 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,232 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,232 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,233 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,233 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,233 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_499c79cf', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,234 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,346 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 110, 'fields': []}
2025-10-30 11:57:25,347 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,399 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,404 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,405 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,405 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,405 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,406 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,406 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,407 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,407 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_eae14cfd', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,408 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,417 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:25,418 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,463 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,468 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,469 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,469 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,469 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,469 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,469 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,470 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,475 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8000e45d', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,476 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,481 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:25,485 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,525 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,526 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,527 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,527 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,528 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,528 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,528 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,528 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,528 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7eca164b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,533 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,544 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:25,545 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,587 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,588 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,590 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,591 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,591 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,592 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,592 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,593 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,593 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d8b6264b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,594 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,602 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:25,602 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,650 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,651 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,652 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,652 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,653 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,653 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,654 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,654 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,655 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7bce724b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,656 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,662 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:25,663 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,714 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,715 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,716 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,716 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,717 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,718 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,719 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,719 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,720 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4793eb94', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,721 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,726 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:25,727 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,777 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,778 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,779 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,780 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,780 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,781 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,781 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,782 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,783 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8fe83ecb', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,783 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,790 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:25,790 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,840 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,843 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,843 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,843 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,843 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,844 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,853 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,853 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,854 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_aca1f831', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,855 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,862 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:25,863 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,904 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,906 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,910 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,911 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,916 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,916 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,918 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,918 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,922 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_54200f42', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,923 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:25,930 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:25,934 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:25,985 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:25,986 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:25,987 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:25,989 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:25,990 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:25,991 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:25,991 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:25,992 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:25,992 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a8f1f060', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:25,993 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,001 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:26,003 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,045 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,048 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,052 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,052 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,063 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,073 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,074 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,076 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,077 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9fd8df73', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,078 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,087 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:26,088 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,139 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,142 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,142 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,143 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,144 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,144 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,145 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,145 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,146 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3db6ac02', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,147 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,153 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,155 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,203 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,205 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,205 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,205 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,206 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,206 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,206 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,207 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,207 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1c420cb6', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,208 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,214 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,215 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,266 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,268 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,268 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,268 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,269 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,269 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,269 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,269 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,269 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8409d0d1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,271 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,278 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,278 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,328 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,329 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,332 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,332 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,333 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,333 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,334 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,334 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,335 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4873c9a1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,336 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,343 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:26,343 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,391 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,392 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,392 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,392 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,392 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,393 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,393 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,393 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,394 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_79a8849b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,394 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,400 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,401 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,455 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,458 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,458 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,461 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,462 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,463 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,463 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,463 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,463 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d683c928', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,464 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,469 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,477 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,518 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,520 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,521 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,521 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,522 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,522 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,523 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,523 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,524 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c563d3f2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,525 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,534 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:26,536 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,582 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,583 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,584 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,585 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,586 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,586 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,587 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,588 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,590 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4a8b6b0e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,591 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,597 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:26,597 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,646 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,647 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,650 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,651 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,651 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,653 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,653 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,654 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,654 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b62c7e25', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,655 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,660 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,661 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,709 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,710 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,711 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,711 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,712 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,712 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,713 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,713 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,714 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8b7d204e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,715 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,721 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:26,721 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,772 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,773 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,774 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,774 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,775 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,778 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,778 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,779 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,779 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_577e4de9', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,780 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,786 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:26,786 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,835 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,836 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,838 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,838 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,839 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,840 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,840 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,840 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,842 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c4dfa53b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,843 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,848 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,849 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,899 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,901 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,901 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,902 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,902 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,902 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,902 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,902 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,903 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_488385b1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,903 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,909 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:26,909 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:26,963 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:26,968 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:26,968 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:26,968 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:26,969 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:26,969 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:26,969 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:26,969 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:26,970 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d4cbb836', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:26,971 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:26,977 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:26,978 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,026 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,027 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,028 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,028 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,029 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,029 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,030 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,030 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,031 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_2d624729', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,032 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,038 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:27,039 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,088 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,089 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,091 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,092 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,092 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,096 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,097 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,097 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,098 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_968e54ed', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,098 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,103 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:27,104 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,151 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,152 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,155 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,156 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,156 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,157 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,157 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,158 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,158 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_30c55234', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,159 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,166 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:27,167 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,215 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,216 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,217 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,218 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,218 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,219 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,219 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,219 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,220 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c2cd5283', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,221 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,230 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:27,230 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,278 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,279 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,280 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,281 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,281 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,282 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,284 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,284 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,284 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d0416f7c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,285 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,297 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:27,297 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,341 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,344 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,344 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,345 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,346 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,346 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,347 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,347 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,347 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d9e69b04', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,348 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,355 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:27,356 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,404 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,405 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,406 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,407 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,407 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,408 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,408 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,408 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,408 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_12b83d62', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,409 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,416 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:27,416 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,466 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,468 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,469 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,469 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,469 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,472 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,473 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,474 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,474 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ebf4430a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,475 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,487 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:27,489 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,529 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,530 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,532 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,532 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,533 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,533 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,534 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,534 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,535 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_c56abe0f', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,536 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,542 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:27,543 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,592 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,593 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,594 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,594 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,595 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,595 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,595 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,596 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,597 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_dfe7a876', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,597 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,603 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:27,603 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,656 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,657 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,659 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,661 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,661 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,662 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,662 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,662 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,662 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_d4a31de2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,663 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,669 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:27,669 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,719 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,720 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,721 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,722 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,722 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,723 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,723 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,724 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,724 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_09cd393a', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,725 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,734 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:27,734 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,781 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,782 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,783 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,783 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,784 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,784 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,785 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,785 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,786 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_ae826386', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,787 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,793 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:27,794 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,845 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,846 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,847 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,848 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,849 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,849 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,850 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,850 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,851 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_2ee15309', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,852 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,858 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:27,860 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,907 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,908 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,909 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,909 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,910 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,910 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,910 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,911 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,911 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_7d0c2982', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,912 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,920 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:27,921 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:27,973 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:27,979 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:27,979 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:27,980 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:27,980 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:27,980 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:27,980 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:27,980 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:27,981 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1ac713d4', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:27,981 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:27,990 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:27,992 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,033 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,034 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,038 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,038 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,039 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,039 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,040 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,040 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,041 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b96f91f2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,042 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,050 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:28,051 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,096 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,097 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,099 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,100 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,100 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,101 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,101 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,102 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,102 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_30a18fbe', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,103 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,110 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:28,111 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,159 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,160 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,161 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,161 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,162 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,162 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,163 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,164 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,165 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_fa56b6b4', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,166 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,174 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:28,174 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,222 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,223 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,224 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,226 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,226 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,226 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,226 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,227 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,227 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1f15d628', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,228 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,239 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:28,240 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,285 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,290 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,292 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,292 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,292 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,292 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,293 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,295 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,296 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_0a8cf5f1', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,297 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,304 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:28,308 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,349 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,350 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,351 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,357 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,358 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,358 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,359 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,359 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,360 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_891d11a2', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,361 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,372 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 7, 'fields': []}
2025-10-30 11:57:28,372 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,412 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,413 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,414 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,414 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,415 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,415 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,415 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,415 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,416 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_36b6f2eb', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,416 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,427 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:28,427 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,475 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,478 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,484 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,485 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,485 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,485 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,487 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,488 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,489 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_be14dda5', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,489 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,496 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:28,498 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,539 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,540 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,543 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,543 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,544 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,544 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,544 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,544 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,545 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_6d840716', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,552 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,561 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:28,561 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,602 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,603 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,605 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,605 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,605 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,606 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,606 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,606 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,606 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a2eb1dbf', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,607 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,621 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:28,621 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,666 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,667 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,676 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,676 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,677 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,677 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,677 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,677 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,677 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_62e62040', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,678 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,688 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:28,688 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,730 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,731 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,733 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,734 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,734 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,734 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,734 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,735 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,735 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_b025c524', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,736 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,741 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 1, 'fields': []}
2025-10-30 11:57:28,742 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,794 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,798 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,800 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,801 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,801 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,802 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,802 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,803 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,803 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_05c56100', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,804 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,809 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:28,810 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,857 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,859 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,860 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,860 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,861 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,861 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,862 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,862 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,863 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_8685c80c', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,864 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,869 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:28,870 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,920 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,921 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,922 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,923 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,923 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,924 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,924 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,924 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,925 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_07992148', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,926 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,931 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:28,932 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:28,983 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:28,985 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:28,986 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:28,986 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:28,987 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:28,991 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:28,991 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:28,992 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:28,992 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_31e9cb9b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:28,993 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:28,999 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:29,004 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,046 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,051 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,051 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,052 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,052 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,052 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,052 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,052 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,054 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_a7bebb58', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,055 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,063 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:29,078 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,108 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,114 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,115 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,115 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,116 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,131 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,133 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,133 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,133 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_5eb8c3f7', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,134 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,142 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:29,143 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,185 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,186 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,192 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,193 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,193 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,193 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,193 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,194 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,194 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4843255e', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,194 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,207 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 6, 'fields': []}
2025-10-30 11:57:29,208 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,248 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,251 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,275 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,279 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,279 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,279 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,285 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,286 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,287 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_3f3e0fc7', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,288 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,294 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:29,308 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,343 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,344 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,345 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,346 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,347 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,347 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,347 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,348 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,349 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_1303c59b', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,349 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,355 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:29,356 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,405 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,406 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,407 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,407 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,408 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,408 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,409 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,409 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,413 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_9ec1d7cf', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,414 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,420 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:29,426 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,468 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,474 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,474 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,474 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,474 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,475 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,475 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,475 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,475 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_4b7709a0', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,476 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,483 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 3, 'fields': []}
2025-10-30 11:57:29,484 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,532 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,533 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,534 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,534 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,535 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,535 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,536 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,536 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,537 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (c:Contexto {id: $contexto_id})\n                            \n                            WITH c\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:ACTIVA_CONTEXTO {timestamp: $timestamp}]->(c)\n                        ' {'contexto_id': 'inst_44286e77', 'yo_id': 'yo_0', 'timestamp': '2025-10-30T11:57:02.642985'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,538 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,544 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 2, 'fields': []}
2025-10-30 11:57:29,544 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,596 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=', 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,598 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,602 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,604 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,604 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,604 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,605 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,605 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,605 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (cont:Contradiccion {id: $id})\n                            SET cont.tipo = $tipo,\n                                cont.descripcion = $descripcion,\n                                cont.intensidad = $intensidad,\n                                cont.timestamp = $timestamp,\n                                cont.resuelta = $resuelta\n                            \n                            WITH cont\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:PRESENTA_CONTRADICCION {detectada_en: $timestamp}]->(cont)\n                        ' {'id': 'cont_2', 'tipo': 'indefinida', 'descripcion': '', 'intensidad': 0.5, 'timestamp': '2025-10-30T11:57:02.668518', 'resuelta': False, 'yo_id': 'yo_0'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2ZA=']}
2025-10-30 11:57:29,606 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,617 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 5, 'fields': []}
2025-10-30 11:57:29,620 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,673 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2pA=', 'stats': {'contains-updates': True, 'labels-added': 1, 'relationships-created': 1, 'nodes-created': 1, 'properties-set': 7}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,674 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,675 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
2025-10-30 11:57:29,675 [DEBUG] neo4j: [#0000]  _: <WORKSPACE> routing towards fixed database: None
2025-10-30 11:57:29,676 [DEBUG] neo4j.pool: [#0000]  _: <POOL> acquire direct connection, access_mode='WRITE', database=AcquisitionDatabase(name=None, guessed=False)
2025-10-30 11:57:29,676 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> picked existing connection bolt-27
2025-10-30 11:57:29,676 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> checked re_auth auth=None updated=False force=False
2025-10-30 11:57:29,676 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> handing out existing connection
2025-10-30 11:57:29,677 [DEBUG] neo4j.io: [#DB1C]  C: RUN '\n                            MERGE (cont:Contradiccion {id: $id})\n                            SET cont.tipo = $tipo,\n                                cont.descripcion = $descripcion,\n                                cont.intensidad = $intensidad,\n                                cont.timestamp = $timestamp,\n                                cont.resuelta = $resuelta\n                            \n                            WITH cont\n                            MATCH (y:YO {id: $yo_id})\n                            MERGE (y)-[:PRESENTA_CONTRADICCION {detectada_en: $timestamp}]->(cont)\n                        ' {'id': 'cont_2', 'tipo': 'indefinida', 'descripcion': '', 'intensidad': 0.5, 'timestamp': '2025-10-30T11:57:21.268313', 'resuelta': False, 'yo_id': 'yo_0'} {'bookmarks': ['FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB2pA=']}
2025-10-30 11:57:29,677 [DEBUG] neo4j.io: [#DB1C]  C: PULL {'n': 1000}
2025-10-30 11:57:29,685 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'t_first': 4, 'fields': []}
2025-10-30 11:57:29,685 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: READY > STREAMING
2025-10-30 11:57:29,737 [DEBUG] neo4j.io: [#DB1C]  S: SUCCESS {'bookmark': 'FB:kcwQGCA2GPKzTf+eE1C3VTz2YMkB25A=', 'stats': {'contains-updates': True, 'relationships-created': 1, 'properties-set': 6}, 'type': 'w', 't_last': 0, 'db': 'neo4j'}
2025-10-30 11:57:29,738 [DEBUG] neo4j.io: [#DB1C]  _: <CONNECTION> server state: STREAMING > READY
2025-10-30 11:57:29,741 [DEBUG] neo4j.pool: [#DB1C]  _: <POOL> released bolt-27
🗄️ Generando exportación Neo4j...
2025-10-30 11:57:29,742 [ERROR] DiagnosticadorSistema: ✗ Error en ejecución del sistema: 'SistemaFenomenologicoV2' object has no attribute '_generar_exportacion_neo4j'
2025-10-30 11:57:29,747 [ERROR] DiagnosticadorSistema: Traceback (most recent call last):
  File "C:\Users\Public\#...Raíz Dasein\YO estructural\verificar.py", line 126, in ejecutar_sistema_principal
    resultado = sistema.procesar_flujo_completo('entrada_bruta')
  File "C:\Users\Public\#...Raíz Dasein\YO estructural\sistema_principal_v2.py", line 180, in procesar_flujo_completo
    self._generar_exportacion_neo4j()
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'SistemaFenomenologicoV2' object has no attribute '_generar_exportacion_neo4j'

❌ Error en la ejecución del sistema principal
2025-10-30 11:57:29,844 [DEBUG] neo4j.pool: [#0000]  _: <POOL> close
2025-10-30 11:57:29,845 [DEBUG] neo4j.io: [#DB1C]  C: GOODBYE
2025-10-30 11:57:29,848 [DEBUG] neo4j.io: [#DB1C]  C: <CLOSE>
2025-10-30 11:57:29,849 [INFO] Neo4jConnection: Conexión a Neo4j cerrada correctamente

C:\Users\Public\#...Raíz Dasein\YO estructural> aq esta lo que salio en el terinal l eecutar .py