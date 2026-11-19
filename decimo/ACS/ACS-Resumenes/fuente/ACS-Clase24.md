% materia: Arquitectura Cliente-Servidor
% titulo: Clase 24 · Transferencia de archivos cifrada (FTP seguro)
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · martes 17 nov 2026 · Tema 4 (transferencia de archivos) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Culminación del semestre: `cliente_envia_encriptado.c` y `servidor_recibe_desencriptado.c` mandan un directorio completo cifrado con AES-256-CBC, con el IV de 16 bytes al inicio de cada archivo; cómo compartir la llave simétrica y por qué un archivo de 31 bytes cifrado pesa 48.

!!! Fuente
Fuente: NotebookLM (audio `ACS-Clase24.m4a`), 19 nov 2026. El profesor no dictó preguntas de examen; la sección de examen sale de lo que recalcó y de la pregunta capciosa que hizo al grupo. Junta la Clase 22 (cifrar archivos) y la Clase 23 (transferir archivos).

## 1. Distribuir la llave simétrica: el problema y ejemplos reales
Con cifrado simétrico, cliente y servidor necesitan exactamente la misma llave (32 bytes); el problema es cómo repartirla sin comprometer la confidencialidad.

!!! En simple
Un candado de combinación que deben conocer tú y el encargado de la bodega. Si el encargado cambia la combinación cada mañana, nadie con la de ayer puede entrar; si la anotan en un papel dentro de un cajón, ambos la consultan siempre, pero quien robe el papel abre todo. Límite: en un sistema asimétrico (como SSH) el candado se reparte abierto a todo el público y solo una persona guarda la llave que lo abre.

Abrió retomando el error de la clase anterior: si cliente y servidor no usan la misma llave exacta, el descifrado falla. Comparó dos diseños:

- **El servidor genera la llave al arrancar** (en RAM) y la distribuye. Desventaja: si el servidor se cae, se reinicia o hay un corte de luz, la llave cambia y las de los clientes anteriores ya no sirven. Ventaja: permite revocar accesos rápido si una llave fue robada.
- **La llave ya existe en un archivo** (`llave_archivo.key`), creada por un tercer programa generador, y ambos programas la leen. Persiste entre reinicios, pero hay que proteger ese archivo. Es el esquema que se usó en clase.

**Tarjeta bancaria con chip:** el chip trae grabada la llave simétrica y el servidor del banco guarda la misma, ligada a la cuenta. Al meter la tarjeta y teclear el NIP, el cajero cifra y el banco descifra. Si roban tarjeta y NIP, se rompe la confidencialidad de la triada de seguridad. Para más seguridad, un chip puede guardar varias llaves (K1, K2, K3) y elegir una al azar en cada sesión.

**¿La e.firma del SAT es simétrica o asimétrica?** (pregunta de una alumna). La regla que dio: si te dan una sola llave privada (`.key`), es simétrico; si se manejan dos (pública y privada), es asimétrico. En el SAT el `.cer` es el certificado; en SSH se genera la pareja de llaves (la pública a veces con extensión `.pub`).

Por qué importa: liga la triada de seguridad (confidencialidad, integridad, disponibilidad) con cajeros, certificados y firmas digitales.
Error común: confundir el certificado (`.cer`) con una llave simétrica.

## 2. El cliente: `cliente_envia_encriptado.c`
Lee la llave, recorre un directorio con `dirent.h`, omite lo que no debe mandar, cifra cada archivo y lo envía por TCP en tres pasos.

!!! En simple
Un archivista que empaca papeles para otra sucursal: descarta las referencias al piso actual y al de arriba («.» y «..»), deja fuera la llave de la bodega para no regalarla en el paquete, mete cada hoja en una caja fuerte portátil, le pega al frente el código de arranque (IV) y se la da al mensajero. Límite: si le pides empacar la oficina donde él mismo está, se empacaría a sí mismo.

**Uso:** `./cliente_envia_encriptado <IP_servidor> <puerto> <ruta_directorio>` (valida `argc == 4`).

**Llave:** abre `llave_archivo.key` con `fopen` en `"rb"` y la carga en un arreglo de 32 bytes.

**Recorrido:** `opendir(ruta_directorio)` da un `DIR *carpeta`; con `readdir` recorre cada entrada usando `archivo->d_name`.

**Exclusiones** dentro del `while` (con `strcmp` y `strstr`):
- «.» (directorio actual) y «..» (directorio padre).
- `llave_archivo.key`, para no cifrar ni mandar la llave por la red.
- Archivos que ya terminan en `.encrypt`, para no cifrar dos veces.
- El profesor se dio cuenta en vivo de que, si la ruta es la misma carpeta del ejecutable del cliente, hay que excluir también el propio ejecutable, o se cifra y se envía a sí mismo.

**Cifrado:** arma la ruta de salida agregando `.encrypt` con `snprintf` y llama a `encriptar_archivo(ruta_completa, ruta_encriptada, llave)`.

**Tres envíos por archivo:**
1. **Nombre** del archivo (ya con `.encrypt`).
2. **Tamaño** del archivo cifrado, obtenido con `stat` (`st_size`), como `long`.
3. **Contenido:** abre el `.encrypt` en `"rb"` y manda bloques con `fread` + `send` hasta que `fread` devuelve 0.

El profesor lo escribió por pasos: el nombre y el tamaño viajan **sin cifrar**; lo único cifrado es el **contenido**, «que es realmente lo que nos interesa».

Por qué importa: manda por lotes cualquier cantidad de archivos uniendo el sistema de archivos, OpenSSL y los sockets TCP.
Error común: no excluir `llave_archivo.key`, con lo que la llave terminaría en el servidor remoto.

## 3. El servidor: `servidor_recibe_desencriptado.c`
Escucha en un puerto, acepta un cliente, recibe uno por uno los archivos cifrados y, para cada uno, saca el IV de los primeros 16 bytes y descifra el resto en un archivo `.decrypt`.

!!! En simple
El encargado de la bodega recibe las cajas fuertes: anota el nombre, mide el peso total para no perder piezas, despega el código de arranque (IV) del frente y, con la llave de su gaveta, abre la caja y guarda los documentos con la etiqueta `.decrypt` para no pisar los originales. Límite: el IV no es secreto; sin la llave no sirve de nada.

**Uso:** `./servidor_recibe_desencriptado <puerto>` (valida `argc == 2`). Carga los 32 bytes de `llave_archivo.key` en `"rb"`.

**Socket:** `socket()` → `sin_family = AF_INET`, `sin_addr.s_addr = INADDR_ANY`, `sin_port = htons(puerto)` → `bind()` → `listen()` → `accept()`.

**Ciclo de recepción:**
1. Recibe el nombre (p. ej. `archivo1.txt.encrypt`). Si `recv` ≤ 0, el cliente terminó o se desconectó y sale del ciclo.
2. Recibe el tamaño total (un `long`).
3. Abre el archivo en `"wb"`, recibe los bloques con `recv` y los escribe con `fwrite`.

**Descifrado (`desencriptar_archivo`):** abre el archivo recibido en `"rb"` y lee **primero exactamente 16 bytes con `fread`: el IV**, que el cliente escribió ahí antes de los datos cifrados. Crea el contexto con `EVP_CIPHER_CTX_new()`, llama a `EVP_DecryptInit_ex` con AES-256-CBC, la llave y ese IV, y procesa el resto en bloques con `EVP_DecryptUpdate` y `EVP_DecryptFinal_ex`. Cambia `.encrypt` por `.decrypt` para no sobrescribir el original si cliente y servidor corren en la misma carpeta.

El código trae comentada una llamada a `remove()` (el equivalente en C de `rm`) para borrar el `.encrypt` temporal después de descifrarlo.

Por qué importa: cierra el ciclo de la arquitectura cliente-servidor segura; es el modelo de los programas de respaldo y sincronización seguros, y también la mecánica de un ransomware.
Error común: no separar exactamente los primeros 16 bytes del IV antes de `EVP_DecryptInit_ex`, o imprimir datos cifrados con `printf("%s")`.

## 4. Demostración y la pregunta capciosa: de 31 a 48 bytes
En `/tmp/temporal` el profesor creó `archivo1.txt` y `archivo2.txt` y los mandó al servidor del puerto 4898.

!!! En simple
Pesar el paquete en la báscula: además del mensaje con su relleno, pesa la etiqueta de apertura que va pegada al inicio de la caja.

`archivo1.txt` tenía una frase de prueba: 30 caracteres más el salto de línea `\n` que agrega Linux = **31 bytes**.

**La pregunta al grupo:** si AES trabaja en bloques de 16 bytes y el relleno PKCS sube al siguiente múltiplo (32), ¿por qué `archivo1.txt.encrypt` pesa **48**?

**Respuesta:** los 31 bytes se completan con 1 byte de relleno (valor `0x01`) y dan 32 bytes cifrados (dos bloques). Antes de ellos el programa escribe, sin cifrar, los **16 bytes del IV**: 16 + 32 = **48 bytes**.

```
./cliente_envia_encriptado 132.248.59.6 4898 /tmp/temporal
```

El cliente generó `archivo1.txt.encrypt` (48 bytes) y lo transmitió; el servidor recibió los 48, separó los 16 del IV, descifró los 32 y generó `archivo1.txt.decrypt` con los 31 bytes originales, comprobado con `cat`.

Por qué importa: junta el cálculo del relleno PKCS con el manejo de cabeceras en archivos binarios en una prueba medible.
Error común: olvidar que el `\n` final cuenta como un byte, o no sumar los 16 bytes del IV al tamaño del archivo cifrado.

## Contexto (no examen)
- Por copiar y pegar, el cliente imprimía «llave de desencriptación cargada» y el servidor «llave de encriptación cargada»; prometió corregirlo.
- Al dibujar la llave en el pizarrón bromeó con que nunca le sale bien.
- Varios alumnos le dijeron que ya terminaban otras materias, así que confirmó que esta es la última semana del curso.

## Pendiente / próxima clase
- **Ya no hay tareas para entregar.** El profesor dijo que tiene que devolver calificada la **Tarea 5** «en estos días».
- **Tarea moral (no se entrega):** probar el par cliente/servidor con archivos grandes (un PDF, un MP3, un video) y comprobar que el `.decrypt` abre igual que el original.
- **Programa final:** según NotebookLM, el «programa final» es este FTP cifrado que se fue armando en las clases 22–24; no hubo enunciado aparte, equipos, fecha de entrega ni rúbrica, y en las clases 23 y 24 quedó como tarea moral.
- **Próxima clase (jueves 19 nov): la última del semestre**, con ejemplos de serialización en Java. La semana siguiente ya no hay clase (el profesor da un curso del 23 al 27 nov). No mencionó otro examen.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Los tres envíos por archivo y que solo el contenido va cifrado.** lo escribió por pasos y recalcó que nombre y tamaño van en claro.
- **Calcular el tamaño del `.encrypt`: 31 bytes → 32 con relleno → 48 con el IV.** fue la pregunta capciosa al grupo.
- **Llave generada al arrancar contra llave en archivo.** dedicó la primera mitad de la clase a comparar disponibilidad y revocación.
- **Exclusiones al recorrer el directorio: «.», «..», la llave, los `.encrypt` y el propio ejecutable.** las mostró en el código y agregó la última en vivo.
- **El servidor lee primero 16 bytes (IV) y luego descifra con EVP.** fue el núcleo de `desencriptar_archivo`.

!!! Puntos clave
- Cliente: `argc == 4` (IP, puerto, directorio); servidor: `argc == 2` (puerto); ambos leen `llave_archivo.key` (32 bytes).
- Nombre y tamaño (`long`, con `stat`) en claro; contenido cifrado con AES-256-CBC.
- Archivo cifrado = IV (16 bytes, sin cifrar) + datos con relleno PKCS al múltiplo de 16.
- Servidor: `fread` de 16 bytes → `EVP_DecryptInit_ex` → `Update` → `Final`; salida `.decrypt`.
- Una llave = simétrico; pareja pública/privada = asimétrico.

## Ponte a prueba
1. **¿Qué argumentos pide `cliente_envia_encriptado`?** Cuatro contando el ejecutable: IP del servidor, puerto y ruta del directorio.
2. **¿Qué tres datos manda por archivo y cuál va cifrado?** Nombre, tamaño y contenido; solo el contenido va cifrado.
3. **¿Por qué el servidor guarda con `.decrypt`?** Para no sobrescribir el original si cliente y servidor corren en la misma carpeta.
4. **Un `datos.txt` de 42 bytes: ¿cuánto pesa `datos.txt.encrypt`?** 64 bytes: 42 sube a 48 con 6 bytes de relleno, más 16 del IV.
5. **Llave generada al arrancar contra llave en archivo.** La primera invalida a los clientes si el servidor se reinicia, pero permite revocar rápido; la segunda persiste, pero si se roba hay que reemplazarla en todos lados.
6. **¿Cómo distingues simétrico de asimétrico según el profesor?** Una sola llave privada = simétrico; dos llaves (pública y privada) = asimétrico.
7. **¿Qué omite el cliente al recorrer el directorio?** «.», «..», `llave_archivo.key`, los `.encrypt` y, si está en la misma carpeta, su propio ejecutable.
8. **¿Qué función borra el `.encrypt` temporal en el servidor?** `remove()`, el equivalente en C de `rm`.
