% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 7 · Interrupciones, DMA, chipset y temporizadores
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · lunes 21 sep 2026 · Tema 2 (2.3 y 2.4) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 2.3.1 Unidad controladora de interrupciones (ICU)
Una **interrupción** es un mecanismo de hardware que altera el flujo normal del programa para obligar al procesador a atender un evento externo.
| Tipo | Qué significa |
|---|---|
| Enmascarable | El procesador puede ignorarla o diferirla según un registro de configuración |
| No enmascarable (NMI) | Crítica: no se puede bloquear, se atiende de inmediato y con prioridad |
!!! Máscara con compuertas
Cada bit del vector de máscara se **niega** y entra a una **AND** con la señal del periférico. Máscara **0** → se niega a 1 → la AND deja pasar la interrupción. Máscara **1** → se niega a 0 → salida siempre 0: bloqueada.

## 2.3.2 Prioridad y resolución
- **Monivel:** misma prioridad para todas; se atienden por orden de llegada.
- **Multinivel:** jerarquías; una de mayor prioridad suspende la que se está atendiendo.
| Resolución | Cómo | Ventaja / desventaja |
|---|---|---|
| **Por tabla** (software; ARM, microcontroladores) | Tabla en memoria con las rutinas; el SO la recorre registro por registro (el procesador "sufre de amnesia" al apagarse) | Barata en hardware; lenta, **O(N)** y varios ciclos |
| **Por vector** (hardware; Intel x86, APIC) | La ICU localiza la rutina, la precarga en RAM y entrega todo listo al procesador | Instantánea, sin ciclos de búsqueda |

## 2.3.3 Disparo por valor vs. por flanco
- **Por valor (nivel):** activa mientras el pin conserve el nivel. Estándar en los 70–80. Ejemplos: botón de reset (presionado, la PC se queda congelada) y la señal de **sobrecalentamiento**.
- **Caso Windows 11 (abril 2024):** una refactorización borró el manejador de la interrupción de overheat; la GPU siguió calentando y, según se dijo en clase, llegó a fundir soldaduras.
- **Por flanco:** detecta la **transición** (subida o bajada) en un solo ciclo de reloj.
!!! Por qué se prefiere el flanco (examen)
Serie a 9,600 baudios ≈ 1 ms por byte. Por valor, un procesador de **8 MHz** perdería **8,000 ciclos** retenido; por flanco, un pulso de un ciclo y el periférico deja de interrumpir.
Error común (de la diapositiva): decía "cambio al / cambio abajo"; es **cambio a alto / cambio a bajo**.

## 2.3.4 IRQ, PCI y DMA
- **Bus ISA (16 bits):** una línea IRQ física dedicada por tarjeta; ruteo complejo.
- **Bus PCI (32 bits, 150 MHz según los apuntes):** IRQ multiplexadas; 4 líneas de control → 2⁴ = **16 dispositivos**. Dos líneas activas fuera del protocolo = error.
- **DMA:** la CPU va en GHz y los periféricos en MHz; el DMA (en el chipset) mueve bloques periférico ↔ RAM **sin la CPU**. El **RP2040** tiene 2 núcleos y **2 DMA** (p. ej. USB → SPI mientras los núcleos calculan).

## 2.3.5 Chipset: Puente Norte y Puente Sur
| Puente | Componentes (cifras del profesor) |
|---|---|
| **Norte** (ultra alta velocidad) | CPU 3 GHz, RAM 2.66 GHz, GPU en PCIe x16, SSD |
| **Sur** (periféricos lentos) | SATA 60 MB/s, PCI 150 MHz / 2 GB/s, USB 3.1 a 5 Gbps (÷8 < 1 GB/s), Gigabit Ethernet ≈ 125 MB/s |
Videojuegos: en la pantalla de carga, el DMA pasa texturas del SSD a la RAM de la GPU sin despertar a la CPU.
!!! Ojo con las cifras
Verificadas contra el audio. Referencia externa (no de clase): SATA III = 600 MB/s y PCI clásico = 33/66 MHz. Para el examen, usar las del profesor y confirmar con él si se preguntan.

## 2.4 Temporizadores (timers)
!!! Definición (examen)
"Un temporizador en hardware es un **contador que activa una interrupción al llegar a cero** y reinicia el conteo automáticamente (o se reconfigura mediante software)."
**No hay SO multitarea sin timer.** El SO tiene 3 módulos, uno por componente físico:
| Componente físico | Módulo del SO |
|---|---|
| Procesador | Scheduler (calendarizador) — necesita el timer como "reloj de pared" |
| Memoria | Sistema de asignación de memoria |
| Periféricos | Manejadores (drivers) |
| Parámetro del timer | Opciones |
|---|---|
| Modo | Free running (en bucle) / One shot (una vez y se detiene) |
| Dirección | Up (0, 1, 2…) / Down (255, 254…) |
| Rango | 8 bits (0–255) o 16 bits (65,536); 10 y 12 son raros |
| Fuente de reloj | Interna (reloj del procesador) / externa (encoder de motor, decodificador de audio, miógrafo) |
Ejemplo: audio de CD/Spotify a 44,100 Hz; un timer de 16 bits alcanza porque 65.536 kHz > 44.1 kHz.
**Bajo consumo:** collares GPS o estaciones meteorológicas: el timer despierta al chip (p. ej. cada 3 s), sincroniza por **NTP**, transmite la bitácora y lo vuelve a apagar.

## Pendiente
Las fechas del parcial en los apuntes no cuadran con lunes/miércoles (25 sep, 1 y 3 oct no son días de FSE); verificar. Sin tarea.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Enmascarable / NMI | Se puede bloquear con la máscara (bit 1 → AND da 0) / no se puede |
| Monivel / multinivel | Orden de llegada / prioridades que se interrumpen |
| Tabla / vector | ARM, software O(N), barato / Intel APIC, hardware, instantáneo |
| Valor / flanco | Nivel sostenido (reset, overheat) / transición en un ciclo |
| DMA | Mueve periférico ↔ RAM sin CPU; RP2040 tiene 2 |
| Norte / Sur | CPU, RAM, GPU, SSD / SATA, PCI, USB, Ethernet |

!!! Timer (seguro en el examen)
Contador que interrumpe al llegar a cero. 4 parámetros: **modo** (free running / one shot), **dirección** (up / down), **rango** (8 / 16 bits), **fuente de reloj** (interna / externa). Indispensable para el scheduler.
