% materia: Minería de Datos
% titulo: Clase 19 · Segundo Examen Parcial
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 5 nov 2026 · Día de examen · Resumen de examen

# PARTE 1 · El examen

!!! Datos
Individual; PDF `Examen2OrtegadelaPazRafael.pdf` de las 16:39 del 5 nov (en `decimo/MD/MD-Examenes/MD-E02/`). **No hay registro de la calificación** ni del texto de Classroom. El profesor lo anunció en la Clase 18 como un examen de todo el temario.

## Qué preguntó y qué respondí
| # | Pregunta | Mi respuesta, en corto |
|---|---|---|
| 1 | 3 desafíos del aprendizaje supervisado | Calidad de variables, sobreajuste, errores de la matriz de confusión |
| 2 | K-means vs DBSCAN (3 diferencias) y Mean Shift | Número de grupos previo, forma, outliers; Mean Shift: ventana que se desplaza hacia la mayor densidad |
| 3 | Clasificación: propósito, algoritmos y métricas | Árboles, Random Forest, regresión logística, KNN, SVM, Naive Bayes, redes; matriz, accuracy, precisión, recall, F1, ROC/AUC, KS/Gini, K-Fold |
| 4 | Reducción de dimensionalidad | Eficiencia, sobreajuste, ruido; extracción y selección de características |
| 5 | StandardScaler, feature_importances_, t-SNE, Ridge/Lasso | Preprocesamiento, selección con árboles, visualización, regularización |
| 6 | Holt-Winters | Tres componentes, ponderación exponencial, 2 a 4 ciclos, MAPE/MAE/RMSE |
| 7 | ARIMA, SARIMA y ACF | AR, I, MA y la parte estacional; ACF con decaimiento lento si no es estacionaria |
| 8 | Redes neuronales | Componentes; MLP, CNN, RNN/LSTM; épocas por validación (sin responder capas y neuronas) |
| 9 | Actividades con el cliente | Negocio, EDA, limpieza, transformación, reducción, partición, modelado, evaluación, interpretación, despliegue |
| 10 | Casos de negocio a–h | Ver tabla de abajo |

## Casos de negocio (pregunta 10)
| Caso | Algoritmo |
|---|---|
| Reclamaciones | Random Forest o árboles (Naive Bayes para texto) |
| Epidemia | SARIMA o regresión |
| Precios | Regresión lineal o Ridge |
| Presupuestos | Regresión regularizada o series de tiempo |
| Rutas | DBSCAN o clustering jerárquico |
| Campañas | K-means + regresión logística |
| Inventarios | Holt-Winters o SARIMA |
| Diagnóstico médico | CNN (imágenes) o regresión logística y árboles (datos clínicos) |

## Dónde repasar
| Tema | Clases |
|---|---|
| Clustering | 9, 11 |
| Clasificación, métricas, validación cruzada | 12, 13, 15, 16 |
| Regresión, Ridge y Lasso | 11, 14 |
| Redes neuronales | 16 |
| Proceso con el cliente, robustez, series de tiempo | 18 |

# PARTE 2 · Para el siguiente
~ Lo que conviene verificar al recibir la calificación.

| Pendiente | Qué hacer |
|---|---|
| Calificación | Anotarla cuando la den |
| Redes neuronales (capas y neuronas) | Repasar la Clase 16, porque esa parte quedó sin responder |
| Entrega en Classroom | Confirmar el estado del examen y de la práctica MLP |
