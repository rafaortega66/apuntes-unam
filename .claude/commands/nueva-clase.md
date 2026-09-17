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

Si no está claro por $ARGUMENTS o por el mensaje del usuario, pregunta:
materia, número de clase, y fecha.

**Verificación de fecha, siempre:** antes de aceptar una fecha dictada de
memoria, revisa el patrón de días de esa materia (los dos días fijos a la
semana que ya se ven en las clases anteriores del mismo `materias/<slug>/index.html`,
vista "Por clase") y confirma que la fecha propuesta cae en uno de esos días.
Si no cuadra, dilo explícitamente y pide confirmación en vez de asumir.

## Paso 2 — Prompt para NotebookLM

Si el usuario todavía no tiene el resultado de NotebookLM, dale este prompt
(ajustado con el nombre real del profesor/a, materia y fecha):

```
Eres mi asistente de apuntes de clase. Te voy a dar el audio de una clase de
la materia "<MATERIA>", impartida por <PROFESOR/A>, del <DÍA fecha> (Clase <NN>).

Necesito apuntes de estudio completos y bien redactados — NO un resumen
ejecutivo. El objetivo es que, leyéndolos, pueda "revivir" la clase: que no
se pierda nada técnico de lo que se explicó, pero que esté redactado como
prosa clara y bien organizada, no como fragmentos sueltos.

Genera el resultado en este formato:

1. UNA LÍNEA de resumen del tema principal de la clase (para usar como subtítulo).

2. "TEMAS" — divide el contenido de la clase en secciones temáticas, en el
   MISMO ORDEN en que se explicaron (no por importancia ni alfabético). Usa el
   título de cada tema como encabezado. Dentro de cada sección, escribe
   PÁRRAFOS COMPLETOS (no solo bullets) explicando: qué es el concepto, por
   qué importa, cómo se conecta con lo anterior, toda definición o fórmula
   exacta que se haya dado, y cualquier ejemplo o ejercicio resuelto en vivo
   con sus números/pasos reales (no "se resolvió un ejemplo", sino el ejemplo
   completo). Usa bullets o tablas solo para lo genuinamente tabular
   (comparaciones, pasos numerados, fórmulas). Si el profesor hizo una
   pregunta y un alumno respondió (bien o mal), inclúyelo — es información
   real de la clase. No omitas nada técnico por parecer menor: prioriza
   completitud sobre brevedad.

3. "CONTEXTO — NO EXAMEN" — anécdotas, comentarios personales, referencias a
   experiencias laborales, o tangentes que no son contenido académico pero dan
   contexto.

4. "PENDIENTE / PRÓXIMA CLASE" — tareas asignadas, prácticas a entregar,
   fechas límite, o lo que se dijo que se verá en la siguiente sesión.

5. "PUNTOS CLAVE" (al final, no al principio) — 3 a 5 bullets cortos como
   repaso rápido, SOLO como cierre tras el detalle completo, nunca como
   sustituto de él.

No resumas de más en las secciones de "Temas" — ahí es donde debe estar todo
el detalle técnico, con el nivel de tecnicismo que usó el profesor/a. Escribe
en español.
```

Si el usuario faltó a esa clase, en vez de esto usa el patrón de
"clase reconstruida" — revisa `arquitectura-cliente-servidor/clase-05.html`
como ejemplo: se busca el material oficial del profesor (su sitio, PDFs) y se
marca con una nota visible de que no se asistió, sin sección de examen ni
contexto propios (no hay audio del que sacarlos).

## Paso 3 — Construir la página

Con el resultado de NotebookLM (o el material oficial reconstruido), arma
`materias/<slug>/clase-NN.html` siguiendo exactamente la plantilla descrita en
`CLAUDE.md` (detail-head, secciones `<details>` en prosa completa con `id`
único por sección tipo `cNN-slug`, contexto, pendiente, puntos-clave al
final). Usa el color de acento correcto de la tabla en `CLAUDE.md`. Mira 2-3
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
python3 scripts/build_search_index.py
git add -A
git commit -m "<Sigla>: agregar Clase NN (fecha) — resumen corto del contenido"
git push origin main
```

Commitea y pushea sin pedir confirmación adicional — es el flujo ya
establecido con el usuario (GitHub Pages se actualiza solo). Al final,
confírmale en un mensaje corto qué se agregó y qué sigue pendiente en la cola
si estaban procesando varias clases.
