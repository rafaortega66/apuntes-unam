# OAC-T02 — Producto punto · indicaciones

OAC (teoría) no usa Classroom. Fuente: NotebookLM, cuaderno OAC (audios de clase).
- Rutina de **suma de productos / producto punto** de dos vectores de punto flotante en ensamblador.
- Un puntero de entrada por vector (R0, R1), uno de salida (R2) y un contador (R3/R4).
- Avanzar los apuntadores **4 bytes** por elemento (float de 32 bits) y acumular en un registro de la **FPU**.
- Formato: **MicroPython con ensamblador en línea** (`@micropython.asm_thumb`). Fecha: no especificada.
