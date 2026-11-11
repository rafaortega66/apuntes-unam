% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 20 · Memoria virtual y temporizadores por software
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · lunes 9 nov 2026 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Memoria virtual, páginas y swapping
Usa el disco como extensión de la RAM mediante bloques de tamaño fijo (páginas). La MMU mapea los espacios virtuales de cada proceso a páginas físicas.
- **Swapping:** con la RAM llena, el sistema mueve las páginas de procesos inactivos, en espera o de baja prioridad a la partición o archivo de intercambio.
- Se mueven **páginas**, no archivos sueltos.
- Mover páginas al disco pasa por DMA, buses y controladores: mucho más lento que la RAM.
- Cierra el punto 3.4 del temario.

## 2. Desgaste de la flash y particionado
!!! Cálculo de vida útil
1 año ≈ 31,536,000 s ≈ 3.2×10⁷ s. Con una escritura por segundo: 10 megaescrituras (10⁷) duran unos meses; 100 megaescrituras (10⁸) duran unos 3 años.

- Se separan `/boot`, `/` y `/home` en medios distintos y se evita escribir de más sobre la flash.
- ⚠️ NotebookLM no deja claro qué partición va en qué medio ni la cifra de 25 años; confirmar con el audio.

## 3. zram
Módulo del kernel que reserva RAM como dispositivo de intercambio comprimido.
- Comprime las páginas al vuelo (unos 30 % de reducción) y las guarda en la misma RAM; no toca el disco.
- Mostrado en vivo con `/dev/zram0`.
- ⚠️ Formato ext2 y compresores gzip y bzip2 según NotebookLM; en Linux real suele ser lzo, lz4 o zstd.

## 4. Temporizadores y relojes por software (3.5)
Servicios del kernel colgados del scheduler: hora y fecha, y calendarización de eventos (únicos o periódicos). El temporizador permite dormir al núcleo para ahorrar batería (marcapasos, 120 a 180 latidos por minuto). No se deben usar bucles de retardo activo.

## 5. Retardos síncronos
Sin sistema operativo, `delay()` ejecuta NOP y gasta energía. Con sistema operativo:
| Tiempo pedido | Comportamiento del scheduler |
|---|---|
| Cero | Reevalúa la cola READY y semáforos y devuelve el control casi de inmediato (nanosegundos) |
| Corto (0 a 100 ms) | Saca el proceso del CPU y lo reencola; sin precisión exacta (50 ms pueden ser 54 o más) |
| Largo (> 100 ms) | Suspende la tarea y programa una alarma para readmitirla |

## 6. Temporizador asíncrono periódico sin solapamiento
**Problema:** una función cada 10 ms que tarda 3, 15 y 25 ms genera hasta 3 instancias simultáneas.
!!! Solución («pregunta para entrar a Google»)
La función del temporizador solo hace `sem_post` sobre un semáforo binario; un hilo trabajador hace `sem_wait` y ejecuta el trabajo. A lo más hay una instancia a la vez.

El código de NotebookLM es una reconstrucción; el nombre de la bandera de control es dudoso.

## 7. Fecha y hora
- `date`: fecha y hora civil. `time`: tiempo de procesador y duración de un comando.
- El reloj de Linux suma ticks (jiffies) por interrupción; sin NTP durante un año se desfasa entre 4 y 10 minutos.
- Solución: RTC por hardware con batería o NTP.

## 8. Avisos
- Próxima clase: temporizadores asíncronos (`init_timer`, `add_timer`, `del_timer`, por confirmar), luego manejadores de dispositivos y sistema de archivos.
- Sin tarea nueva.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Patrón del temporizador (examen)
Temporizador: solo `sem_post`. Hilo trabajador: `sem_wait` y trabajo. Resultado: nunca dos instancias a la vez, aunque la tarea dure más que el periodo.

| Concepto | Idea clave |
|---|---|
| Swapping | Se mueven páginas, no archivos |
| Vida útil flash | 3.2×10⁷ s por año; 10⁷ escrituras duran meses, 10⁸ unos 3 años |
| zram | Swap comprimido dentro de la RAM, sin desgaste de flash |
| Retardo 0 / corto / largo | Reevalúa y devuelve / reencola sin precisión / suspende con alarma |
| `date` contra `time` | Hora civil contra tiempo de procesador |
| Jiffies | 4 a 10 minutos de deriva por año sin NTP |
