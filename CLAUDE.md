# Este repo: identidad y flujo de trabajo

Este archivo lo carga Claude Code automáticamente al abrir este proyecto,
**en cualquier máquina y cualquier sesión** — es la fuente de verdad que no
depende de la memoria de una conversación particular. Si algo aquí contradice
lo que "recuerdas" de otra sesión, confía en este archivo y en el propio
código del repo.

## Qué es esto

Sitio estático de **apuntes del semestre 2027-1** (Facultad de Ingeniería,
UNAM) del usuario, hosteado gratis en GitHub Pages:
`https://rafaortega66.github.io/apuntes-unam/`. Todo son archivos HTML reales
+ PDFs; nada corre en sandbox. Repo: `rafaortega66/apuntes-unam` (remote
`origin`, branch `main`).

**Las 9 materias** (slug de carpeta · sigla que usa el usuario · color de acento):

| Materia | Slug | Sigla | Color |
|---|---|---|---|
| Administración de Servicios de Internet | `administracion-de-servicios-de-internet` | ASI | `#7C9CD6` (índigo) |
| Arquitectura Cliente-Servidor | `arquitectura-cliente-servidor` | ACS | `#E8735C` (coral) |
| Fundamentos de Sistemas Embebidos | `fundamentos-de-sistemas-embebidos` | FSE | `#A98BD1` (ciruela) |
| Lab. de Fundamentos de Sistemas Embebidos | `lab-de-fundamentos-de-sistemas-embebidos` | Lab FSE | `#E8735C` |
| Lab. de Organización y Arq. de Computadoras | `lab-de-organizacion-y-arquitectura-de-computadoras` | Lab OAC | `#7C9CD6` |
| Minería de Datos | `mineria-de-datos` | MD | `#A98BD1` |
| Organización y Arquitectura de Computadoras | `organizacion-y-arquitectura-de-computadoras` | OAC | `#45B8A8` (verde) |
| Reconocimiento de Patrones | `reconocimiento-de-patrones` | RP | `#45B8A8` |
| Seguridad Informática Básica | `seguridad-informatica-basica` | SIB | `#E8735C` |

ACS **no usa Google Classroom** (profesor tiene su propio sitio en
`cromanzamitiz.github.io/arquitectura-cliente-servidor/`); las otras 8 sí.

## Horario oficial (confirmado por el usuario el 16 sep 2026 — fuente de verdad)

Patrón fijo semanal, **no inferir de memoria ni de "cuadra con el patrón de
fechas anteriores"** — usar esta tabla directamente:

| Día | Materias (en orden) |
|---|---|
| Lunes | RP → OAC → FSE → ASI |
| Martes | SIB, MD |
| Miércoles | OAC, FSE, ASI |
| Jueves | SIB, MD, ACS |
| Viernes | RP |

Lab FSE y Lab OAC **no están en este patrón semanal** — sus prácticas se
agendan aparte, no son clase teórica recurrente. Si una fecha propuesta para
Clase de RP/OAC/FSE/ASI/SIB/MD/ACS no cae en el día que le toca según esta
tabla, es un error — decirlo explícitamente y pedir confirmación antes de
usarla.

## El origen de todo el contenido: nunca se inventa nada

El usuario graba el audio de cada clase. Ese audio se procesa en **Gemini
NotebookLM** con un prompt que Claude genera (ver `/nueva-clase` abajo), y el
resultado se pega de vuelta a Claude para convertirlo en la página HTML.
**Regla no negociable: todo el contenido técnico, fechas, nombres y citas
viene de una fuente real (audio de la clase, material del profesor, o
Classroom) — nunca se fabrica ni se aproxima.** Si algo no está confirmado,
se dice explícitamente en vez de inventarlo.

Cuando el usuario faltó a una clase, la página se reconstruye a partir del
**material oficial del profesor** (su sitio, PDFs, diapositivas) y se marca
con una nota visible de "no asistí" — ver `arquitectura-cliente-servidor/clase-05.html`
como ejemplo de este patrón.

## Estructura de cada materia

```
materias/<slug>/
  index.html        ← temario oficial (vista "Por tema") + lista de clases (vista "Por clase")
  evaluacion.html    ← criterios de evaluación, tareas, rúbricas (si existe)
  material.html      ← TODOS los archivos que dio el profesor/a (guiones, diapositivas, plantillas)
  entregas.html      ← TODO lo que el usuario ya entregó (con enlace al PDF/código o a la clase)
  clase-NN.html      ← apuntes completos de cada clase (ver plantilla abajo)
  files/             ← archivos del profesor (los que se listan en material.html)
  files/entregas/    ← archivos que el usuario ya entregó (los que se listan en entregas.html)
```

**Regla de oro de archivos (site-wide desde el 14 sep 2026):** todo archivo del
profesor va en `files/` (raíz de la materia) y se lista en `material.html`;
todo archivo que el usuario haya entregado va en `files/entregas/` y se lista
en `entregas.html`. Nunca mezclar los dos. El `index.html` de cada materia
tiene siempre estas tarjetas, en este orden: Evaluación (si existe) →
Material → Entregas → (otras específicas de la materia, ej. Programas de ACS).

`index.html` tiene un botón fijo "Por tema / Por clase" (JS en `assets/app.js`,
persiste en `localStorage`). **Por tema** = mapa del temario oficial que se va
pintando de azul conforme se cubre en clase (con enlace a la clase que lo vio).
**Por clase** = bitácora cronológica, una tarjeta por clase.

### Plantilla de una página `clase-NN.html`

**Cambio de formato (desde el 16 sep 2026):** el usuario dejó claro que las
cajas "En corto" / "🎯 Para el examen" como resumen principal NO sirven para
estudiar — se perdía información real de la clase. El objetivo ahora es que
el apunte se pueda leer y "revivir" la clase completa, con prosa bien
redactada y nada del contenido técnico recortado. Ver cualquier `clase-*.html`
**anterior** a esta fecha como ejemplo del formato viejo (ya no se usa para
clases nuevas); no reprocesar las viejas a menos que el usuario lo pida
explícitamente.

Secciones de una página nueva, en este orden:
1. `detail-head` — número de clase, profesor, fecha, resumen de una línea.
2. Uno o más `<details class="section-block sec" id="cNN-slug">` — el
   contenido **completo en prosa**, en el mismo orden en que se explicó en
   clase, con el mismo nivel técnico que dio el profesor (definiciones
   exactas, ejemplos resueltos con sus números/pasos reales, preguntas y
   respuestas en vivo). Bullets/tablas solo para lo genuinamente tabular
   (comparaciones, pasos, fórmulas) — el resto en párrafos. Esta es la parte
   que antes iba comprimida en "En corto"/"Para el examen"; ahora es el
   cuerpo principal, sin recortar.
3. `<details ... id="cNN-contexto">` — anécdotas, tangentes, no-examen.
4. `<details ... id="cNN-pendiente">` — tareas asignadas, próxima clase.
5. `.puntos-clave` (opcional, al final de todo) — 3-5 bullets cortos de
   repaso, solo como cierre después del detalle completo, nunca como
   sustituto.

Los `id` en los `<details>` son importantes: el buscador global enlaza
directo a ellos (ver más abajo).

## El buscador global — hay que mantenerlo actualizado

El sitio tiene un buscador (botón 🔍 flotante, tecla `/`) que indexa las 9
materias. El índice es `assets/search-index.json`, generado por:

```bash
python3 scripts/build_search_index.py
```

**Correr este script y commitear el JSON actualizado cada vez que se agregue
o edite una página.** Si se te olvida, el buscador sigue funcionando pero con
contenido desactualizado — no rompe nada, pero hay que evitarlo.

## Flujo para agregar una clase nueva

Usa el comando **`/nueva-clase`** (`.claude/commands/nueva-clase.md`) — guía
todo el proceso: prompt para NotebookLM → construir la página → actualizar
temario/vista-por-clase → regenerar buscador → commit → push.

Resumen si se hace a mano:
1. Confirmar materia, número de clase y fecha real (cuidado: las fechas que
   dicta el usuario de memoria a veces no cuadran — corroborar contra el
   patrón de días de la materia y contra lo ya registrado en el sitio).
2. Dar el prompt de NotebookLM (plantilla en `/nueva-clase`).
3. Con el resultado, construir `clase-NN.html` siguiendo la plantilla de arriba.
4. Actualizar `index.html` de la materia: badge del tema ("Clases 01–NN"),
   marcar subtemas como vistos (`<span class="seen">`), agregar la tarjeta en
   la vista "Por clase" (`a.clase-link`).
5. `python3 scripts/build_search_index.py`
6. `git add -A && git commit -m "..." && git push origin main` — **hacerlo
   sin pedir confirmación cada vez**, es el flujo establecido del usuario
   (GitHub Pages se actualiza solo con el push).

## Flujo para cruzar contra Google Classroom

Usa el comando **`/revisar-classroom`** (`.claude/commands/revisar-classroom.md`)
cuando el usuario quiera saber qué falta, qué ya entregó, o detectar
discrepancias de fechas entre lo dicho en clase y lo real en Classroom (ya
pasó una vez: una fecha de entrega de ASI estaba mal por 8 días porque la
extendieron en Classroom y no se mencionó en el audio de clase — Classroom es
la fuente de verdad para fechas de entrega, el audio de clase es la fuente de
verdad para contenido académico).

Requiere la extensión **Claude en Chrome** conectada (`claude.ai/chrome`,
misma cuenta, Chrome reiniciado tras instalar). Si no conecta, dáselo al
usuario como prompt para que lo corra en una pestaña de claude.ai normal y te
pegue el resultado.

Descargar un archivo de Classroom (adjuntos, PDFs) requiere confirmación
explícita del usuario cada vez (nombre del archivo, origen, tamaño) — no es
una acción que se pueda automatizar sin permiso, por regla del harness.

## Registrar entregas

Cuando el usuario entrega algo (o Classroom confirma "Turned in"), agregar
una fila a `entregas.html` de esa materia con: qué es, cuándo, y enlace al
PDF (en `files/entregas/` si es un archivo nuevo) o a la página de la clase
donde se presentó (si fue una exposición en vivo, no un PDF).

## Memoria persistente (fuera de este repo)

Hay memoria de proyecto en
`/Users/rafa/.claude/projects/-Users-rafa-Desktop-site/memory/` que
complementa esto con contexto de sesión a sesión (quién es el usuario, su
equipo/proveedor asignado en cada proyecto, etc.) — revisarla al inicio pero
tratar este `CLAUDE.md` como la referencia estructural definitiva del repo.
