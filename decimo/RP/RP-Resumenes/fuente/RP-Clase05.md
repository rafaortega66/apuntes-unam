% materia: Reconocimiento de Patrones
% titulo: Clase 5 · Práctica 1: PCA, SVD y Eigenfaces
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 11 sep 2026 (sesión 8 del curso) · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Nota personal
Exposición y evaluación de la Práctica 1. No grabé mi exposición; el profesor me hizo preguntas y no supe responderlas: hay que estudiar estos temas a fondo (sección 6).

## 1. Centrado, estandarización y covarianza
- **Centrar:** restar el vector de medias (xi − μ); el centro de la nube queda en el origen.
- **Estandarizar:** además, dividir entre σ; escalas comparables. Indispensable con unidades distintas.
**Ejemplo sintético (200 muestras, 2 características):**
| Elemento | Valor |
|---|---|
| Varianzas (diagonal) | 1.04 y 5.9 |
| Covarianzas | 2.1 y 2.1 → fuerte correlación positiva |
| PC1 | [0.35, 0.93] |
| PC2 | [0.93, −0.35] |
| Ortogonalidad | Producto punto = 0; W·Wᵀ = identidad (90°) |
Error común: confundir centrar con estandarizar.

## 2. ¿Cuántas componentes (K)?
| Criterio | Regla |
|---|---|
| Codo | Donde la curva de varianza (scree plot) cae y se aplana |
| Kaiser | Autovalor **λ > 1** |
| Umbral acumulado | Mínimo de componentes para 90 % o 95 % |
- **Iris (4 características):** PC1 = 92.46 %, PC2 = 5.3 %. 90 % → 1 componente; 95 % → 2 (97.7 %, mitad de la dimensión).
- **Wine (13, SVD estandarizado):** autovalores 4.7, 2.5, 2.1 y el cuarto < 1 → codo y Kaiser = **3**; umbral 90 % = 8, 95 % = 10. Que los criterios difieran es normal: responden preguntas distintas.

## 3. Escala, reconstrucción y equivalencias
- **Wine sin estandarizar:** PC1 absorbe **99.809 %**, PC2 0.74 %; las variables de magnitud grande dominan la covarianza.
- **MSE de reconstrucción (Wine):** 1 componente 0.6; 2 → 0.4; … 13 → 0.0.
- Covarianza manual, SVD y scikit-learn dan **autovalores idénticos**; los autovectores pueden salir con **signo opuesto** (×−1): misma dirección, no es error.

## 4. Olivetti Faces (Eigenfaces)
- 400 imágenes de 64×64 → matriz **400 × 4096**.
- **Rostro promedio** = media de cada píxel.
- Primeras eigenfaces: forma global (silueta, ojos, mandíbula); últimas: detalle fino, iluminación, ruido.
| Componentes | Reconstrucción |
|---|---|
| 10 | Borrosa |
| 50–100 | Rasgos del individuo |
| 200–300 | Prácticamente idéntica |
- **X̂ = Z·Wᵀ + μ**: con K pequeño, Z·Wᵀ aporta poco y domina μ → se parece al rostro promedio.
Error común: creer que las primeras componentes separan clases; PCA es no supervisado.

## 5. Álgebra de la proyección
Xc es M×N; W (autovectores elegidos) es **N×K**; **Z = Xc·W** es M×K.

## 6. Preguntas del profesor en la evaluación
1. ¿Centrar vs. estandarizar? — Restar μ / restar μ y dividir entre σ.
2. Iris, ¿1 o 2 componentes? — 92.46 % puede bastar; con 97.7 % se separan mejor Versicolor y Virginica.
3. ¿Kaiser? — Autovalor > 1; en Wine, 3.
4. ¿Cuántos autovectores da PCA? — **Tantos como características**: 4, 13, 4096.
5. ¿Dimensión de W? — N×K.
6. ¿Por qué pocas eigenfaces dan el rostro promedio? — Por el término + μ.

## Pendiente
Próxima sesión el lunes; dos alumnos se juntan para quedar en dos equipos.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Pregunta | Respuesta |
|---|---|
| ¿Cuántos autovectores? | Igual al número de características |
| Kaiser | λ > 1 (Wine: 4.7, 2.5, 2.1 → 3) |
| Iris | PC1 92.46 %; con 2 → 97.7 % |
| Sin estandarizar (Wine) | PC1 se lleva 99.8 % |
| Proyección | Z = Xc·W; W es N×K |
| Reconstrucción | X̂ = Z·Wᵀ + μ; MSE baja hasta 0 con todas |
| Signo distinto | Misma dirección (×−1) |

!!! Repasar antes del examen
Centrar ≠ estandarizar; por qué pocas eigenfaces = rostro promedio; dimensiones de las matrices.
