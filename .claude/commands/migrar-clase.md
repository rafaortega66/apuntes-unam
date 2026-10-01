---
description: Migrar la siguiente clase (o la indicada) al formato de estudio, de la más reciente hacia atrás
---

El usuario aprobó el formato de estudio (1 oct 2026) y pidió migrar **todas**
las clases en orden cronológico inverso, mezclando materias: la clase más
reciente primero (por fecha y hora de inicio según `assets/horario.json`), y
de ahí hacia atrás. Argumento opcional: $ARGUMENTS (una clase concreta o
"N clases").

## 1. Cuál sigue

```bash
git pull --ff-only origin main
python3 scripts/build_progress.py
```

Ordena `assets/progreso.json` por fecha + hora de inicio de la sesión,
descendente, y toma la primera con `formato != "estudio"`. (La página
`progreso.html` muestra cuántas lleva cada materia.)

## 2. Pedirlo a NotebookLM (Claude en Chrome)

Cuadernos (id en `notebook.google.com/notebook/<id>`):

| Materia | id | Audio de la clase N |
|---|---|---|
| ACS | 8b22fe2f-0c6c-4d5c-b331-95f4939e9309 | `ACS-ClaseN.m4a` (1–2: `clienteServidorClaseN.m4a`; 3–4: `AQS-ClaseN.m4a`) |
| ASI | 69be3e91-d77e-432b-952b-6607ac764c63 | `ASI-ClaseN.m4a` (1: `adminServInternet1Clase.mp3`; 2: `ASIClase2.m4a`) |
| FSE | 3a7a8c54-8fde-4e8d-ba14-2ee99d5e0d26 | `FSE-ClaseN.m4a` (1: `embebidosClase1.mp3`; 2: `FSEClase2.m4a`) |
| SIB | 93097ed6-0aa4-4806-86a5-717474969f03 | revisar la lista de fuentes |
| OAC | e22a6e3e-10b8-4db7-8da4-75a43bcdc9a3 | revisar la lista de fuentes |
| MD  | ee31f2d0-9d2f-4373-87fe-a06f2c554610 | revisar la lista de fuentes (tiene menos audios que clases) |
| RP  | b7b75532-3038-449a-9bc5-5f9fb476d0ed | revisar la lista de fuentes |

Ids de sección para el prompt:
`python3 scripts/migrar_formato_estudio.py --secciones materias/<slug>/clase-NN.html`

Prompt (una sola línea; pide ortografía con acentos en la respuesta):
pedir `=== EXAMEN` (líneas `- punto || evidencia`), un `=== SECCION <id>` por
sección con `SIMPLE:`, `ROMPE:`, `IMPORTA:`, `ERRORES:` (o NINGUNO), y
`=== PRUEBA` con 8 pares `P:`/`R:`. Exigir "usa SOLO la fuente <audio>" y
"no inventes nada". Genéralo con `python3 scripts/prompt_migracion.py <clase-NN.html> <audio> "<materia con profesor>" "<día fecha>" <N>`.

Trucos de la UI de NotebookLM que ya costaron tiempo:
- **No uses la acción `type`**: si la ventana de Chrome no tiene el foco, el
  texto se pierde o llega como basura. Mete el prompt con JS:
  `ta=document.querySelector('textarea[aria-label="Query box"]'); ta.focus(); ta.select(); document.execCommand('insertText', false, PROMPT)`
  (hay otro textarea de búsqueda web: usa siempre el aria-label).
- Envía con un **clic de mouse** sobre el botón de flecha (screenshot para
  ubicarlo); `btn.click()` por JS no funciona porque el botón sigue `disabled`
  para el framework.
- Para sacar la respuesta: el texto largo se trunca por JS. Cambia el
  `aria-label` del botón copiar del último `chat-message` a `COPIAR ULTIMA`,
  ubícalo con `find`, haz `scroll_to` + `left_click` y lee con
  `LANG=en_US.UTF-8 pbpaste`.

## 3. Aplicar y revisar

```bash
python3 scripts/migrar_formato_estudio.py materias/<slug>/clase-NN.html salida.txt
```

El script **no toca la prosa existente**: agrega meta `formato=estudio`, el
bloque de examen, los bloques por sección y "Ponte a prueba". Después
revisa el resultado: quita lo que no venga de la clase, nombres o apodos de
compañeros, y cualquier dato que contradiga la prosa ya verificada (la
prosa manda). Si el audio no está en NotebookLM, no migres esa clase:
anótala y sigue con la siguiente.

## 4. Publicar

```bash
python3 scripts/build_search_index.py
git add -A && git commit -m "<Sigla> Clase NN: formato de estudio" && git push origin main
```

Un commit por clase (el usuario quiere ver el avance en cada push).
