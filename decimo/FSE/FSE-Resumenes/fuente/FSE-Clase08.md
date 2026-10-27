% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 8 · De los puertos legados a USB 2.0
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · miércoles 23 sep 2026 · Tema 2 (2.6–2.7) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 2.6.1 Puertos legados y fisiología humana
Conectores legados: **PS/2** (teclado y ratón), **DB-9** (serie RS-232), **DB-15** (juegos/MIDI o VGA), **DB-25** (paralelo y SCSI).
**Latencia de una pulsación:**
| Etapa | Tiempo |
|---|---|
| Impulso nervioso cerebro → dedo | ≥ 20 ms |
| Contracción muscular y retroalimentación táctil | 40 ms |
| Retorno para levantar el dedo | 20 ms |
| **Pulsación completa** | **60–100 ms** → máximo ≈ 600–700 acciones/min (**7–10 Hz**) |
- Visión: cine a 24 fps; monitores a 30 (29.9) o 60 fps; respuesta del ojo ≈ 40 ms (25 Hz).
- El **ratón** usa un codificador óptico que genera pulsos de kHz; para no saturar la CPU se **muestrea a 100 Hz** (multiplexación en el tiempo).

## 2.6.2 Cuellos de botella de los puertos legados
| Puerto | Velocidad | Uso / límite |
|---|---|---|
| Serie (RS-232) | 1.5 Mbit/s ≈ 200 KB/s | Módems (56.6 kbit/s), DSL inicial |
| Paralelo (IEEE 1284) | 2.5 Mbit/s → **0.31 MB/s** | Impresoras lentas; colapsa con fotos y escaneos |
| SCSI | Hasta 20 MB/s | Tarjeta de $9,000 MXN (procesador y búfer propios) |
**Cálculos en vivo:**
- Foto 1995: 1024 × 768 × 3 bytes = **2,359,296 B ≈ 2.35 MB**.
- Escaneo 300 DPI de 7.5 × 9 in: (7.5·300) × (9·300) = 2250 × 2700 = 6,075,000 puntos × 3 = **18,225,000 B ≈ 18.2 MB** → casi **1 minuto** a 0.31 MB/s.

## 2.6.3 FireWire (IEEE 1394) vs. USB 1.0/1.1 (1995)
| Característica | FireWire | USB 1.0 / 1.1 |
|---|---|---|
| Voltaje | Dinámico, 5–30 V | Fijo, 5 V |
| Potencia | Hasta 1.5 A (45 W) | Hasta 500 mA (2.5–5 W) |
| Velocidad (1995) | 3 Gbit/s | 12 Mbit/s |
| Carga de CPU | Coprocesador propio (0 %) | La CPU hace todo |
| Memoria y reloj | Búfer dedicado; síncrono y asíncrono | RAM del sistema; solo asíncrono |
| Costo | Muy elevado | Muy económico |
Ganó **USB por bajo costo**, no por superioridad técnica. USB 1.0 tuvo fallas; **USB 1.1 (12 Mbit/s)** fue el estándar definitivo.

## 2.6.4 USB 2.0: modos de velocidad (tema de examen)
USB 2.0 (≈ 2004): 480 Mbit/s nominales.
| Modo | Velocidad | Para qué |
|---|---|---|
| **Low Speed** | **1.5 Mbit/s** | Entrada humana: teclados, ratones, estiletes, gamepads, **hápticos** (simuladores, microcirugía) |
| **Full Speed** | **12 Mbit/s** | Telefonía, audio, módems; latencia garantizada (isócrono, interrupciones) |
| **High Speed** | **480 Mbit/s** | Video, cámaras, discos y SSD |
| Audio en Full Speed | Cálculo |
|---|---|
| Telefonía | 8 kHz × 8 bits = 64 kbit/s |
| MP3 estéreo | 48 kHz × 16 bits × 2 = 1.536 Mbit/s |
| 7.1 (8 canales) | 48 kHz × 16 × 8 ≈ 6.14 Mbit/s (< 12) |
**Más allá:** USB 3.0 = 5 Gbit/s. Video 4K a 60 fps: 3840 × 2160 × 32 bits × 60 = **15,925,248,000 bit/s ≈ 15.9 Gbit/s** → excede USB 3.0; requiere DisplayPort, HDMI o USB4 al puente norte.

## 2.6.5 Topología, par diferencial y detección de conexión (examen)
- **Topología en árbol de 7 niveles:** nivel 1 = host y **root hub**; niveles 2–7 = hubs encadenados y dispositivos. No más de 7 niveles.
- **Par trenzado diferencial D+ / D−:**
| Bit | D+ | D− |
|---|---|---|
| 1 | Alto (5 V) | Bajo (0 V) |
| 0 | Bajo (0 V) | Alto (5 V) |
| 1 1 o 0 0 | — | **Error de bus** (deben ser complementarias) |
El trenzado genera un campo que **blinda contra EMI**.
- **Detección eléctrica:** con resistencias de acoplamiento; sin dispositivo la línea está en **5 V**; al conectar, el circuito del periférico cierra a tierra y cae a **0 V** ("conectado"); al desconectar regresa a 5 V.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Humano.** Pulsación 60–100 ms (7–10 Hz); ratón muestreado a 100 Hz. Por eso existe Low Speed.

**Legados.** Serie ≈ 200 KB/s, paralelo 0.31 MB/s (escaneo de 18.2 MB ≈ 1 min), SCSI 20 MB/s pero caro. FireWire era superior; USB ganó por costo.

!!! USB 2.0 (examen)
**Low** 1.5 Mbit/s (humanos, hápticos) · **Full** 12 Mbit/s (audio, telefonía) · **High** 480 Mbit/s (video, discos). Árbol de **7 niveles**. D+/D− complementarias (1 1 o 0 0 = error). Conexión detectada por caída de 5 V a 0 V.

| Cálculo | Resultado |
|---|---|
| Foto 1024×768×3 | 2.35 MB |
| 4K a 60 fps, 32 bits | 15.9 Gbit/s |
