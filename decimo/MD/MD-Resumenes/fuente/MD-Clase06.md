% materia: Minería de Datos
% titulo: Clase 6 · Lakehouse, bases vectoriales y aprendizaje supervisado vs. no supervisado
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 22 sep 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Cierre de exposiciones del Proyecto 2 (Databricks, Pinecone, MongoDB, Milvus) e inicio del Tema 3.

## 1. Databricks y la arquitectura Lakehouse — equipo 1
!!! Lakehouse
Arquitectura que une lo mejor del **Data Lake** (almacenamiento económico y flexible) y del **Data Warehouse** (datos estructurados y alto rendimiento) en una sola plataforma.
- Databricks: plataforma colaborativa sobre **Apache Spark** que integra data lake, data warehouse, streaming y machine learning; corre en AWS, Azure o Google Cloud.
- Flujo: fuentes (BD, APIs, archivos, IoT) → transporte → procesamiento con Spark → almacenamiento en **Delta Lake**.
- **Delta Lake:** capa de código abierto con datos en **Parquet** que permite transacciones **ACID** (atomicidad, consistencia, aislamiento, durabilidad).
- **Unity Catalog:** gobierno centralizado de datos y acceso por roles.
| Beneficio | Por qué |
|---|---|
| Menor costo total | No se mantienen lake y warehouse por separado |
| Rompe silos | Ingenieros, analistas y negocio en la misma plataforma |
| Sin vendor lock-in | Los datos quedan crudos en la nube del cliente |
| Listo para IA | Datos unificados para IA generativa y predictiva |

## 2. Pinecone (base de datos vectorial) — equipo 6
- El foco son **vectores y similitudes**: búsqueda por similitud, filtrado, ranking y **embeddings**; acceso por APIs, SDK y consola.
- Base de muchas herramientas de IA, sistemas de recomendación y **RAG**/chatbots: las búsquedas **no son por coincidencia rígida de palabras sino por contexto**.
- Seguridad en cuatro capas: identidad y acceso (**RBAC**), tráfico (HTTPS y restricción por IP), **namespaces** (espacios lógicos aislados) y almacenamiento cifrado. SLA de 99.9 % (estándar); soporte 24/7 en el nivel empresarial.

## 3. MongoDB — equipo 4
- NoSQL con documentos **BSON** (JSON binario). Ediciones: Community (gratuita), Enterprise Advanced y **Atlas** (nube).
- **Modelo de documentos flexible** (sin esquema idéntico por colección), alta disponibilidad con réplicas, **escala horizontal por sharding** y multi-nube.
- Conectores: Kafka (bidireccional), Spark (ETL por lotes), Atlas Stream Processing; **Change Streams** detectan eventos en tiempo real; colecciones de series temporales (desde 5.0).
- No es data warehouse: lo complementan **Atlas Data Federation** (consultas combinadas) y **Online Archive** (datos fríos a almacenamiento barato).
- Sin algoritmos de ML propios (se combina con Spark); Aggregation Framework, Atlas Search y **Vector Search**. SLA de 99.995 %.

## 4. Milvus — equipo 11
- Base vectorial **de código abierto**, de alto rendimiento y escalable; local, en clúster o gestionada (**Zilliz Cloud**).
- Cuatro capas independientes: **proxies** (acceso y reparto de carga), **coordinadores**, **nodos trabajadores** (streaming, datos, consulta) y **almacenamiento** (metadatos en etcd, log en Kafka, objetos en S3/GCS/Azure/MinIO).
- Clientes: Roblox (avatares), Walmart (catálogo), Cisco (base de conocimiento), Reddit, IBM (búsqueda de código).
- Pinecone vs. Milvus: Pinecone es más cerrado y sencillo; Milvus permite configurar más pero exige más trabajo.

## 5. Tema 3: aprendizaje supervisado vs. no supervisado
| | No supervisado | Supervisado |
|---|---|---|
| Objetivo | Descubrir patrones, agrupaciones o estructuras **sin etiquetas** | Predecir o clasificar tras **entrenar con datos etiquetados** ("si no lo entreno, no puedo sacarlo") |
| Algoritmos | Clustering, asociación, detección de anomalías | Clasificación, regresión, series de tiempo |
| Ejemplo | Agrupar clientes según su consumo y darle "sabor" a cada clúster | Diabetes tipo 2 (1/0) con ≈ 50,000 pacientes de historial |
**Proceso supervisado (iterativo):** muestra → particionar → correr algoritmos → ajustar variables y parámetros "hasta que tenga una calidad, una confianza" → modelo entrenado que predice sobre datos nuevos.

### Clustering
| Tipo de clúster | Rasgo |
|---|---|
| Superpuesto | Un punto puede estar en varios clústeres |
| Compacto | Alta concentración con centro bien definido (útil para decidir) |
| Disperso | Puntos aislados sin cohesión (no aporta) |
| Jerárquico | Ascendente (se combinan grupos pequeños) o descendente/divisivo |
| Probabilístico | Distribución gaussiana: más concentrada = más compacto |

### Asociación
Reglas sobre variables (tickets: leche → pan; refresco → papas), con **Apriori**. Una regla que ocurrió 10 veces puede no tener sentido; con 40 o más empieza a ser relevante.

### Supervisado: clasificación y regresión
- Variable objetivo **categórica** (sí/no, dañado/no) → **clasificación**; **continua** → **regresión** (lineal, logística, dinámica).
- Aplicaciones de clasificación: reconocimiento de imágenes, análisis de sentimiento, detección de spam.
- **Todo lo predictivo es supervisado**; lo descriptivo se toma como no supervisado (con casos híbridos: leer un árbol de decisión para entender variables; usar un clúster para ubicar un dato nuevo).
!!! El trabajo real del científico de datos
No es correr el algoritmo, sino **validar la calidad de los datos, seleccionar variables, segmentar** (no estudiar a 150 millones de mexicanos sin estratos) y **explicar el camino y los beneficios**. Correr 2–3 (o 5–6) algoritmos y comparar.

## Avisos
- Próximas clases: modelos predictivos y descriptivos, luego algoritmos uno por uno (K-Means, K-Medoids, jerárquico, Mean-Shift, densidad). Equipos de 3 para las prácticas.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Supervisado vs. no supervisado (examen)
**No supervisado:** sin etiquetas, descubre patrones (clustering, asociación, anomalías). **Supervisado:** con variable objetivo etiquetada y entrenamiento (clasificación si es categórica, regresión si es continua, series de tiempo). Todo lo predictivo es supervisado.

| Plataforma | Rasgo clave |
|---|---|
| Databricks | Lakehouse = lake + warehouse; Spark; Delta Lake con ACID |
| Pinecone | Vectorial gestionada; búsqueda por contexto (RAG); RBAC y namespaces |
| MongoDB | NoSQL BSON; sharding; Change Streams; no es warehouse |
| Milvus | Vectorial de código abierto en 4 capas; Zilliz Cloud |

**Clústeres:** superpuesto, compacto, disperso, jerárquico (ascendente/divisivo), probabilístico (gaussiano).
