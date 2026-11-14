% materia: Reconocimiento de Patrones
% titulo: Clase 21 · RNN, LSTM y Transformers
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 13 nov 2026 · Procesamiento de lenguaje natural: de las RNN a los Transformers (última clase teórica) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Cierre de lenguaje natural: RNN y desvanecimiento del gradiente, celdas LSTM, y la arquitectura Transformer (tokens, codificación posicional, autoatención Q-K-V, atención multicabeza, normalización por capas, generación de texto, RAG y modelos derivados); alcance del segundo examen.

!!! Fuente
🔢 Sesión 24 del curso (cronología real). Fuente: NotebookLM (audio `RP-Clase21.m4a`, completo), 14 nov 2026. ⚠️ marca datos dudosos. Fechas sin contrastar con Classroom.

## 1. De N-gramas a vectores densos y redes recurrentes
**CBOW** predice una palabra faltante a partir de su contexto; **Skip-gram**, a partir de una palabra, infiere las que la rodean (es más difícil de entrenar). Una **RNN** mantiene un estado oculto hₜ (memoria de lo visto) y lo combina con la entrada xₜ para predecir.

!!! En simple
CBOW: te dan la oración menos una palabra y adivinas el hueco; Skip-gram: te dan la palabra del medio y adivinas las de alrededor. La RNN es leer una novela cargando un resumen mental que actualizas con cada frase. Límite: con mil palabras, ese resumen se «apaga» al multiplicar muchas veces valores pequeños hacia atrás.

Para la oración larga «el perro que estaba jugando… su pelota», las representaciones discretas no sirven; cada palabra pasa a ser un vector denso en un espacio latente.

En la RNN, cada celda recibe hₜ y xₜ, con neuronas completamente conectadas, y produce yₜ y la memoria siguiente.

¿Cuál es el problema? Los alumnos dijeron que pierde la memoria del inicio. El profesor precisó: es el **desvanecimiento del gradiente**; con capas conectadas en secuencia y tangente hiperbólica (saturada), las derivadas multiplicadas hacia atrás se vuelven tan pequeñas que las primeras capas casi no se actualizan. Funciona con 50–100 palabras y falla con 1,000–2,000.

## 2. Celdas LSTM y codificador-decodificador
Celda recurrente con compuertas que deciden qué mantener, qué actualizar y qué descartar.

!!! En simple
Una autopista superior casi intacta y tres porteros: uno tira los recuerdos viejos (olvido), otro decide qué anotar (entrada) y otro qué pasar al siguiente paso (salida). Límite: sigue procesando en fila india, así que entrena lento.

La línea de estado Cₜ lleva la información casi limpia de un extremo a otro, parecido a una conexión residual, para que fluya el gradiente. **Compuerta de olvido:** cuánto conservar de la celda anterior. **De entrada:** cuánto de lo nuevo guardar. **De salida:** cuánto mandar a la siguiente celda.

En codificador-decodificador, el codificador comprime la oración en un vector de contexto y el decodificador genera la traducción palabra por palabra; si el vector fijo no capturaba una oración larga, la traducción salía mal (por eso el Google Translate de antes tenía errores).

Su gran defecto: es secuencial y difícil de paralelizar.

## 3. El Transformer: arquitectura agnóstica y tokens
Arquitectura del artículo *Attention Is All You Need* (⚠️ NotebookLM dice ~2018; el artículo es de 2017) que no supone nada sobre el tipo de dato y procesa secuencias completas en paralelo. Un **token** es información encapsulada en un vector: la unidad de entrada y salida.

!!! En simple
CNN y RNN son especialistas con anteojeras (cuadrícula de píxeles, fila temporal). El Transformer convierte todo (palabras, parches de imagen, fragmentos de audio) en fichas iguales y las analiza a la vez. Límite: no suponer nada le cuesta muchísimos datos y cómputo.

GPT = *Generative Pretrained Transformer*. Modelos con alto sesgo (CNN: vecindad espacial; RNN: dependencia secuencial) contra el Transformer agnóstico. Tiene codificador y decodificador (ChatGPT, Claude y Gemini usan el decodificador).

Flujo: secuencia → *embeddings* contextuales (como «banco») → + codificación posicional → bloques Transformer → capa lineal → Softmax para la siguiente palabra. Las imágenes se parten en parches, el audio en fragmentos.

## 4. Codificación posicional
Información numérica de la posición de cada token, sumada a su *embedding*.

!!! En simple
Como el Transformer recibe todas las fichas a la vez, se le escribe a cada una su número de asiento con tinta invisible.

Se suma un vector calculado con senos y cosenos (alternando según la posición par o impar) o una tabla de *embeddings* entrenable.

## 5. Autoatención y atención multicabeza
La atención deja que cada token decida a qué otros prestar más importancia. La multicabeza repite el cálculo n veces en paralelo para captar distintos tipos de relaciones.

!!! En simple
En una junta preguntas «¿a quién se refiere ‘su’?» (query), cada quien muestra un cartel de lo que es (key), comparas qué tan bien encaja cada cartel y mezclas el contenido (value) de quienes importan.

«El corazón de todo el Transformer». Los *embeddings* pasan por capas lineales y se proyectan en **Q** (qué busco), **K** (qué ofrezco) y **V** (mi contenido real).

1. Multiplicar Q por Kᵀ y escalar entre la dimensionalidad de las keys (en la fórmula original, entre la raíz de d_k).
2. Softmax: pesos entre 0 y 1 que suman 1 (cerca de 1 = prestar atención).
3. Multiplicar por V.

Se repite en n cabezas (verbos con sustantivos, adjetivos con sustantivos…); las salidas se concatenan y una capa lineal las regresa al tamaño original. Permite relacionar palabras lejanas o regiones distintas de una imagen.

## 6. El bloque Transformer: residual, LayerNorm y feed-forward
Atención multicabeza → suma y normalización por capas → feed-forward → otra suma y normalización. **LayerNorm** normaliza sobre las características de cada muestra; **BatchNorm** sobre los ejemplos del lote.

!!! En simple
Tabla de alumnos (filas) por materias (columnas): BatchNorm compara a todos los alumnos en una materia; LayerNorm equilibra todas las materias de un alumno.

La salida de la atención se suma con la entrada (residual) y pasa por LayerNorm, para el flujo del gradiente. Feed-forward: lineal → GELU (no saturada) → dropout → lineal → dropout. Otra suma y LayerNorm.

Entrada y salida del bloque tienen la misma dimensión, así que se apilan; más bloques, mejor desempeño.
Error común: confundir LayerNorm con BatchNorm.

## 7. Clasificación, generación, ventajas, RAG y modelos derivados
**Generación:** predecir el siguiente token, añadirlo a la entrada y repetir. **RAG** (*Retrieval-Augmented Generation*): conectar el modelo a una base de datos actualizada para que consulte antes de responder y no invente.

!!! En simple
Sin RAG, el modelo es un alumno brillante encerrado que solo recuerda lo que estudió hace años: si le preguntas los horarios del próximo semestre, dice «no sé» o inventa. Con RAG consulta la carpeta actualizada.

Clasificación (oración positiva o negativa): embeddings + posicional → bloques → capa de clasificación y pérdida. Generación: «H O L» → probabilidad de la siguiente letra → se anexa y se repite. Por eso la IA entiende aunque tengas errores de dedo.

**Ventajas:** se entrena en paralelo, modela dependencias largas (resumir un PDF completo), escala con más bloques y parámetros, da representaciones contextuales. Aplicaciones: clasificación, traducción, resumen, NER, generación, sentimiento, RAG.

**Sesgo contra datos:** una CNN desde cero va muy bien con ~1 millón de imágenes; un Transformer desde cero necesita ~300 millones, pero con esos datos supera a la CNN, y el *transfer learning* es muy poderoso. **Desventajas:** alto costo de cómputo, muchísimos datos y baja interpretabilidad.

Derivados: BERT, GPT, ViT (visión) y Segment Anything (segmentación).

## Pendiente / próxima clase
- Fue la última clase teórica.
- **Última tarea** (13 nov), para el **miércoles 18 nov**: (1) calcular a mano el índice Gini en la raíz y los dos nodos internos de un árbol dado, la clase de cada hoja y qué ejemplos caen en cada una; (2) diseñar una red de 3 neuronas con escalón unitario que aproxime una operación lógica (⚠️ el enunciado salió poco claro en el audio).
- **Lunes 16 nov:** sin clase. **Viernes 20 nov:** última práctica (15 min por equipo). **Lunes 23 nov: segundo examen parcial.** **Viernes 27 nov:** proyecto final (hasta media hora por equipo).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Alcance del segundo examen: desde los clasificadores de aprendizaje automático a partir de DBSCAN; extensión parecida al primero; mayoría opción múltiple más ejercicios de clase o tareas.** lo respondió directamente al inicio de la clase.
- **Ejercicios tipo la última tarea: índice Gini en un árbol y un perceptrón multicapa con escalón.** dijo que los ejercicios salen de clase y tareas, y dejó esos dos de tarea.
- **Por qué fallan las RNN en secuencias largas y cómo lo resuelve la LSTM.** preguntó al grupo, corrigió y lo ligó con el desvanecimiento del gradiente.
- **Transformer agnóstico, autoatención Q-K-V y atención multicabeza.** fue el tema central («pongan atención»); no resolvió un cálculo con matrices.
- **LayerNorm contra BatchNorm y qué es RAG.** preguntó si conocían RAG y lo explicó con un ejemplo de la Facultad.

!!! Puntos clave
- Segundo examen (23 nov): desde DBSCAN; teoría de opción múltiple más ejercicios como las tareas (Gini, perceptrón con escalón).
- RNN: desvanecimiento del gradiente; LSTM: compuertas de olvido, entrada y salida + línea de estado.
- Transformer: tokens + codificación posicional + autoatención (Q·Kᵀ escalado → Softmax → ·V), multicabeza, residual + LayerNorm, feed-forward con GELU.
- RAG evita que invente; necesita muchos datos; BERT, GPT, ViT.

## Ponte a prueba
1. **¿Por qué una RNN falla con secuencias largas?** Por el desvanecimiento del gradiente: con tanh saturada, las derivadas multiplicadas hacia atrás se vuelven tan pequeñas que las primeras capas no se actualizan.
2. **¿Qué hacen las tres compuertas de una LSTM?** Olvido: cuánto conservar; entrada: cuánto de lo nuevo guardar; salida: cuánto mandar a la siguiente celda.
3. **¿Qué significa que el Transformer sea agnóstico?** Que no supone nada sobre el tipo de dato: todo se convierte en tokens.
4. **¿Para qué la codificación posicional?** Para que, al procesar todo en paralelo, no se pierda el orden; se suma un vector (seno/coseno o entrenable).
5. **Pasos de la autoatención.** Q·Kᵀ, escalar, Softmax y multiplicar por V; se repite en varias cabezas y se concatena.
6. **LayerNorm contra BatchNorm.** LayerNorm normaliza sobre las características de cada muestra; BatchNorm sobre los ejemplos del lote.
7. **¿Qué es RAG?** Conectar el modelo a una base de datos actualizada para que consulte antes de responder y no invente.
8. **¿Cuándo conviene una CNN y cuándo un Transformer desde cero?** CNN con ~1 millón de imágenes; el Transformer necesita ~300 millones, pero con esos datos gana.
