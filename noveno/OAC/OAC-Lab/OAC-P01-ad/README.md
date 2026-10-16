# Práctica 1 — Introducción a las herramientas de desarrollo de los FPGAs

Organización y Arquitectura de Computadoras — UNAM, Facultad de Ingeniería
Ortega de la Paz Rafael | 420054085

## Contenido de esta carpeta

- `Practica1_Reporte.docx` / `Practica1_Reporte.pdf` — reporte final (carátula, introducción, desarrollo, conclusión, referencias).
- `capturas/` — las 5 capturas usadas en el reporte: diagrama esquemático, compilación exitosa, simulación base (RESET=0, reloj 10ns), variación RESET=1, variación reloj 20ns.
- `codigo/run_sim.do` — script de simulación funcional para Questa, ya corregido (ver notas abajo).

## Circuito

Contador binario de 4 bits con el integrado 74193 sobre una tarjeta Altera Cyclone IV E (EP4CE22F17C6N):
- CLK → UP
- RESET → CLR
- VCC → LDN y DN (deshabilita carga paralela y conteo descendente)
- QA, QB, QC, QD → salidas A, B, C, D

## Notas del toolchain (por si se repite el setup en otra máquina)

- Quartus Prime Lite Edition 21.1 es la última versión gratuita con soporte para Cyclone IV.
- Questa se instala en la carpeta `questa_fse` (con "s"), no `questa_fe` — detalle que causó errores de ruta.
- Quartus genera automáticamente un `.do` con las banderas `-novopt -c`, que ya no funcionan en Questa 2021.2. La solución es usar un `.do` propio (`run_sim.do`, incluido en `codigo/`) con `-voptargs="+acc"` sin `-c`, más la línea `add wave -radix binary /*` antes de `run -all`, para que las señales se grafiquen automáticamente.
- La licencia gratuita de Questa Starter Edition (SW-QUESTA) se tramita en altera.com/SSLC, ligada al NIC ID (MAC address, sin guiones) del equipo. Sobrevive reinstalaciones de Windows porque depende del hardware, no del sistema operativo. Hay que apuntar la variable de entorno `LM_LICENSE_FILE` al archivo `.dat` de licencia.
- Flujo de simulación: editar `Waveform.vwf` en Quartus → guardar → correr "Simulation > Run Functional Simulation" en Quartus (da un error esperado por el `-novopt`, se ignora; solo sirve para regenerar `practica1.vo` y `Waveform.vwf.vt`) → cerrar Quartus → correr `vsim.exe -do run_sim.do` desde la carpeta `simulation/qsim` del proyecto.
