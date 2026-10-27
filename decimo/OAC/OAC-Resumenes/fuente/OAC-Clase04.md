% materia: Organización y Arquitectura de Computadoras
% titulo: Clase 4 · ISA, CISC vs. RISC y Pico 1 vs. Pico 2 (RP2350)
% subtitulo: Organización y Arquitectura de Computadoras · M.I. José Antonio de Jesús Arredondo Garza · miércoles 9 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Punto flotante: Pico 1 vs. Pico 2
!!! Medición de laboratorio (examen)
Un algoritmo de muestreo de **125 µs** sube a **220 ms** con punto flotante por software en la Pico 1 (sin FPU); en la Pico 2, con FPU por hardware, tarda **102 µs**.
- Arranque de la Pico 2: un **registro leído por el bootloader** decide si arranca en ARM o en RISC-V. Correr ambos a la vez exigiría un bootloader propio en ensamblador puro.

## 2. ISA vs. microarquitectura
| ISA | Microarquitectura |
|---|---|
| Organización funcional vista por el software | Implementación física en silicio |
| Instrucciones, memoria, registros visibles (AX, BX, PC, SP; x0–x31), formatos, modos | Datapath, unidad de control, caché, predicción de saltos, ejecución fuera de orden |
| Estable por años (x86 desde 1978) | Cambia en cada generación |
Ej.: Pentium, Pentium Pro y Core i3/i5/i7 comparten ISA x86 con microarquitecturas muy distintas. Cambiar de microarquitectura no obliga a reescribir el código si la ISA es la misma.

## 3. CISC vs. RISC
| | CISC (x86) | RISC (ARM, RISC-V, MIPS) |
|---|---|---|
| Instrucciones | ~1500, heterogéneas | ~50 base en RISC-V, ortogonales |
| Longitud | Variable, 1–15 bytes | Fija (4 bytes; Thumb en bloques de 2 o 4) |
| Operaciones | Complejas (`IMUL [mem1], [mem2]`) | Simples: carga, almacena, ALU, salto |
| Código | Compacto | Más líneas |
| Ciclos | 1 a 20+ | Casi todas 1 (carga/almacena 2–3) |
| Consumo | Alto | Bajo; pipeline optimizado |
Navaja suiza (CISC) vs. herramientas simples coordinadas (RISC). Error común: creer que RISC es inferior por usar más líneas.

## 4. x86, ARM y RISC-V
| | x86 | ARM | RISC-V |
|---|---|---|---|
| Filosofía | CISC | RISC | RISC abierta y modular |
| Mercado | PC y servidores | Móviles, IoT, Apple M1–M4 | Emergente: Google, Nvidia, Alibaba |
| Consumo | 100–500 W en servidores | 5–15 W móviles; 10–30 W M4 | Bajo |
| Licencia | Propietaria | **Licencia + regalías** por chip | **Libre, sin regalías** |
- Intel Atom fracasó en móviles por el calor. ARM no fabrica chips: diseña y licencia.
- Código ARM no es portable a cualquier ARM (Orange Pi vs. Raspberry Pi).

## 5. Pico 1 vs. Pico 2
| | Pico 1 (RP2040) | Pico 2 (RP2350) |
|---|---|---|
| Núcleos | 2× Cortex-M0+ a 133 MHz | 2× Cortex-M33 + 2× RISC-V Hazard3 a 150 MHz |
| SRAM | 264 KB | 520 KB |
| Flash | 2 MB QSPI externa | 4 MB QSPI externa |
| FPU | No (emulación) | Sí: S0–S31 |
| PIO | 2 interfaces (8 máquinas en un bloque de la página; 4 en otro) | 3 interfaces, **12** máquinas |
| Overclock | ~250 MHz | ~350 MHz |
| Seguridad | — | TrustZone, cripto por hardware, OTP |
!!! Nomenclatura RP2350
**RP** = Raspberry Pi · **2** = serie/doble núcleo · **3** = Cortex-M33 · **5** = SRAM: 2⁵ × 16 KB (= 512; se reporta 520 KB) · **0** = 0 KB de Flash **interna** (usa 4 MB externa en la placa).

## 6. PIO, seguridad y fetch
- **PIO:** máquinas de estado programables, como una mini-FPGA; implementan protocolos sin la CPU (WS2812 en 10–15 líneas). **SPI por PIO: 20–30 MHz** frente a **7.5 MHz** del SPI nativo.
- **TrustZone** aísla credenciales (Wi-Fi) y claves; aceleración criptográfica; **OTP** (8 KB, programable una vez).
- **Fetch:** a 133 MHz el ciclo dura ≈ 7.5 ns; a 150 MHz ≈ 6.7 ns; a 350 MHz ≈ 2.9 ns. La Flash QSPI tiene ≈ 30 ns de latencia: el overclock ayuda más desde SRAM.

## 7. C vs. Inline Assembly
- El profesor critica que MicroPython oculte la arquitectura. Alternativa: `@micropython.asm_thumb` con subrutinas en ensamblador que usan los registros S de la FPU.
- La FPU solo hace aritmética básica y raíz cuadrada: **no** seno ni coseno.
- Videos: *RISC-V vs ARM vs x86* (13 min) y reseña de la Pico 2.

## Pendiente
Tema 3 (RTL, ALU, datapath, unidad de control, ciclo fetch-decode-execute) y práctica en ARM Thumb: LED, CPUID y macro de delay.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| ISA vs. microarquitectura | Qué instrucciones existen vs. cómo se implementan en silicio |
| CISC / RISC | Variable y complejo (x86) / fijo, 1 ciclo, bajo consumo |
| ARM / RISC-V | Regalías / libre |
| FPU | 125 µs → 220 ms sin FPU; 102 µs con FPU |
| RP2350 | 4 núcleos, 520 KB, 4 MB externa, 12 máquinas PIO |
| PIO | SPI 20–30 MHz vs. 7.5 MHz nativo |

!!! Nomenclatura
RP · 2 · 3 (M33) · 5 (2⁵ × 16 KB) · 0 (sin Flash interna).
