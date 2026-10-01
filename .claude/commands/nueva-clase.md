---
description: Agregar una clase nueva al sitio de apuntes, de punta a punta (prompt de NotebookLM → página → temario → buscador → commit → push)
---

Vas a guiar el flujo completo para agregar una clase nueva al sitio de apuntes
del semestre. Lee `CLAUDE.md` en la raíz del repo primero si no lo tienes ya
en contexto — ahí está la estructura, convenciones y colores de cada materia.

Argumento opcional del usuario: $ARGUMENTS (puede venir vacío, o con la
materia/fecha ya indicada, o incluso con el resultado de NotebookLM ya
pegado — revisa antes de preguntar nada que ya te hayan dado).

## Paso 1 — Identificar la clase

**Primero mira qué falta:** abre `progreso.html` (o corre
`python3 scripts/build_progress.py` y cruza `assets/progreso.json` contra
`assets/horario.json`). Ahí sale cuál es la siguiente clase por meter y todas
las faltantes, calculadas con el horario oficial. No le pidas al usuario el
horario: está en `assets/horario.json`.

Si no está claro por $ARGUMENTS o por el mensaje del usuario, pregunta:
materia, número de clase, y fecha.

**Verificación de fecha, siempre:** usa la tabla "Horario oficial" en
`CLAUDE.md` (confirmada directamente por el usuario, no inferida) para
verificar que la fecha propuesta cae en el día que le toca a esa materia. Si
no cuadra, dilo explícitamente y pide confirmación en vez de asumir — nunca
adivinar el patrón a partir de páginas anteriores.

## Paso 2 — Prompt para NotebookLM (formato de estudio, desde 1 oct 2026)

Si el usuario todavía no tiene el resultado de NotebookLM, dale este prompt
(ajustado con el nombre real del profesor/a, materia y fecha). Si tienes
Claude en Chrome conectado y el usuario ya subió el audio a NotebookLM,
puedes pegarlo tú mismo en el cuaderno de la materia y leer la respuesta.

```
Eres mi asistente de estudio. Usa SOLO las fuentes de este cuaderno (el audio
de la clase de "<MATERIA>" con <PROFESOR/A>, del <DÍA fecha>, Clase <NN>, y
el material del profesor que esté cargado). No inventes nada: si algo no se
dijo en clase ni está en el material, no lo pongas. Cuando algo venga del
material y no del audio, márcalo con [material].

Mi objetivo: entender cada concepto tan bien que se lo pueda explicar a
cualquier persona, y llegar preparado al examen. Genera, en español:

1. RESUMEN — una línea con el tema principal de la clase.

2. LO QUE PROBABLEMENTE VIENE EN EL EXAMEN — de 3 a 6 puntos. Para cada uno,
   di POR QUÉ crees que viene, con evidencia de la clase: el profesor lo dijo
   explícitamente, lo repitió, lo escribió en el pizarrón, resolvió un
   ejercicio de eso, o lo conectó con una tarea/práctica. Si no hay evidencia
   fuerte, dilo.

3. TEMAS — en el MISMO ORDEN en que se explicaron. Para cada concepto
   importante, usa esta estructura:
   a) Qué es — la definición exacta como la dio el profesor.
   b) Explicado en simple — cómo se lo explicarías a alguien sin la carrera,
      con una analogía cotidiana (y aclara dónde la analogía deja de servir).
   c) Cómo funciona — el detalle técnico completo en PÁRRAFOS: pasos,
      fórmulas, comandos, ejemplos y ejercicios resueltos en vivo con sus
      números reales, preguntas que hizo el profesor y lo que respondieron
      los alumnos. No recortes nada técnico por parecer menor.
   d) Por qué importa / con qué se conecta — relación con clases anteriores,
      con prácticas o con el mundo real (según lo dicho en clase).
   e) Errores comunes — confusiones que el profesor señaló o que se notaron
      en las respuestas de los alumnos (solo si las hubo).

4. PONTE A PRUEBA — de 6 a 10 preguntas con su respuesta, mezclando:
   recordar (definiciones), explicar con tus palabras, aplicar (un ejercicio
   como los de clase con otros datos) y comparar conceptos. La respuesta debe
   salir de la clase o del material.

5. CONTEXTO — NO EXAMEN — anécdotas, tangentes, experiencias del profesor.

6. PENDIENTE / PRÓXIMA CLASE — tareas, entregas, fechas y lo que se verá
   después, tal como se dijo.
```

**Por qué este formato** (para no rediseñarlo en cada sesión): combina las
técnicas de estudio con más evidencia según la revisión de Dunlosky et al.
(2013) — práctica de recuperación (*Ponte a prueba*, Roediger y Karpicke
2006) e interrogación elaborativa (*por qué importa*) — con ejemplos resueltos
(Sweller) y la técnica Feynman (*explicado en simple*). La predicción de
examen siempre lleva evidencia de la clase, nunca adivinanzas.

Si el usuario faltó a esa clase, en vez de esto usa el patrón de
"clase reconstruida" — revisa `arquitectura-cliente-servidor/clase-05.html`
como ejemplo: se busca el material oficial del profesor (su sitio, PDFs) y se
marca con una nota visible de que no se asistió, sin sección de examen ni
contexto propios (no hay audio del que sacarlos).

## Paso 3 — Construir la página

Con el resultado de NotebookLM (o el material oficial reconstruido), arma
`materias/<slug>/clase-NN.html` siguiendo exactamente la plantilla descrita en
`CLAUDE.md` ("Plantilla de una página clase-NN.html — formato de estudio").
Ejemplo de referencia: `materias/administracion-de-servicios-de-internet/clase-10.html`. Usa el color de acento correcto de la tabla en `CLAUDE.md`. Mira 2-3
páginas de clase recientes de esa misma materia para igualar tono y
densidad — pero nota que a partir de sep 2026 el formato cambió (ver
`CLAUDE.md`): ya no se usan las cajas "En corto"/"🎯 Para el examen" como
resumen principal, el cuerpo detallado es la prosa completa.

## Paso 4 — Actualizar el índice de la materia

En `materias/<slug>/index.html`:
- Vista "Por tema": actualizar el badge de clases del tema correspondiente
  (ej. "Clases 01–05"), marcar subtemas nuevos como vistos con
  `<span class="seen">Clase NN</span>` y el enlace correspondiente.
- Vista "Por clase": agregar la tarjeta `<a class="clase-link" href="clase-NN.html">...`
  con fecha, tema y descripción corta.

Si la clase trae tareas o rúbricas nuevas, también actualizar
`evaluacion.html` si existe. Si el usuario comparte un archivo nuevo del
profesor (guion, diapositiva, plantilla), va a `files/` y se agrega una fila
en `material.html`; si comparte algo que él mismo entregó, va a
`files/entregas/` y se agrega una fila en `entregas.html` — nunca mezclar los
dos (ver "Regla de oro de archivos" en `CLAUDE.md`).

## Paso 5 — Buscador y publicación

```bash
python3 scripts/build_search_index.py   # también regenera assets/progreso.json
git add -A
git commit -m "<Sigla>: agregar Clase NN (fecha) — resumen corto del contenido"
git push origin main
```

Commitea y pushea sin pedir confirmación adicional — es el flujo ya
establecido con el usuario (GitHub Pages se actualiza solo). Al final,
confírmale en un mensaje corto qué se agregó y qué sigue pendiente en la cola
si estaban procesando varias clases.
