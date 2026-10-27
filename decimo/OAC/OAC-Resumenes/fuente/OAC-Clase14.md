% materia: Organización y Arquitectura de Computadoras
% titulo: Clase 14 · Proyecto final y red neuronal en la Pico
% subtitulo: Organización y Arquitectura de Computadoras · M.I. José Antonio de Jesús Arredondo Garza · lunes 26 oct 2026 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Clase sin tema nuevo del temario: opciones técnicas del proyecto final, una red neuronal multicapa corriendo en MicroPython sobre la Raspberry Pi Pico 2 y la fecha de entrega. Continúa la Clase 13.

## 1. Proyecto final: ensamblador o mem32
El profesor propuso dos vías para el proyecto en la Raspberry Pi Pico 2. Hay que elegir la que mejor se acomode al diseño.

| Vía | Para qué conviene | Costo |
|---|---|---|
| **Ensamblador nativo** | Procesamiento numérico y punto flotante: aprovecha la **FPU** de la Pico 2 | Muy laborioso para direccionar periféricos: instrucción por instrucción |
| **mem32** (`machine.mem32`) | Control de hardware: lee y escribe directo los registros de memoria del hardware desde MicroPython | No sustituye a la FPU para cálculo de precisión |

!!! Regla de decisión
Proyecto de cálculo o punto flotante → ensamblador. Proyecto de control de hardware → direccionar registros con mem32.

Error común: manejar todos los periféricos con rutinas largas en ensamblador cuando basta el acceso directo a memoria.

## 2. Red neuronal (perceptrón multicapa) en MicroPython: la compuerta XOR
Un paquete ligero de perceptrón multicapa que corre en MicroPython sobre la Pico. En clase se usó para que la red **aprenda la XOR a partir de ejemplos**, sin darle la fórmula.

### Por qué XOR necesita una red
AND y OR son **linealmente separables** y tienen solución directa. La XOR (OR exclusiva) no se separa con una recta, así que necesita una **capa oculta con activación no lineal**.

| x₁ | x₂ | XOR |
|---|---|---|
| 0 | 0 | 0 (falso) |
| 0 | 1 | 1 (verdadero) |
| 1 | 0 | 1 (verdadero) |
| 1 | 1 | 0 (falso) |

### Topología (2, 2, 1)
- **Entrada:** 2 neuronas (las dos entradas).
- **Oculta:** 2 neuronas (combinaciones no lineales).
- **Salida:** 1 neurona (la respuesta aproximada).
- **Activación:** gaussiana.

### Flujo del programa de ejemplo
1. Crear la red y definir las capas (2, 2, 1).
2. Elegir la activación gaussiana y definir los estados lógicos falso y verdadero.
3. Agregar los cuatro ejemplos de la tabla de verdad.
4. Ejecutar el aprendizaje y comprobar las respuestas con la predicción.
La librería va en un archivo grabado en la flash de la Pico. Los nombres exactos del módulo y de las funciones no están confirmados (reconstrucción de NotebookLM): revisar el archivo que dio el profesor.

### Otras ideas de proyecto que dio
- **Convertidor °C → °F:** se entrenan solo 5 puntos de Celsius y la red predice (interpola) los Fahrenheit intermedios sin conocer la ecuación.
- **Tabla de verdad grande** con estados independientes, resuelta sin álgebra booleana tradicional.

Se conecta con las SBC y la Pico 2 (Clase 13) y con las redes neuronales de Reconocimiento de Patrones. Error común: usar una red para problemas lineales directos (AND, OR) o hacerla tan grande que no quepa en la memoria de la Pico.

## 3. Calendario de cierre
| Dato | Fecha |
|---|---|
| Fin oficial de clases | sábado 28 nov 2026 |
| Días inhábiles mencionados | lunes 2 nov y lunes 16 nov |
| Clases efectivas restantes | 6 |
| **Presentación del proyecto final** | **miércoles 25 nov 2026** |
El profesor adelanta la revisión por una cita médica, para liberar calificaciones a tiempo. Error común: suponer que la entrega es hasta el sábado 28. Próxima sesión (según NotebookLM, sin confirmar): herramientas de software de embebidos que no se vieron en pandemia (Raspberry Pi grande y simuladores).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Proyecto final.** Dos vías en la Pico 2: ensamblador (cálculo, FPU) o mem32 (registros de hardware desde MicroPython).

!!! XOR en una red (examen)
XOR no es linealmente separable: necesita capa oculta y activación no lineal. Red (2, 2, 1): 2 entradas, 2 ocultas, 1 salida, activación gaussiana. Tabla: 00→0, 01→1, 10→1, 11→0. AND y OR no necesitan red.

**Cómo aprende.** Se le dan ejemplos (la tabla de verdad), aprende y luego predice; con 5 puntos °C→°F interpola los intermedios.

!!! Fecha que importa
Presentación del proyecto final: **miércoles 25 de noviembre de 2026** (no el sábado 28).
