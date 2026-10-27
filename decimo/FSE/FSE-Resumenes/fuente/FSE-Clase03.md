% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 3 · Historia de x86: del 4004 al 486, modos y coprocesador
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · miércoles 2 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. El die de un procesador de 4 núcleos
Núcleos en **simetría de espejo**; se ven L2, L1D, L1I, bus interno, control, registros (vectoriales), FPU y ALU. **La ALU es diminuta**: el chip está dominado por memoria (cachés y registros).

## 2. Los primeros Intel
| Chip | Año | Bits | Reloj | Notas |
|---|---|---|---|---|
| 4004 | 1971 | 4 | 740 kHz | < 1 MIPS; instrucciones elementales |
| 4040 | 1974 | 4 | — | Evolución del 4004 |
| 8008 | 1972 | 8 | 500 kHz | 0.0005 MIPS |
| 8080 | 1974 | 8 | 2 MHz | Sin llegar a 1 MIPS |
| 8085 | 1976 | 8 | 3 MHz | El 8080 con más reloj; 25 KB de RAM |
!!! Paradoja del 8080 (examen)
¿Por qué el 8080 a 2 MHz rinde menos MIPS de lo esperado? Porque tiene mnemónicos complejos (seno, coseno…) que por dentro usan **la misma ALU entera** del 4004 → muchas instrucciones internas por mnemónico. En el 4004 el ingeniero programaba la serie de Taylor a mano. (Un alumno dijo "por ser RISC": incorrecto.)
- Subir la frecuencia no era trivial: los transistores de la época fallaban con cristales muy rápidos.

## 3. La promesa de Intel (8085)
"Todos los programas que hagas van a funcionar en el procesador siguiente": origen de la **retrocompatibilidad binaria**, que le ganó el mercado frente a TI, Cyrix, Motorola.
- Microarquitectura del 8085: ALU entera, interrupciones, puerto serie, acumulador de 8 bits, banderas, decodificador, registros generales en pares de 16 (HL), SP, PC.

## 4. El 8086 y la ISA x86
- 1978, **primer procesador de 16 bits**, 5–10 MHz, ~20,000 instrucciones, ~10 ciclos por instrucción, **2²⁰ = 1 MB** direccionable.
- Un binario de 1978 corre igual en un Intel moderno.
- Registros: **AX** (AH + AL), SI, DI, BP, SP, PC, segmentos, flags; cola de *prefetch*. El 186 es "un 8086 en esteroides".

## 5. El 286 (1982): MMU y Modo Protegido
- Hasta 25 MHz, 2.66 MIPS. Quita la multiplexación de buses; **segunda ALU** solo para base + offset; **MMU**; 30 mnemónicos nuevos (≈ 23,000 instrucciones).
- Todo x86 **arranca en Modo Real** (8086: dirección lógica = pin físico). Un bit por software pasa a **Modo Protegido**: paginación, multitarea y segmentación con privilegios; si una aplicación falla, se elimina sin colapsar el sistema.
- Desde el 486, placa metálica y disipador obligatorio.

## 6. El 386 (1985) y el coprocesador 80387
- **Primer x86 de 32 bits**: 40 MHz, 10 MIPS, **4 GB**; pipeline de 3 etapas; **Modo Virtual 8086** (varios 8086 aislados, como matrioskas); 16 mnemónicos y 2 registros de debug.
- ALU solo de **enteros**; sin FPU. Audio (MP3 de Fraunhofer) y criptografía necesitan punto flotante. Por software: sin(x) ≈ x − x³/3! + x⁵/5! − x⁷/7! + … (miles o millones de ciclos).
- **80387:** coprocesador externo con **tablas de interpolación** en silicio: seno, coseno, exp, log en **4–5 ciclos**.

## 7. El 486 (1989)
Hasta 100 MHz; **caché L1 integrada** y separada en **L1I y L1D** (prefetch sin chocar con datos); **FPU integrada**; pipeline de **5 etapas**; 6 mnemónicos. Después: Pentium (P5), 1993, 200 MHz.

## 8. Conceptos de examen
!!! Pipeline fuertemente acoplado
Alta codependencia: cambiar un bloque obliga a rediseñar todo el procesador (lo opuesto a RISC). Software: todo en `main` vs. MVC con interfaces.
!!! "Examen: explique qué es un bus coherente"
La caché copia la RAM (10–1,000 veces más lenta). **No coherente:** la escritura solo va a la caché; la RAM queda vieja. **Coherente:** actualiza **caché y RAM a la vez**; más lento pero íntegro.

## 9. Intel vs. AMD
- 1982: convenio; AMD fabrica 186 y 286 (a ¼ del precio). Intel quiso impedir el 386; AMD argumentó que era extensión del 286 y, con ingeniería inversa, sacó el **Am386DX-40** (40 MHz vs. 33, menos consumo, ⅓ del precio).
- Derecho romano (México) ≈ CISC; anglosajón (precedentes) ≈ RISC. AMD ganó en **1991** (386) y por precedente en **1995** (486). Intel respondió con el P5/Pentium.

## Pendiente
Lab: Raspbian en la MicroSD y circuito alambrado (LEDs, resistencias, ULN).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Chip | Para recordar |
|---|---|
| 8080 | Menos MIPS: mnemónicos complejos sobre ALU entera |
| 8086 | 16 bits, 1 MB, retrocompatibilidad |
| 286 | Segunda ALU, MMU, Modo Protegido |
| 386 | 32 bits, 4 GB, VM86, pines para el 80387 |
| 80387 | Tablas de interpolación: 4–5 ciclos |
| 486 | L1 separada I/D, FPU integrada, 5 etapas |

**Arranque:** siempre en Modo Real. **Bus coherente:** escribe en caché y RAM a la vez. **Fuertemente acoplado:** cambiar algo = rediseñar todo.
