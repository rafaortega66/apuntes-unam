% materia: Reconocimiento de Patrones
% titulo: Clase 0 · Momentos geométricos, Hu y textura con GLCM
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 24 ago 2026 (sesión 3 del curso) · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Fuente
**No asistí** (me inscribí tarde) y **no hay audio**. Todo sale del deck oficial «Clase 3. Extracción de características II» (Classroom, 27 ago). El profesor confirmó en la Clase 1 que aquí se vieron los momentos geométricos. Los resultados de los ejemplos 1, 2 y 4 los calculé con las fórmulas del deck.

## 1. Momentos geométricos
Las medidas geométricas simples no bastan para formas complejas ni dan invariancia.
- **Espaciales:** M_pq = ΣΣ xᵖ yᵠ f(x, y). Área = M00; centroide = (M10/M00, M01/M00).
- **Centrales:** μ_pq = ΣΣ (x − x̄)ᵖ (y − ȳ)ᵠ f → invariantes a **traslación**. μ00 = M00; μ10 = μ01 = 0; μ11 = M11 − x̄M01.
- **Normalizados:** η_ij = μ_ij / μ00^(1 + (i+j)/2), i + j ≥ 2 → + **escala**; siguen variando con la rotación.
**Ejemplo 1 (5×5, cuadrado 2×2 en (1,2), (1,3), (2,2), (2,3); x = fila):** M00 = 4; M10 = 6; M01 = 10; M11 = 15; centroide (1.5, 2.5).
**Ejemplo 2:** μ00 = 4, μ10 = μ01 = 0, μ11 = 15 − 1.5·10 = **0** (simétrico, sin inclinación).

## 2. Momentos de Hu
**7 momentos** invariantes a **rotación, escala y traslación**, a partir de los η:
- I1 = η20 + η02
- I2 = (η20 − η02)² + 4η11²
- I3 = (η30 − 3η12)² + (3η21 − η03)²
- I4 = (η30 + η12)² + (η21 + η03)²
- I5, I6, I7: combinaciones de tercer orden (ver el deck).
**Ejemplo 3 (plátano vs. huevo), con escala logarítmica H = −signo(h)·log₁₀|h|:**
| Objeto | Hu1 | Hu2 | Hu3 | Hu4 | Hu5 | Hu6 | Hu7 |
|---|---|---|---|---|---|---|---|
| Plátano | 0.518 | 1.257 | 2.318 | 3.257 | −6.194 | −3.972 | 6.194 |
| Huevo | 0.789 | 2.966 | 5.254 | 7.186 | 13.407 | 8.669 | −14.687 |
Sin logaritmo, los de orden alto (e-07, e-15) no pesan nada frente a Hu1. Los Hu solo describen la silueta, no la textura.

## 3. GLCM
P(i, j | d, θ): cuántas veces el nivel i tiene a j como vecino a distancia d en dirección θ (N×N). Arena vs. pasto: la diferencia es la textura, no la forma.
**Ejemplo 4 (d = 1, θ = 0, 4 niveles):**
```
0 0 1 1
0 0 1 1
0 2 2 2
2 2 3 3
```
| | O→E (0 1 2 3) | E→O (0 1 2 3) | Simétrica (0 1 2 3) |
|---|---|---|---|
| 0 | 2 2 1 0 | 2 0 0 0 | 4 2 1 0 |
| 1 | 0 2 0 0 | 2 2 0 0 | 2 4 0 0 |
| 2 | 0 0 3 1 | 1 0 3 0 | 1 0 6 1 |
| 3 | 0 0 0 1 | 0 0 1 1 | 0 0 1 2 |
Normalizada (÷ 24): diagonal 0.166, 0.166, 0.250, 0.083; fuera: 0.083 (0–1), 0.042 (0–2, 2–3).
| Descriptor | Fórmula | Ejemplo 4 (cálculo propio) |
|---|---|---|
| Contraste | Σ P(i − j)² | 14/24 ≈ 0.583 |
| Dissimilarity | Σ P\|i − j\| | 10/24 ≈ 0.417 |
| Homogeneidad | Σ P/(1 + (i − j)²) | ≈ 0.808 |
| ASM / energía | Σ P² / √ASM | 0.146 / 0.382 |
| Entropía | −Σ P ln P | ≈ 2.10 |
| Media, varianza | μ = Σ iP; σ² = Σ P(i − μ)² | 1.29; 1.04 |
| Correlación | Σ P(i − μi)(j − μj)/√(σi²σj²) | ≈ 0.72 |
Error común: olvidar la **transpuesta** o calcular con conteos sin **normalizar**.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Entró en el primer parcial
Ejercicio 33: cadena de momentos hasta Hu (10 puntos). Ejercicio 34: GLCM norte-sur con ASM, energía y contraste (10 puntos).

| Concepto | Para recordar |
|---|---|
| Espaciales | M00 área; centroide M10/M00, M01/M00 |
| Centrales | Quitan traslación; μ10 = μ01 = 0 |
| Normalizados | Quitan escala; i + j ≥ 2 |
| Hu | 7; quitan rotación; usar −signo·log₁₀ |
| GLCM | d y θ → contar → + transpuesta → ÷ total |
| Descriptores | Contraste, homogeneidad, ASM, energía, entropía, correlación |
