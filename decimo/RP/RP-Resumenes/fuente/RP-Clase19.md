% materia: Reconocimiento de Patrones
% titulo: Clase 19 · Revisión de la Práctica 4
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · viernes 6 nov 2026 (sesión 22 del curso) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Nota sobre la grabación
El audio está incompleto al inicio: arranca a mitad de las preguntas de la exposición de la Práctica 4 (KNN y regresión logística). No hubo teoría nueva; es la revisión de la práctica y el cierre administrativo.

## 1. Elección de k en KNN
**KNN** decide por voto de la mayoría entre los k vecinos más cercanos (algoritmo perezoso basado en instancias).
- En la práctica el mejor puntaje de exactitud salió con **k = 41** (con otro pico en k = 81).
- El equipo argumentó que, aunque la práctica pedía el mejor k numérico, conviene un valor menor para no suavizar de más las fronteras.
- [material] k muy pequeño (k = 1): sobreajuste, fronteras irregulares, sensible al ruido. k muy grande: subajuste, fronteras sobresuavizadas, rendimiento hacia el azar.

## 2. Estrategia de lotes en regresión logística
El profesor preguntó qué estrategia de lotes usaron.
- Breast Cancer: **569** observaciones; partición 80/20 → **455** de entrenamiento y **114** de prueba.
- El equipo mandó los 455 ejemplos juntos en cada iteración (lote completo).
- En regresión logística la entropía cruzada binaria es **convexa**: no hay mínimos locales y converge al mínimo global. En redes neuronales no es convexa, por eso allí se usan minilotes.

## 3. Caja blanca contra caja negra
| Modelo | Interpretabilidad |
|---|---|
| Regresión logística | Caja blanca: z = θ₀ + Σ θᵢxᵢ pasada por la sigmoide; cada θᵢ muestra el impacto y la dirección de xᵢ |
| Redes neuronales profundas | Caja negra: muchas transformaciones no lineales; difícil explicar la decisión |

Importa en áreas como la salud, donde hay que saber qué rasgos llevaron al diagnóstico.

## 4. Regularización L1 y L2 en los pesos θ
La penalización (con hiperparámetro λ) frena el crecimiento de θ y el sobreajuste.
| Caso | Comportamiento de θ |
|---|---|
| Sin regularizar | Crecen sin control; en la práctica quedaron en [−1.5, 1.5], pero en problemas reales pueden llegar a 25,000, 50,000 o 100,000 |
| L1 (Lasso) | Los pesos varían y los que no aportan se vuelven exactamente 0 (selección de características) |
| L2 (Ridge) | No anula; estabiliza y acota los pesos (≈ 15 épocas) |

- [material] L2: J = BCE + (λ/2m)·Σθⱼ², gradiente extra (λ/m)·θⱼ. L1: J = BCE + (λ/m)·Σ|θⱼ|, gradiente extra (λ/m)·signo(θⱼ).
- L1 cuando muchas características son ruido (modelo disperso); L2 cuando todas aportan y se busca estabilidad.
- Un λ demasiado grande: con L1 anula todo; con L2 encoge tanto que subajusta.

## 5. Signo y tamaño de los pesos
Un θ positivo empuja hacia una clase (p. ej. maligno) y uno negativo hacia la otra (benigno). No significa «mejor» ni «peor»: importa el conjunto de variables, ninguna decide sola. «Dimensión fractal» quedó pegada a cero: candidata a descartarse con L1.

## 6. Pesado por clase
Penaliza más los errores sobre la clase minoritaria. Dataset: 357 benignos y 212 malignos (569).
!!! Regla del profesor («ojo, esto es muy importante»)
Se aplica sobre la **clase** (etiquetas), nunca sobre las características ni sobre ejemplos aislados.

- [material] w_k = m / (K·m_k): m total de ejemplos, K número de clases, m_k ejemplos de la clase k.
- Evita predecir siempre la clase mayoritaria con una exactitud aparentemente alta.

## 7. Avisos de la clase
- **Próxima clase (lunes 9 nov):** terminar redes neuronales.
- **Práctica 5:** la deja el lunes; con el lunes feriado siguiente (NotebookLM dijo «17 de noviembre»; el lunes es el 16, por confirmar) la entrega y exposición pasan al viernes. Sin contrastar con Classroom.
- **Proyecto final:** último viernes, 27 nov según el audio (el sitio decía 30 nov tentativo). 30 % reporte y código, 20 % exposición, 50 % metodología. Opciones: FER2013 o RAF-DB, RAVDESS, Speech Commands (35 clases).
- Después: procesamiento de lenguaje natural y Transformers.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Tema | Idea que debes poder explicar |
|---|---|
| L1 contra L2 | L1 manda pesos a 0 (dispersión); L2 los acota sin anularlos |
| Caja blanca contra negra | Regresión logística: se leen los θᵢ. Redes: no |
| Pesado por clase | Sobre la clase, no sobre características ni ejemplos |
| Lote completo | Converge al mínimo global porque la entropía cruzada binaria es convexa |
| Elegir k | No tomar a ciegas el pico de exactitud; k grande sobresuaviza |

**Números a recordar.** 569 observaciones; 455 entrenamiento y 114 prueba; 357 benignos y 212 malignos; k = 41 mejor puntaje.

!!! Signo de θ (examen)
Positivo o negativo no es «bueno» o «malo»: cada peso empuja la probabilidad hacia una clase y lo que decide es la combinación de todas las variables.
