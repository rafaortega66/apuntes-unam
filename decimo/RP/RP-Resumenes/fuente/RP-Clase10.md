% materia: Reconocimiento de Patrones
% titulo: Clase 10 · Primer Examen Parcial
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 28 sep 2026 (sesión 13 del curso) · Día de examen · Resumen de examen

# PARTE 1 · El examen

!!! Datos
En papel, sesión completa de 7:00 a 8:30. **Calificación: 20.5** escrita en el examen; **20/100** en Classroom (solo la parte entera; los decimales se guardan para la final). Examen escaneado y solución en `decimo/RP/RP-Examenes/RP-E01/`. La revisión pregunta por pregunta fue la **Clase 11** (2 oct).

## Estructura
| Bloque | Preguntas | Puntos |
|---|---|---|
| Teoría (65 %) | 32: la 1 vale 3; de la 2 a la 32, 2 cada una | 65 |
| Práctica (35 %) | 33 Hu (10), 34 GLCM norte-sur (10), 35 LDA con eigenvalores (15) | 35 |
Según el profesor, toda la teoría salió de diapositivas y discusiones de clase; dos ejercicios eran iguales a las tareas y el tercero una adaptación de un ejemplo del pizarrón.

## Temas que entraron y dónde repasarlos
| Preguntas | Tema | Clases |
|---|---|---|
| 1–6 | Patrón, supervisado/no supervisado, etapas del sistema, espacios de características y de pesos, maldición de la dimensionalidad | −2, 6 |
| 7, 8, 12 | Extracción vs. selección; propiedades de un buen conjunto; **7 pasos de MFCC en orden** | −1, 1 |
| 13–16 | Filtrado, wrapper, embebidos; PCA vs. LDA | 2, 3 |
| 17–21 | Hold-out, K-Fold (la prueba no se usa en cada iteración), data drift | 4 |
| 22–24 | Funciones discriminantes, frontera gi = gj | 6 |
| 25–29 | Distancia mínima, Mahalanobis, K-Means, LBG, ISODATA | 7 |
| 30–32 | Bayes, posterior, QDA vs. LDA vs. Naive Bayes | 8 |
| 33 | Momentos → Hu con escala logarítmica | 0, 1 |
| 34 | GLCM: transpuesta, normalizar (÷ 40), ASM, energía, contraste | 0, 1 |
| 35 | LDA a mano: medias, S_B, S_W, inversa, λ y vector | 3 |
!!! Corrección del ejercicio 35
Con los datos impresos: μ2 = (8.4, 7.6), −2.2 en S_W y λ1 ≈ **7.83**; el profesor usó −2.02 y obtuvo 7.74. El eigenvector (2.34, 1) es el mismo.

# PARTE 2 · Qué repasar para el siguiente

| Prioridad | Qué |
|---|---|
| 1 | LDA completo a mano (15 pts, el de más peso) |
| 2 | GLCM: simétrica + normalizada antes de los descriptores |
| 3 | Cadena de momentos hasta Hu y logaritmo |
| 4 | Orden de MFCC; métricas y ROC (sensibilidad, especificidad, FPR) |
