% materia: Minería de Datos
% titulo: Clase 18 · El proceso de minería de datos y series de tiempo (Práctica 3.5)
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 3 nov 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Metodología completa de un proyecto de minería de datos (13 actividades, triple ajuste, robustez), ejercicio de identificar el algoritmo según el problema y exposiciones de la Práctica 3.5 (pronóstico de ventas con Holt-Winters y SARIMA). Continúa la Clase 16.

!!! Fuente
NotebookLM (audio MD-Clase18.m4a). Las cifras de las exposiciones son de los equipos, no del profesor. Lo que no se pudo contrastar con el audio se marca como dudoso.

## 1. KDD y minería de datos
- **KDD** es el macroproceso: desde las entrevistas de negocio hasta la puesta en operación. La **minería de datos** es el «kernel», el núcleo técnico.
- El proyecto arranca con una reunión con directivos para evaluar si el problema es abordable; si no hay viabilidad, se detiene.
- También se puede cancelar tras explorar los datos: con solo 3 o 4 meses de historial es imposible un pronóstico confiable de series de tiempo.
Error común: creer que la minería de datos abarca todo el proceso de negocio por sí sola.

## 2. Modelos predictivos y descriptivos
| | Predictivo | Descriptivo |
|---|---|---|
| Datos | Etiquetados y estructurados | Sin etiquetas; estructurados o no |
| Salida | Estimación hacia el futuro | Clusters o reglas de asociación |
| Se evalúa con | Exactitud y error (precisión, residuos) | Cohesión de los grupos y confianza de las reglas |
!!! Examen
El profesor dijo: «Tienen que tener bien claro qué cosa es un modelo predictivo y descriptivo.»

## 3. Ejercicio: ¿qué algoritmo usar?
| Caso | Respuesta |
|---|---|
| Sensores de máquinas para predecir fallas | Series de tiempo, regresión y árboles de decisión (se pueden combinar) |
| Transacciones bancarias sospechosas (fraude) | **Clasificación** binaria: ¿es anómalo o no? (un alumno dijo series de tiempo y el profesor lo corrigió) |
| Qué productos se venden más por temporada y fechas | Series de tiempo |
| Grupos de clientes parecidos para promociones | Agrupamiento (K-means) |
!!! Examen
«Recuerden esa parte binaria de clasificación, es muy importante; en el examen vendrá una pregunta como estas… no es la misma, pero va a ser similar.»

## 4. Las 13 actividades del proceso
1. Definición del problema (reunión con directivos).
2. Exploración y viabilidad de los datos (historial, SQL, APIs, infraestructura).
3. Preprocesamiento (codificación, normalización, escalado, limpieza).
4. Selección del algoritmo.
5. Selección de variables y reducción de dimensionalidad (por ejemplo con 70 atributos).
6. Partición de datos: 80/20, 70/30 o K-Fold.
7. Entrenamiento y **primer ajuste** (hiperparámetros por defecto).
8. **Tuning**: optimización deliberada de hiperparámetros.
9. Evaluación con métricas (F1 en clasificación; MAE/RMSE en regresión). Un rendimiento mediocre, como 70%, obliga a regresar.
10. Validación cruzada.
11. Validación con el cliente y **«último apretoncito»** (tercer ajuste).
12. Puesta en producción.
13. Monitoreo continuo: mínimo de 3 a 6 meses.
!!! Examen
El ajuste de hiperparámetros ocurre en tres momentos: inicial por defecto, tuning y último apretoncito tras validar con el cliente. El profesor concluyó: «El examen va a ser exactamente sobre todo el tema.»
Error común: dar el modelo por terminado tras el primer entrenamiento, o saltarse el monitoreo.

## 5. Criterios de éxito y robustez
- **Alineado al reto del negocio:** aporta valor real, no solo métricas teóricas.
- **Resistente al cambio de datos:** debe mantenerse estable con los datos del mes n+1 o n+2; si se descompone, estuvo mal entrenado o sobreajustado.
- **Comparar al menos dos modelos:** «¿Recuerdan que siempre corríamos dos?», por ejemplo K-means contra DBSCAN, o Holt-Winters contra SARIMA.

## 6. Práctica 3.5: pronóstico de ventas de Tempra (cifras de los equipos)
- Datos: 7 plazas (CDMX, Guadalajara, Guanajuato, Morelia, Puebla, Querétaro, Veracruz), 2016–2020, 420 registros; 48 meses de entrenamiento (2016–2019) y 12 de prueba (2020); pronóstico hacia 2021.
- Alternativa que recomendó el profesor: entrenar con N meses y predecir el siguiente (por ejemplo 6 y proyectar el 7.º) para compararlo con la realidad.
- **Anomalías:** Guadalajara 2018 con ventas en cero y 190 unidades, corregido imputando el promedio de los mismos meses de otros años; datos idénticos de Querétaro y Veracruz (probable error de captura); pico de marzo 2020 por compras de pánico (COVID-19), que el profesor aplaudió que un equipo relacionara con el contexto de salud pública.
- **Escala temporal:** mensual. Se descartó la trimestral porque aplanaba el pico de marzo y la caída de agosto y daba más error.
- **Modelos:** SARIMA (estacionalidad anual, residuos y prueba ADF) y Holt-Winters (estacionalidad regular y picos aislados).
- **Horizonte (Equipo 5):** el error crece con la distancia: 5.33% a 1 mes, 3.60% a 3 meses y hasta 11.48% más lejos; recomendaron 1 a 3 meses con reentrenamiento móvil.
- **Resultados del Equipo 5:** CDMX ganó SARIMA (11.48% contra 13.56%); Guadalajara ganó Holt-Winters (SARIMA 94.73% por los ceros); Guanajuato Holt-Winters 7.23%; Morelia SARIMA 23.60% contra casi 50%; Querétaro y Veracruz Holt-Winters 8.69%. Puebla: SARIMA 29.43% (dudoso si superó a Holt-Winters).
Moraleja: ningún modelo es universalmente mejor; depende de la estacionalidad, las anomalías y la escala temporal.
Dudoso: NotebookLM dijo que un ADF mayor a 0.05 indicaba ruido blanco; no se contrastó con el audio.

## Contexto — no examen
- Analogía del médico que manda estudios antes de recetar.
- La IA descansa en estos mismos principios de machine learning.
- Bromas al configurar proyectores sobre un foco controlado desde una app.
- Analogía del clima: mañana se acierta, a varios meses casi no.

## Pendiente
- **Práctica de redes neuronales (MLP):** entrega el viernes (6 nov): diapositivas de PowerPoint, resumen escrito y código Python completo con datos. No inventar datos; se vale apoyarse en ChatGPT, Google o repositorios si se entiende cada paso. Exposición de máximo 5 minutos por equipo.
- **Examen:** la siguiente sesión, probablemente en computadora, sobre todo el temario del curso.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Tema | Idea para recordar |
|---|---|
| KDD vs minería | KDD = todo el proceso; minería = el kernel técnico |
| Predictivo | Datos etiquetados; estima el futuro; exactitud y error |
| Descriptivo | Sin etiquetas; clusters y reglas; cohesión y confianza |
| Fraude | Clasificación binaria, no series de tiempo |
| Ventas por temporada | Series de tiempo |
| Grupos de clientes | Agrupamiento (K-means) |
| Triple ajuste | Default, tuning, último apretoncito con el cliente |
| Monitoreo | Mínimo 3 a 6 meses |
| Robustez | Valor de negocio, resistir datos nuevos, comparar al menos dos modelos |
| Series de tiempo | Mensual mejor que trimestral; horizonte corto de 1 a 3 meses; Holt-Winters vs SARIMA |

!!! Hilo conductor
Un buen proyecto de minería de datos empieza decidiendo si es viable y qué tipo de problema es, se afina en tres momentos, se compara contra al menos otro modelo y se vigila en producción.
