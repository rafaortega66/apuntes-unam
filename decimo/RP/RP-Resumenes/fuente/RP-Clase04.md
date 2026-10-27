% materia: Reconocimiento de Patrones
% titulo: Clase 4 · Evaluación de modelos
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 7 sep 2026 (sesión 7 del curso) · Tema 4 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Repaso: PCA vs. LDA
| | PCA | LDA |
|---|---|---|
| Tipo | No supervisado | **Supervisado** (requiere etiquetas) |
| Maximiza | Varianza total | Separabilidad entre clases |
- Supuestos de LDA: gaussiana por clase, **homocedasticidad** (misma covarianza), separabilidad lineal.
- QDA = LDA con una covarianza por clase. t-SNE: visualización 2D/3D. Kernel PCA: kernel trick + PCA.

## 2. Matriz de confusión
Filas = clases reales; columnas = predichas; diagonal = aciertos.
| | Predicho + | Predicho − |
|---|---|---|
| Real + | VP | FN (**Tipo II**: incendio sin alarma; suele ser el peor) |
| Real − | FP (**Tipo I**: alarma sin fuego) | VN |

## 3. Métricas
| Métrica | Fórmula |
|---|---|
| Exactitud | (VP + VN) / total |
| Precisión | VP / (VP + FP) — de lo predicho positivo |
| Recall / sensibilidad | VP / (VP + FN) — de lo realmente positivo |
| Especificidad | VN / (VN + FP) |
| F1 | 2·P·R / (P + R), media armónica |
| Exactitud balanceada | (Sensibilidad + Especificidad) / 2 |
Ejemplo spam equilibrado: exactitud 90 %; precisión, recall y F1 = 85.7 %.

## 4. Curva ROC y AUC
Eje X = **FPR** = FP/(FP + VN) = 1 − especificidad; eje Y = **TPR** = recall. Se recorre el umbral.
| AUC | Lectura |
|---|---|
| 1.0 | Perfecto |
| 0.9–1.0 | Excelente |
| 0.7–0.9 | Bueno |
| 0.5–0.7 | Regular |
| 0.5 | Azar (diagonal) |
| < 0.5 | **Invertido**: detecta bien la clase contraria; basta con invertir la predicción |
Solo es inservible cerca de la diagonal.

## 5. Sesgo y varianza
- **Sesgo:** error sistemático por simplificar (arquero siempre a la izquierda). **Underfitting:** error alto en entrenamiento y validación (memorizar solo la fórmula del determinante).
- **Varianza:** sensibilidad al ruido (arquero disperso). **Overfitting:** error bajo en entrenamiento y alto en validación (memorizar exámenes pasados).
| Conjunto | Proporción | Para qué |
|---|---|---|
| Entrenamiento | 60–80 % | Parámetros |
| Validación | 10–20 % | Hiperparámetros, generalización |
| Prueba | 10–20 % | Intocable hasta el final |
- Degradación normal: 95 % → 91 % → 87 % no es overfitting.
- ¿Se arregla? Underfitting: entrenar más o modelo más complejo. Overfitting: regularización, aumentación, **early stopping**.

## 6. Datos desbalanceados
!!! Ejemplo de cáncer (examen)
1,000 pacientes: 950 sanos, 50 enfermos. "Todos sanos" → **exactitud 95 %** y **0 de 50** detectados (50 FN). La exactitud esconde un modelo inútil.
- Desbalance real: fraude ≈ 0.1 %; cáncer 1–5 %; intrusos ≈ 0.5 %.
- Remedios: F1, exactitud balanceada, ROC; pesos de clase; re-muestreo (oversampling sintético); umbral más exigente.

## 7. Esquemas de validación
- **Hold-out:** una división fija; sensible a la partición.
- **K-Fold:** se aparta la prueba y el resto se rota en K folds (por convención impar).
- **Stratified K-Fold:** mantiene la proporción de clases; obligatorio con desbalance.
- Preguntas en clase: entrenar con lo difícil y probar con lo fácil = "hacer trampa". La validación cruzada va **solo** dentro de entrenamiento/validación; luego se reentrena con todo y se evalúa una vez en prueba. Pocos folds en datasets chicos (200 imágenes); 9 o más en masivos; 15–20 no aporta en modelos simples.

## 8. Fuga de datos y data drift
- **Data leakage:** temporal (futuro para predecir pasado), de preprocesamiento (normalizar o PCA con todo el dataset), del target, en lenguaje (mostrar la palabra a predecir).
- **Data drift:** cambian las estadísticas en producción → degradación **silenciosa y progresiva**. Se reentrena desde cero con una **ventana móvil** de datos recientes.

## Pendiente
Viernes: exposición de la Práctica 1. Lunes: clasificadores.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Tipo I / Tipo II | FP (alarma sin fuego) / FN (fuego sin alarma) |
| Precisión / recall | VP/(VP+FP) / VP/(VP+FN) |
| ROC | TPR vs. FPR; AUC < 0.5 → invertir |
| Underfitting / overfitting | Error alto en ambos / bajo en train, alto en val |
| Desbalance | 95 % de exactitud con 0 enfermos detectados |
| Stratified K-Fold | Misma proporción de clases por fold |
| Leakage / drift | Contaminar con prueba / cambio silencioso en producción |
