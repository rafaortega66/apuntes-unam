% materia: Reconocimiento de Patrones
% titulo: Clase 7 · Clasificación por distancia y clustering: K-Means, LBG e ISODATA
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 18 sep 2026 (sesión 10 del curso) · Tema 6 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Clasificación no supervisada y distancia mínima
- **No supervisado:** sin etiquetas; se busca cómo se agrupan los datos de forma natural. **Patrón** = vector de características; **clase** = conjunto de patrones similares.
- Intuición: menor distancia = mayor similitud.
| Distancia | Qué mide |
|---|---|
| Euclidiana | Línea recta |
| Manhattan | Suma de diferencias absolutas |
| Mahalanobis | Punto contra una **distribución** (usa la covarianza de la clase) |
- **Un prototipo por clase** (centroides M1, M2, M3) o **varios prototipos** (cada punto es un ejemplo real; gana la clase con la distancia individual mínima).
!!! Regla de distancia mínima
X ∈ Wk si **d(X, Mk) < d(X, Mj)** para todo j ≠ k. Simple, barata y buena con clases separadas. Limitaciones: **sensible a la escala** (hay que normalizar) y no considera la forma de las clases (salvo Mahalanobis).

## 2. Clustering
Grupos donde los elementos se parecen más entre sí que a los de otros grupos; sin etiquetas y a veces sin saber cuántos grupos hay.
- **Cohesión intracluster** y **separación intercluster**.
- Aplicaciones: compresión (cuantización vectorial), segmentación, clasificación de documentos, fraudes bancarios.
| Similitud | Uso |
|---|---|
| Coseno | Ángulo, sin importar magnitud |
| Pearson | Relación lineal; selección de características |
| Jaccard | Conjuntos binarios, categóricos, texto |
| Minkowski | (Σ|xi − yi|^P)^(1/P): P = 1 Manhattan, P = 2 Euclidiana, P → ∞ Chebyshev |

## 3. K-Means
Divide en K grupos minimizando la **inercia** (suma de distancias cuadradas al centro).
1. Definir K (único parámetro obligatorio).
2. Inicializar K centroides: aleatoria o **K-Means++** (primero al azar; los siguientes con probabilidad ponderada por la distancia: más lejos = más probable).
3. Asignar cada punto al centroide más cercano.
4. Actualizar cada centroide como la media; cluster vacío → se reinicializa con un punto aleatorio.
5. Parar si no cambian las asignaciones, si el cambio de inercia < ε o al máximo de iteraciones.
- Los centroides empiezan en puntos del dataset, pero al promediar ya no coinciden con datos reales.
- Complejidad **O(N·K·I·D)**. Sensible a inicialización (mínimos locales), outliers y escala; solo fronteras **esféricas**.

## 4. LBG (Linde-Buzo-Gray)
Diseña un **codebook** (codewords prototipo) para cuantización vectorial; p. ej. resumir 5,000 pacientes con cáncer y 10,000 sin cáncer en pocos codewords. Minimiza la **distorsión** D = (1/N) Σ ‖Xi − C‖².
1. Codeword inicial = **media global** (más estable que K-Means).
2. Splitting: C⁺ = C(1 + ε), C⁻ = C(1 − ε), ε ≈ 0.1.
3. Asignar y actualizar como en K-Means.
4. Parar la etapa si |Dant − Dact| / Dant < tolerancia (la fija el usuario).
5. Repetir hasta el tamaño deseado: siempre **potencia de 2** (1 → 2 → 4 → 8…).
- Genera **regiones de Voronoi**. Para clasificar: un codebook **por clase**; X va a la clase con el codeword más cercano.
- Codebook chico = subajuste; grande = sobreajuste.

## 5. ISODATA
Evolución **heurística** de K-Means (sin garantía de mínimo global) que ajusta K:
| Operación | Cuándo |
|---|---|
| División | σ de la dimensión máxima > σmax y K < límite: Mk ± 0.5·σ·ej |
| Fusión | Distancia entre centroides < Dmin: Mnuevo = (Ni·Mi + Nj·Mj)/(Ni + Nj), en orden creciente de distancia, hasta Lmax |
| Eliminación | Menos de Nmin puntos; se reasignan |
Parámetros: K0, Nmin, σmax, Dmin, Lmax, Imax y límites de K.
- **Medias lunas:** ni K-Means ni ISODATA separan fronteras no lineales; ISODATA partió las dos lunas en **7** clusters circulares.
- ¿Por qué ISODATA? El buen resultado de K-Means requirió varias corridas con inicializaciones a mano; ISODATA lo logró solo con inicialización aleatoria.

## 6. Comparativo
| Criterio | K-Means | LBG | ISODATA |
|---|---|---|---|
| K | Fijo desde el inicio | Tamaño del codebook | Dinámico |
| Resultado | K esféricos | Potencias de 2 | Variable |
| Inicialización | Muy sensible | Baja (media global) | Moderada/baja |
| Fronteras | Esféricas | Voronoi | Esféricas |
| Parada | Centroides, inercia, iteraciones | Tolerancia de distorsión | Convergencia o iteraciones |
Aplicaciones: teledetección, imágenes médicas, paletas de color, minería de datos, visión.

## Examen y pendiente
- Ejercicios sencillos: distancia Euclidiana de puntos como (1,2) y (2,−5) a centroides (0,1) y (1,1), asignar y calcular la nueva media de una iteración.
- Práctica 2 «Algoritmos de clustering»: viernes 25 sep, 7:00.
- Primer parcial: lunes 28 sep, sesión completa 7:00–8:30 (corregido en la Clase 9); Prácticas 1 y 2; calculadora física; fórmulas en el pizarrón.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Ejercicio tipo examen
Distancia Euclidiana de cada punto a cada centroide (diferencias al cuadrado) → asignar al más cercano → nueva media por cluster. Normalizar si las escalas difieren.

| Algoritmo | Idea | Para recordar |
|---|---|---|
| K-Means | Asignar y promediar | K fijo; inercia; K-Means++; O(N·K·I·D) |
| LBG | Splitting desde la media global | Distorsión; potencias de 2; codebook por clase |
| ISODATA | K-Means + heurísticas | Divide (σmax), fusiona (Dmin), elimina (Nmin) |

**Minkowski:** P = 1 Manhattan, P = 2 Euclidiana, P → ∞ Chebyshev. Ninguno de los tres separa las medias lunas.
