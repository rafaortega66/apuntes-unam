# Prompts de NotebookLM para FSE (12 oct 2026)

Objetivo: apuntes tipo libro de cada clase de FSE, con el audio ligado a las
presentaciones del profesor. Prioridad: examen del miércoles 14 oct (Unidades
1 y 2). Unidad según el temario oficial: U1 = tema 1 (1.1–1.5), U2 = tema 2
(2.1–2.9), U3 = tema 3 en adelante (fuera del examen).

Cómo usarlos: en el notebook, deja activas SOLO estas fuentes: el audio de
esa clase, las 8 presentaciones (Clase 01 a 08) y `00-temario.pdf`. Corre el
PROMPT A una vez por audio. Cuando termines todos los audios, corre el
PROMPT B una sola vez con todos los audios activos.

Nota: NotebookLM a veces acorta la transcripción literal. Si lo hace, abre la
fuente del audio (clic en su nombre) y copia la transcripción de ahí.

## PROMPT A (uno por audio)

```
Eres mi asistente de apuntes para Fundamentos de Sistemas Embebidos. Trabaja SOLO con las fuentes activas: el audio de esta clase, las presentaciones del profesor (Clase 01 a 08) y el temario. No inventes nada; si algo no está en las fuentes, dilo.

PASO 0 — UNIDAD. Usando el temario, di a qué unidad y subtemas (con su número, p. ej. 2.6) pertenece esta clase. Si la clase pertenece a la Unidad 3 o posterior (subtemas 3.x, 4.x, 5.x), DETENTE: escribe solo "UNIDAD 3+ — FUERA DEL EXAMEN" y una línea con el tema, sin más.

Si es Unidad 1 o 2, entrega lo siguiente, en este orden y con estos títulos exactos:

## 1. ENCABEZADO
Número de clase (en orden de grabación), fecha si el audio la dice, unidad y subtemas del temario.

## 2. TRANSCRIPCIÓN
La transcripción completa del audio, lo más literal posible, sin resumir.

## 3. MAPA CLASE ↔ PRESENTACIÓN
Tabla con una fila por tema visto: Tema | Presentación (p. ej. "Clase 05.pdf") | Láminas (números) | Cobertura en esta clase (Completa / Parcial / Solo mencionada / No se tocó en la presentación, explicado de viva voz).
Después, una lista "Láminas de esas presentaciones que el profesor NO cubrió en esta clase", con número y título de cada una.

## 4. APUNTES TIPO LIBRO
Solo teoría, lo más resumido posible pero SIN dejar nada de fuera: cada concepto, definición, clasificación, fórmula, dato numérico, ejemplo resuelto, comparación y advertencia que el profesor dio. Estructura: capítulo por tema, secciones numeradas, definiciones exactas en negritas, tablas solo para comparaciones, fórmulas aparte. Sin anécdotas ni relleno. Marca con "[solo en lámina]" lo que sale de la presentación pero el profesor no dijo en el audio, y con "[solo en clase]" lo que dijo el profesor y no aparece en ninguna lámina.

## 5. LO QUE EL PROFESOR ENFATIZÓ
Lista de lo que repitió, resolvió en el pizarrón, preguntó en vivo o dijo que importa para evaluar, con la evidencia entre comillas cortas.

Si la respuesta no cabe, termina con "CONTINUARÁ EN LA PARTE N" y espera a que yo escriba "continúa". No omitas secciones para ahorrar espacio.
```

## PROMPT B (una sola vez, con todos los audios activos)

```
Con todas las fuentes activas (todos los audios de FSE, las presentaciones Clase 01 a 08 y el temario), construye una matriz de cobertura. Para CADA presentación (Clase 01.pdf ... Clase 08.pdf) y CADA lámina o grupo de láminas con tema propio, indica:
- Número(s) de lámina y título.
- Subtema del temario al que pertenece (p. ej. 2.6) y unidad.
- Estado: "Visto en clase N" (el audio explica ese contenido; indica en qué clases y si fue completo o parcial) o "No visto en ninguna clase grabada" (el contenido nunca aparece en los audios; es previo a la primera clase grabada o el profesor no lo cubrió).
No inventes: si dudas, escribe "dudoso" y explica por qué. Entrega tabla por presentación y al final dos listas: (1) todas las láminas "No visto en ninguna clase grabada" de las Unidades 1 y 2, (2) los subtemas 1.x y 2.x del temario que no aparecen en ningún audio. Si no cabe, termina con "CONTINUARÁ EN LA PARTE N".
```
