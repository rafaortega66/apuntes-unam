% materia: Reconocimiento de Patrones
% titulo: Clase 15 · Máquinas de vectores de soporte (SVM)
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 16 oct 2026 (sesión 18 del curso) · Tema 8 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
!!! Fuente
No asistí a esta clase y no hay audio. Todo sale de las diapositivas oficiales «Clase 13 SVM» del profesor (Classroom, 18 oct). Entra al segundo parcial.

## 1. Qué es SVM
SVM (Support Vector Machine) es un método **supervisado** de clasificación y regresión cuyo objetivo es encontrar el **hiperplano que mejor separa las clases maximizando el margen**.
Un clasificador lineal se define por pesos w y bias b: si w·x + b > 0 → +1; si < 0 → −1. Hay infinitas rectas que separan los mismos datos; SVM elige la de margen máximo.
| Concepto | Definición |
|---|---|
| **Hiperplano** | Plano de decisión que separa objetos de distintas clases |
| **Margen** | Distancia entre el hiperplano y los vectores de soporte; idealmente sin puntos dentro |
| **Vectores de soporte** | Los puntos más cercanos al hiperplano; solo ellos definen la frontera |

## 2. Maximizar el margen
Plano positivo w·x + b ≥ +1 y negativo w·x + b ≤ −1; con y = ±1 se resumen en **yᵢ(w·xᵢ + b) ≥ 1**.
**Derivación del ancho** (x⁺ = x⁻ + λw):
1. w·x⁺ + b = +1 y w·x⁻ + b = −1.
2. w·(x⁻ + λw) + b = 1 → −1 + λ w·w = 1 → **λ = 2/(w·w)**.
3. M = |λw| = λ‖w‖ = 2‖w‖/(w·w) = **2/‖w‖**.
!!! Problema de optimización
Maximizar M = 2/‖w‖ equivale a **min ½‖w‖²** sujeto a yᵢ(w·xᵢ + b) ≥ 1. Hacer w pequeño es ensanchar la "carretera".

**Lagrangiano:** ℒ(w, b, α) = ½‖w‖² − Σ αᵢ[yᵢ(wᵀxᵢ + b) − 1].
- ∂ℒ/∂w = 0 → **w = Σ αᵢ yᵢ xᵢ**; ∂ℒ/∂b = 0 → **Σ αᵢ yᵢ = 0**.
- **Forma dual:** max_α Σ αᵢ − ½ ΣᵢΣⱼ αᵢαⱼ yᵢyⱼ xᵢᵀxⱼ, con αᵢ ≥ 0 y Σ αᵢ yᵢ = 0.
- Los vectores de soporte son los puntos con **αᵢ > 0**. En la dual solo aparecen productos punto xᵢᵀxⱼ: eso permite el truco del kernel. Esta versión solo funciona con datos linealmente separables.

## 3. Margen suave: holgura y C
Con solapamiento entre clases se agrega una holgura ξᵢ por ejemplo:
**yᵢ(wᵀxᵢ + b) ≥ 1 − ξᵢ** y **min ½‖w‖² + C Σ ξᵢ**.
| C | Efecto |
|---|---|
| Grande | Pocos errores permitidos → margen angosto (riesgo de sobreajuste con ruido) |
| Pequeño | Más errores tolerados → margen ancho |

## 4. Truco del kernel
Datos no separables linealmente (círculo dentro de un anillo, medias lunas, rojos a ambos lados de azules en una recta): se llevan a una **dimensión mayor** donde sí se separan (en 1D, añadir x² convierte la recta en parábola).
!!! Kernel
K(xᵢ, xⱼ) = φ(xᵢ)ᵀφ(xⱼ): calcula el producto punto en el espacio grande **sin calcular φ explícitamente**. Dual: max Σ αᵢ − ½ ΣΣ αᵢαⱼ yᵢyⱼ K(xᵢ, xⱼ).
| Kernel | Fórmula |
|---|---|
| Lineal | K = xᵢᵀxⱼ |
| Polinomial | K = (1 + xᵢᵀxⱼ)ᵖ |
| RBF (base radial) | K = exp(−‖xᵢ − xⱼ‖² / 2σ²) |
| Sigmoide | K = tanh(α xᵢᵀxⱼ + c) |
**Multiclase:** SVM es binario; se usa uno vs. el resto o uno vs. uno. Misma idea que Kernel PCA (Clase 03) y funciones de decisión multiclase (Clase 06).

## 5. Ejemplos del deck
**Breast Cancer:**
| Kernel | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| **Lineal** | **0.982** | 0.982 | 0.982 | 0.982 |
| Polinomial (grado 3) | 0.895 | 0.910 | 0.895 | 0.890 |
| RBF (gamma = scale) | 0.977 | 0.977 | 0.977 | 0.977 |
| Sigmoide | 0.936 | 0.936 | 0.936 | 0.936 |
Un kernel más complejo no siempre ayuda: aquí gana el lineal.

**German Credit (riesgo):**
| Kernel | Accuracy | Recall | F1 | Riesgos no detectados |
|---|---|---|---|---|
| linear | 74.0 % | 84.6 % | 0.820 | 27 |
| rbf | 70.4 % | **100 %** | **0.825** | 0 |
| poly | 70.0 % | 80.6 % | 0.790 | 34 |
| sigmoid | 66.8 % | 74.3 % | 0.758 | 45 |
!!! Leer la matriz de confusión
El RBF tiene recall 100 % y el F1 más alto, pero porque clasifica casi todo como "riesgo" (solo 1 "bueno" acertado de 75: matriz [1, 74; 0, 175]). Es un modelo casi trivial: no basta una métrica.

## 6. Ventajas y desventajas
| Ventajas | Desventajas |
|---|---|
| Muy efectivo en alta dimensionalidad | Lento con datasets muy grandes |
| Funciona bien con pocos datos | Sensible a la elección del kernel e hiperparámetros |
| Robusto a outliers: solo dependen los vectores de soporte | El escalamiento de los datos es crucial |
| Modela no linealidad y multiclase | Difícil de interpretar con kernels no lineales |

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Idea.** Hiperplano de margen máximo; solo los vectores de soporte (αᵢ > 0) lo definen. Restricción yᵢ(w·xᵢ + b) ≥ 1.

!!! Derivación (examen)
λ = 2/(w·w) → M = 2/‖w‖ → maximizar M ≡ min ½‖w‖². Lagrange: w = Σ αᵢyᵢxᵢ y Σ αᵢyᵢ = 0; la dual solo usa productos punto.

| Concepto | Para recordar |
|---|---|
| Margen suave | ξᵢ; min ½‖w‖² + CΣξᵢ; C grande = margen angosto, C chico = ancho |
| Kernel | K = φ(xᵢ)ᵀφ(xⱼ) sin calcular φ |
| Kernels | Lineal, polinomial (1 + xᵀx)ᵖ, RBF exp(−‖·‖²/2σ²), sigmoide tanh |
| Multiclase | Uno vs. resto o uno vs. uno |
| Ejemplos | Breast Cancer: gana lineal (0.982). German Credit: RBF engaña (todo "riesgo") |
| Desventajas | Lento con muchos datos, sensible al kernel, requiere escalar |
