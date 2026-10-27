% materia: Reconocimiento de Patrones
% titulo: Clase −2 · Presentación del curso y conceptos básicos
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 17 ago 2026 (sesión 1 del curso) · Tema 1 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Fuente
**No asistí** (me inscribí tarde) y **no hay audio**. Todo sale del deck «Clase 1. Presentación del curso» (Classroom, 21 ago). La fecha se dedujo por cronología: el deck 3 fue el 24 ago y el semestre empieza el 17 ago.

## 1. El curso
- Lunes y viernes, 07:00–08:30, salón S227; 15 semanas, 28 sesiones; días inhábiles 2 y 16 nov; Python; Classroom `tz6dpily`.
- Temario del profesor (10 temas): conceptos básicos, extracción de características, selección y reducción, evaluación de modelos, funciones de decisión, clasificación por distancia, por similitud, aprendizaje automático, aprendizaje profundo, patrones estructurales y PLN.
| Rubro | Peso | Reglas |
|---|---|---|
| Tareas | 15 % | Individuales; −10 % por día de retraso |
| Prácticas / examen | 45 % | En equipo: código reproducible, reporte **IEEE** y presentación oral; no se aceptan tarde |
| Proyecto final | 40 % | Mismos 3 componentes; entrega tentativa 30 nov |
- Bibliografía: Fieguth; Braga-Neto; Dougherty; *Dive into Deep Learning*.

## 2. Qué es el reconocimiento de patrones
- Inferir algo desconocido a partir de mediciones: si es **continuo**, es **estimación**; si es **discreto**, es **reconocimiento de patrones**.
- Determinar la **clase** de un patrón; el proceso que elige la clase es el **clasificador**. Dos partes: **extracción de características** y **clasificación**.

## 3. Términos básicos (pregunta 1 del parcial)
| Término | Definición |
|---|---|
| **Patrón** | Cualquier objeto, proceso o evento que puede ser descrito y distinguido de otros |
| **Clase** | Categoría o etiqueta; conjunto de patrones con propiedades similares |
| **Característica** | Medición individual de un aspecto del patrón |
| **Clasificación** | Asignar un patrón a una clase con base en sus características |
| **Entrenamiento** | Aprender de ejemplos conocidos para clasificar patrones nuevos |
!!! Estructura del sistema (pregunta 2 del parcial)
**Patrón → mediciones → características → clasificador → clase.** Ej.: imagen de un perro como vector x = [131, 126, 128, …] → f(x) → y = 0 (gato) o 1 (perro).

## 4. Los tres problemas del diseño
1. **Representación:** ¿medí lo suficiente? Peso → salud (50 kg no sano, 60 y 70 sano, 80 no sano) no se separa con un umbral: falta la estatura. Salmón vs. robalo: la longitud se traslapa; la **luminosidad** separa mejor.
2. **Extracción y reducción:** ¿medí de más? Breast Cancer Wisconsin: 569 casos (357 benignos, 212 malignos), 30 características; correlación con la clase: área 0.82, textura 0.79, concavidad 0.85, simetría 0.12, dimensión fractal 0.05 → quedarse con área, textura y concavidad. Imagen de 3000×1800 = ℝ^5,400,000 → reducida a ℝ^500.
3. **Decisión óptima:** con lo que medí, ¿cómo decido?

## 5. Maldición de la dimensionalidad (pregunta 6 del parcial)
Al añadir dimensiones el volumen crece **exponencialmente**: dispersión, más cómputo, **sobreajuste**, distancias sin sentido, peor rendimiento, difícil visualizar.
!!! El verdadero problema
La distancia media **aumenta** con las dimensiones y la **variabilidad de la distancia disminuye exponencialmente**: todos los puntos quedan casi a la misma distancia y un clasificador por distancia ya no distingue vecinos.
- Solución: **reducción de dimensionalidad** (conservar lo importante, con pérdida inevitable de información). Más dimensiones ≠ mejor.
- Ejemplos de sistemas: visión (rostros, imagen médica, autos autónomos), PLN (asistentes, traducción), biometría (huella, iris).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Patrón | Objeto, proceso o evento descriptible y distinguible |
| Sistema | Patrón → mediciones → características → clasificador → clase |
| Estimación vs. RP | Continuo vs. discreto |
| 3 problemas | Representar, extraer/reducir, decidir |
| Maldición | Distancias casi iguales; sobreajuste; se reduce dimensión |
| Evaluación | Tareas 15 %, prácticas/examen 45 %, proyecto 40 % |
