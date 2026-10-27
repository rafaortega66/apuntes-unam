% materia: Minería de Datos
% titulo: Clase 3 · Servidores, nube, Data Lake vs. Data Warehouse y Big Data
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 8 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Servidores de bases de datos
| Servidor | Rasgo |
|---|---|
| SAP HANA, Sybase IQ | **Columnares**: compresión del 80–90 % (100 GB → 10–20 GB) |
| Oracle Database | Relacional tradicional, aplicaciones legacy |
| IBM Db2 / Informix | En memoria, transacciones rápidas |
| Microsoft SQL Server | Ecosistema Azure; OLTP y OLAP |
| PostgreSQL / MySQL | Open source, bajo costo |
Error común: confundir el servidor (administra conexiones, seguridad, software intermedio) con la base de datos.

## 2. On-Premise vs. nube
| | On-Premise (~30 %) | Nube (~70 %) |
|---|---|---|
| Cuándo | **Baja latencia** (bolsa de valores, ms), regulación | Despliegue en minutos, escalabilidad |
| Costo | Inicial alto + personal TI/DBA | Accesible: $10,000–20,000 MXN; pago por consumo |
| Control | Total | Seguridad compartida con el proveedor |
Escalabilidad: Google atiende 100 millones de usuarios simultáneos; Ticketmaster cae con 10,000. La decisión depende de la infraestructura existente, el stack y el costo de almacenamiento.

## 3. Data Lake vs. Data Warehouse
| | Data Lake | Data Warehouse |
|---|---|---|
| Datos | Crudos, no estructurados (imágenes, PDF, JSON, logs, IoT) | Estructurados, limpios |
| Esquema | **Al leer** (schema-on-read): "ingesta primero, preguntas después" | **Al escribir** (schema-on-write): dimensiones y hechos (Kimball, estrella) |
| Uso | Volumen masivo, petabytes, barato (HDFS, S3) | Reportes y OLAP para decisiones |
| Riesgo / costo | Volverse "pantano" sin gobernanza | Más caro, consultas rápidas y confiables |
Cantera (lago) vs. joyería pulida (almacén). Son **complementarios**.

## 4. Ecosistema Big Data
- **Kafka:** streaming de eventos; productor-consumidor desacoplado; replicación de particiones entre brokers. Alertas, recomendaciones, fraude.
- **Spark:** procesamiento distribuido **en memoria**, ~**100×** más rápido que MapReduce; SQL, PySpark, Scala, Java; ETL y ML a escala. Corre sobre HDFS.
- **Hadoop:** **HDFS** con 3 réplicas por defecto; **MapReduce** divide (Map) y agrega (Reduce); lento pero confiable para batch nocturno.

## 5. Casos KDD expuestos
| Caso | Problema | Métodos | Propuesta |
|---|---|---|---|
| News Corp (Eq. 3) | Confianza de 75 % (2018) a 46 % (2022); la opinión da 30 % de ingresos | K-Means, asociación, redes, series de tiempo, regresión, redes neuronales, optimización | Reducir opinión 15 % |
| Bwood, delivery (Eq. 1) | Entregas de 30 min que llegan en 45; desbalance repartidores | Clasificación (50,000 pedidos), regresión, K-Means, árboles | 5-fold CV con 3 meses; error ±5 min |
| Nu Bank (Eq. 10) | Millones sin historial; CNBV y Banxico exigen explicabilidad | LightGBM, XGBoost, logística Ridge/Lasso, Isolation Forest, PCA (150 → 20), RFM | ROC/AUC, **KS ≥ 0.30**, SMOTE (morosos 2–5 %), SHAP; morosidad < 3 % |
Error común (Nu): proponer caja negra. (Bwood): arreglar la interfaz en vez de la estimación.

## 6. Proyecto de arquitectura de datos
- PowerPoint de **máximo 10 diapositivas y 7 minutos**, ejecutivo para el Director General; **anexo técnico** con matemáticas, algoritmos, matrices de confusión, código y formatos.
- Califica: contenido técnico, claridad visual, dominio, seguridad al hablar.
- Debe incluir ingesta, almacenamiento, gobernanza y minería; no solo lo comercial.

## Pendiente
El examen cubre **Temas 1 y 2**; el Tema 3 (proceso, los 7 métodos, metodología) va después.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| On-Premise / nube | Latencia y control / rapidez y escala (30 % / 70 %) |
| Lake / Warehouse | Crudo, schema-on-read / limpio, schema-on-write |
| Kafka / Spark / Hadoop | Streaming / memoria 100× / HDFS + MapReduce batch |
| Columnares | SAP HANA, Sybase IQ: 80–90 % de compresión |
| Crédito | ROC/AUC, KS, SMOTE, SHAP |

!!! Pregunta de examen
Diseñar una arquitectura de datos que integre ingesta, almacenamiento y procesamiento analítico.
