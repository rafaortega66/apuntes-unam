% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 4 · Pentium, GCC, alineación de memoria y la guerra de los 64 bits
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · lunes 7 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Pentium (P5): pipeline superescalar U/V
Tras el litigio con AMD, Intel deja los números: Pentium (P5), 1993, 200 MHz.
- **Pipeline U:** cualquier instrucción x86, incluida la FPU.
- **Pipeline V:** solo instrucciones simples de carga, almacenamiento e índices.
!!! Dato de examen
En un programa compilado, **60–75 %** de las instrucciones son load/store simples y solo **25–40 %** es cómputo pesado (FPU, trigonometría, matrices, sigmoides). Por eso V corre en paralelo mientras U hace lo pesado.

## 2. Toolchain GCC
| Comando | Resultado |
|---|---|
| `gcc programa.c -o ejecutable` | Binario (o `a.out`) |
| `gcc -c modulo1.c` | Objeto `.o`; make/cmake compara fechas y no recompila lo que no cambió |
| `gcc -S programa.c` | Ensamblador `.s` para revisar los registros |
| `ld` | Enlaza `.o` y librerías |
"Compilar es caro, checar fechas es gratis."

## 3. Cierre convexo (convex hull)
Fuerza bruta O(Nᴺ) u O(N²); **ordenando** los puntos baja a **O(N log N)**. El ordenamiento es ~95 % comparación, carga, almacenamiento e índices: se resuelve moviendo memoria, no con la ALU ni la FPU.

## 4. Alineación de memoria
En 64 bits la RAM se direcciona en palabras de **8 bytes**.
```
struct Datos { int a; int b; double c; };          /* 24 bytes con padding */
struct Datos { int a; int b; double c; } __attribute__((packed));  /* 16 bytes */
```
Nominal 4 + 4 + 8 = 16, pero el compilador alinea cada miembro → **24 bytes**. `packed` elimina el relleno para enviar por bus serie o red.

## 5. MMX, DDR y SSE
| Tecnología | Año | Rasgo |
|---|---|---|
| **MMX** | 1997 | SIMD; 1 registro de 64 bits **compartido con la FPU** (8 char, 4 short, 2 int o 1 long); pipeline de 5 etapas; 32 KB L1; 57 mnemónicos nuevos; Windows 95 y 2D |
| **DDR** | — | Transfiere en flanco de subida **y** de bajada: doble ancho de banda |
| Pentium II | 1997 | 450 MHz, núcleo P6 |
| **SSE** (Pentium III) | 1999 | 8 registros **XMM de 128 bits** independientes de la FPU; 70 instrucciones; 3D |

## 6. Pentium Pro (P6), 1995
- **PAE:** bus de direcciones de 36 bits → **64 GB** de RAM con registros de 32.
- Pipeline de **14 etapas**; 3 decodificadores (1 completo + 2 simples).
- **Micro-operaciones:** por dentro es RISC; las instrucciones CISC se parten en µ-ops.
- **Ejecución fuera de orden:** primero lo que ya tiene sus datos en caché.
- **Ejecución especulativa** (pregunta obligatoria): evaluar ramas antes de saber si se necesitan.
- **Renombrado de registros:** AX, BX… se mapean a un banco físico más grande.

## 7. Pentium 4 (NetBurst), 2000
Pipeline de 20+ etapas pensado para 10 GHz; procesadores de 400 W, fuentes de hasta 1.4 kW (transformadores ~60 % eficientes); rendía menos por ciclo que el Pentium III o el Athlon. **Más frecuencia ≠ más rendimiento.**

## 8. Segunda guerra de los 64 bits
Límite de 4 GB en 32 bits.
| | Intel Itanium (IA-64) | AMD Opteron (AMD64), 2003 |
|---|---|---|
| ISA | **No** compatible con x86 | Compatible: IA-32, x86, MMX, SSE2, SSE3; modos real, protegido, virtual y largo |
| Frecuencia | 733 MHz–1.26 GHz | Hasta 3.2 GHz |
| Núcleos | 1–8 (P7) | Hasta 16 (K10) |
| Memoria | Controlador externo en el Northbridge | **IMC integrado** en el die |
| Interconexión | FSB | **3 enlaces HyperTransport** + crossbar |
Itanium fracasó por romper la retrocompatibilidad; Intel terminó **licenciando AMD64** (Intel 64 / x86-64).

## Pendiente
Lab: Raspbian grabado en la MicroSD y circuitos cableados (LEDs, resistencias, ULN), revisando VSS y VCC del ULN. Teoría: HyperTransport y crossbar del Opteron.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| U/V | 60–75 % load/store → pipeline V; U para todo |
| GCC | `-c` objeto, `-S` ensamblador, `ld` enlaza |
| Struct | 16 nominal → 24 alineado; `packed` → 16 |
| MMX / SSE | 64 bits con FPU / 8 XMM de 128 bits |
| P6 | PAE 64 GB, µ-ops, fuera de orden, especulativa, renombrado |
| NetBurst | Más GHz, menos rendimiento |
| IA-64 vs. AMD64 | Sin vs. con retrocompatibilidad; IMC + HyperTransport |
