# **RP · Guía para el examen final**

**Reconocimiento de Patrones** · Semestre 2027-1 · 16 nov 2026  
*Hecha con NotebookLM a partir de todas las fuentes del cuaderno de la materia (audios de cada clase y material del profesor): hilo conductor del curso, unidades con sus conceptos explicados, lo que más probablemente viene y las conexiones entre conceptos. Acompáñala con el mapa mental (RP-mapa-mental.pdf, en esta misma carpeta).*  
*Clases que no estaban en el cuaderno: −2, −1, 0, 10, 15\. Su resumen va en el Anexo al final.*

## **\> Aclaración sobre las fuentes del cuaderno: Este cuaderno contiene 19 transcripciones de audio de las clases (RP-Clase1.m4a a RP-Clase21.m4a, faltando las grabaciones de las Clases 10 y 15). No hay archivos separados de diapositivas ni PDFs escritos cargados en el cuaderno; cuando se mencionan valores ambiguos o con ruido en las transcripciones automáticas, se indica expresamente. Además, el contenido de Máquinas de Soporte Vectorial (SVM) (correspondiente a la Clase 15 ausente) se cubre a partir del repaso detallado que dio el profesor al inicio de la Clase 16 y sus menciones en las Clases 17 y 19\.**

## **1\. HILO CONDUCTOR**

Todo sistema de reconocimiento de patrones arranca con una pregunta práctica: cómo lograr que una máquina perciba el mundo físico —imágenes, audio o texto— y tome decisiones confiables sobre él. Como una computadora no entiende objetos ni sonidos directamente, el primer paso es la **detección** y la **extracción de características**: transformar datos crudos en vectores numéricos compactos y discriminantes (como momentos geométricos, GLCM o HOG para imágenes, y descriptores temporales, espectrales o MFCC para audio). Sin embargo, extraer demasiadas variables dispara la **maldición de la dimensionalidad**, haciendo que los modelos sobreajusten y que las distancias pierdan sentido. Por eso, antes de clasificar, hay que depurar el espacio de entrada mediante **selección de características** (quedarse con las variables más útiles) o **reducción de dimensionalidad** como PCA y LDA (proyectarlas a un espacio más compacto sin perder la varianza o la separabilidad entre clases). Con los datos listos, necesitamos reglas rigurosas de **evaluación** —matrices de confusión, precisión, recall, curvas ROC, validación cruzada y vigilancia contra fuga de datos y *data drift* — porque entrenar un modelo que memoriza sin generalizar no sirve en el mundo real.

## **Ya con un espacio bien representado y una forma confiable de medir errores, entra el núcleo de decisión: los modelos de agrupamiento y clasificación. La historia comienza con funciones de decisión lineales y cuadráticas clásicas que trazan fronteras geométricas en el espacio de características, y luego se bifurca según si conocemos o no las etiquetas: cuando no hay etiquetas, los algoritmos no supervisados descubren grupos naturales por distancia o cuantización (K-Means, LBG, ISODATA) o por densidad sin asumir formas esféricas (DBSCAN); cuando sí hay etiquetas, pasamos a modelos supervisados que deciden por probabilidad y teoría de Bayes (QDA, LDA, Naive Bayes), por memoria local de vecinos (KNN), por fronteras lineales optimizadas con descenso de gradiente y regularización (Regresión Logística), o maximizando el margen con trucos de kernel (SVM). Cuando los datos tabulares presentan fronteras complejas no lineales, evolucionamos hacia árboles de decisión (regiones rectangulares por pureza Gini/entropía) y ensambles que combinan múltiples árboles débiles en paralelo (Random Forest) o secuencialmente corrigiendo residuos (Gradient Boosting). Finalmente, para no depender de extraer características a mano en datos masivos con estructura espacial o secuencial (donde los modelos tabulares fallan), damos el salto al aprendizaje profundo: perceptrones multicapa, redes convolucionales (CNN) y autoencoders para imágenes, y modelos secuenciales (RNN/LSTM) hasta llegar al Transformer con autoatención y *embeddings* contextuales, capaz de procesar texto, audio o imagen de forma agnóstica y paralela.**

## **2\. UNIDADES Y TEMAS DEL CURSO**

### **Unidad 1: Fundamentos del Sistema de Reconocimiento y Extracción de Características**

*(Clases 1 y 11\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Un sistema de reconocimiento de patrones consta de cuatro etapas: **detección** (tomar mediciones del patrón), **extracción de características**, **clasificación** y **evaluación del modelo**. Esta unidad resuelve el problema inicial de convertir datos crudos (píxeles o señales de onda) en vectores numéricos medibles con cuatro propiedades deseables: **discriminabilidad** (separar clases), **compacidad** (dimensión reducida), **robustez** (tolerar ruido y variaciones intraclase) y **bajo costo computacional**. Prepara la entrada numérica para todas las unidades posteriores.

#### **(b) Conceptos clave**

> * **Patrón y Aprendizaje Supervisado vs. No Supervisado** *(Clase 11\)*: Un **patrón** es cualquier objeto, proceso o entidad que puede ser descrito y distinguido de otros; es **supervisado** cuando se conoce de antemano la etiqueta de clase (ej. perro, gato) y **no supervisado** cuando se desconocen las etiquetas y el número de clases. *Analogía:* es como clasificar fruta con etiquetas ya pegadas en la caja vs. ordenar fruta desconocida por parecido físico. *Ejemplo:* el reconocimiento supervisado clasifica especies o diagnósticos médicos, mientras el no supervisado agrupa pacientes por similitud de características sin diagnóstico previo.  
> * **Momentos Geométricos y Momentos de Hu** *(Clases 1 y 11\)*: Descriptores de **forma** para imágenes binarias/objetos que corrigen progresivamente variaciones geométricas en cuatro niveles: **espaciales** (mpq), **centrados** (μpq, invariantes a traslación), **normalizados** (ηpq\=μpq/μ00^(1+(p+q)/2), invariantes a traslación y escala, pero aún variantes a rotación) y **Momentos de Hu**, invariantes a **traslación, escala y rotación**. *Analogía:* medir la silueta de una llave desde su propio centro y en proporción a su tamaño para reconocerla aunque esté girada o lejos de la cámara. *Ejemplo de examen (Clase 11):* dada una imagen en forma de "H", se calculó μ00\=m00\=5, xˉ=2.4, m11\=27⟹μ11\=27−2.4(12)=−1.8, μ20\=3.2, μ02\=3.2, obteniendo η11\=−0.072, η20\=η02\=0.128 y finalmente Hu2\=(η20−η02)2\+4η112\=0.020736 (en escala logarítmica 1.6832).  
> * **GLCM (Matriz de Coocurrencia de Niveles de Gris)** *(Clases 1 y 11\)*: Descriptor de **textura** que cuenta con qué frecuencia ocurren pares de intensidades luminosas a una **distancia** dada y en una **dirección** θ (ej. oeste-este o norte-sur), y luego se divide entre el total de cuentas (tras sumar su transpuesta para volverla simétrica) para obtener una matriz de probabilidades y extraer medidas como **contraste**, **energía**, **ASM** y **entropía**. *Analogía:* recorrer una tela con una regla de 1 cm mirando qué tan seguido junto a un hilo blanco hay un hilo negro. *Ejemplo (Clase 11):* en el ejercicio 34 del examen, se dio una imagen cuantizada para calcular GLCM norte-sur a distancia de 1 píxel, normalizando por el total (ej. 40 en la explicación) antes de aplicar ASM=∑pij2, Energía=√(ASM) y Contraste=∑pij(i−j)2.  
> * **HOG (Histograma de Gradientes Orientados)** *(Clase 1\)*: Descriptor de **forma y bordes** que codifica magnitudes y orientaciones de los cambios de intensidad luminosa en regiones locales. *Analogía:* trazar sobre una foto un mapa de pequeñas flechas que señalan hacia dónde cambia la luz en cada cuadrito, resumiendo el contorno y estructura interna del objeto. *Ejemplo real de clase:* una imagen original de 1090×612 píxeles se recorta a 196×438 y se redimensiona al estándar de 64×128**píxeles**; se aplican filtros detectores de bordes 1×3 (eje X, detecta bordes verticales) y 3×1 (eje Y, detecta bordes horizontales), se calcula magnitud √(Gx2\+Gy2) y orientación tan−1(Gy/Gx) ajustada a \[0^∘,180^∘) (restando 180^∘), se divide en celdas de 8×8, se agrupan bloques de 4 celdas (36 valores normalizados con L2 o L1) y al deslizarlos sobre toda la imagen resulta un vector de 3,780**características**. También se mencionaron **SIFT** (puntos clave mediante diferencia de gaussianas, vector de 128**características** por punto, robusto a escala, rotación, luz y perspectiva moderada) y **SURF** (versión más rápida hacia 2004).  
> * **Descriptores de Audio (Temporales, Espectrales y MFCC)** *(Clases 1 y 11\)*: El audio es una señal 1D de amplitud en el tiempo. *Analogía:* estudiar una canción midiendo qué tan fuerte suena (temporal), qué notas agudas o graves contiene (espectral) y cómo la percibiría el oído humano (tiempo-frecuencia MFCC). *Ejemplos concretos con números reales de la Clase 1:*  
  * **Temporales:** Energía y **RMS** (raíz de la energía promedio en ventana, ej. 4 muestras); **Tasa de Cruces por Cero (ZCR)**, que cuenta cambios de signo (alto \= ruido/percusivo, bajo \= armónico; en el ejemplo de ventana 0.3, 0.5, \-0.2... dio 0.4); **Autocorrelación** (desplazar la señal sobre sí misma).  
  * **Espectrales (vía FFT, que asume estacionariedad): Centroide espectral** (para frecuencias 100,500,1000,2000 Hz con amplitudes 0.1,0.5,0.3,0.1 da 760 Hz); **Ancho de banda espectral** (498.4 Hz); **Spectral Rolloff** (punto donde se acumula el 85% de la amplitud total 1.2, es decir 1.02, alcanzado en el bin 3 a 150 Hz); **Flujo espectral** (cambio cuadrático entre frames t y t−1, resultado 0.27); **Spectral Flatness** (media geométrica 0.144 / media aritmética 0.15 \= 0.96, espectro plano).  
  * **MFCC (Coeficientes Cepstrales en Frecuencia Mel):** siguen **7 pasos en orden estricto**: (1) **Preénfasis** (filtro paso altas x\[n\]−αx\[n−1\]), (2) **Framing** (ventanas de 20**a** 40 ms con 50% de solapamiento), (3) **Ventana de Hamming** (atenúa extremos para evitar artefactos de la FFT), (4) **FFT** y espectro de potencia, (5) **Banco de** 20**a** 40**filtros triangulares en escala Mel** (Mel(f)=2595log10(1+f/700), lineal en bajas frecuencias y logarítmica en altas), (6) **Logaritmo** de la energía de cada filtro, y (7) **Transformada Coseno Discreta (DCT)** (sin inversa, por lo que no reconstruye el audio original). Se descarta el coeficiente C0 (solo energía promedio) y se conservan C1**a** C12**o** C13, más sus derivadas **Delta** (velocidad) y **Delta-Delta** (aceleración), construyendo por ejemplo un vector final de 80**características** por audio al aplicar estadísticos y descriptores espectrales.

#### **(c) Tabla resumen: Pasos y fórmulas clave de la Unidad 1**

| Descriptor | Qué mide | Pasos o fórmula clave | Salida típica en clase   |
| :---- | :---- | :---- | :---- |
| **Momentos de Hu** *(Cl. 1, 11\)* | Forma invariante | mpq→μpq→ηpq\=(μpq)/(μ00^(1+(p+q)/2))→Huk | Hu2\=0.020736 (log 1.6832) |
| **GLCM** *(Cl. 1, 11\)* | Textura | Definir (θ,d=1)→ simétrica →÷ total →ASM,√(ASM),Contraste | 6 características (N-S y O-E) |
| **HOG** *(Cl. 1\)* | Forma/Bordes | Normalizar →64×128→ gradientes 1×3,3×1→ celdas 8×8→ bloques 4 celdas | Vector de 3,780 valores |
| **MFCC** *(Cl. 1, 11\)* | Envolvente perceptual audio | Preénfasis → Framing → Hamming → FFT → Banco Mel →log→ DCT | Coefs. 1–13 (+Δ,ΔΔ) |

#### **(d) Errores comunes y puntos de examen**

> * En **GLCM**, olvidar sumar la transpuesta o **olvidar normalizar** entre el conteo total antes de calcular ASM, energía y contraste.  
> * En **Momentos Geométricos**, recordar que μ10\=μ01\=0 siempre, y que los **momentos normalizados** son invariantes a escala y traslación, pero **aún varían con la rotación** (solo Hu es invariante a rotación).  
> * En **MFCC**, confundir el orden exacto de los 7 pasos (en el primer examen fue pregunta directa) o creer que con los MFCC se puede reconstruir el audio original (la DCT usada aquí no tiene inversa para volver al audio).

### ---

**Unidad 2: Selección de Características y Reducción de Dimensionalidad**

*(Clases 2, 3, 4, 5 y 11\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Tras extraer miles de características (como los 3,780 valores de HOG), aparece la **maldición de la dimensionalidad**: los datos se vuelven dispersos, crece el costo computacional, aumenta el riesgo de sobreajuste, las distancias pierden sentido, se degrada el rendimiento y es imposible visualizar. Esta unidad resuelve ese problema por dos vías: **seleccionar** un subconjunto de las variables originales o **proyectar** todas hacia un espacio nuevo de menor dimensión.

#### **(b) Conceptos clave**

> * **Selección de Características: Filtrado, Wrapper y Embebido** *(Clases 2 y 11\)*:  
  * *Filtrado:* evalúa características **antes** de entrenar el modelo usando criterios estadísticos independientes (ej. correlación de Pearson).  
  * *Wrapper:* evalúa subconjuntos usando el desempeño real del clasificador **después** de entrenarlo. *Ejemplos numéricos de Clase 2 con variables A, B, C, D:* en **Forward Selection** se arranca vacío, gana B (70%), se prueba B+A, B+C, B+D (gana B+A), luego B+A+C (80%), pero B+A+C+D empeora 1% y se detiene (orden: B, A, C); en **Backward Selection** se entrena con todas (82%), al quitar A sube a 83%, al quitar D sube a 84%, y al intentar quitar B o C cae 24% y 14%, quedando B y C (84%); en **Exhaustive Feature Selection** se prueban todas las combinaciones (gana B+C con 84%), garantizando el óptimo global pero volviéndose inviable desde más de 15 o 20 características.  
  * *Embebido:* selecciona **durante** el entrenamiento dentro del mismo algoritmo (ej. **norma L1 / Lasso**, que manda pesos irrelevantes a 0, o **árboles de decisión**, que normalizan importancias y filtran por umbral como \>0.5).  
  * *Analogía:* elegir qué materias llevar a un examen por su índice en el temario (filtrado), probando combinaciones en simulacros reales (wrapper), o dejando que el propio método descarte temas mientras estudias (embebido).  
> * **PCA (Análisis de Componentes Principales) y SVD** *(Clases 2, 3, 5 y 11\)*: Técnica **no supervisada** que transforma variables posiblemente correlacionadas en nuevas variables **ortogonales y no correlacionadas** (combinaciones lineales llamadas componentes principales), ordenadas por la cantidad de **varianza** que capturan. *Analogía:* tomarle una foto a un objeto 3D desde el ángulo exacto donde su sombra se ve más estirada y muestra mejor su silueta. *Detalle técnico y casos reales:* el número total de vectores propios que arroja PCA es siempre igual al **número de características originales** (D); la proyección es Z=X\_cW de tamaño N×K. Como calcular la matriz de covarianza explícita es costoso y exige matriz cuadrada, en cómputo se usa **SVD** (Xc\=UΣVT), donde los vectores propios son VT y los valores propios se obtienen elevando los valores singulares **al cuadrado** (σi2). *Criterios para elegir* K*:* **Regla del codo**, **umbral de varianza** (ej. 90–95%) y **Criterio de Kaiser** (λ\>1, aporta más información que una variable estandarizada original).  
  * *Casos reales vistos (Clases 3 y 5):* En **Iris** (4 características), PC1 explica 92.46% y PC2 5.31% (acumulado 97.7%). En **Wine** (178 observaciones, 13 características químicas con escalas muy distintas), sin estandarizar el PC1 concentra el 99.809% de la varianza artificialmente por escala, mientras que estandarizado Kaiser y el codo eligen 3 componentes, 90% requiere 8 y 95% requiere 10\. En **Eigenfaces** (400 imágenes de 64×64), las primeras componentes capturan la geometría general del rostro y las últimas solo detalles finos o "estática", reconstruyendo rostros nítidos entre 100 y 300 componentes (recordando volver a sumar la media centrada al reconstruir).  
> * **LDA (Análisis Discriminante Lineal) como reducción de dimensionalidad** *(Clases 4 y 11\)*: Método **supervisado** que proyecta los datos hacia los ejes que maximizan la **separabilidad entre clases** (cociente entre dispersión entre clases SB y dispersión intraclase SW). Hace **tres supuestos fuertes**: distribución gaussiana, matriz de covarianza igual para todas las clases y separabilidad lineal. Su número máximo de dimensiones está limitado por el número de clases o características. En el ejercicio 35 del examen (Clase 11), resolviendo SW−1S\_Bw=λw se obtuvo λ1\=7.74 y el vector propio w=(2.34,1)T. Se mencionaron además **t-SNE** (visualización) y **Kernel PCA** (lleva a mayor dimensión vía kernel antes de aplicar PCA).

#### **(c) Comparación PCA vs. LDA**

| Criterio | PCA *(Clases 2, 3, 5, 11\)* | LDA *(Clases 4, 11\)*   |
| :---- | :---- | :---- |
| **Tipo** | No supervisado (sin etiquetas) | Supervisado (requiere etiquetas) |
| **Objetivo** | Maximizar la **varianza** de los datos | Maximizar la **separabilidad** entre clases |
| **Sensibilidad** | Muy sensible a la escala (exige **estandarizar** , no solo centrar) | Asume gaussiana, misma Σ y separabilidad lineal |

#### **(d) Errores comunes y puntos de examen**

> * **Confundir centrar con estandarizar:** centrar es solo restar la media (x−xˉ); estandarizar es restar la media y dividir entre la desviación estándar ((x−xˉ)/(σ)). Si no se estandariza en datasets heterogéneos como *Wine*, una sola variable de gran magnitud secuestra la primera componente.  
> * **Criterio de Kaiser:** se eligen componentes con **valor propio** λ\>1, NO las que explican más de 0.1% o 1% de la varianza (error cometido por un alumno en la Clase 5 y corregido por el profesor).  
> * **Valores singulares en SVD:** en SVD los valores de Σ deben **elevarse al cuadrado** para equivaler a los eigenvalores λ de la matriz de covarianza.  
> * **PCA vs. separación de clases:** tener alta varianza en PCA **no garantiza** separabilidad de clases porque no usa etiquetas.

### ---

**Unidad 3: Evaluación de Modelos, Validación y Fallas en Producción**

*(Clases 4, 6 y 11\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Construir un modelo es solo el 50% del trabajo; el resto es evaluarlo correctamente para asegurar que **generalice** a datos nunca vistos y no caiga en falsa confianza. Esta unidad dota al curso de las métricas y protocolos de validación que se exigirán en todos los clasificadores y prácticas siguientes.

#### **(b) Conceptos clave**

> * **Matriz de Confusión y Métricas Derivadas** *(Clases 4, 6 y 11\)*: Tabla con clases reales en filas y predicciones en columnas (diagonal \= aciertos **TP** y **TN**; fuera de diagonal \= errores **FP** o falsa alarma de incendio, y **FN** o incendio no detectado). *Ejemplo crítico de Clase 4:* en 1,000 pacientes (950 sanos y 50 con cáncer), un modelo que dice siempre "sano" logra 95%**de exactitud**, pero tiene 0% de *recall* (deja morir a los 50 enfermos). En el ejemplo de correos *spam*, se obtuvo 90% de accuracy y 85.7% en precisión, recall y F1.  
> * **Curva ROC y AUC** *(Clases 4, 6 y 11\)*: Para modelos que entregan probabilidades continuas, evalúa el desempeño moviendo el umbral de decisión (desde 0.1 hasta 1.0). Grafica **Eje X \= FPR** (1−Especificidad) contra **Eje Y \= TPR** (Sensibilidad / Recall). El **AUC** (área bajo la curva) mide la capacidad discriminativa: 1 perfecto, 0.9**–** 1 excelente, 0.7**–** 0.9 bueno, 0.5**–** 0.7 regular, 0.5 aleatorio (moneda al aire) y \<0.5 peor que el azar (conviene invertir la predicción).  
> * **Underfitting (Alto Sesgo) vs. Overfitting (Alta Varianza)** *(Clases 4 y 18\)*: En *underfitting*, el error es alto tanto en entrenamiento como en validación (faltó complejidad, características o entrenamiento). En *overfitting*, la exactitud de entrenamiento es muy alta (ej. 96–100%) pero cae fuerte en validación/prueba porque memorizó ruido (se corrige con más datos, regularización, *dropout* o parada temprana).  
> * **Estrategias de Validación** *(Clases 4 y 11\)*:  
  * **Hold-out:** divide en **3 conjuntos**: entrenamiento (60–80%), validación (10–20% para ajustar hiperparámetros) y prueba (solo para evaluación final).  
  * **K-Fold Cross-Validation:** separa primero el conjunto de **prueba** (que NO se toca durante las iteraciones), y divide el entrenamiento en K particiones iguales (ej. K=5,9,11), entrenando K veces dejando un *fold* distinto para validación en cada iteración.  
  * **Stratified K-Fold:** mantiene en cada *fold* la proporción original de clases cuando hay **datos desbalanceados** (como fraudes bancarios 0.1%, cáncer 1–5%, intrusión de red 0.5%).  
> * **Data Leakage (Fuga de Datos) y Data Drift** *(Clases 4 y 11\)*: La **fuga de datos** ocurre cuando información de validación o prueba contamina el entrenamiento, produciendo métricas artificialmente optimistas: fuga **temporal** (usar futuro para predecir pasado), fuga de **procesamiento** (calcular PCA o normalización usando estadísticas de validación/test) y fuga del **target**. El **Data Drift** ocurre cuando la distribución estadística de los datos en producción cambia respecto al entrenamiento (puede ser **abrupto**, **gradual** o **incremental**); se detecta monitoreando estadísticas en producción y se corrige reentrenando con una ventana de datos actualizada.

#### **(c) Fórmulas de métricas de evaluación *(Clases 4, 6 y 11\)***

| Métrica | Fórmula | Qué responde   |
| :---- | :---- | :---- |
| **Exactitud (Accuracy)** | (TP+TN)/(TP+TN+FP+FN) | Porcentaje global de aciertos. |
| **Precisión** | (TP)/(TP+FP) | De los que predije positivos, ¿cuántos sí lo eran? |
| **Recall / Sensibilidad (TPR)** | (TP)/(TP+FN) | De todos los positivos reales, ¿cuántos logré capturar? |
| **Especificidad** | (TN)/(TN+FP) | De todos los negativos reales, ¿cuántos identifiqué? |
| **F1-Score** | Media armónica de Precisión y Recall | Castiga extremos: si P=1 y R=0, media aritmética \=0.5, pero F1\=0. |
| **Exactitud Balanceada** | (Sensibilidad+Especificidad)/(2) | Promedio equilibrado por clase. |

#### **(d) Errores comunes y puntos de examen**

> * **Confundir los ejes de la curva ROC:** en el examen (pregunta 18, Clase 11\) se aclaró que eje X es **FPR** (1−especificidad) y eje Y es **TPR** (sensibilidad/recall), nunca 1−sensibilidad ni *recall* contra especificidad.  
> * **Usar Test dentro de K-Fold:** en validación cruzada, el conjunto de *test* **jamás se usa en cada iteración**; se reserva estrictamente hasta el final.  
> * **Aplicar PCA o estandarización sobre todo el dataset antes de dividir:** genera *fuga de procesamiento*.

### ---

**Unidad 4: Clasificadores Clásicos — Funciones de Decisión y Sistemas Ortogonales**

*(Clases 6 y 11\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Una vez reducidas y validadas las características, entramos a la etapa de **clasificación**: diseñar una función matemática que tome un vector x∈Rn y decida a qué clase pertenece. Introduce la geometría de fronteras e hiperplanos que fundamentará a LDA, Regresión Logística y SVM.

#### **(b) Conceptos clave**

> * **Espacio de Características vs. Espacio de Pesos, Clase, Región y Frontera** *(Clases 6 y 11\)*: En el **espacio de características**, cada punto es un **patrón** (ejemplo) y responde "¿dónde está cada patrón?"; en el **espacio de pesos**, cada punto/región representa **posibles clasificadores válidos** y responde "¿qué clasificador separa las clases?". Una **región de decisión** es el subespacio donde todo patrón se asigna a la misma clase, y una **frontera de decisión** es la superficie donde d(x)=0 o donde dos funciones discriminantes se igualan (gi(x)=gj(x)).  
> * **Funciones de Decisión (Lineales, Cuadráticas y No Lineales)** *(Clases 6 y 11\)*: Una función lineal d(x)=w^Tx+w0 traza un **hiperplano** en cualquier dimensión; clasifica por el **signo** (\>0 clase 1, \<0 clase 2\) y la distancia perpendicular del punto al hiperplano depende de d(x)/∥w∥. Una función cuadrática x^TAx+b^Tx+c añade flexibilidad con riesgo de sobreajuste.  
  * *Ejemplo 2 clases (Clase 6):* con w=(−3,0.75,1)T y x=(1,x1,x2)T, para el punto (4,3) resulta (−3)(1)+(0.75)(4)+(1)(3)=+3\>0 (clase ω1); para (0,0) da −3\<0 (clase ω2).  
> * **Clasificación Multiclase (OVR, OVO y Linear Machine) y Funciones Generalizadas** *(Clases 6 y 11\)*:  
  * **Uno contra el Resto (OVR):** una función por clase; asigna la clase i solo si di(x)\>0 y todas las demás \<0. *Ejercicio resuelto de Clase 6:* con D1\=−x1\+x2, D2\=x1\+x2−5 y D3\=−x2\+1, el punto (6,5) da (−1,+6,−4)→ω2; el punto (0,2) da (+2,−3,−1)→ω1; (6,4) da (−2,+5,−3)→ω2; en cambio, (2,6) da (+,+,−) cayendo en una **región indeterminada o ambigua**.  
  * **Uno contra Uno (OVO):** compara por pares dij(x)\>0 para todo j=i (ej. 1 vs 2, 1 vs 3, 1 vs 4); reduce regiones ambiguas pero aún puede tenerlas.  
  * **Linear Machine:** asigna la clase cuyo valor escalar gi(x) sea el **máximo** frente a todas las demás (gi(x)\>gj(x) ∀j=i), eliminando las regiones indeterminadas.  
  * **Funciones Generalizadas:** combinan salidas de distintos clasificadores fi ponderadas por pesos wi (antecedente directo de los **ensambles**).  
> * **Sistemas de Funciones Ortogonales** *(Clase 6\)*: Descomponen una función de decisión compleja no lineal en una suma ponderada de polinomios sencillos e independientes (sin redundancia y numéricamente estables). Sus dominios válidos son críticos: **Legendre** en \[−1,1\] (formas/intensidad en imágenes), **Laguerre** en \[0,∞) y **Hermite** en (−∞,∞) (audio/voz y distribuciones normales).

#### **(c) Tabla comparativa: Polinomios Ortogonales y Estrategias Multiclase**

| Sistema Ortogonal *(Clase 6\)* | Dominio válido | Aplicación principal   |
| :---- | :---- | :---- |
| **Legendre** | \[−1,1\] | Formas geométricas normalizadas e intensidad en imágenes. |
| **Laguerre** | \[0,∞) | Patrones no negativos en ese dominio. |
| **Hermite** | (−∞,∞) | Voz/audio y datos con distribución normal. |

#### **(d) Errores comunes y puntos de examen**

> * En **OVR**, creer que si dos funciones dan negativo ya es ambiguo: solo es **región indeterminada** cuando hay más de una función positiva o ninguna positiva; la regla válida exige **exactamente una positiva y el resto negativas**.  
> * Recordar que en una **función discriminante general** (Linear Machine), un patrón se clasifica en la clase cuya función sea la **mayor**, no donde valga 0 (donde vale 0 o donde gi\=gj es la **frontera de decisión**).

### ---

**Unidad 5: Aprendizaje No Supervisado (Clustering) y Métricas Internas**

*(Clases 7, 8, 9, 11 y 12\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Cuando no existen etiquetas previas en los datos, ya no podemos entrenar funciones de decisión supervisadas: debemos descubrir la estructura intrínseca agrupando observaciones similares en **clusters** (cohesión intracluster alta y separación intercluster alta) y evaluar esos grupos sin etiquetas mediante métricas internas. Además, el **Segundo Examen Parcial** inicia oficialmente a partir de **DBSCAN** dentro de este módulo.

#### **(b) Conceptos clave**

> * **Métricas de Distancia y Similitud** *(Clase 7\)*: La distancia de **Minkowski** generaliza: con p=1 es **Manhattan** (diferencias absolutas), con p=2 es **Euclidiana**, con p→∞ es **Chebyshev**. La distancia de **Mahalanobis** mide qué tan cerca está un punto de una *distribución* tomando en cuenta su **matriz de covarianza** (correlaciones entre variables). Otras medidas: similitud **coseno** (ángulo), **Pearson** (correlación lineal) y **Jaccard** (conjuntos binarios).  
> * **K-Means y K-Means++** *(Clases 7, 9 y 11\)*: Agrupa datos en K**clusters fijos** buscando minimizar implícitamente la **inercia** (suma de distancias cuadradas de cada punto a su centroide). *Analogía:* ubicar K antenas en una ciudad, asignar cada casa a la antena más cercana, mover cada antena al centro promedio de sus casas y repetir hasta que no cambien. *K-Means++* mejora la inicialización eligiendo el primer centroide al azar y seleccionando los siguientes con probabilidad proporcional a su distancia al primer centroide, reduciendo iteraciones (en la Práctica 2 bajó el promedio de 7.3 a 4.3 iteraciones en sintéticos, y en **Wine** —178 obs, 13 var— logró un *Adjusted Rand Index* de ∼0.895–0.91). Si un cluster queda vacío, se reinicializa aleatoriamente. **Limitación mayor:** asume clusters **esféricos** isotrópicos, por lo que falla en fronteras no lineales (ej. medias lunas), y es sensible a escala y *outliers*.  
> * **LBG (Linde-Buzo-Gray)** *(Clases 7, 8 y 11\)*: Diseña un *codebook* de *codewords* para **cuantización vectorial**, buscando minimizar la **distorsión**. Arranca con un único centroide igual a la **media global** (inicialización muy estable) y aplica *splitting* añadiendo ±ϵ (ej. 0.1) y actualizando hasta cumplir tolerancia de distorsión, por lo que el tamaño del *codebook* siempre es **potencia de 2** (2,4,8,16…). Forma regiones de **Voronoi** y puede usarse como clasificador entrenando un *codebook* por clase.  
> * **ISODATA** *(Clases 7, 8, 9 y 11\)*: Evolución de K-Means basada en **heurísticas** (sin garantía matemática de óptimo) que puede **modificar dinámicamente el número de clusters** mediante tres operaciones: **eliminar** clusters con menos de nmin puntos, **dividir** un cluster en dos (±0.5σj sobre el eje de mayor desviación estándar) si σj\>σmax, y **fusionar** dos centroides (ponderados por su número de puntos) si su distancia es menor a dmin. *Ejemplo Práctica 2 (Clase 9):* iniciando con K=6 o con K=3 en datos sintéticos de 4 grupos, convergieron igualmente a 4 clusters con la misma inercia (2086). Sigue limitado a clusters esféricos.  
> * **Métricas Internas de Clustering** *(Clases 8 y 9\)*: Evalúan clusters sin etiquetas:  
  * **Índice de Dunn** (\[0,∞), **mayor es mejor**): (mindistancia entre clusters)/(maxdiámetro de un cluster). *Ejemplo Clase 8:* con grupos S1\={1,2,3},S2\={7,8},S3\={15,16,17}, la distancia mínima entre clusters es 4 (entre 3 y 7\) y el diámetro máximo es 12 (de 1 a 13? No, de 1 a 3 es 2, de 7 a 8 es 1, de 15 a 17 es 2 —en la transcripción dice diámetro máximo 12 dando 4/12=0.333 \[dudoso en audio por lectura del gráfico\]).  
  * **Índice de Davies-Bouldin (DBI)** (\[0,∞), **menor es mejor**): promedio del máximo Rij\=(si\+sj)/(dij) por cluster; en el ejemplo de Clase 8 dio 0.188.  
  * **Coeficiente de Silueta** (\[−1,1\], **cercano a** 1**es mejor**): s(i)=(b(i)−a(i))/(max(a(i),b(i))), donde a(i) es la distancia media a su propio cluster y b(i) la menor distancia media a otro cluster. *Ejemplo Clase 8:* para x=2 en S1, a=1, b=5.5? No, a=1 y s=(b−a)/max⟹ 0.818; para x=7 en S2, a=1, b=5 (media hacia S1 \= 5, hacia S3 \= 9\) ⟹ 0.8. Interpretación: \<0.25 sin estructura, 0.26–0.5 débil, 0.5–0.7 razonable, 0.71–1 excelente; negativo indica mala asignación.  
> * **DBSCAN** *(Clases 12 y 14\)*: Algoritmo no supervisado **basado en densidad** que agrupa regiones densas separadas por zonas poco densas, descubre automáticamente el número de clusters K, traza **fronteras no lineales arbitrarias** (círculos concéntricos, medias lunas) e **identifica outliers como ruido** en una sola pasada. Usa dos parámetros: ε (radio máximo de vecindad, estimado con el codo de la gráfica de K-distancias) y **MinPts** (mínimo de puntos en ese radio; heurística inicial entre d+1 y 2d, ej. para 2 características entre 3 y 4). Clasifica puntos en: **punto núcleo** (≥MinPts en su radio ε), **punto frontera** (\<MinPts pero dentro de ε de un núcleo), y **punto ruido** (ni núcleo ni frontera). **Limitaciones:** sensible a ε y MinPts, falla cuando hay **densidades variables** entre clusters, y es costoso con datos muy grandes o alta dimensionalidad.

#### **(c) Comparación de Algoritmos de Clustering**

| Algoritmo | Parámetro K | Forma de Frontera | Criterio / Qué optimiza | ¿Detecta ruido?   |
| :---- | :---- | :---- | :---- | :---- |
| **K-Means / \++** *(Cl. 7, 9\)* | Fijo de entrada | Esférica | Minimiza inercia | No |
| **LBG** *(Cl. 7, 8\)* | Potencias de 2 | Regiones Voronoi | Minimiza distorsión | No |
| **ISODATA** *(Cl. 7, 9\)* | Dinámico (divide, une, elimina) | Esférica | Heurísticas (σmax,dmin,nmin) | Elimina clusters chicos |
| **DBSCAN** *(Cl. 12\)* | Automático | **Arbitraria / No lineal** | Densidad (ε, MinPts) | **Sí (puntos ruido)** |

#### **(d) Errores comunes y puntos de examen**

> * **Inercia en ISODATA:** al reducir centroides (ej. de 6 a 4), la inercia puede **subir** (de 1902.79 a 2086.95); esto NO es un error, pues menos centroides implican distancias sumadas mayores.  
> * **Ruido en DBSCAN:** un punto rodeado de puntos de un cluster puede quedar como **ruido** si en su radio ε no queda encerrado ningún **punto núcleo**. Además, un punto etiquetado inicialmente como ruido sí puede cambiar a **punto frontera** durante la expansión de un núcleo.  
> * En el primer examen se preguntó explícitamente qué asume K-Means (**forma esférica isotrópica**), qué minimiza LBG (**distorsión**) y la diferencia K-Means vs. ISODATA.

### ---

**Unidad 6: Clasificadores Probabilísticos (Bayes, QDA, LDA, GNB) y Basados en Instancias (KNN)**

*(Clases 8, 11, 12, 13, 14 y 19\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Pasamos del agrupamiento sin etiquetas al aprendizaje **supervisado**, incorporando la probabilidad y teoría de decisión de Bayes (para considerar costos asimétricos de error) o la proximidad directa en memoria con KNN.

#### **(b) Conceptos clave**

> * **Teoría de Decisión Bayesiana y Riesgo Condicional** *(Clase 8\)*: Usa la **regla de Bayes** P(ωi∣x)=(p(x∣ωi)P(ωi))/(p(x)) eliminando la evidencia p(x) porque es igual para todas las clases. Incorpora una matriz de pérdida λij (simétrica 0/1 o **asimétrica**, ej. en cáncer donde un falso negativo cuesta más que un falso positivo) y elige la acción αi que **minimiza el riesgo esperado**. *Ejemplo numérico (Clase 8):* con P(ω1∣x)=0.7, P(ω2∣x)=0.3 y pérdida 0/1, R(α1)=0(0.7)+1(0.3)=0.3 y R(α2)=1(0.7)+0(0.3)=0.7⟹ se elige ω1.  
> * **Clasificadores Gaussianos de Bayes: QDA, LDA y GNB** *(Clases 8, 11, 12 y 13\)*: Para estimar la verosimilitud p(x∣ωi) se asume distribución **normal multivariada** y se aplica logaritmo natural, quedando la función discriminante en términos de tres componentes: **distancia de Mahalanobis**, ln∣Σi∣ y lnP(ωi). Según qué se asuma sobre la matriz de covarianza Σ surgen tres modelos:  
  * **QDA:** matriz Σk **diferente para cada clase** → fronteras cuadráticas.  
  * **LDA:** matriz Σ **compartida** por todas las clases → fronteras lineales.  
  * **Gaussian Naive Bayes (GNB):** matriz **diagonal** (solo varianzas) asumiendo **independencia condicional** entre características.  
  * *Naive Bayes Discreto y Suavizado de Laplace (Clases 8 y 12):* en conteo de palabras (*spam* vs *no spam* en 8 correos), si una palabra no aparece en una clase (0), anula todo el producto de probabilidades. Se corrige con **suavizado** sumando 1 / conteo total (ej. \+1/12) a **todas** las palabras en **ambas clases** para que la densidad siga sumando 1\.  
  * *Casos reales vistos (Clases 8 y 13):* En **Iris** (120 train / 30 test), GNB falla en 1 ejemplo y QDA alcanza 100%. En la **Práctica 3**: (1) segmentación por color RGB (etiquetado temporal con HSV para 4 imágenes \= 1,440,000 píxeles) mostró el desbalance del fondo (76%); al meter una imagen de prueba con una **papa** (clase no vista), QDA no tiene categoría "desconocido" y la clasificó como plátano/huevo por cercanía cromática; (2) en **Breast Cancer** (569 obs, 30 características, 212 malignas/357 benignas, split 80/20 estratificado \= 455/114, regularización 10−4 en QDA para invertibilidad), QDA y LDA empataron en 95.61% y GNB cayó a 92.98% porque ignora correlaciones entre variables.  
> * **KNN (K-Nearest Neighbors)** *(Clases 12, 14 y 19\)*: Algoritmo **supervisado, no paramétrico y basado en instancias ("perezoso")**: no tiene fase de entrenamiento, simplemente memoriza el dataset y en inferencia mide la distancia del nuevo punto a todos los ejemplos, ordena y asigna por voto mayoritario de los k vecinos más cercanos (también sirve para regresión e **imputación de datos faltantes**). *Efecto de* k*:* k muy pequeño (k=1) captura ruido y sobreajusta con fronteras irregulares; k muy grande (30,50,100) suaviza demasiado, subajusta y decae al azar (50%). *Práctica 4 (Clase 19):* un equipo obtuvo el pico en k=41 (y 81 atípico), pero reconoció que un k menor daría mayor estabilidad.

#### **(c) Comparación de los 3 Clasificadores Bayesianos Gaussianos *(Clases 8, 11, 12, 13\)***

| Clasificador | Supuesto sobre Σ | Frontera | Parámetros por estimar | Ventaja / Desventaja en clase   |
| :---- | :---- | :---- | :---- | :---- |
| **QDA** | Σk propia por clase | Cuadrática | μk,Σk,P(ωk) | Muy flexible con muchos datos (RGB), requiere regularizar diagonal (10−4) |
| **LDA** | Σ compartida | Lineal | μk,Σ,P(ωk) | Menos parámetros que QDA; rindió igual en *Breast Cancer* (95.61%) |
| **GNB** | Diagonal (independencia) | Cuadrática/eje-alineada | μkj,σkj2,P(ωk) | Funciona con pocas muestras (100); cae si hay correlación o variables irrelevantes |

#### **(d) Errores comunes y puntos de examen**

> * En el primer examen se preguntó explícitamente qué necesita la pseudoprobabilidad bayesiana gaussiana (**Mahalanobis,** ln∣Σ∣**y** P(ωi), NO matriz de correlación) y la diferencia de Σ entre QDA, LDA y GNB.  
> * En **suavizado de Laplace**, olvidar aplicarlo a **todas** las clases descompensa la distribución de probabilidad (debe sumar 1).  
> * En **KNN**, nunca quedarse con k=1 aunque dé el pico de exactitud en un experimento simple, porque sobreajusta al ruido; además, al ser basado en distancias, es **obligatorio normalizar** las características y es lento en predicción.

### ---

**Unidad 7: Regresión Logística y Máquinas de Soporte Vectorial (SVM)**

*(Clases 14, 16 y 19\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Frente a KNN (lento en inferencia y sin parámetros) y los modelos generativos bayesianos (que asumen normalidad), la **Regresión Logística** aprende directamente una frontera lineal probabilística rápida y altamente interpretable ("el caballo de batalla de la industria"), mientras que **SVM** busca la frontera lineal óptima maximizando el margen e introduce el truco del kernel para problemas no linealmente separables.

#### **(b) Conceptos clave**

> * **Regresión Logística, Función Sigmoide y Entropía Cruzada Binaria** *(Clases 14 y 19\)*: Modela la probabilidad de pertenecer a la clase 1 pasando la combinación lineal z=θ^Tx por la función **sigmoide**: σ(z)=(1)/(1+e−z)∈(0,1). En escala logarítmica (*log-odds* ln(p)/(1−p)), el comportamiento es lineal. **Regla clave de implementación:** siempre añadir x0\=1 **al inicio** del vector de características para multiplicar al sesgo θ0. No se usa error cuadrático medio porque con la sigmoide se vuelve **no convexo**; se usa **Entropía Cruzada Binaria (BCE)**, que es **convexa** (garantiza mínimo global): J(θ)=−(1)/(m)∑\[ylny^+(1−y)ln(1−y^)\]. Al derivarla con regla de la cadena, el gradiente se simplifica a (1)/(m)∑(y^−y)x. Se entrena con tasas α≈0.1–0.5 mediante lote completo (*batch*), minilotes o descenso estocástico (SGD). Es un modelo de **caja blanca** (interpretable mediante los pesos θ) frente a redes neuronales de caja negra. Para multiclase usa **OVR** o **Softmax** (entropía cruzada multiclase).  
> * **Regularización L1 (Lasso) vs. L2 (Ridge) y Pesado por Clase** *(Clases 14 y 19\)*: Sin regularización, las magnitudes de θ crecen sin control (en datasets reales llegan a ±25,000, 50,000, 100,000 o 1,000,000), disparando el costo de memoria y cómputo en producción (ej. 18 millones de inferencias al día) y dificultando la interpretación.  
  * **L1 (Lasso):** añade (λ)/(m)∑∣θj∣ (gradiente (λ)/(m)signo(θj)); tiene la propiedad de **mandar exactamente a cero** los pesos de características irrelevantes (si λ es muy grande anula casi todo).  
  * **L2 (Ridge):** añade (λ)/(2m)∑θj2 (gradiente (λ)/(m)θj); **no hace cero** los pesos, los **acota en valores pequeños y los estabiliza rápidamente** a través de las épocas (alrededor de ∼15 épocas en la Práctica 4).  
  * **Pesado por Clase ( Class Weighting ):** ante desbalanceo, asigna pesos wk\=(m)/(K⋅mk) en la función de costo. *Ejemplo numérico Clase 14:* con 1,000 datos (950 clase 0 y 50 clase 1), w0\=(1000)/(2⋅950)=0.526 y w1\=(1000)/(2⋅50)=10 (el error en la clase minoritaria pesa ∼19–20 veces más).  
> * **SVM (Máquinas de Soporte Vectorial)** *(Repaso en Clase 16\)*: Busca el hiperplano que separa las clases **maximizando el margen** (distancia entre los **vectores de soporte**). Su versión simple asume separabilidad lineal; para datos no separables usa dos herramientas: (1) **variables de holgura** (dar tolerancia explícita a ciertos errores) y (2) **truco del kernel** (proyectar implícitamente a mayor dimensión donde sí sean linealmente separables). Multiclase aplica OVO u OVR.

#### **(c) Comparación L1 vs. L2 y Regresión Logística vs. Redes**

| Técnica / Modelo | Comportamiento de pesos θ | Estabilidad e interpretabilidad   |
| :---- | :---- | :---- |
| **Sin Regularización** *(Cl. 14, 19\)* | Crecen sin control (±50,000 a 1,000,000) | Alto costo en inferencia masiva; difícil de interpretar |
| **L1 (Lasso)** *(Cl. 14, 19\)* | Manda a **cero** variables irrelevantes | Sigue variando entre épocas; selecciona características |
| **L2 (Ridge)** *(Cl. 14, 19\)* | Penaliza haciéndolos **pequeños** (no cero) | Se estabiliza rápido (\~15 épocas) y facilita interpretar |

#### **(d) Errores comunes y puntos de examen**

> * **Dónde se aplica el pesado por clase (advertencia explícita "ojo" del profesor en Clase 19):** se aplica **estrictamente sobre la clase**, **NUNCA sobre las características/variables** ni sobre ejemplos aislados (error de un alumno al exponer).  
> * **Signo de los pesos** θ**en Regresión Logística:** un peso negativo **no significa que la variable importe menos**; los pesos positivos empujan hacia una clase y los negativos hacia la otra, operando juntos como combinación lineal.  
> * **Agregar** x0\=1**al final:** debe ir siempre **al inicio** para alinear θ0 con x0.  
> * **Lote completo en Regresión Logística:** funciona sin caer en mínimos locales porque la BCE es **convexa**.

### ---

**Unidad 8: Árboles de Decisión y Métodos de Ensamble**

*(Clases 16, 17, 18 y 21\)*

#### **(a) Qué problema resuelve y cómo se conecta**

La regresión logística solo traza fronteras lineales y SVM con kernel es poco interpretable. Los **árboles de decisión** dividen el espacio con reglas "si-entonces" formando **regiones hiperrectangulares** altamente interpretables y sin exigir normalización ni codificación de variables categóricas. Como un solo árbol es inestable y tiende a sobreajustar, los **ensambles** combinan muchos árboles débiles para lograr modelos mucho más precisos y generalizables.

#### **(b) Conceptos clave**

> * **Árboles CART, Impureza (Entropía y Gini) y Umbrales** *(Clases 16 y 21\)*: Algoritmo **voraz** con nodo raíz, nodos internos, hojas y ramas. En cada nodo evalúa todas las características y umbrales posibles (para numéricas ordena y prueba puntos medios (xi\+xi+1)/2, ej. 15,20,22,27→t1\=17.5,t2\=21; para categóricas prueba divisiones binarias directamente). Usa dos métricas de impureza (donde 0 es puro):  
  * **Entropía** ( en 2 clases): −∑p\_ilog2(pi).  
  * **Índice Gini** (\[0,0.5\] en 2 clases): 1−∑pi2. *Ejemplos de Clase 16:* en un nodo con 7 de clase A y 3 de clase B (0.7 y 0.3), Entropía \=0.881 y Gini \=1−(0.72\+0.32)=0.420 (alta impureza). En la tabla edad/ingresos (5 casos, umbral edad ≤35), izquierdo (2 casos: 1/2,1/2) da Gini \=0.5, derecho (3 casos: 1/3,2/3) da Gini \=0.444, y el Gini ponderado es (2)/(5)(0.5)+(3)/(5)(0.444)=0.466. En el ejemplo de enfermedad (8 casos: 4 sí, 4 no), la raíz parte en 0.5, y al empatar fiebre/tos/dolor de cabeza (0.375 en hijos), elige la **primera evaluada** (fiebre).  
> * **Sobreajuste, Pre-poda, Post-poda (** Cost-Complexity**) y Pesado por Clase** *(Clase 16\)*: Un árbol sin límite llega a hojas de 1 ejemplo (100% en train, caída fuerte en test). Se controla con **pre-poda** (max\_depth, mínimo de muestras por nodo, mínimo de muestras por hoja, mínimo decaimiento de impureza) o **post-poda** usando αcrítico\=(R(t)−R(Tt))/(∣Tt∣−1). *Ejemplo numérico de poda (Clase 16):* de 40 ejemplos totales, el subárbol Tt tiene Hoja 1 (8 A, 2 B → error 0.2) y Hoja 2 (7 A, 3 B → error 0.3), dando R(Tt)=(10)/(40)(0.2)+(10)/(40)(0.3)=0.125; colapsado en el nodo t (15 A, 5 B) falla en 5/40=0.125=R(t)⟹αt\=(0.125−0.125)/(2−1)=0\<αglobal\=0.1, por lo que **se poda**. Con **pesado por clase** en un nodo de 90 A (peso 1\) y 10 B (peso 10), las proporciones ponderadas pasan de 0.9/0.1 a 90/190 vs 100/190.  
> * **Ensambles: Bagging (Random Forest), Stacking y Boosting (Gradient Boosting)** *(Clases 16, 17 y 18\)*:  
  * **Bagging / Random Forest (paralelo):** entrena muchos árboles independientes (sin podar) con dos fuentes de diversidad: **Bootstrap** (muestreo aleatorio uniforme **con reemplazo** de tamaño N, que deja en cada árbol 63.2% de muestras dentro y 36.8%**fuera**, llamadas **Out-of-Bag / OOB**, pues limn→∞(1−1/n)n\=e−1≈0.368) y **selección aleatoria de un subconjunto de características** en cada división. Aumenta la varianza de cada árbol débil pero al promediar votos **cancela los errores y reduce el sesgo/sobreajuste** (ej. clase 0 pasa de 0.84 en CART a 0.95 en Random Forest con 40 árboles, accuracy de 0.91 a 0.95).  
  * **Stacking:** dos niveles; el nivel 0 entrena modelos distintos (ej. logística, SVM, GNB) y sus predicciones alimentan a un **metamodelo** en nivel 1 que aprende en quién confiar más.  
  * **Boosting / Gradient Boosting (secuencial):** cada modelo nuevo intenta corregir los errores del anterior. AdaBoost repondera ejemplos; **Gradient Boosting** optimiza en el **espacio de funciones** (no de pesos del árbol) ajustando cada árbol nuevo a las **pseudo-residuales** (gradiente negativo de cualquier función de pérdida diferenciable) mediante Fm(x)=Fm−1(x)+ηγjm. **XGBoost** añade paralelización y regularización para acelerar su lentitud secuencial. *Ejemplo numérico binario (Clase 17):* comprar producto según edad (3 sí, 3 no): inicialización F0\=ln(3/3)=0⟹p0\=0.5, residuos ±0.5; árbol divide en edad \<32; gamas por hoja γ=(∑residuos)/(∑p(1−p))=−2 y \+2; con η=0.5, F1\=0+0.5(±2)=±1⟹σ(±1) mueve las probabilidades a 0.27**y** 0.73, reduciendo residuos a ±0.27. Para **multiclase** (ej. gato, perro, caballo), entrena K secuencias en paralelo con *One-Hot* y combina al final con **Softmax**. *Limitación crítica:* domina datos tabulares pero **falla en datos espaciales (imágenes) y temporales/secuenciales (audio, series de tiempo)**, y es mucho más lento (en Breast Cancer: Logística 35 s, Árbol 2 s, RF 134 s, Gradient Boosting 1300 s).

#### **(c) Comparación de los 3 Métodos de Ensamble *(Clases 17 y 18\)***

| Método | Arquitectura | Muestreo / Datos | Qué mejora principalmente   |
| :---- | :---- | :---- | :---- |
| **Bagging (Random Forest)** | Paralela, voto por mayoría | Bootstrap con reemplazo (63.2%/36.8% OOB) \+ m características | Reduce varianza de árboles sin podar |
| **Stacking** | Dos niveles (nivel 0 \+ metamodelo nivel 1\) | Modelos base heterogéneos | Aprende a ponderar qué modelo acierta según el dato |
| **Boosting (Gradient Boosting)** | Secuencial aditiva | Pseudo-residuales (−∇L) | Corrige errores sucesivos; alta precisión tabular |

#### **(d) Errores comunes y puntos de examen**

> * **Tipo de pregunta confirmada para el segundo parcial (Clase 21):** en la última tarea pidió calcular a mano el **Gini del nodo raíz y dos nodos internos**, determinar qué clase predice cada hoja y listar qué ejemplos caen en cada hoja.  
> * **Gini ponderado:** no olvidar multiplicar el Gini de cada hijo por su proporción de muestras respecto al nodo padre (Nizq/N y Nder/N).  
> * **Gradient Boosting NO optimiza pesos internos con gradiente:** el gradiente se usa en el **espacio de funciones** para calcular los pseudo-residuales, no para actualizar parámetros internos de los árboles.  
> * **Dependencias que NO modela Gradient Boosting** (preguntado explícitamente al grupo en Clase 18): datos **secuenciales/temporales** (audio, series) y datos **espaciales** (píxeles de imágenes).

### ---

**Unidad 9: Redes Neuronales Artificiales, Convolucionales (CNN) y Autoencoders**

*(Clases 18, 20 y 21\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Como los métodos tabulares anteriores requieren características extraídas manualmente y no capturan relaciones espaciales ni secuenciales, surgen las **redes neuronales profundas**: capaces de aproximar funciones no lineales arbitrarias y **extraer automáticamente sus propias características** desde datos crudos (radiografías, imágenes, audio).

#### **(b) Conceptos clave**

> * **Perceptrón, MLP, Activaciones No Lineales y Entrenamiento** *(Clases 18 y 21\)*: El **perceptrón** (Rosenblatt 1957/1958) calcula ϕ(w^Tx+b); puede resolver compuertas lineales como AND y OR, pero en 1969 se demostró que **no puede resolver XOR** porque no es linealmente separable. Para resolverlo nace el **Perceptrón Multicapa (MLP)** (Teorema de Aproximación Universal), que requiere **capas ocultas \+ funciones de activación no lineales** (sin no linealidad, múltiples capas colapsan en una sola combinación lineal gigante). *Salidas según tarea:* **lineal** \+ MSE para regresión, **sigmoide** \+ BCE para clasificación binaria, y **Softmax** \+ entropía cruzada multiclase para multiclase. *Entrenamiento en 4 pasos:* (1) *Forward pass*, (2) cálculo de pérdida, (3) *Backward pass* (retropropagación por **regla de la cadena** reutilizando derivadas intermedias), y (4) actualización con optimizadores (**SGD, RMSProp, Adagrad, Adam**, η≈10−4) para superar puntos silla en funciones de pérdida no convexas. Cada **época** recorre todos los minilotes de tamaño B, barajando los datos entre épocas para no memorizar el orden.  
> * **Problemas de Redes Profundas y Regularización** *(Clase 18\)*: Apilar muchas capas (ej. 50–100 capas) mejora el desempeño pero causa:  
  * **Explosión del gradiente:** actualizaciones gigantes cerca de la entrada → se resuelve con **recorte de gradientes** (*gradient clipping*) y **Batch Normalization** (normaliza cada canal/característica sobre los ejemplos del lote).  
  * **Desvanecimiento del gradiente:** gradientes se vuelven casi cero al multiplicarse hacia atrás por usar activaciones **saturadas** (**sigmoide** o **tanh**, cuyas derivadas solo son grandes cerca de \[−2,2\]) → se resuelve con activaciones **no saturadas** (**ReLU, LeakyReLU, GELU, SiLU**) y **conexiones residuales**.  
  * **Sobreajuste en redes:** se combate con inicialización adecuada (normal/uniforme), L1/L2, **Early Stopping**, **Dropout** (apaga neuronas aleatoriamente), **Data Augmentation**, **Label Smoothing** y aprendizaje multitarea.  
> * **Redes Neuronales Convolucionales (CNN) y ResNet** *(Clase 20\)*: Una red densa falla con imágenes porque: (1) una imagen RGB de 224×224×3 exige 150,528 neuronas de entrada y más de 150**millones de parámetros** en las dos primeras capas, y (2) aplanar destruye la **vecindad espacial**. La **convolución** refleja una señal respecto al origen, la desplaza y multiplica (es **conmutativa**: I∗K=K∗I), a diferencia de la **correlación cruzada** (no refleja y el orden **sí** altera el resultado). En una CNN, los pesos aprendidos son los **coeficientes de los filtros ( kernels )** (ej. un filtro 3×3×3 para imagen 28×28×3 solo necesita 27**coeficientes**). *Hiperparámetros:* número de filtros (= mapas de características), **stride** (desplazamiento, ej. 2\) y **padding** (ceros en bordes). *Capas adicionales:* **Max Pooling** y **Average Pooling** (ninguno es universalmente mejor; depende del diseño), **Global Average Pooling** (promedia todo el mapa a 1 escalar antes de clasificar), **convolución transpuesta** (aumenta resolución en segmentación/generación) y **convolución** 1×1 (resume o cambia profundidad de mapas, ej. 8×8×3→8×8×1). **ResNet (2015)** sumó la entrada sin procesar a la salida procesada para evitar desvanecimiento/explosión del gradiente mediante **bloques básicos** (64 canales) y **bloques bottleneck** (256→64→256), logrando bajar el error en ImageNet de 7.4% (ResNet-34) a 5.7% (ResNet-152). Línea evolutiva: *LeNet (1998)* →*AlexNet (2012)* →*VGGNet / GoogLeNet* →*ResNet (2015)* →*MobileNet (2017)* →*EfficientNet* →*Vision Transformers (ViT)*.  
> * **Autoencoders, Data Augmentation y Transfer Learning** *(Clase 20\)*: Un **autoencoder** reconstruye su propia entrada pasando por un *Encoder*, un cuello de botella (**espacio latente** reducido, ej. 28×28×1→ vector de 10**valores**) y un *Decoder* (siempre **con pérdida**, a diferencia de WinRAR). Sirve para **detección de anomalías** (entrenado solo con transacciones normales, las anómalas arrojan error alto de reconstrucción), **eliminación de ruido ( denoising )**, compresión y recomendación. Cuando hay pocos datos (ej. 1,000–2,000 fotos de lunares de cáncer de piel), **Data Augmentation** transforma las imágenes existentes y **Transfer Learning** reutiliza los pesos de un modelo preentrenado en otra tarea masiva (100,000–1,000,000 de radiografías pulmonares), acelerando convergencia y evitando sobreajuste.

#### **(c) Resumen comparativo de arquitectura e ingeniería profunda**

| Problema en Red Profunda *(Clases 18, 20\)* | Causa principal | Soluciones vistas en clase   |
| :---- | :---- | :---- |
| **Falla en XOR / no linealidad** | Falta de capas ocultas o uso de activación lineal | MLP \+ activaciones no lineales |
| **Desvanecimiento del gradiente** | Multiplicación en cadena \+ sigmoide/tanh saturadas | ReLU, LeakyReLU, GELU, SiLU \+ **Conexiones residuales** |
| **Explosión del gradiente** | Tasas altas, entradas grandes, mucha profundidad | **Recorte de gradientes** \+ **Batch Normalization** |
| **Explosión de parámetros en imagen** | Capas densas aplanadas (224×224×3→\>150M) | Convoluciones (filtros compartidos 3×3×3=27) \+ Pooling |
| **Escasez de datos** | Sobreajuste en redes grandes | *Data Augmentation* \+ *Transfer Learning* |

#### **(d) Errores comunes y puntos de examen**

> * **Ejercicio anunciado en la última tarea (Clase 21):** diseñar a mano una red neuronal de **3 neuronas con función escalón unitario** para resolver una operación lógica no lineal.  
> * **Pesos en una CNN:** los pesos no ponderan características ya extraídas; los pesos **son los valores numéricos de los filtros** y filtros distintos no "aportan más o menos", sino que extraen **tipos distintos de información** (bordes, desenfoque, esquinas).  
> * **Convolución vs. Correlación Cruzada:** la convolución refleja y es **conmutativa**; la correlación cruzada no refleja y sí depende del orden.

### ---

**Unidad 10: Procesamiento de Lenguaje Natural (NLP), Modelos Secuenciales y Transformers**

*(Clases 20 y 21\)*

#### **(a) Qué problema resuelve y cómo se conecta**

Concluimos con el reconocimiento de patrones sintácticos/lenguaje. A diferencia de las imágenes, el lenguaje humano es **secuencial**: el orden importa (*"El perro mordió al hombre"* vs. *"El hombre mordió al perro"*). Esta unidad recorre la evolución desde modelos estadísticos discretos y redes recurrentes hasta la arquitectura agnóstica **Transformer**.

#### **(b) Conceptos clave**

> * **N-gramas, Representaciones Discretas y Gramática** *(Clase 20\)*: Los **N-gramas** predicen la siguiente palabra usando solo las n−1 anteriores (ej. *"me gusta aprender PLN"* → 3 bigramas, 2 trigramas; en el corpus del gato, tras *"el gato"* hay 67% *"come"* y el resto *"bebe"*, pero tras *"comer arroz"* da 0). Fallan por **explosión combinatoria** (con 1,000 palabras crece enormemente), **contexto corto** y **dispersión / probabilidad cero**. Las **representaciones discretas** incluyen **One-Hot Encoding**, **Bolsa de Palabras** (ignora orden) y **TF-IDF** (da peso alto a palabras raras en el corpus como *"felino"* \[0.479\] y bajo a comunes como *"el"*). Se distinguió **sintaxis** (estructura gramatical correcta, analizada con árboles de constituyentes y de dependencias en *parsing*) de **semántica** (sentido real) y la **ambigüedad** (*"Vi al hombre con el telescopio"*).  
> * **Embeddings, CBOW, Skip-gram, RNN y LSTM** *(Clases 20 y 21\)*: Los **embeddings** proyectan palabras a vectores densos continuos donde la cercanía refleja significado (*Word2Vec*, *GloVe*, *FastText*, frente a los **contextuales** donde *"banco"* cambia de vector según *"depositar dinero"* vs *"banco del parque"*). **CBOW** predice una palabra faltante a partir de su contexto; **Skip-gram** (más difícil) predice el contexto a partir de una sola palabra. Las **RNN** mantienen un estado oculto (memoria ht) combinando pasado y entrada actual xt, pero al encadenar capas densas con **tangente hiperbólica (saturada)** sufren **desvanecimiento del gradiente**, limitándose a 50**–** 100**palabras** y fallando en 1,000**–** 2,000**palabras**. Las celdas **LSTM** añaden una línea de estado superior casi limpia (similar a una **conexión residual**) y **tres compuertas** (**olvido**, **entrada** y **salida**). En arquitectura *Encoder-Decoder* comprimían la oración en un **vector de contexto** fijo (causando fallas gramaticales en traductores como Google Translate antiguo en textos largos), y su gran defecto es ser **estrictamente secuenciales y difíciles de paralelizar**.  
> * **Transformer, Codificación Posicional, Autoatención (** Q,K,V**), LayerNorm y RAG** *(Clase 21\)*: Propuesto en 2018 (*Attention Is All You Need*), es un modelo **agnóstico** (a diferencia de CNN/RNN de **alto sesgo inductivo**): convierte texto, parches de imagen o fragmentos de audio en **tokens** vectoriales y los procesa en **paralelo**.  
  * **Positional Encoding:** suma a cada *embedding* su posición original mediante funciones **seno y coseno** (alternando par/impar) o tablas entrenables.  
  * **Atención Multicabeza ("el corazón del Transformer"):** proyecta los tokens con capas lineales a **Queries (** Q, qué busco), **Keys (** K, qué ofrezco) y **Values (** V, contenido real), y en cada cabeza calcula el **producto punto escalado**: multiplica Q⋅K, divide entre la dimensionalidad de las K, aplica **Softmax** (pesos entre 0 y 1 que suman 1\) y multiplica por V; luego concatena las n cabezas y las pasa por una capa lineal que devuelve exactamente la dimensionalidad original.  
  * **Bloque Transformer:** Atención Multicabeza → suma residual \+ **Layer Normalization** (normaliza sobre dimensiones de **características**, distinto a *BatchNorm* que normaliza sobre ejemplos del lote) → **Feed-Forward** (Lineal → **GELU** → **Dropout** → Lineal → **Dropout**) → suma residual \+ **Layer Normalization**. Mantiene idéntica dimensionalidad de entrada y salida, permitiendo apilar bloques.  
  * **Tareas y Ecosistema:** Clasificación y **Generación autoregresiva** (anexa la salida predicha a la entrada y repite); **RAG ( Retrieval-Augmented Generation )** conecta una base de datos externa actualizada al Transformer para evitar alucinaciones sobre datos que no vio en entrenamiento (ej. horarios de la Facultad de Ingeniería). *Trade-off sesgo vs. datos:* entrenar desde cero una CNN (alto sesgo) requiere ∼1 millón de imágenes, mientras un Transformer requiere ∼300 millones (aunque con esos datos o vía *Transfer Learning* la supera). Derivados: **BERT, GPT, ViT** y **Segment Anything**.

#### **(c) Comparación de Arquitecturas Secuenciales / NLP *(Clases 20 y 21\)***

| Modelo | Paralelización | Contexto largo | Sesgo inductivo / Datos desde cero | Limitación principal   |
| :---- | :---- | :---- | :---- | :---- |
| **N-gramas** | No aplica (conteo) | Muy corto (n−1) | Basado en frecuencias del corpus | Explosión combinatoria y probabilidad cero |
| **RNN simple** | No (secuencial) | Corto (50–100 pal.) | Alto (asume secuencia) | Desvanecimiento del gradiente (tanh) |
| **LSTM** | No (secuencial) | Mejorado (3 compuertas) | Alto (asume secuencia) | Entrenamiento lento; cuello de botella en vector de contexto |
| **Transformer** | **Sí (total)** | **Muy largo (global)** | **Agnóstico** (∼300M imgs vs 1M CNN) | Alto costo matricial, necesidad de datos y baja explicabilidad |

#### **(d) Errores comunes y puntos de examen**

> * **TF-IDF:** un peso de 0 para *"felino"* en *"el perro come carne"* **NO** significa que el perro no sea un felino, sino simplemente que la palabra *"felino"* **no aparece** en ese documento.  
> * **Layer Normalization vs. Batch Normalization:** *LayerNorm* normaliza sobre la dimensión de **características**; *BatchNorm* normaliza sobre los **ejemplos** del lote.  
> * **GPT:** significa *Generative Pretrained Transformer*.

## ---

**3\. LO QUE MÁS PROBABLEMENTE VIENE EN EL FINAL**

**Nota importante sobre el alcance del próximo examen:** En las Clases 11, 12 y 21, el profesor confirmó que solo habrá **dos exámenes parciales** en el semestre (a veces referido en Clase 20 como "segundo examen final"), y que el **Segundo Examen (lunes 23 de noviembre)** evaluará **desde clasificadores de aprendizaje automático a partir de DBSCAN hasta Transformers** (ya no entra el temario del Primer Parcial). La lista siguiente prioriza los puntos con mayor evidencia directa para este cierre, incluyendo también los pilares evaluados previamente por si necesitas una visión integral de toda la materia:

> 1. **Cálculo manual de Índice Gini en Árboles de Decisión y clase de cada hoja**  
   * *Evidencia:* En la Clase 21 el profesor dejó la última tarea con este ejercicio exacto (calcular Gini en nodo raíz y nodos internos, y decir qué clase predice cada hoja y qué ejemplos caen en ella), tras haber afirmado minutos antes que los ejercicios del examen salen de lo visto en clase y tareas.  
> 2. **Diseño a mano de un Perceptrón Multicapa (3 neuronas, activación escalón unitario)**  
   * *Evidencia:* Es el segundo ejercicio explícito de la última tarea (Clase 21), conectando directamente con la demostración de Clase 18 de por qué una sola neurona no resuelve XOR y requiere capas ocultas.  
> 3. **DBSCAN: parámetros (** ε**, MinPts), clasificación de puntos (núcleo, frontera, ruido) y ventajas frente a K-Means**  
   * *Evidencia:* El profesor señaló explícitamente en Clases 12 y 21 que el segundo examen arranca desde DBSCAN; además, fue el primer ejercicio de la tarea dejada en la Clase 16 (graficar puntos y clasificar núcleo, frontera y ruido dado ε y MinPts).  
> 4. **Cálculo con Naive Bayes (discreto con suavizado de Laplace y gaussiano continuo)**  
   * *Evidencia:* En la Clase 16 dejó dos ejercicios completos de tarea (calcular a priori y verosimilitudes discretas por tabla, y medias/varianzas gaussianas continuas), además de insistir en Clase 12 en cómo aplicar el suavizado a todas las frecuencias para evitar ceros.  
> 5. **Regularización L1 (Lasso) vs. L2 (Ridge) y Regresión Logística (caja blanca,** x0\=1**, convexidad de BCE)**  
   * *Evidencia:* En la Clase 19 el profesor reabrió las gráficas de θ para dar una explicación magistral a todo el grupo (*"para que les quede más claro"*), contrastando sin regularización vs. L1 (manda a cero) vs. L2 (acota estable en \~15 épocas) y caja blanca vs. caja negra.  
> 6. **Regla estricta de Pesado por Clase ( Class Weighting )**  
   * *Evidencia:* Al cierre de la Clase 19 enfatizó con *"ojo"*: el peso se aplica **únicamente sobre las clases** (nunca sobre características ni ejemplos), y en Clase 14 resolvió el cálculo numérico (950/50→0.526 y 10).  
> 7. **Gradient Boosting vs. Random Forest (Bootstrap/OOB** 63.2%**/** 36.8%**, pseudo-residuales, limitaciones)**  
   * *Evidencia:* En Clases 17 y 18 repasó en vivo las diferencias entre Bagging (paralelo) y Boosting (secuencial en espacio de funciones), y preguntó directamente al grupo qué dos dependencias no modela Gradient Boosting (secuencial/temporal y espacial).  
> 8. **Redes Profundas: Desvanecimiento vs. Explosión del Gradiente y sus soluciones (ReLU/GELU, ResNet, BatchNorm)**  
   * *Evidencia:* Concepto repetido y conectado transversalmente en **tres clases consecutivas**: Clase 18 (teoría de activaciones saturadas vs. no saturadas y clipping), Clase 20 (bloques residuales de ResNet) y Clase 21 (falla de RNN con tanh y autopista de LSTM / LayerNorm).  
> 9. **CNNs (por qué fallan las redes densas en imágenes, Convolución vs. Correlación Cruzada) y Autoencoders (detección de anomalías)**  
   * *Evidencia:* En Clase 20 calculó el desbordamiento de parámetros (150,528 entradas y \>150M parámetros vs. 27 coeficientes de un filtro 3×3×3), distinguió la conmutatividad de la convolución y interrogó al grupo sobre la utilidad del cuello de botella de los autoencoders.  
> 10. **Transformers: por qué es agnóstico, Tokens, Positional Encoding, Autoatención (** Q,K,V**), LayerNorm y RAG**  
    * *Evidencia:* En Clase 21 dedicó la mayor parte de la última sesión teórica a este tema, pidiendo explícitamente *"pongan atención"* al explicar el producto punto escalado de Q,K,V (corazón del Transformer) y preguntando al grupo sobre GPT y RAG.  
> 11. **Si se evalúa el bloque clásico (Primer Parcial, Clase 11):** diferencias entre extracción y selección de características, 7 pasos de MFCCs, PCA vs. LDA, ejes de la curva ROC, K-Fold sin tocar Test, Data Drift/Leakage, distancia de Mahalanobis y cálculo a mano de Momentos de Hu, GLCM o LDA.

## ---

**4\. CONEXIONES CLAVE**

> 1. Detección \-\> captura mediciones crudas para \-\> Extracción de características  
> 2. Momentos de Hu \-\> garantizan invarianza geométrica frente a \-\> Traslación, escala y rotación  
> 3. GLCM normalizada \-\> cuantifica cambios probabilísticos de luminosidad para describir \-\> Textura de imágenes  
> 4. Descriptor HOG \-\> codifica orientaciones locales de gradientes para capturar \-\> Forma y bordes  
> 5. Banco de filtros Mel \-\> imita la percepción logarítmica del oído humano para construir \-\> Coeficientes MFCC  
> 6. Exceso de características extraídas \-\> provoca \-\> Maldición de la dimensionalidad  
> 7. Métodos Wrapper (Forward/Backward) \-\> evalúan subconjuntos mediante el desempeño real de \-\> Un clasificador entrenado  
> 8. PCA no supervisado \-\> proyecta hacia ejes ortogonales que maximizan \-\> Varianza de los datos  
> 9. Descomposición SVD \-\> evita calcular explícitamente la matriz de covarianza para acelerar \-\> PCA  
> 10. Estandarización previa \-\> evita que variables de gran magnitud dominen \-\> PCA y distancias  
> 11. LDA supervisado \-\> proyecta maximizando la separabilidad entre clases asumiendo \-\> Igual covarianza y gaussianidad  
> 12. Matriz de confusión \-\> desglosa TP, TN, FP y FN para calcular \-\> Precisión, Recall y F1  
> 13. Curva ROC \-\> evalúa TPR contra FPR al variar \-\> El umbral de decisión probabilístico  
> 14. Validación cruzada K-Fold \-\> rota particiones de validación dentro de entrenamiento reservando al final \-\> El conjunto de prueba  
> 15. Fuga de datos (*Data Leakage*) \-\> contamina el entrenamiento con información de validación/test generando \-\> Métricas falsamente optimistas  
> 16. *Data Drift* en producción \-\> desplaza la distribución estadística respecto al entrenamiento exigiendo \-\> Reentrenamiento periódico  
> 17. *Linear Machine* \-\> selecciona el máximo valor escalar entre discriminantes para eliminar \-\> Regiones ambiguas de OVR  
> 18. Sistemas ortogonales (Legendre, Laguerre, Hermite) \-\> descomponen fronteras complejas en \-\> Sumas ponderadas de polinomios simples  
> 19. K-Means++ \-\> pondera distancias desde el primer centroide para mejorar \-\> Inicialización de K-Means  
> 20. Algoritmo LBG \-\> divide centroides en potencias de dos para minimizar \-\> Distorsión de cuantización vectorial  
> 21. ISODATA \-\> añade división, fusión y eliminación heurística para ajustar dinámicamente \-\> Número de clusters  
> 22. Algoritmo DBSCAN \-\> agrupa regiones densas mediante ε y MinPts para detectar \-\> Clusters arbitrarios y ruido  
> 23. Distancia de Mahalanobis \-\> incorpora la matriz de covarianza dentro de \-\> Clasificadores Bayesianos Gaussianos  
> 24. Suavizado de Laplace \-\> suma una fracción positiva a todas las frecuencias para evitar \-\> Probabilidades cero en Naive Bayes  
> 25. Algoritmo KNN \-\> memoriza instancias sin entrenar para decidir por mayoría según \-\> Vecinos más cercanos  
> 26. Entropía Cruzada Binaria \-\> garantiza convexidad matemática para optimizar mediante gradiente \-\> Regresión Logística  
> 27. Regularización L1 (Lasso) \-\> manda coeficientes irrelevantes a cero mientras L2 (Ridge) \-\> Acota y estabiliza pesos  
> 28. Máquinas de Soporte Vectorial \-\> usan variables de holgura y truco del kernel para \-\> Maximizar el margen en datos no separables  
> 29. Árboles CART \-\> minimizan impureza Gini o entropía para dividir el espacio en \-\> Regiones hiperrectangulares  
> 30. Random Forest \-\> combina muestreo Bootstrap (63.2%/36.8% OOB) y selección aleatoria de variables para reducir \-\> Varianza y sobreajuste  
> 31. Gradient Boosting \-\> entrena árboles secuenciales sobre pseudo-residuales para corregir \-\> Errores de modelos previos  
> 32. Funciones no saturadas y conexiones residuales \-\> evitan la atenuación multiplicativa en backpropagation resolviendo \-\> Desvanecimiento del gradiente  
> 33. Capas convolucionales \-\> comparten filtros pequeños sobre vecindarios locales para preservar \-\> Estructura espacial en imágenes  
> 34. Autoencoders \-\> comprimen entradas hacia un espacio latente reducido para habilitar \-\> Detección de anomalías y limpieza de ruido  
> 35. Celdas LSTM \-\> incorporan tres compuertas y línea de estado superior para retener memoria en \-\> Secuencias largas  
> 36. Arquitectura Transformer \-\> sustituye la recurrencia mediante *Positional Encoding* y autoatención (Q,K,V) para procesar \-\> Secuencias arbitrarias en paralelo  
> 37. Enfoque RAG \-\> conecta bases de datos actualizadas al Transformer para prevenir \-\> Alucinaciones por falta de entrenamiento reciente

💡 *¿Quieres que armemos ejercicios tipo examen resueltos paso a paso para los tres cálculos clave del Segundo Parcial (DBSCAN con* ε*y MinPts, Índice Gini de un árbol ya construido y red de 3 neuronas con escalón unitario)?*

## **Anexo · Clases que no estaban en el cuaderno de NotebookLM**

*Resumen para estudiar de cada una, tomado de los apuntes por clase del sitio (decimo/RP/RP-Resumenes/).*  
*Las sesiones 1–3 del curso (Clase −2, −1 y 0\) son anteriores a tu inscripción y se reconstruyeron con las diapositivas del profesor.*

### **Clase −2 · Presentación del curso y conceptos básicos (lunes 17 ago 2026 (sesión 1 del curso))**

*Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.*

| Concepto | Para recordar   |
| :---- | :---- |
| Patrón | Objeto, proceso o evento descriptible y distinguible |
| Sistema | Patrón → mediciones → características → clasificador → clase |
| Estimación vs. RP | Continuo vs. discreto |
| 3 problemas | Representar, extraer/reducir, decidir |
| Maldición | Distancias casi iguales; sobreajuste; se reduce dimensión |
| Evaluación | Tareas 15 %, prácticas/examen 45 %, proyecto 40 % |

### **Clase −1 · Extracción de características I: estadísticas, ventanas e histograma (viernes 21 ago 2026 (sesión 2 del curso))**

*Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.*

| Concepto | Para recordar   |
| :---- | :---- |
| Se busca | Discriminabilidad, compacidad, robustez, bajo costo |
| Skewness | Signo \= hacia dónde va la cola |
| Curtosis | \> 0 colas pesadas; \< 0 ligeras |
| Ventanas | Con o sin traslape; concatenar, estadísticas de estadísticas, pooling |
| Histograma | Robusto y simple; pierde la posición |

### **Clase 0 · Momentos geométricos, Hu y textura con GLCM (lunes 24 ago 2026 (sesión 3 del curso))**

*Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.*  
**Entró en el primer parcial** Ejercicio 33: cadena de momentos hasta Hu (10 puntos). Ejercicio 34: GLCM norte-sur con ASM, energía y contraste (10 puntos).

| Concepto | Para recordar   |
| :---- | :---- |
| Espaciales | M00 área; centroide M10/M00, M01/M00 |
| Centrales | Quitan traslación; μ10 \= μ01 \= 0 |
| Normalizados | Quitan escala; i \+ j ≥ 2 |
| Hu | 7; quitan rotación; usar −signo·log₁₀ |
| GLCM | d y θ → contar → \+ transpuesta → ÷ total |
| Descriptores | Contraste, homogeneidad, ASM, energía, entropía, correlación |

### **Clase 10 · Primer Examen Parcial (lunes 28 sep 2026 (sesión 13 del curso))**

| Prioridad | Qué   |
| :---- | :---- |
| 1 | LDA completo a mano (15 pts, el de más peso) |
| 2 | GLCM: simétrica \+ normalizada antes de los descriptores |
| 3 | Cadena de momentos hasta Hu y logaritmo |
| 4 | Orden de MFCC; métricas y ROC (sensibilidad, especificidad, FPR) |

### **Clase 15 · Máquinas de vectores de soporte (SVM) (viernes 16 oct 2026 (sesión 18 del curso))**

*Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.*  
**Idea.** Hiperplano de margen máximo; solo los vectores de soporte (αᵢ \> 0\) lo definen. Restricción yᵢ(w·xᵢ \+ b) ≥ 1\.  
**Derivación (examen)** λ \= 2/(w·w) → M \= 2/‖w‖ → maximizar M ≡ min ½‖w‖². Lagrange: w \= Σ αᵢyᵢxᵢ y Σ αᵢyᵢ \= 0; la dual solo usa productos punto.

| Concepto | Para recordar   |
| :---- | :---- |
| Margen suave | ξᵢ; min ½‖w‖² \+ CΣξᵢ; C grande \= margen angosto, C chico \= ancho |
| Kernel | K \= φ(xᵢ)ᵀφ(xⱼ) sin calcular φ |
| Kernels | Lineal, polinomial (1 \+ xᵀx)ᵖ, RBF exp(−‖·‖²/2σ²), sigmoide tanh |
| Multiclase | Uno vs. resto o uno vs. uno |
| Ejemplos | Breast Cancer: gana lineal (0.982). German Credit: RBF engaña (todo "riesgo") |
| Desventajas | Lento con muchos datos, sensible al kernel, requiere escalar |

