% materia: Arquitectura Cliente-Servidor
% titulo: Clase 3 · SetUID en Codespaces, bits especiales, errno y la red de la FI
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · martes 1 sep 2026 · Tema 1 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Codespaces y ajuste de la Tarea 2
- Botón "Code" → pestaña Codespaces (con sesión de GitHub) → "Create codespace on main" → "Confiar y continuar". Abre VS Code en el navegador.
- Si sales sin destruirlo, queda **pausado pero vivo** y consume la cuota gratuita.
- `fdisk` no existe en el contenedor: la Actividad 1 solo con Linux propio; la **Actividad 2** (programa02_ids.c con getuid/geteuid bajo SetUID) es obligatoria para todos.
- get = leer; set = escribir. En C todo parte de `main`.

## 2. Demo del bit SetUID
```
whoami                         # codespace (UID 1000)
gcc programa02_ids.c -o programa02_ids   # quitar el .c del -o
./programa02_ids               # real = efectivo = 1000
sudo su                        # root (UID siempre 0)
cat /etc/passwd ; cat /etc/shadow
chown root:root programa02_ids
chmod 700 programa02_ids       # el usuario codespace: "Permiso denegado"
chmod 4511 programa02_ids      # 4 = SetUID: la x del usuario se vuelve s
./programa02_ids               # (como codespace) real = 1000, efectivo = 0
```
!!! Real vs. efectivo (examen)
Con SetUID y dueño root, quien lo lanza (1000) es el usuario **real** y el dueño del archivo (0, root) el **efectivo**. El cambio es **temporal**: solo mientras el proceso vive.
- En algunas distros root no aparece en `/etc/passwd` sino "en las sombras" (`/etc/shadow`), junto a demonios como sys.
Error común: escribir `-o programa02_ids.c` y sobrescribir el fuente.

## 3. Bits especiales (4.º dígito de chmod)
| Dígito | Bit | Efecto visible |
|---|---|---|
| 4 | SetUID | `s` en el usuario |
| 2 | SetGID | `s` en el grupo; cambia grupo real y efectivo |
| 6 | Ambos | — |
| 1 | Sticky | `t`/`T` en "otros" (chmod 1511) |
Solo existen `getuid`, `geteuid`, `getgid`, `getegid`; no hay "get others ID", así que el sticky no se puede demostrar desde C.

## 4. errno
- Variable **global** en minúsculas que el sistema fija cuando hay error; no se declara.
- ~131 códigos estándar (en el contenedor la tabla llega a 133); macros con E: **ENOENT** (2, *No such file or directory*), **EPERM** (sin privilegios), **EIO** (E/S).
- **0 = éxito**; cualquier otro entero = error. Por eso `main` termina con `return 0;`.
- programa03_codigos_sistema.c recorre 0–150 con `strerror(i)`: 0 → *Success*, 2 → *No such file…*, sobrantes → *Unknown error*.

## 5. Red de la Facultad de Ingeniería
- **132.247.x.x y 132.248.x.x** = IPs públicas de la UNAM; tercer octeto **59** = FI.
- Años 90, cuatro subredes: **FI-A** (Principal), **FI-B** (Anexo), **FI-C** (Ciencias Básicas), **FI-P** (Posgrado). El servidor de profesores está en Posgrado.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| SetUID | `chown root:root` + `chmod 4511` → real 1000, efectivo 0 |
| Bits | 4 SetUID, 2 SetGID, 1 sticky |
| root | UID 0; puede estar en /etc/shadow |
| errno | Global; 0 éxito; ENOENT = 2 |
| UNAM | 132.247 / 132.248; FI = .59; FI-A, B, C, P |
