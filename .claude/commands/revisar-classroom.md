---
description: Cruzar Google Classroom (todas las materias) contra el sitio — detectar tareas/fechas/entregas que faltan o están desactualizadas
---

Vas a revisar el Google Classroom del usuario y cruzarlo contra el estado
actual del sitio de apuntes. Lee `CLAUDE.md` primero si no lo tienes en
contexto.

$ARGUMENTS puede traer una materia específica a revisar; si viene vacío,
revisa todas las que usan Classroom (todas excepto Arquitectura
Cliente-Servidor, que no lo usa).

## Paso 1 — Conectar el navegador

Intenta `tabs_context_mcp` con `createIfEmpty: true`. Si la extensión no
conecta:
- Explica al usuario los 3 pasos (extensión instalada, misma cuenta logueada,
  Chrome reiniciado si es la primera vez) y ofrece la alternativa: dale un
  prompt en español para que lo corra en una pestaña normal de claude.ai con
  la extensión activa ahí, y que te pegue el resultado de vuelta.
- No inventes contenido de Classroom si no lo pudiste ver — sé explícito
  sobre qué sí y qué no revisaste.

## Paso 2 — Recorrer cada curso

Para cada materia (usa el mapeo de slugs/siglas de `CLAUDE.md`), entra a su
curso de Classroom y registra, por cada assignment/material publicado:
- Título exacto tal como aparece en Classroom.
- Fecha de publicación y fecha límite (si tiene).
- Estatus: Turned in / Assigned / Missing / Done late, etc. — usa el texto
  literal que muestra Classroom, no lo traduzcas de forma ambigua.
- Si es "Material" (no "Assignment"), acláralo — no tiene fecha límite ni
  estatus de entrega.

No asumas que un curso de Classroom corresponde 1:1 a una materia del sitio
— a veces un solo curso de Classroom mezcla teoría + laboratorio (ya pasó con
"FSEm"), o no existe un curso separado para algo que en el sitio sí es una
materia aparte. Dilo explícitamente si notas un desajuste así.

## Paso 3 — Cruzar contra el sitio

Para cada materia, compara lo que acabas de ver contra:
- `materias/<slug>/entregas.html` — ¿lo que Classroom marca "Turned in" ya
  está registrado ahí? Si no, agrégalo (con enlace al PDF si lo tienes, o a
  la página de la clase si fue una entrega en vivo/presentación).
- `materias/<slug>/evaluacion.html` e `index.html` — ¿las fechas límite que
  puso el profesor en clase (capturadas en el audio) coinciden con las
  reales de Classroom? **Classroom manda sobre fechas de entrega** — si hay
  discrepancia, corrige el sitio y dilo explícitamente (ya pasó una vez: una
  fecha de ASI estaba mal por 8 días).
- Archivos: si Classroom tiene un adjunto (PDF, docx) que no está en
  `materias/<slug>/files/`, pregunta al usuario si quiere que lo descargues
  — descargar un archivo requiere su confirmación explícita cada vez (nombre,
  origen, tamaño), nunca lo hagas sin preguntar.

## Paso 4 — Reportar y actualizar

Preséntale al usuario, agrupado por urgencia (vencido / próximos días / sin
fecha fija), lo que encontraste. Aplica directo al sitio las correcciones de
fecha y los registros de entrega que sean inequívocos (Classroom lo confirma
con certeza); pregunta antes de tocar algo ambiguo (ej. una entrega que
Classroom no rastrea, como pasó con un reporte de laboratorio).

Al final:
```bash
python3 scripts/build_search_index.py
git add -A
git commit -m "Cruzar Classroom contra el sitio: <resumen de lo corregido>"
git push origin main
```
