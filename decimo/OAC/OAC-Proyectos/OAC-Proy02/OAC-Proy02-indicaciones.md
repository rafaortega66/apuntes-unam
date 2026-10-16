# OAC-Proy02 — Filtro digital IIR de segundo orden · indicaciones

OAC (teoría) no usa Classroom. Fuente: NotebookLM, cuaderno OAC (audios de clase).
- Implementar en ensamblador la **ecuación de diferencias de un filtro IIR de segundo orden**.
- Proponer coeficientes para una respuesta **subamortiguada**, con tiempo de muestreo **Ts = 0.05 s** y frecuencia f < 1/(2·Ts).
- Procesar una **onda cuadrada** generada por el programa, actualizando en cada iteración las entradas/salidas presentes y pasadas en arreglos de punto flotante, **sin loops dentro del ensamblador**.
- Formato: MicroPython con subrutina en ensamblador FPU (`@micropython.asm_thumb`). Fecha: no especificada.
