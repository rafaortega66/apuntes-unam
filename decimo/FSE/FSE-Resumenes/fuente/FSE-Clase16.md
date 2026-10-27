% materia: Fundamentos de Sistemas Embebidos
% titulo: Clase 16 · Linux embebido: elegir el kernel
% subtitulo: Fundamentos de Sistemas Embebidos · M.C. José Mauricio Matamoros de María y Campos · miércoles 21 oct 2026 · Tema 3 (3.9) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Cambio de orden del temario
El profesor adelantó la selección de Linux y la compilación del kernel ("un salto cuántico al futuro") para no retrasar las prácticas. Los algoritmos de planificación de propósito general (Round Robin) y las frecuencias del scheduler **se pospusieron, no se eliminaron**. Nadie se opuso.

## 2. Cómo elegir el kernel de Linux para un embebido
!!! Regla de examen
En un sistema embebido se elige un kernel **estable, maduro y probado** (soporte largo, **LTS**), no el más reciente. Una versión nueva solo se justifica si un hardware de última generación tiene su controlador únicamente ahí.

**Monitoreo en kernel.org.** Hay que suscribirse a la lista de notificaciones de la versión elegida:
| Rama | Correos que llegan |
|---|---|
| Madura (ejemplo: kernel 4.x) | Muy pocos, ≈ 2 al año |
| En desarrollo activo (ejemplo: 6.11) | Hasta ≈ 30 al día, con errores que nadie ha probado |
Un alumno de otra generación se suscribió a la rama equivocada y se le llenó la bandeja.

**Parches.** Cada parche se evalúa: ¿corrige un error que afecta mi sistema (se integra) o rompe la estabilidad de otros controladores?
Errores comunes: elegir siempre la versión más nueva por parecer "la mejor"; no vigilar los parches de seguridad de la versión elegida.

## 3. Por qué no un sistema de escritorio en un embebido
Un SO de escritorio (administrador de ventanas y atajos) en un equipo de propósito específico es un **riesgo de seguridad**.
- Ejemplo: quioscos de autoservicio de comida rápida que terminan corriendo **Doom**.
- Con **Alt+Tab** o **Alt+F4** se cierra la aplicación principal y se llega al sistema, incluso a un usuario con privilegios.
- Por eso el laboratorio pide un Linux mínimo en modo consola (Clase 13).

## 4. Árbol de directorios y familias de distribuciones
!!! Raíz única
En sistemas tipo UNIX/POSIX hay una sola jerarquía: todo directorio, archivo, partición y dispositivo cuelga de la raíz **/**. No hay letras de unidad (C:, D:).

| Sistema | Dónde aparecen los dispositivos externos |
|---|---|
| macOS | `/Volumes` |
| Linux moderno | `/media` |
| Linux tradicional / montaje manual | `/mnt` |

**Familias.** De UNIX derivan Linux, Minix y BSD (de BSD: macOS y FreeBSD).
| Familia Linux | Distribuciones | Paquetes |
|---|---|---|
| Debian | Ubuntu, Linux Mint, **Raspberry Pi OS** | `apt` |
| Red Hat | Fedora (y SUSE según NotebookLM; SUSE usa RPM pero no es rama Red Hat: confirmar) | RPM con `dnf`/`yum` |
| Independientes | Arch | — |
Es la base para construir el sistema de archivos raíz (**RootFS**) de una distribución embebida y ubicar binarios, librerías e intérpretes (bash, sh).

## 5. Reglas de la Práctica 8 (compilar el kernel)
- La **primera compilación se hace en casa**, antes del laboratorio: obligatorio.
- Tiempos: ≈ 45 min en un equipo potente (SSD, 12 núcleos, 32 GB RAM); **4 a 6 horas** en equipos modestos o con disco mecánico. Conviene dejarla corriendo la noche anterior.
- **Prohibido** descargar o compilar por primera vez en el laboratorio: no hay tiempo, los equipos no son potentes y no hay permisos elevados. Se llega con la compilación lista para pruebas y modificaciones.
Sin tareas nuevas; la planificación de tiempo real (3.3) queda pospuesta.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Kernel para un embebido (examen)
Estable y maduro (LTS), no el más reciente; uno nuevo solo si el hardware lo exige. Suscribirse a la lista de kernel.org (rama madura ≈ 2 correos/año; rama en desarrollo ≈ 30/día) y evaluar cada parche.

**Escritorio = riesgo.** Quioscos con Doom; Alt+Tab o Alt+F4 abren el sistema. Usar Linux mínimo en consola.

| Concepto | Para recordar |
|---|---|
| Raíz | Una sola jerarquía desde `/`; sin letras de unidad |
| Montaje | macOS `/Volumes`; Linux `/media` o `/mnt` |
| Debian | Ubuntu, Mint, Raspberry Pi OS — `apt` |
| Red Hat | Fedora — RPM (`dnf`/`yum`) |
| Práctica 8 | Primera compilación en casa (45 min a 6 h) |
