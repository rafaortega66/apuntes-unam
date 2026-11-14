% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 21 · Manejadores de dispositivos y sistemas de archivos
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · miércoles 11 nov 2026 · Tema 3 (3.6 manejadores de dispositivos · 3.7 sistemas de archivos) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Manejadores de dispositivos (funciones, controladores dedicados y genéricos, categorías y modelo POSIX) e introducción a los sistemas de archivos: FAT, escritura asíncrona con *flush*, con y sin bitácora, y los de embebidos (ext2, ramfs/tmpfs, cramfs, initramfs, JFFS).

!!! Fuente
Fuente: NotebookLM (audio `FSE-Clase21.m4a`), 14 nov 2026. Lo marcado [material] viene de las diapositivas cargadas; ⚠️ marca datos dudosos. Continúa la Clase 20.

## 1. Manejadores de dispositivos y el sistema operativo como árbitro
Un controlador (*device driver*) es el software que gestiona el hardware y lo liga con cualquier otra capa (sistema operativo, *middleware*, aplicaciones). El sistema operativo es el árbitro del acceso a la entrada y salida.

!!! En simple
Es el mesero y el reglamento de la cocina: los clientes (aplicaciones) no entran a prender la estufa; le piden al mesero (el sistema operativo), que usa al cocinero especialista de cada aparato (el controlador) para que dos clientes no usen el mismo sartén. Límite: no todo se arbitra igual: la cámara es de uso exclusivo (salvo que un intermediario como OBS la retransmita), y el micrófono sí se comparte.

Todo periférico es, en la práctica, de entrada/salida, y las aplicaciones nunca lo tocan directo: el teclado entrega las teclas a la aplicación con el foco; si Zoom abre la cámara, queda bloqueada para otras; para mandar una webcam a YouTube y Twitch a la vez se usa OBS. (FFplay descarta cuadros si no alcanza; OBS los respeta aunque vaya más lento.)

La pila básica es hardware → controladores → sistema → aplicación (Arduino con `#include <Wire.h>`; la RP2040 con MicroPython, que ya trae *scheduler* y controladores I²C). En sistemas modernos se agregan capas de *middleware* que cuestan rendimiento.

Demostración: Ubuntu 24 contra Debian Bookworm, mismo kernel 6.1, misma glibc y mismo Xfce. Un alumno culpó al escritorio; la causa real es que Ubuntu empaqueta Firefox en Snap (contenedor) y Debian lo compila nativo: ~45 s y 1.4 GB contra ~10 s y 340 MB. Lo mismo con las apps bancarias hechas como páginas web dentro de un navegador.

Por qué importa: Cierra la tríada del núcleo: procesador, memoria y periféricos.
Error común: atribuir la lentitud al escritorio cuando es el empaquetado en contenedor.

## 2. Las funciones de un controlador
Las operaciones que el controlador ofrece al sistema operativo para inicializar, coordinar el acceso exclusivo, operar, ahorrar energía y retirar un dispositivo.

!!! En simple
El manual de un electrodoméstico en una casa compartida: cómo enchufarlo, presentarlo a la familia, prenderlo, ponerle candado mientras alguien lo usa, ajustar sus perillas, dormirlo y vaciarlo antes de desconectarlo.

| Función | Ejemplo de clase |
|---|---|
| Arranque / apagado | El disco duro energiza su electrónica, se identifica y pide ~1 A para girar; si no hay corriente, no inicializa. Al expulsar en Linux se oye el click y se apaga el LED (en Windows muchas veces el foco sigue prendido). |
| Habilitación / deshabilitación | Sacar el disco del bajo consumo, colocar el cabezal del CD, prender la lámpara del escáner, limpiar el cabezal de la impresora / dejarlo conectado pero en pausa. |
| Adquisición (*lock*) / liberación | Zoom adquiere la cámara para que nada más la encienda y la libera al terminar. |
| Lectura / escritura | Leer la imagen del escáner o un archivo / escribir la resolución de la cámara o un archivo. |
| Instalación / desinstalación | El mouse informa su DMA, su IRQ, cuántos botones tiene y su resolución, y el sistema le asigna recursos. Un mouse se desenchufa directo; un disco primero vuelca búferes, se desinstala, deshabilita y apaga. |

Funciones por familia: **ACPI** agrega *suspend*, *standby* y *wake* (el disco deja de girar, el Wi-Fi baja potencia, el monitor apaga la matriz; la impresora de inyección, al despertar, olvida que ya limpió y vuelve a purgar tinta). **USB**: el modo Control más su modo de transferencia (Interrupt, Bulk o Isócrono). **Almacenamiento**: montar, desmontar y expulsar.

Por qué importa: Explica por qué expulsar detiene el disco; conecta con IRQ, DMA y los modos USB de la Unidad 2.
Error común: creer que todo se puede desconectar en caliente como un mouse.

## 3. Controladores dedicados contra genéricos (pregunta de examen)
**Dedicados:** ligados al procesador; le dicen al sistema operativo cómo está organizada la CPU por dentro y con qué recursos está conectada. **Genéricos:** para todo el hardware externo al núcleo, soldado o conectado en la tarjeta madre.

!!! En simple
El dedicado es el amigo que te despierta tras la fiesta y te recuerda quién eres y con qué extremidades despertaste. El genérico te explica la casa donde amaneciste: tuberías, alacenas y enchufes. Límite: un mismo núcleo no sabe, hasta leer esa definición, si está solo o acompañado de otro núcleo y una FPU.

Al despertar, el procesador tiene «amnesia». Los **dedicados** le dicen cómo está organizada la memoria, cuánta caché tiene, dónde están las MMU y por qué pines llega a la RAM, o por qué líneas accede a un coprocesador o a una FPGA. Un Cortex-M0 puede estar solo (Blackpill) o con un hermano (RP2040); un Cortex-M4 solo en una Bluepill o, según el profesor, en un RP2350 con otro núcleo y FPU (⚠️ el RP2350 usa Cortex-M33). En Intel, le dicen si es un i5 de 2 núcleos y 4 hilos, de 4 y 8 o híbrido.

Los **genéricos** cubren buses (SMBus, I²C, PCI, PCMCIA), memoria y caché L2 externas, cómo acceder a los bancos de DRAM (el mismo Intel puede estar en una laptop con RAM soldada o en un mainframe), Ethernet, puerto serie y paralelo, y USB.

Por qué importa: Lo dijo como pregunta de examen.

## 4. Categorías de controladores y el modelo POSIX
Clasificación según el bus o periférico que gestionan y su integración por capas en POSIX.

!!! En simple
Camiones de carga (SATA), repartidores en bici (serie/TTY) y camionetas (USB) pueden circular por la misma autopista (PCI), pero un solo policía de tránsito (el controlador de interrupciones del kernel) decide quién pasa.

- **Puertos serie:** USART/UART, más I²C, SPI y SMBus (que controla los DIMM, la fuente y el ventilador [material: 10 a 100 kHz]).
- **Red:** Ethernet y Wi-Fi; las tarjetas buenas traen el stack TCP/IP y el cifrado dentro para descargar al CPU. Mencionó WiMAX, con antenas de hasta 5 km que hacen de repetidoras.
- **SATA y Flash:** la flash se guarda en bloques (no secuencial) con balanceo para que todos los bloques se desgasten igual.
- **Buses:** PCI, PCIe, USB, SMBus: qué está conectado, qué recursos pide y cómo acceder.
- **Interrupciones:** solo el kernel decide si las atiende, habilita o deshabilita.

En POSIX el controlador PCI es transversal (capturadoras, caracteres, red, USB, bloques SATA). Un disco remoto montado por red entra como dispositivo de bloques (el profesor dijo «NTFS, Network File System»; ⚠️ es NFS). Bluetooth trae al menos 256 puertos serie virtuales que llegan a las TTY, la terminal clásica de Linux.

No van a programar drivers: los manuales pasan de 10,000 páginas (Barry y Noergaard, ya en la bibliografía de Classroom).

## 5. Sistemas de archivos: FAT, escritura asíncrona y bitácora
Un sistema de archivos es una colección de archivos con sus protocolos de administración: en esencia, una tabla con los registros de cómo está estructurada la información en el dispositivo.

!!! En simple
El índice de un almacén de cajas numeradas (clústeres). Al escribir no corres al fondo del almacén por cada hoja: las dejas en un carrito junto a la puerta (búfer en RAM) y las llevas juntas al llenarse o al cerrar (flush). Con bitácora, antes de mover cajas anotas «estoy moviendo la caja 5», y si se va la luz sabes qué quedó a medias. Límite: si arrancas la USB sin *flush*, lo que estaba en el carrito desaparece aunque en pantalla pareciera guardado.

**FAT** (Microsoft, MS-DOS): FAT12 (disquetes), FAT16 y FAT32 (nombres 8.3 y archivos de máximo **4 GB**, como corrigió un alumno). Tiene tabla principal y copia de respaldo; un clúster no admite dos archivos, pero un archivo puede quedar repartido (fragmentación). Todo sistema de archivos se monta sobre el gestor del dispositivo.

**read** va al dispositivo y sube los datos; **write es asíncrono**: regresa de inmediato sin haber escrito. El controlador junta las escrituras en un búfer en RAM y las manda en bloque cuando se llena o tras un tiempo (por ejemplo ~3 minutos). Al copiar una película a una USB, los primeros 300 MB van a 120 MB/s llenando la RAM y luego cae a ~20 MB/s. Al expulsar se hace **flush**.

**Con bitácora** (*journaling*): trata el disco como una base de datos con transacciones atómicas; registra los cambios antes de hacerlos y, si se corta la luz antes del *commit*, hace *rollback* y solo se daña ese archivo. **Sin bitácora**: si se corta mientras se actualiza la tabla, se puede corromper toda.

| Sin bitácora | Con bitácora |
|---|---|
| FAT32, exFAT, ext2 | NTFS, ext3, ext4 |

Linux también usa ISO 9660 para CD (650 MB).

Por qué importa: Explica la expulsión segura y conecta con los RAM disk de las clases 18 y 20.
Error común: creer que write graba de inmediato; creer que todo sistema de archivos es persistente.

## 6. Sistemas de archivos para embebidos y enlaces duros
Sistemas de archivos para RAM o flash en embebidos, que priorizan ligereza, arranque comprimido o durabilidad de la flash.

!!! En simple
Equipo de campamento según el vehículo: navaja ligera sin bitácora (ext2), bolsa que se infla (ramfs), paquete al vacío que abres al llegar (cramfs, initramfs) o libreta hecha para escribir y borrar en flash sin quemarla (JFFS).

- **ext2** (~1995): sin bitácora, ligero; particiones de hasta 32 TB y archivos de 2–4 GB. En embebidos va en RAM disks y flash (si la flash se daña, ya no se lee de todos modos; no vale gastar escrituras en bitácora).
- **ramfs y tmpfs:** ramfs monta la RAM como disco que crece hasta un límite; sobre la RAM se monta ext2 para formar tmpfs (⚠️ el profesor dijo que ramfs «solo soporta un archivo»).
- **cramfs:** el primer sistema para cargar el kernel; solo lectura, sin bitácora, comprimido con zlib; aún en televisiones. Al encender, se lee, se descomprime en memoria y cede el control.
- **initramfs:** evolución de cramfs, solo lectura, con gzip (comprime más, pide más CPU) y puede descomprimir a cualquier destino. **Es el que carga GRUB al arrancar Linux** («Loading initial ramdisk»).
- **JFFS:** con bitácora, para flash NOR y NAND, límite de 128 MB, con enlaces duros.

Un **enlace duro** es el mismo archivo en varias rutas con distintos nombres: si modificas uno, cambian todos (un acceso directo de Windows no hace eso). `rdfind` busca duplicados (tamaño, primeros y últimos bits, hash) y los reemplaza por enlaces duros (un gamer recuperó ~3 GB en Steam).

Por qué importa: Conecta con el arranque de Linux (GRUB) y con el cuidado de la flash.
Error común: no reconocer initramfs, que aparece cada vez que arranca Linux.

## Pendiente / próxima clase
- Faltan algunos sistemas de archivos; continúa el martes («Continuamos el miércoles. No, el martes»).
- No se anunciaron tareas ni fechas. Los libros de controladores ya están en la bibliografía de Classroom.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Controladores dedicados contra genéricos.** «Vamos a tener dos tipos de controladores y esto es pregunta de examen: los dedicados y los genéricos».
- **Sistemas de archivos de embebidos: ramfs/tmpfs, cramfs, initramfs y JFFS.** sobre initramfs: «si no han oído este, están en el hoyo… ese sí se lo tienen que saber» (es el que carga GRUB).
- **Las funciones de un controlador (y suspend, standby, wake).** sin mención explícita de examen, pero recorrió la lista una por una con ejemplos.
- **Escritura asíncrona (write contra flush) y sistemas con y sin bitácora.** sin mención explícita; lo explicó a fondo y marcó con asterisco rojo la diferencia de bitácora.
- **Categorías de controladores y el esquema POSIX.** evidencia débil: aclaró que no van a programar drivers.

!!! Puntos clave
- El sistema operativo arbitra los periféricos; el controlador es la liga hardware-software.
- 10 funciones: arranque/apagado, habilitar/deshabilitar, adquirir/liberar, leer/escribir, instalar/desinstalar; ACPI: suspend, standby, wake.
- Dedicados (arquitectura interna del procesador) contra genéricos (todo lo externo en la tarjeta madre): pregunta de examen.
- write asíncrono + flush al expulsar; con bitácora (NTFS, ext3/4) contra sin bitácora (FAT32, exFAT, ext2).
- Embebidos: ext2, ramfs/tmpfs, cramfs (zlib), initramfs (gzip, lo carga GRUB), JFFS (flash, 128 MB, enlaces duros).

## Ponte a prueba
1. **Diferencia entre controlador dedicado y genérico.** El dedicado le describe al sistema la arquitectura interna del procesador (caché, MMU, coprocesadores, núcleos); el genérico administra el hardware externo de la tarjeta madre (buses, DRAM, Ethernet, USB).
2. **¿Qué estados agrega ACPI y qué hace la impresora de inyección al despertar?** Suspend, standby y wake; al despertar vuelve a purgar tinta porque olvidó que ya limpió.
3. **Mismo kernel, glibc y Xfce: ¿por qué Firefox tarda ~45 s en Ubuntu 24 y ~10 s en Debian?** Ubuntu lo ejecuta en un contenedor Snap; Debian lo compila nativo.
4. **¿Por qué write() regresa de inmediato?** Porque es asíncrono: los datos se juntan en un búfer en RAM y se escriben en bloque al llenarse, periódicamente o al hacer flush.
5. **Copias 1.5 GB con un búfer de 400 MB: va a 110 MB/s y cae a 18 MB/s; y pierdes un Word guardado hace un minuto al desconectar sin expulsar. ¿Qué pasó?** Los primeros 400 MB llenaron el búfer; luego se fue a la velocidad real de la USB. El Word seguía en el búfer y sin expulsar no hubo flush.
6. **¿Qué controlador le dice a un Cortex-M4 con qué hardware está, qué sistema de archivos usarías en 64 MB de flash con bitácora y qué carga GRUB?** El dedicado; JFFS; initramfs.
7. **Con bitácora contra sin bitácora ante un apagón.** Con bitácora se hace rollback de la transacción incompleta y el resto queda consistente; sin bitácora puede corromperse toda la tabla.
8. **cramfs contra initramfs.** Ambos solo lectura y sin bitácora; cramfs con zlib (televisiones), initramfs con gzip, a cualquier destino, el que usa GRUB.
