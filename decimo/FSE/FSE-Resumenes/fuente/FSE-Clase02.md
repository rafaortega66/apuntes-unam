% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 2 · RISC vs. CISC en PIC, AVR, ESP32, RP2040, Cortex-M e Intel
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · lunes 31 ago 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. RISC vs. CISC
| | RISC (ARM, PIC, AVR) | CISC (Intel x86) |
|---|---|---|
| Memoria | Programa y datos separados (Harvard) | Unificada; instrucciones operan sobre memoria |
| Catálogo | ~1000 instrucciones, ancho fijo | Millones de combinaciones, ancho variable |
| Estilo | Load/store por un registro | Instrucciones que hacen varias cosas |
| Costo | Verboso, pero el **pipeline** lo compensa | Compacto, decodificador caro |
Todos los Intel de escritorio heredan del 8086. Error común: decir que el 8080 era RISC.

## 2. PIC (RISC de 8 bits)
- Flash separada de la RAM; un bus de datos une RAM, registro **W**, control, puertos y periféricos (un ciclo).
- Bus de datos de 8 bits → **2⁸ = 256 bytes**; bus de programa de 14 bits → **2¹⁴ = 16 K**. Potencias: 2¹⁰ = 1024 … 2¹⁴ = 16384.
- Ejemplo: robot que resolvía un laberinto con grafos y caminos mínimos en 256 bytes.
!!! Pila de 8 niveles (examen)
La pila **no está en la RAM**: es un registro aparte de **8 niveles**. Un `fact(9)` recursivo la desborda: **no se usa recursión** en el PIC16F84.
- ALU: entrada izquierda por multiplexor; derecha cableada a **W**. A + B = cargar A en W, W = W + B, escribir W (3 accesos).
- Expansión: 2 puertos de direcciones + 1 de datos → 2¹⁶ = 64 KB; con el puerto A (5 bits) → 21 bits, más de 1 MB; la RAM interna queda como caché.

## 3. AVR (Arduino)
RISC con **32 registros** de propósito general (no un solo W); la ALU trabaja sobre registros; hasta 8 K de RAM; hasta **50 MHz**. SRAM = **estática** (no "Status RAM").

## 4. ESP32
- Núcleo RISC + RF (WiFi), reloj de tiempo real, sensores, aceleración y cripto por hardware.
- La ROM **no** es memoria de programa (funciones del sistema, JTAG, caché).
- Datos e instrucciones revueltos en SRAM/PSRAM; una interfaz los separa en colas de instrucciones y datos.
- **SHA por hardware** cifra el flujo sin cargar la CPU (llaves de AWS de 256 bits). ISA Xtensa / RISC-V.

## 5. Caché
- "**Almacenamiento en proxy**": copiar lo frecuente a un medio más rápido y cercano.
- HDD ≈ 100 MB/s vs. DDR ≈ 500 MB/s (5×), más el retardo mecánico del disco.
!!! Cuello de botella CPU–RAM (examen)
CPU a **4.2 GHz** y DDR4 a **2.6 GHz**: si cada instrucción fuera a la RAM, la CPU nunca correría a 4.2. Se toca la RAM una vez para traer un bloque (8 MB); un programa de ~500 KB cabe entero en caché.
- Multinúcleo: **mínimo 2 niveles**: L1 (dividida en L1-D y L1-I) y L2 por núcleo, L3 global.

## 6. RP2040 (Pico)
- GPIO, oscilador, debugger, flash externa, **PIO**, regulador; dos núcleos + SRAM; la ROM es otro periférico.
- Bancos de memoria independientes por los que los núcleos se turnan (sin orden, "entropía").
- Núcleo **Cortex-M0+**; bloques: NVIC, wake-up, MPU, crossbar, GPIO rápido, breakpoints, JTAG, DMA. "M" = microcontrolador; Cortex-A = aplicaciones.

## 7. Elegir un Cortex-M
| Núcleo | Punto flotante | Cuándo |
|---|---|---|
| M0 | Sin FPU: ~30 instrucciones enteras por operación | El más barato (~1 USD) |
| M3 | Multiplicación por hardware; divide con el inverso multiplicativo | Intermedio |
| M4 | **FPU nativa** | Mucho punto flotante |
| M7 | FPU + DSP vectorial | Procesamiento de señales |
Con red, ESP32. Ningún Cortex-M maneja gráficos. Reto: dividir flotantes en C solo con enteros (corrimientos, mantisa).

## 8. Intel: CISC por fuera, RISC por dentro
- **Retrocompatibilidad:** un Core i9 corre código del 8086. **Itanium (IA-64)** la rompió y fracasó; triunfó **x86-64** de AMD. Cambiar de ISA (Mac Intel → Apple Silicon) exige recompilar o **Rosetta**.
- Decodificador con predictor de saltos → L1-I (32 KB, 8 vías); predecodificador de 16 bytes por ciclo; instrucciones CISC → **micro-operaciones** (decodificadores simples + uno completo, porque 60–75 % del código es carga/almacenamiento); cola → reordenador (**fuera de orden**).
- **Renombrado de registros:** más registros físicos que los 8 nominales; dos programas de 32 bits en paralelo por hardware.
- Coffee Lake (2017): 8 puertos → 4 núcleos, hasta 32 µops por ciclo. Golden Cove (2021): 12 puertos, cola de 512.

## Pendiente
Elegir arquitectura para la práctica. La práctica de Windows exige **Raspberry Pi 3** (no funciona en la 4).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| PIC | 256 B de RAM, pila de 8 niveles fuera de RAM, sin recursión, acumulador W |
| AVR | 32 registros, 50 MHz |
| ESP32 | RF + SHA por hardware; PSRAM separada en colas |
| Caché | Proxy; 4.2 GHz vs. 2.6 GHz; L1 D/I, L2, L3 |
| Cortex-M | M0 sin FPU, M3 multiplica, M4 FPU, M7 FPU + DSP |
| Intel | CISC fuera, µops RISC dentro; fuera de orden; renombrado |
