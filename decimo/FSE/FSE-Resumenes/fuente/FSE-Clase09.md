% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 9 · Potencia en USB, HID, modos de transferencia e I²C
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · lunes 28 sep 2026 · Tema 2 (2.6–2.7) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 2.6.1 PHY y administración de potencia en USB
- El transceptor físico de USB 1.1/2.0 es muy simple (negadores, transceptor diferencial, sensor de desconexión): por eso los periféricos USB son baratos.
!!! Potencia por defecto
Al conectarse, todo dispositivo recibe **100 mA a 5 V** sin negociar ("absoluto comunismo"); si necesita más, lo **negocia por software** con el maestro. Máximo de USB 2.0: **500 mA → P = 5 V × 0.5 A = 2.5 W**.
| Carga | Consumo |
|---|---|
| Pin digital | Microamperios (500 mA alcanzarían para 500,000 pines) |
| LED | < 20 mA nominal; ≈ 1 mA tenue |
| Motores, bobinas, solenoides | Picos altos de arranque; una impresora láser ≥ 40 W |
| Disco duro mecánico USB 2.0 | ≥ 1 A: con 500 mA "se moría de hambre"; cables en Y o eliminador de 3 W |
USB se diseñó para **datos, no potencia**. USB 3.0 subió la corriente nativa (los apuntes dicen 800 mA; la especificación suele citar 900 mA) y USB Power Delivery llega a 5 A.

## 2.6.2 Pila de software USB y clase HID
Flujo (ejemplo: vibración de un control al recibir un golpe en un juego): aplicación → subsistema USB del SO (Control Pipe) → controlador del host y bus → dispositivo lógico y **endpoints** → función de hardware (motores).
- Un gamepad es un **dispositivo compuesto**: varios dispositivos lógicos (mando analógico, botones, acelerómetros, audio, háptica).
- **Por qué HID:** USB 1.0/1.1 no tenían clases estandarizadas; cada periférico requería un disco de drivers ("infierno de controladores" de Windows 98/XP). El consorcio (Microsoft, Genius…) definió **HID**: el dispositivo envía una **carta de descriptores** y el host carga un **driver genérico al vuelo** (Plug and Play).
| Dispositivo | Su carta de descriptores |
|---|---|
| Mouse sencillo | 2 enteros de 8 bits (X, Y) + 1 byte de botones (bit 0 izquierdo, bit 1 derecho) |
| Mouse de alta resolución | 2 flotantes de 32 bits (X, Y) + 1 flotante (rueda) + 1 byte (8 botones) |
| Gamepad | ADC de 16 bits (65,536 valores por eje) + 1 byte de botones + PWM para la háptica |

## 2.6.3 Los cuatro modos de transferencia (tema de examen)
| Modo | Rasgo | Ejemplos |
|---|---|---|
| **Control** | **Obligatorio** (100 % de los dispositivos en la negociación inicial); paquetes cortos de configuración, descriptores y comandos | Todos; "extraer de forma segura" (Linux corta la alimentación, Windows deja el LED) |
| **Bulk (ráfaga)** | Grandes volúmenes a la máxima velocidad, **sin latencia garantizada**; se negocia antes; **cede el bus** a Interrupt | Discos, memorias USB, escáneres, impresoras |
| **Interrupt** | Paquetes pequeños (< 1 KB), **periódicos, latencia fija** | Teclados, ratones, estiletes |
| **Isócrono** | **Tiempo real** con **ancho de banda reservado** (p. ej. 10 % de cada segundo); **sin retransmisión** de errores | Robótica industrial (Ford, Hyundai, BYD), tomógrafos, audio/video |
!!! Inseguridad física del bus
El hub transmite por **difusión**: todos los dispositivos escuchan todo y los datos no van cifrados; un keylogger de hardware en el mismo bus captura teclas y contraseñas.

## 2.7.1 Interfaces de baja velocidad: sensores y actuadores
Buses baratos (< 1 MHz, pocos pines) para sensores, actuadores, EEPROM/Flash y pantallas LCD/OLED.
- **Transductor (sensor):** magnitud física → eléctrica. **Actuador:** eléctrica → física (calor, movimiento, luz).
| Topología | Cómo funciona |
|---|---|
| **Maestro-esclavo** | Un maestro coordina el reloj, pasa lista y autoriza; barata, simple, sin colisiones |
| **Entre pares (P2P)** | Todos compiten "democráticamente"; requiere consenso (relojes de Lamport) y microcontroladores más caros |

## 2.7.2 El bus I²C
Bus **serie síncrono de 2 hilos** (más tierra), atribuido a Philips:
- **SCL** (reloj, lo genera el maestro) y **SDA** (datos bidireccionales).
- **Dirección de 7 bits** → 128 teóricas, máximo práctico **112** dispositivos (las demás reservadas). El fabricante fija 4 bits en el silicio y **3 se configuran por hardware** (pines A2, A1, A0) → hasta **8 dispositivos idénticos** en el mismo bus.
| Modo | Frecuencia |
|---|---|
| Estándar | 100 kHz |
| Rápido (Fast Mode) | 400 kHz (el usual, p. ej. RP2040) |
| Rápido Plus | 1 MHz |
| Alta velocidad | 1.7 a 3.4 MHz |
- **Colector abierto + pull-up:** los dispositivos solo escriben **ceros** derivando a tierra; si nadie escribe, el pull-up sube la línea a 1. Permite mezclar chips de 3.3 V y 5 V sin daño.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Potencia USB.** 100 mA a 5 V por defecto; hasta 500 mA (2.5 W) en USB 2.0 negociando por software. USB es para datos: motores y discos mecánicos necesitan más.

**HID.** Carta de descriptores → driver genérico al vuelo; acabó con los discos de controladores.

!!! Modos de transferencia (examen)
**Control** (obligatorio, configuración), **Bulk** (volumen, sin latencia garantizada, cede el bus), **Interrupt** (< 1 KB, periódico, latencia fija), **Isócrono** (tiempo real, ancho reservado, sin retransmisión).

| I²C | Para recordar |
|---|---|
| Líneas | SCL + SDA |
| Direcciones | 7 bits; 112 dispositivos; 3 bits por pines A2–A0 = 8 idénticos |
| Velocidades | 100 kHz, 400 kHz, 1 MHz, 3.4 MHz |
| Electrónica | Colector abierto + pull-up; solo se escriben ceros |
| Topología | Maestro-esclavo (barata) vs. P2P (consenso) |
