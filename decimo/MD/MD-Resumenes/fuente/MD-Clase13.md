% materia: Minería de Datos
% titulo: Clase 13 · Reglas de asociación (cierre) y clasificación
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 15 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Cierre de las exposiciones de la Práctica 3.2 (análisis de canasta)
Apriori y FP-Growth sobre tickets: Requerimiento A (catálogo general) y B (comidas preparadas). Objetivo: encontrar productos "gancho" que venden a otros.
- **One-hot encoding:** las transacciones venían en varias filas por ticket; se convierten a **una fila por ticket** con columnas 1/0 por producto.
- **Agrupar por líneas:** con 479 productos individuales la matriz era tan dispersa que nada llegaba al soporte mínimo; agrupados en **62 líneas** mejoró la detección.

| Caso | Parámetros | Reglas destacadas |
|---|---|---|
| A (general, 11,344 tickets) | Soporte mín. 1 %, confianza 30–50 % | Yogur griego fresa → mora (confianza 70 %); chorizo + queso americano → crema dulce (soporte 2.8 %, confianza 44.8 %, **lift 3.71**) |
| B (comidas, 2,480 tickets) | Soporte 0.5 %, confianza > 15–20 %, lift > 1.5 | Pastas y quesos como antecedente de burritos y flautas |
| Lift extremos | — | Lift 82 y 136 en sabores (yogur pistache → vainilla; uva → ponche); "Regla 90" (soporte 0.05 %, confianza 90–92 %) |

!!! Estrategia de negocio
Promedio de **1.48 productos por ticket**. No descontar el **antecedente** (el producto ancla que el cliente ya busca): poner el incentivo en el **consecuente** o armar combos, para subir la canasta hacia 2.
**Apriori vs. FP-Growth:** dan exactamente los mismos conjuntos frecuentes y reglas; cambia el costo (muchos escaneos vs. un FP-Tree en dos escaneos).

## 2. Preparación de datos para clasificación
La etapa que más inteligencia requiere, según el profesor; una buena selección de variables vale más que el algoritmo.
- Eliminar variables con varianza casi cero, muy correlacionadas o sesgadas (p. ej. "embarazada" en población mixta).
- **Variable dominante:** si una sola explica ≈ 90 % del resultado (glucosa en diabetes), se quita del entrenamiento para ver el peso real de las demás.
- **Bins:** las continuas (glucosa, edad, ingresos) se discretizan en rangos con conocimiento experto (edad < 18, 18–25, … > 50; glucosa baja/media/alta), para que el algoritmo no se atasque con infinitos decimales.

## 3. Los seis algoritmos y sus hiperparámetros
| Algoritmo | Idea | Hiperparámetros / nota |
|---|---|---|
| Árbol de decisión | Raíz, nodos internos y hojas; cortes por Gini o entropía | `max_depth`, máximo de hojas (contra sobreajuste) |
| Random Forest | Muchos árboles que votan | `n_estimators`, `max_depth`, `random_state` (cambiar la semilla para comprobar estabilidad) |
| Regresión logística | Sigmoide entre 0 y 1 | `max_iter`. Churn: identificar por nombre a clientes con saldo < $3,000, 18–25 años, ingresos $20–40 mil y alta probabilidad de irse |
| Naive Bayes | Probabilístico | Gaussiano (continuos, biológicos); multinomial (texto, spam, sentimiento) |
| KNN | Vecinos más cercanos | Distancia euclidiana o Manhattan |
| SVM / SVC | Hiperplano con margen entre vectores de soporte | Penalización **C** y kernel (lineal o no lineal) |

## 4. Métricas de clasificación
| Métrica | Fórmula / lectura |
|---|---|
| Matriz de confusión | VP y VN aciertos; FP y FN errores. Sacar la **lista de casos FP y FN** para auditar por qué falló |
| **Precisión** | VP / (VP + FP) |
| **Recall** (sensibilidad) | VP / (VP + FN) |
| **F1** | Media armónica de precisión y recall |
| **AUC-ROC** | ≈ 1.0 discrimina muy bien; ≈ 0.5 no es mejor que el azar |
| **K-fold** | K bloques: se entrena con K − 1 y se prueba con 1, K veces; el resultado no depende de un corte afortunado |
!!! Pregunta principal al evaluar
Auditar FP y FN: decir que un paciente no tiene leucemia cuando sí, o que un cliente es leal cuando se va a ir. Una exactitud alta con datos desbalanceados no basta.

## Avisos
- Práctica 3.4 (Clasificación, 6 algoritmos en Python): vence jueves 22 oct, 1:00 p. m. Al exponer, 3 preguntas: cómo seleccionaron y limpiaron variables, cómo interpretaron FP y FN, y la propuesta de negocio.
- Próximo tema: series de tiempo (ARIMA, suavizado exponencial).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Canasta.** One-hot (una fila por ticket); agrupar productos en líneas si la matriz es muy dispersa. Apriori y FP-Growth dan lo mismo, cambia el costo. **Descuento al consecuente, nunca al antecedente.**

**Preparar datos.** Quitar varianza ≈ 0, correlacionadas y sesgadas; quitar la variable dominante para ver las demás; continuas a bins.

!!! Métricas (examen)
Precisión = VP/(VP+FP). Recall = VP/(VP+FN). F1 = media armónica. AUC-ROC: 1 excelente, 0.5 azar. K-fold contra el sobreajuste. Siempre auditar FP y FN.

| Algoritmo | Perilla clave |
|---|---|
| Árbol | max_depth, hojas |
| Random Forest | n_estimators, random_state |
| Logística | max_iter |
| Naive Bayes | Gaussiano / multinomial |
| KNN | Euclidiana / Manhattan |
| SVM | C y kernel |
