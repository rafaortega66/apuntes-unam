% materia: Reconocimiento de Patrones
% titulo: Clase −1 · Extracción de características I: estadísticas, ventanas e histograma
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 21 ago 2026 (sesión 2 del curso) · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Fuente
**No asistí** (me inscribí tarde) y **no hay audio**. Todo sale del deck «Clase 2. Extracción de características» (Classroom, 21 ago). Los números se revisaron con las fórmulas del deck; donde no cuadran, se marca.

## 1. Qué es y qué se busca
Transformar datos crudos en x = (x1, …, xn)ᵀ: y ∈ ℝᴺ → x ∈ ℝᵈ, d ≪ N.
- **Por qué menos:** muestras finitas limitan la dimensión confiable; características correlacionadas degradan; la complejidad crece con n.
- **Pasos:** analizar el dato → identificar propiedades → medirlas → vector comparable.
!!! Pregunta 8 del primer parcial
Se busca **discriminabilidad** (separar clases), **compacidad** (reducir dimensión), **robustez** (ruido, variación intra-clase) y **bajo costo computacional**.

## 2. Estadísticas
μ = (1/N)Σxi; σ² = (1/N)Σ(xi − μ)²; skewness = Σ(xi − μ)³/(Nσ³); curtosis en exceso = Σ(xi − μ)⁴/(Nσ⁴) − 3. (El deck trae la curtosis con σ³ y potencia 3; la correcta usa 4.)
| | Skewness | Curtosis |
|---|---|---|
| > 0 | Cola a la derecha | Concentrada, colas pesadas |
| = 0 | Simétrica | Como la normal |
| < 0 | Cola a la izquierda | Dispersa, colas ligeras |
- **Ejemplo 1:** seis señales con media ≈ 5; la **varianza** separa x1–x3 (0.36, 0.25, 0.5) de x4–x6 (9.5, 12, 8.75).
- **Ejemplo 2:** media ≈ 11.5 y σ² ≈ 1.62–1.68 en todas; las separa la **forma**: x1–x3 cerca de (0, −1.2) y x4–x6 cerca de (1.85, 2.45) en el plano skewness–curtosis.

## 3. Ventanas locales
Señal: 2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1 (media global 5: no dice que sube y baja).
| Esquema | Ventanas | Medias |
|---|---|---|
| Sin traslape (L = 4) | 4 | 3.5, 7.5, 6.5, 2.5 (σ² = 1.25) |
| Con traslape 50 % (paso 2) | 7 | 3.5, 5.5, 7.5, 8.0, 6.5, 4.5, 2.5 |
(El deck da σ² = 0.25 para ω4 = 8,9,8,7; con la fórmula sale **0.5**.)
- **Concatenar:** conserva lo local; la dimensión crece (8 o 14 valores).
- **Estadísticas de estadísticas:** sin traslape, media de medias 5.0 y varianza 4.25; con traslape 5.42 y 3.60.
- **Pooling:** p. ej. máx σ²k.
| Enfoque | Captura |
|---|---|
| Global | Tendencia general |
| Local | Cambios y estructura |
| Local + pooling | Estructura y robustez |
No conviene con señales estacionarias, datos muy ruidosos, ventanas muy pequeñas o si la estructura local no importa.

## 4. Histograma como vector
h = (146, 870, 1159, 1394, …); imágenes (grises o RGB) y audio.
| Ventajas | Desventajas |
|---|---|
| Simple, robusto al ruido, invariante a permutaciones, dimensión controlable, sirve con pocos datos | Pierde lo espacial, sensible a los bins, ignora vecinos |
Más adelante: **HOG** sí conserva estructura local.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Se busca | Discriminabilidad, compacidad, robustez, bajo costo |
| Skewness | Signo = hacia dónde va la cola |
| Curtosis | > 0 colas pesadas; < 0 ligeras |
| Ventanas | Con o sin traslape; concatenar, estadísticas de estadísticas, pooling |
| Histograma | Robusto y simple; pierde la posición |
