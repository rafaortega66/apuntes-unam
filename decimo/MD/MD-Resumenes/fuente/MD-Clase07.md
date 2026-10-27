% materia: Minería de Datos
% titulo: Clase 7 · Arquitecturas de datos en la nube y modelos predictivos
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 24 sep 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Cierre de las exposiciones del Proyecto 2 (Oracle, Cassandra, Azure, Snowflake), repaso de modelos descriptivos e inicio de los predictivos.

## 1. Oracle (base de datos autónoma) — equipo 5
Arquitectura por etapas: extracción → integración → almacenamiento → procesamiento con IA/ML → consulta y monitoreo.
- **Automatización**, **autoescalado de CPU** (hasta 3× sin intervención), **respaldo continuo** ("respaldo del respaldo"), aprovisionamiento **serverless** en minutos, prioridades **high/medium/low** según la carga.
- Cinco V en el repositorio: volumen, velocidad, almacén único (evita el **"pantano de datos"**), veracidad (limpieza) y valor (Oracle Machine Learning), alineadas con el proceso **KDD**.
- Monitoreo en tres capas: acceso, seguridad (en reposo y en tránsito) y resiliencia.

## 2. Apache Cassandra — equipo 13
- NoSQL **descentralizada**: todos los nodos con la misma jerarquía, **sin punto único de falla**; código abierto.
- Se apoya en **Apache Spark** para procesar (ETL) y tiene **CDC** (Change Data Capture).
- Prioriza **velocidad y disponibilidad sobre consistencia estricta**; buena con series de tiempo y streaming.
- Es una base **operacional, no un data warehouse analítico**; escalado horizontal. Consulta con **CQL**, estado del clúster con `nodetool`.

## 3. Microsoft Azure — equipo 2
| Capa | Servicio |
|---|---|
| Fuentes | Relacionales, JSON/CSV, telemetría |
| Conectividad | Hub-and-spoke con puerta de enlace (túnel seguro) |
| Ingesta | **Data Factory** (lotes) y **Event Hub** (continua, compatible con Kafka) |
| Almacenamiento | Data Lake con **arquitectura medallón**: **bronce** (crudo), **plata** (limpio), **oro** (listo para negocio); Azure SQL Database y Cosmos DB (búsqueda vectorial) |
| Procesamiento | **Databricks** (Spark en RAM), Azure ML, Stream Analytics |
| Data Warehouse | **Synapse Analytics** (pool dedicado o SQL Serverless) |
| Visualización | Power BI |
- Usan **ELT** (no ETL): primero se guarda todo en el lake en su forma original para poder volver a ella.
- Control: Synapse Studio, Power BI (clientes con riesgo de cancelar), Azure Monitor, catálogo con **linaje**. Soporte por niveles, MFA, SLA con responsabilidad compartida. Adopción gradual con piloto.

## 4. Snowflake (multi-nube) — equipo 12
- **Cómputo y almacenamiento desacoplados:** cada uno escala por separado, sin cuellos de botella.
- **Dato unificado:** estructurados y no estructurados en un solo lugar.
- **Multi-nube:** sobre AWS, Azure y Google Cloud.
- ETL y ELT, Kafka, ejecutar Python/Java sobre los datos sin moverlos, streaming continuo, **clonación instantánea** y soporte 24/7; se paga solo lo que se usa.

## 5. Repaso: modelos descriptivos
- **No supervisados** (aunque hay casos híbridos): **agrupación** (clusters), **asociación** (relación entre variables) y **redes** (cómo se conectan).
- Elegir el algoritmo según datos y objetivo (K-Means da grupos compactos): **correr 2–3 algoritmos y comparar**.
- Asociación = market basket (pasta → leche y pan) y recomendaciones (Spotify con Pink Floyd).

## 6. Modelos predictivos (supervisados)
Los principales cubren ≈ 90 % de los casos: clasificación, regresión, series de tiempo y redes neuronales.
| Modelo | Variable objetivo / idea |
|---|---|
| **Clasificación** | **Binaria** (enfermo/no, anomalía/no); árboles, regresión logística, redes; probar 2–3 algoritmos |
| **Regresión lineal** | Dependiente **continua** (un costo); proyecta con una línea; la calidad depende de los datos |
| **Regresión logística** | Dependiente **categórica** (salida binaria) aunque internamente maneje continuos |
| **Series de tiempo** | Pronóstico desde un historial; identificar tendencia y estacionalidad; siempre con probabilidad, no certeza |
| **Redes neuronales** | Capas de nodos con **peso y sesgo** |
| Área | Aplicación |
|---|---|
| Finanzas | Riesgo de crédito, fraude |
| Salud | Infecciones por síntomas con pesos distintos |
| Cadena de suministro | Refacciones caras (engranes de excavadora) con compromiso de 24 h |
| Marketing | Abandono (churn) |
| RR. HH. | Rotación de puestos difíciles de reemplazar |
| Mantenimiento | Cambio de llantas de flotillas |
| Seguridad | Comportamientos sospechosos |

## 7. Demo de RapidMiner
Operadores a la izquierda, parámetros a la derecha, lienzo al centro: carga de datos → tratamiento → algoritmo. En reglas de asociación, **subir el umbral de confianza deja menos reglas pero más sólidas** (producto 19 ↔ 11; 12 ↔ 11). Equipos de 3 para las prácticas.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Supervisado vs. no supervisado (examen)
**Predictivos (supervisados):** hay variable objetivo — clasificación (binaria), regresión (continua), series de tiempo, redes. **Descriptivos (no supervisados):** agrupación, asociación, redes.

| Plataforma | Rasgo clave |
|---|---|
| Oracle autónoma | Autoescalado, respaldo continuo, serverless |
| Cassandra | NoSQL sin nodo central; disponibilidad > consistencia; operacional |
| Azure | Medallón bronce/plata/oro; ELT; Databricks, Synapse, Power BI |
| Snowflake | Cómputo y almacenamiento desacoplados; multi-nube |

**Asociación en RapidMiner.** Más confianza exigida = menos reglas, más sólidas.
