% materia: Organización y Arquitectura de Computadoras
% titulo: Clase 3 · Pico 1 vs. Pico 2, RISC-V y FPU
% subtitulo: Organización y Arquitectura de Computadoras · M.I. José Antonio de Jesús Arredondo Garza · lunes 7 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Diferencias de hardware Pico 1 vs. Pico 2
- Pico 1 sin FPU: el punto flotante va por software. La Pico 2 admite overclocking (ciclo máquina más rápido).
!!! Mapa de memoria (examen)
El mapa de memoria **se reestructuró por completo** en la Pico 2. Si se manipulan registros directamente con el mapa de la Pico 1, el programa falla o accede a direcciones equivocadas.
- RP2350 en variantes de **30 y 48 pines** (más E/S en la de 48).
- Máquinas de estado PIO: **de 4 a 8** según esta clase (en la Clase 4 se dio 12 en total para la Pico 2; comparar).

## 2. RISC-V: origen y filosofía
- Pagar regalías por cada chip (como en ARM) es carísimo en producción masiva; RISC-V es al hardware lo que Linux al software: **abierto y sin regalías**.
- **Modular:** set base + extensiones (punto flotante, multiplicación…).
- Nació en **UC Berkeley, 2014–2015**. Consorcio: Google, Intel, Huawei, Ali Cloud; ya llega al ESP32.

## 3. CISC vs. RISC
| Criterio | Intel/AMD | ARM | RISC-V |
|---|---|---|---|
| Tipo | CISC | RISC | RISC |
| Ancho de palabra | 16, 32, 64 | 32, 64 | 32, 64, **128** |
| Licencia | Propietaria | Licencia + regalías | Libre |
| Instrucciones | Complejas | Reducidas | Base + extensiones |
- RISC-V: **32 registros** generales; la **ABI** fija la convención de uso de cada registro (paso de parámetros).
- Conceptos: overflow, carry, modos inmediato e indirecto.
- En RISC, los **saltos consumen más de un ciclo** (costo del pipeline).

## 4. Independencia funcional de periféricos
Una vez configurado, el periférico trabaja **sin que la CPU lo atienda**. Ejemplo: **ADC + DMA** con una región de RAM reservada: el ADC convierte y el DMA guarda en ráfaga en segundo plano, sin ciclos de los núcleos.

## 5. Selección ARM / RISC-V en la Pico 2
El **bootloader** evalúa al arranque un **bit habilitado por software**: toma el camino ARM Cortex-M33 o el RISC-V. La decisión es **única al arranque**: desde modo ARM no se puede pasar a RISC-V en la misma sesión.

## 6. FPU de la Pico 2
- **32 registros S0–S31**: suma, resta, multiplicación, división y raíz cuadrada (VSQRT). **Sin** seno, coseno ni trascendentales.
- Código con FPU **no corre en la Pico 1**.
- Aplicación: un filtro digital en ensamblador con punto flotante. MicroPython y VS Code aún no soportan todas las instrucciones de DSP.

## 7. Entorno de desarrollo
VS Code + Make + emulador integrado (sin QEMU pesado); ensamblador desde C o inline en MicroPython; ejercicios de **direccionamiento directo a registros sin librerías**; memoria externa por interfaz serial.

## Pendiente
Teclear y analizar el set de instrucciones: primero aritméticas y lógicas, luego direccionamiento directo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Mapa de memoria | Distinto en la Pico 2: no reutilizar direcciones de la Pico 1 |
| RISC-V | Berkeley 2014–15, libre, modular, hasta 128 bits, 32 registros + ABI |
| Independencia funcional | ADC + DMA en segundo plano |
| Bootloader | Un bit decide ARM o RISC-V solo al arranque |
| FPU | S0–S31; + − × ÷ √; no trascendentales; no corre en Pico 1 |
