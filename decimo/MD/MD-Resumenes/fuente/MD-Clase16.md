% materia: Minería de Datos
% titulo: Clase 16 · Diabetes (cierre) y redes neuronales
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 27 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Cierre de las exposiciones de diabetes e introducción a las redes neuronales. Las cifras de las exposiciones son de los equipos. Continúa la Clase 15.

!!! Fuente
NotebookLM (audio MD-Clase16.m4a). Lo no contrastado con el audio se marca como dudoso.

## 1. Cierre de la práctica de diabetes
- 829 registros: 64 % sin diabetes (537), 36 % con diabetes (292). Decir "nadie tiene diabetes" da 64 % de accuracy → usar recall, precisión, F1, ROC-AUC.
- Ceros en glucosa, presión, grosor de piel, insulina, IMC = datos no tomados; un equipo los reemplazó con la mediana.
- Descartadas: insulina y grosor de piel (demasiados ceros); urea y lipoproteína (igual en sanos y enfermos).
- Medianas: glucosa 139 vs. 108 mg/dL; IMC 34.3 vs. 30.3.
!!! Variable trampa (examen)
El identificador de la persona (ID) se elimina desde el origen: es una etiqueta, no información. El profesor la puso a propósito.

| Modelo | Lo reportado (70/30) |
|---|---|
| Regresión logística | Momios ×2.47 por desv. est. de glucosa, ×2.1 por IMC; 37 FN |
| Árbol de decisión | Podado a 4 niveles; 32 FN |
| Random Forest (mejor) | 0.832, validación cruzada de 5 pliegues; 55 de 83 diabéticos, 28 FN |

- Falsos positivos: glucosa ~143, IMC ~38 (prediabetes, obesidad severa).
- Falsos negativos: glucosa promedio 119.5, sobre todo jóvenes; 39 personas fallaron en los tres modelos.
- **Umbral de 0.5 a 0.35:** menos falsos negativos a cambio de más falsos positivos.
!!! Falso negativo = el error caro
"Lo más crítico son los falsos negativos porque dejan ir a una persona enferma a su casa sin tratamiento." Un falso positivo solo cuesta un estudio de confirmación.
Error común: dejar el ID como predictor; evaluar solo con accuracy; no sacar la lista de pacientes en FP y FN.

## 2. El perceptrón y cómo aprende
- Entradas x1…xn; pesos w1…wn; suma ponderada Z = x1·w1 + … + xn·wn.
- Sesgo B: Z + B mueve el punto de activación.
- Salida: **Y = f(Z + B)**.
1. **Forward propagation:** entrada → ocultas → salida: predicción.
2. Se compara con el valor real: error.
3. **Backpropagation:** el error vuelve de la salida a la entrada y ajusta pesos y sesgo.
4. **Época:** una pasada completa por todos los datos.
- Ejemplo (flores): época 1 ≈ 0.5; épocas 10–20 ≈ 0.7–0.8; 30–50 ≈ 0.9 y se estabiliza. Más épocas ya no mejoran.
- Hiperparámetros: tasa de aprendizaje, tamaño de lote, capas ocultas y neuronas.
Error común: pocas épocas (subajuste) o demasiadas con pocos datos (sobreajuste).

## 3. Funciones de activación
| Función | Qué hace | Dónde va |
|---|---|---|
| ReLU | max(0, x) | Capas ocultas |
| Sigmoide | 1 / (1 + e^−x): entre 0 y 1 | Salida binaria |
| Softmax | Probabilidades que suman 1 | Salida multiclase |
- Ejemplo softmax: adulto 0.70, joven 0.20, niño 0.10 = 1.00.

## 4. Arquitecturas
| Red | Datos | Ejemplo |
|---|---|---|
| MLP (densa) | Tablas | Fraude, abandono de clientes, riesgo crediticio |
| CNN (convolucional) | Imágenes | Neumonía en 5,856 radiografías, recall 96 % |
| RNN (LSTM, GRU) | Secuencias: series de tiempo, texto, audio | Memoria de pasos anteriores |
### Flujo de una CNN
1. Imagen (matriz de píxeles).
2. Convolución: filtros que sacan bordes, texturas, formas.
3. ReLU.
4. Pooling: reduce tamaño.
5. Aplanado: matriz → vector.
6. Capa densa.
7. Salida con softmax o sigmoide.
- Data augmentation: rotar e inclinar imágenes para evitar sobreajuste.

## Pendiente
- Práctica de redes neuronales: **individual**.
- Práctica de series de tiempo: última entrega y exposición en equipo.
- Examen: NotebookLM dice "jueves 13 de noviembre"; dudoso, el 13 nov 2026 es viernes. Confirmar.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Idea para recordar |
|---|---|
| Falso negativo | El error caro en salud: enfermo a casa sin tratamiento |
| Umbral 0.35 | Menos FN a cambio de más FP |
| Variable trampa | El ID: eliminarlo desde el origen |
| Perceptrón | Y = f(Σ xi·wi + B) |
| Aprendizaje | Forward → error → backpropagation; época = pasada completa |
| Activación | ReLU ocultas; sigmoide binaria; softmax multiclase |
| Arquitectura | MLP tablas; CNN imágenes; RNN secuencias |

!!! Hilo conductor
Elegir el modelo y su umbral según el costo del error, y elegir la red según el tipo de datos.
