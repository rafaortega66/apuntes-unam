% materia: Minería de Datos
% titulo: Clase 22 · Proyectos de redes neuronales e inicio del Tema 5
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 17 nov 2026 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Exposiciones de los alumnos con redes neuronales (autoencoder convolucional, MLP en datos tabulares, RNN/LSTM en series de tiempo) con la retroalimentación del profesor; inicio del Tema 5: reglas rudimentarias, modelación estadística y Big Data. Lineamientos del tercer examen (todo el curso) y del proyecto final.

!!! Fuente
Fuente: NotebookLM (audio `MD-Clase22.mp3`), 19 nov 2026. El profesor dijo explícitamente que el tercer examen cubre todo el curso; el resto de la sección de examen sale de lo que enfatizó. Los números de las exposiciones son los que presentaron los equipos.

## 1. Exposiciones: autoencoder convolucional para defectos en botellas
Una CNN armada como autoencoder para inspección visual de botellas sin necesitar miles de ejemplos de defectos.

!!! En simple
Un artesano que se aprende de memoria cómo es una botella perfecta; al darle una dañada, intenta dibujarla sana y la diferencia entre su dibujo y la real revela el daño. Límite: si cambian mucho la iluminación o la posición, confunde sombras con defectos.

**Datos:** 209 imágenes normales para entrenar; para prueba, 20 con daño grande, 22 con daño pequeño, 21 con contaminación y 20 en buen estado. Las imágenes RGB de 900×900 se redujeron a 256×256 para aligerar el cómputo.

**Entrenamiento:** autoencoder con entrada y salida de 256×256×3, pérdida de error cuadrático medio (MSE), máximo 100 épocas.

**Detección:** se calcula un mapa de error de reconstrucción entre la imagen original y la reconstruida y se le aplica un umbral para obtener una máscara binaria de anomalías.

**Resultados:** a nivel imagen detecta bien las anomalías, pero falla al localizar el daño píxel por píxel. Al subir el umbral mejora la precisión pero baja mucho el recall.

Error común: segmentar sin calibrar el umbral: salen muchos falsos positivos o se pierden defectos pequeños.

## 2. Exposiciones: perceptrón multicapa (MLP) en datos tabulares
Red densa hacia adelante para registros en renglones y columnas: fraude financiero y detección de intrusiones.

!!! En simple
Un panel de analistas que revisa monto, hora e intentos de acceso; si la combinación de señales pasa de cierto nivel, marcan la transacción como sospechosa. Límite: no sirve donde importa la posición relativa, como en píxeles o palabras.

**¿Por qué no CNN en una tabla?** Porque las columnas no tienen vecinos espaciales como los píxeles; la convolución no tiene sentido.

**Fraude (473 casos fraudulentos):** `RobustScaler` sobre tiempo y monto; partición 70 % entrenamiento, 15 % validación y 10 % prueba (así se presentó). Dos capas ocultas con ReLU, salida sigmoide, Batch Normalization y Early Stopping, que paró en la época 22. Con el umbral de decisión en 0.997: 56 fraudes detectados, 42,477 normales correctas, 15 falsos positivos y 11 falsos negativos (detecta 4 de cada 5 fraudes).

**Intrusiones (NSL-KDD):** 125,973 registros de entrenamiento/validación y 22,544 de prueba. Se quitaron variables constantes o irrelevantes como `num_outbound_cmds` (toda en ceros) y `difficulty_level`. Se probaron arquitecturas de 1 a 3 capas con regularización L2 (alpha), optimizando el F1-score.

Por qué importa: es el estándar para clasificar datos transaccionales y se lee con la matriz de confusión: falsas alarmas contra ataques o fraudes no detectados.
Error común: dejar columnas con varianza cero o no regularizar, lo que lleva a sobreajuste.

## 3. Exposiciones: RNN y LSTM en series de tiempo
Redes con memoria interna para datos que dependen del tiempo.

!!! En simple
Leer un libro recordando los capítulos anteriores para entender el giro actual, en vez de leer cada página aislada. Límite: no anticipa un choque externo sin precedentes en el historial.

**Ozono (LSTM):** predecir con 3 horas de anticipación si el ozono pasa de 90 ppm entre las 14:00 y 17:00, con 32 neuronas y una ventana de 12 horas. Entrenamiento 2015–2022, validación 2023 y prueba 2024. Acertó 60 %, contra 23 % de solo mirar el valor de 3 horas antes.

**Actividad económica (IGAE del INEGI):** serie mensual de 404 registros (1993–2026), partición 80/20 y ventanas de 12 meses. La primera versión, que predecía el valor del índice, dio MAE de 5.68 puntos y MAPE de 5.65 %. La segunda predijo los **cambios mensuales** escalados con `StandardScaler`: MAE de 1.94 y MAPE de 2.5 % (66 % menos error).

Por qué importa: transformar una serie no estacionaria en diferencias mejora mucho la generalización.
Error común: predecir los valores brutos de una serie con tendencia sin diferenciarla.

## 4. Tema 5: reglas rudimentarias
Modelos de decisión con condiciones simples hechas a mano («si pasa A, haz B»), basadas en la experiencia o en prácticas empíricas, sin aprendizaje automático.

!!! En simple
Las reglas de cocina de la abuela: «si la masa está pegajosa, échale harina». Límite: no funcionan cuando intervienen decenas de factores que interactúan de forma no lineal.

No requieren optimización ni entrenamiento. Ejemplos que dio:
- **Regla 80/20 (Pareto):** el 20 % de las causas genera el 80 % de los efectos; en optimización se atienden los 20 problemas o clientes principales en vez de los 100.
- **Regla 3-2-1 de respaldos:** 3 copias, en 2 medios distintos, 1 fuera del sitio.

| | Reglas rudimentarias | Machine learning |
|---|---|---|
| Complejidad | Simples | Complejos |
| Interpretabilidad | Alta | Menor |
| Cómo se construye | Lógica manual humana | Aprendizaje automático |
| Variables | Muy pocas | Cientos a la vez |

El profesor dijo que de estas reglas surgieron históricamente los árboles de decisión, los sistemas expertos y la lógica difusa, y que prepararía preguntas sobre este contraste.

Error común: querer resolver problemas con muchas variables solo con reglas fijas.

## 5. Tema 5: modelación estadística
Transformar datos en ecuaciones (sobre todo lineales, de primer grado) basadas en supuestos teóricos, para explicar la relación entre variables y proyectar comportamientos.

!!! En simple
Calcular la gasolina con gasto = distancia × consumo por km. Límite: falla cuando entran el tráfico, el desgaste del motor o el clima.

Se toma una variable dependiente (el ejemplo de clase: ventas mensuales) y se estima combinando linealmente pocas variables explicativas con coeficientes calculados estadísticamente. Requiere conocimiento formal de probabilidad y estadística, es sensible a la calidad de los datos y depende de que se cumplan sus supuestos.

**Estadística contra machine learning:** la estadística se centra en la inferencia y en explicar relaciones con pocas variables bajo supuestos formales; el machine learning busca precisión predictiva con muchos datos y alta dimensionalidad, de forma automática.

Error común: suponer linealidad en fenómenos complejos o extrapolar fuera del rango donde valen los supuestos.

## 6. Tema 5: Big Data
Toda la infraestructura, almacenamiento, herramientas de procesamiento y capacidad analítica para capturar, transformar y procesar enormes volúmenes y variedades de datos, en tiempo real y por lotes.

!!! En simple
La red de agua de una ciudad: no es «mucha agua», sino presas, acueductos, plantas de filtrado y tuberías para llevarla a donde se necesita.

El profesor recalcó que decir que Big Data son «muchos datos» o «grandes volúmenes» **se queda corto**.

**Arquitectura:**
- **Fuentes:** bases SQL y NoSQL, ERP (compras, inventarios, contabilidad, facturación), CRM, sensores IoT, archivos planos y streaming (Kafka).
- **Procesamiento y analítica:** cómputo distribuido en memoria (Apache Spark), data lakes y data warehouses, entrenamiento con TensorFlow/PyTorch o MLflow.
- **Salidas:** dashboards, móviles y modelos en producción.

**Ejemplo bancario:** millones de transacciones por segundo de cajeros, apps y sucursales que se procesan a la vez para conciliar operaciones y disparar la detección de fraudes.

Por qué importa: se conecta con la fase de despliegue de CRISP-DM.
Error común: pensar que Big Data es solo tener discos enormes e ignorar la latencia, la integración de formatos y la velocidad de consulta.

## Contexto (no examen)
- Durante las exposiciones se oyó por megáfono una protesta estudiantil sobre la falta de luz y agua en la facultad y otras demandas.
- El profesor bromeó con que entrega las calificaciones en persona para que el alumno pueda inconformarse.

## Pendiente / próxima clase
- **Tercer examen parcial: todo el curso** («me puedo hacer una pregunta de cualquiera de los cinco temas»), en computadora. Según NotebookLM, el profesor lo **recorrió al jueves 26 de noviembre** para dar más tiempo de estudio; conviene confirmarlo en Classroom.
- **Proyecto final (individual):** cada alumno tiene un caso asignado de una empresa ficticia con nombre y cobertura territorial. Las 6 fases de CRISP-DM, con énfasis en la Fase 1 (comprensión del negocio) y la Fase 6 (despliegue). **Exactamente 10 diapositivas** («ni una más, ni una menos»), diseño profesional con logotipo y colores formales, más el notebook de Python (no se penaliza si los datos son aproximados; importa la coherencia entre algoritmo y problema). Exposición de máximo 5 minutos por persona; NotebookLM dice que la entrega es el día de la sesión a la 1:00 p. m. (falta confirmar el día exacto).
- **Calificaciones finales:** en persona, en el horario de clase del martes siguiente.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **El tercer examen cubre todo el curso.** lo dijo textualmente.
- **Reglas rudimentarias contra machine learning.** dijo que prepararía preguntas sobre ese contraste.
- **Big Data no es solo «muchos datos».** lo repitió como respuesta que se queda corta.
- **Modelación estadística contra machine learning.** lo explicó con ecuaciones de primer grado.
- **Qué red usar según los datos: CNN imágenes, MLP tablas, RNN/LSTM secuencias.** lo comentó en todas las exposiciones.

!!! Puntos clave
- Reglas rudimentarias: manuales, interpretables, pocas variables (Pareto 80/20, respaldo 3-2-1); origen de árboles de decisión, sistemas expertos y lógica difusa.
- Modelación estadística: ecuaciones con supuestos, inferencia, pocas variables.
- Big Data: fuentes heterogéneas + procesamiento distribuido + analítica + salidas.
- MLP para tablas (sin vecindad espacial); en series con tendencia, predecir diferencias.
- Umbral más alto → más precisión, menos recall.

## Ponte a prueba
1. **¿Por qué definir Big Data como «muchos datos» es incompleto?** Porque implica la arquitectura para integrar fuentes (ERP, IoT, streaming, SQL/NoSQL), procesarlas (Spark) y alimentar analítica, modelos y tableros.
2. **¿Qué es la regla 3-2-1?** 3 copias de respaldo, en 2 medios distintos, 1 fuera del sitio.
3. **Regla rudimentaria contra machine learning.** La regla es manual, rígida y con pocas variables; el ML aprende de los datos y maneja muchas variables.
4. **¿Por qué falló la primera RNN del IGAE y cómo se corrigió?** Predecía el valor bruto del índice; la segunda predijo cambios mensuales escalados y bajó el MAPE de 5.65 % a 2.5 %.
5. **¿Por qué MLP y no CNN para fraude?** Las columnas de una tabla no tienen vecindad espacial como los píxeles.
6. **¿Qué pasó al subir el umbral en el autoencoder de botellas?** Subió la precisión y bajó mucho el recall.
7. **¿Qué es la modelación estadística y su limitación?** Ecuaciones (lineales) que explican relaciones entre variables; depende de supuestos rígidos y es menos flexible ante relaciones no lineales.
8. **¿Qué ventaja tuvo la LSTM del ozono?** Acertó 60 % con 3 horas de anticipación contra 23 % de mirar el valor de 3 horas antes.
