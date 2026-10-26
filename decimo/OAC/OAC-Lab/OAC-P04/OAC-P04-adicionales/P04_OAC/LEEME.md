# Práctica 4 OAC: Direccionamiento Entrada-Estado (DE10-Lite)

## Contenido
- `quartus/`: código VHDL listo para Quartus (top-level `p4_top`), los pines de la DE10-Lite (`pines_DE10-Lite.tcl`) y la simulación para Questa (`tb_p4.vhd` + `run_sim.do`).
- `docs/`: el enunciado y los mapas de Karnaugh de la liga falsa.

## Estado de cada punto del enunciado
| # | Punto | Estado |
|---|---|---|
| 1 | Carta ASM: 8 estados, 4 entradas, 4 salidas (2 estándar y 2 negadas), ≥3 salidas condicionales | Diseñada (la de clase). **Falta dibujarla para el reporte.** |
| 2 | Tamaño y contenido de la memoria | Hecho (tabla abajo) |
| 3 | Implementación en Quartus | Hecho y probado en la tarjeta (14/10) |
| 4 | Demostración en la FPGA | Hecha en el laboratorio. **Falta el video** (guion abajo) |
| 5 | Simulación con la memoria y el estado presente | **Falta correrla en Questa y tomar capturas** (`run_sim.do`) |
| — | Reporte (carátula, objetivo, introducción, desarrollo, conclusiones, bibliografía) | **Falta**. Nombre: `practica04_equipo07_Apellido1_Apellido2.pdf` |

## Asignación binaria
- Estados E0–E7 = 000–111
- Entradas (prueba): X=000, Y=001, Z=010, W=011, QX=100 (auxiliar, siempre 1)
- Salidas: S1 y S4 estándar (activas en 1); S2 y S3 negadas (activas en 0). Inactivas = `0110`

## Memoria: 2^3 × 17 = 136 bits
Palabra = prueba(3) | LF(3) | LV(3) | SF: S1 S2 S3 S4 (4) | SV: S1 S2 S3 S4 (4)

| Estado | Prueba | LF | LV | SF | SV |
|---|---|---|---|---|---|
| E0 000 | QX 100 | 001 | 001 | 1111 | 1111 |
| E1 001 | X 000 | 011 | 010 | 0010 | 0110 |
| E2 010 | Y 001 | 101 | 100 | 0100 | 0111 |
| E3 011 | Z 010 | 000 | 110 | 0110 | 1110 |
| E4 100 | W 011 | 101 | 010 | 0010 | 0010 |
| E5 101 | QX 100 | 111 | 111 | 0100 | 0100 |
| E6 110 | W 011 | 110 | 111 | 0111 | 0010 |
| E7 111 | QX 100 | 000 | 000 | 1001 | 1001 |

Salidas condicionales (SF ≠ SV): E1, E2, E3 y E6.

## Ecuaciones (mapas de 3 variables con el estado ABC, como corrigió el profesor)
- LF2 = AB' + BC'
- LF1 = B'C + ABC'
- LF0 = B' + A'C'
- LV2 = A'B + BC' + AB'C
- LV1 = A'C + AB' + AC'
- LV0 = A'B'C' + AB'C + ABC'
- P2 = AC + A'B'C'
- P1 = AC' + A'BC
- P0 = BC' + AC'

## Tarjeta DE10-Lite
- Izquierda, **LEDR9–LEDR7**: estado presente (LEDR9 = bit más significativo)
- Derecha, **LEDR3–LEDR0**: S4, S3, S2, S1 (LEDR1 = S2 y LEDR2 = S3 son negadas: encendido = inactiva)
- **SW0–SW3** = X, Y, Z, W (arriba = 1). **KEY0** = reset (regresa a E0). Avanza un estado cada 0.5 s.
- Las salidas pasan por `registro_salidas`, así que muestran las del estado **anterior** (un paso atrás).

## Guion del video (lo que debe verse)
Cada renglón es un tic (0.5 s): estado → LEDs del estado | LEDs de salida.

**1. Presiona KEY0.** E0 → ninguno | LEDR1, LEDR2 (ninguna salida activa).

**2. Todos los switches abajo.** Ciclo E0 → E1 → E3 → E0:
- E1 → LEDR7 | LEDR0–3
- E3 → LEDR8, 7 | LEDR2
- E0 → ninguno | LEDR1, 2

Narración: "X=0 manda de E1 a E3 por la liga falsa; Z=0 regresa a E0."

**3. Sube SW0, SW1 y SW3 (X=Y=W=1).** Alterna E2 ↔ E4:
- E2 → LEDR8 | LEDR2
- E4 → LEDR9 | LEDR1, 2, 3

Narración: "X=1 toma la liga verdadera a E2; Y=1 va a E4; W=1 regresa a E2."

**4. Baja SW1 (Y=0).** Ciclo E2 → E5 → E7 → E0 → E1 → E2:
- E5 → LEDR9, 7 | LEDR1
- E7 → LEDR9, 8, 7 | LEDR1
- E0 → ninguno | LEDR0, 3
- E1 → LEDR7 | LEDR0–3
- E2 → LEDR8 | LEDR1, 2

Narración: "E5 y E7 usan QX, así que avanzan solos."

**5. Baja SW0 y SW3 y sube SW2 (X=0, Z=1, W=0).** Llega a E6 y se queda:
- E6 → LEDR9, 8 | LEDR1, 2, 3

Narración: "E6 revisa W; como W=0, la liga falsa lo deja en E6."

**6. Sube SW3 (W=1).** E6 → E7 → E0 → E1 → E3 → E6 …

Narración: "Con W=1 sale a E7. Ya recorrimos los 8 estados."

## Simulación (Questa)
1. Abre Questa. En **File → Change Directory** escoge la carpeta `quartus`.
2. En la consola escribe `do run_sim.do`.
3. Toma capturas donde se vean `est_pres`, `palabra` (contenido de la memoria), `qsel` y las salidas.
