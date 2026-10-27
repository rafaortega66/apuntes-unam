% materia: Reconocimiento de Patrones
% titulo: Clase 12 · Bayes (repaso), DBSCAN y KNN
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 5 oct 2026 (sesión 15 del curso) · Tema 8 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Inicio del segundo parcial: desde Bayes/Laplace todo entra. Diapositivas del profesor: Clase 11 (DBSCAN y KNN).

## 1. Repaso de clasificadores bayesianos
Clasificación supervisada por probabilidad a posteriori con la regla de Bayes. Cambia lo que se supone de la covarianza:
| Clasificador | Covarianza |
|---|---|
| **QDA** | Una Σₖ distinta por clase (solo con los ejemplos de esa clase) |
| **LDA** | Una Σ única compartida por todas las clases |
| **Naive Bayes** | Diagonal: independencia condicional; la posterior es un producto de P(xᵢ\|ωₖ) |
- Continuas: verosimilitud normal (media y varianza). Discretas: conteos de frecuencias (filtro de spam).
- Con el logaritmo de la gaussiana multivariada, la decisión depende de **P(ωₖ)**, **Σₖ** y la **distancia de Mahalanobis**.
!!! Probabilidad cero y suavizado de Laplace
Si llega una característica nunca vista (una palabra nueva), P(xᵢ\|spam) = 0 y **todo el producto se anula**. Solución: **suavizado de Laplace**: sumar una pequeña probabilidad uniforme al numerador y al denominador **de todas las clases**, para que la suma siga siendo 1. Error: sumarlo solo a una clase.

## 2. DBSCAN: clustering por densidad
Algoritmo **no supervisado** que agrupa regiones densas separadas por regiones de baja densidad; **detecta solo el número de clústers y el ruido**.
- **ε:** distancia máxima para ser vecinos. **min_pts (min_samples):** mínimo de puntos dentro de ε para una región densa.
| Tipo de punto | Definición |
|---|---|
| **Núcleo** | Tiene al menos min_pts dentro de su radio ε |
| **Frontera** | Está dentro del radio ε de un núcleo, pero no reúne min_pts en su vecindad |
| **Ruido** | Ni núcleo ni frontera |
**Algoritmo** (una sola pasada, a diferencia de K-Means):
1. Todos "no visitados"; K = 0.
2. Para cada P no visitado: marcarlo y calcular su vecindad (distancia ≤ ε).
3. Si tiene menos de min_pts → ruido (temporal).
4. Si tiene min_pts o más → núcleo: K += 1, asignarlo y **expandir**: sus vecinos a una cola; cada Q de la cola: si era ruido → frontera de K; si no estaba visitado → visitarlo, asignarlo a K y, si también es núcleo, agregar sus vecinos.
Un punto de ruido **sí puede volverse frontera** si cae en el radio de un núcleo procesado después.
!!! Elegir hiperparámetros
**min_pts:** entre características + 1 y 2 × características (con 2 características: 3 a 4). **ε:** distancia de cada punto a su K-ésimo vecino, ordenar y graficar la **K-distancia**; ε en el **codo**.
- Ventaja sobre K-Means/ISODATA (Clase 09): fronteras arbitrarias (anillos, dos lunas) y detección natural de outliers.
- Falla con **densidades variables** (un solo ε) y en muy alta dimensión.

## 3. KNN: K vecinos más cercanos
Supervisado, **no paramétrico**, basado en instancias y **perezoso**: no entrena, memoriza todo y calcula al llegar la consulta. Sirve para clasificación o regresión.
1. Guardar (Xᵢ, Yᵢ).
2. Calcular la distancia del punto nuevo a todos (euclidiana, Manhattan, Mahalanobis).
3. Ordenar de menor a mayor y tomar los K más cercanos.
4. **Votación por mayoría.** Empates (K = 4, 2 y 2): al azar o por costo del dominio.
| K | Efecto |
|---|---|
| Pequeño (1, 2, 3) | Sensible a ruido, fronteras irregulares, **sobreajuste**. "Nunca usen K = 1 en aplicaciones reales" |
| Grande (30, 50, 70) | Fronteras demasiado suaves, **subajuste**; llega a equivaler a lanzar una moneda |
| Óptimo | Graficar exactitud vs. K en validación; tomar donde se estabiliza el máximo (p. ej. 8–14) |
Usos: recomendación (Netflix), anomalías, **KNN Imputer** (rellena faltantes con la media de los K vecinos). Error común: no estandarizar antes de medir distancias.

## 4. Práctica 3
- **Parte 1 — color:** clases plátano, huevo, chile y fondo. Máscaras binarias de los tres objetos; la del **fondo es el complemento** (no se dibuja). DataFrame (R, G, B, clase); QDA **desde cero** con μₖ, Σₖ y P(ωₖ) por clase; clasificar píxel por píxel las imágenes de prueba.
- **Parte 2 — Breast Cancer Wisconsin:** `train_test_split`, estandarizar, QDA, LDA y Gaussian NB con Scikit-Learn; matriz de confusión, exactitud, precisión y recall; recomendar un modelo para diagnóstico y justificarlo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Bayes.** QDA: Σ por clase; LDA: Σ compartida; NB: diagonal (independencia). Laplace: sumar a numerador y denominador de todas las clases para evitar probabilidad cero.

!!! DBSCAN (examen)
Núcleo (≥ min_pts en ε), frontera (en el radio de un núcleo, sin min_pts), ruido (ninguno; puede pasar a frontera). min_pts entre d + 1 y 2d; ε en el codo de la K-distancia. Falla con densidades variables.

**KNN.** Perezoso y no paramétrico: distancias a todos, K más cercanos, mayoría. K chico = sobreajuste (nunca K = 1); K grande = subajuste; K por validación. Estandarizar.

| Práctica 3 | Clave |
|---|---|
| Fondo | Complemento de las máscaras |
| QDA | μₖ, Σₖ, P(ωₖ) por clase |
| Breast Cancer | QDA vs. LDA vs. GNB con matriz de confusión y recall |
