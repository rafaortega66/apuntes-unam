# FSE-E02 — Segundo examen parcial · indicaciones

Fuentes: Google Classroom (tarea «Segundo examen parcial», tema «3. Sistemas operativos para plataformas embebidas», revisado el 24 nov 2026)
y NotebookLM, cuaderno FSE, audios FSE-Clase13 a FSE-Clase21 (consultado el 24 nov 2026).

- **Fecha:** miércoles 25 nov 2026. Classroom pone como vencimiento las 2:30 PM (la hora en que termina la clase, 13:00–14:30, A107).
  En los audios no se dio fecha ni formato (el profesor ubicó la última sesión del curso el 25 nov, Clase 18).
- **Alcance:** Unidad 3 completa, «Sistemas operativos para plataformas embebidas» (en la Clase 13 dijo que la Unidad 3 no entraba en el 1.er parcial).
  Diapositivas del profesor: `FSE-Material/diapositivas-clase-09.pdf` a `-18.pdf`.
- **Formato:** no lo dijo. Como referencia, el 1.er parcial fue de 50 preguntas (25 abiertas y 25 de opción múltiple), según la Clase 15.
- **Clase 22 (18 nov):** el usuario no fue y no hay audio; puede haber avisos del examen que no están aquí.

## Lo que el profesor dijo que viene (o no viene)

| Clase | Tema | Lo que dijo (según NotebookLM) | Tipo |
|---|---|---|---|
| 13 | Los 6 pasos de una llamada a servicio (system call) | «Vamos a pasar por seis deliciosos pasos. Pregunta de examen.» | Pasos en orden |
| 13 | Programa vs. programa en ejecución vs. proceso | «Si no sabe la diferencia entre programa, programa en ejecución y proceso…» no merece estar en la carrera | Definición |
| 17 | Orden de atención de las colas con prioridad (scheduling) | Puso analogías para que «se acuerden en el maldito examen» | Conceptual |
| 18 | Minimal Laxity First | «Si fuera examen, voy a volver a ejecutar la tarea P1 y ya acabé.» | Ejercicio (línea de tiempo) |
| 18 | Rate Monotonic: cota del 70 % | **No viene la demostración**; sí aplicar el criterio Σ Cᵢ/Tᵢ ≤ 1 y la cota n(2^(1/n) − 1) → ln 2 ≈ 0.7 | Criterio |
| 19 | Los 5 algoritmos de asignación de memoria: First, Next, Best, Worst y Quick Fit | «Los cinco algoritmos que vienen en el examen» | Conceptual/comparativo |
| 21 | Controladores dedicados vs. genéricos | «Esto es pregunta de examen: los dedicados y los genéricos.» | Definición/clasificación |
| 21 | initramfs | «Ese sí se lo tienen que saber.» | Identificación |
| 20 | Temporizador asíncrono periódico con semáforo binario (bar() cada 10 ms que dura más que su periodo) | «Es pregunta para entrar a Google»: no dijo «examen», pero lo marcó como el problema clave del tema | Diseño/ejercicio |

Mapa completo de las clases 13–21: `FSE-E02-adicionales/FSE-E02-mapeo-notebooklm.md`.
