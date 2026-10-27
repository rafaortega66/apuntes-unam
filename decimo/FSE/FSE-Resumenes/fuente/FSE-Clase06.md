% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 6 · Memorias no volátiles, Flash/SSD y modos de direccionamiento
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · lunes 14 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Ráfaga y disipación térmica
- **Burst mode:** la RAM dinámica abre una fila completa y la reescribe en cada ciclo, en vez de bit por bit; por eso transfiere bloques rápido.
| | RP2040 (Pico) | Intel Core i7 / Xeón |
|---|---|---|
| Memoria | 264–360 KB de RAM | 8 MB o más de caché SRAM |
| Reloj | 150 MHz | 1.5–4.2 GHz |
| Calor | ≈ 50 °C, "tibio" | Hasta **100 veces** más |
La disipación **no es lineal**: depende a la vez de frecuencia, tipo de memoria y tamaño.

## 2. Estado sólido y evolución de la ROM
**Estado sólido** = hecho con transistores de silicio (no bulbos); no es algo reciente.
| Memoria | Borrado / escritura |
|---|---|
| ROM | Fija desde fábrica |
| PROM / UV-EPROM | Ventanita: luz UV 15 min; programación con pulso de 13 V (opera a 5 V TTL) |
| EEPROM | Eléctrica, pulsos de 25 V; ≈ 1 millón de ciclos |

## 3. Memoria Flash y SSD
- Problema de la EEPROM: leer cuesta ns, pero escribir ≈ **1 ms** → a 20 MHz son miles de ciclos perdidos.
!!! Invención de la Flash (examen)
Celdas en **clústeres** (64 KB, 128 KB, 4 MB) escritos **en paralelo**. Un clúster de 64 KB en 50 ms → ≈ **0.8 µs por byte**; con clústeres de MB, ns por byte.
| Celda | Bits | Durabilidad / uso |
|---|---|---|
| SLC | 1 | 100 millones–1,000 millones de ciclos; cara; servidores (Google, Facebook, Oracle) |
| MLC | 2 | Buena durabilidad comercial; 3D/multicapa |
| TLC | 3 | Sustrato más delgado, más errores |
| QLC | 4 (un nibble) | La menos durable y la más barata; SSD económicos |
**Wear leveling:** la **TOC** guarda el mapa y cuántas veces se escribió cada celda; el balanceador manda las escrituras a las celdas menos gastadas. Si falla la celda de la TOC, **todo el disco** queda inutilizable.
- Radiación continua (microondas, router WiFi) puede afectar USB/SSD.
- Ocupación > 30–50 % → velocidad ≈ **70 %**; > 70 % → **menos de 60 %**.
- El pagefile de Windows (~10 escrituras/s ≈ 3.15 millones/año) desgasta el SSD: mandarlo a un disco mecánico; en Linux usar **zram** (swap comprimido en RAM).
Error común: creer que QLC es lo más durable.

## 4. Medios magnéticos y ópticos
- Cintas (secuenciales) → disquete 8" → 5¼" (320–720 KB) → 3½" (720 KB–1.44 MB, 2.88 MB especial; plaquita metálica para precisión del motor a pasos).
| Disco | Láser (apuntes) | Capacidad |
|---|---|---|
| CD (ISO 9660) | Rojo, 7 µm | 650–700 MB |
| DVD | Rojo, 4 µm | 4.7 GB (9.6 GB doble capa) |
| Blu-ray | Azul-UV, 0.04 µm | Full HD y 4K |
!!! Verificar longitudes de onda
Los valores reales son CD ≈ 780 nm, DVD ≈ 650 nm, Blu-ray ≈ 405 nm (así salió al reconsultar el audio). Confirmar qué cifras dio el profesor antes del examen.
- Holográfico (cultura general): láser de 1 kW que altera el medio en 3D; no entra.

## 5. Modos de direccionamiento (Motorola 6800 / 68HC11)
| Modo | Cómo | Ejemplo |
|---|---|---|
| Inherente | Operando implícito en el opcode | NOP, RTS, RESET |
| Inmediato | Constante justo después del opcode | `ADD A, #8` |
| Extendido | Dirección completa de 16 bits | `ADD A, $1000` |
| Directo | Página cero (primeros 256 bytes), dirección de 8 bits; ahorra ciclos | — |
| Indexado | Registro X o Y + offset; arreglos y matrices | `ADD A, 5, X` → dato en X + 5 |
| Relativo | PC = PC + delta con signo; saltos | JMP, JNE, JNZ, CALL |
Error común: confundir indexado (X + offset, datos) con relativo (PC + offset, siguiente instrucción).
| Otras arquitecturas | Rasgo |
|---|---|
| PIC18F4550 | Instrucciones fijas de 16 bits, Harvard; mover a RAM puede costar 2 ciclos |
| AVR (Arduino) | 1 o 2 operandos, normalmente 1 ciclo |
| ARM Cortex-M | Load/Store puro; sin modos extendido/directo |

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Calor | Intel (MB a GHz) hasta 100× el RP2040 (KB a 150 MHz) |
| EEPROM | 25 V, 1 millón de ciclos, escribir ≈ 1 ms |
| Flash | Clústeres en paralelo: 64 KB / 50 ms ≈ 0.8 µs por byte |
| SLC → QLC | Más bits por celda = más barato y menos durable |
| Wear leveling | TOC + balanceador; > 50 % lleno baja a ≈ 70 %, > 70 % lleno < 60 % |

!!! Los 6 modos del 6800
Inherente, inmediato (#), extendido (16 bits), directo (página cero, 8 bits), indexado (X + offset), relativo (PC + delta).
