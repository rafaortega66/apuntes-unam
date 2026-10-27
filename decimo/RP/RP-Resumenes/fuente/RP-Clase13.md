% materia: Reconocimiento de Patrones
% titulo: Clase 13 · Práctica 3: QDA, LDA y Naive Bayes en la práctica
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 9 oct 2026 (sesión 16 del curso) · Tema 7 (cierre) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Sesión de exposición y evaluación de la Práctica 3. El profesor aclaró que la Práctica 3 no entra en el segundo parcial, pero preguntó los conceptos de abajo a los dos equipos.

## 1. Parte 1 de la práctica: segmentación de imágenes por color
Clasificación **píxel a píxel** con QDA en RGB: 4 imágenes de entrenamiento de 360,000 píxeles (**1,440,000** en total) y 3 de prueba.
- **Etiquetado automático temporal con umbrales HSV** (dibujar máscaras a mano era más exacto pero demasiado lento):
| Clase | Umbral HSV |
|---|---|
| Plátano | 15 ≤ H ≤ 38, S ≥ 75, V ≥ 75 |
| Chile | 35 ≤ H ≤ 95, S ≥ 75, V ≥ 45 |
| Huevo | Blanco (umbrales de saturación y valor) |
| Fondo | El complemento de las otras tres |
- El fondo fue 1,103,000 píxeles (**76.6 %**): fuerte desbalance → el prior del fondo pesa mucho.
- Dataset de 4 columnas (R, G, B, clase). En las covarianzas 3 × 3, los valores fuera de la diagonal (verde–rojo 524 en plátano, 601 en chile) mostraron **dependencia entre canales**, lo que justifica QDA.
- La **variación dentro de una clase** (brillos en el chile, sombras en el plátano) la absorbe la **matriz de covarianza**.
!!! Clase no vista (la papa)
En la prueba 3 apareció una papa: se clasificó como plátano (por tono) y como huevo (por brillo). Un clasificador supervisado **siempre elige una de las clases que conoce** (menor Mahalanobis / mayor posterior). Solución: agregar la clase "papa" al entrenamiento o un umbral de rechazo. Cambiar a HSV no lo arregla.
Sin máscaras de referencia para las pruebas, el análisis fue cualitativo.

## 2. Parte 2: Breast Cancer Wisconsin
569 observaciones, 30 características; 212 malignos (37.26 %) y 357 benignos (62.74 %). Split 80/20 con `stratify` y `random_state=42`; estandarización Z-score. QDA con `reg_param = 10⁻⁴`, LDA estándar y GNB.
| Modelo | VP | FN | FP | VN | Exactitud |
|---|---|---|---|---|---|
| QDA / LDA | 38 | 4 | 1 | 71 | (38 + 71)/114 = **95.61 %** |
| Gaussian Naive Bayes | 38 | 4 | 4 | 68 | (38 + 68)/114 = **92.98 %** |
| Línea base (siempre "benigno") | — | — | — | — | 62.74 % |
114 muestras de prueba (42 malignas, 72 benignas). El equipo 1 dijo 95.95 % y 91.92 %, que no corresponden a sus matrices.
!!! Recall en diagnóstico (lo preguntó a ambos equipos)
Es preferible **más recall en la clase maligna** que más precisión: un **falso negativo** (enfermo clasificado como sano) es el error más costoso.

## 3. QDA y regularización de la covarianza
QDA supone que cada clase es una **normal multivariada con su propia covarianza**:
**gᵢ(x) = −½ (x − μᵢ)ᵀ Σᵢ⁻¹ (x − μᵢ) − ½ ln|Σᵢ| + ln P(ωᵢ)**
| Término | Significado |
|---|---|
| (x − μ)ᵀ Σ⁻¹ (x − μ) | **Distancia de Mahalanobis** al cuadrado a la media de la clase (en código: `(x - mu) @ inv(Sigma) @ (x - mu).T`) |
| −½ ln\|Σᵢ\| | Penaliza clases muy "infladas" |
| ln P(ωᵢ) | Probabilidad a priori |
!!! Regularización: Σ + λI
Sumar una constante pequeña a la diagonal garantiza |Σ| > 0 y que **exista Σ⁻¹** cuando hay pocas muestras o canales colineales (estabilidad numérica). `reg_param` de la librería es ese λ. Con λ demasiado grande todas las nubes se vuelven esferas y se pierde lo que distingue a QDA.

## 4. Naive Bayes con variables correlacionadas
GNB supone **independencia condicional** (covarianza diagonal): multiplica probabilidades sin términos cruzados. En Breast Cancer las 30 mediciones del tumor están muy correlacionadas, así que GNB tira información útil: más FP (4 vs. 1) y menor exactitud que QDA/LDA.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Segmentación.** QDA píxel a píxel en RGB con etiquetas por umbrales HSV; fondo 76.6 % (prior grande). La covarianza absorbe brillos y sombras; covarianzas cruzadas grandes justifican QDA.

!!! Conceptos preguntados
- **Recall** de malignos > precisión: el FN es el peor error.
- **Σ + λI** (reg_param): evita Σ singular.
- (x − μ)ᵀ Σ⁻¹ (x − μ) = **Mahalanobis**.
- **GNB** pierde con variables correlacionadas (supone independencia).
- **Clase no vista:** el clasificador la asigna a una conocida (la papa → plátano/huevo); hay que agregarla.

| Breast Cancer | Exactitud |
|---|---|
| QDA / LDA | 95.61 % (4 FN, 1 FP) |
| GNB | 92.98 % (4 FN, 4 FP) |
| Siempre "benigno" | 62.74 % |
