% materia: Reconocimiento de Patrones
% titulo: Clase 20 · CNN, autoencoders y arranque de NLP
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 9 nov 2026 (sesión 23 del curso) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Por qué las redes densas fallan con imágenes
La IA contiene al aprendizaje automático, que contiene al aprendizaje profundo. La visión computacional busca detectar, segmentar y reconocer objetos.
- Una imagen de 224×224×3 (RGB) son **150,528 entradas**.
- Con una capa oculta de 1024 neuronas: 150,528 × 1024 ≈ **154 millones de pesos** solo en dos capas.
- Aplanar la imagen destruye la **vecindad espacial** entre píxeles.

## 2. Convolución, correlación cruzada y autocorrelación
!!! Convolución
Refleja una señal respecto al origen y la desplaza multiplicando y sumando. (f∗g)[n] = Σ f[k] g[n−k]. Es **conmutativa**: f∗g = g∗f.

- **Correlación cruzada:** igual, pero **sin reflejar**; el orden sí importa.
- **Autocorrelación:** la señal contra sí misma, para hallar patrones repetitivos.
- **1D:** audio. **2D:** imágenes. **3D:** video o imágenes satelitales. Procesar video en 1D se puede forzar, pero destruye movimiento y espacio.

## 3. Redes convolucionales (CNN)
Los filtros (kernels) deslizantes aprenden por descenso de gradiente; sus coeficientes son los pesos de la red. Un filtro 3×3×3 tiene solo **27 coeficientes**.
| Hiperparámetro | Qué controla |
|---|---|
| Número de filtros | Cuántos mapas de características salen (32 filtros, 32 mapas) |
| Stride | Cuántos píxeles avanza el filtro por paso |
| Padding | Bordes de ceros para cubrir extremos sin encoger el mapa |

## 4. Pooling, convolución transpuesta y 1×1
| Operación | Qué hace |
|---|---|
| Max pooling | Conserva el máximo de la ventana |
| Average pooling | Promedia la ventana |
| Global average pooling | Un valor por canal; evita capas densas enormes |
| Convolución transpuesta | Aumenta la resolución (segmentación, generativas) |
| Convolución 1×1 | Cambia el número de canales sin cambiar alto ni ancho |

No hay un pooling universalmente mejor: depende de la arquitectura y la tarea.

## 5. Arquitectura típica de una CNN
1. Extracción: convolución + activación no lineal + pooling, repetidos.
2. Transición: flatten o global average pooling.
3. Clasificación: red totalmente conectada; salida con sigmoide (binaria) o softmax (multiclase), una neurona por clase.

## 6. ResNet y evolución histórica
!!! Conexión residual
H(x) = F(x) + x. La derivada de +x es 1, así que el gradiente fluye por el atajo y no se desvanece.

- **Bloque básico:** canales constantes (64 a 64).
- **Bottleneck:** 1×1 baja de 256 a 64, 3×3 en medio, 1×1 restaura a 256, y se suma la identidad.
- Si x y F(x) no coinciden en dimensiones, se ajusta con una convolución 1×1.
- Línea del tiempo: LeNet (1998), AlexNet (2012), VGGNet y GoogLeNet, ResNet (2015), MobileNet (2017), EfficientNet, Vision Transformers.

## 7. Autoencoders
Red no supervisada que reconstruye su entrada pasando por un espacio latente.
- **Encoder:** comprime (784 variables a 8 o 10 valores). **Decoder:** reconstruye. Compresión **con pérdida** (no como ZIP).
- **Anomalías:** se entrena solo con datos normales; la anomalía produce un error de reconstrucción alto (fraude bancario).
- **Denoising:** entrada ruidosa, salida limpia. **Compresión y recomendación:** guardar solo el vector latente.

## 8. Aumento de datos y transferencia
- **Aumento de datos:** rotaciones, volteos, recortes, color o brillo, desenfoque; la red aprende invariancias.
- **Transferencia:** partir de un modelo preentrenado (ImageNet, 200,000 radiografías) para una tarea con pocos datos (1,000 imágenes de piel). Converge más rápido y generaliza mejor.
- Error común: entrenar desde cero con menos de unas 2,000 imágenes.

## 9. Introducción a NLP y N-gramas
El orden importa: «el perro mordió al hombre» no es «el hombre mordió al perro». Tres niveles: caracteres, palabras y dependencias largas.
- **N-grama:** la siguiente palabra depende solo de las n−1 anteriores (supuesto de Markov). Bigramas de 2 palabras, trigramas de 3.
- Ejemplo del corpus: tras «el gato», 67 % «come» y 33 % «bebe».
- **Limitaciones:** explosión combinatoria (10⁶ bigramas y 10⁹ trigramas con 1000 palabras), contexto corto y probabilidad cero para lo no visto.

## 10. Sintaxis, semántica, TF-IDF y embeddings
- **Sintaxis:** bien construida. **Semántica:** con sentido («vi al hombre con el telescopio» es ambigua).
- **TF-IDF:** peso bajo a palabras comunes, alto a las distintivas; ausente en el documento, 0.
- **Embeddings estáticos** (Word2Vec, GloVe, FastText): un vector fijo por palabra; rey − hombre + mujer ≈ reina.
- **Embeddings contextuales** (Transformers, BERT, GPT): el vector cambia con el contexto («banco» de dinero o de parque).

## 11. Avisos de la clase
- **Práctica 5:** se sube el lunes; entrega y exposición el siguiente viernes presencial (15 a 20 min). Tema [material]: CNN para clasificar imágenes; por confirmar en Classroom.
- **Última tarea:** se deja el viernes; cálculos sencillos a mano; entrega el lunes o el viernes siguiente.
- **Segundo examen parcial:** el lunes de la última semana (fecha por confirmar); calificaciones por Classroom.
- **Proyecto final:** viernes 27 nov; exposición de 25 a 30 minutos; código en el reporte solo si es esencial.
- Próxima clase: Transformers (atención, BERT y GPT).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Por qué convolución (examen)
Imagen 224×224×3 = 150,528 entradas; con 1024 neuronas ocultas, ≈ 154 millones de pesos. Un filtro 3×3×3 usa 27 coeficientes y respeta la vecindad espacial.

| Concepto | Idea clave |
|---|---|
| Convolución contra correlación | La convolución refleja y es conmutativa; la correlación no |
| CNN | Convolución + activación + pooling, luego flatten o GAP y capa densa |
| ResNet | H(x) = F(x) + x; el gradiente pasa por el atajo |
| Autoencoder | Encoder, espacio latente y decoder; anomalía = error alto |
| Aumento de datos contra transferencia | Datos nuevos artificiales contra pesos preentrenados |
| N-gramas | Markov; explosión combinatoria, contexto corto, probabilidad cero |
| Embeddings | Estáticos: un vector por palabra. Contextuales: cambian con el contexto |

**Números a recordar.** 150,528 entradas; ≈ 154 millones de pesos; 27 coeficientes; bottleneck 256 → 64 → 256; 10⁶ bigramas y 10⁹ trigramas con 1000 palabras.
