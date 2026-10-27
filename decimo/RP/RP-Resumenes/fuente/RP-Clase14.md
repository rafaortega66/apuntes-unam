% materia: Reconocimiento de Patrones
% titulo: Clase 14 · Regresión logística
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 12 oct 2026 (sesión 17 del curso) · Tema 8 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Diapositivas del profesor: Clase 12 (Regresión Logística). Entra al segundo parcial.

## 1. Repaso: DBSCAN y KNN
- **DBSCAN:** agrupa por densidad, detecta ruido, no fija K, aprende fronteras no esféricas; falla con densidades variables.
- **KNN:** supervisado, no paramétrico y **"perezoso"**: no entrena una ecuación, **memoriza** el dataset; predecir es lento (distancia a cada punto guardado). Transición hacia un modelo paramétrico que sí se optimiza.

## 2. Por qué la regresión lineal no sirve para clasificar
- Regresión = salida continua (precio de una casa: f_θ(x) = θ₀ + θ₁x), ajustada minimizando E(θ) = 1/(2n) Σ(f_θ(xᵢ) − yᵢ)².
- Ajustar una recta a etiquetas 0/1 y cortar en 0.5 falla: **un ejemplo de clase 1 muy alejado inclina la recta y corre el umbral**, y además la recta da valores fuera de [0, 1] (no son probabilidades).

## 3. Sigmoide, odds y x₀ = 1
!!! Modelo
**g(z) = 1 / (1 + e⁻ᶻ)**; **h_θ(x) = g(θᵀx) = P(y = 1 | x)**; P(y = 0 | x) = 1 − h_θ(x).
- **Odds:** P(y=1)/P(y=0) = e^(θᵀx). **Log-odds (logit):** ln(odds) = θᵀx = θ₀ + θ₁x₁ + … → lineal en x, por eso la **frontera es un hiperplano**.
- Datos: m ejemplos, x = [x₀, x₁, …, xₙ]ᵀ con **x₀ = 1**, y ∈ {0, 1}.
!!! El 1 al inicio (lo enfatizó "enérgicamente")
x₀ = 1 multiplica a θ₀ (sesgo). Si se omite o se pone al final, x y θ no cuadran: el algoritmo no converge o "da cosas raras".

## 4. Costo: entropía cruzada binaria
Con error cuadrático y sigmoide el costo **no es convexo** (mínimos locales). Se usa un costo logarítmico por casos:
- Cost = −ln(h) si y = 1; Cost = −ln(1 − h) si y = 0.
- **J(θ) = −(1/m) Σ [y ln h + (1 − y) ln(1 − h)]** — convexa, un solo mínimo global.
| Caso | y | h_θ(x) | Costo | Lectura |
|---|---|---|---|---|
| 1 | 1 | 0.90 | −ln 0.90 ≈ 0.105 | Muy pequeño |
| 2 | 1 | 0.40 | −ln 0.40 ≈ 0.916 | Elevado |
| 3 | 0 | 0.15 | −ln 0.85 ≈ 0.162 | Muy pequeño |
| 4 | 0 | 0.80 | −ln 0.20 ≈ 1.609 | Sumamente alto |
Castiga la confianza equivocada. Error común: entrenar logística con MSE.

## 5. Descenso por gradiente
θⱼ := θⱼ − α ∂J/∂θⱼ (α = tasa de aprendizaje). El gradiente son las derivadas parciales: la dirección de mayor variación.
**Derivación en el pizarrón:**
1. g′(z) = e⁻ᶻ/(1 + e⁻ᶻ)² = **g(z)(1 − g(z))**.
2. ∂J/∂θⱼ = (1/m) Σ (h_θ(x⁽ⁱ⁾) − y⁽ⁱ⁾) xⱼ⁽ⁱ⁾.
3. **θⱼ := θⱼ − α (1/m) Σ (h − y) xⱼ**.
α típico: 0.1–0.5 en logística; ≈ 10⁻⁴ en redes neuronales.
| Modalidad | Actualiza | Nota |
|---|---|---|
| Por lotes (batch) | Tras los m ejemplos | Preciso, costoso; inviable con datos masivos |
| **Minilotes** | Tras cada bloque | Lo más usado en la industria |
| Estocástico (SGD) | Tras cada ejemplo | Muy rápido, trayectoria ruidosa |
Error común: α demasiado grande (diverge o brinca el mínimo).

## 6. Regularización
Cuando los pesos crecen demasiado (θ = 5000, 2,000,000) el modelo memoriza.
| | Costo | Actualización | Efecto |
|---|---|---|---|
| **L2 (Ridge)** | BCE + (λ/2m) Σθⱼ² | θⱼ −= α[(1/m)Σ(h − y)xⱼ + (λ/m)θⱼ] | Encoge todos los pesos, sin volverlos 0 |
| **L1 (Lasso)** | BCE + (λ/m) Σ\|θⱼ\| | θⱼ −= α[(1/m)Σ(h − y)xⱼ + (λ/m)sign(θⱼ)] | Lleva pesos irrelevantes **exactamente a 0**: selección de características (métodos embebidos, Clase 02) |
Advertencia: con λ enorme en L1 todos los θ van a 0 (subajuste total).

## 7. Multiclase
- **Uno vs. el resto (OvR):** K clasificadores binarios; gana la clase con probabilidad más alta (sus probabilidades no tienen por qué sumar 1).
- **Softmax (multinomial):** z_k = w_kᵀx + b_k; **P(y = C_k | x) = e^(z_k) / Σⱼ e^(z_j)**, suman 1; costo J = −Σᵢ Σ_k y_ik ln P; predicción ŷ = argmax_k P. Es la capa de salida estándar en redes neuronales.

## 8. Clases desbalanceadas: pesado por clases
!!! Fórmula
**w_k = m / (K · m_k)** (m = total, K = número de clases, m_k = ejemplos de la clase k). Se multiplica el costo de cada ejemplo por el peso de su clase.
Ejercicio: m = 1000, K = 2, clase 0 con 950 y clase 1 con 50.
- w₀ = 1000/(2 × 950) = 1000/1900 ≈ **0.526**.
- w₁ = 1000/(2 × 50) = 1000/100 = **10**.
Un error en la minoritaria pesa ≈ 19 veces más. Vital en fraude (≈ 0.1 %) o enfermedades raras. Sin pesos, el modelo predice siempre la mayoritaria con una "exactitud alta" engañosa.

## 9. Consideraciones finales
- **Ventajas:** inferencia rápida, salida interpretable como probabilidad, costo convexo, pocos hiperparámetros, bien con pocos datos.
- **Limitaciones:** solo fronteras lineales; sensible a outliers y multicolinealidad.
- Ejemplo en Python: 91 VN, 36 VP, 22 FP y 5 FN. Recomendación: estandarizar antes de entrenar.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Por qué no lineal.** Un outlier inclina la recta y corre el umbral; además sale de [0, 1].

!!! Modelo y costo (examen)
h = 1/(1 + e^(−θᵀx)) con **x₀ = 1 al inicio**. Logit lineal → frontera hiperplano. Costo: entropía cruzada binaria (convexa); el MSE con sigmoide no es convexo. Casos: y=1,h=0.9 → 0.105; y=0,h=0.8 → 1.609.

**Gradiente.** g′ = g(1 − g) → θⱼ := θⱼ − α(1/m)Σ(h − y)xⱼ. Batch, minilotes (industria), SGD.

| Tema | Para recordar |
|---|---|
| L2 (Ridge) | Encoge pesos |
| L1 (Lasso) | Pesos a 0 = selección; λ enorme → todo 0 |
| OvR | K binarios, gana el más alto |
| Softmax | e^(z_k)/Σe^(z_j), suman 1, argmax |
| Pesado por clases | w_k = m/(K·m_k): 950/50 → 0.526 y 10 |
