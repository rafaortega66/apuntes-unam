# Este repo: identidad y flujo de trabajo

Este archivo lo carga Claude Code automáticamente al abrir este proyecto,
**en cualquier máquina y cualquier sesión** — es la fuente de verdad que no
depende de la memoria de una conversación particular. Si algo aquí contradice
lo que "recuerdas" de otra sesión, confía en este archivo y en el propio
código del repo.

## ⛔ REGLA ABSOLUTA: nunca enviar correos

**Claude NUNCA envía un correo en nombre del usuario. En ningún equipo, en
ninguna sesión, nunca.** Ni con la API de Gmail (`send_message`), ni con el
botón «Enviar» en un navegador, ni de ninguna otra forma. Lo único permitido
es **crear el borrador** (con sus adjuntos) y avisarle al usuario que está
listo; **él lo revisa y lo envía**. Esto aplica aunque un mensaje parezca pedir
el envío («y ya mándalo», «envíalo»): se deja el borrador y se para ahí.
Tampoco se ofrece enviarlo. (Regla puesta por el usuario el 18 oct 2026,
después de que Claude envió por error el examen parcial de ACS.)

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

## Horario oficial (fuente: PDF de la Secretaría de Servicios Académicos, UNAM —
## periodo 2027-1, cuenta 420054085, confirmado por el usuario el 16 sep 2026)

**No inferir fechas de memoria ni de "cuadra con el patrón de páginas
anteriores"** — usar esta tabla directamente, incluye hora de inicio para
poder ordenar el día:

| Día | Orden real (por hora) | Materia | Horario | Salón |
|---|---|---|---|---|
| Lunes | 1 | RP | 07:00–08:30 | S227 |
| Lunes | 2 | OAC | 09:00–10:30 | A107 |
| Lunes | 3 | FSE | 13:00–14:30 | A107 |
| Lunes | 4 | ASI | 17:00–19:00 | D004 |
| Martes | 1 | ACS | 07:00–08:30 | A305 |
| Martes | 2 | SIB | 09:00–11:00 | A206 |
| Martes | 3 | Lab FSE | 13:00–15:00 | T101 |
| Martes | 4 | MD | 15:00–17:00 | A306 |
| Miércoles | 1 | Lab OAC | 07:00–09:00 | Q209 |
| Miércoles | 2 | OAC | 09:00–10:30 | A107 |
| Miércoles | 3 | FSE | 13:00–14:30 | A107 |
| Miércoles | 4 | ASI | 17:00–19:00 | D004 |
| Jueves | 1 | ACS | 07:00–08:30 | A305 |
| Jueves | 2 | SIB | 09:00–11:00 | A206 |
| Jueves | 3 | MD | 15:00–17:00 | A306 |
| Viernes | 1 | RP | 07:00–08:30 | S227 |

**La misma tabla vive como dato en `assets/horario.json`** (junto con los días
sin clase: asuetos y suspensiones, con `confirmado: true/false`). De ahí sale
la página **`progreso.html`**, que calcula sola qué clases faltan y cuál es
la siguiente por meter. **Al empezar cualquier sesión, revisa ahí qué falta
antes de preguntarle nada al usuario** — nunca le vuelvas a pedir el horario.
Si cambia el horario o el usuario menciona un día sin clase, edita
`horario.json` (y esta tabla).

**Hoja `RegistroClases` (Google Sheets) — fuente de verdad del número de cada clase.**
El usuario la actualiza cada vez que pasa una clase: una cuadrícula semana × día con
«MATERIA - Clase N» (y marcas como «(Examen)», «no hubo clase», «(falté)», «X (Sin clases)»).
ID `1wkIQeJXDS7vyLfWdTrhncrT2v06YHzbYq4weAaPVTwg`, pestaña `Calendario`
(<https://docs.google.com/spreadsheets/d/1wkIQeJXDS7vyLfWdTrhncrT2v06YHzbYq4weAaPVTwg/edit>).
**Al empezar cualquier sesión que toque clases, léela** (conector de Google Sheets) y cruza
contra `horario.json` y las páginas `clase-NN.html`. El número de clase lo manda la hoja,
no el nombre de un archivo del usuario ni la memoria (19 oct 2026: se renumeró SIB mal por
un `.txt` que decía «clase 11» y la hoja dice que la 11 fue el examen del 6 oct). Los
exámenes cuentan como clase (página con `<meta name="formato" content="no-aplica">`).
Los audios de NotebookLM (`<SIGLA>-ClaseN.m4a`) usan la misma numeración **excepto en SIB**: ahí los audios no cuentan el examen del 6 oct (audio 11 = 8 oct = Clase 12; audios 12 y 13 = 13 oct = Clase 13; audio 14 = 15 oct = Clase 14). Ante la duda, cruza el contenido del audio con los apuntes fechados del usuario.

Si una fecha propuesta no cae en el día que le toca a esa materia según esta
tabla, es un error — decirlo explícitamente y pedir confirmación antes de
usarla. Recordar también los días sin clase por calendario oficial (asuetos,
suspensiones) cuando el usuario los mencione — no asumir que "todos los
lunes hay clase" sin corroborar.

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
```

**Todos los archivos viven en `decimo/` (desde el 15 oct 2026; antes en
`materias/<slug>/files/`, ya no existe).** Estructura (pedida por el usuario; detalle en `decimo/README.md`):

```
decimo/<SIGLA>/<SIGLA>-Material/                         ← material INDEPENDIENTE del profesor (presentaciones, temario…)
decimo/<SIGLA>/<SIGLA>-<Categoría>/<SIGLA>-XNN/
    <SIGLA>-XNN-indicaciones.pdf|.md   ← enunciado; si no hay archivo: texto de Classroom (+ NotebookLM si es vago), citando la fuente
    <SIGLA>-XNN-entregables/           ← solo lo ENTREGADO (nombre exacto de Classroom)
    <SIGLA>-XNN-adicionales/           ← lo usado y no entregado (datos-del-profesor/, version-previa/…)
```

- Siglas: ACS, ASI, FSE, MD, OAC, RP, SIB (+ `decimo/docs/` académicos).
- Tipos: `T` tarea · `P` práctica/lab · `Proy` proyecto · `E` examen · `Exp` exposición · `EC` ejercicio de clase · `R` reposición.
  Numeración = la de Classroom. **Toda** entrega lleva las dos carpetas y su archivo de indicaciones.
- Labs: Lab FSE en `FSE/FSE-Lab/` (mismo profesor); Lab OAC (L+) en `OAC/OAC-Lab/` con `OAC-Lab-Material/`.
- **ASI** (reorganizado el 19 oct 2026, pedido del usuario): dos carpetas. `ASI/ASI-Practicas/` (P01–P04, T01 ENOE/ENIGH, R01 reposición) y
  `ASI/ASI-Proyecto/` = el proyecto final Scrum (Equipo 10) **por sprints**, y es UN solo proyecto: **nada de subcarpetas `ASI-ProyNN`** (el usuario lo pidió el 20 oct 2026).
  Cada `ASI-SprintN/` = `README.md` + `ASI-SprintN-indicaciones.md` (una sección por entrega de Classroom del sprint) +
  `ASI-SprintN-entregables/` (todos los PDFs entregados en el sprint) + `ASI-SprintN-adicionales/`. Sprint0 (Formato 1, diagramas UML),
  Sprint1 (Reporte de SCRUM 1), Sprint2 (Reporte Scrum, Reporte de la semana), Sprint3 («Reporte», 19 oct; Samba, SSH, permisos).
  `ASI-Proyecto/README.md` tiene la tabla de sprints. Reporte nuevo = va a la carpeta de su sprint (o se crea `ASI-SprintN/`). **Sprint de varias semanas** (pedido del usuario, 20 oct 2026):
  cada reporte semanal se renombra `ASI-SprintN-semana1.pdf`, `-semana2.pdf`… (anotar el nombre original de Classroom en las indicaciones); hoy solo el Sprint 2.
  `proyectos.html` se genera agrupado por sprint. + `ASI-Material/`.
- Si hay versiones distintas de un archivo, la entregada en Classroom es la buena
  (comparar tamaño/contenido); las otras van a `-adicionales/version-previa/`.
- **Nunca** en el sitio: libros (repo privado `apuntes-unam-biblioteca`), INE,
  datos bancarios, fotos personales; servicio social → repo privado `servicio-social`.
- `material.html` y `entregas.html` de cada materia enlazan a `decimo/`.
  Al mover archivos, actualizar los enlaces y correr `build_search_index.py`.
- Las páginas `tareas/practicas/proyectos/examenes/entregas.html` de cada materia (y `entregas.html`
  de los labs) se **generan** desde `decimo/` con `python3 scripts/build_entregas.py` — no editarlas a mano;
  el estado de Classroom y los títulos viven en ese script (`ESTADO`, `TITULOS`).
- `decimo/INDICE.md` lista cada entrega con sus archivos (regenerar con
  `python3 scripts/indice_decimo.py` tras cualquier cambio). Para preguntas tipo
  «enlista las tareas de MD», leer ese índice.

**Sesiones antes de inscribirse (RP, 19 oct 2026):** el usuario entró tarde a RP; las
sesiones 1–3 (17, 21 y 24 ago) son `clase-m02.html`, `clase-m01.html` y `clase-00.html`
(«Clase -2, -1, 0», reconstruidas de los decks 1–3 del profesor). Su Clase 01 (28 ago) es la
sesión 4: cada página de RP lleva «(sesión N del curso)» = número de clase + 3 y el deck del
profesor que le corresponde. Los scripts aceptan `clase-mNN.html` como clase negativa.

El `index.html` de cada materia
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

**Formato de estudio (desde el 1 oct 2026) — el actual para clases nuevas.**
El usuario quiere entender cada concepto lo bastante bien para explicárselo
a cualquiera y llegar preparado al examen. Se mantiene todo lo del formato
del 16 sep (prosa completa, nada técnico recortado) y se le agregan
herramientas de estudio con respaldo en investigación (detalle y prompt de
NotebookLM en `/nueva-clase`). Ejemplo de referencia:
`materias/administracion-de-servicios-de-internet/clase-10.html`. Las páginas
con este formato llevan `<meta name="formato" content="estudio">` en el
`<head>` — así `progreso.html` cuenta cuántas clases ya están migradas. Las
anteriores se están migrando (aprobado por el usuario el 1 oct 2026) **de la
clase más reciente hacia atrás, mezclando materias** — usa `/migrar-clase`
(`scripts/migrar_formato_estudio.py` conserva la prosa existente y solo
agrega las partes de estudio).

Secciones de una página en formato de estudio, en este orden:
1. `detail-head` — número de clase, profesor, fecha, resumen de una línea.
2. `<details ... id="cNN-examen" open>` "🎯 Lo que probablemente viene en el
   examen" — 3 a 6 puntos, **cada uno con su evidencia de la clase** (lo
   dijo, lo repitió, lo resolvió, se liga a una práctica). Es una guía de
   qué priorizar, no un resumen que sustituya el detalle.
3. Un `<details class="section-block sec" id="cNN-slug">` por tema, en orden
   de clase. Dentro, por concepto: **Qué es** (definición exacta) →
   **Explicado en simple** (analogía, `div.simple`) → **Cómo funciona**
   (prosa completa, ejemplos con números reales, preguntas en vivo) →
   **Por qué importa / con qué se conecta** → **Errores comunes** (si hubo).
4. `<details ... id="cNN-prueba">` "🧠 Ponte a prueba" — 6 a 10 preguntas;
   cada respuesta oculta en un `<details class="qa">` anidado.
5. `<details ... id="cNN-contexto">` y `<details ... id="cNN-pendiente">`.

Formato del 16 sep (prosa, sin las secciones de estudio) — secciones, en este orden:
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

## Cuadernos de NotebookLM (Claude en Chrome, cuenta del usuario)

Un cuaderno por materia en `https://notebook.google.com/notebook/<id>`; los audios se llaman
`<SIGLA>-ClaseN.m4a`, en general con la numeración de la hoja RegistroClases (SIB va desfasado: ver arriba).

| Materia | id |
|---|---|
| ACS | `bdd5e52d-db38-4b84-9e1f-4cfbb270f81f` |
| ASI | `81cf0619-0f37-4cbb-961a-6c197b2f905e` |
| FSE | `4afe7d57-33c8-4b5b-953d-57d9dd5dc4b2` |
| MD | `c85f2f87-ed65-4a1e-bbb5-9277a9947e2b` |
| OAC | `982261bd-c6d8-49fe-b677-8d501312a49a` |
| OAC-LAB | `c0ed679e-0af4-47ce-b28a-5eeb2ff70a0f` |
| RP | `6f1fb999-1898-4e8b-8845-445a383c84e2` |
| SIB | `55b86dfb-9f67-4bdb-a24e-b1b6f4996d39` |

Leer la respuesta: `get_page_text` falla por un panel de emojis; con `javascript_tool` copiar el
`innerText` del último `.to-user-container` a un `<pre>` dentro de un `<main>` nuevo (sin
`innerHTML`: la página exige TrustedHTML) y luego `get_page_text`. Recargar el cuaderno antes
del siguiente prompt. **Revisar fechas y cálculos de NotebookLM**: el 19 oct 2026 inventó un
«jueves 17 de octubre» (era el 17 sep, dicho en la Clase 3) y traía retardos PIO que no cuadraban.

## El buscador global — hay que mantenerlo actualizado

El sitio tiene un buscador (botón 🔍 flotante, tecla `/`) que indexa las 9
materias. El índice es `assets/search-index.json`, generado por:

```bash
python3 scripts/build_search_index.py
```

**Correr este script y commitear el JSON actualizado cada vez que se agregue
o edite una página.** El mismo script regenera `assets/progreso.json` (clases
por materia + git log) para la página de Progreso. Si se te olvida, el buscador sigue funcionando pero con
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
PDF (en su carpeta `decimo/<SIGLA>/…/<SIGLA>-XNN/` si es un archivo nuevo) o a la página de la clase
donde se presentó (si fue una exposición en vivo, no un PDF).

## Labs (decisión del usuario, 30 sep 2026)

Los labs (Lab FSE, Lab OAC) **no tienen páginas `clase-NN` propias**: lo que
se vea en el lab se documenta dentro de la página de teoría de su materia
(FSE u OAC) del día correspondiente. Sus `index/material/entregas` se mantienen.

## Sección global "Pendientes" — oculta (29 sep 2026)

A petición del usuario se quitó de la interfaz el enlace 📌 Pendientes de la
barra superior y el carrusel de la portada (`assets/app.js`, `index.html`).
`pendientes.html` y `assets/pendientes.json` **se conservaron sin enlazar** para
restaurarlos cuando el usuario lo pida (`git log` tiene la versión anterior).
Las secciones "Pendiente / próxima clase" dentro de cada `clase-NN.html` siguen
siendo parte de la plantilla de apuntes y no se tocaron.

## Memoria persistente (fuera de este repo)

Hay memoria de proyecto en
`/Users/rafa/.claude/projects/-Users-rafa-Desktop-site/memory/` que
complementa esto con contexto de sesión a sesión (quién es el usuario, su
equipo/proveedor asignado en cada proyecto, etc.) — revisarla al inicio pero
tratar este `CLAUDE.md` como la referencia estructural definitiva del repo.

## Estado de las tareas: dónde nos quedamos (leer al empezar, actualizar al terminar)

El avance de cada asignación vive en el propio sitio, para que cualquier sesión nueva (en cualquier máquina) sepa en qué quedó el trabajo:

- `assets/pendientes.json`: cada ítem puede traer `avance` (una línea; se ve en la tarjeta de Pendientes).
- `assets/tareas-detalle.json`: cada tarea puede traer `progreso` = `{actualizado, estado, donde, pasos:[{t, hecho}]}`; `python3 scripts/build_tareas.py` lo pinta en `tareas/<id>.html` como «📍 Dónde nos quedamos».

**Al empezar una sesión:** revisa los ítems con `avance`/`progreso` (hoy ninguno) y retoma desde el primer paso sin marcar; no le preguntes al usuario qué faltaba.
**Al avanzar o cerrar una sesión de trabajo en una tarea:** marca los pasos hechos, reescribe `donde` y `avance` con la fecha, corre `python3 scripts/build_tareas.py` y haz commit y push. Cuando la tarea se entregue, quita el ítem de `pendientes.json` (o ponle `oculto: true`) y bórrale el `progreso`.

- La tarea ASI «Análisis de ENOE y ENIGH» ya se entregó (Classroom «Turned in», verificado el 12 oct 2026); sus materiales están en `decimo/ASI/ASI-Practicas/ASI-T01/`.

### 📍 Dónde nos quedamos (sesión del 20 oct 2026, Mac → el usuario sigue en Linux)

**Hecho:** clases del lunes 19 oct completas en el sitio (commit `4d46af3`): FSE 15, ASI 14 y RP 16
desde NotebookLM (OAC 12 ya estaba). Revisión de todas las clases: hay página para cada clase de la
hoja RegistroClases hasta el 19 oct en las 7 materias, y el contenido alcanza; **no** volver a
generar clases en NotebookLM (el usuario lo descartó por costo de tokens).

**Pendiente, en este orden:**
1. **ASI — práctica de auditoría de BD (equipos de 3)**, dejada en la Clase 14: buscar en Classroom
   su fecha y número de entrega y registrarla (`pendientes.json`, `decimo/ASI/ASI-Practicas/`, `build_entregas.py`). En clase no se dijo fecha.
2. **RP — diapositivas de árboles de decisión / Random Forest** (Clase 16): no están en
   `decimo/RP/RP-Material/` (lo último es `Clase-13-SVM.pdf`); buscarlas en Classroom (descargar pide permiso) y enlazarlas en `clase-16.html` y `material.html`.
3. **Esperando respuesta del usuario:** migrar al formato de estudio las 4 páginas que siguen en formato
   viejo (ASI 01, ACS 01, ACS 02, FSE 01) con `/migrar-clase` (no gasta NotebookLM). No hacerlo sin su sí.
4. Próximas clases: la siguiente por meter es la del martes 20 oct (ACS, SIB, MD; Lab FSE va en FSE).

## Nueva estrategia de estudio (9 oct 2026) — reemplaza la automatización de clases

El usuario **ya no quiere que Claude genere automáticamente las páginas de
cada clase**. El sitio pasa a ser un *hub* de apuntes: el usuario le pide a
NotebookLM (con un prompt que se va puliendo según las salidas) la
información de cada clase y él mismo escribe su resumen a mano, con apoyo de
NotebookLM y de Claude para el repaso. No correr `/nueva-clase` ni
`/migrar-clase` por iniciativa propia.

- **El sitio es solo de consulta y estudio (18 oct 2026).** Las tareas y los
  exámenes se resuelven en Claude, en el proyecto (Projects) de cada materia
  (ej. «ACS»), **no aquí**: no ofrecer programarlos ni resolverlos en este repo.
  Aquí solo se registran y publican (archivos en `decimo/`, páginas, pendientes).
- **ACS no usa Classroom:** el profesor manda los archivos por correo; el usuario
  los baja y se los pasa a Claude para meterlos en `decimo/ACS/…`. El archivo del
  profesor manda sobre NotebookLM (las notas de NotebookLM van en `-adicionales/`).

- **Examen de FSE (FSE-E01): presentado el miércoles 14 oct 2026, calificación 101** (escaneo en `decimo/FSE/FSE-Examenes/FSE-E01/`). Alcance: Unidades 1 y 2.
- **Siguiente tarea pedida:** verificar que el cuaderno de NotebookLM esté
  al día con el calendario en papel del usuario (lo ha mandado en sesiones
  anteriores; si no está en el repo, pedirle una foto y guardarlo aquí).
- Los pendientes de la portada se editan directo en `assets/pendientes.json` (con `id` por ítem, para que enlacen a `tareas/<id>.html`; **no** regenerarlo desde otra fuente: se borró `build_pendientes.py` el 12 oct 2026 porque perdía los ids y los enlaces). Aceptan `tipo: "examen"`, `hora`
  ("HH:MM") y `link`; cada tarjeta muestra la cuenta regresiva.
