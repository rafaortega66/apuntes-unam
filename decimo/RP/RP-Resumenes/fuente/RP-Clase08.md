% materia: Reconocimiento de Patrones
% titulo: Clase 8 · Métricas de clustering y clasificación bayesiana
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 21 sep 2026 (sesión 11 del curso) · Temas 6 y 7 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Repaso de clustering
- **K-Means:** K fijo, asume clusters esféricos; falla con fronteras no lineales (medias lunas).
- **LBG:** cuantización vectorial; codebook de tamaño **potencia de 2** (cada iteración duplica los vectores con perturbación ±).
- **ISODATA:** K-Means + dividir dispersos, fusionar cercanos, eliminar pequeños.
**Métricas internas:** evalúan los grupos solo con la geometría, **sin etiquetas** (ground truth).

## 2. Índice de Dunn (más alto = mejor, 0 a +∞)
Dunn = mín d(Si, Sj) entre clusters ÷ máx Δ(Sk) (diámetro).
**Ejemplo:** S1 = {1, 2, 3}, S2 = {7, 8}, S3 = {15, 16, 17}.
| Paso | Valores |
|---|---|
| Separaciones | S1–S2 = 4; S1–S3 = 12; S2–S3 = 7 → mín = **4** |
| Diámetros | S1 = 2; S2 = 1; S3 = 2 → máx = **2** |
| Dunn | 4 / 2 = **2** |
!!! Corrección (19 oct, audio)
En el pizarrón se dictó 4/12 = 0.333; el 12 es una separación, no un diámetro. Correcto: **2**.

## 3. Índice de Davies-Bouldin (más bajo = mejor)
Rij = (Si + Sj) / d(mi, mj); Di = máx Rij; DB = promedio de los Di.
**Ejemplo:** S1 = 0.67, S2 = 0.5, S3 = 0.67; d(m1,m2) = 5.5, d(m1,m3) = 14, d(m2,m3) = 8.5.
| R | Cálculo |
|---|---|
| R12 | (0.67 + 0.5)/5.5 = 0.212 |
| R13 | 1.34/14 ≈ 0.096 |
| R23 | 1.17/8.5 ≈ 0.138 |
D1 = 0.213, D2 = 0.213, D3 = 0.138 → **DB ≈ 0.188**. (En clase se dictó D1 = 0.33; corregido con el audio; el resultado final sí era 0.188.)

## 4. Coeficiente de Silueta
s(i) = (b − a) / máx(a, b); a = distancia media a su cluster; b = distancia media al **cluster vecino más cercano**. La global es el promedio.
- X = 2 en S1: a = 1; b a S2 = (5 + 6)/2 = 5.5 → s = 4.5/5.5 = **0.818**.
- X = 7 en S2: a = 1; b = mín(5, 9) = 5 → s = 4/5 = **0.8**.
| Silueta | Estructura |
|---|---|
| < 0.25 | Sin estructura |
| 0.26–0.50 | Débil |
| 0.51–0.70 | Razonable |
| 0.71–1.00 | Excelente |

## 5. Funciones de similitud y repaso de probabilidad
Regla: asignar X a ωi si **gi(X) > gj(X)** para todo j ≠ i.
- PDF: P ≥ 0 y área total 1; CDF monótona no decreciente.
- Normal: definida por μ y σ. Momentos: E[(X − μ)^r].
- Covarianza: Σ = 1/(N−1) Σ (Xi − μ)(Xi − μ)ᵀ; diagonal = varianzas, fuera = covarianzas.
- Correlación = covarianza ÷ σiσj. **Correlación cero NO implica independencia.**

## 6. Decisión de Bayes y riesgo condicional
- Función de pérdida λ(αi | ωj): costo de asignar a i cuando es j. Acierto = 0; **simétrica 0/1**; **asimétrica** (médico: falso negativo de cáncer mucho peor que falso positivo).
- **Riesgo:** R(αi | X) = Σj λ(αi | ωj) · P(ωj | X).
!!! Ejercicio (viene en el examen)
P(ω1|X) = 0.7, P(ω2|X) = 0.3, pérdida 0/1.
R(α1) = 0·0.7 + 1·0.3 = **0.3**; R(α2) = 1·0.7 + 0·0.3 = **0.7** → se elige **α1** (menor riesgo).
- Con 0/1: R(αi|X) = 1 − P(ωi|X) → minimizar riesgo = **maximizar posterior**.
- **Bayes:** P(ωi|X) = P(X|ωi)·P(ωi) / P(X) (verosimilitud · prior / evidencia). P(X) es igual para todas las clases y se quita.
- Con logaritmo: gi(X) = ln P(X|ωi) + ln P(ωi).

## 7. Clasificadores gaussianos
gk(X) = −½ dM²(X, μk) − ½ ln|Σk| + ln P(ωk), con Mahalanobis dM² = (X − μk)ᵀ Σk⁻¹ (X − μk).
| Clasificador | Covarianza | Frontera |
|---|---|---|
| **QDA** | Una Σi distinta por clase | Cuadrática |
| **LDA** | Una Σ compartida | Lineal (hiperplanos) |
| **Naive Bayes gaussiano** | Diagonal (independencia) | — |
Error común: creer que LDA da fronteras cuadráticas.

## 8. Naive Bayes y suavizado de Laplace
P(X|ωi) = Π P(Xj|ωi) (independencia condicional dada la clase; "ingenuo" porque casi nunca se cumple, pero funciona).
- Continuo: una normal por característica; 6 características × 4 clases = 24 medias y 24 σ. Prior = Ni / Ntotal.
**Filtro de spam (8 correos: 3 spam, 5 no):** P(Spam) = 0.375, P(No) = 0.625.
| Palabra | Spam | No spam |
|---|---|---|
| oferta | 1/10 | 0/21 |
| gratis | 2/10 | 0/21 |
| hoy | 1/10 | 2/21 |
| es | 1/10 | 2/21 |
| secreto | 3/10 | 1/21 |
"hoy es secreto": Spam = (1/10)(1/10)(3/10)(3/8) = **0.001125**; No spam = (2/21)(2/21)(1/21)(5/8) ≈ **0.00027** → **SPAM** (corregido con el audio; en clase se mencionó 0.001).
- **Frecuencia cero:** una palabra no vista anula el producto. **Laplace:** sumar una constante (p. ej. 1/V, V = vocabulario, 1/12) a los conteos, cuidando que las probabilidades sigan sumando 1.

## 9. Código y evaluación en Iris
- Se trabaja en logaritmos para evitar **underflow**.
- Iris (120 entrenamiento, 30 prueba, 4 características, 3 clases): Naive Bayes **1 error** (Versicolor → Virginica); QDA **100 %**.
| Ventajas de Naive Bayes | Desventajas |
|---|---|
| Pocos parámetros y pocas muestras | Sensible a correlación |
| Alta dimensionalidad | No capta interacciones |
| Actualización en línea | Sensible a variables irrelevantes y a frecuencias cero |

## Pendiente
Práctica 2 «Algoritmos de clustering» (Classroom): K-Means (K = 4, semillas, K-Means++), ISODATA, métricas de hoy y matriz contra clases reales; entrega viernes 25 sep, 7:00. Primer parcial: lunes 28 sep (calculadora física, sin celular).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Métrica | Fórmula | Mejor |
|---|---|---|
| Dunn | mín separación / máx diámetro | Alto |
| Davies-Bouldin | promedio de máx (Si + Sj)/d(mi, mj) | Bajo |
| Silueta | (b − a)/máx(a, b) | Cerca de 1 |

!!! Riesgo condicional
R(αi|X) = Σ λ(αi|ωj)·P(ωj|X); se elige el menor. Con 0/1 equivale a escoger la posterior más alta. Ejemplo: 0.3 vs 0.7 → α1.

| Modelo | Covarianza | Frontera |
|---|---|---|
| QDA | Una por clase | Cuadrática |
| LDA | Compartida | Lineal |
| Naive Bayes | Diagonal | Independencia |

**Naive Bayes:** producto de probabilidades por característica × prior; Laplace evita ceros; logaritmos evitan underflow.
