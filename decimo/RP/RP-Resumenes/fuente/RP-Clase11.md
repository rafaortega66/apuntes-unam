% materia: Reconocimiento de Patrones
% titulo: Clase 11 · Revisión del primer examen parcial
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 2 oct 2026 (sesión 14 del curso) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Sin teoría nueva: solución pregunta por pregunta del primer parcial (Clase 10). Sirve como banco de ejercicios resueltos. Cifras de LDA corregidas con el examen escaneado.

## 1. Estructura del examen
| Bloque | Preguntas | Puntos |
|---|---|---|
| Teoría (65 %) | 32: la 1 vale 3; de la 2 a la 32, 2 cada una | 65 |
| Práctica (35 %) | 33 Hu (10) · 34 GLCM (10) · 35 LDA (15) | 35 |
Medios puntos en respuestas parciales. El 100 % de la teoría salió de diapositivas y discusiones de clase; dos ejercicios eran idénticos a tareas y uno, adaptación de un ejemplo del pizarrón.

## 2. Fundamentos (preguntas 1–6)
- **Patrón:** cualquier objeto, proceso o evento que puede describirse y distinguirse de otros.
- **Supervisado:** se conoce la clase de cada patrón (perro/gato/caballo). **No supervisado:** se desconoce la clase **y el número de clases** (agrupar pacientes sin etiquetas).
- **Etapas:** sensing → extracción de características → clasificación → evaluación del desempeño.
- **Espacio de características:** cada punto es un patrón (x₁ … xₙ). **Espacio de pesos:** cada punto es un clasificador (w₀ … wₙ), que fija la orientación y posición del hiperplano.
- **Maldición de la dimensionalidad:** dispersión de datos, mayor costo, sobreajuste, distancias sin sentido, degradación del rendimiento y retos de visualización.

## 3. Características, MFCC, PCA y LDA (7, 8, 12–16)
- **Extracción** (mediciones crudas → vector compacto) ≠ **selección** (subconjunto de lo ya extraído).
- Buen conjunto: discriminable, compacto, robusto y de bajo costo.
- **MFCC en orden:** preénfasis → framing → ventaneo (Hamming) → FFT → banco Mel → logaritmo → DCT.
| Selección | Idea | Ejemplo |
|---|---|---|
| Filtrado | Antes e independiente del modelo | Correlación de Pearson |
| Wrapper | Con el desempeño de un clasificador | Forward Selection (puede llegar al óptimo con búsqueda exhaustiva) |
| Embebido | Dentro del entrenamiento | L1 / Lasso |
- **PCA:** no supervisado, máxima varianza. **LDA:** supervisado, maximiza varianza entre clases / dentro de clases. PCA no separa clases.

## 4. Evaluación (17–21)
- FP: positivo cuando era negativo; FN: negativo cuando era positivo. **ROC:** eje Y = TPR (sensibilidad), eje X = FPR.
- **Hold-Out:** entrenamiento, validación y prueba (no necesariamente iguales). **K-Fold:** K particiones, K entrenamientos; **el test se reserva para la evaluación final** (no se evalúa en cada iteración).
- **Data Drift:** la distribución en producción cambia respecto al entrenamiento.

## 5. Discriminantes, distancia, clustering y Bayes (22–32)
- x ∈ ωᵢ si gᵢ(x) > gⱼ(x) ∀ j ≠ i; lineal en dos clases = hiperplano; gᵢ = gⱼ → sobre la frontera.
- K-Means/distancia mínima: prototipo media, espacio esférico. **Mahalanobis** incorpora la covarianza. **LBG:** cuantización vectorial, minimiza la distorsión promedio. **ISODATA** ajusta K (dividir, fusionar, eliminar); K-Means lo fija.
- **Bayes:** P(ωᵢ\|x) = P(x\|ωᵢ)P(ωᵢ)/P(x) (posterior, verosimilitud, a priori, evidencia). **QDA:** Σ por clase, fronteras cuadráticas; LDA comparte Σ; Naive Bayes, diagonal.

## 6. Ejercicio 33: momentos de Hu
Píxeles (x, y): (3,3), (3,1), (3,2), (1,3), (2,3).
| Paso | Cálculo |
|---|---|
| m₀₀, m₁₀, m₀₁ | 5; 12; 12 → centroide (2.4, 2.4) |
| m₁₁ y μ₁₁ | m₁₁ = 27; μ₁₁ = 27 − 2.4·12 = **−1.8** |
| μ₂₀ = μ₀₂ | 1.96 + 0.16 + 1.08 = **3.2** |
| η (γ = 2, ÷ 5² = 25) | η₁₁ = −0.072; η₂₀ = η₀₂ = 0.128 |
| HU₂ = (η₂₀ − η₀₂)² + 4η₁₁² | 0 + 4(0.005184) = **0.020736** → −log₁₀ ≈ **1.6832** |

## 7. Ejercicio 34: GLCM
Transiciones norte-sur a distancia 1, niveles 0–3.
1. Contar transiciones verticales.
2. **Simetría:** sumar la transpuesta; total = **40**.
3. **Normalizar:** dividir entre 40 → P(i, j).
4. **ASM** = ΣP² = **0.1075**; **energía** = √ASM = **0.3278**; **contraste** = ΣP(i − j)² = **1.1**.
Errores típicos: no normalizar o no sumar la transpuesta.

## 8. Ejercicio 35: LDA completo
Clase 1: (4,1), (2,4), (2,3), (3,6), (4,4) → μ₁ = (3, 3.6). Clase 2: (9,10), (6,8), (9,5), (8,7), (10,8) → μ₂ = (8.4, 7.6). μ = (5.7, 5.6).
| Paso | Resultado |
|---|---|
| S_B = Σ Nₖ(μₖ − μ)(μₖ − μ)ᵀ | [[72.9, 54], [54, 40]] |
| S₁; S₂ | [[4, −2], [−2, 13.2]]; [[9.2, −0.2], [−0.2, 13.2]] |
| S_W = S₁ + S₂ | [[13.2, −2.2], [−2.2, 26.4]] |
| det(S_W) | 348.48 − 4.84 = 343.64 |
| S_W⁻¹ | ≈ [[0.07682, 0.00640], [0.00640, 0.03841]] |
| A = S_W⁻¹S_B | ≈ [[5.9462, 4.4046], [2.5410, 1.8822]] |
| det(A − λI) = 0 | λ² − 7.8284λ + 0 = 0 → λ = 0 y **λ₁ ≈ 7.83** |
| Eigenvector | −1.8822w₁ + 4.4046w₂ = 0 → **w ≈ (2.34, 1)** (normalizado ≈ (0.920, 0.393)) |
Con dos clases A tiene rango 1: una raíz siempre es 0 (buena verificación).

# PARTE 2 · Resumen para estudiar
~ Patrón del examen: teoría de las diapositivas + ejercicios iguales a tareas o ejemplos del pizarrón.

!!! Cadenas de cálculo (examen)
**Hu:** centroide → m₁₁ → μ₁₁ → η (÷ m₀₀^γ, γ = 2) → HU₂ → −log₁₀. **GLCM:** contar → + transpuesta → ÷ total → ASM, energía = √ASM, contraste. **LDA:** medias → S_B → S_W → S_W⁻¹ → A → λ → w.

| Teoría | Para recordar |
|---|---|
| No supervisado | No se conocen clases ni cuántas son |
| MFCC | Preénfasis, framing, Hamming, FFT, Mel, log, DCT |
| Selección | Filtrado (Pearson), wrapper (Forward), embebido (L1) |
| PCA vs. LDA | Varianza sin etiquetas vs. separación con etiquetas |
| ROC | Y = TPR, X = FPR |
| K-Fold | Test solo al final |
| ISODATA vs. K-Means | K dinámico vs. K fijo |
| QDA / LDA / NB | Σ por clase / compartida / diagonal |
