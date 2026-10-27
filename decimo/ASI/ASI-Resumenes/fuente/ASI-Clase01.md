% materia: Administración de Servicios de Internet
% titulo: Clase 1 · Von Neumann vs. Harvard, jerarquía de Linux y Práctica 0
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · miércoles 26 ago 2026 · Tema 1 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Del modelo de Turing a Von Neumann
- El procesador es la abstracción física de la **Máquina de Turing** (autómata de doble pila con lenguaje finito): un autómata simple puede computar cualquier cosa computable.
- **Von Neumann:** controlador, registro de estado, registros generales, contador de programa, ALU, **una sola memoria** para programa, datos y pila, y E/S mapeadas.
!!! Cuello de botella (examen)
Con un solo bus y una memoria, Fetch → Decode → Execute → Write Back va en serie y casi todo está ocioso. En un `for` sobre CISC, la ALU calcula solo el **20–33 %** del tiempo; el **66–80 %** se pierde en accesos a memoria.

## 2. Harvard/RISC y pipeline
- **Patterson y Hennessy:** modelo **Load-Store**: todo programa se reescribe con carga, almacenamiento y una ALU simple (equivalente a Turing).
- **Harvard** separa memoria de instrucciones y de datos: leer instrucción y dato a la vez.
| Ciclo | F | D | E | WB |
|---|---|---|---|---|
| T1 | I1 | | | |
| T2 | I2 | I1 | | |
| T3 | I3 | I2 | I1 | |
| T4 | I4 | I3 | I2 | I1 |
Tras 4 ciclos de llenado, **una instrucción por ciclo**.

## 3. Jerarquía de Linux (FHS)
| Directorio | Prioridad | Contenido |
|---|---|---|
| /boot | Alta | Arranque y kernel |
| /bin | Alta | Binarios esenciales |
| /dev | Alta | Archivos de dispositivos |
| /etc | Alta | Configuración (tocarlo mal = borrar System32) |
| /usr | Alta | Programas, bibliotecas, documentación (no es de usuarios) |
| /lib | Alta | Bibliotecas compartidas |
| /var | Media | Logs, temporales, colas |
| /root | Media | Home del superusuario |
| /home | — | Homes de usuarios |
| /tmp | Baja | Temporales; se borran al reiniciar |
| /opt | — | Software de terceros |
Rutas relativas (desde el directorio actual) vs. absolutas (desde /).

## 4. Elegir distribución
| Distro | Uso |
|---|---|
| Ubuntu | Principiantes |
| Debian | Servidores (estable) |
| Fedora | Desarrollo |
| CentOS → AlmaLinux | Servidores gratuitos basados en Red Hat |
| Red Hat | Empresarial de paga |
| Arch | Avanzados, instalación manual |
| Linux Mint | Migrar usuarios de Windows |
| Kali | Ciberseguridad |

## 5. Comandos de la Práctica 0
- `whereis ls`: todas las rutas (binarios, fuentes, manuales); `which ls`: solo el ejecutable. `man ls` (salir con q).
- `ps`: procesos de la sesión. `ps aux`: **a** todos los usuarios, **u** uso de recursos, **x** procesos **sin terminal** (primer chequeo ante malware). `top`: tiempo real.
- `nano` (Ctrl+X para salir); `cat -n` numera líneas; `cat archivo1.txt archivo2.txt > todito.txt` concatena **en ese orden** (invertir cambia el resultado).
- `ls -l`, `-a` (ocultos, . y ..), `-s`, `-h`; combinables (`ls -la`).
- Permisos de 10 caracteres: tipo (- o d), propietario, grupo, otros; **r = 4, w = 2, x = 1**. **Nunca 777.**
- `mkdir -m 700 reprobados21` (permisos al crear); `mkdir -p reprobados/271/ads` (árbol completo; sin `-p` falla).

## Pendiente: Práctica 0 "Uso básico de Linux"
Desarrollo con lo visto en clase; Resultados investigando `tree`, `ls -d`, `ls -h`, `ls -R`, `grep`, `touch` y `tee`. PDF individual **P0_usobasico_INICIALES.pdf**.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Von Neumann | Una memoria; ALU útil solo 20–33 % |
| Harvard/RISC | Memorias separadas + pipeline: 1 instrucción por ciclo |
| FHS | /etc config, /bin binarios, /boot arranque, /tmp se borra |
| ps aux | a todos, u recursos, x sin terminal (malware) |
| Permisos | r4 w2 x1; nunca 777 |
| mkdir | -m permisos, -p árbol |
