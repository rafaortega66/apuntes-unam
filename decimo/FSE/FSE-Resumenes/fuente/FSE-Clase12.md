% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 12 · Bootstrap, tipos de RESET y paginación
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · miércoles 7 oct 2026 · Tema 2 (cierre) e inicio de la Unidad 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Última clase antes del primer parcial (Unidades 1 y 2). Lo marcado (material) viene de las diapositivas.

## 2.8 Secuencia de arranque (bootstrap)
!!! Definición
Secuencia ordenada de inicialización de hardware y software que ejecuta un procesador justo después de encenderse o recibir un reinicio, para pasar de un estado inactivo a ejecutar el kernel o el SO.
**Vector de RESET** (dirección del primer fetch), según arquitectura (material):
| Arquitectura | Vector de RESET |
|---|---|
| Intel | 0xFFFFFFF0 |
| ARM Cortex-M/R | 0x00000000 o 0xFFFF0000 |
| PowerPC | 0x00000100 o 0xFFF00100 |
**Orden de las fases** (se pide el orden general, **no** las 32 cajas del diagrama):
1. Estabilizar voltajes y reloj.
2. Fetch del vector de RESET y salto (corto o largo) a la ROM/firmware.
3. Cambio a modo protegido ("modo 286").
4. Parches de microcódigo de la CPU.
5. Deshabilitar las cachés.
6. Inicializar y probar la DRAM; configurar la pila en DRAM (material).
7. Rehabilitar las cachés con sus reglas definitivas.
8. Paso de lista BSP/AP (multiprocesador).
9. Cargar BIOS/UEFI y luego el sistema operativo.
Error común: ejecutar BIOS o SO antes de tener DRAM y pila: el procesador colapsa.

## 2.8.1 Hard RESET y Soft RESET
| Tipo | Origen | Detalle |
|---|---|---|
| **Hard RESET** (Power-On Reset, POR) | Entrada inicial de corriente | Un CPLD espera a que se estabilicen ±12 V, ±5 V, ±3.3 V (material) y el reloj, y libera la línea de reset |
| **Soft RESET** | Evento de software o periférico, sin cortar la alimentación | Cuatro causas (abajo) |
Causas del Soft RESET:
- **Línea de reset dedicada:** el botón de reset.
- **Desbordamiento del Watchdog Timer:** si el programa se congela en un segmento más del tiempo permitido (p. ej. 1 s), el watchdog desborda y reinicia.
- **Sobrecalentamiento (overheat):** sensores térmicos detectan temperatura o consumo crítico.
- **Salida de suspensión ACPI:** la CPU se apagó casi por completo dejando su estado en la RAM, que siguió refrescándose con un microcontrolador de ultra bajo consumo; al despertar pasa por el bootstrap y el SO reconoce que sus datos ya están en memoria (no se recarga desde disco).

## 2.8.2 Arranque multiprocesador: BSP y AP
1. Al reiniciarse, todos los núcleos se tratan como procesadores completos (material); el **LAPIC** de cada uno se resetea.
2. Bit BSP del LAPIC = **1** para el **Bootstrap Processor**, **0** para los **Application Processors**.
3. El BSP hace el fetch del vector de RESET, carga BIOS/UEFI e inicializa la APIC.
4. Los AP hacen su autoprueba y entran en **WAIT-for-SIPI**.
5. El BSP envía la **SIPI** (Startup Inter-Processor Interrupt) con una instrucción que apunta a los primeros 4 KB de RAM.
6. **Condición de carrera regulada por semáforo:** cada AP despierta, registra su APIC ID en la tabla de procesadores, incrementa el contador global, reinicia su vector de interrupciones y vuelve a esperar.
7. El BSP cierra la tabla, configura PCI e inicia el kernel (material). Con BIOS el BSP carga el SO solo; con UEFI los AP ayudan (material).
Evita que varios núcleos ejecuten el BIOS a la vez y choquen en el bus.

## Reglas del primer parcial
Unidades 1 y 2 (la 3 no entra). **3 preguntas abiertas** + tecnicismos con terminología exacta: "si son de esos que me confunden BGA con HDMI, los puse fritos". Presentado el 14 oct (FSE-E01).

## 3.0 Introducción a la Unidad 3
Del bare metal a un **kernel** que reparte tiempo y memoria. Tres capas: **API y llamadas a sistema** (`printf`, `malloc`, `write`), **planificador** (scheduler) y **administración de memoria** (paginación). Conecta firmware con Linux embebido y RTOS.

## 3.0.1 Paginación, pila y falla de segmento
- En bajo nivel la pila apunta a la última localidad (ejemplo: 64 KB); un retorno con la pila al tope y un POP hacia otra localidad puede sobrescribir el propio código o el kernel.
- **Paginación:** la MMU y el kernel dividen la RAM en páginas; cada proceso trabaja en su **espacio virtual** y no conoce la memoria física.
!!! Segmentation fault
Si una instrucción accede fuera de sus páginas (escribir en 0x00000000 o encima del kernel), el hardware genera una excepción y el kernel termina el proceso con **Segmentation Fault**.
- **Swap:** si la RAM se satura, el kernel copia al disco las páginas de procesos inactivos (la sesión de Matlab olvidada hace días).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Bootstrap (examen: orden general)
Voltajes y reloj → vector de RESET (Intel 0xFFFFFFF0; ARM 0x00000000/0xFFFF0000) → modo protegido → microcódigo → cachés off → DRAM y pila → cachés on → BSP/AP → BIOS/UEFI → SO.

| RESET | Causa |
|---|---|
| Hard (POR) | Encendido; CPLD espera voltajes y reloj estables |
| Soft | Botón, watchdog desbordado, sobrecalentamiento, salida de ACPI (RAM conservada) |

**Multiprocesador.** LAPIC: bit BSP = 1 (maestro) / 0 (AP). El BSP carga BIOS/UEFI e inicializa la APIC; los AP esperan la SIPI, se registran por semáforo (APIC ID, contador) y vuelven a esperar.

**Memoria (Unidad 3).** Paginación con MMU: espacio virtual por proceso; salirse = segmentation fault; swap manda páginas inactivas a disco.
