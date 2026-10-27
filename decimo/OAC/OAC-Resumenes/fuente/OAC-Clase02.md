% materia: Organización y Arquitectura de Computadoras
% titulo: Clase 2 · Material del curso y Pico 1 vs. Pico 2 (FPU, MAC, DMA)
% subtitulo: Organización y Arquitectura de Computadoras · M.I. José Antonio de Jesús Arredondo Garza · miércoles 2 sep 2026 · Presentación y Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

!!! Sesión corta
El profesor terminó antes para entregar un informe de su candidatura de doctorado.

## 1. Antecedentes y herramientas
- Historia: el procesador "180" que dio problemas a IBM, el timer 555, el origen de BASIC y **Texas Instruments**, que empezó como petrolera.
- Lecturas: "He creado una CPU de 8 bits, corre tu propio juego"; microcontroladores vs. microprocesadores.
- Herramientas: **Osciloscopio Virtual v3** y una **terminal web** sin instalación.

## 2. Pico 1 vs. Pico 2: FPU
- La Pico 2 tiene **FPU** con **32 registros de punto flotante**; la Pico 1 no la tiene físicamente.
!!! Portabilidad (examen)
Un programa en ensamblador con instrucciones de FPU para la Pico 2 **no corre en la Pico 1**: no es un límite de software, es ausencia de hardware.

## 3. MAC, bootloader y DMA
- La Pico 2 tiene en teoría una unidad **MAC** (multiplicación acumulativa, como en los DSP), pero **aún no se puede usar** desde los ensambladores disponibles.
- El bootloader oficial **no distingue** entre Pico 1 y Pico 2.
- Las librerías estándar de **DMA** rendían mal; el profesor hizo **su propia librería** para manejar imágenes directamente. Moraleja: no depender solo del software de alto nivel.

## 4. Bootloader alternativo y ejemplos
- Bootloader alternativo (transcrito como "Pori Bimor", nombre impreciso) con una librería matemática reducida tipo Python: matrices y ecuaciones.
| Ejemplo del material | Detalle |
|---|---|
| Pantalla | Display **ILI9488**, 320 × 480 píxeles |
| Servomotores | Driver de posición |
| Red neuronal | Ejemplo de MATLAB adaptado para resolver la **compuerta XOR** |
| Proyectos anteriores | Guía de lo que se puede lograr |

## 5. FPU64 y bibliografía
- **FPU64:** microcontrolador de 64 bits a **40 MHz** cuyo set de instrucciones es tan potente que no necesita componentes extra.
- **Numerical Recipes (in C):** algoritmos de integración y derivación; usar la versión digital de dominio público.

## Pendiente
Compartir las carpetas (Osciloscopio v3, Assembler Pico, terminal web, ejemplos); se formó grupo de WhatsApp. Próxima: temario e inicio de ejercicios en ensamblador.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| FPU | Pico 2 sí (32 registros), Pico 1 no; código con FPU no es portable |
| MAC | Existe en la Pico 2, aún inaccesible desde ensamblador |
| Bootloader oficial | No distingue Pico 1 y Pico 2 |
| DMA | El profesor hizo su propia librería |
| Ejemplos | ILI9488 320×480, servos, XOR con red neuronal |
| Libro | Numerical Recipes (dominio público) |
