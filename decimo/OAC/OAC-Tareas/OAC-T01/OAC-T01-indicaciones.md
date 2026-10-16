# OAC-T01 — Raíz cuadrada en ensamblador · indicaciones

OAC (teoría) no usa Classroom. Fuente: NotebookLM, cuaderno OAC (audios de clase).
- Implementar la **raíz cuadrada en ensamblador**.
- Método propuesto al inicio: **restas sucesivas de impares consecutivos** (√25: 25−1=24, 24−3=21, 21−5=16, 16−7=9, 9−9=0 → 5 restas → resultado 5), obteniendo parte entera y residuo.
- Después se mostró la versión directa con la **FPU** de la Raspberry Pi Pico 2 (instrucción de raíz cuadrada de punto flotante).
- Formato: **MicroPython con ensamblador en línea** (`@micropython.asm_thumb`). Fecha: no especificada.
