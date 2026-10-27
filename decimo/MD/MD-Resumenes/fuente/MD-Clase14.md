% materia: Minería de Datos
% titulo: Clase 14 · Regresión del vino e introducción a series de tiempo
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 20 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Retroalimentación de la Práctica 3.3: alcohol en vino
Predecir el **porcentaje de alcohol** (variable continua) de un vino a partir de **12 variables fisicoquímicas** de **178 muestras**, con Regresión Lineal Múltiple, Lasso, Árbol de Decisión y Random Forest, en Python y RapidMiner.

### 1.1 Objetivo de negocio
El alcohol va de 12 % a 14 % (media ≈ 13 %). Estimarlo sirve para informar al cliente, calcular impuestos (más graduación, más impuesto) y controlar calidad y sabor durante la fermentación, sin pagar análisis de laboratorio.

### 1.2 Preparación
- **Atípicos** en 7 de 12 variables (ácido málico, ceniza): **no se eliminaron**, porque son variaciones químicas reales, no errores de captura.
- **StandardScaler:** prolina y magnesio tienen rangos enormes frente al matiz o los flavonoides (decimales).

### 1.3 Variables influyentes
| Variable | Efecto en el alcohol |
|---|---|
| Color intenso | ↑ — 44.15 % de importancia en Random Forest |
| Prolina | ↑ — 19.94 % |
| Ceniza alcalina | ↓ — coeficiente −0.33 en la regresión |
| Protocianinas | ↓ efecto inverso |

### 1.4 Comparación de modelos
| Modelo | Resultado |
|---|---|
| Regresión Lineal | R² 0.434 (RapidMiner) y 0.68 (otra corrida), error 0.17–0.628 |
| Árbol de Decisión | Mucha dispersión; **R² en prueba cayó a 0.29** (sobreajuste) |
| **Random Forest** | Ganador: **R² 0.75–0.77**, menor error (0.12–0.13), robusto a atípicos y no linealidades |

!!! Modelo reducido
Con solo **5 variables** (color intenso, prolina, protocianinas, flavonoides, ceniza alcalina) se perdió apenas **0.03–0.04 de R²** frente a las 12: cinco variables concentran casi todo el poder predictivo.

!!! Entrenamiento vs. prueba
R² alta en entrenamiento y baja en prueba (0.29) = la muestra de prueba no fue representativa o el modelo sobreajustó. Solución: **validación cruzada K-fold**, que rota los estratos y estabiliza la evaluación (Clase 13).

## 2. Series de tiempo
!!! Definición
Conjunto secuencial de valores de una variable registrados a **intervalos regulares** (días, semanas, meses, años). Eje X = tiempo; eje Y = la variable (ventas, demanda de energía, temperatura…).

**Usos:** pronosticar (3 a 5 meses), detectar patrones (tendencia, estacionalidad) y detectar anomalías (fraude, fallas).
**Horizonte:** aunque se pueda calcular a 12 meses, la confiabilidad cae al alejarse. Los algoritmos pesan más los últimos 2–3 años que lo de hace 15.

| Componente | Qué es |
|---|---|
| **Tendencia** | Movimiento de largo plazo, ascendente o descendente |
| **Ciclicidad** | Fluctuaciones de largo plazo que abarcan varios años |
| **Estacionalidad** | Patrón que se repite en un periodo fijo, normalmente un año (picos a mitad de año o diciembre) |
| **Irregular / ruido** | Variaciones impredecibles por eventos extraordinarios (pandemia, ciclones, remates) |
Los picos extraordinarios se analizan y se filtran (sobre cierto umbral) para que no deformen el pronóstico.

## 3. Modelos y métricas
| Modelo | Cuándo |
|---|---|
| Suavizado exponencial **simple** | Sin tendencia ni estacionalidad; solo suaviza el ruido |
| **Doble (Holt)** | Agrega la tendencia |
| **Triple (Holt-Winters)** | Tendencia + estacionalidad + irregular |
| **ARIMA / SARIMA** | Series complejas no estacionarias que se transforman en estacionarias |

| Parámetro ARIMA | Significado |
|---|---|
| **p** (AR, autorregresivo) | Cuántas observaciones pasadas (rezagos) influyen en el valor actual |
| **d** (I, integrado) | Grado de diferenciación para volver estacionaria la serie (quitar tendencia) |
| **q** (MA, media móvil) | Ventana de errores de pronósticos pasados para corregir el modelo |

**Métricas:** **MAPE** (error porcentual absoluto medio; la más popular por ser porcentual e intuitiva), MAE (unidades de la variable), MSE/RMSE (castigan más los errores grandes).
Errores comunes: suavizado simple en una serie con tendencia o estacionalidad; mal ajuste de p, d, q.

## Avisos
- La Práctica 3.4 (clasificación) vence el jueves 22 oct, 1:00 p. m.; se puede hacer solo en Python. El curso concluye hacia el 13 de noviembre (según NotebookLM).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Vino.** Color intenso y prolina suben el alcohol; ceniza alcalina lo baja. Atípicos reales no se borran. Random Forest gana (R² 0.75–0.77). Con 5 variables se pierde solo 0.03–0.04 de R².

**Sobreajuste.** R² de prueba muy por debajo de la de entrenamiento (el árbol: 0.29) → validación cruzada K-fold.

!!! Componentes de una serie (examen)
Tendencia (largo plazo), ciclicidad (varios años), estacionalidad (se repite cada periodo fijo) e irregular (eventos extraordinarios).

| Modelo | Para recordar |
|---|---|
| Simple | Solo ruido |
| Holt (doble) | + tendencia |
| Holt-Winters (triple) | + tendencia + estacionalidad |
| ARIMA(p, d, q) | p = rezagos, d = diferenciaciones, q = errores pasados |
| MAPE | Error en porcentaje; la métrica más usada en pronóstico |
