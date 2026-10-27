% materia: Reconocimiento de Patrones
% titulo: Clase 9 · Práctica 2: K-Means, K-Means++ e ISODATA
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 25 sep 2026 (sesión 12 del curso) · Tema 6 (cierre) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Sesión de exposiciones con números reales de las corridas. La teoría viene de las Clases 07 y 08. Antesala del primer parcial: "los ejercicios a mano serán sencillos, midiendo diferencias al cuadrado".

## 1. Repaso: distancia mínima y métricas
- **Regla de distancia mínima:** x se asigna a ωₖ si d(x, mₖ) < d(x, mⱼ) ∀ j ≠ k. Con varios prototipos por clase: Dᵢ = min_λ ‖x − z_iλ‖.
| Métrica | Expresión | Nota |
|---|---|---|
| Euclidiana | √Σ(xᵢ − yᵢ)² | Norma L2 |
| Manhattan | Σ\|xᵢ − yᵢ\| | Norma L1 |
| Mahalanobis | (x − y)ᵀ Σ⁻¹ (x − y) | Incorpora la covarianza |
| Minkowski | (Σ\|xᵢ − yᵢ\|ᵖ)^(1/p) | p = 1 Manhattan, 2 Euclidiana, ∞ Chebyshev |
| Coseno | x·y / (‖x‖‖y‖) ∈ [−1, 1] | Orientación, no magnitud |
| Pearson | r ∈ [−1, 1] | Relaciones lineales |
| Jaccard | \|A ∩ B\| / \|A ∪ B\| | Conjuntos binarios o categóricos |
Clustering: sin etiquetas; maximizar cohesión intra-clúster y separación inter-clúster.

## 2. K-Means, K-Means++ y LBG
**K-Means** minimiza la **inercia J = Σⱼ Σ_{xᵢ∈Cⱼ} ‖xᵢ − μⱼ‖²**:
1. Definir K. 2. Inicializar centroides. 3. Asignar: argminⱼ ‖xᵢ − μⱼ‖. 4. Actualizar: μⱼ = promedio de sus puntos. 5. Converger (desplazamiento < ε, sin cambios o máx. iteraciones).
Complejidad O(n·k·i·d). Limitaciones: clústeres esféricos, sensible a la escala, **mínimos locales** por mala inicialización.
!!! K-Means++
El primer centroide al azar; los siguientes con probabilidad **p(x) = D(x)² / Σ D(x)²** (proporcional al cuadrado de la distancia al centroide más cercano): quedan lejos entre sí y se evitan mínimos locales.
**LBG (Linde-Buzo-Gray):** diseña un **codebook** para cuantización vectorial minimizando D = (1/N) Σ‖xᵢ − c(xᵢ)‖². Enfoque **divisivo**: media global → dividir cada centroide c(1 ± ε) (K → 2K) → Lloyd hasta que la mejora relativa < δ → repetir hasta N = 2^L. Clasificar: codeword más cercano de cada clase.

## 3. ISODATA y métricas
K-Means con **K variable** por división, fusión y eliminación.
| Parámetro | Función |
|---|---|
| K_init / K_max | Clústeres iniciales / máximo |
| N_min | Mínimo de puntos por clúster (eliminar) |
| σ_max | Desviación máxima por dimensión (dividir) |
| d_min | Distancia mínima entre centroides (fusionar) |
| θ_c | Máximo de fusiones por iteración |
- **Eliminar** si \|Cₖ\| < N_min. **Dividir** si σₖ > σ_max y K < K_max: mₖ ± δ en el eje de mayor varianza (δ = 0.5·σₖ). **Fusionar** si dᵢⱼ < d_min: m = (\|Cᵢ\|mᵢ + \|Cⱼ\|mⱼ)/(\|Cᵢ\| + \|Cⱼ\|).
- Sigue suponiendo clústeres esféricos (falla con dos lunas).
| Métrica | Lectura |
|---|---|
| **Silueta** s(i) = (b − a)/máx(a, b) | ≈ 1 óptimo; ≈ 0 frontera; < 0 mal asignado |
| **Davies-Bouldin** | Menor = mejor |
| **ARI** (Rand ajustado) | Concordancia con etiquetas reales; 1 perfecto |

## 4. Experimento 1: datos sintéticos (400 puntos, K = 4)
| Inicialización | Iteraciones | Inercia |
|---|---|---|
| Aleatoria (semillas 11, 22, 33) | 8, 8, 6 | 2086.79 / 2068.85 / 2086.79 |
| K-Means++ (44, 55, variable) | 4, 4, 5 | 2086.79 |
- K-Means++ bajó el promedio de **7.3 a 4.3 iteraciones**. Con una semilla mala (20) el aleatorio quedó en un mínimo local con inercia **3550** (76 % peor).
- **ISODATA:** con K_init = 6 fusionó 6 → 5 → 4; con K_init = 3 dividió 3 → 4. Ambos llegaron a 2086.79.
!!! La inercia sube al fusionar (no es error)
Con K_init = 6 la inercia empezó en 1902.79 y subió a 2086.79 al quedar 4 clústeres: con menos centroides la suma de distancias al cuadrado necesariamente aumenta.

## 5. Experimento 2: dataset Wine
178 muestras, 13 características químicas, 3 clases.
- **Estandarizar (Z-score):** Proline va de 70 a 1620 y Hue ≈ 0.69; sin escalar, Proline domina la distancia.
- **PCA al 95 % de varianza:** 13 → **10 componentes**.
- K-Means (K = 3): 10 iteraciones, inercia **127.98**. ISODATA (K_init = 5, N_min = 8, σ_max = 1.2, d_min = 3, θ_c = 2): 5 → 4 → 3 clústeres, misma inercia 127.98.
| Clúster | Contenido |
|---|---|
| 1 → clase 3 | 48 de la clase 3 + 3 de la clase 2 |
| 2 → clase 2 | 65 puros de la clase 2 |
| 3 → clase 1 | 59 de la clase 1 + 3 de la clase 2 |
Silueta **0.2849**, Davies-Bouldin **1.3892**, ARI **0.895** (casi perfecta concordancia).

## 6. Preguntas del profesor
1. **¿Ventaja de K-Means++ si llega a la misma inercia?** Menos iteraciones y, sobre todo, **evita mínimos locales** por centroides iniciales juntos o un centroide entre dos clases.
2. **¿Cómo unir/separar centroides?** K-Means no puede (K rígido). En ISODATA: **σ_max** controla dividir y **d_min** fusionar.
3. **¿Con solo 2 componentes (57 %)?** Más rápido y graficable, pero perder el 43 % de información sube el error.
4. **¿Estandarizar o normalizar en Wine?** Estandarizar (Z-score): conserva la distribución sin comprimir a un intervalo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Métricas de distancia.** Euclidiana (L2), Manhattan (L1), Mahalanobis (covarianza), Minkowski (generaliza), coseno (ángulo).

!!! K-Means vs. K-Means++ vs. ISODATA (examen)
K-Means minimiza la inercia con K fijo y cae en mínimos locales. K-Means++ elige centroides con p ∝ D(x)²: menos iteraciones (7.3 → 4.3) y sin mínimos locales. ISODATA ajusta K: σ_max divide, d_min fusiona, N_min elimina; la inercia sube al fusionar sin ser error.

| Concepto | Para recordar |
|---|---|
| Estandarizar | Imprescindible con escalas distintas (Proline) |
| PCA | Conservar ≈ 95 % de varianza |
| Silueta / DBI / ARI | ≈ 1 bueno / menor mejor / 1 perfecto |
| LBG | Divisivo: c(1 ± ε), K → 2K, codebook |
