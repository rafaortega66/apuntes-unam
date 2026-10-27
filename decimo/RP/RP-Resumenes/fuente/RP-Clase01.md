% materia: Reconocimiento de Patrones
% titulo: Clase 1 · Extracción de características: estadísticas, Hu, GLCM, HOG y audio
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 28 ago 2026 (sesión 4 del curso) · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Qué es y por qué reducir
Transformar datos crudos en un vector compacto: y ∈ ℝᴺ → x ∈ ℝᵈ, d ≪ N. Pocas muestras limitan la dimensión confiable; características correlacionadas degradan; más características = clasificador más complejo. Se busca **discriminabilidad, compacidad, robustez y bajo costo**.

## 2. Características estadísticas
μ = (1/N)Σxi; σ² = (1/N)Σ(xi − μ)²; skewness = Σ(xi − μ)³/(Nσ³); exceso de curtosis = Σ(xi − μ)⁴/(Nσ⁴) − 3.
| | Skewness | Curtosis |
|---|---|---|
| > 0 | Cola a la derecha | Concentrada, colas pesadas |
| = 0 | Simétrica | Como la normal |
| < 0 | Cola a la izquierda | Dispersa, colas ligeras |
- **Ventanas** (con o sin traslape; L = 4, 50 %, paso 2). Combinar: concatenar (crece la dimensión), estadísticas de estadísticas, **pooling** (máx σ²). No vale en señales estacionarias, muy ruidosas o con ventanas muy pequeñas.
- **Histograma** como vector: simple, robusto, invariante a traslación; pierde lo espacial y depende de los bins.

## 3. Momentos geométricos y de Hu
| Momento | Fórmula | Invariante a |
|---|---|---|
| Espacial | M(p,q) = ΣΣ x^p y^q f(x,y); área = M00; centroide = (M10/M00, M01/M00) | Nada |
| Central | μ(p,q) = ΣΣ (x − x̄)^p (y − ȳ)^q f | Traslación |
| Normalizado | ηij = μij / μ00^((i+j)/2 + 1), i + j ≥ 2 | Traslación y escala |
| **Hu** (7) | De los normalizados; se usa escala logarítmica | **Traslación, escala y rotación** |
**Ejercicio (5×5, cuatro unos en x ∈ {2,3}, y ∈ {1,2}):** M00 = 4, M10 = 10, M01 = 6, M11 = 15. Centroide (2.5, 1.5). μ00 = 4, μ10 = μ01 = 0, μ11 = 0.25 − 0.25 − 0.25 + 0.25 = **0** (μ11 = M11 − x̄·M01).

## 4. Textura: GLCM
Matriz N×N: P(i, j | d, θ) = cuántas veces el nivel i aparece junto a j a distancia d en dirección θ.
1. Definir **distancia d y dirección θ** (los dos parámetros).
2. Contar transiciones.
3. **Simétrica:** sumar la matriz y su **transpuesta**.
4. **Normalizar** dividiendo entre el total.
5. Estadísticos: contraste, dissimilarity, homogeneidad; ASM/energía, entropía; media, varianza, correlación.
**Ejemplo (4×4, niveles 0–3, d = 1, θ = 0°, 12 pares):** fila 0: 2 2 1 0; fila 1: 0 2 0 0; fila 2: 0 0 3 1; fila 3: 0 0 0 1.

## 5. HOG
1. Normalizar a 0–1 y **redimensionar a 64 × 128** (persona 1090×612 → recorte 196×438 → 64×128).
2. Gradientes por convolución: filtro **1×3 (Gx, bordes verticales)** y **3×1 (Gy, bordes horizontales)**; M = √(Gx² + Gy²), θ = arctan(Gy/Gx).
3. Celdas de **8 × 8**; histograma 0–180° en **9 bins de 20°**; cada píxel suma su magnitud a su bin (θ > 180 → restar 180).
4. Bloques de **2 × 2 celdas** = 36 valores, normalizados (L2, L1, L1-sqrt) para robustez a iluminación; se desplazan celda por celda.
!!! Vector HOG (examen)
**105 bloques × 36 = 3,780** valores para una imagen de 64 × 128.

## 6. SIFT y SURF
- **SIFT:** gaussianas sucesivas → **Diferencia de Gaussianas (DoG)** → puntos clave → **128** características por punto; invariante a escala, rotación y luz.
- **SURF** (~2004): más rápido; añade el radio de influencia del punto. Usos: objetos, video, rostros, realidad aumentada.

## 7. Audio
**Temporales:** E = Σx²; RMS = √(Σx²/N); **ZCR** (alto = ruido, bajo = armónico); autocorrelación R(k) = Σ x[n]x[n − k].
- Ej.: [0.5, −0.3, 0.8, −0.2] → E (promedio) = 0.255. [0.5, 0.3, −0.2, −0.4, 0.1] → 2 cruces → ZCR = 4/(2·5) = **0.4**.
**Espectrales** (FFT; supone señal **estacionaria**): con {100, 500, 1000, 2000} Hz y {0.1, 0.5, 0.3, 0.1}:
| Descriptor | Resultado |
|---|---|
| Centroide Σf|X|/Σ|X| | (10 + 250 + 300 + 200)/1.0 = **760 Hz** |
| Ancho de banda | ≈ **498.4 Hz** |
| Roll-off (85 %) | Bin 3 (la página da 150 Hz en un bloque y 1500 Hz en otro: verificar) |
| Flux [0.2,0.5,0.3] → [0.3,0.4,0.8] | 0.01 + 0.01 + 0.25 = **0.27** |
| Flatness [0.1, 0.2, 0.15] | 0.144/0.15 ≈ **0.96** (plano) |

## 8. MFCC
Escala Mel: **Mel(f) = 2595·log₁₀(1 + f/700)** (lineal en graves, logarítmica en agudos).
1. **Preénfasis:** y[n] = x[n] − αx[n − 1] (α ≈ 0.95).
2. **Framing:** 20–40 ms, 50 % de solape.
3. **Hamming:** w[n] = 0.54 − 0.46 cos(2πn/(N − 1)); evita discontinuidades en los bordes.
4. **FFT** → espectro de potencia.
5. **Banco de 20–40 filtros triangulares Mel.**
6. **Logaritmo** de las energías.
7. **DCT.**
8. **Truncar** a 12–13 coeficientes, **descartando el coeficiente 0** (energía promedio).
!!! Irreversible (examen)
Del MFCC **no se puede reconstruir el audio**: se truncan coeficientes de la DCT y se descarta la fase de la FFT.
- **Δ** = velocidad (ventana actual − anterior); **ΔΔ** = aceleración. Con ambos: 39 por ventana.
**Vector final:** 13 MFCC × 4 estadísticos (media, σ, máx, mín) = 52; 2 temporales × 4 = 8; 5 espectrales × 4 = 20 → **80**.

## Pendiente: Tarea 1 (viernes, Classroom)
Hu de una figura en forma de "C" (hasta los 7 momentos); GLCM Oeste-Este y Norte-Sur (d = 1), simétrica, normalizada, con contraste, energía y entropía (6 valores); un párrafo sobre **LBP**. Próxima: selección de características.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Momentos | Espacial → central (traslación) → normalizado (+ escala) → Hu (+ rotación) |
| GLCM | d y θ; + transpuesta; normalizar; contraste, energía, entropía |
| HOG | 64×128, celdas 8×8, 9 bins, bloques 2×2 (36) → 3,780 |
| SIFT | DoG; 128 por punto |
| ZCR | Alto = ruido |
| MFCC | Preénfasis, frames, Hamming, FFT, Mel, log, DCT, truncar (sin el 0) |
| Audio total | 52 + 8 + 20 = 80 |
