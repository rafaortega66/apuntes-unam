% materia: Reconocimiento de Patrones
% titulo: Clase 6 · Funciones de decisión lineales y multiclase
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 14 sep 2026 (sesión 9 del curso) · Tema 5 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Repaso: métricas y validación
- Precisión = TP/(TP + FP) (de lo predicho positivo, cuánto es real); recall = de lo realmente positivo, cuánto capturó.
- Matriz de confusión: diagonal = aciertos. Alarma de incendio: FP = suena sin fuego; FN = hay fuego y no suena.
| AUC | Interpretación |
|---|---|
| 1.0 | Perfecto |
| 0.9–1.0 | Excelente |
| 0.7–0.9 | Bueno/regular |
| 0.5 | Aleatorio |
| < 0.5 | Invertido |
- **K-Fold:** K subconjuntos permutados para no depender de una partición.

## 2. Funciones de decisión
Pipeline: patrones → características (x ∈ ℝⁿ) → selección/reducción → clasificador. g(x) da un escalar cuyo **signo** decide la clase.
| Tipo | Forma | Nota |
|---|---|---|
| Lineal | g(x) = wᵀx + w₀ | Hiperplano; simple e interpretable; solo clases linealmente separables |
| Cuadrática | xᵀAx + bᵀx + c | Más flexible; más parámetros, sobreajuste |
| No lineal | Arbitraria | Difícil de entrenar; se transforma a un espacio separable |
- wi = importancia de xi. g > 0 → clase 1; g < 0 → clase 2; **g = 0 → frontera**: al azar o según el costo del error (en diagnóstico de cáncer se prefiere el falso positivo).

## 3. Multiclase
| Esquema | Regla |
|---|---|
| **1 vs. Resto** | Clase i si Di(x) > 0 **y** Dj(x) < 0 para todo j ≠ i |
| **1 vs. 1** | Clase i si Dij(x) > 0 para todo j ≠ i |
| **Máquina lineal** | Clase con el **gi(x) máximo**; sin zonas ambiguas |
- **Región de ambigüedad:** dos o más positivas, o todas negativas.
- Funciones generalizadas / ensambles: g(x) = Σ wi·fi(x); wi = confianza (voto) de cada clasificador.

## 4. Ejercicios resueltos en clase
**Binario:** g(x) = −3 + 0.75x1 + x2. (4,3): −3 + 3 + 3 = **3 > 0 → clase 1**; (0,0): **−3 → clase 2**.
**1 vs. Resto:** D1 = −x1 + x2; D2 = x1 + x2 − 5; D3 = −x2 + 1.
| Punto | D1 | D2 | D3 | Clase |
|---|---|---|---|---|
| (6,5) | −1 | 6 | −4 | 2 |
| (0,2) | 2 | −3 | −1 | 1 |
| (6,4) | −2 | 5 | −3 | 2 |
| (2,−2) (lo resolví yo) | −4 | −5 | 3 | 3 |
| (2,6) (Jorge) | 4 | 3 | −5 | **Ambigüedad** |
Error común: un negativo no es indeterminación; lo es tener **dos o más positivos**.

## 5. Interpretación geométrica
- g(x) = 0 es el hiperplano; **w es perpendicular** a él.
- Distancia dirigida: **r = g(x)/‖w‖**.
| Espacio | Ejes | Puntos |
|---|---|---|
| Características (ℝⁿ) | Variables medibles | Patrones |
| Pesos | w0…wn | Clasificadores completos |
Frontera: g(x) = 0 o gi(x) = gj(x).

## 6. Aprendizaje de pesos (perceptrón)
1. w en ceros o aleatorio pequeño.
2. Para cada (xi, yi), evaluar el signo de g(xi).
3. Si el signo está mal: **w = w + α·error·xi** (α = tasa de aprendizaje).
4. Iterar hasta error aceptable o máximo de iteraciones; inferir con el signo.

## 7. Funciones ortogonales
g(x) = Σ wk·φk(x). Ventajas: sin redundancia, pocos coeficientes, wk independientes, estabilidad numérica.
| Familia | Dominio | Uso |
|---|---|---|
| Legendre | [−1, 1] | Formas, contornos, imágenes |
| Laguerre | [0, ∞) | — |
| Hermite | (−∞, ∞) | Voz, audio, visión, datos gaussianos |

## 8. Clasificación vs. agrupamiento vs. RP
Clasificación = supervisada (con etiquetas); clustering = no supervisado (sin etiquetas); reconocimiento de patrones = todo el proceso. Error común: llamar "clasificación" al clustering.
Próxima clase: clustering (funciones de distancia y luego de similitud). Sin tarea.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Ejercicio tipo examen
Evaluar cada Di en el punto. 1 vs. Resto: exactamente un positivo → esa clase; dos o más positivos (o ninguno) → ambigüedad. Ej.: (2,6) con D1 = 4, D2 = 3 → ambiguo.

| Concepto | Para recordar |
|---|---|
| g(x) = wᵀx + w0 | Signo decide; g = 0 es la frontera |
| Máquina lineal | Gana el gi máximo; no hay ambigüedad |
| Distancia | r = g(x)/‖w‖; w ⟂ hiperplano |
| Perceptrón | w = w + α·error·xi si se equivoca |
| Ortogonales | Legendre [−1,1], Laguerre [0,∞), Hermite (−∞,∞) |
