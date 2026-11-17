# **FSE · Guía para el examen final**

**Fundamentos de Sistemas Embebidos** · Semestre 2027-1 · 16 nov 2026  
*Hecha con NotebookLM a partir de todas las fuentes del cuaderno de la materia (audios de cada clase y material del profesor): hilo conductor del curso, unidades con sus conceptos explicados, lo que más probablemente viene y las conexiones entre conceptos. Acompáñala con el mapa mental (FSE-mapa-mental.pdf, en esta misma carpeta).*  
*Clases que no estaban en el cuaderno: 14\. Su resumen va en el Anexo al final.*

## ---

**HILO CONDUCTOR**

La historia del curso comienza entendiendo qué hace distinto a un **sistema embebido**: no es una computadora general, sino un sistema dedicado sujeto a restricciones estrictas de costo, energía, memoria y confiabilidad cuya **arquitectura** debe resolver esos desafíos desde el diseño (Diapositivas clase 1). Al bajar al silicio para diseñar esa arquitectura, el primer protagonista es el **procesador** (desde microcontroladores simples de 8 bits hasta ARM Cortex, ESP32, RP2040 y CPUs Intel) junto con su **mapa de memoria**, donde el hardware separa o unifica instrucciones, datos y periféricos, y distingue entre memorias volátiles rápidas y memorias no volátiles persistentes que interactúan mediante **modos de direccionamiento** (Clases 2–6; Diapositivas clases 2–4). Pero un procesador aislado no sirve si no reacciona al mundo físico ni mide el tiempo: por eso aparecen el **controlador de interrupciones (ICU)** para dejar de desperdiciar ciclos consultando pines, los **timers de hardware** para marcar el pulso periódico del sistema, y los buses externos (**USB**) e internos (**I²C, SMBus, SPI, I²S, UART, RS-232/485, One-Wire**) para hablar con sensores, actuadores y memorias, culminando el bloque de hardware con la **secuencia de arranque (*bootstrap*)** que despierta al procesador desde el vector de RESET hasta dejar todo listo para cargar software (Clases 7–12; Diapositivas clases 5–8).  
Cuando el sistema embebido crece y un simple ciclo infinito ya no basta, entra en escena el **sistema operativo** como árbitro de los tres recursos fundamentales que heredamos del hardware: el procesador, la memoria y los periféricos (Clases 7, 12, 13). Para usar esos recursos, las aplicaciones cruzan una frontera protegida mediante llamadas al sistema y se organizan como **procesos, hilos o tareas** (Clases 13, 15). A partir de ahí, el curso desarma cada componente del núcleo del sistema operativo: primero el ***scheduler***, que decide quién usa la CPU en cada instante y cómo garantizar plazos en **tiempo real** (Clases 17–18); después el ***Memory Allocation System*** **(MAS)**, que evita tablas gigantes mediante **paginación**, combate la **fragmentación** con algoritmos de asignación o **pozos de memoria** y protege los discos flash del desgaste usando **particionado** y **zram** (Clases 19–20); luego los **relojes y temporizadores por software**, que convierten un solo *timer* físico en retardos síncronos, tareas periódicas seguras y hora civil sincronizada por **NTP** (Clase 20); y finalmente los **manejadores de dispositivos (*drivers*)** y los **sistemas de archivos**, que estandarizan el acceso al hardware y garantizan que los datos persistan en RAM o flash sin corromperse ante apagones (Clase 21).

## ---

**UNIDAD 1: Introducción a los Sistemas Embebidos**

### **1.1 Sistema, Sistema Embebido y Arquitectura**

> * **(a) Problema que resuelve y conexión**: Antes de elegir procesadores o sistemas operativos, se necesita definir qué es un sistema embebido y por qué sus restricciones de ingeniería obligan a diseñar hardware y software a la medida (Diapositivas clase 1).  
> * **(b) Conceptos clave**:  
  * **Sistema (ingeniería)**: Conjunto de elementos interconectados o interrelacionados que realizan una función o cumplen un propósito específico; no todo sistema tiene entradas, salidas, ni es electrónico o digital, y existen sistemas abiertos y cerrados (Diapositivas clase 1). *Analogía*: Un automóvil o el sistema de transporte colectivo tienen piezas mecánicas, humanas y de control cooperando para mover personas, aunque no todo sistema requiera electrónica (Diapositivas clase 1). *Ejemplo*: En el laboratorio y en el mundo físico se mencionan desde un controlador PID, un automóvil o una bacteria hasta un medidor de CFE, donde bajar el umbral de detección de corriente de 5 microamperes a 5 nanoamperes hace que cualquier aparato conectado mueva el medidor (Clase 1; Diapositivas clase 1).  
  * **Sistema embebido (o integrado)**: Sistema de cómputo de propósito específico y de características más restringidas que una computadora personal o supercomputadora, caracterizado por: (1) funcionalidad más limitada en hardware y software que una PC, (2) diseño para una función específica y dedicada, y (3) requerimientos de calidad, confiabilidad y robustez superiores a otros sistemas de cómputo (Diapositivas clase 1). *Analogía*: Un cirujano especialista frente a un médico general: no atiende cualquier enfermedad ni instala aplicaciones arbitrarias, pero la única operación que realiza debe hacerla sin fallar. *Ejemplo*: Dispositivos como PDA o tabletas a menudo se llaman embebidos, pero **no son realmente sistemas embebidos** porque tienen propósito general; en cambio, un marcapasos o un chip GPS implantado en una mascota sí lo son (Diapositivas clase 1; Clases 19–20).  
  * **Arquitectura de un sistema embebido**: Abstracción o generalización del dispositivo donde los componentes de hardware y software (internos o externos) se representan como elementos interactivos, describiendo sus propiedades, comportamientos e interrelaciones sin mostrar detalles finos de código o circuitos (Diapositivas clase 1). *Analogía*: El plano arquitectónico de una casa frente a la lista de tornillos y cables eléctricos.  
> * **(c) Desafíos de diseño, modelos de desarrollo y clasificación (Diapositivas clase 1\)**:

| Eje | Opciones / Criterios vistos en clase   |
| :---- | :---- |
| **Desafíos arquitectónicos** | Costos; confiabilidad y seguridad; limitaciones físicas (procesamiento, memoria, batería); comerciabilidad y vendibilidad; requisitos específicos. |
| **Modelos de diseño** | **Big-bang** (sin planeación); **Programa y corrige** (ensayo y error, requisitos informales); **Cascada** (pasos secuenciales según necesidad); **Espiral** (diseño general por etapas ajustado en ciclos Planeación → Análisis → Desarrollo). |
| **Capas del modelo tipo** | 1\) Capa de Hardware (**obligatoria**); 2\) Capa de Software de Sistema (**opcional**); 3\) Capa de Software de Aplicación (**opcional**). |
| **Tipos (función / tecnología)** | *Por función*: entretenimiento, manejo de red, monitoreo, control. *Por tecnología*: sistema operativo, lenguaje, hardware (procesador, memoria, periféricos). |
| **Tamaños o alcances** | Micro, pequeño, mediano y ¿grande? *(Nota: los criterios numéricos exactos por tamaño no aparecen detallados en los fragmentos recuperados del audio de la Clase 1\)*. |

> * **(d) Puntos clave para examen**: Distinguir por qué una tableta o PDA no es un sistema embebido real, y recordar que definir la arquitectura resuelve los desafíos de costo, batería y confiabilidad de manera intrínseca (Diapositivas clase 1).

## ---

**UNIDAD 2: Organización, Arquitectura y Plataformas de Sistemas Embebidos**

### **2.1 El Procesador: Taxonomía, CISC vs. RISC y Plataformas Comerciales**

> * **(a) Problema que resuelve y conexión**: Elegida la arquitectura general en la Unidad 1, hay que seleccionar la unidad central de cómputo entendiendo cómo procesa flujos de instrucciones y datos, por qué difiere su conjunto de instrucciones y qué compilador/hardware exige (Clases 2–4; Diapositivas clase 2).  
> * **(b) Conceptos clave**:  
  * **Computadora (concepto básico)**: Máquina compuesta por elementos de entrada, elementos de salida, un procesador central y memoria (Diapositivas clase 2).  
  * **Taxonomía de Flynn**: Clasifica las computadoras según el número de flujos de instrucciones (*Instruction Pool*) y datos (*Data Pool*) que procesan sus unidades (*PU*) (Diapositivas clase 2).  
  * **CISC vs. RISC**: **CISC** (*Complex Instruction Set Computer*, ejemplo Intel 80x86) maneja instrucciones complejas y numerosas (millones de combinaciones/operaciones acumuladas y mezcla datos e instrucciones en memoria común), mientras **RISC** (*Reduced Instruction Set Computer*) reduce las instrucciones al orden de \~1,000 o \~60 mnemónicos y conceptualmente separa instrucciones de datos (Clase 2; Diapositivas clase 2). *Analogía*: CISC es un robot de cocina con 500 botones específicos ("haz pastel de chocolate"), mientras RISC tiene 10 herramientas básicas ("bate", "hornea", "mezcla") con las que construyes cualquier receta. *Ejemplo real*: Un Intel Core i7 Coffee Lake (2017) es CISC por fuera pero usa un predecodificador con **microfusión** que parte instrucciones CISC en microoperaciones tipo RISC internamente, sabiendo que el 60%–75% del programa solo carga y almacena; el Intel P6 ya tenía *pipeline* de **14 etapas** y dividía un cálculo de seno en **64 microoperaciones** (Clases 2, 4).  
  * **Ejecución especulativa y renombramiento de registros**: El procesador renombra registros de hardware para correr dos programas de 16 bits en registros de 32 bits (partes baja L y alta H) o dos programas de 32 bits en registros de 64 bits sin intervención de hilos ni semáforos del sistema operativo (Clases 2, 4).  
  * **Bus coherente vs. no coherente y acoplamiento**: En un *pipeline* **fuertemente acoplado** cambiar un módulo exige rediseñar todo el CPU (como tener todo el código en main()), frente al **débilmente acoplado** modular (como MVC) (Clase 3). Un **bus no coherente** escribe solo en caché y deja la RAM desactualizada; un **bus coherente** frena al CPU para actualizar caché y RAM garantizando consistencia de datos aunque sea más lento (Clase 3).  
> * **(c) Comparaciones técnicas (Clases 2–4; Diapositivas clase 2\)**:

| Taxonomía de Flynn | Significado y estructura en diagrama   |
| :---- | :---- |
| **SISD** | 1 flujo de instrucciones → 1 PU ← 1 flujo de datos. |
| **SIMD** | 1 flujo de instrucciones compartido → múltiples PUs ← múltiples flujos de datos. |
| **MISD** | Múltiples flujos de instrucciones → múltiples PUs encadenadas sobre un mismo flujo de datos. |
| **MIMD** | Múltiples flujos de instrucciones → múltiples PUs ← múltiples flujos de datos. |

| Plataforma comercial | Arquitectura y detalles clave vistos en clase   |
| :---- | :---- |
| **PIC18F452 / 4550** | Microcontrolador con un solo registro acumulador W, pila pequeña de 8 (o 31 en PIC18F452) niveles que desaconseja recursividad (ej. factorial(9) desborda pila de 8), bus de 16 bits \+ 5 bits (21 bits \= \>1 MB) (Clase 2; Diapositivas clase 3). |
| **ESP32 / ESP32-C3** | SoC con CPU RISC-V 32 bits (C3) o Xtensa LX6 (Harvard por buses I/D separados, aunque la SRAM/PSRAM externa revuelve datos e instrucciones que luego separan las cachés I-cache y D-cache). Incluye acelerador criptográfico SHA de 256 bits para AWS (Clase 2; Diapositivas clase 2). |
| **ARM Cortex-M0+ / M3 / M4 / M7** | Todos comparten el mismo conjunto de instrucciones base, pero difieren en hardware: **M0** no tiene FPU y emula división flotante inyectando \~30 instrucciones enteras en la ALU; **M3** multiplica y soporta flotante sin optimizar (calcula inverso y multiplica); **M4** optimiza punto flotante (multiplica y divide); **M7** añade unidad vectorial (BPU/FPU) para DSP; **Cortex-A** añade multimedia y usa compilador distinto (hf vs eabi) (Clases 2, 16). |
| **RP2040 / RP2350** | **RP2040** (Raspberry Pi Pico): doble núcleo ARM Cortex-M0+ (ARMv6-M), 264 KB/340 KB según versión (en clase: \<1 MB RAM, XIP/Cache, PIO0/PIO1, 2x SPI, 2x I²C, 2x UART, USB). **RP2350**: 2 núcleos Cortex-M4/M33 \[audio dice Cortex-M4 con hermanito y FPU\], **512 KB** RAM y **16 MB** Flash (Clases 2, 5, 21; Diapositivas clase 2). |
| **Intel x86 / x86-64** | **8086** (16 bits, 5–10 MHz, 220 dirs.), **286** (25 MHz, 2.66 MIPS, **modo protegido**), **386** (**IA32**, 32 bits, hasta 4 GB RAM, modo virtual **VM86**), **Itanium** (64 bits, IA64 incompatible con x86, North Bridge separado), **AMD64/x86-64** (retrocompatible con IA32 y controlador de memoria integrado), **Golden Cove** (2021, 12 puertos de ejecución, 502 entradas) (Clases 2–4). |

> * **(d) Errores comunes / puntos de examen**: No confundir la arquitectura externa de un procesador (RISC/CISC) con cómo organiza sus memorias: en el ESP32-C3 y ARMv6-M los datos e instrucciones viven revueltos en la SRAM/DRAM externa, pero se separan al entrar a las cachés L1 de instrucciones y datos del procesador (Clase 2; Diapositivas clase 2). En examen: saber explicar qué es un **bus coherente** (Clase 3).

### ---

**2.2 Mapa de Memoria, Memoria Volátil/No Volátil y Direccionamientos**

> * **(a) Problema que resuelve y conexión**: Una vez que el procesador sabe ejecutar instrucciones, necesita saber en qué direcciones físicas buscar código, variables y registros de periféricos, qué tipo de memoria física resiste cortes de energía y cómo referenciar operandos en ensamblador (Clases 5–6; Diapositivas clases 3–4).  
> * **(b) Conceptos clave**:  
  * **Mapa de memoria del sistema**: Distribución lógica de direcciones que separa memoria de programa, memoria de datos (registros de propósito general GPR, registros de funciones especiales SFR) y periféricos (Diapositivas clase 3). En **ARM**, coexisten el mapa de la arquitectura (buses en tarjeta madre) y el mapa del núcleo, intercalando bloques de RAM y periféricos para mantener retrocompatibilidad de direcciones entre versiones (Clase 5). *Regla crítica*: Los registros de periféricos **nunca se cachean**, porque leer una copia vieja de un puerto serie impediría ver el dato nuevo real del mundo exterior (Clase 5). *Ejemplo*: En el **PIC18F452**, el vector de RESET está en 0000h, las interrupciones de alta prioridad en 0008h y baja prioridad en 0018h; el **ATMega328p** mapea 32 registros (0–1Fh), 64 registros E/S (20–5Fh), 416 E/S externos (60–1FFh) y SRAM interna (200–21FFh, 8192 × 8\) (Diapositivas clase 3).  
  * **Memoria volátil vs. no volátil**: La **volátil** pierde la información sin energía y se divide en **estática (SRAM)** —que no caduca, es rapidísima, cara y se calienta mucho, por lo que se usa en cachés pequeñas (ej. 4 MB en Intel)— y **dinámica (DRAM)** —basada en capacitores parásitos que no se calientan, mucho más barata y densa, pero que pierde su carga y requiere **refresco cada \~60 ms** (60.03 o 60.3 ms) antes de caer a un voltaje ambiguo— (Clase 5). La **no volátil** conserva los datos sin energía: **ROM** (matriz fija), **PROM** (programable una vez), **EPROM** (borrable 15 min con luz UV y grabada a 13 V), **EEPROM** (borrable eléctricamente a 25 V, muy lenta en ms por byte), **Flash** (evolución matricial en **clústeres** de 64 KB, 128 KB o 4 MB que baja el tiempo efectivo de escritura a nanosegundos aunque muere el clúster si falla un bit), medios **magnéticos** (cintas secuenciales, disquetes, HDD) y **ópticos** (eternos, grabados con láser de 1 kW) (Clase 6). *Analogía*: SRAM es una pizarra luminosa encendida al instante pero carísima de mantener; DRAM es un balde con una gotera constante que debes rellenar cada 60 ms; Flash es una hoja dividida en cuadritos grandes que borras por bloques completos.  
  * **Modos de direccionamiento (Motorola 68HC11 como modelo didáctico)** (Clase 6; Diapositivas clase 4):

| Modo de direccionamiento | Definición técnica | Ejemplo de clase   |
| :---- | :---- | :---- |
| **Inherente** | No necesita operandos; la operación actúa implícitamente sobre registros o control. | NOP, retorno de subrutina (RTS), corrimientos, reinicio. |
| **Inmediato** | El dato constante viene inmediatamente después del código de operación. | ADDA \#8 (suma constante 8 al registro A); en PIC MOVLW 7Fh. |
| **Extendido** | El código de operación va seguido de la dirección completa (palabra completa) donde reside el dato en memoria. | Sumar al registro A el contenido de una dirección completa de 16 bits. |
| **Directo** | Igual al extendido pero abreviado (media palabra) para acceder rápido únicamente a la **parte baja** de la memoria sin leer ceros altos. | Variables frecuentes del kernel o programas pequeños. |
| **Indexado** | Código de operación \+ desplazamiento de 8 bits sin signo sumado a un registro índice (X o Y) para localizar el **dato**. | ADDA 5,X (recorre vectores y matrices). |
| **Relativo** | Código de operación \+ desplazamiento de 8 bits con signo sumado al **Contador de Programa (PC)** para calcular la **siguiente instrucción**. | Saltos condicionales/incondicionales (JMP, JZ, JNZ, CALL). |

> * **(d) Errores comunes / puntos de examen**: Confundir **indexado** (calcula la dirección de un **dato** usando X/Y \+ delta) con **relativo** (calcula la dirección de la **siguiente instrucción** usando PC \+ delta) (Clase 6). También no confundir memoria Flash (no volátil) con DRAM (volátil con refresco de 60 ms) (Clase 5).

### ---

**2.3 Controlador de Interrupciones (ICU) y Temporizadores de Hardware**

> * **(a) Problema que resuelve y conexión**: Si el CPU consulta periódicamente en un ciclo (*busy wait / polling*) si llegó un byte por el puerto serie o si se presionó un botón, desperdicia energía y ciclos de reloj. Las **interrupciones** invierten el control para que el hardware avise al CPU, y los **timers** permiten generar interrupciones periódicas precisas (Clase 7; Diapositivas clase 5).  
> * **(b) Conceptos clave**:  
  * **Interrupción y Controlador de Interrupciones (ICU / PIC / APIC)**: Señal que interrumpe el flujo de ejecución de instrucciones de un programa para que el procesador atienda una petición externa (Clase 7; Diapositivas clase 5). *Analogía*: En lugar de asomarte a la puerta cada segundo para ver si llegó el repartidor (*busy wait*), sigues cocinando hasta que suena el timbre. *Tipos*: **Enmascarables** (ignorables mediante máscara Intr\_Mask y compuerta AND con Intr\_Pending: PWM, timers, teclado, serial, banderas) y **no enmascarables** (no ignorables: **Reset** y **Overheat**, "como cuando te habla tu madre") (Clase 7; Diapositivas clase 5).  
  * **Identificación y Prioridad**: **Por tabla** (la tabla CPU apunta a una rutina genérica en software que busca qué línea fue, más lenta) vs. **por vector** (la propia UCI entrega el vector o apuntador directo a la ISR, instantánea pero costosa en hardware embebido) (Clase 7; Diapositivas clase 5). En prioridad: **mononivel** (todas iguales) vs. **multinivel** (se atienden primero las de mayor prioridad) (Diapositivas clase 5).  
  * **Desencadenamiento (*trigger*)**: **Por valor (0 o 1\)**, donde la interrupción permanece activa mientras el pin siga en ese nivel (ej. botón físico de Reset u Overheat; desastroso en CPUs rápidos de 8 MHz recibiendo datos serie a 9600 bps porque se atora \~1000 pulsos durante la duración del byte), vs. **por flanco (*edge*)**, donde solo dispara un instante en el cambio de nivel (Clase 7; Diapositivas clase 5).  
  * **IRQ y DMA**: En el bus **ISA** (16 bits) cada IRQ es un alambre dedicado que exige pistas de igual longitud; en **PCI** (32 bits) un multiplexor permite compartir IRQs (Clase 7; Diapositivas clase 5). El **DMA** (*Direct Memory Access* / *"Direct Memory Allocation"* en diapositiva \[diapositivas-clase-05.pdf\]) permite que hardware externo atienda interrupciones y escriba directo en RAM **saltándose al CPU** (Diapositivas clase 5).  
  * **Temporizador o *Timer* de hardware**: **Contador en cuenta regresiva que activa una interrupción al llegar a cero y reinicia el conteo automáticamente**; también llamado **reloj de pared**, es esencial en todas las computadoras y todo sistema operativo requiere al menos uno (Clase 7; Diapositivas clase 5).  
  * **Cristal oscilador (XTAL)**: Su precisión se mide en **PPM** (*Parts per Million*); **12 PPM ≈ 1 segundo de error por día**, mayor precisión cuesta más y requiere batería (no siempre disponible), por lo que **se recomienda NTP como respaldo** en dispositivos autónomos (estaciones meteorológicas, chips en animales) (Clase 7; Diapositivas clase 5).  
> * **(c) Las 4 características de los Timers — "Todas son preguntas de examen" (Clase 7; Diapositivas clase 5\)**:

| Característica del Timer | Valores / Opciones posibles   |
| :---- | :---- |
| **1\. Modo** | *Free run* (reinicia al llegar a cero indefinidamente) o *One shot* (corre una vez y se detiene). |
| **2\. Dirección de conteo** | Incrementa o decrementa. |
| **3\. Rango** | Número de bits del contador. |
| **4\. Fuente** | Oscilador interno o señal externa (ej. *encoder* de motor, audio, electromiógrafo). |

> * **(d) Puntos recalcados para examen**: La definición exacta de *timer* y sus **4 características** (*"Todas son preguntas de examen"*), la diferencia entre *trigger* por valor vs. flanco y cómo funcionan las compuertas de enmascaramiento (Clase 7; Diapositivas clase 5).

### ---

**2.4 Bus Serie Universal (USB) e Interconexión de Dispositivos**

> * **(a) Problema que resuelve y conexión**: Los puertos clásicos (Serial a 1.5 Mbps, Paralelo a 2.5 Mbps y SCSI caro con conector DB25 a 20 MB/s) eran lentos, voluminosos e incompatibles entre sí; USB unificó la conexión hacia la PC/host, mientras que dentro de la placa madre o entre chips embebidos se usan buses seriales más simples de pocos pines (\<100 MHz, \<1 Mbps típico) para abaratar el hardware (Clases 8–10; Diapositivas clases 6–7).  
> * **(b) Conceptos clave**:  
  * **USB vs. IEEE 1394 (Firewire)**: Firewire (1995) era más potente (30 V, 1.5 A \= **45 W**, hasta **3200 Mbps**, coprocesador independiente y búfer externo, síncrono/asíncrono) pero muy costoso; ganó **USB** por económico (5 V, 1 A \= **5 W**, hasta **12 Mbps** en 1.1, anclado al procesador usando RAM buffer, asíncrono) (Clase 8; Diapositivas clase 6).  
  * **Topología y física de USB 2.0**: **Topología en árbol/pirámide de máximo 7 niveles** (Nivel 1: *Host* con *Root Hub* obligatorio; intermedios: *Hubs* encadenados; hojas: *Funciones* o periféricos). Usa **par trenzado diferencial** (D+ y D-) con un buffer y un negador muy baratos que detectan ruido automáticamente si ambas líneas caen iguales. Al conectarse, todo dispositivo recibe **100 mA** garantizados por derecho base (hasta 800 mA en USB 3.0 si negocia potencia) (Clases 8–9).  
> * **(c) Tablas comparativas clave de USB y Protocolos de Interconexión (Clases 8–11; Diapositivas clases 6–7)**:

| Versión USB | Velocidad y canales | Notas de arquitectura   |
| :---- | :---- | :---- |
| **USB 1.1** | 12 Mbps, 1 canal | Incluye *Low Speed* (humanos, 1.5 Mbps en especificación clásica) y *Full Speed* (12 Mbps, audio/módem). |
| **USB 2.0** | 480 Mbps, 1 canal | *"Se come"* a USB 1.1 (retrocompatible total); modo *High Speed* (25–400+ Mbps) para video y discos. |
| **USB 3.0 / 3.2** | 3 canales (Gen1: 5 Gbps, Gen2: 10 Gbps) | Encapsula a USB 2.0 añadiendo 2 canales SuperSpeed y mayor potencia de salida. |

| Modo de transferencia USB 2.0 | Uso y característica principal (Diapositivas clase 6; Clases 9, 21\)   |
| :---- | :---- |
| **Control** | Obligatorio en todo dispositivo USB; configuración e inicialización. |
| **Bulk** | Transmisión de bloques grandes de datos en ráfagas (alto volumen, ej. discos). |
| **Interrupt** | Paquetes cortos que representan cambios físicos (mouse, teclado). |
| **Isochronous (Isócrono)** | Simulación síncrona mediante **reserva fija de ancho de banda** (si solo usas el 10% de tu rebanada, nadie más puede usar el resto; ej. audio/ultrasonido/motores). |

| Protocolo | Alambres | Tipo / Reloj | Topología / Maestros | Velocidades y detalles críticos vistos en clase   |
| :---- | :---- | :---- | :---- | :---- |
| **I²C** | 2 (SCL, SDA) \+ GND | Síncrono | Multimaestro, múltiples esclavos | Colector abierto con resistencias *pull-up* (solo escribe ceros, permite mezclar 3.3 V y 5 V); Start \= bajar SDA antes del reloj; Stop \= subir SDA después; transmite byte a byte con ACK/NACK. Modos: Estándar 100 kbps (400 pF), Rápido 400 kbps (400 pF, RP2040), Fast+ 1 Mbps (55 pF), Alta velocidad 1.7–3.4 Mbps (100 pF). |
| **SMBus** | 2 (SCL, SDA) \+ GND | Síncrono | Punto a punto (1 maestro, 1 esclavo) | Basado en I²C pero lento (**10–100 kHz**); sin dirección de esclavo, usa bits libres para modo comando en *motherboards* (fuente, ventilador, temperatura, DRAM). |
| **SPI / QSPI** | 4 (SCK, MOSI/TX, MISO/RX, CS) | Síncrono | Maestro-esclavo (CS por esclavo) | Hasta **80 MHz** o más. A 80 MHz: SPI estándar \= **10 MB/s**, QSPI (4 líneas) \= **20 MB/s**, Octa-SPI \= **40 MB/s** (o **80 MB/s** simétrico). Usado por Intel para cargar BIOS desde Flash ROM y en MicroSD. |
| **I²S** | 3 (CLK, SD, WS) | Síncrono | Maestro-esclavo | Inventado por Philips exclusivamente para audio digital; hasta **3 MHz**. |
| **UART** | 2 (TX, RX) cruzados (*null-modem*) | Asíncrono (baudios) | Punto a punto | Reloj interno por acuerdo previo de **baudrate** (ej. 9600, 56600, 115200 bps); muestrea a medio bit tras flanco de bajada. Paquete típico **N81** \= 1 start \+ 8 datos \+ sin paridad \+ 1 stop (10 bits/byte). Control de flujo HW (RTS/CTS, \+2 alambres) o SW (XON Ctrl+S / XOFF Ctrl+Q). Bluetooth emula hasta 60 puertos seriales virtuales sobre UART. |
| **RS-232 vs RS-422/485** | 2+ (datos) / 4 (con potencia en 485\) | Capa física de UART | **232**: punto a punto (1:1). **422/485**: multipunto | **RS-232**: no diferencial, ± 12 V (hasta ± 5 V), máx. **15 m** y **20 kbps**. **RS-485**: diferencial (recupera señal con ± 1.5 V), hasta **32 receptores**, **1.2 km**, **10–35 Mbps**, estándar industrial. |
| **One-Wire** | 1 señal (+ GND; alimentación parásita) | Asíncrono (tiempos fijos) | Maestro-muchos esclavos | Reset \= línea en bajo **480 µs** (8 bits a 9600 bps con F0); lectura/escritura a 115200 bps enviando FF o 00\. Enumeración por búsqueda binaria (Search ROM leyendo bit \+ complemento) sobre ID único de **64 bits** (8 bits familia \+ **48 bits** dispositivo \+ CRC). Comandos: Read ROM (0x33), Skip ROM, Match ROM. En Linux se lee/escribe como archivo en /sys/bus/w1/.... |

> * **(d) Puntos recalcados para examen**: El profesor dijo explícitamente en la Clase 8 que el **límite máximo de 7 niveles en USB 2.0** y sus **modos de operación** vienen en el examen; en la Clase 9 pidió saberse de memoria de cada mecanismo de interconexión su **topología, configuración (maestro/esclavo o pares), frecuencia, nombre y número de líneas**.

### ---

**2.5 Secuencia de Arranque (*Bootstrap*)**

> * **(a) Problema que resuelve y conexión**: Con todo el hardware cableado e interconectado, al encender la energía el procesador tiene "amnesia" (ni la memoria RAM ni las cachés están listas ni sabe cuántos núcleos tiene); necesita una rutina determinista desde hardware para despertar e iniciar el sistema operativo (Clase 12; Diapositivas clase 8).  
> * **(b) Conceptos clave**:  
  * **Hard Reset vs. Soft Reset**: **Hard Reset** ocurre al suministrar corriente (*power-on*), estabilizando voltajes y oscilador principal (en baterías un microcontrolador/CPLD estabiliza el *power*); **Soft Reset** ocurre por interrupción (botón de reset, *Watchdog Timer* por bloqueo en una instrucción, *Overheat* o despertar tras **suspensión ACPI**, donde la RAM retiene el SO y el procesador reinicia pero salta directo a reanudar sin recargar el sistema operativo) (Clase 12; Diapositivas clase 8).  
  * **BSP (*Bootstrap Processor*) vs. AP (*Application Processor*)**: Al recibir RESET, todos los núcleos/hilos se tratan como procesadores completos; el **LAPIC** asigna el bit BSP en **1** al procesador elegido como **BSP** (arranca el sistema) y en **0** a todos los **AP** (ejecutan autoprueba y quedan en WAIT-for-SIPI) (Diapositivas clase 8).  
  * **Vector de RESET**: Dirección fija inicial donde el procesador hace su primer *fetch* (en Intel FFFFFFF0h; otras direcciones fijas para ARM Cortex-M/R, Cortex-A y PowerPC) (Clase 12; Diapositivas clase 8).  
> * **(c) Flujo general del arranque en plataformas Intel — "Funcionamiento general" para examen (Clase 12; Diapositivas clase 8\)**:  
  1. Estabilización de energía/reloj y *fetch* del vector de **RESET** en el BSP (mientras los AP esperan SIPI).  
  2. Salto corto/largo a código ROM, cambio a **modo protegido** y actualización de microcódigo.  
  3. Deshabilitar cachés, configurar caché segura y rehabilitar cachés.  
  4. Inicializar memoria (DRAM) y probarla (si falla: HALT); configurar pila DRAM, copiar código/datos de ROM a RAM y saltar a DRAM (aquí inicia la BIOS/UEFI).  
  5. Inicializar y habilitar interrupciones (APIC).  
  6. **Detección multiproc**: el BSP envía una interrupción **SIPI** a los primeros 4 KB de RAM y se inicia una **condición de carrera con semáforo** donde cada AP suma 1 al contador, registra su APIC ID y entra en espera de INIT.  
  7. Deshabilitar cachés para reglas finales avanzadas, rehabilitarlas, descubrir y configurar dispositivos **PCI/ISA** y enrutamiento de interrupciones.  
  8. Cargar imagen del sistema operativo y saltar al cargador (*bootloader*) —en **UEFI** los AP ayudan a inicializar periféricos y cargar el SO en paralelo, a diferencia de **BIOS** donde solo el BSP lo hace—.  
> * **(d) Puntos clave para examen**: Un alumno preguntó en Clase 12 si debían memorizar las 32 cajas exactas o el orden general; el profesor aclaró que se pregunta el **funcionamiento general y el orden correcto de las fases** (no las direcciones hexadecimales ni los 32 pasos de memoria).

## ---

**UNIDAD 3: Sistemas Operativos para Plataformas Embebidas**

### **3.1 Interfaz de Aplicación, Procesos, Hilos y Tareas**

> * **(a) Problema que resuelve y conexión**: Una vez que el *bootstrap* entrega el control al sistema operativo (Linux o RTOS como FreeRTOS/VxWorks), el SO debe aislar la memoria de cada programa (para evitar fallos de segmento o corrupciones como desbordar la pila hacia el kernel) y ofrecer una puerta segura para pedir servicios del núcleo (Clases 12–13).  
> * **(b) Conceptos clave**:  
  * **Interfaz de aplicación y saltos de privilegio**: Conjunto de comandos de usuario (cat, sort, ls) y llamadas de librerías (stdio, stdlib como printf, malloc) que solicitan servicios al kernel. En **Linux** hay **1 salto** (usuario → kernel); en **Windows** hay **2 saltos** (usuario → capa ejecutiva → kernel) (Clase 13).  
  * **Programa, Proceso, Hilo y Tarea**: Un **programa** es el archivo ejecutable pasivo en disco con un encabezado que indica formato, arquitectura de bits (16/32/64) y memoria inicial requerida (Clase 15). Un **proceso** es la estructura instanciada en memoria por el SO con su espacio aislado (PID) y recursos; en sistemas de propósito general (**GPOS** como Linux/Windows) el **hilo** (*light process*) es la unidad mínima de ejecución dentro de un proceso y **comparte memoria y prioridad** con los demás hilos de su proceso padre (Clases 13, 15). En un **RTOS** (como **FreeRTOS** o **VxWorks**), existe un solo superproceso raíz sin prioridad propia y la unidad mínima es la **tarea**, que posee atributos propios, prioridad individual y ***deadline***, y cuyos accesos se verifican en compilación porque el binario corre estáticamente (Clases 13, 15).  
> * **(c) Los 6 pasos de una llamada a servicio — "Pregunta de examen" (Clase 13\)**:  
  1. **Enmascaramiento (en compilación/enlace)**: El **linker** resuelve las llamadas (ej. malloc / printf) contra librerías dinámicas (.so con identificadores retrocompatibles de **64 bits para librería \+ 64 bits para llamada**, evitando el *"DLL Hell"* de Windows).  
  2. **Paso de argumentos**: Se colocan primero los argumentos en la pila y al final la llamada, y se carga en un registro del CPU (ej. EAX) el número de servicio (ej. 45 para sys\_brk).  
  3. **Despacho de la trampa**: Se genera una interrupción por software (ej. int 80h en x86) que dispara la trampa hacia el vector de interrupciones.  
  4. **Cambio de nivel**: Se transfiere el control desde el modo usuario sin privilegios al modo kernel (en segmentos distintos de memoria).  
  5. **Desenmascaramiento y ejecución**: El kernel abre la trampa, traduce el identificador al servicio correspondiente (ej. sys\_brk ampliando memoria o buscando en *fastbins*) y lo ejecuta en nombre del proceso.  
  6. **Retorno**: El kernel devuelve el resultado (ej. apuntador asignado) y restaura el flujo al proceso en modo usuario.  
> * **Estados de un proceso (Clase 15\)**: Los **3 estados base** son **wait** (cargándose en memoria o bloqueado esperando un periférico como scanf() o la red; nunca pasa directo de *wait/blocked* a *running*, sino a *ready*), **ready** (listo y formado en la cola esperando CPU) y **running** (uno por núcleo ejecutando instrucciones). En sistemas POSIX existen además **pending** (cargado por cron esperando su hora), **delayed** (demorado por tarea de mayor prioridad, ej. respaldo vs. consulta de servidor), **suspended** (pausado con 0% de CPU), **stopping** (ejecuta destructores y libera puertos/cámara antes de morir) y **stopped** (terminado esperando limpieza).  
> * **(d) Errores comunes / puntos de examen**: Los **6 pasos de la llamada a servicio** (*"Pregunta de examen"*), distinguir qué unidad mínima existe en **GPOS** (**hilo**) frente a **RTOS** (**tarea**, mientras FreeRTOS ni siquiera soporta procesos dinámicos ni cargador), y recordar que un proceso bloqueado en wait siempre regresa primero a ready y nunca directo a running (Clases 13, 15).

### ---

**3.2 Planificación (*Scheduler*) y Sistemas de Tiempo Real**

> * **(a) Problema que resuelve y conexión**: Con múltiples procesos, hilos o tareas en estado ready, el *scheduler* decide cuál ocupa el núcleo en cada instante y cómo garantizar en sistemas embebidos que ninguna respuesta crítica llegue tarde (Clases 15, 17, 18).  
> * **(b) Conceptos clave**:  
  * **Tiempo real (definición exacta)**: No significa "rápido", sino **que la salida se calcula antes de que llegue la siguiente entrada y responde en tiempo constante** (ej. audio a 48 kHz requiere MHz, frenos ABS a 200 km/h avanzan 1 mm/ms y les basta 1 kHz, y un horno de pan Bimbo tolera segundos) (Clase 15). Se divide en **tiempo real duro** (si falla un plazo el sistema se desestabiliza irreversiblemente con consecuencias catastróficas: reactor nuclear, colisionador de hadrones, alerones de avión, cablebús) y **tiempo real blando/flexible** (degrada calidad de servicio pero se reencausa: llamadas por WhatsApp, *streaming*, enrutadores) (Clase 15).  
  * **Tipos de tareas**: **Periódicas** (tienen periodo T y *deadline*, base del análisis de planificabilidad), **aperiódicas** (tienen *deadline* pero no periodo, ej. calcular frenado ante un obstáculo inesperado; se modelan como periódicas en el peor caso para garantizar planificabilidad) y **esporádicas** (sin *deadline*, ocupan el tiempo sobrante; desde tiempo real todas las tareas de GPOS se ven esporádicas) (Clase 15).  
  * **Minimal Laxity First (MLF)**: Política dinámica que elige la tarea con menor holgura o laxitud: Laxitud \= (Tiempo restante hasta el deadline) \- (Trabajo pendiente por consumir) (Clase 18).  
  * **Resource Reservation**: Módulo acoplable a cualquier política donde cada tarea declara en su encabezado su periodo y peor consumo esperado para decidir matemáticamente al admitirla si cabe o se rechaza (Clase 18).  
  * **Rate Monotonic Scheduling (RMS)**: Algoritmo **estático óptimo** donde las prioridades se fijan antes de ejecutar según la regla **a menor periodo, mayor prioridad** (Clase 18).  
> * **(c) Algoritmos de planificación y fórmulas clave (Clases 17–18)**:

| Algoritmo | Funcionamiento, costos y uso en clase   |
| :---- | :---- |
| **Simple FIFO (Cooperativo)** | Ejecuta en orden de llegada hasta que la tarea termina o se bloquea; presente en \~80–90% de embebidos simples (while(1) o FreeRTOS por demanda). |
| **Shortest Job First (SJF)** | Usa cola de prioridad ordenada por menor duración estimada (peor caso); reordenar en árbol toma O(Nlog N) y buscar O(log N). |
| **Priority** | Asigna prioridad fija por tarea (en Linux \-20 es mayor que 20); puede ser **preemptivo** (interrumpe a las de menor prioridad). |
| **Round Robin (RR)** | Divide el tiempo en rebanadas (*quanta*) de **4 ms** en escritorio (250 Hz; servidores 100 Hz; RT 1 ms / 1 kHz). Variantes: **RR con prioridad** y **RR preemptivo** con **árbol de colas** para evitar que dos tareas altas acaparen el CPU (para 300 procesos Linux, altura de árbol lceil log2 300 rceil \= 9). |
| **CFS (Linux moderno)** | *Completely Fair Scheduler* con políticas: Normal (RR), Batch (lotes a completitud en servidores), Idle (mínima prioridad, estaciones meteorológicas), y tiempo real RT-FIFO / RT-RR (prioridades **1 a 99**, donde **RT1 \> RT99 \> \-20 \> 20**). Preempción: *None* (servidores), *Voluntary* (mixto) o *Full* (embebidos). |
| **EDF *(sin siglas explícitas en fragmento)* / MLF** | En Clase 18 se describe primero la política fija por el programador, luego la que escoge dinámicamente **la que se entrega primero** (EDF) y luego **MLF** (menor holgura). *Ejercicio 1 en vivo*: P1(T=50, C=25) y P2(T=100, C=40): uso de P1 \= 25/50 \= 0.5 (50%); si P1 tiene prioridad, cumplen ambas; si P2 corre primero (0–40), P1 falla su *deadline* en 50\. Con MLF en t=0: L1\=50-25=25 \< L2\=100-40=60, gana P1 y cumple. *Ejercicio 2 en vivo*: T1(50,30), T2(50,15), T3(100,15) apenas cumple asumiendo *scheduler* de **tiempo 0** (si el *scheduler* gasta 1 unidad, falla). |

> * **Fórmulas obligatorias de Tiempo Real (Clase 18\)**:  
  * **Uso de procesador**: Ui \= (Ci)/(Ti).  
  * **La Regla de Oro**: Σi=1n (Ci)/(Ti) ≤ 1\. *Ejercicio fallido de clase*: (35)/(50) \+ (15)/(50) \+ (15)/(100) \= (70+30+15)/(100) \= 1.15 \> 1, por lo que falla inevitablemente en el segundo ciclo de 50 ms.  
  * **Cota de planificabilidad de RMS**: U(n) \= n(21/n \- 1\) xrightarrown → ∞ ln(2) ≈ 0.693 ≈ 0.7 (70%), lo que implica que desde **4 tareas** (ej. sensado, filtrado, control y actuación) no debe superarse el **70%** de uso de CPU.  
> * **(d) Errores comunes / puntos de examen**: Confundir periodo T con consumo C al calcular uso de CPU; creer que tiempo real significa velocidad bruta; en Linux recordar que un número nice o RT **menor** indica **mayor** prioridad (RT1 \> RT99 \> \-20 \> 20); el profesor advirtió explícitamente en Clase 18 que **la demostración matemática del límite de RMS NO viene en el examen**, pero los ejercicios de MLF y la Regla de Oro sí.

### ---

**3.3 Administración de Memoria (MAS, Paginación, Asignación, GC, Pozos y Memoria Virtual)**

> * **(a) Problema que resuelve y conexión**: Repartido el CPU por el *scheduler*, el sistema operativo necesita asignar RAM a los procesos, permitirles comunicarse cuando cooperan, impedir que la fragmentación paralice sistemas de larga vida y aprovechar el almacenamiento secundario sin destruir unidades flash (Clases 19–20).  
> * **(b) Conceptos clave**:  
  * **Paginación y cálculo de tabla**: Administrar memoria dirección por dirección es inviable. *Ejercicio en vivo (Clase 19\)*: una memoria de **64 KB** en arquitectura de **16 bits** tiene **32K localidades**. Cada renglón necesitaría 16 bits de dirección \+ 2 bits de banderas (*libre/ocupado* y *limpio/sucio*, donde *limpio* \= datos congruentes y *sucio* \= basura) \+ 8 bits para **256 procesos** \= 26 bits, redondeados a **32 bits (4 bytes)**; 32K × 4 bytes \= 128 KB (el doble de la RAM disponible). Al dividir en **páginas de 1 KB** (32 páginas), cada entrada usa **5 bits** de ID de página (corrigiendo en clase el desliz de 4 bits: 25\=32) \+ **5 bits** de proceso \+ 6 bits de banderas \= 16 bits (1 palabra), ocupando **32 palabras \= 64 bytes**; con páginas de **512 bytes** (64 páginas) ocupa **64 palabras \= 128 bytes**.  
  * **Comunicación entre procesos (IPC) y RPC**: **Memoria compartida** (variables globales visibles protegidas por semáforos/mutex; rapidísima sin serialización ni cifrado, estándar en embebidos pequeños compilados en C/FreeRTOS) frente a **Paso de mensajes** (obligatorio entre sistemas heterogéneos o distribuidos mediante JSON/YAML/XML, que exige **serialización/deserialización** y cifrado costosos en CPU). Sobre ambos se construye **RPC** (*Remote Procedure Call*) para recibir respuesta bidireccional (Clases 18–19).  
  * **MAS (*Memory Allocation System*) y Fragmentación**: Componente del kernel que carga/descarga procesos, reserva/libera bloques, rastrea ubicación física (RAM/GPU/disco), mapea espacios virtuales a físicos vía la **MMU** y minimiza la **fragmentación** (huecos no contiguos dejados al morir procesos intercalados; mientras en GPOS se suspende y compacta, en embebidos de baja gama falla la carga) (Clases 19–20).  
  * **Recolección de basura (*Garbage Collection*)**: Heredada de Java para liberar objetos sin referencias. **Mark & Sweep** lleva contador de referencias (al cerrar llave } decrementa; en 0 borra la entrada de tabla, no bloquea pero **fragmenta mucho**); **Mark & Compact** recorre y compacta objetos vivos eliminando huecos, pero **bloquea todo el sistema** (causó fallos graves en las primeras versiones de Linux al usar *pipes* en bash); **Generacional** revisa frecuente a objetos jóvenes y poco a veteranos (optimizado hoy con modelos ocultos de Markov). *Regla crítica*: Requiere *middleware* y **no existe en C/C++ nativo** (Clase 19).  
  * **Pozos de memoria (*Memory Pools*)**: Reserva previa de bloques en **potencias de 2** (ej. 32 bytes para int, 64 bytes para long/double, 128 bytes para char/char). Al pedir memoria (ej. 64 KB), el MAS busca: (1) en el pozo de su tamaño, (2) en el siguiente pozo más grande libre, (3) en el *heap*, y (4) si todo está lleno, suspende el proceso, lo copia a un segmento mayor y duplica los pozos. En embebidos críticos se afina tras **3 a 5 compilaciones** editando el **archivo de *linker*** para garantizar sistemas predecibles por 20 años (Clase 19).  
  * **Memoria virtual, *Swapping*, *RAM disk* y zram**: La memoria virtual requiere **páginas** y vuelca páginas inactivas al disco (*swapping*). Windows coloca swapfile.sys en C: (fragmenta el sistema), mientras Linux coloca una partición swap fija al final del disco. *Ancho de banda en vivo (Clase 20\)*: un núcleo de **64 bits (8 bytes) a 3.2 GHz** pide **25.6 GB/s** (DDR entregaba 3.2 GB/s, DDR2 6.4 GB/s, DDR4 25.6 GB/s; 4 núcleos piden \~100 GB/s), mientras un SSD escribe a **433 MB/s** (100x más lento que RAM) y un HDD a **60 MB/s** (1000x más lento). *Vida útil SSD en vivo*: 1 año \= 31.536 × 106 s ≈ 3.2 × 107 s; a 1 escritura/s, un SSD de **10 megaescrituras** dura **meses**, y uno de **100 megaescrituras** dura **\~3 años**. *Soluciones Linux*: (a) Particionado separando /boot y / o /usr (\>10 GB, casi solo lectura) en SSD y /home en HDD barato para durar **25 años**; (b) **RAM disk (ramfs / tmpfs)** que monta un bloque de RAM en ext2 (usado para /tmp en /etc/fstab, al contrario del *swap*); (c) **zram** (/dev/zram0 visto con swapon), que reserva RAM con ext2 y comprime páginas con gzip/bzip2 al **\~30%** sin tocar el disco físico (Clases 6, 18, 20).  
> * **(c) Los 5 algoritmos de asignación del MAS — "Vienen en el examen" (Clase 19\)**:

| Algoritmo | Estrategia de búsqueda | Ventaja / Desventaja / Uso ideal   |
| :---- | :---- | :---- |
| **First Fit** | Busca siempre desde el inicio de la tabla y asigna el primer hueco donde quepa. | Simple, pero reescanea desde el inicio cada vez. |
| **Next Fit** | Continúa buscando desde la última posición asignada hacia adelante. | Suele ser el más rápido en barrido lineal, pero sigue generando fragmentación. |
| **Best Fit** | Barre toda la tabla y elige el hueco más ajustado al tamaño pedido. | Reduce fragmentación; ideal cuando las apps saben su consumo fijo. |
| **Worst Fit** | Barre toda la tabla y asigna el hueco más grande disponible (avaricioso). | Ideal para apps que crecen (filosofía Google Chrome) para dar espacio de expansión. |
| **Quick Fit** | Tabla auxiliar tipo *hash* ordenada con tamaños y apuntadores libres. | Búsqueda muy rápida (O(log N) con binaria) y acelera Best/Worst Fit; gasta RAM adicional. |

> * **(d) Puntos recalcados para examen**: El profesor señaló explícitamente que los **5 algoritmos de asignación de memoria vienen en el examen** (Clase 19); también hay que evitar la confusión común entre **swap** (RAM → disco) y **RAM disk / tmpfs** (RAM usada como disco rápido) (Clase 18).

### ---

**3.4 Relojes y Temporizadores por Software**

> * **(a) Problema que resuelve y conexión**: Con un solo *timer* de hardware (reloj del sistema de Unidad 2), el *scheduler* construye servicios de software para dormir microcontroladores en lugar de quemar batería en while(1) (ej. marcapasos a **8 MHz** frente a un corazón bajo taquicardia de **\<200 Hz**, \~160 estándar), gestionar retardos, lanzar funciones futuras sin traslapes y llevar la fecha civil (Clase 20).  
> * **(b) Conceptos clave**:  
  * **Timer vs. Reloj contador**: El *timer* produce interrupciones periódicas; el *reloj contador* lleva la cuenta del tiempo (Clase 20).  
  * **Jiffy**: Unidad de tiempo interna del *scheduler*, calculada automáticamente al arrancar el sistema operativo según su reloj (Clase 20).  
  * **Ejecución síncrona (delay / sleep)**: En *bare-metal* quema millones de instrucciones NOP. En un SO, el *scheduler* intercepta la llamada en **3 escenarios**: (1) **\>100 ms**: saca y suspende la tarea reprogramándola a futuro; (2) **0**: abstracción para reevaluar colas y semáforos y devolver control casi inmediato (nanosegundos); (3) **entre 0 y 100 ms**: saca la tarea y la vuelve a encolar en READY, **sin garantizar precisión exacta** (pedir 50 ms puede tardar 54 ms o más) (Clase 20).  
  * **Ejecución asíncrona periódica y prevención de solapamiento ("Pregunta para entrar a Google")**: Si un *timer* llama cada **10 ms** a bar(), y las ejecuciones duran **3 ms, 15 ms, 25 ms, 20 ms, 15 ms**, llegan a coexistir **3 instancias simultáneas** no deseadas. *Solución de clase*: La función bar() del *timer* no hace trabajo pesado, únicamente libera un **semáforo binario** inicializado cerrado (0, máx. 1\) mediante sem\_post; un hilo trabajador independiente con foo() corre while(running) bloqueado en sem\_wait, garantizando **a lo más una instancia a la vez** (Clase 20).  
  * **Primitivas del kernel**: **init\_timer** (configura apuntador a función, parámetros y delta\_t en *jiffies*, sin arrancar), **add\_timer** (encola el *timer* para ejecutarlo; volverlo a llamar al final de la función logra repetición periódica) y **del\_timer** (cancela y saca el *timer* de la tabla) (Clase 20).  
  * **Servicio de Fecha/Hora**: En Linux, **date** consulta la fecha y hora civil del sistema, mientras **time** mide el tiempo de procesador que tarda un proceso (no da la hora). Sin internet, sumar *jiffies* acumula un **atraso o adelanto de 4 a 10 minutos al año**; por ello los sistemas embebidos remotos se conectan brevemente por **NTP** (sincronizado a relojes atómicos con 1 pulso de variación cada 100 millones de años —nota: en clase se mencionó erróneamente "germanio dopado" al referirse al cristal/elemento del reloj atómico \[dudoso\]—) y vuelven a dormir (Clase 20).

### ---

**3.5 Manejadores de Dispositivos (*Drivers*) y Sistemas de Archivos**

> * **(a) Problema que resuelve y conexión**: Para completar la tríada del núcleo (CPU, memoria y periféricos), las aplicaciones jamás acceden directo al hardware; el SO actúa como **árbitro** (bloqueando exclusividad en dispositivos como la cámara web o compartiendo el micrófono, y evitando penalizaciones de *middleware* como **Snapcraft** en Ubuntu 24 —45 s y 1.4 GB en Firefox— frente a la compilación nativa de Debian Bookworm —10 s y 340 MB— con el mismo kernel 6.1 y Xfce) mediante **controladores** y **sistemas de archivos** montados sobre ellos (Clase 21).  
> * **(b) Conceptos clave**:  
  * **Controlador (*device driver*)**: Software encargado de gestionar el hardware y servir de liga entre los fierros y cualquier capa superior (Clase 21).  
  * **10 funciones generales de un driver \+ familias**: (1) **Arranque** (negocia potencia, ej. 1 A para girar plato de disco), (2) **Apagado** (corta energía física), (3) **Habilitación** (encender lámpara de escáner, purgar cabezales de impresora), (4) **Deshabilitación** (pausa sin desconectar), (5) **Adquisición** (*lock* exclusivo), (6) **Liberación**, (7) **Lectura**, (8) **Escritura**, (9) **Instalación** (negocia DMA, IRQ, resolución, botones), (10) **Desinstalación** (vuelca búferes en discos antes de deshabilitar y apagar). Se añaden **ACPI** (suspend, standby, wake), **USB** (Control \+ modo de transferencia) y **almacenamiento** (montar, desmontar, expulsar) (Clase 21).  
  * **Tipos de controladores — "Pregunta de examen" (Clase 21\)**: **Dedicados** (vinculados al CPU antes de la arquitectura; le "recuerdan" tras el despertar cómo está su memoria, caché, MMU, FPU, coprocesadores, FPGA o núcleos gemelos como un Cortex-M0 en Blackpill vs. RP2040 o Cortex-M4 en Bluepill vs. RP2350) y **genéricos** (gestionan todo el hardware externo al núcleo en la tarjeta madre: SMBus, I²C, PCI, bancos DRAM, Ethernet, USB).  
  * **Categorías y modelo POSIX**: Puertos serie (UART, I²C, SPI, SMBus), dispositivos de red (Ethernet, Wi-Fi con TCP/IP y cifrado en tarjeta, WiMAX hasta 5 km), SATA/Flash (almacenamiento matricial con **balanceo de desgaste**), buses (PCI, PCIe, USB, SMBus) e interrupciones (exclusivos del kernel). En **POSIX**, **PCI** es transversal y conecta red (ej. montaje remoto —el profesor dijo *"NTFS, Network File System"*, lapsus por **NFS** \[dudoso\]— como dispositivo de bloques), tarjetas USB y Bluetooth (con **256 puertos virtuales** hacia caracteres y **TTY** sobre puerto serie) (Clase 21).  
  * **Sistema de archivos, escritura asíncrona y bitácora**: Tabla estructurada de registros montada sobre el driver; en **FAT** (FAT12 para disquetes, FAT16 y FAT32 con nombres 8.3 y límite de **4 GB**), el disco se divide en **clústeres** (no caben dos archivos en un clúster, pero un archivo se fragmenta en varios). Las lecturas van al disco, pero la **escritura (write) es asíncrona**: se acumula en un búfer en RAM para consolidar operaciones de alto volumen (explicando por qué copiar a USB arranca a \~120 MB/s los primeros \~300 MB y luego cae a \~20 MB/s, y por qué desconectar sin expulsar / **flush** borra lo que seguía en RAM). Según tolerancia a fallos, hay sistemas **con bitácora (*journaling*)** —aplican actualizaciones transaccionales atómicas y escritura diferida para hacer *rollback* ante apagones (NTFS, ext3, ext4, JFFS)— y **sin bitácora** —riesgo de corromper toda la tabla (FAT32, exFAT, ext2)— (Clase 21).  
> * **(c) Sistemas de archivos para sistemas embebidos (Clase 21\)**:

| Sistema de archivos | Bitácora / Lectura-Escritura | Características técnicas y uso real visto en clase   |
| :---- | :---- | :---- |
| **ext2** | Sin bitácora / RW | Creado en \~1995 para el kernel Linux; soporta particiones hasta **32 TB** y archivos de **2–4 GB**; usado en **RAM disks** y flash (si la flash falla físicamente ya no se lee). |
| **ramfs / tmpfs** | Sin bitácora / RW (no persistente) | ramfs monta RAM con expansión dinámica (en clase se dijo que *"solamente soporta un archivo"* \[dudoso en Linux real\]), por lo que sobre RAM se formatea **ext2** para crear **tmpfs** (ej. /tmp). |
| **cramfs** | Sin bitácora / Solo lectura | Primer sistema de carga del kernel; comprimido con **zlib** (\~256 MB+); aún usado en televisiones actuales. |
| **initramfs** | Sin bitácora / Solo lectura | Evolución de cramfs que cambia zlib por **gzip** (mayor compresión, más CPU) y descomprime a cualquier destino; **lo carga GRUB al arrancar Linux** (*"ese sí se lo tienen que saber"*). |
| **JFFS** | **Con bitácora** / RW | Para memorias flash **NOR** y **NAND** (hoy dominantes), límite **128 MB** y soporte de **enlaces duros** (múltiples rutas al mismo archivo real, aprovechados por rdfind para deduplicar). |

> * **(d) Puntos recalcados para examen**: Distinguir **controladores dedicados vs. genéricos** (*"pregunta de examen"*), conocer **initramfs** (*"si no han oído este, están en el hoyo... ese sí se lo tienen que saber"*), y comprender la diferencia entre **write asíncrono \+ flush** y sistemas **con/sin bitácora** (Clase 21).

## ---

**LO QUE MÁS PROBABLEMENTE VIENE EN EL FINAL**

> 1. **Definición y 4 características de los *Timers* de hardware**: El profesor señaló explícitamente en Clase 7: *"memorizar la definición... Tiene estas cuatro características. Todas son preguntas de examen"* (*Free run/one shot*, dirección de conteo, rango en bits, fuente oscilador/externa).  
> 2. **USB 2.0 (topología de 7 niveles, 3 velocidades y 4 modos de transferencia)**: En Clase 8 afirmó explícitamente que *"el máximo nivel, pregunta de examen, es siete"* y los modos de operación de USB 2.0; en Clase 9 evaluó los 4 modos (*Control*, *Bulk*, *Interrupt*, *Isochronous*) y en Clase 15 confirmó su presencia en evaluaciones.  
> 3. **Protocolos de interconexión (tabla comparativa completa)**: En Clase 9 exigió: *"cuando yo termino el tema, ustedes se tienen que saber de memoria las características de cada uno: topología, configuración maestro-esclavo o pares, frecuencia, nombre y número de líneas"* (I²C, SMBus, SPI/QSPI, I²S, UART N81, RS-232 vs. RS-485, One-Wire).  
> 4. **Funcionamiento general y orden de la secuencia de arranque (*Bootstrap*)**: En Clase 12 aclaró ante pregunta de un alumno que no pide memorizar las 32 cajas ni direcciones hexadecimales, pero sí el **orden general de fases** (RESET → modo protegido → cachés → DRAM → interrupciones → detección APs con SIPI/semáforo → PCI → SO).  
> 5. **Los 6 pasos de una llamada a servicio del sistema operativo**: En Clase 13 presentó la lista diciendo explícitamente **"Pregunta de examen"**: enmascaramiento por *linker*, argumentos \+ EAX, trampa (int 80h), cambio de nivel, desenmascaramiento/ejecución en kernel (sys\_brk) y retorno.  
> 6. **Diferencia entre unidades mínimas de ejecución (Proceso, Hilo en GPOS y Tarea en RTOS) y estados de proceso**: En Clases 13 y 15 dedicó gran énfasis a que FreeRTOS solo usa tareas y no procesos, a la transición running → wait → ready (nunca wait → running), y a que la arquitectura de RTOS verifica accesos en compilación.  
> 7. **Ejercicios de Planificación en Tiempo Real (MLF y Regla de Oro) y cota del 70% de RMS**: En Clase 18 resolvió tres ejercicios numéricos en vivo (*"si fuera examen, voy a volver a ejecutar la tarea P1"*), bautizó Σ Ci/Ti ≤ 1 como la **"regla de oro"** y precisó que **la demostración matemática del límite del 70% de RMS NO viene**, solo el criterio y la cota.  
> 8. **Los 5 algoritmos de asignación de memoria del MAS y cálculo de tabla de paginación**: En Clase 19 dijo explícitamente *"esto nos lleva a los cinco algoritmos que vienen en el examen sobre fragmentación / alocación de memoria"* (*First, Next, Best, Worst, Quick Fit*) y resolvió paso a paso el ejercicio de 64 KB / 16 bits.  
> 9. **Temporizador asíncrono periódico sincronizado con semáforo binario y comportamiento de delay**: En Clase 20 planteó el problema de bar() cada 10 ms con duraciones de 3, 15 y 25 ms como *"pregunta para entrar a Google"* y clasificó los 3 comportamientos del *scheduler* para delay (0, 0–100 ms sin garantía, \>100 ms).  
> 10. **Controladores dedicados vs. genéricos y sistemas de archivos embebidos (initramfs)**: En Clase 21 afirmó textualmente *"dos tipos de controladores y esto es pregunta de examen: los dedicados y los genéricos"*, y advirtió sobre initramfs: *"si no han oído este, están en el hoyo, joven; ese sí se lo tienen que saber"*.  
> 11. **Memoria virtual, desgaste de SSD y zram (evidencia moderada)**: Aunque no los etiquetó con la frase "pregunta de examen", en Clase 20 resolvió cálculos numéricos en vivo (ancho de banda 25.6 GB/s, vida útil con 3.2 × 107 s/año) y demostró /dev/zram0 en terminal.

## ---

**CONEXIONES CLAVE**

> 1. Arquitectura del sistema embebido → resuelve intrínsecamente → restricciones de costo, batería y confiabilidad.  
> 2. Taxonomía de Flynn → clasifica → procesadores según sus flujos de instrucciones y datos.  
> 3. Predecodificador con microfusión → convierte → instrucciones CISC complejas en microoperaciones RISC paralelas.  
> 4. Bus coherente → sincroniza → escrituras entre memoria caché y DRAM principal.  
> 5. Mapa de memoria del sistema → prohíbe cachear → direcciones mapeadas a registros de periféricos.  
> 6. DRAM capacitiva → requiere → ciclos de refresco cada \~60 ms para no perder datos.  
> 7. Memoria Flash matricial → agrupa escrituras en → clústeres de bloques para acelerar escritura y balancear desgaste.  
> 8. Modo de direccionamiento indexado → calcula → dirección de datos usando registro índice más desplazamiento.  
> 9. Modo de direccionamiento relativo → calcula → dirección de la siguiente instrucción usando el Contador de Programa.  
> 10. Controlador de interrupciones (ICU) → elimina → el desperdicio de CPU del *busy wait* o *polling*.  
> 11. Desencadenamiento por flanco → evita → que periféricos serie lentos bloqueen procesadores rápidos durante todo el byte.  
> 12. Controlador DMA → transfiere → datos entre periféricos y RAM saltándose al CPU.  
> 13. *Timer* de hardware → provee → la interrupción periódica base (*reloj del sistema*) para todo sistema operativo.  
> 14. Par trenzado diferencial en USB → detecta → errores por ruido eléctrico con hardware mínimo.  
> 15. Modo isócrono de USB → simula → transmisión síncrona mediante reserva fija de ancho de banda.  
> 16. Colector abierto con *pull-up* en I²C → permite → comunicar dispositivos de 3.3 V y 5 V en un mismo bus.  
> 17. Protocolo QSPI → carga → el firmware de BIOS/UEFI desde Flash ROM a gran velocidad.  
> 18. Estándar RS-485 diferencial → extiende → comunicaciones UART multipunto hasta 1.2 km frente a los 15 m de RS-232.  
> 19. Procesador de arranque (BSP) → despierta mediante SIPI → a los procesadores de aplicación (AP) en condición de carrera con semáforo.  
> 20. *Linker* → enmascara → llamadas de librería generando identificadores de 128 bits antes de la trampa int 80h.  
> 21. Hilos en GPOS → comparten → memoria virtual y prioridad dentro de un mismo proceso padre.  
> 22. Tareas en RTOS → dependen de → un superproceso raíz verificando accesos y *deadlines* desde compilación.  
> 23. Estado bloqueado (wait) → transita obligatoriamente hacia → la cola ready antes de volver a running.  
> 24. *Minimal Laxity First* (MLF) → prioriza → la tarea con menor diferencia entre tiempo restante al *deadline* y trabajo pendiente.  
> 25. Regla de Oro → exige → que la suma de consumos entre periodos sea menor o igual al 100%.  
> 26. *Rate Monotonic Scheduling* (RMS) → acota → el uso seguro del procesador al \~70% desde 4 o más tareas.  
> 27. Paginación de memoria → impide → que las tablas administrativas consuman más RAM que la memoria disponible.  
> 28. *Memory Allocation System* (MAS) → combate → la fragmentación mediante algoritmos de encaje (*Fit*) o *memory pools*.  
> 29. *Memory Pools* afinados en el *linker script* → aseguran → sistemas embebidos predecibles sin fragmentación en C/C++.  
> 30. Particionado inteligente \+ zram → protegen → las unidades SSD/MicroSD contra el desgaste por ciclos de escritura.  
> 31. Semáforo binario \+ hilo trabajador → evitan → instancias simultáneas cuando un *timer* asíncrono tarda más que su periodo.  
> 32. Conteo de *jiffies* sin NTP → acumula → una deriva de 4 a 10 minutos al año en el reloj de Linux.  
> 33. Controladores dedicados → informan → al sistema operativo la arquitectura interna y recursos propios del núcleo CPU.  
> 34. Escritura asíncrona (write) \+ flush → consolidan → datos en búferes de RAM antes de volcarlos al disco físico.  
> 35. Bitácora (*journaling*) en ext4 o JFFS → garantiza → consistencia mediante transacciones atómicas y *rollback* ante apagones.

---

📝 Si quieres, puedo armarte un **simulador de examen final** con 10–15 preguntas difíciles estilo Matamoros (mezclando cálculo de tablas de páginas, MLF, RMS, QSPI/UART y casos de init\_timer/semáforos) para que te pongas a prueba antes del examen.

## **Anexo · Clases que no estaban en el cuaderno de NotebookLM**

*Resumen para estudiar de cada una, tomado de los apuntes por clase del sitio (decimo/FSE/FSE-Resumenes/).*

### **Clase 14 · Primer examen parcial (Unidades 1 y 2\) (miércoles 14 oct 2026\)**

Calificación completa: el método funcionó. Para el segundo parcial, misma estrategia con la Unidad 3: definiciones exactas (como la del timer) y el funcionamiento de cada mecanismo con sus números.