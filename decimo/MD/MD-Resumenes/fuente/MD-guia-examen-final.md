# **MD · Guía para el examen final**

**Minería de Datos** · Semestre 2027-1 · 16 nov 2026  
*Hecha con NotebookLM a partir de todas las fuentes del cuaderno de la materia (audios de cada clase y material del profesor): hilo conductor del curso, unidades con sus conceptos explicados, lo que más probablemente viene y las conexiones entre conceptos. Acompáñala con el mapa mental (MD-mapa-mental.pdf, en esta misma carpeta).*  
*Clases que no estaban en el cuaderno: 19\. Su resumen va en el Anexo al final.*  
*(Nota sobre las fuentes: Este cuaderno contiene exclusivamente las transcripciones de las 18 grabaciones de clase en audio (MD-Clase1.m4a a MD-Clase21.m4a); no hay archivos de diapositivas ni material escrito adicional del profesor cargado por separado. En los puntos donde alguna fórmula algebraica o parámetro no se dictó completo en voz alta o presenta ruido en la transcripción del audio, se indica expresamente.)*

## ---

**HILO CONDUCTOR**

La materia cuenta el viaje completo para convertir datos crudos de una organización en decisiones inteligentes y sistemas en producción. Todo comienza en el **terreno físico y tecnológico de los datos** (Clases 1 a 7): antes de pensar en cualquier algoritmo, necesitas saber dónde vive la información, qué diferencia una base de datos pequeña de un repositorio empresarial, por qué los datos históricos estructurados se organizan en *Data Warehouses* y *Data Marts* mientras que los datos crudos y multimedia caen en *Data Lakes* o ecosistemas *Big Data* en memoria y en la nube, y cómo han surgido bases especializadas —sobre todo las vectoriales— para manejar texto, imágenes y audio. Pero tener una infraestructura impecable no sirve de nada si no sabes qué preguntarle ni bajo qué metodología actuar.  
Por eso el curso introduce primero la distinción entre **modelos descriptivos (no supervisados)** y **modelos predictivos (supervisados)** y luego recorre sistemáticamente cada familia de algoritmos según el problema de negocio (Clases 6 a 16). Arrancas explorando datos sin etiquetas mediante **agrupamiento (*clustering*) y reducción de dimensionalidad (PCA)** para segmentar clientes o productos (Clases 8, 9 y 11), pasas a descubrir qué artículos se compran juntos mediante **reglas de asociación** (Clases 9, 10, 12 y 13), y das el salto al aprendizaje supervisado: primero prediciendo valores numéricos continuos con **regresión** (Clases 11 y 14), luego tomando decisiones categóricas o binarias con **clasificación** —el algoritmo estrella del profesor— (Clases 12, 13 y 15), después proyectando variables ordenadas en el tiempo con **series de tiempo** (Clases 14, 15 y 18), y cerrando con **redes neuronales artificiales** capaces de aprender patrones complejos en tablas, imágenes y secuencias (Clases 16, 20 y 21). Finalmente, el cierre del curso (Clases 18, 20 y 21\) amarra toda esa caja de herramientas dentro de la metodología industrial **CRISP-DM** y las técnicas formales de **evaluación, validación cruzada, control de sobreajuste y monitoreo en producción**, garantizando que un modelo no solo funcione en la computadora de pruebas sino que resista datos nuevos y genere valor real para el cliente.

## ---

**UNIDADES Y TEMAS DEL CURSO**

### **Unidad 1: Fundamentos de Datos, Repositorios, Bases de Datos y Arquitectura Empresarial *(Clases 1, 2, 3, 4, 6, 7 y 8\)***

#### **a) Qué problema resuelve y cómo se conecta con el resto del curso**

Resuelve el problema de dónde almacenar, asegurar, integrar y consultar grandes volúmenes de información heterogénea antes de analizarla. La minería de datos analiza grandes conjuntos de datos ("nuestra carnita, nuestra esencia"), y sin comprender si los datos están en tablas transaccionales, almacenes históricos, lagos sin procesar o en la nube, es imposible extraer variables confiables para los algoritmos de las unidades siguientes.

#### **b) Conceptos clave**

> * **Minería de Datos** *(Clase 1\)*: Proceso de análisis de grandes conjuntos de datos para identificar patrones y dar respuestas a los clientes. *Analogía*: Es como refinar petróleo crudo en una planta para obtener combustibles útiles; los datos por sí solos son petróleo bruto. *Ejemplo*: Extraer patrones de tickets de compra o historial clínico para decidir estrategias comerciales o médicas.  
> * **Base de Datos vs. Repositorio de Datos vs. Servidor de Base de Datos** *(Clases 1 y 3\)*: Una **base de datos** es una colección estructurada (por ejemplo, en tablas) de tamaño pequeño o moderado con menor detalle histórico y de acceso restringido. Un **repositorio de datos** es un contenedor estructurado y jerárquico, generalmente centralizado, con **metadatos**, control de acceso, respaldos, historial controlado y capacidad para administrar grandes volúmenes (como terabytes) para múltiples usuarios. Un **servidor de base de datos** opera bajo un esquema **cliente-servidor**: no es el repositorio en sí, sino el equipo (hardware y software) que recibe solicitudes (por ejemplo vía HTML/ODBC/JDBC), valida seguridad, balancea la carga y se conecta a una o varias bases de datos. *Analogía*: La base de datos es una libreta de contabilidad personal; el repositorio es el archivo central del banco con bóveda, catálogo (metadatos) y permisos por rango; el servidor es la ventanilla y el oficial que verifica tu credencial antes de ir a buscar el expediente al archivo. *Ejemplo*: Un sistema escolar o de inventarios donde miles de accesos diarios consultan vía ODBC/JDBC sin tocar directamente los discos.  
> * **Data Warehouse, Data Mart y Data Lake (y Lakehouse)** *(Clases 2, 3 y 6\)*: Un **Data Warehouse** recopila, integra y organiza grandes cantidades de datos históricos y actuales en una estructura ordenada para ser la "única fuente confiable" de análisis y toma de decisiones; en la práctica, cerca del 70% se accede mediante **virtualización** (en tiempo real sin copiar todos los campos físicamente). Un **Data Mart** es un subconjunto específico del *warehouse* enfocado en un área o proyecto concreto (ej. distribución, finanzas o marketing). Un **Data Lake** almacena enormes volúmenes de datos crudos (estructurados, semiestructurados y no estructurados: audio, video, imágenes, logs, sensores) sin esquema rígido previo, lo que exige gobernanza y catalogación para evitar un "pantano de datos" (*data swamp*). Una arquitectura **Lakehouse** (como la expuesta para Databricks) fusiona la flexibilidad y bajo costo del *Data Lake* con la estructura y transacciones ACID del *Data Warehouse*. *Analogía*: El *Data Lake* es un río y presa donde entra agua con todo lo que arrastra; el *Data Warehouse* es la planta embotelladora con garrafones etiquetados por pureza; el *Data Mart* es la vitrina exclusiva para refrescos o lácteos. *Ejemplo real citado por el profesor*: Bancomer tardó \~3 años y gastó cerca de 5 millones de dólares en un *Data Warehouse* fallido con Teradata hace \~12–14 años; hoy, plataformas como SAP o Google permiten armarlo modularmente como "Lego" en 2 o 3 meses.  
> * **Big Data (5 Vs), Hadoop, Spark y Kafka** *(Clases 3 y 7\)*: Conjunto de tecnologías para procesar datos masivos caracterizados por volumen, velocidad, variedad, veracidad y valor. **Apache Hadoop** distribuye archivos en clústeres mediante **HDFS** (*Hadoop Distributed File System*) y los procesa por lotes con **MapReduce** (mapea/divide tareas entre nodos y agrupa resultados) gestionado por YARN. **Apache Spark** ejecuta el procesamiento directamente en **memoria RAM** (miles de veces más rápido que ir a disco), soporta Python (*PySpark*), Java y R, e incluye librerías de *streaming* y *Machine Learning*. **Apache Kafka** es una plataforma distribuida para ingesta y distribución de eventos en tiempo real (*streaming*). *Analogía*: Hadoop es una flota de camiones repartidores que guardan paquetes en bodegas (disco); Spark es una línea de chefs preparando todo sobre la mesa de trabajo (RAM) sin ir a la alacena en cada paso; Kafka es la banda transportadora en vivo que reparte pedidos al instante. *Ejemplo*: Procesamiento de millones de clics o telemetría de sensores cada pocos segundos.  
> * **On-Premise vs. Cloud** *(Clases 1, 3 y 8\)*: En *on-premise* la empresa compra, instala y mantiene su propio hardware y software (\~30% de empresas); en *cloud* (Amazon AWS, Google Cloud, Microsoft Azure) se virtualizan servidores y almacenamiento bajo demanda (\~70% de la información actual). *Analogía*: Comprar un camión propio con taller y chofer (*on-premise*) frente a rentar exactamente el espacio de carga que necesitas cada mes (*cloud*).  
> * **Bases de Datos Especializadas y Bases Vectoriales** *(Clases 1, 4, 6 y 8\)*:  
  * *Relacionales*: Tablas estructuradas con esquemas rígidos (ej. SQL Server, Oracle).  
  * *Columnares*: Guardan datos por columnas en lugar de filas, optimizadas para lectura analítica rápida y compresión mediante diccionarios (ej. SAP HANA, donde 100 GB pueden comprimirse a 10–20 GB y campos repetidos como "México" 10,000 veces se sustituyen por un diccionario).  
  * *Espaciales*: Almacenan coordenadas, áreas y distancias para mapeo y logística rápida.  
  * *Documentales / NoSQL*: Guardan documentos flexibles sin esquema rígido de tabla (ej. MongoDB en formato BSON binario; útil para leyes, noticias, catálogos).  
  * *En Memoria*: Residen totalmente en RAM para máxima velocidad (ej. SAP HANA).  
  * *Series de Tiempo*: Optimizadas para registros indexados cronológicamente (ej. colecciones temporales desde MongoDB 5.0 o motores especializados).  
  * *Vectoriales*: Convierten texto, imágenes, audio o video en vectores numéricos (**embeddings**), dividiendo textos largos en fragmentos (**chunking**), para realizar **búsquedas aproximadas por similitud o contexto semántico** en lugar de coincidencias exactas de SQL (ej. Pinecone, Milvus). *Analogía*: Una base SQL busca en un directorio telefónico el nombre exacto "Juan Pérez"; una base vectorial funciona como cuando tarareas una melodía y la aplicación encuentra las canciones más parecidas por su ritmo y tono. *Ejemplo*: La frase *"El cliente está satisfecho con el servicio"* se convierte en un vector numérico (\[0.12, \-0.34, ...\]), o la pregunta *"¿dónde puedo reparar mi automóvil?"* recupera talleres mecánicos aunque la palabra "taller" no esté en la consulta.

#### **c) Comparación rápida de arquitecturas y tipos de almacenamiento *(Clases 1–4, 6–8)***

| Tecnología / Enfoque | Tipo de datos que acepta | Dónde procesa / Cómo busca | Caso de uso visto en clase   |
| :---- | :---- | :---- | :---- |
| **BD Relacional (SQL)** | Estructurados en tablas | Disco/RAM; coincidencia exacta (= / \>) | Transacciones, inventarios, clientes |
| **BD Columnar / In-Memory** | Estructurados por columnas | RAM; compresión por diccionario | Analítica rápida en tiempo real (SAP HANA) |
| **Data Warehouse / Mart** | Estructurados e integrados | Virtualización (\~70%) o ETL *batch* | Fuente única de reportes y BI |
| **Data Lake** | Crudos, no estructurados y estructurados | Almacenamiento masivo en nube | Audios, videos, sensores, redes sociales |
| **BD Documental (NoSQL)** | Semi/no estructurados (JSON/BSON) | Colecciones sin esquema rígido | Periódicos, leyes, telemetría (MongoDB) |
| **BD Vectorial** | Vectores (*embeddings*) de texto/imagen/audio | Índices vectoriales; similitud semántica | Chatbots/RAG, recomendaciones, imágenes (Pinecone, Milvus) |
| **Hadoop vs. Spark** | Grandes volúmenes distribuidos (*Big Data*) | Hadoop: disco (HDFS \+ MapReduce); Spark: RAM | Procesamiento masivo distribuido |

#### **d) Errores comunes y puntos recalcados para examen *(Clases 1, 2, 3 y 4\)***

> * **Diagrama de arquitectura de datos**: El profesor advirtió en Clase 4 que **una pregunta de examen es crear una arquitectura de datos** definiendo primero **requerimientos funcionales** (cualitativos: qué debe hacer) y **no funcionales** (rendimiento, escalabilidad, seguridad, tolerancia a fallos, respaldos), integrando fuentes, ETL/ELT o *streaming*, almacenamiento, capa analítica/minería y visualización.  
> * **Confundir Base de Datos con Repositorio o Data Warehouse**: Un *Data Warehouse* no es solo una base de datos grande; integra gobierno, seguridad, conectividad (APIs, ODBC/JDBC) y servicios de negocio/analíticos.  
> * **Usar ETL rígido cuando conviene ELT**: En arquitecturas modernas de nube (como Azure), guardar primero los datos crudos en un *Data Lake* (ELT) permite conservar la versión original antes de transformar.  
> * **Errores en presentaciones ejecutivas**: El profesor relató que una **sola falta de ortografía** hizo que un director cancelara un proyecto millonario; además, las láminas ejecutivas deben ser limpias y breves (\~10 láminas para \~20 minutos), dejando el detalle técnico en un documento anexo.

### ---

**Unidad 2: Paradigmas de Aprendizaje y Metodologías de Proyectos (KDD, Proceso Técnico y CRISP-DM) *(Clases 1, 6, 7, 18, 20 y 21\)***

#### **a) Qué problema resuelve y cómo se conecta con la Unidad 1**

Una vez que la arquitectura de datos está clara, el científico de datos necesita saber **qué tipo de pregunta responde cada familia de algoritmos** y **qué pasos metodológicos seguir** desde la reunión con los directivos hasta el mantenimiento en producción, evitando desperdiciar tiempo en problemas inviables o modelos sin impacto de negocio.

#### **b) Conceptos clave**

> * **Aprendizaje Supervisado vs. No Supervisado** *(Clase 6\)*: En el **supervisado**, el modelo aprende de datos históricos que ya tienen una **etiqueta o variable objetivo** (requiere partición, entrenamiento y validación); en el **no supervisado**, **no hay etiquetas previas** y el algoritmo busca patrones ocultos, ordenamientos o agrupaciones por sí mismo. *Analogía*: El supervisado es estudiar con una guía que ya trae las respuestas correctas atrás; el no supervisado es llegar a una biblioteca sin letreros y organizar los libros por parecido.  
> * **Modelo Predictivo vs. Modelo Descriptivo** *(Clases 6 y 18\)*: El **predictivo** (prácticamente siempre supervisado) usa datos **etiquetados y en formato estructurado** para **pronosticar un valor o categoría a futuro** (se evalúa con métricas de exactitud o error de regresión). El **descriptivo** (prácticamente siempre no supervisado) puede trabajar sin etiquetas y con datos menos estructurados para **descubrir grupos, asociaciones o patrones** (se evalúa por **cohesión** interna de los grupos o **nivel de confianza** en asociaciones). *Nota de clase*: Un árbol de decisión puede usarse de forma descriptiva para interpretar cómo se relacionan las variables, aunque su naturaleza sea predictiva supervisada.  
> * **KDD vs. Proceso Técnico de Minería de Datos vs. CRISP-DM** *(Clases 1, 18 y 20\)*:  
  * **KDD (*Knowledge Discovery in Databases*)**: Macroproceso de corte **más académico y conceptual**, centrado en descubrir patrones ocultos desde la entrevista inicial hasta la entrega, viendo la minería de datos como una fase técnica central (*kernel*) con menor énfasis en la integración operativa final.  
  * **Proceso Técnico de Minería de Datos (13 actividades)** *(Clase 18\)*: Es el detalle tecnológico del *kernel*, donde el ajuste de parámetros ocurre en **tres momentos** (ajuste inicial por defecto, *tuning* técnico para rendimiento y el **"último apretoncito"** tras validar con el cliente).  
  * **CRISP-DM (*Cross-Industry Standard Process for Data Mining*)** *(Clases 20 y 21\)*: Es el **estándar universal de la industria** (acordado por empresas como IBM, Microsoft, Oracle, Google, Amazon y SAP) para proyectos de minería de datos, *machine learning* y ciencia de datos. Se distingue por iniciar obligatoriamente con los **objetivos de negocio** y cerrar con el **despliegue e impacto real**, organizándose en 4 niveles (Nivel 1: 6 fases universales; Nivel 2: subtareas; Niveles 3–4: hasta \~500 actividades detalladas según herramienta). *Analogía*: KDD es un libro de teoría médica; el proceso de 13 actividades es el protocolo quirúrgico en quirófano; CRISP-DM es la norma ISO completa del hospital desde la admisión y presupuesto hasta el seguimiento postoperatorio en casa.  
  * *Ejemplo vivo de Fase 1 CRISP-DM (Clase 20\)*: Empresa de *e-commerce* con baja conversión web; se reúnen **ventas, marketing y TI** (no mantenimiento); fijan criterios de éxito de negocio (**\+10% ventas, \-20% tiempo de respuesta**) y de ciencia de datos (**precisión \> 90%**), identificando como limitante el **presupuesto limitado** y como riesgo datos de usuarios incompletos.

#### **c) Comparación estructural: Paradigmas y las 6 Fases de CRISP-DM *(Clases 18, 20 y 21\)***

| Criterio | Modelo Predictivo | Modelo Descriptivo   |
| :---- | :---- | :---- |
| **Aprendizaje típico** | Supervisado | No supervisado |
| **Datos requeridos** | Etiquetados y estructurados | Sin etiquetas (estructurados o no) |
| **Propósito / Salida** | Estimar un valor o clase a futuro | Descubrir grupos, asociaciones o patrones |
| **Evaluación** | Exactitud, ROC, F1, MSE/MAE/RMSE | Cohesión (Silueta), confianza, lift |
| **Algoritmos del curso** | Regresión, Clasificación, Series de tiempo, Redes Neuronales | Clustering (K-Means, DBSCAN, etc.), Asociación (Apriori, FP-Growth) |

**Las 6 Fases de CRISP-DM y el Flujo de 13 Actividades:**

> 1. **Entendimiento del Negocio** *(Fase 1\)*: Objetivos de negocio, inventario de recursos, limitantes, supuestos, riesgos, costo-beneficio, metas de negocio y metas técnicas de ciencia de datos. *(Se puede detener el proyecto si no es viable)*.  
> 2. **Entendimiento de los Datos** *(Fase 2\)*: Recopilación, descripción, exploración (**EDA**) y verificación de calidad/historial. *(Se puede detener si no hay historial suficiente, ej. solo 3–4 meses para series de tiempo)*.  
> 3. **Preparación de los Datos** *(Fase 3\)*: Inclusión/exclusión justificada, limpieza (imputación con mediana/media, duplicados, *outliers*), creación de atributos derivados, integración (*merge*) y formateo/normalización.  
> 4. **Modelado** *(Fase 4 — el "kernel")*: Selección de algoritmo y variables (reducción de dimensionalidad), partición (80/20, 70/30 o *K-Folds*), entrenamiento inicial (*default*), y optimización de hiperparámetros (*tuning*).  
> 5. **Evaluación** *(Fase 5\)*: Evaluación técnica (métricas \+ validación cruzada) y evaluación con el negocio; aquí se da el **"último apretoncito"** a los hiperparámetros o variables tras validar con el cliente.  
> 6. **Despliegue (*Deployment*)** *(Fase 6\)*: Plan de implementación en producción, plan de monitoreo y mantenimiento (**mínimo 3 a 6 meses**), memoria técnica / informe final y revisión de lecciones aprendidas.

#### **d) Errores comunes y puntos recalcados para examen *(Clases 18 y 20\)***

> * **Mapeo directo problema → modelo (pregunta explícita de examen en Clase 18\)**: El profesor resolvió 4 casos en clase y advirtió que vendrá uno similar centrado en distinguir **clasificación binaria**:  
  1. *Sensores en máquinas para predecir fallas*: Serie de tiempo, regresión o árboles de decisión (si cada sensor es una variable).  
  2. *Monitoreo de transacciones bancarias en tiempo real para fraude*: **Clasificación binaria** (¿es anómalo o no?), **NO** serie de tiempo (Trinidad se equivocó diciendo series de tiempo y el profesor lo corrigió).  
  3. *Productos más vendidos por temporada, ubicación y festivos*: **Serie de tiempo** (modelo) con algoritmos como SARIMA.  
  4. *Agrupar clientes similares para promociones*: **Agrupación (*clustering*)** (ej. K-Means), **NO** clasificación (otro alumno confundió ambos).  
> * **Distinguir Modelo vs. Algoritmo**: En el examen hay que responder el nivel correcto (ej. modelo \= clasificación o serie de tiempo; algoritmo \= Random Forest o SARIMA).  
> * **Tener clarísima la diferencia entre Predictivo y Descriptivo**, así como el **triple ajuste** y el **monitoreo mínimo de 3 a 6 meses**.

### ---

**Unidad 3: Aprendizaje No Supervisado — Reducción de Dimensionalidad (PCA) y Clustering *(Clases 6, 7, 8, 9 y 11\)***

#### **a) Qué problema resuelve y cómo se conecta con el tema anterior**

Al iniciar un proyecto sin etiquetas previas (enfoque descriptivo de la Unidad 2), la empresa suele tener decenas de miles de tickets y decenas de variables con escalas incompatibles. Esta unidad resuelve cómo **comprimir dimensiones redundantes** y **segmentar observaciones similares** (clientes, productos, plantas o zonas) para diseñar estrategias diferenciadas en lugar de tratar a todos por igual.

#### **b) Conceptos clave**

> * **Estandarización (StandardScaler) y Transformación Logarítmica** *(Clases 8, 9 y 11\)*: Escalado que transforma variables con rangos muy dispares (ej. importes de \$6,000 vs. frecuencias de 2 días) a una escala comparable centrada en 0 (desviaciones estándar o rangos tipo \[-1, 1\] / \`\`), mientras la función logarítmica suaviza picos extremos o asimetrías. *Analogía*: Convertir pesos, dólares y yenes a una sola moneda antes de comparar quién gastó más.  
> * **PCA (Análisis de Componentes Principales) y t-SNE** *(Clases 8 y 9\)*: **PCA** es una técnica lineal de reducción de dimensionalidad que condensa muchas variables correlacionadas en unos pocos **componentes principales** nuevos que retienen la máxima varianza y permiten graficar en 2D o 3D y acelerar hasta 100 veces el procesamiento; **t-SNE** es una alternativa para estructuras **no lineales**. *Analogía*: Resumir las 25 calificaciones de un alumno en 2 índices compuestos: "habilidad matemática" y "habilidad verbal". *Ejemplo de clase*: En el ejemplo de clase del profesor, numerosas variables se comprimieron en 3 componentes interpretables (PC1: factores financieros/ingresos; PC2: penetración de marketing; PC3: fallas/retención), y en la Práctica 3.1 (58,903 registros agrupados en **524 clientes únicos**), un equipo usó PCA con PC1 \= volumen/frecuencia de compra y PC2 \= intensidad económica del ticket.  
> * **K-Means (*K-Medias*)** *(Clases 8 y 11\)*: Algoritmo de partición que agrupa datos en K clústeres de forma **esférica/compacta** minimizando las distancias cuadráticas (**distancia euclidiana**) hacia K centroides que se reubican iterativamente hasta estabilizarse. Es rápido y claro para marketing (\~20,000 registros; si hay 100,000+ conviene estratificar primero). *Analogía*: Colocar K tiendas OXXO al azar en una ciudad, asignar cada casa a su tienda más cercana, mover cada tienda al centro de las casas asignadas y repetir hasta que ninguna tienda necesite moverse. *Ejemplo real*: Con 524 clientes en la Práctica 3.1, K-Means con K=3 o K=5 separó compradores ocasionales, clientes promedio y mayoristas/VIP.  
> * **Método del Codo (*Elbow Method*) e Inercia (WCSS)** *(Clases 8 y 11\)*: **WCSS** (*Within-Cluster Sum of Squares* / inercia) suma las distancias al cuadrado de cada punto a su centroide; al graficarla contra distintos valores de K, el punto de inflexión ("el codo") sugiere el K óptimo. El profesor recomienda probar también K-1 y K+1 (ej. si el codo da 7, probar 6 y 8).  
> * **DBSCAN** *(Clases 8 y 11\)*: Algoritmo basado en **densidad y conectividad** de puntos que **descubre automáticamente el número de clústeres**, puede formar figuras arbitrarias (como donas o medialunas) y marca puntos aislados como **ruido (*outliers*)**. Sus dos parámetros ("perillas") son **épsilon (ε)** (radio de vecindad) y **mínimo de puntos**. *Analogía*: Formar grupos en un concierto juntando a quienes están a menos de 1 metro de distancia en grupos de al menos 4 personas; los que quedan solos lejos de todos se marcan como "ruido". *Ejemplo de Práctica 3.1*: Un equipo obtuvo 2 clústeres y **23.28% de ruido** en Python (mientras que un ε mal calibrado de 0.3 dejó todo como ruido y 1.0 colapsó todo en 1 clúster).  
> * **Clustering Jerárquico (Aglomerativo y Divisivo)** *(Clases 6, 8 y 11\)*: Construye una jerarquía visualizada en un **dendrograma**: el **aglomerativo** (ascendente) parte de cada dato individual y va uniendo los pares más cercanos; el **divisivo** (descendente) parte de un solo grupo y lo divide sucesivamente. Útil en análisis genético, documentos y comunidades. *Ejemplo real del profesor*: En **FEMSA Coca-Cola** (\~12,000 tiendas en Monterrey / 31,600 totales), lo usó en R para agrupar tiendas con comportamiento similar en venta de bebidas energéticas y replicar estrategias.  
> * **Mezclas Gaussianas (GMM) y Desplazamiento Medio (Mean Shift)** *(Clases 6 y 8\)*: **GMM** realiza agrupación probabilística ajustando campanas de Gauss según dispersión (útil para **reconocimiento de voz**, color/textura); **Mean Shift** desliza una ventana/radio buscando zonas de mayor concentración de puntos (útil para **seguimiento de objetos en video**, como saber dónde hay más tiempo de pantalla en un partido de básquetbol o hockey).  
> * **Métricas de evaluación en Clustering** *(Clases 8 y 11\)*: **Coeficiente de Silueta (*Silhouette Score*)** (mide qué tan compacto es cada clúster internamente y qué tan separado está de los demás) y **Davies-Bouldin** (menor valor indica mejor compactación/relación entre clústeres).

#### **c) Tabla comparativa de algoritmos de Clustering *(Clases 8 y 9\)***

| Algoritmo | Criterio de agrupación | Parámetros clave ("perillas") | Ventaja principal | Aplicación típica vista   |
| :---- | :---- | :---- | :---- | :---- |
| **K-Means** | Distancia euclidiana a centroides | Número K, iteraciones, semilla (random\_state) | Rápido, compacto, fácil de explicar al negocio | Segmentación de clientes y marketing |
| **DBSCAN** | Densidad de puntos | Radio ε, mínimo de puntos | No pide K; detecta formas raras y ruido/*outliers* | Resonancias médicas, anomalías, datos irregulares |
| **Jerárquico** | Similitud ascendente o divisiva | Método de enlace / corte en dendrograma | No requiere K inicial; visualiza jerarquías | Genética, documentos, tiendas FEMSA |
| **Mezclas Gaussianas** | Probabilidad bajo campanas de Gauss | Número de componentes gaussianos | Modela formas elípticas y pertenencia probabilística | Reconocimiento de voz, texturas |
| **Mean Shift** | Ventana deslizante hacia máxima densidad | Radio/ancho de ventana | Descubre modos/picos de densidad | Rastreo de objetos en video |

#### **d) Errores comunes y puntos recalcados para examen *(Clases 8, 9 y 11\)***

> * **Correr K-Means sin estandarizar ni aplicar PCA cuando hay muchas variables**: Si no usas StandardScaler, las variables de magnitudes grandes (ej. miles de pesos) aplastan a las pequeñas (ej. frecuencia de compra).  
> * **Entregar clústeres sin "sabor" (interpretación de negocio)**: El profesor advirtió que correr el algoritmo toma 20 minutos; la calificación y el valor real están en **nombrar e interpretar cada segmento** (ej. "especialistas de quesos", "mayoristas", "ocasionales") y verificar que sean estables, compactos y accionables.  
> * **Usar solo un algoritmo**: En todas las prácticas el profesor exigió comparar **al menos 2 o 3 algoritmos** (K-Means, DBSCAN y Jerárquico/GMM) porque un mismo dataset produce agrupaciones muy distintas según la técnica.  
> * **Caso real Túnel Emisor Oriente**: El profesor contó que tardaron \~2–3 meses con \~30 variables para segmentar 5 tipos de anillos de excavación porque sin la interpretación del cliente los clústeres carecían de sentido operativo.

### ---

**Unidad 4: Aprendizaje No Supervisado — Reglas de Asociación (Market Basket Analysis) *(Clases 9, 10, 12 y 13\)***

#### **a) Qué problema resuelve y cómo se conecta con la Unidad 3**

Mientras el *clustering* agrupa **clientes** o **entidades completas** por parecido general, las reglas de asociación responden otra pregunta sobre los mismos tickets transaccionales: **qué productos o eventos suelen ocurrir juntos dentro de una misma canasta o registro**. Además, pueden aplicarse *dentro* de un clúster específico (por ejemplo, analizar qué compran los clientes más fieles los fines de semana).

#### **b) Conceptos clave**

> * **Regla de Asociación (Antecedente → Consecuente)** *(Clase 10\)*: Expresión del tipo *"si ocurre A (antecedente), tiende a ocurrir B (consecuente)"*; por ejemplo, {pan, huevos} \-\> {leche}. *Analogía*: Es como notar que en un restaurante quien pide café y pan dulce casi siempre termina pidiendo también un vaso de agua.  
> * **Soporte (*Support*)** *(Clase 10\)*: Frecuencia con la que aparecen juntos el antecedente y el consecuente respecto al total de transacciones. Sirve como filtro inicial para descartar coincidencias raras (ej. empezar con un umbral alto como 3% e ir bajándolo hasta 1% o 0.5% para no ahogarse en 90 reglas irrelevantes).  
> * **Confianza (*Confidence*)** *(Clase 10\)*: Proporción de las transacciones que contienen el antecedente X en las que también aparece el consecuente Y (mide qué tan probable es Y dado X). En clase el profesor señaló como referencia deseable valores por encima de 0.6–0.7 o 0.8 en asociaciones fuertes (según el volumen del catálogo; en comidas preparadas de menor frecuencia los equipos bajaron el umbral a 15%–30%). *Ejemplo*: Si 70 de cada 100 tickets con yogur griego de fresa también llevan yogur de moras, la confianza es 0.70.  
> * **Lift (Elevación / Mejora)** *(Clase 10\)*: Mide cuántas veces más probable es encontrar el consecuente cuando está presente el antecedente **en comparación con una compra al azar**. Si Lift \= 1, no hay asociación real más allá de la casualidad; si Lift \> 1, la asociación es positiva y fuerte (ej. Lift \= 8.39 en {chorizo, queso americano, queso fresco} \-\> {crema dulce, pasta, salchicha} mostrado por el profesor, o Lift \= 82 en yogur de pistache con vainilla reportado por un equipo).  
> * **Algoritmo Apriori** *(Clase 10\)*: Escanea iterativamente las transacciones, poda los ítems que no cumplen el soporte mínimo, genera combinaciones candidatas de tamaño creciente (pares, tríos) y vuelve a podar. Es muy fácil de entender y rápido en datasets pequeños, pero **realiza múltiples escaneos** y se degrada en memoria y tiempo cuando hay miles de productos y millones de registros.  
> * **Algoritmo Eclat** *(Clase 10\)*: En lugar de barrer fila por fila de transacciones, trabaja con formato vertical por producto generando listas de identificadores de tickets (**tidlists**) y calculando **intersecciones de conjuntos**; reduce la carga computacional en datos dispersos, aunque consume memoria si las listas son muy densas.  
> * **Algoritmo FP-Growth (*Frequent Pattern Growth*)** *(Clase 10\)*: Construye una estructura comprimida de árbol (**FP-Tree**) ordenando los productos por frecuencia tras solo **dos escaneos** del dataset y poda ramas por debajo del soporte mínimo. Es más complejo de entender, pero mucho más eficiente y escalable que Apriori en volúmenes grandes o en salud.

#### **c) Fórmulas y comparación de algoritmos *(Clase 10\)***

| Métrica | Fórmula conceptual vista en clase | Qué indica / Criterio práctico   |
| :---- | :---- | :---- |
| **Soporte** | (Transacciones con (X e Y))/(Total de transacciones) | Qué tan común es la combinación en toda la tienda; filtra ruido |
| **Confianza** | (Transacciones con (X e Y))/(Transacciones con X) | Probabilidad condicional de llevar Y dado que ya lleva X |
| **Lift** | (Confianza(X → Y))/(P(Y) (transacciones de Y / total)) | Fuerza real vs. azar (Lift \> 1 útil; ordena mejores reglas) |

**Comparación Apriori vs. Eclat vs. FP-Growth:**

> * **Apriori**: Múltiples escaneos del dataset; rápido en pocos datos, lento en catálogos masivos.  
> * **Eclat**: Intersección de *tidlists*; menos carga computacional en datos dispersos, sensible a densidad en memoria.  
> * **FP-Growth**: Solo \~2 escaneos construyendo un árbol comprimido (*FP-Tree*); conserva eficiencia a gran escala y coincide en reglas/métricas con Apriori bajo los mismos umbrales.

#### **d) Errores comunes y puntos recalcados para examen *(Clases 9, 10, 12 y 13\)***

> * **Los 3 Niveles de Validación (marcado explícitamente como pregunta de examen en Clase 10\)**: (1) **Validación técnica** (soporte, confianza, lift); (2) **Validación con usuarios operativos / gente de negocio** (ver si las reglas tienen sentido operativo y qué productos quieren impulsar); y (3) **Validación ejecutiva / estratégica** (alinear con la estrategia de la dirección, como el caso real del profesor en C\&A / "CNI" donde el director holandés quería crecer 50% y las tallas/colores variaban entre Monterrey, Veracruz y Chiapas).  
> * **Confundir una confianza alta con una buena regla cuando el consecuente es básico**: Si casi todo el mundo compra jamón o leche por defecto, la confianza será alta aunque el *Lift* ronde 1 (no aporta promoción nueva). El profesor recalcó en Clase 10 que el **valor del negocio está en hallar asociaciones inesperadas** (como detergente \+ jugo de naranja) o potenciar productos nuevos junto a un ancla, no en hacer 2x1 en lo que la gente ya compra sola.  
> * **Granularidad errónea**: En la Práctica 3.2 (11,344 tickets y \~469 productos), un equipo notó que analizar 479 SKU individuales generaba una matriz muy dispersa sin soporte mínimo, por lo que agruparon en **62 líneas de producto** (o 117 en otro equipo) para hallar reglas sólidas. En el caso B (comidas preparadas, \~2,480 tickets), al ser menor el volumen fue necesario bajar el soporte (ej. 0.5%–2%) y la confianza (15%–30%).  
> * **Aplicación fuera de supermercados**: El profesor mostró su proyecto real con el IMSS en Chiapas y Oaxaca sobre **\~789,000 casos de dengue (2011–2015)**, usando reglas de asociación para descubrir qué síntomas clínicos (hemorragia \+ hematemesis \+ melena) alertaban sobre dengue hemorrágico.

### ---

**Unidad 5: Aprendizaje Supervisado — Modelos de Regresión *(Clases 7, 11 y 14\)***

#### **a) Qué problema resuelve y cómo se conecta con las unidades anteriores**

Dejamos el terreno puramente descriptivo para entrar al **aprendizaje supervisado predictivo**, donde ya existe una **variable objetivo (Y) numérica y continua**. Mientras la clasificación dirá *"sí o no"*, la regresión responde **"¿cuánto?"** (precio de una casa, porcentaje de alcohol en un vino, probabilidad continua de incumplimiento, costo de tratamiento).

#### **b) Conceptos clave**

> * **Regresión Lineal Simple y Múltiple** *(Clase 11\)*: Modela la relación lineal entre una (simple) o varias (múltiple) variables independientes X y una variable objetivo continua Y. *Analogía*: Calcular el costo total de un viaje en taxi sumando la tarifa base más un monto fijo por cada kilómetro recorrido y por cada minuto de espera. *Ejemplo de clase*: Estimar el precio de una casa en función de su superficie (precio \= 34 \+ 4.8x) o sumando ubicación y antigüedad.  
> * **Regresión Polinomial** *(Clase 11\)*: Introduce términos polinómicos (exponentes de las variables independientes) para ajustar curvas cuando la relación entre los datos no es una línea recta. *Analogía*: Trazar una carretera con curvas suaves que sigue la forma de una montaña en lugar de intentar cruzarla con una regla recta.  
> * **Regresión Ridge vs. Lasso** *(Clases 11 y 21\)*: Ambas son regresiones regularizadas que manejan múltiples variables correlacionadas controlando el sobreajuste, pero actúan de forma opuesta: **Ridge** conserva y pondera las variables similares/colineales repartiendo peso entre ellas sin eliminarlas, mientras que **Lasso** penaliza y **elimina variables no significativas** dejando solo las más influyentes. *Analogía*: En un proyecto en equipo con tareas repetidas, Ridge reparte el trabajo proporcionalmente entre todos los integrantes; Lasso despide a los que no aportan valor único y deja solo a los indispensables. *Ejemplo de la Práctica 3.3 (vinos)*: Lasso descartó la mayoría de las 12 variables químicas dejando principalmente **prolina** y **color intenso** (y en sentido inverso ceniza alcalina).  
> * **Regresión con Árboles y Random Forest Regressor** *(Clases 11 y 14\)*: En lugar de ajustar una sola ecuación global, divide los datos en rangos mediante condiciones (ej. ingreso \> 50 o \> 83\) y **Random Forest** promedia múltiples árboles aleatorios, capturando relaciones **no lineales** y siendo mucho más robusto ante valores atípicos (*outliers*). *Ejemplo de la Práctica 3.3 (178 vinos, 12 variables fisicoquímicas)*: La regresión lineal múltiple logró R2 ≈ 0.68 (error 0.17) en un equipo o 0.434 en RapidMiner en otro, mientras que **Random Forest** ganó consistentemente con R2 ≈ 0.75–0.77 y menor error (0.12–0.13), permitiendo evitar costosas pruebas físicas de laboratorio.  
> * **SVR (*Support Vector Regression*)** *(Clase 11\)*: Variante de máquinas de vectores de soporte para valores continuos que ajusta un "tubo" o franja de tolerancia alrededor del plano de predicción.  
> * **Métricas de evaluación de Regresión** *(Clases 11, 14 y 18\)*:  
  * **R2 (Coeficiente de determinación)**: Mide cuánta varianza de la variable dependiente explica el modelo; entre más cercano a 1, mejor ajuste.  
  * **MSE / RMSE (Error Cuadrático Medio y su raíz)**: Mide el promedio de los errores al cuadrado (penalizando más los errores grandes); entre más cercano a 0, mejor.  
  * **MAE (Error Absoluto Medio)**: Promedio del valor absoluto de las diferencias entre lo predicho y lo real.

#### **c) Fórmulas y tabla comparativa *(Clases 11 y 14\)***

*(Nota: En el audio de la Clase 11 el profesor mostró las gráficas y mencionó en voz alta la estructura lineal y \= a \+ bx —en transcripción "y \= bx \+ 1..." / "y \+ a \+ x"— y el ejemplo numérico 34 \+ 4.8x; las ecuaciones completas de Ridge, Lasso, R2 y MSE no se dictaron término a término).*

| Algoritmo de Regresión | Cómo modela | Fortaleza clave | Limitación / Cuándo evitar   |
| :---- | :---- | :---- | :---- |
| **Lineal (Simple / Múltiple)** | Recta o hiperplano lineal | Muy fácil de interpretar con coeficientes | Falla si los datos tienen curvaturas no lineales |
| **Polinomial** | Curva con potencias de X | Se adapta a relaciones curvas | Riesgo de sobreajuste y complejidad si sube el grado |
| **Ridge** | Pondera variables colineales | No descarta variables útiles que se parecen | No hace selección automática eliminando variables |
| **Lasso** | Recorta variables no significativas | Simplifica modelos eliminando variables de poco aporte | Puede descartar variables correlacionadas útiles |
| **Random Forest** | Ensamble de árboles por partición | Captura no linealidades; resiste *outliers*; alta precisión | Menor interpretabilidad de fórmula directa |

#### **d) Errores comunes y puntos recalcados para examen *(Clases 11 y 14\)***

> * **Qué hacer si las métricas (R2, error) salen mal (pregunta hecha por el profesor en Clase 11\)**: (1) Verificar limpieza y **estandarización** de las variables (en vinos, prolina y magnesio tenían magnitudes de cientos frente a decimales en matiz); (2) revisar la **selección de variables** (quitar las que meten ruido o son irrelevantes como el ID de muestra); (3) revisar *outliers* o fechas atípicas en el historial; (4) probar otro tipo de modelo (ej. de lineal a Random Forest o polinomial); o (5) **aceptar honestamente que no hay datos suficientes para calcularlo**.  
> * **Sobreajuste por muestreo sesgado**: Si en entrenamiento R2 sale altísimo y en prueba se desploma (o viceversa por muestra pequeña de 178 vinos), se debe usar *K-Fold Cross-Validation* y probar varias semillas (random\_state), no confiar en un único corte 70/30.  
> * **Principio de parsimonia en variables**: En la Práctica 3.3, reducir de 12 variables químicas a solo las **5 más significativas** apenas bajó R2 en 0.03–0.04, demostrando que las demás aportaban casi puro ruido.

### ---

**Unidad 6: Aprendizaje Supervisado — Modelos de Clasificación *(Clases 6, 7, 12, 13, 15 y 16\)***

#### **a) Qué problema resuelve y cómo se conecta con la Unidad 5**

El profesor lo definió como el **"algoritmo estrella"**, el número uno que recomienda dominar al 200%. A diferencia de la regresión (variable continua), la clasificación resuelve problemas supervisados donde la **variable objetivo es discreta o categórica**: generalmente **binaria** (sí/no, tiene diabetes/no tiene, fraude/legítimo, aprueba crédito/rechaza, abandona/se queda) o **multiclase** (bajo/medio/alto, 6 tipos de paisaje).

#### **b) Conceptos clave y los 6 Algoritmos**

> * **Preprocesamiento, Discretización (*Binning*) y Selección de Variables** *(Clases 12 y 13\)*: Antes de clasificar, es vital hacer EDA (histogramas, *boxplots*, mapas de calor), eliminar variables sin varianza, redundantes o sesgadas (como la variable trampa embarazos cuando hay hombres y mujeres), imputar ceros imposibles (glucosa 0 o presión 0 con la mediana) y agrupar variables continuas en intervalos o **bins** (ej. temperatura alta/media/baja o edades de 10 en 10 años para optimizar árboles). *Analogía*: Antes de clasificar frutas por tamaño, pones etiquetas de "Chica, Mediana, Grande" en lugar de medir milímetro por milímetro.  
> * **1\. Árboles de Decisión (*Decision Trees*)** *(Clases 12 y 13\)*: Divide iterativamente los datos mediante preguntas condicionales sobre los atributos hasta formar hojas de decisión; usa criterios matemáticos de desigualdad/impureza como el **Índice de Gini** o la **Entropía**. Sus hiperparámetros clave son el criterio (gini o entropy), la **profundidad máxima** (max\_depth / **poda** para evitar que crezca demasiado y sobreajuste) y el tamaño de hoja. *Analogía*: El juego de "Adivina Quién" donde cada pregunta ("¿glucosa \> 142?", "¿edad \> 30?") parte al grupo hasta llegar a la respuesta. *Ejemplo de clase*: Decidir si jugar golf según clima, humedad y viento, o reglas médicas claras en diabetes (donde un equipo podó a 4 niveles logrando \~68% de detección interpretable por médicos).  
> * **2\. Bosques Aleatorios (*Random Forest*)** *(Clases 12, 13, 15 y 16\)*: Ensamble que entrena múltiples árboles de decisión sobre subconjuntos aleatorios de datos y variables y combina sus votaciones, logrando mucha mayor estabilidad y precisión. Sus hiperparámetros incluyen **número de árboles**, tamaño mínimo del nodo, cantidad de características, profundidad y semilla aleatoria (random\_state, que el profesor sugiere variar ej. 35 vs. 50 para probar estabilidad). *Ejemplo de clase*: En los proyectos de diabetes (829 registros clínicos), Random Forest fue el ganador recurrente (\~75%–83% de exactitud), identificando glucosa, IMC y edad como las variables de mayor importancia.  
> * **3\. Regresión Logística** *(Clases 7, 12 y 13\)*: Modelo lineal para clasificación binaria que calcula la probabilidad de pertenecer a la clase positiva ajustando una curva logística sobre el historial, fácil de interpretar mediante razones de momios (*odds ratios*). Parámetros: número de iteraciones y **umbral de decisión** (por defecto 0.5). *Ejemplo*: En un equipo de diabetes, aumentar una desviación estándar en glucosa multiplicaba los momios por 2.47 (p \= 0.001) y en IMC por 2.1.  
> * **4\. Naive Bayes (*Bayes Ingenuo*)** *(Clases 12 y 13\)*: Basado en el teorema de Bayes, evalúa la probabilidad de cada variable independiente respecto a una línea base; se usa muchísimo en **análisis de texto, detección de spam y análisis de sentimientos**. Tiene dos variantes principales vistas en clase: **Gaussiana** (para variables numéricas continuas, ej. biología/medicina) y **Multinomial** (para conteos/frecuencias de palabras en texto). *Analogía*: Leer un correo y sumar puntos de sospecha por cada palabra clave ("premio", "urgente", "clic") de forma independiente para decidir si es spam.  
> * **5\. K-Vecinos Más Cercanos (*KNN*)** *(Clases 12 y 13\)*: Algoritmo basado en distancia que clasifica una observación nueva asignándole la clase mayoritaria entre sus K vecinos históricos más cercanos. Parámetros: número de vecinos (K) y métrica de distancia (**Euclidiana** o **Manhattan**, siendo Manhattan útil por tomar valores absolutos cuando hay datos dispersos o negativos). *Analogía*: Llegar a una fiesta sin saber de qué carrera es la gente y asumir que eres de la misma facultad que las 5 personas que tienes más cerca.  
> * **6\. Máquinas de Vectores de Soporte (*SVM*)** *(Clases 12 y 13\)*: Busca trazar un **hiperplano** óptimo en el espacio multidimensional que separe las clases maximizando la franja o **margen** entre ellas; muy útil en control de calidad industrial, imágenes, spam y fraude. Parámetros: **kernel** (**lineal**, **RBF/radial**, **polinomial**), penalización por error (C) y ancho del margen. *Analogía*: Poner una avenida lo más ancha posible entre dos colonias rivales de modo que quede la máxima distancia libre hasta las casas de ambos lados.  
> * **Métricas de Evaluación y Desbalanceo de Clases** *(Clases 12, 13, 15 y 16\)*:  
  * **Matriz de Confusión**: Cruza valores reales contra predichos mostrando **Verdaderos Positivos (VP)**, **Verdaderos Negativos (VN)**, **Falsos Positivos (FP — falsa alarma)** y **Falsos Negativos (FN — caso real que el modelo no detectó)**.  
  * **Exactitud (*Accuracy*)**: Porcentaje total de aciertos; **es engañosa cuando hay clases desbalanceadas** (en el dataset de diabetes, 64.78% no tenían diabetes; un modelo tonto que dijera "todos sanos" ya sacaría \~65% de exactitud; si una clase domina al 95%, el modelo se sesga y se aplican técnicas de **oversampling / undersampling**).  
  * **Precisión (*Precision*)**: Qué porcentaje de los que el modelo predijo como positivos realmente lo son.  
  * **Sensibilidad (*Recall*)**: De todos los casos positivos reales, cuántos logró detectar el modelo. *(En medicina es la métrica más crítica para no mandar enfermos a casa)*.  
  * **F1-Score**: **Media armónica** entre Precisión y Sensibilidad.  
  * **Curva ROC y Área Bajo la Curva (AUC)**: Mide la capacidad del modelo para distinguir entre clases en distintos umbrales; cuanto más cercana a 1, mejor.

#### **c) Mapa rápido de algoritmos de clasificación y sus parámetros *(Clases 12 y 13\)***

| Algoritmo | Lógica central | Hiperparámetros vistos en clase | Uso destacado mencionado   |
| :---- | :---- | :---- | :---- |
| **Árbol de Decisión** | Reglas por división de nodos | Criterio (Gini / Entropía), profundidad máxima (max\_depth / poda) | Reglas interpretables para médicos o crédito |
| **Random Forest** | Múltiples árboles aleatorios | Nº de árboles, profundidad, tamaño nodo, variables, random\_state | Diagnósticos médicos, fraude, biología computacional |
| **Regresión Logística** | Probabilidad sigmoide lineal | Nº de iteraciones, umbral (*threshold*, default 0.5) | Churn de clientes, enfermedades, fraude |
| **Naive Bayes** | Teorema de Bayes (independencia) | Tipo: **Gaussiana** vs. **Multinomial** | Texto, spam, análisis de sentimientos |
| **KNN** | Votación de K vecinos cercanos | Nº de vecinos K, distancia (**Euclidiana** / **Manhattan**) | Clasificación por cercanía en datos/texto |
| **SVM** | Hiperplano de máximo margen | **Kernel** (lineal, RBF, polinomial), penalización, ancho de margen | Calidad industrial, imágenes, spam, fraude |

#### **d) Errores comunes y puntos recalcados para examen *(Clases 12, 13, 15, 16 y 18\)***

> * **No inspeccionar por ID quiénes son los Falsos Positivos y Falsos Negativos**: En las exposiciones de diabetes (Clase 15 y 16), el profesor recalcó que **no basta con imprimir el número de FP y FN**; el analista debe extraer la **lista con los identificadores exactos de esas personas** (ej. persona \#1, \#14, \#25), revisar sus valores (ej. en un equipo los FN tenían glucosa promedio de 119.5 frente a 165 en diabéticos claros, y los FP tenían 143 de glucosa e IMC 38\) y definir acciones concretas.  
> * **Dejar el umbral fijo en 0.5 cuando el falso negativo cuesta vidas**: En diagnóstico médico (diabetes o cáncer), bajar el umbral (ej. de 0.5 a 0.35, o ajustar sensibilidad) reduce drásticamente los falsos negativos aunque genere algunos falsos positivos que luego se confirman en laboratorio.  
> * **No detectar variables sesgadas o imposibles**: En el dataset de diabetes, el profesor incluyó a propósito la variable **embarazos** mezclando hombres y mujeres para comprobar si los alumnos la detectaban y limpiaban; además, había **ceros** en glucosa, presión, insulina y grosor de piel que representaban datos faltantes (y \~50% de nulos en insulina).  
> * **Regla de oro para el examen**: Si la pregunta plantea una decisión dicotómica (*¿es anómalo o no?, ¿abandona o no?, ¿tiene la enfermedad o no?*), el modelo es **clasificación binaria**.

### ---

**Unidad 7: Pronóstico de Series de Tiempo *(Clases 14, 15 y 18\)***

#### **a) Qué problema resuelve y cómo se conecta con las unidades anteriores**

A diferencia de la regresión o clasificación estándar donde el orden de las filas no importa, aquí el **eje X es obligatoriamente el tiempo en intervalos iguales** (horas, días, semanas, meses). Resuelve problemas de pronóstico hacia el futuro (demanda, inventarios, consumo eléctrico, tráfico) ponderando con mayor fuerza el pasado reciente.

#### **b) Conceptos clave**

> * **Requisitos de una Serie de Tiempo** *(Clases 14 y 18\)*: Intervalos equidistantes (no mezclar días con meses; no inventar datos diarios si solo tienes mensuales) e **historial suficiente** (el profesor recomienda mínimo **2 a 4 años** para capturar ciclos estacionales; con 3–4 meses la incertidumbre es inaceptable y se frena el proyecto).  
> * **Componentes de una Serie de Tiempo** *(Clases 14 y 15\)*:  
  1. **Tendencia**: Dirección general ascendente o descendente a largo plazo (lineal o no lineal).  
  2. **Estacionalidad**: Fluctuaciones que se repiten de forma regular **dentro de un año** o periodo fijo (ej. picos cada marzo o en Navidad).  
  3. **Ciclicidad**: Oscilaciones largas **mayores a un año** (ej. ciclos económicos o sexenios).  
  4. **Componentes Irregulares / Outliers**: Eventos atípicos inesperados (pandemia COVID-19, huracán, noche de ofertas) que deben investigarse antes de decidir si se excluyen o se modelan.  
> * **Estacionariedad vs. Estacionalidad** *(Clase 15\)*: El profesor recalcó no confundirlas: **estacional** significa que varía siguiendo estaciones o periodos repetitivos del calendario; **estacionaria** significa que la serie no tiene tendencia marcada (su media y varianza son estables en el tiempo), condición que exige ARIMA para funcionar.  
> * **Prueba ADF, ACF, PACF y Ruido Blanco** *(Clases 15 y 18\)*:  
  * **ADF (Dickey-Fuller Aumentada)**: Prueba estadística para verificar si la serie ya es estacionaria.  
  * **ACF (Autocorrelación) y PACF (Autocorrelación Parcial)**: Gráficas que miden cuánto depende un periodo actual de sus rezagos (*lags*) pasados; PACF elimina los efectos intermedios para evaluar el rezago directo.  
  * **Ruido Blanco**: Residuos completamente aleatorios e independientes entre sí (media cero y varianza constante); si los residuos son ruido blanco (ej. p \> 0.05 en las pruebas usadas por los equipos), significa que el modelo ya extrajo todo el patrón útil y lo que sobra es puro azar.  
> * **Suavizamiento Exponencial (Simple, Doble y Triple / Holt-Winters)** *(Clases 14 y 15\)*: Modela el futuro dando más peso exponencial a los datos recientes: el **simple** trabaja solo con el nivel, el **doble** añade **tendencia** (β) y el **triple (Holt-Winters)** incorpora nivel (α), tendencia (β) y **estacionalidad** (γ). *Analogía*: Es como ajustar el termostato de casa poniendo más atención a la temperatura de los últimos minutos que a la de hace tres días, recordando además que todos los días a las 3 p.m. entra el sol.  
> * **ARIMA y SARIMA** *(Clases 14, 15 y 18\)*: Modelos estadísticos que trabajan sobre una **serie estacionaria** combinando tres componentes mediante los hiperparámetros **(p, d, q)**: **AR (p, Autorregresivo)** usa valores pasados recientes; **I (d, Integración)** aplica diferenciación para volver estacionaria la serie; **MA (q, Media Móvil)** corrige el modelo usando los errores/residuos pasados. **ARMA** omite la diferenciación; **SARIMA** añade términos estacionales al esquema ARIMA (útil cuando hay estacionalidad compleja o cambios de nivel). *Analogía*: Para adivinar el tráfico de hoy, ARIMA mira cómo estuvo el tráfico ayer (AR), mide si respecto a la semana pasada va subiendo o bajando (I) y corrige según cuánto se equivocó su predicción de ayer (MA).

#### **c) Comparación de modelos y métricas *(Clases 14, 15 y 18\)***

| Criterio | Holt-Winters (Triple Exponencial) | ARIMA | SARIMA   |
| :---- | :---- | :---- | :---- |
| **Exige estacionariedad** | No | Sí (vía diferenciación d) | Sí \+ componente estacional |
| **Maneja estacionalidad** | Sí (estacionalidad regular clara) | No directamente | Sí (estacionalidad anual/compleja) |
| **Parámetros ("perillas")** | α (nivel), β (tendencia), γ (estacionalidad) | (p, d, q) | (p, d, q) \+ estacionales (ej. s=12) |
| **Fortaleza en caso Tempra** | Mejor en estacionalidad regular, corto plazo (1–3 meses) y con anomalías (ej. Guadalajara 2018\) | Más estable a mediano/largo plazo (\>6 meses) según equipo | Mejor en cambios estructurales de nivel (CDMX 11.48%, Morelia 23.60%, Puebla 29.43%) |

*Métricas clave*: **MAE** (Error Absoluto Medio), **RMSE** (Raíz del Error Cuadrático Medio, penaliza errores grandes) y **MAPE** (Error Porcentual Absoluto Medio, independiente de la escala y muy popular en negocios). *Caso real Práctica 3.5 (Ventas de Tempra — datos de los equipos)*: Dataset de **420 registros** (7 estados × 60 meses, 2016–2020), entrenado con 48 meses (2016–2019) y probado con 12 meses (2020). Hallaron picos en marzo (potenciado por compras de pánico de COVID-19 en 2020), caídas en agosto, registros anómalos en cero/190 en Guadalajara 2018 (donde SARIMA falló con **94.73% de error** frente a Holt-Winters) y duplicidad exacta entre Querétaro y Veracruz.

#### **d) Errores comunes y puntos recalcados para examen *(Clases 14, 15 y 18\)***

> * **Ejercicio visual y de sectores (pregunta explícita de examen en Clase 15\)**: El profesor proyectó gráficas de series y dijo ***"esta es una pregunta de examen"***: saber identificar a simple vista en una gráfica si tiene **tendencia**, **estacionalidad** o si es **estacionaria** (y qué algoritmo elegir en comercio/ventas, banca por hora del día o consumo eléctrico por hora).  
> * **Aplanar datos cambiando la escala temporal**: En la Práctica 3.5, usar escala **trimestral** borró el pico de marzo y la caída de agosto aumentando el error, por lo que debió mantenerse la escala **mensual** (tampoco se pueden inventar datos diarios/semanales si la fuente es mensual).  
> * **Validación móvil recomendada por el profesor**: En lugar de proyectar ciegamente 12 meses, usar ventanas como **6 y 1** (correr 6 meses, pronosticar el 7.º como si no existiera y contrastarlo con la realidad) o reentrenar cada 1–3 meses con pronóstico móvil.

### ---

**Unidad 8: Redes Neuronales Artificiales *(Clases 16, 20 y 21\)***

#### **a) Qué problema resuelve y cómo se conecta con las unidades anteriores**

Cuando los datos son masivos o altamente complejos (como miles de imágenes médicas o satelitales, secuencias largas de texto/clima o tablas con patrones muy profundos no lineales), los algoritmos clásicos de clasificación y regresión alcanzan su límite. Las redes neuronales artificiales cierran la caja de herramientas de algoritmos integrando clasificación, regresión y extracción automática de características.

#### **b) Conceptos clave**

> * **Neurona Biológica vs. Neurona Artificial** *(Clase 16\)*: El cerebro humano cuenta con decenas de miles de millones de neuronas (el profesor citó \~38,000 millones y luego corrigió a **86,000 millones**) que reciben estímulos por **dendritas**, los procesan, transmiten por el **axón** y se comunican mediante **sinapsis** (conexiones químicas/eléctricas según sensibilidad). La **neurona artificial** imita esto recibiendo entradas (x1, x2, …, xn), multiplicándolas por **pesos** (w1, w2, …, wn) en una **suma ponderada**, sumándole un **sesgo (*bias*)** que se ajusta iterativamente para afinar el aprendizaje, y pasando el resultado por una **función de activación**.  
  * *Fórmula vista en clase*: ActivaciónBig(Σi (xi · wi) \+ biasBig).  
  * *Analogía*: Decidir si salir con paraguas: tus entradas son las nubes, la humedad y el pronóstico de la app; cada una tiene distinto "peso" según cuánto confíes en ella; el *bias* es qué tan friolento o precavido eres tú por defecto; si la suma supera cierto umbral, la función de activación dispara la decisión "Sí, lleva paraguas".  
> * **Funciones de Activación principales** *(Clase 16\)*:  
  * **ReLU**: Devuelve 0 o el valor positivo (muy usada en capas ocultas; en las exposiciones destacaron que evita el desvanecimiento del gradiente).  
  * **Sigmoide**: Mapea valores entre 0 y 1 (ideal para salidas de probabilidad binaria).  
  * **Softmax**: Convierte las salidas de la última capa en un **vector de probabilidades** que suman 1 para **clasificación multiclase** (ej. cebra 70%, caballo 20%, perro 10%, o 6 tipos de uso de suelo / 10 prendas de ropa).  
> * **Entrenamiento e Hiperparámetros** *(Clases 16, 20 y 21\)*:  
  * **Época (*Epoch*)**: Una vuelta completa de entrenamiento sobre todo el dataset, combinando **propagación hacia adelante** (calcula error) y **propagación hacia atrás** (ajusta pesos y *bias*). Si pones muy pocas no aprende; demasiadas memoriza y gasta cómputo.  
  * **Tamaño de lote (*Batch Size*)**: Cantidad de registros procesados antes de actualizar los pesos (ej. lotes de 32 o 128).  
  * **Tasa de aprendizaje (*Learning Rate*)** y optimizador (ej. Adam \= 0.001): Controlan qué tan rápido ajusta sus pasos la red.  
  * **Búsqueda automática**: **Grid Search** (matriz de combinaciones), **Random Search** (combinaciones aleatorias) y **AutoML / Keras** (sugieren capas y neuronas automáticamente).  
> * **Las 3 Arquitecturas principales \+ Autoencoder** *(Clases 16, 20 y 21\)*:  
  1. **MLP (Perceptrón Multicapa)**: Capas densas conectadas entre sí; ideal para **datos tabulares estructurados**. *Ejemplos Práctica 3.6*: Retención universitaria UCI (4,424 alumnos, 121 entradas tras One-Hot, 16 neuronas ReLU, regularización α=1, 80% acierto en deserción); *churn* en telecomunicaciones (\~7,000 clientes IBM, capas 64 y 32, peso 1.88 al abandono, umbral 0.3, recall \= 0.78); ocupación de oficina (12,000 registros con luz/CO2/humedad/temperatura); y *scouteo* de futbolistas con **MLP \+ Autoencoder** (70 \-\> 48 \-\> 36 \-\> 12 neuronas y regreso) para comprimir métricas de 12,000 jugadores y hallar similitudes.  
  2. **CNN (Red Neuronal Convolucional)**: Simula la visión humana mediante **filtros convolucionales** (ej. bloques 3x3 con 32, 64, 128, 256 filtros) que extraen bordes y texturas, capas de reducción (**pooling**) y una capa **Flatten** que convierte los mapas en un vector plano para clasificar. *Ejemplos Práctica 3.6*: Clasificación de uso de suelo Intel (17,000 imágenes 150x150x3, \~1.24M de parámetros frente a \~17M que habría requerido un MLP, logrando **87% train / 86% val / 86% test**); neumonía en 5,126 radiografías de tórax (1 canal); clasificación de 26 clases de malware convertido a imagen (256x256, 53% \-\> 81%); peluches comparando CNN desde cero contra **MobileNetV2** (*transfer learning*) \+ mapas **Grad-CAM**; y **Fashion-MNIST** (70,000 imágenes 28x28, donde **CNN ganó con 92.39%** frente a MLP 89.66% y RNN 89.37%, reduciendo 26% el error aunque tardó 32.4 min sin GPU).  
  3. **RNN / LSTM (Red Neuronal Recurrente)**: Posee "memoria" para procesar **secuencias** donde el orden importa (texto, audio, series de tiempo). *Ejemplos Práctica 3.6*: Clima con bloques secuenciales de 10 días (4 capas, 50 nodos), precios de acciones Walmart/Costco, y afluencia diaria de la **Línea 3 del Metro** con **LSTM** (50 unidades de memoria sobre \~2,000 días post-pandemia, **MAE \= 46,000 pasajeros**, \~7%–8% de error en días normales).

#### **c) Tabla guía: ¿Qué Red Neuronal elegir según el dato? *(Clases 16, 20 y 21\)***

| Tipo de dato | Arquitectura recomendada | Mecanismo distintivo | Técnicas anti-sobreajuste vistas   |
| :---- | :---- | :---- | :---- |
| **Tabulares** (columnas independientes) | **MLP** | Capas densas; One-Hot \+ StandardScaler | Regularización α, Dropout (0.3), Batch Normalization, mantener capas simples |
| **Imágenes / Espacial** | **CNN** | Convoluciones (3x3), Pooling, Flatten, filtros crecientes | Dropout (50%), *Data Augmentation* (rotación/zoom, cuidando no alterar color si es el rasgo), *Early Stopping* |
| **Secuencias / Series / Texto** | **RNN / LSTM** | Celdas con memoria de estados pasados | Ventanas temporales coherentes, Dropout, paro temprano (*early stopping*) |

#### **d) Errores comunes y puntos recalcados para examen *(Clases 16, 20 y 21\)***

> * **Sobreajuste por memorización temprana o exceso de capas**: En el caso de neumonía, llegar a \~100% en la época 10 significó memorización hasta aplicar *data augmentation*, *dropout* 50% y *early stopping*; en el proyecto de internet de Mariana, su MLP simple de una sola capa (32 neuronas) **no superó a un modelo lineal**, y al añadir más capas solo empeoraba por sobreajuste.  
> * **Aumento de datos inadecuado**: En el proyecto de peluches idénticos que solo cambiaban de color, aplicar *data augmentation* alterando el tono cromático habría destruido la información clave.  
> * **Regla de oro de generalización expuesta en clase**: Comparar exactitud entre entrenamiento, validación y prueba (\< 3 puntos de diferencia \= buena generalización; 3–8 \= ligero sobreajuste; \> 8 \= memorización).  
> * **Retroalimentación continua**: El profesor aclaró una duda de Ortega: aunque la red es supervisada en su diseño y ajuste de hiperparámetros, una vez entrenada y desplegada se vuelve autónoma y puede seguir mejorando al recibir nuevos lotes de datos.

### ---

**Unidad 9: Evaluación Integral, Validación Cruzada, Ajuste y Despliegue *(Clases 18, 20 y 21\)***

#### **a) Qué problema resuelve y cómo se conecta con todo el curso**

Es el filtro final de calidad antes de entregar cualquier proyecto (regresión, clasificación, clustering, series o redes neuronales) al cliente bajo CRISP-DM. Resuelve cómo comprobar que las métricas no fueron producto de la suerte de una partición 70/30 sesgada, cómo corregir errores graves en la matriz de confusión y cómo garantizar que el modelo resista datos futuros en producción.

#### **b) Conceptos clave**

> * **Validación Cruzada (*K-Folds*) y sus variantes** *(Clases 20 y 21\)*: Divide los datos en K particiones (ej. 5-Fold), entrenando en K-1 bloques y probando en el restante de manera rotativa hasta que todos fueron prueba una vez, y **promedia los *scores* de todas las vueltas**. Mientras 70/30 puede bastar en modelos sencillos de marketing, los modelos complejos o científicos/médicos exigen *K-Fold*. Variantes clave: **K-Fold aleatorio** (baraja antes), **Stratified K-Fold** (conserva proporción de clases), **Repeated K-Fold** (repite varias veces con distinta aleatoriedad) y **Group K-Fold** (mantiene juntos todos los registros de un mismo paciente o usuario para no mezclar su historial entre entrenamiento y prueba).  
> * **Underfitting vs. Good Fitting vs. Overfitting** *(Clases 20 y 21\)*:  
  * **Underfitting (Subajuste)**: El modelo es demasiado sencillo (pocos datos, pocas variables útiles o mucha correlación entre ellas); rinde **mal en entrenamiento y mal en prueba**. Solución: ser sincero con el cliente y enriquecer el dataset con nuevas variables relevantes.  
  * **Overfitting (Sobreajuste)**: El modelo memoriza el entrenamiento (por corte 70/30 sesgado, variables sobrantes o demasiadas épocas); rinde **excelente en entrenamiento y mal en prueba**.  
  * **Good Fitting (Buen ajuste)**: Entrenamiento bueno y prueba buena y consistente.  
> * **Selección y Reducción de Variables** *(Clase 21\)*: Evaluar variable por variable mediante matrices de correlación (eliminando colineales), pruebas estadísticas como **Chi-cuadrada** y **ANOVA** (para verificar diferencias significativas), y **eliminación recursiva de características (*feature elimination*)** descartando las que aportan casi cero (ej. 0.001%), sin recortar en exceso. *Caso real del profesor*: Redujo un dataset industrial de **500 registros y \~760 variables** (bombas, torque, presión) a **\~25–30 variables clave**.  
> * **Muestreo, Estratificación y Binning** *(Clase 21\)*: Ante millones de tickets o lecturas de sensores cada segundo casi idénticas, se recomienda **estratificar** (por región norte/sur, tienda o categoría como lácteos sin mezclar zapatos) o **agregar por intervalos** (ej. promediar sensores cada 5 minutos). El **Binning** agrupa valores continuos en rangos manejables (ej. edades 0–10, 10–20, 20–30, 30–40) para reducir ruido y variables.  
> * **Principio de Longitud Mínima** *(Clase 21\)*: Busca el punto medio equilibrado entre la **simplicidad** del modelo (que genera mucho error) y su **complejidad excesiva** (que reduce el error pero provoca sobreajuste).  
> * **Umbrales de aceptación por dominio y costo del error** *(Clases 20 y 21\)*:  
  * *Ventas / Negocio general*: Arriba de **80%** suele considerarse bueno.  
  * *Medicina / Impacto científico crítico*: Se exige **90% o más**, sabiendo que **nunca existe el 100%** y el techo práctico ronda **93%–94%**.  
  * *Matriz de confusión según dominio*: En **medicina** (ej. cáncer sano / nivel 3 / nivel 5\) se toleran más falsos positivos para evitar falsos negativos mortales; en **crédito bancario y fraudes** se cuida reducir los falsos positivos para no aprobar clientes riesgosos ni bloquear tarjetas legítimas.

#### **c) Tabla de diagnóstico y pasos de corrección *(Clases 18, 20 y 21\)***

| Síntoma / Problema | Diagnóstico | Acciones correctivas concretas vistas en clase   |
| :---- | :---- | :---- |
| Train bajo, Test bajo | **Underfitting** | Pedir/agregar variables ricas al cliente, reducir correlación redundante |
| Train excelente, Test malo | **Overfitting** | **1\)** Regularización Ridge/Lasso; **2\)** *Dropout* en redes; **3\)** Simplificar/podar árboles; **4\)** *K-Fold Cross-Validation*; **5\)** *Data augmentation* y depuración variable por variable |
| Errores graves en Matriz de Confusión (ej. FN en cáncer) | Umbral o variables inadecuadas | **1\)** Revisar matriz e IDs de FP/FN; **2\)** Ajustar umbral; **3\)** Balancear clases; **4\)** Mejorar variables; **5\)** Probar 2–3 algoritmos; **6\)** Evaluar precisión, *recall*, F1 |
| Métricas colapsan al llegar el mes n+1 o n+2 | Modelo **no resistente al cambio** | Modelo mal construido; reentrenar con *K-Folds*, revisar deriva/variables y monitorear 3–6 meses |

#### **d) Errores comunes y puntos recalcados para examen *(Clases 18, 20 y 21\)***

> * **Tres criterios obligatorios de éxito de un modelo (Clase 18\)**: (1) Resolver el reto empresarial aportando valor real; (2) **resistir el cambio de datos** cuando entran meses nuevos (n+1, n+2); y (3) **comparar al menos dos modelos** antes de elegir (K-Means vs. DBSCAN, Holt-Winters vs. SARIMA, etc.).  
> * **Tiempo de monitoreo en producción**: Mínimo de **3 a 6 meses** después de implementar.  
> * **Creer en un 100% real**: El profesor enfatizó que si un modelo en pruebas da 100%, probablemente memorizó; el máximo realista ronda 93%–94%.

## ---

**LO QUE MÁS PROBABLEMENTE VIENE EN EL FINAL**

> 1. **Mapeo de problemas de negocio a tipo de modelo y algoritmo (con foco en Clasificación Binaria)** \* *Evidencia*: En Clase 18, tras corregir a un alumno en el caso de fraude bancario en tiempo real, el profesor dijo **explícitamente**: *"Recuerden esa parte binaria de clasificación, es muy importante; en el examen vendrá una pregunta como estas... no es la misma, pero va a ser similar"*.  
> 2. **Diferencias entre Modelo Predictivo y Modelo Descriptivo (y Supervisado vs. No Supervisado)** \* *Evidencia*: Lo recalcó en Clases 6 y 18 diciendo: *"Ese es un punto bien importante. Tienen que tener bien claro qué cosa es un modelo predictivo y descriptivo"*, exigiendo conocer qué tipo de datos requiere cada uno (etiquetados/estructurados vs. sin etiquetas) y sus métricas.  
> 3. **Diferencia entre Regresión y Clasificación** \* *Evidencia*: En Clases 6, 12 y 13 lo preguntó directamente a los alumnos (Martínez) y reiteró que la clasificación es su algoritmo estrella, diferenciándose de la regresión porque predice categorías discretas/binarias en lugar de un valor numérico continuo.  
> 4. **Identificación visual de gráficas de Series de Tiempo (Tendencia, Estacionalidad, Estacionaria) y elección del modelo** \* *Evidencia*: En Clase 15 proyectó gráficas y anunció **explícitamente**: *"Esta es una pregunta de examen"*, pidiendo distinguir tendencia, estacionalidad y series estacionarias, y asignar Holt-Winters, ARIMA o SARIMA a casos de comercio, banca o consumo eléctrico.  
> 5. **Interpretación de la Matriz de Confusión (FP vs. FN), ajuste de umbral y acciones por dominio** \* *Evidencia*: En Clases 12, 13, 15, 16 y 21 insistió en que la matriz de confusión es el elemento de mayor valoración: exigió en las prácticas sacar la lista por ID de falsos positivos/negativos, y en Clase 21 explicó el caso de cáncer señalando cuándo tolerar más FP (medicina) vs. reducir FP (crédito bancario).  
> 6. **Diagnóstico de *Underfitting*, *Overfitting* y *Good Fitting* \+ 5 formas de prevenir el sobreajuste** \* *Evidencia*: En Clase 21 señaló directamente: *"muchos de ustedes mismos ya me lo han hasta contestado en el examen"*, desglosando cómo se ve cada uno en entrenamiento vs. prueba y cómo corregirlo (Ridge/Lasso, *dropout*, poda, *K-Folds*, *data augmentation*).  
> 7. **Proceso integral de Minería de Datos, triple ajuste de hiperparámetros y criterios de robustez** \* *Evidencia*: Al cerrar el Tema 3 en Clase 18 (13 actividades, triple ajuste incluyendo el *"último apretoncito"*, monitoreo 3–6 meses, resistencia al cambio de datos n+1 y comparación ≥ 2 modelos), sentenció: *"Eso es el examen. El examen va a ser exactamente sobre todo el tema"*.  
> 8. **CRISP-DM (6 fases) frente a KDD y al proceso técnico** \* *Evidencia*: En Clases 20 y 21 dedicó la teoría central a contrastar KDD (académico) vs. CRISP-DM (estándar industrial de 6 fases desde negocio hasta despliegue), confirmando que el examen del tercer parcial cubre *"todo lo que hemos visto"*.  
> 9. **Los 3 Niveles de Validación y métricas de Reglas de Asociación (Soporte, Confianza, Lift)** \* *Evidencia*: En Clase 10, al enumerar los 3 niveles de validación (técnica/métricas, operativa/negocio y ejecutiva), dijo **explícitamente**: *"Es pregunta de examen"*.  
> 10. **Diseño de una Arquitectura de Datos y tipos de bases de datos (Warehouse, Lake, Vectorial)**  
    * *Evidencia*: En Clase 4 afirmó textualmente: *"Una de las preguntas que \[viene en\] examen es crear arquitectura de \[datos\]"*, señalando que se deben definir requerimientos funcionales y no funcionales; además insistió en distinguir Data Warehouse, Data Lake y bases vectoriales.  
> 11. **Validación Cruzada (*K-Folds*, *Stratified*, *Group K-Fold*) y Selección de Red Neuronal (MLP vs. CNN vs. RNN)**  
    * *Evidencia*: Aunque son prácticas que ya aplicaron, en Clase 21 resumió formalmente por qué 70/30 no basta en medicina (*Group K-Fold*), y en Clases 16, 20 y 21 evaluó la justificación de arquitectura según el tipo de dato (tabular → MLP, imagen → CNN, secuencia → RNN).

## ---

**CONEXIONES CLAVE**

> 1. Arquitectura de datos \-\> provee y asegura \-\> datos confiables para el modelado  
> 2. Repositorio de datos \-\> añade metadatos y seguridad sobre \-\> bases de datos convencionales  
> 3. Data Lake \-\> almacena datos crudos y multimedia antes de \-\> estructurarse en un Data Warehouse  
> 4. Data Mart \-\> extrae una vista especializada desde \-\> el Data Warehouse corporativo  
> 5. Base de datos columnar en RAM \-\> acelera consultas analíticas frente a \-\> tablas tradicionales en disco  
> 6. Base de datos vectorial \-\> convierte texto e imágenes en *embeddings* para \-\> búsquedas por similitud semántica  
> 7. Spark \-\> procesa en memoria RAM superando en velocidad a \-\> MapReduce en disco de Hadoop  
> 8. CRISP-DM \-\> amplía con enfoque de negocio y despliegue al \-\> marco académico KDD  
> 9. Fase 4 de CRISP-DM (Modelado) \-\> aloja el núcleo técnico llamado \-\> proceso de Minería de Datos  
> 10. Falta de historial suficiente \-\> obliga a cancelar en Fase 2 \-\> proyectos de Series de Tiempo  
> 11. Modelos descriptivos \-\> emplean aprendizaje no supervisado para \-\> descubrir clústeres y asociaciones  
> 12. Modelos predictivos \-\> exigen datos etiquetados y estructurados para \-\> estimar valores o clases futuras  
> 13. StandardScaler \-\> iguala magnitudes numéricas para \-\> evitar sesgos en PCA, K-Means y KNN  
> 14. PCA \-\> reduce variables correlacionadas en componentes principales para \-\> visualizar y acelerar el clustering  
> 15. Método del Codo (WCSS) \-\> sugiere el número óptimo K para \-\> inicializar K-Means  
> 16. DBSCAN \-\> agrupa por densidad ε superando a K-Means al \-\> detectar ruido y formas no esféricas  
> 17. Coeficiente de Silueta \-\> mide cohesión y separación para \-\> comparar algoritmos de clustering  
> 18. Reglas de asociación \-\> buscan combinaciones frecuentes en tickets que \-\> complementan la segmentación de clientes  
> 19. Lift mayor a 1 \-\> confirma una asociación real por encima de \-\> compras básicas coincidentes al azar  
> 20. FP-Growth \-\> comprime transacciones en un *FP-Tree* escalando mejor que \-\> Apriori en grandes volúmenes  
> 21. Regresión \-\> predice una variable objetivo continua a diferencia de \-\> la clasificación discreta o binaria  
> 22. Lasso \-\> elimina variables no significativas mientras que \-\> Ridge conserva y pondera las colineales  
> 23. Clasificación binaria \-\> responde decisiones dicotómicas críticas como \-\> fraude bancario o diagnóstico médico  
> 24. Matriz de confusión \-\> desglosa falsos positivos y falsos negativos para \-\> calibrar el umbral de decisión  
> 25. F1-Score y Recall \-\> evalúan modelos desbalanceados mejor que \-\> la exactitud (*accuracy*) simple  
> 26. Prueba ADF y diferenciación \-\> transforman una serie no estacionaria para \-\> hacerla apta para ARIMA y SARIMA  
> 27. Holt-Winters \-\> modela nivel, tendencia y estacionalidad sin exigir \-\> estacionariedad previa como ARIMA  
> 28. Neurona artificial \-\> pondera entradas más *bias* mediante \-\> funciones de activación (ReLU, Sigmoide, Softmax)  
> 29. Arquitectura CNN \-\> extrae patrones espaciales en imágenes reduciendo parámetros frente a \-\> redes densas MLP  
> 30. Validación cruzada (*K-Folds*) \-\> promedia múltiples rotaciones de prueba para \-\> evitar particiones 70/30 sesgadas y sobreajuste  
> 31. Dropout, poda y regularización \-\> previenen la memorización detectada cuando \-\> el entrenamiento supera ampliamente a la prueba  
> 32. Principio de longitud mínima \-\> equilibra simplicidad contra complejidad buscando \-\> minimizar error sin caer en sobreajuste  
> 33. Criterio de robustez empresarial \-\> exige comparar mínimo dos modelos y \-\> resistir datos nuevos en monitoreo de 3 a 6 meses

---

🎯 ¿Quieres que armemos un **examen simulacro completo** (con ejercicios de mapeo de problemas, gráficas de series de tiempo, una matriz de confusión para diagnosticar y una arquitectura de datos) o prefieres repasar primero alguno de los bloques técnicos que sientas más flojo?

## **Anexo · Clases que no estaban en el cuaderno de NotebookLM**

*Resumen para estudiar de cada una, tomado de los apuntes por clase del sitio (decimo/MD/MD-Resumenes/).*

### **Clase 19 · Segundo Examen Parcial (jueves 5 nov 2026\)**

*Lo que conviene verificar al recibir la calificación.*

| Pendiente | Qué hacer   |
| :---- | :---- |
| Calificación | Anotarla cuando la den |
| Redes neuronales (capas y neuronas) | Repasar la Clase 16, porque esa parte quedó sin responder |
| Entrega en Classroom | Confirmar el estado del examen y de la práctica MLP |

