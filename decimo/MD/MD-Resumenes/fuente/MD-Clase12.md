% materia: Minería de Datos
% titulo: Clase 12 · Reglas de asociación (Práctica 3.2) e introducción a la clasificación
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 13 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Exposiciones de la Práctica 3.2: análisis de canasta
Market Basket Analysis sobre **11,344 tickets**, comparando **Apriori** y **FP-Growth** en Python y RapidMiner. Cada producto cuenta una sola vez por ticket (campos: transacción, producto, descripción, cantidad, fecha, cliente).
| Requerimiento | Parámetros | Hallazgos |
|---|---|---|
| A — catálogo general | Soporte 1–2 % (114–227 tickets), confianza 30–50 %, lift > 1.1 | Jamón / salchicha / queso fresco → crema dulce o queso amarillo: **lift 2.19**, confianza 57–80 % |
| B — comidas preparadas (47–48 líneas, 2,480 tickets) | Soporte 0.5–2 % (50–194 tickets), confianza > 20–30 %, lift > 1.5 | Jamones, pastas o quesos como antecedente que detona burritos o flautas |
- **Gráfica de burritos:** la barra de antecedente era mucho mayor que la de consecuente: quien compra un burrito suele llevar otro o una bebida, pero casi nada lleva a comprar un burrito.
!!! Lift
**Lift > 1:** antecedente y consecuente se compran juntos más de lo que se esperaría por azar. Reglas con lift ≥ 1.5–1.6 son especialmente útiles comercialmente.
| Apriori | FP-Growth |
|---|---|
| Escanea la matriz muchas veces | Construye un **FP-Tree** en solo **dos escaneos** |
| Rápido en datos pequeños, se degrada con volumen | Cuesta más al inicio con pocos datos, escala mucho mejor |
Errores comunes: recomendar combinaciones obvias o quedarse en categorías demasiado generales sin bajar a submarca o sabor.

## 2. Clasificación supervisada
!!! Clasificación vs. regresión (examen)
La **regresión** predice un valor numérico **continuo** (precio, demanda). La **clasificación** decide entre **clases discretas** o binarias (sí/no, fraude/no fraude, aprobado/rechazado).
- Y discreta (¿abandona el cliente?, ¿diabetes tipo 2?); X = atributos históricos (glucosa, edad, saldo, clics).
- **Selección de variables:** quitar varianza casi cero, ruidosas o incompletas; quitar las que meten **sesgo** ("embarazada" en una población de hombres y mujeres); vigilar **variables dominantes** (si la glucosa explica el 90 %, ver si opaca a las demás).
- **Bins:** discretizar continuas en rangos (glucosa < 120 normal, 120–140 media, > 140 alta; humedad alta/baja) para que algoritmos como los árboles trabajen más rápido y preciso.

## 3. Los seis algoritmos
| Algoritmo | Cómo decide | Detalles |
|---|---|---|
| Árbol de decisión | Preguntas sí/no; cortes por Gini o entropía | Ej.: ¿se juega golf?, ¿se aprueba el préstamo? Riesgo de sobreajuste: limitar profundidad y hojas |
| Random Forest | Comité de árboles con subconjuntos aleatorios (bagging) que votan | `n_estimators`, profundidad, `random_state` |
| Regresión logística | Probabilidad con sigmoide (0 a 1) | Churn bancario; `max_iter` |
| Naive Bayes | Bayes suponiendo independencia entre variables | Texto, spam, sentimiento (gaussiano, multinomial) |
| KNN | Clase mayoritaria de los K vecinos | Euclidiana o Manhattan |
| SVM / SVC | Hiperplano de franja máxima entre vectores de soporte | Imágenes, control de calidad, fraude |

## 4. Métricas y validación
- **Matriz de confusión:** VP, VN, FP, FN. Auditar **por qué** se equivocó en los FP y FN y qué impacto tiene cada error.
- **AUC-ROC:** cuanto más cerca de 1, mejor discrimina frente al azar (0.5).
- **Validación cruzada K-fold:** K bloques (5 o 10) alternando entrenamiento y prueba, para resultados estables sin sobreajuste.
!!! Los 3 niveles de validación ("es pregunta de examen")
1. **Técnico:** validar las métricas del algoritmo (soporte, confianza, lift, matriz de confusión, R²).
2. **Negocio y operativos:** que la gente del día a día confirme que los hallazgos tienen sentido.
3. **Alta dirección:** alinear con la visión estratégica (el director holandés solo quería crecer 50 % en tiendas: sin este nivel, el proyecto no se implementa).
**Caso dengue:** 6 meses de desarrollo y 1 año de seguimiento con la Secretaría de Salud; cuatro módulos (diagnóstico, tratamiento, seguimiento, prevención); hemorragias asociadas a hepatitis y melena; desplegado en iPads en Chiapas, Tabasco, Guerrero y Oaxaca, cruzado con lluvia y temperatura.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Asociación.** Lift > 1 = se compran juntos más que por azar. Apriori: muchos escaneos; FP-Growth: FP-Tree en dos escaneos, escala mejor. El burrito es antecedente, casi nunca consecuente.

**Clasificación.** Y discreta (regresión = continua). Quitar variables ruidosas, sesgadas o dominantes; discretizar en bins.

!!! Tres niveles de validación (examen)
Técnico (métricas) → negocio/operativo (tiene sentido en el día a día) → alta dirección (estrategia).

| Herramienta | Para recordar |
|---|---|
| Matriz de confusión | Auditar FP y FN |
| AUC-ROC | 1 = excelente, 0.5 = azar |
| K-fold | K bloques rotando prueba |
| 6 algoritmos | Árbol, Random Forest, logística, Naive Bayes, KNN, SVM |
