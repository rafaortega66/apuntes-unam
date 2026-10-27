% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 10 · I²C, SMBus, SPI, I²S y UART
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · miércoles 30 sep 2026 · Tema 2 (2.7) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 2.7.1 Colector abierto y pull-ups en I²C
- SCL (reloj) y SDA (datos) se implementan con transistores en **colector abierto** (open-drain) y **resistencias pull-up a VCC**.
- Con corriente en la base, el transistor conduce y la línea cae a ≈ 0 V (cero lógico); sin corriente, el pull-up la sube a VCC (uno).
!!! Solo se escriben ceros
El transistor escribe **ceros activos a tierra**; el uno lo fija la resistencia de pull-up. Esto permite **multimaestro** y convivencia de dispositivos de 3.3 V y 5 V sin quemar salidas.

## 2.7.2 Trama I²C
El maestro verifica que el bus esté libre y genera:
| Elemento | Definición |
|---|---|
| **Start** | Flanco de **bajada en SDA** con SCL en alto (1 → 0) |
| Dirección + R/W | 7 bits de dirección (MSB a LSB) + octavo bit: escritura 0 / lectura 1 |
| **ACK / NACK** | El maestro libera SDA; el esclavo la baja a 0 (ACK). Si queda en alto por el pull-up → NACK |
| Clock stretching | El esclavo mantiene SCL en bajo para pausar al maestro |
| **Stop** | Flanco de **subida en SDA** con SCL en alto (0 → 1) |
**Ejercicio de rendimiento:**
| Paso | Cálculo |
|---|---|
| Trama de dirección | 1 Start + 7 dirección + 1 R/W + 1 ACK = 10 bits |
| Byte de datos | 8 + 1 ACK = 9 bits |
| Primer byte completo | 10 + 9 + 1 Stop = **20 bits** |
| A 400 kHz (Fast Mode) | 400,000 ÷ 20 = **20 KB/s** |
| UART N81 a 115,200 (≈ 10.5 bits/byte) | 115,200 ÷ 10.5 ≈ **11 KB/s** |
I²C a 400 kHz rinde casi el doble que un puerto serie a 115.2 kbps; a 2 MHz (cifra del profesor) ≈ 100 KB/s. Los modos oficiales son 100 kHz, 400 kHz, 1 MHz y 3.4 MHz.

## 2.7.3 SMBus
Variante simplificada y más lenta de I²C (Intel y Philips): misma capa física de 2 hilos con pull-ups, pero **punto a punto** (sin enviar dirección), **10–100 kHz**. Estándar de gestión en tarjetas madre: fuente, sensores térmicos de la CPU, ventiladores, módulos RAM, refresco DRAM, comandos short/long y ráfaga.

## 2.7.4 SPI, QSPI y Octa-SPI
Bus **síncrono, punto a punto, full duplex real**, más de 80 MHz.
| Línea | Función |
|---|---|
| SCLK | Reloj del maestro |
| MOSI | Maestro → esclavo |
| MISO | Esclavo → maestro |
| SS / CS | Habilita al esclavo |
- **QSPI:** 4 líneas de datos (2×2), transfiere nibbles; lee la Flash de BIOS/UEFI en Intel; base de las MicroSD.
- **Octa-SPI:** 8 líneas; pantallas de relojes inteligentes y memorias rápidas.
| A 80 MHz | Por sentido | Combinado |
|---|---|---|
| SPI | 80 MHz ÷ 8 = 10 MB/s | 20 MB/s |
| QSPI | 20 MB/s | 40 MB/s |
| Octa-SPI | 40 MB/s | 80 MB/s |
No lleva direcciones por byte; no confundir megabits con megabytes.

## 2.7.5 I²S (audio digital)
Variante síncrona de Philips solo para **audio entre circuitos integrados** (decodificador MP3, DSP, DAC/amplificador), punto a punto, hasta 3 MHz. Líneas: reloj, datos y **Word Select (WS)**, que indica canal izquierdo o derecho.
| Cálculo | Resultado |
|---|---|
| Canal a 2 MHz (÷ 10 bits con overhead) | 200 KB/s |
| Audio CD: 44,100 × 2 canales × 2 bytes | 176.4 KB/s < 200 → pasa |
| 48 kHz | 192 KB/s → pasa |
I²S va al amplificador, no directo a las bocinas (que reciben señal analógica).

## 2.7.6 UART, RS-232, MAX232 y paridad
- **Asíncrono:** sin reloj compartido; mismos baudios en ambos extremos; **null-modem** (TX cruzado con RX).
- **RS-232** usa **−12 V a +12 V**; para la lógica TTL (5 o 3.3 V) se necesita el acoplador **MAX232**. Conectar +12 V directo a un Arduino "le saca humo".
- Reposo en alto; bit de inicio (1 → 0); paquetes de 6, 7 u 8 bits + paridad + paro.
**Paridad:** 0x1F = 0001 1111 → 5 unos (impar). Con paridad par configurada, el receptor detecta el error. Pero si cambian **dos** bits la suma vuelve a cuadrar: **≈ 50 % de efectividad**.

## Contexto: perfil del ingeniero en computación
El profesor rechazó que "quien quiera hardware se vaya a Eléctrica": el ingeniero en computación es **el pegamento entre hardware y software**.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! I²C (examen)
Colector abierto + pull-up (solo se escriben ceros; multimaestro). **Start:** SDA baja con SCL alto. **Stop:** SDA sube con SCL alto. ACK = esclavo baja SDA. 20 bits por byte → 20 KB/s a 400 kHz (vs. ≈ 11 KB/s UART a 115,200).

| Bus | Para recordar |
|---|---|
| SMBus | I²C punto a punto, 10–100 kHz, gestión de tarjeta madre |
| SPI | SCLK, MOSI, MISO, CS; full duplex; 80 MHz → 10 MB/s por sentido |
| QSPI / Octa-SPI | 4 / 8 líneas → 20 / 40 MB/s por sentido |
| I²S | Audio estéreo; WS elige canal; CD = 176.4 KB/s |
| UART/RS-232 | ±12 V; MAX232 a TTL; paridad ≈ 50 % efectiva |
