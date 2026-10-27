% materia: Organización y Arquitectura de Computadoras
% titulo: Clase 13 · Minicomputadoras (SBC) II
% subtitulo: Organización y Arquitectura de Computadoras · M.I. José Antonio de Jesús Arredondo Garza · miércoles 21 oct 2026 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Segunda sesión sobre tarjetas monoplaca (SBC): Orange Pi frente a Raspberry Pi, herramientas de trabajo remoto, la gama baja y por qué la Pico 2 no corre un sistema operativo completo. Sin código ni ejercicios numéricos. Continúa la Clase 12.

## 1. Orange Pi 5 y Orange Pi 6
SBC (Single Board Computer) de alto desempeño con el SoC ARM **RK3588** de 8 núcleos de 64 bits.
| Característica | Orange Pi 5 |
|---|---|
| CPU | 8 núcleos: 4 Cortex-A76 (rendimiento) + 4 Cortex-A55 (eficiencia), 2.4 GHz base (overclock posible) |
| RAM | 4, 8, 16 o 32 GB |
| Tamaño | ≈ 10 × 6.2 cm |
| Almacenamiento | Ranura SSD M.2 y MicroSD (TF) |
| Puertos | HDMI, Ethernet RJ45, USB 2.0, USB 3.0, USB-C (alimentación) |
| WiFi | No soldado; ranura para tarjeta WiFi |
| Cámaras | Hasta 3 a la vez (visión e IA) |
- **Orange Pi 6:** más reciente, procesador de 12 núcleos.
- Permite procesamiento paralelo (varias cámaras) que rebasa a las tarjetas de 4 núcleos.
- Error común: grabarle una imagen de Linux hecha para Raspberry Pi; necesita la suya para RK3588.

## 2. Raspberry Pi 5 y disipación de calor
- CPU de **4 núcleos Cortex-A76 a 2.4 GHz**, conector de **40 pines GPIO**, WiFi integrado, varias opciones de RAM.
- Novedad: conector para el **HAT M.2**, un "piso" superior donde se inserta directo un SSD M.2 (comparación SSD vs. MicroSD en la Clase 12).
!!! Disipación
A 2.4 GHz con carga intensiva, tanto la Pi 5 como la Orange Pi 5 **necesitan disipador** (pasivo o con ventilador) sobre el integrado para no sobrecalentarse.

## 3. Herramientas de trabajo remoto
Programas libres para grabar, administrar y controlar la tarjeta desde la PC, sin monitor ni teclado propios.
| Herramienta | Función |
|---|---|
| **VNC** (Virtual Network Computing) | Ver y operar la interfaz gráfica completa de la tarjeta desde la PC, con su IP (Ethernet o WiFi) |
| **WinSCP** | Dos paneles: archivos de la PC y de la tarjeta; transferir, crear y editar código gráficamente |
| **BalenaEtcher** | Grabar (flashear) la imagen del SO Linux en una MicroSD o un SSD M.2 |
VNC y WinSCP exigen que PC y tarjeta estén en la misma red. Las tarjetas se programan en Python, C e incluso BASIC.

## 4. Gama baja
| Tarjeta | Rasgos |
|---|---|
| **Raspberry Pi Zero 2 W** | ≈ $500 MXN, apenas mayor que la Pico 2, 40 pines; con un HAT se le agrega Ethernet RJ45 y E/S |
| **Orange Pi Zero 3 W** | Competidora directa china en precio y tamaño |
| Gama alta (Pi 3/4/5, Orange Pi 5) | $1,000 a $4,000 MXN |
Error común: confundir la **Pi Zero 2 W** (SBC que corre Linux) con la **Pico 2** (microcontrolador con código nativo o MicroPython).

## 5. Por qué la Pico 2 no corre un SO completo
!!! La diferencia clave
Las Raspberry Pi 3, 4 y 5 tienen un **módulo de RAM dinámica externa** en la placa; la Pico 2 solo tiene su memoria interna, insuficiente para un sistema operativo completo.
- Lo que dijo el profesor (según NotebookLM): 4 MB de Flash y ≈ 2 MB de RAM de trabajo. La hoja de datos de la RP2350 indica **520 KB de SRAM**; verificar.
- **Expansión:** existe un módulo comercial de **16 MB por SPI** para Pico y Pico 2. Hipótesis del profesor (no probada): con él y un SO mínimo sería técnicamente posible. La memoria por SPI es mucho más lenta que la DRAM de la Pi grande.
- **DMA:** en las Picos exige más rigor de programación que en las Pi grandes por los parámetros que se configuran a mano.
Marca la frontera entre microcontrolador y microprocesador con memoria dinámica; se liga con la PIO y la FPU de la Pico 2 (Clases 10 y 11). Error común: creer que basta ampliar la Flash (almacenamiento) cuando lo que falta es RAM de trabajo.

## Avisos
- Próxima clase propuesta: sesión práctica mostrando VNC y WinSCP con Raspberry Pi. Sin tareas nuevas.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Tarjeta | Para recordar |
|---|---|
| Orange Pi 5 | RK3588, 8 núcleos (4 A76 + 4 A55), 2.4 GHz, M.2, hasta 3 cámaras, imagen propia |
| Orange Pi 6 | 12 núcleos |
| Raspberry Pi 5 | 4 Cortex-A76 a 2.4 GHz, 40 GPIO, WiFi, HAT M.2 para SSD |
| Pi Zero 2 W | ≈ $500, Linux completo, HAT Ethernet |
| Pico 2 | Microcontrolador: sin DRAM externa, no corre SO completo |

**Calor.** Pi 5 y Orange Pi 5 a 2.4 GHz con carga intensiva requieren disipador.

**Herramientas.** VNC = pantalla remota; WinSCP = archivos PC ↔ tarjeta; BalenaEtcher = grabar la imagen del SO.

!!! Pi grande vs. Pico 2 (examen)
La Pi grande corre un SO completo porque trae **RAM dinámica externa** en la placa. La Pico 2 no la tiene; con un módulo de **16 MB por SPI** y un SO mínimo sería teóricamente posible, aunque lento.
