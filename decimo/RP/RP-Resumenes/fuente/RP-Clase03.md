% materia: Reconocimiento de Patrones
% titulo: Clase 3 · Reconstrucción con PCA, Eigenfaces y LDA
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 4 sep 2026 (sesión 6 del curso) · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Fuente
El audio de esta sesión es **parcial** (solo el tramo final, sobre la práctica). LDA, t-SNE, Kernel PCA y QDA vienen del deck del profesor «Clase 6 — Reducción de dimensionalidad II» y **no** se confirmaron en el audio.

## 1. Reconstrucción con PCA
| Paso | Expresión |
|---|---|
| Datos | X ∈ ℝ^(m×n) |
| Centrar | Xc = X − μ |
| Autovectores | Wk ∈ ℝ^(n×k) |
| Proyectar | Z = Xc·Wk (m×k) |
| Reconstruir | X̂ = Z·Wkᵀ + μ |
- Error ‖X − X̂‖²: mínimo con los k componentes de mayor varianza → **mejor aproximación de rango k**.
- Wine (13 características): el MSE baja de un valor alto con 1 componente hasta **0 con las 13**.

## 2. Eigenfaces
- Matriz **N×P** (N imágenes, P píxeles), centrar y aplicar PCA por SVD.
- **Rostro promedio:** liso, sin facciones de nadie (lo comentó Roberto; es lo esperado).
- **Primeras ~10:** rasgos estructurales (ojos, boca, contorno). **Últimas ~10:** como estática de TV.
- Validación: reconstruir con 10, 20, 50, 100… 300 eigenfaces en una figura; el MSE baja porque se recupera más varianza.

## 3. Elegir K
| Criterio | Regla |
|---|---|
| Codo | Cambio abrupto de pendiente en la varianza acumulada |
| Kaiser | Autovalor **λ > 1** |
| Umbral | 90–95 % de varianza total |

## 4. LDA (deck)
Supervisado: clases separadas y compactas. Supuestos: gaussiana por clase, misma covarianza, separabilidad lineal.
- Entre clases: **S_B** = Σ ni (μi − μ)(μi − μ)ᵀ. Dentro: **S_W** = Σ Σ (x − μi)(x − μi)ᵀ.
- **Rayleigh:** J(w) = (wᵀS_B w)/(wᵀS_W w), se maximiza.
- Resolver S_W⁻¹S_B w = λw; da **K − 1** discriminantes (máx. min(K − 1, d)); Z = X·W.
- S_W singular: PCA antes, regularizar (1 − α)S_W + αI, o pseudoinversa por SVD.
- Ventajas: supervisada, interpretable, también clasifica. Desventajas: gaussianidad, covarianza compartida, lineal.

## 5. Otros métodos (deck)
- **t-SNE:** no lineal para visualizar 2D/3D; gaussiana en el original, t de Student en el reducido; minimiza la divergencia KL.
- **Kernel PCA:** truco del kernel con K(xi, xj) sin mapeo explícito.
- **QDA:** covarianza propia por clase, fronteras cuadráticas.

## 6. Lo que recalcó en el audio
- **Sin estandarizar** (Wine), la variable de mayor escala (Proline) se lleva casi toda la varianza en PC1; estandarizando, la curva sube gradual.
- **Estandarizar** = restar la media y dividir entre σ.
- Covarianza, SVD y scikit-learn: mismos autovalores; autovectores pueden cambiar de **signo** sin afectar la ortogonalidad.
- SVD y covarianza ya vienen en `numpy.linalg`.

## Pendiente: Práctica 1
Código, reporte en **formato IEEE a dos columnas** (las respuestas van en el reporte **y** se exponen) y presentación oral el viernes de la siguiente semana, con una computadora por equipo (equipos de 3 y de 2).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Reconstrucción | X̂ = Z·Wkᵀ + μ; MSE baja hasta 0 con todas |
| Eigenfaces | Primeras = estructura; últimas = ruido; promedio liso |
| K | Codo, Kaiser (λ > 1), 90–95 % |
| Sin estandarizar | PC1 absorbe casi todo |
| Signos | Pueden invertirse; misma dirección |
| LDA | Maximiza J(w) = S_B/S_W; K − 1 ejes |
