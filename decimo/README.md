# decimo — archivos del semestre 2027-1

Un directorio por asignatura (sigla). Dentro:

```
<SIGLA>/
├─ <SIGLA>-Material/              ← material independiente del profesor (presentaciones, temario, formatos generales)
└─ <SIGLA>-<Categoría>/           ← Tareas, Practicas, Lab, Proyectos, Examenes… (ASI: una sola, ASI-Entregables)
   └─ <SIGLA>-XNN/
      ├─ <SIGLA>-XNN-indicaciones.pdf|.md   ← enunciado del profesor; si no hubo archivo, lo que dijo Classroom
      │                                       (y NotebookLM cuando Classroom era vago), con la fuente indicada
      ├─ <SIGLA>-XNN-entregables/           ← solo lo que se entregó (versión de Classroom)
      └─ <SIGLA>-XNN-adicionales/           ← lo que se usó y no se entregó: borradores, código de apoyo,
                                               datos-del-profesor/, version-previa/, otras-versiones-del-guion/
```

Códigos: `T` tarea · `P` práctica/lab · `Proy` proyecto · `E` examen · `Exp` exposición · `EC` ejercicio de clase · `R` reposición.
Números de dos dígitos, iguales a los de Classroom. Labs: FSE en `FSE/FSE-Lab/`, OAC (L+) en `OAC/OAC-Lab/` (con su `OAC-Lab-Material`).
Los libros no van aquí (repo privado `apuntes-unam-biblioteca`). Índice de todo: `INDICE.md` (`python3 scripts/indice_decimo.py`).
