% materia: Minería de Datos
% titulo: Clase 21 · Más exposiciones de redes neuronales, selección de variables y matriz de confusión
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 12 nov 2026 · Práctica 3.6 (redes neuronales) y Tema 4 (CRISP-DM y evaluación de modelos) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Segunda ronda de exposiciones de la Práctica 3.6 (CNN, MLP, LSTM y autoencoder) y continuación del Tema 4: repaso de CRISP-DM, variantes de validación cruzada, selección de variables, muestreo, umbrales, matriz de confusión, principio de longitud mínima y *binning*.

!!! Fuente
Fuente: NotebookLM (audio `MD-Clase21.m4a`), 14 nov 2026. Parte de la teoría y de los pendientes coincide con la Clase 20; aquí se agrega solo lo nuevo. ⚠️ Es posible que NotebookLM haya mezclado algo de la clase anterior en los pendientes.

## 1. Exposiciones de la Práctica 3.6 (segunda ronda)
Cifras de los alumnos; las intervenciones del profesor se indican.

!!! En simple
Elegir el vehículo según el terreno: CNN para fotos, MLP para tablas, LSTM para series donde ayer importa, autoencoder para comprimir estadísticas y encontrar perfiles parecidos.

| Caso | Red | Lo más importante |
|---|---|---|
| Uso de suelo (Intel, 17,000 imágenes, 6 clases balanceadas) | CNN de 4 bloques (32→256 filtros) | ~1.24 millones de parámetros contra ~17 millones solo en la primera capa de un MLP; paro temprano en la época 18 (pesos de la 12); 87 / 86 / 86 % → generaliza bien (diferencia < 3 puntos; 3–8 = ligero sobreajuste; > 8 = memoriza). Encontró imágenes mal etiquetadas. El profesor: «perfecto, muy bien». |
| Deserción escolar (UCI, Portugal, 4,424 alumnos, 36 variables, 3 clases) | MLP de 16 neuronas, alfa = 1 | One-hot de la carrera (121 entradas); acertó al 80 % de los que abandonaron (209 de 284); pesó más la regularización que la cantidad de datos. |
| Churn en telecomunicaciones (IBM, ~7,000) | MLP 64-32 con batch normalization | Recall ~78 %; con el 20 % superior captura 2.46 veces más que al azar. |
| ¿Oficina ocupada? (UCI, 4 variables) | MLP | ~5 % de error en vacías y ~20 % en ocupadas. |
| Churn de internet (IBM) | MLP de 32 neuronas | El MLP no superó al modelo lineal. El profesor preguntó por qué: con más capas sobreajustaba y con menos perdía capacidad. |
| Afluencia de la Línea 3 del metro | LSTM de 50 unidades | Solo fecha y afluencia; sin años previos a 2021 por la pandemia; MAE de 46,000 pasajeros (~7–8 %), falla en días atípicos como sismos. |
| Scouteo de futbolistas para Pumas | Autoencoder 70-48-36-12 | De 12,000 jugadores a 5 candidatos para 3 puestos; complementa, no sustituye al scouteo humano. |
Error común: datos mal etiquetados en origen; agregar complejidad innecesaria.

## 2. Repaso de CRISP-DM
Las 6 fases: negocio, datos, preparación, modelado, evaluación y despliegue (ver la Clase 20).

Quien conoce un sector (banca, seguros, hospitales) puede proponer métricas más ricas que las que pidió el cliente. En la preparación se generan variables nuevas (incorporar el tiempo para la demanda, ponderar la temperatura sobre un umbral). La evaluación es técnica (ROC, error cuadrático medio, silueta, validación cruzada) y de negocio.

## 3. Variantes de la validación cruzada
K-fold: dividir en K partes, rotar la de prueba y promediar los scores.

!!! En simple
Dividir la temporada en 5 torneos: en cada uno un bloque distinto juega de visitante y los demás entrenan; al final promedias.

- **K-fold aleatorio:** baraja antes de dividir.
- **Estratificado:** conserva las proporciones de las clases.
- **Repetido:** repite el proceso con distinta aleatoriedad.
- **Por grupo (Group K-fold):** todo el historial de un mismo paciente queda en el mismo bloque.

70/30 basta en modelos sencillos; en científicos o médicos hace falta K-fold.

## 4. Selección de variables y prevención del sobreajuste
Revisar variable por variable su correlación, asociación y aporte.

Eliminar variables muy correlacionadas entre sí; pruebas estadísticas (chi-cuadrada, ANOVA); eliminación recursiva: si de 20 variables 6–8 aportan 0.001 %, se descartan, sin recortar de más.

Proyecto real del profesor: 500 registros y ~760 variables (bombas, torque, presión) que, tras días de trabajo con el cliente, quedaron en 25–30 variables en dos grupos.

Contra el sobreajuste: Ridge/Lasso, dropout, podar árboles, K-fold y aumento de datos.

## 5. Muestreo, umbrales, matriz de confusión, longitud mínima y binning
Criterios para datos masivos, para el porcentaje aceptable según la industria, el costo de los errores y el equilibrio entre error y complejidad.

!!! En simple
No muerdes las 100,000 manzanas del camión: tomas una muestra de cada caja. Y no cuesta lo mismo equivocarte al recomendar una playera que al diagnosticar un cáncer.

**Muestreo y estratificación:** con millones de tickets diarios, muestras por tienda o categoría (lácteos por su caducidad) o por región; sensores cada segundo con valores casi iguales → promediar cada 5 minutos.

**Umbrales:** en ventas, más de 80 % es muy bueno; en medicina, 90 % o más; nunca hay 100 % (el tope práctico ronda 93–94 %).

**Matriz de confusión (cáncer: sano, nivel 3, nivel 5):** lo crítico es decir sano a quien tiene nivel 3, o nivel 5 a un sano. Seis pasos: revisar la matriz, ajustar el umbral, balancear clases, revisar variables, probar 2 o 3 algoritmos y evaluar con precisión, recall y F1. En medicina se toleran más falsos positivos para evitar falsos negativos; en crédito y fraude se cuidan los falsos positivos o se pondera cada error.

**Principio de longitud mínima:** los modelos muy simples tienen más error y los muy complejos sobreajustan; se busca el punto medio.

**Binning:** agrupar valores continuos en rangos (edades 0–10, 10–20, 20–30…).
Error común: esperar 100 %; tratar igual un falso positivo que un falso negativo sin ver el dominio.

## Pendiente / próxima clase
- **Proyecto final: jueves 19 nov a la 1:00 p.m.** Individual, 6 fases de CRISP-DM (más peso en la 1 y la 6), Python y presentación de exactamente 10 láminas; las exposiciones empiezan ese día.
- Las exposiciones de redes neuronales que faltaron pasan al martes.
- **Tercer parcial:** el martes después del jueves 19 (todo el curso). Última clase a más tardar el jueves 26 o el martes 1.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Todo lo visto: el tercer parcial cubre todo el curso.** el profesor lo dijo explícitamente al situar el cierre.
- **Subajuste, sobreajuste y buen ajuste, y cómo corregirlos.** «muchos de ustedes mismos ya me lo han hasta contestado en el examen».
- **Validación cruzada y sus variantes; cuándo basta 70/30.** le dedicó un bloque formal.
- **Matriz de confusión: falsos positivos contra falsos negativos y las seis acciones correctivas.** evidencia por énfasis: lo analizó con el caso de cáncer.
- **CRISP-DM y la selección y preparación de variables.** evidencia moderada: cierre del Tema 4 antes del examen.

!!! Puntos clave
- Diferencia entrenamiento-prueba: < 3 puntos bien; 3–8 ligero sobreajuste; > 8 memoriza.
- K-fold aleatorio, estratificado, repetido y por grupo.
- Selección de variables: correlación, chi-cuadrada, ANOVA, eliminación recursiva.
- Ventas > 80 %, medicina ≥ 90 %, nunca 100 %; en salud, evitar falsos negativos.
- Longitud mínima (equilibrio) y binning (rangos).

## Ponte a prueba
1. **Entrenamiento 87 %, validación 86 %, prueba 86 %: ¿qué indica?** Buena generalización: la diferencia es menor a 3 puntos.
2. **¿Para qué sirve Group K-fold?** Para que todos los registros de un mismo paciente queden en el mismo bloque.
3. **¿Qué haces con variables muy correlacionadas entre sí o que aportan casi nada?** Eliminarlas (correlación, chi-cuadrada, ANOVA, eliminación recursiva), sin recortar de más.
4. **En medicina, ¿qué error se tolera más?** Los falsos positivos, para evitar falsos negativos.
5. **¿Qué es el binning?** Agrupar valores continuos en rangos, como edades por décadas.
6. **¿Qué dice el principio de longitud mínima?** Equilibrar error y complejidad: ni tan simple que falle, ni tan complejo que sobreajuste.
