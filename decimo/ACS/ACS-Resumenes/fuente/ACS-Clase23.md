% materia: Arquitectura Cliente-Servidor
% titulo: Clase 23 · Transferencia de archivos tipo FTP con sockets
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · jueves 12 nov 2026 · Tema 4 (transferencia de archivos) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Un FTP básico en C: recorrer directorios con `dirent.h`, protocolo de tres envíos por archivo (nombre, tamaño y contenido en bloques de 1,024 bytes) y `accept()` fuera del ciclo; aclaraciones sobre DDoS con IoT y la exfiltración del ransomware.

!!! Fuente
Fuente: NotebookLM (audio `ACS-Clase23.m4a`), 14 nov 2026. El profesor no dijo qué vendría en el examen; la sección de examen sale de lo que enfatizó. Continúa la Clase 22.

## 1. Aclaraciones: DDoS con IoT y exfiltración del ransomware
Un DDoS satura un servidor con peticiones ilegítimas desde muchos dispositivos infectados. En el ransomware, los archivos robados pueden viajar al atacante en texto plano o ya cifrados.

!!! En simple
Miles de llamadas falsas a la misma pizzería: mientras el empleado las contesta, los clientes reales encuentran la línea ocupada. Límite: quienes llaman no son personas, sino cámaras y aparatos IoT infectados sin que sus dueños lo sepan.

Lo ligó con la cola SYN y los valores 0 y 1 que se ajustaron en la Tarea 4: con valores mayores hay más reintentos y se pueden dejar peticiones en espera; con 0 y 1 se rechazan rápido.

En el ransomware, tras infectar, el programa abre un socket y manda los archivos al atacante: en texto plano (y luego cifra los locales) o cifrándolos primero. Al atacante no le importa recibirlos cifrados porque tiene la llave.

## 2. Listar un directorio con `dirent.h` (`listado_archivos.c`)
Programa local en C que hace lo básico de `ls`: lista los nombres del directorio actual con `dirent.h`.

!!! En simple
Un bibliotecario abre el cajón de fichas (`opendir`), saca tarjeta por tarjeta (`readdir`) leyendo el título (`d_name`) y cierra el cajón (`closedir`). Límite: en Linux todo es archivo: también salen las subcarpetas y las entradas «.» y «..».

Declara `DIR *carpeta` y `struct dirent *archivo`; abre con `opendir(".")` (el directorio actual; puede ser cualquier ruta) y si devuelve `NULL` hace `perror` y termina.

`while ((archivo = readdir(carpeta)) != NULL)`: cada llamada avanza a la siguiente entrada y al final devuelve `NULL`. Como `archivo` es apuntador a estructura, se usa **`archivo->d_name`** (flecha, no punto). Al terminar, `closedir`.

Se compila con `gcc listado_archivos.c -o listado_archivos` (sin OpenSSL).

Por qué importa: Permite que el cliente descubra solo los archivos de una carpeta.
Error común: usar el punto en vez de la flecha con un apuntador a estructura.

## 3. Cliente y servidor de transferencia de archivos
`cliente_envia_archivos.c` recorre un directorio y manda cada archivo completo en bloques de 1,024 bytes; `servidor_recibe_archivos.c` los recrea en su directorio actual. Es un FTP básico sin cifrar.

!!! En simple
Mandar una colección de libros en sobres de tamaño fijo: primero una etiqueta con el título para que el receptor prepare la carpeta, luego cuántas páginas trae y después las páginas en sobres hasta completar la cuenta. Límite: si falta una página lees el resto; si falta un byte, el archivo queda corrupto.

¿Qué necesita el servidor? El grupo dijo nombre, ruta, tamaño y permisos. **Nombre** (hasta 256 caracteres, el límite de los sistemas operativos); la **ruta** no se manda (el servidor guarda en su directorio actual); el **tamaño** en `long` (más amplio que `int`) para saber cuántos bytes leer; los permisos importan, pero aquí se asume lectura.

**Tres envíos contra dos:** con dos (nombre y contenido) el servidor tendría que reservar un búfer enorme y luego recortarlo; con tres controla el tamaño exacto a cambio de un envío más. Depende del hardware del servidor y de la latencia.

**Cliente** (`./cliente_envia_archivos IP puerto directorio`): valida `argc != 4`, prepara `sockaddr_in`, hace `connect`, recorre el directorio **saltándose «.» y «..»** y por cada archivo: (1) manda el nombre, (2) obtiene el tamaño con `stat` (`st_size`) y lo manda, (3) abre con `"rb"` y manda bloques de hasta 1,024 bytes con `fread` mientras lea más de 0.

**Servidor** (`./servidor_recibe_archivos puerto`): `INADDR_ANY`, `bind`, `listen` (backlog 1) y **`accept()` antes del `while(1)`**, porque atiende a un solo cliente y el ciclo es para recibir varios archivos de esa conexión. En cada vuelta: (A) recibe el nombre; si `recv` da ≤ 0, el cliente terminó y hace `break`; (B) recibe el tamaño y crea el archivo con `"wb"`; (C) `while (total_recibido < tamano_archivo)` con `a_leer = 1024`, o lo que falte si es menos; `recv`, `fwrite` y `total_recibido += leidos`; al final `fclose`.

**Traza (2,048 bytes, búfer de 1,024):** vuelta 1: 2048 − 0 < 1024 es falso → lee 1,024, total = 1,024. Vuelta 2: 2048 − 1024 < 1024 es falso (es igual) → lee 1,024, total = 2,048. 2048 < 2048 es falso → sale tras exactamente 2 `recv`.

**Prueba en vivo:** cliente en GitHub Codespaces (sin IP pública) hacia 132.248.59.6:4898; el servidor corría en una carpeta vacía; se mandaron `archivo1.txt` y `archivo2.txt` (21 bytes cada uno) y llegaron intactos.

Por qué importa: Junta directorios, protocolo síncrono y archivos binarios; la siguiente clase se le integra el cifrado para un FTP seguro.
Error común: no filtrar «.» y «..»; usar `int` para el tamaño; olvidar `fclose`; correr el servidor en una carpeta llena de otros archivos.

## Pendiente / próxima clase
- No hay tarea para entregar; probar el par cliente/servidor con archivos binarios grandes, con el servidor en una carpeta vacía.
- **Próxima clase:** integrar el cifrado a la transferencia para un FTP seguro. El profesor avisará si las últimas clases terminan antes.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **El protocolo de tres envíos por archivo: nombre, tamaño y contenido en bloques.** preguntó al grupo qué datos necesita el servidor y comparó tres envíos contra dos.
- **`accept()` antes del `while(1)` en el servidor receptor.** lo remarcó leyendo el comentario del código.
- **Recibir exactamente los bytes del archivo: `while (total_recibido < tamano_archivo)`.** hizo la traza completa con un archivo de 2,048 bytes y búfer de 1,024.
- **`dirent.h` (DIR, struct dirent, opendir, readdir, closedir) y saltarse «.» y «..».** compiló primero `listado_archivos.c` e insistió en el operador flecha.
- **Tipos y modos: `long` para el tamaño, nombre de 256, `"rb"` / `"wb"`.** justificó cada elección.

!!! Puntos clave
- `dirent.h`: opendir → readdir (hasta NULL) → closedir; `archivo->d_name`; saltar «.» y «..».
- Tres envíos por archivo: nombre (256), tamaño (`long`, con `stat`), contenido en bloques de 1,024.
- Servidor: `accept()` antes del `while(1)`; `recv` ≤ 0 = el cliente terminó.
- `while (total_recibido < tamano_archivo)` con `a_leer` = lo que falte, máximo 1,024.

## Ponte a prueba
1. **¿Qué tres cosas manda el cliente por cada archivo?** Nombre, tamaño y contenido en bloques de 1,024 bytes.
2. **¿Por qué `accept()` va antes del `while(1)`?** Porque el servidor atiende a un solo cliente y el ciclo recibe varios archivos de esa misma conexión.
3. **Archivo de 2,500 bytes con búfer de 1,024: ¿cuántos `recv` y de cuánto?** Tres: 1,024, 1,024 y 452.
4. **¿Por qué `archivo->d_name` y no `archivo.d_name`?** Porque `archivo` es un apuntador a estructura.
5. **¿Por qué el tamaño va en `long`?** Porque es más amplio que `int` y alcanza para archivos grandes.
6. **Tres envíos contra dos.** Con dos el servidor reserva un búfer enorme y recorta; con tres sabe el tamaño exacto a cambio de un envío más.
