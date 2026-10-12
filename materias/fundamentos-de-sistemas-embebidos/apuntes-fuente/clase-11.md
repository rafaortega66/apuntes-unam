# FSE · Clase 11 — apuntes tipo libro (salida de NotebookLM, 12 oct 2026)

> Fuente: NotebookLM, notebook «FSE», con el audio `FSE-Clase11.m4a` y las 8
> presentaciones activas. Sin editar, salvo: se quitaron los números de cita,
> se reconstruyeron las fórmulas que salieron rotas y se omitió la sección
> «Transcripción» (ver nota al final). Hay que contrastar contra las láminas.
> Las etiquetas `[solo en lámina]` / `[solo en clase]` las puso NotebookLM.

## 1. Encabezado

- Clase 11 (`FSE-Clase11.m4a`). Fecha: no mencionada en el audio (en el sitio: 5 oct 2026).
- Unidad 2: Organización, arquitectura y plataformas de sistemas embebidos.
- Subtemas: **2.6** Bus serie universal (UART, RS-232, RS-485, control de flujo por hardware y software); **2.7** Interconexión de dispositivos (I²C, 1-Wire, direccionamiento ROM, acoplamiento a puerto serie e interfaz en Linux sysfs).

## 3. Mapa clase ↔ presentación

| Tema | Presentación | Láminas | Cobertura en esta clase |
|---|---|---|---|
| UART, puerto serie y formato de trama (8N1, start/stop) | diapositivas-clase-07.pdf | 18–20 | Completa (formato, temporización, sincronización por 555/RC y capacitancia) |
| Control de flujo por hardware (RTS/CTS) y software (XON/XOFF) | diapositivas-clase-07.pdf | lámina de UART | Completa (origen histórico, RTS/CTS, interrupciones/búferes) |
| Estándares RS-232, RS-422 y RS-485 | diapositivas-clase-07.pdf | 20–22 | Completa (distancias, topologías, voltajes, nodos, inmunidad diferencial) |
| Bus I²C | diapositivas-clase-07.pdf | 10–14 | Solo mencionada (como referencia: pull-ups y número de alambres frente a 1-Wire) |
| Protocolo 1-Wire (Dallas/Maxim) | — | N/A | No estaba en lámina; explicado de viva voz (alimentación parásita, Reset/Presence, árbol Search ROM, emulación sobre UART, sysfs en Linux) |

**Láminas que el profesor NO cubrió en esta clase**
- `diapositivas-clase-07.pdf`: SPI (láminas 14–17: SCK, MOSI/TX, MISO/RX, CS/SS, modos de transmisión semiparalela y carga de BIOS Flash ROM en Intel a >80 MB/s); I²S (17–18: bus síncrono de 3 alambres CLK, SD, WS, audio estéreo digital hasta 3 MHz); SMBus (14–15: variante de I²C a 10–100 kHz en tarjetas madre para sensores de temperatura, fuentes y ventiladores).
- `diapositivas-clase-01` a `06` y `08`: clasificación de Flynn (SISD/SIMD/MISD/MIMD); mapas de memoria de PIC18F452, ATmega328P y ESP32; controladores de interrupciones, vectores IRQ, DMA, Northbridge/Southbridge; modos de direccionamiento y secuencia de arranque (vector de RESET, hard/soft reset).

## 4. Apuntes tipo libro

### Capítulo 1: Comunicaciones serie asíncronas (UART, RS-232, RS-485)

**1.1 Estructura de la trama serial asíncrona.** Una transmisión **UART** (Universal Asynchronous Receiver/Transmitter) mantiene la línea de datos en nivel lógico alto (IDLE) en reposo.

- **Bit de arranque (start):** transición de alto a bajo (flanco de bajada). Dispara un temporizador/oscilador astable interno del receptor para sincronizar la lectura de los bits en el centro de cada pulso.
- **Bits de datos:** típicamente de 5 a 8 (estándar de 8).
- **Bit de paridad (opcional):** control de errores, par (Even) o impar (Odd). Si ocurren 2 o 4 errores simultáneos en la trama, la paridad no los detecta.
- **Bit de parada (stop):** devuelve la línea al estado inactivo alto durante 1, 1.5 o 2 ciclos de reloj. Ese tiempo muerto permite descargar la capacitancia acumulada en el cable y garantiza la detección del siguiente flanco de bajada.
- Configuración estándar: **8N1** (8 bits de datos, sin paridad, 1 bit de parada). Cada byte requiere **10 bits físicos**.

**1.2 Tasa de transferencia.** Para B baudios en formato 8N1: tasa efectiva = B / 10 bytes/s.
Ejemplo: B = 56,600 baudios → 5,660 bytes/s = 5.66 KB/s. Un archivo de 5 MB (5×10⁶ bytes) tarda 5×10⁶ / 5,660 ≈ 883.39 s ≈ 14.7 min.

**1.3 Control de flujo.**
- **Hardware (RTS/CTS):** el transmisor activa RTS (Request to Send) y espera a que el receptor active CTS (Clear to Send), señal de que su búfer está listo.
- **Software (XON/XOFF):** caracteres dentro del canal de datos: XOFF (ASCII 0x13 / DC3) detiene la transmisión cuando el búfer se llena; XON (0x11 / DC1) la reanuda.

**1.4 Cuadro comparativo de capas físicas serie**

| Parámetro | RS-232 | RS-422 `[solo en lámina]` | RS-485 |
|---|---|---|---|
| Señal | Asimétrica (single-ended) | Diferencial | Diferencial |
| Modo | Full-duplex | Full-duplex / half-duplex | Half-duplex / full-duplex |
| Niveles | −5 a −12 V (1 lógico), +5 a +12 V (0 lógico) | ±2 a ±6 V | ±1.5 a ±5 V |
| Nodos máx. | 1 transmisor, 1 receptor | 1 transmisor, 10 receptores | 32 transmisores, 32 receptores |
| Distancia máx. | 15 m | 1.2 km | 1.2 km |
| Velocidad máx. | 20 kbps | 10 Mbps | 35 Mbps |

### Capítulo 2: Buses de interconexión síncronos y periféricos `[solo en lámina]`

**2.1 I²C (Inter-Integrated Circuit).** Bus síncrono maestro-esclavo desarrollado por Philips en 1980.
- Líneas: dos bidireccionales de colector/drenador abierto, **SCL** (reloj) y **SDA** (datos), más GND.
- Resistencias pull-up externas en SCL y SDA a VDD (típicamente 4.7 kΩ a 10 kΩ).
- Direcciones de 7 bits (4 fijos por fabricante, 3 configurables por pines) → hasta 112 dispositivos. El bit 8 define lectura (1) o escritura (0).

**2.2 SPI (Serial Peripheral Interface)** `[solo en lámina]`. Bus síncrono full-duplex de 4 hilos, hasta 80 MHz o más. **SCK** (reloj del maestro), **MOSI/TX** (maestro → esclavo), **MISO/RX** (esclavo → maestro), **CS/SS** (selección de esclavo, activo en bajo).

**2.3 I²S (Inter-IC Sound)** `[solo en lámina]`. Bus síncrono de Philips para audio digital estéreo multiplexado en el tiempo (hasta 3 MHz). **CLK** (reloj de bits), **SD** (datos), **WS** (Word Select: bajo = canal izquierdo, alto = canal derecho).

### Capítulo 3: Protocolo 1-Wire (One-Wire) `[solo en clase]`

**3.1 Definición y topología.** Bus serie asíncrono semi-dúplex maestro-esclavo de Dallas Semiconductor / Maxim Integrated. Un solo hilo de datos (DQ) más tierra (GND).

**3.2 Alimentación parásita.** Se elimina el pin de alimentación (VDD); el dispositivo se alimenta de la línea de datos.
- Dentro: un diodo D1 y un capacitor C1 de **800 pF** entre la línea DQ y GND.
- **Estado inactivo (alto):** la resistencia pull-up (4.7 kΩ) mantiene la línea en 3.3 V o 5 V; la corriente pasa por D1 y carga C1.
- **Estado activo (bajo):** cuando la línea cae a 0 V (ceros o pulsos de reset), D1 queda en inversa e impide que C1 se descargue hacia el bus; C1 alimenta el circuito interno.
- **Advertencia:** en modo parásito puro, el pin VDD del sensor debe ir a GND. Si VDD queda flotando, el dispositivo no funciona.

**3.3 Tiempos de capa física**

| Ranura / pulso | Duración (maestro) | Línea | Descripción |
|---|---|---|---|
| Reset | 480 µs (mínimo) | Baja | Descarga el capacitor interno y reinicia a los esclavos |
| Presence | 60–240 µs (respuesta del esclavo) | Baja (por el esclavo) | El esclavo indica que está presente |
| Escribir '1' | 1–15 µs | Baja → alta | El maestro baja <15 µs y libera; el pull-up sube la línea |
| Escribir '0' | 60–120 µs | Baja | El maestro sostiene bajo ≈60 µs |
| Leer (slot) | pulso de 1 µs, muestreo a 15–30 µs | Baja → flotante | El maestro baja 1 µs y lee la línea unos 30 µs después |

Especificaciones dichas en clase: hasta 2⁶⁴ dispositivos direccionables en un bus; cable de hasta 100 m con alimentación parásita, 300 m con cable blindado/trenzado, kilómetros con repetidores; velocidad estándar ≈3 kbps y 14.2 kbps en modo Overdrive.

**3.4 Dirección ROM de 64 bits.** Grabada de fábrica en cada esclavo: **8 bits de código de familia** (ej. 0x28 = sensor de temperatura DS18B20), **48 bits de número de serie único**, **8 bits de CRC** (polinomio de 8 bits de comprobación de errores). (El texto de NotebookLM presenta el orden CRC + serie + familia; el audio los lista como familia, serie, CRC. Verificar en la lámina o el datasheet.)

**3.5 Algoritmo de búsqueda (Search ROM, comando 0xF0).** Para descubrir los IDs de todos los esclavos en paralelo, el maestro recorre un árbol binario de 64 niveles, bit a bit:
1. Todos los esclavos activos transmiten el bit actual de su ID y luego su complemento.
2. El maestro lee los dos valores: `0 1` → todos tienen 0 en esa posición; `1 0` → todos tienen 1; `0 0` → **colisión** (hay esclavos con 0 y con 1).
3. En colisión, el maestro elige una rama (envía 0 o 1); los esclavos cuyo bit no coincide pasan a reposo (sleep) hasta el siguiente reset.
4. Se repite 64 veces hasta obtener un ID completo, se guarda y se repite la búsqueda para encontrar los demás.

**Comandos de ROM principales (dichos en clase):** Read ROM (0x33, un solo esclavo), Match ROM (0x55, selecciona uno por su ID), Skip ROM (0xCC, se dirige a todos sin enviar dirección).

### Capítulo 4: Emulación de 1-Wire sobre un puerto serie estándar (UART) `[solo en clase]`

Un UART/RS-232 a nivel TTL puede controlar un bus 1-Wire con **2 transistores NPN (p. ej. BC547) y 3 resistencias** (una de 10 kΩ en la base y el pull-up de 4.7 kΩ a VCC). Ejemplo: TX → R 10 kΩ → base de Q1; colector de Q1 → DQ; RX conectado a DQ; pull-up de 4.7 kΩ de DQ a VCC.

- **Escribir/leer un '1':** UART a **115,200 baudios**, transmitir **0xFF**. Un byte dura 10/115,200 ≈ 86.8 µs (cada bit ≈ 8.68 µs); el start bit mantiene la línea baja solo ≈8.68 µs (<15 µs). Si se lee 0xFF, el esclavo envió un '1'.
- **Escribir/leer un '0':** transmitir **0x00**. La línea queda baja toda la trama (≈86.8 µs, dentro de 60–120 µs). Se lee 0x00.
- **Pulso de Reset:** bajar el UART a **9,600 baudios** (trama de 10/9,600 ≈ 1.04 ms) y transmitir **0xF0**. La línea queda baja ≈520 µs (cumple los 480 µs).

### Capítulo 5: Abstracción en el kernel de Linux (sysfs) `[solo en clase]`

En Linux embebido (p. ej. Raspberry Pi OS), los controladores del kernel (`w1-gpio`, `w1-therm`) manejan las temporizaciones en microsegundos y exponen los dispositivos en el sistema de archivos virtual: `/sys/bus/w1/devices/<DIRECCIÓN_ROM>/`. Para leer un sensor (p. ej. DS18B20), Python o C solo abren un archivo; no hay que hacer bit-banging. Ejemplo: abrir `/sys/bus/w1/devices/28-…/w1_slave` en modo lectura y leer su contenido (el texto del ejemplo de NotebookLM salió dañado: «[suspicious link removed]»; falta el `read()` de la línea final).

## 5. Lo que el profesor enfatizó

1. **Propósito real del bit de parada.** No es una mera convención: es un tiempo muerto que descarga las capacitancias flotantes acumuladas en cables largos a alta frecuencia y garantiza que la línea vuelva a reposo para detectar el siguiente flanco de bajada. Evidencia: «el bit de parada es el tiempo muerto entre paquetes… me elimina las capacitancias parásitas en líneas de alta frecuencia».
2. **Por qué RS-232 usa ±12 V.** En entornos industriales con motores de 20–40 HP, la inducción genera 2–3 V de ruido; con niveles de 0–5 V eso produciría falsos unos. Con +12 V/−12 V el cero lógico es inmune al ruido. Evidencia: «¿Por qué lo voy a hacer de +12V a −12V? Porque… tienen 2 a 3 voltios de puro ruido».
3. **Alimentación parásita de 1-Wire.** Ahorra el cable de alimentación: el sensor se carga de la línea de datos con un capacitor de 800 pF. Evidencia: «mientras no hay transmisión de datos, este se carga colándose en el cable de datos en un capacitor interno».
4. **Controlador 1-Wire con un puerto serie común.** Dos transistores y tres resistencias (<10 pesos): 115,200 baudios y 0xFF/0x00 para bits, 9,600 baudios y 0xF0 para reset. Evidencia: «pones tu puerto serie a 115,200, mandas FF y lees FF para escribir un uno».
5. **Abstracción total en Linux.** Para la práctica no se programa electrónica de bajo nivel: el sensor se maneja como un archivo en `/sys/bus/w1/devices/`. Evidencia: «en Python un maldito archivo… tan sencillo como abrir un archivo, escribir en él».

---

**Notas de verificación (de Claude, no de NotebookLM)**
- La sección «Transcripción» que devolvió NotebookLM **no es literal**: empieza con fragmentos de audio mal reconocidos («Cambalá», «enjuagues») y después se vuelve un resumen redactado. Por eso no se guardó como transcripción.
- Algunos datos del texto de NotebookLM discrepan entre secciones (p. ej. orden de los campos de la dirección ROM). Contrastar con las láminas antes de estudiar de aquí.
