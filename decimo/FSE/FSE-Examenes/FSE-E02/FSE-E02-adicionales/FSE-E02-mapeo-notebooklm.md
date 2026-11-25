# FSE · Mapa de las clases 13–21 (después del 1.er parcial)

Fuente: NotebookLM, cuaderno FSE, audios FSE-Clase13 a FSE-Clase21, consultado el 24 nov 2026. La Clase 14 fue el 1.er examen (no hay audio).
La Clase 22 (18 nov) no tiene audio: el usuario no fue.

| Clase | Fecha | Tema del temario | Tema principal |
|---|---|---|---|
| 13 | 12 oct | 3.1 y 3.2 | Interfaz de aplicación y llamadas al sistema |
| 15 | 19 oct | 3.2 | Estados de procesos (GPOS) y tareas de tiempo real |
| 16 | 21 oct | Laboratorio, 3.9 | Kernel Linux para Raspberry Pi (Práctica 8) |
| 17 | 26 oct | 3.3 | Scheduling clásico (GPOS) |
| 18 | 28 oct | 3.3 | Scheduling de tiempo real: EDF, MLF y RMS |
| 19 | 4 nov | 3.4 | Administración de memoria |
| 20 | 9 nov | 3.4 y 3.5 | Memoria virtual; relojes y temporizadores |
| 21 | 11 nov | 3.6 y 3.7 | Manejadores de dispositivos y sistemas de archivos |

## Clase 13: interfaz de aplicación
- Lo que administra el SO: procesador, memoria y periféricos.
- Interfaz a nivel usuario (comandos del shell) y a nivel desarrollador (stdio, stdlib).
- **Los 6 pasos de una llamada a servicio** 🎯: enmascaramiento por el linker → argumentos en la pila y en el registro EAX → trampa `int 80h` → cambio de nivel usuario a kernel → desenmascaramiento y ejecución con privilegios → retorno.
- Aislamiento entre el espacio de usuario y el del kernel.
- **Programa (estático, en disco) vs. programa en ejecución vs. proceso (dinámico, en memoria)** 🎯.
- Tareas vs. procesos (la tarea tiene deadline).

## Clase 15: procesos y tareas
- Retroalimentación del 1.er parcial (50 preguntas: 25 abiertas y 25 de opción múltiple).
- El cargador (loader) sube el programa a memoria.
- Estados base: wait, ready y running (de wait se pasa a ready, nunca directo a running).
- Estados extendidos POSIX: pending, delayed, suspended, stopping y stopped.
- Sistema de tiempo real: calcula en tiempo constante antes de la siguiente entrada. Duro (falla catastrófica: reactores, aviación) vs. blando (se degrada: streaming, VoIP).
- Tipos de tareas: periódicas (periodo y deadline), aperiódicas (deadline sin periodo, p. ej. el frenado autónomo) y esporádicas (sin deadline, usan el tiempo que sobra).

## Clase 16: kernel Linux embebido (laboratorio)
- Compilación cruzada y toolchain; `menuconfig`.
- Elegir arquitectura (ARM vs. x86) y núcleos, y quitar drivers y módulos que no se usan para que pese menos y arranque más rápido.
- Ejecutables: binarios ELF vs. scripts con shebang.
- Práctica 8: kernel propio, arranque más rápido y otro logo en lugar de la frambuesa.

## Clase 17: scheduling clásico
- El scheduler decide quién usa el procesador entre las tareas que están en ready.
- FIFO / cooperativo; Shortest Job First (colas de prioridad); por prioridad (preemptivo vs. no preemptivo; en Linux −20 le gana a 20) 🎯 orden de las colas.
- Round Robin: quantum de 4 ms (250 Hz) en escritorio, 100 Hz en servidores y 1000 Hz en tiempo real.
- Colas multinivel contra la inanición (starvation); CFS.

## Clase 18: scheduling de tiempo real
- **Minimal Laxity First** 🎯: laxitud = tiempo que falta para el deadline − trabajo pendiente. Ejercicios en el pizarrón: P1(50,25) y P2(100,40); T1(50,30), T2(50,15) y T3(100,15).
- Resource Reservation: periodo y peor consumo esperado para el control de admisión.
- **Regla de oro**: Σ Cᵢ/Tᵢ ≤ 1.
- Rate Monotonic: el algoritmo estático óptimo (a menor periodo, mayor prioridad). Cota n(2^(1/n) − 1) → ln 2 ≈ 70 % (**no viene la demostración**).
- Calendario: última clase el 25 nov; proyecto el 24 nov.

## Clase 19: memoria
- Memory Allocation System (MAS) del kernel.
- Por qué paginar: con 64 KB y direcciones de 16 bits, mapear localidad por localidad pide 128 KB de tablas; con páginas de 1 KB la tabla baja a 64 bytes.
- Comunicación entre procesos: memoria compartida con semáforos vs. paso de mensajes (JSON/YAML).
- Fragmentación interna y externa.
- Garbage collection: Mark & Sweep, Mark & Compact y generacional (no aplica a C/C++).
- Memory pools en bloques de potencias de 2, configurados en el linker script.
- **First Fit, Next Fit, Best Fit, Worst Fit y Quick Fit** 🎯.

## Clase 20: memoria virtual y temporizadores
- Swapping: las páginas inactivas pasan al disco por DMA.
- Ancho de banda: un CPU de 64 bits a 3.2 GHz pide 25.6 GB/s; un SSD da 433 MB/s y un HDD 60 MB/s.
- Vida útil de un SSD: 3.2×10⁷ s/año contra celdas de 10 y 100 «megaescrituras» (así lo dice NotebookLM).
- Particiones: /boot y /usr en el SSD, /home en el HDD; zram (`/dev/zram0`, `swapon`).
- Tiempo síncrono (delay/sleep): con 0, entre 0 y 100 ms (sin garantía de exactitud) y más de 100 ms.
- **Temporizador asíncrono periódico**: semáforo binario que empieza en 0 + hilo trabajador para que las ejecuciones no se encimen («pregunta para entrar a Google»).
- `init_timer`, `add_timer` y `del_timer`, con caducidad en jiffies.
- `date` vs. `time`; deriva de los jiffies (4 a 10 min/año); NTP.

## Clase 21: drivers y sistemas de archivos
- El SO arbitra el acceso exclusivo (cámara) o compartido (micrófono).
- Capas intermedias (Snap) vs. compilación nativa.
- Las 10 funciones de un controlador: arranque, apagado, habilitar, deshabilitar, adquirir, liberar, leer, escribir, instalar y desinstalar. Energía ACPI: suspend, standby y wake.
- **Controladores dedicados (de la arquitectura interna del CPU) vs. genéricos (periféricos de la tarjeta madre)** 🎯.
- Categorías de drivers POSIX: serie, red, SATA/Flash (balanceo de desgaste), PCI/USB e interrupciones.
- Sistema de archivos, particiones y clústeres (FAT). Escritura asíncrona: búfer en RAM y `flush` al expulsar.
- Con bitácora (journaling: ext3/ext4, NTFS, JFFS) vs. sin bitácora (FAT32, exFAT, ext2).
- Embebidos: ext2, ramfs/tmpfs, cramfs (zlib), **initramfs (gzip, lo carga GRUB)** 🎯 y JFFS (flash; enlaces duros con `rdfind`).

Por ver en las diapositivas, sin audio: 3.8 Administración de energía (deck 17) y 3.9 Linux/Windows embebido y Android (deck 18). Seguramente se vieron en la Clase 22 (18 nov), a la que el usuario no fue.
