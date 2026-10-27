% materia: Minería de Datos
% titulo: Clase 15 · Clasificación de diabetes y series de tiempo
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 22 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Primera mitad: exposiciones de la Práctica 3.4 (7 minutos por equipo). Segunda mitad: series de tiempo, ARIMA y qué modelo usar según el negocio. Las cifras varían entre equipos.

## 1. Práctica 3.4: clasificar diabetes
Aplicar clasificación supervisada (regresión logística, árboles, Random Forest, SVM, Naive Bayes, KNN) a datos clínicos ("diabetes demo") para predecir una variable binaria: diabetes (1) o no (0). Sirve para triaje automático y prevención sin pagar laboratorio masivo; no sustituye al médico.

### 1.1 Perfil de los datos
- Entre 829 y 899 pacientes, 12 a 13 columnas según el equipo.
- **Clases desbalanceadas:** ≈ 64.8 % (537) sin diabetes y 35.2 % (292) con diabetes.

### 1.2 Limpieza: ceros falsos y variables que sobran
!!! Ceros que son datos faltantes
En glucosa, presión arterial, grosor de piel, insulina e IMC un cero no es medición: "una glucosa de cero no puede ser cierta en una persona que está viva". Se imputan (un equipo usó la media para no perder muestra) o se eliminan.

| Variable | Decisión | Razón |
|---|---|---|
| ID de la persona | **Se descarta siempre** | Es la "variable trampa": si entra al entrenamiento vicia el modelo |
| Insulina | Se quita | Más de 50 % faltante |
| Grosor de piel | Se quita | 30–50 % de ceros |
| Urea, hipoproteína | Se quitan (un equipo) | AUC univariada ≈ 0.5: no separan las clases |
| **Glucosa** | La más importante | Correlación 0.43–0.44; 35.4 % de importancia en árboles |
| Edad / IMC / embarazos | Secundarias | 18.3 % / ≈ 10 % / efecto positivo menor |

### 1.3 Modelos y resultados
Partición 70 % entrenamiento / 30 % prueba (239–249 registros de prueba), con `StandardScaler`.

| Modelo | Resultado reportado |
|---|---|
| Regresión logística | Razón de momios 2.53 para glucosa (cada unidad que sube multiplica el riesgo por 2.53); 24 FN y 46 FP |
| Árbol de decisión | Regla glucosa ≈ 142.5 mg/dL; por encima el riesgo sube a 62 %; 22 FN y 51 FP |
| Random Forest | El mejor global: exactitud 70–77 %, mayor ROC-AUC; 21 FN y 42 FP |
| SVM | Mayor área bajo la curva ROC según un equipo |

### 1.4 Falsos negativos y ajuste del umbral
!!! El error más grave en diagnóstico
El **falso negativo** (decir sano a un enfermo) es el peor error: "no detectar a tiempo a las personas que están enfermas". El falso positivo solo manda a alguien a una segunda revisión.

- Con umbral 0.5 un modelo daba entre 21 y 38 FN. Bajando el umbral a **0.35** (≈ 135 mg/dL de glucosa) los FN pasaron de **38 a 19**.
- Los 19 restantes: jóvenes con glucosa aún normal pero fuerte antecedente familiar.
- Los FP: sobre todo personas con obesidad e hiperglucemia que aún no desarrollan la enfermedad (prediabetes).
Errores comunes: entrenar con el ID; tomar ceros como mediciones; juzgar solo por exactitud sin ver la matriz de confusión ni el recall; dejar 0.5 cuando el FN cuesta mucho más.

## 2. Series de tiempo
Analizar y pronosticar una variable continua observada en intervalos regulares, descomponiéndola en **tendencia, estacionalidad, ciclicidad y residuales** (ver Clase 14).

### 2.1 ARIMA(p, d, q)
| Parámetro | Parte | Significado |
|---|---|---|
| p | AR (autorregresivo) | Cuántas observaciones pasadas predicen la actual |
| d | I (integrado) | Cuántas veces se diferencia la serie (yₜ − yₜ₋₁) para volverla estacionaria |
| q | MA (media móvil) | Tamaño de la ventana de errores pasados |
Los rezagos se eligen con las funciones de **autocorrelación (ACF)** y **autocorrelación parcial (PACF)**.

!!! Ruido blanco
Un ARIMA bien ajustado deja residuales que son ruido blanco: aleatorios, **sin correlación**, **media cero** y **varianza constante**. Es la prueba de que el modelo ya extrajo todo lo predecible.

### 2.2 Pregunta de examen: leer gráficas
En la lámina de gráficas A–I: **A, E e I** = tendencia clara; **B** = estacionaria (media y varianza estables); **G y H** = estacionalidad (picos que se repiten cada año). El profesor dijo textualmente que es pregunta de examen.
Error común: confundir **estacionaria** (sin tendencia ni cambio de varianza) con **estacional** (patrón que se repite).

### 2.3 Qué modelo según el negocio
| Negocio | Modelo | Por qué |
|---|---|---|
| E-commerce | SARIMA o Holt-Winters | Estacionalidad en fechas festivas |
| Bolsa / finanzas | ARIMA (también ARCH/GARCH) | Relaciones AR/MA de corto plazo, volatilidad |
| Energía por hora | SARIMA o Holt-Winters | Patrón diario: picos de día, caídas de noche |
| Manufactura / demanda | ARIMA o Holt-Winters | — |
| Turismo / hoteles | SARIMA o Holt-Winters | Temporadas vacacionales |
Usos: planeación de personal, inventarios, presupuestos, logística; integrable a ERP. Errores: ARIMA sin diferenciar una serie no estacionaria; suavizado exponencial simple con tendencia y estacionalidad a la vez.

## Avisos
- Examen: NotebookLM dice "jueves 13 de noviembre", pero el 13 nov 2026 es viernes; confirmar.
- Próximo tema: redes neuronales y lo que falta de series de tiempo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Limpieza clínica.** Descartar el ID (variable trampa). Ceros en glucosa, presión, piel, insulina o IMC = faltantes: imputar o quitar. Insulina (> 50 % faltante) y grosor de piel se eliminan. La glucosa es la variable dominante.

!!! Matriz de confusión médica (examen)
FN = enfermo clasificado como sano: el error más grave. Bajar el umbral de 0.5 a 0.35 bajó los FN de 38 a 19. No juzgar solo por exactitud: mirar recall.

**Modelos.** Random Forest fue el mejor global (70–77 %); regresión logística da razón de momios 2.53 para glucosa; el árbol corta en glucosa ≈ 142.5.

**ARIMA(p, d, q).** p = pasado (AR), d = diferenciaciones (I), q = errores pasados (MA); rezagos con ACF/PACF; residuales deben ser ruido blanco (media 0, varianza constante, sin correlación).

| Concepto | Para recordar |
|---|---|
| Tendencia | Nivel que sube o baja sostenidamente (gráficas A, E, I) |
| Estacionaria | Media y varianza estables (B) |
| Estacional | Patrón que se repite cada periodo (G, H) |
| Estacionalidad marcada | SARIMA o Holt-Winters |
| Volatilidad financiera | ARIMA / ARCH-GARCH |
