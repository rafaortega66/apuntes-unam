% materia: Arquitectura Cliente-Servidor
% titulo: Clase 22 · Llave compartida, cifrado de archivos por bloques y ransomware
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · martes 10 nov 2026 · Tema 2 (seguridad en cliente-servidor) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Por qué fallaba el descifrado en el cliente-servidor (llaves distintas), diseño e implementación de `encriptador.c` y `desencriptador.c` para cifrar archivos completos en bloques de 4,096 bytes, y anatomía de un ataque de ransomware.

!!! Fuente
Fuente: NotebookLM (audio `ACS-Clase22.m4a`), 14 nov 2026. El profesor no dijo qué vendría en el examen; la sección de examen sale de lo que enfatizó y demostró. Continúa la Clase 21.

## 1. La misma llave en ambos extremos
Verificar que cliente y servidor carguen exactamente el mismo `llave.key` y compilen con las bibliotecas de OpenSSL.

!!! En simple
Dos personas se mandan mensajes en un cofre: aunque la mensajería entregue intacto cada pedazo del cofre y en orden, si quien recibe usa una llave que fabricó esa mañana, no puede abrirlo. Límite: la respuesta «registro exitoso» viaja en texto plano, así que no depende de la llave.

El profesor corrió `crypto_v2`, que generó una llave nueva en el servidor. Compiló el cliente con `cc archivo.c -o ejecutable -lssl -lcrypto` (`-lssl` junto, espacio, `-lcrypto` con y).

Con el servidor en el puerto 4898 y el cliente hacia 132.248.59.6, mandó «Carlos» (6 caracteres → 16 bytes). El cliente imprimió 119, −111, −72, …, −40 y el servidor recibió exactamente esos bytes en el mismo orden, pero el nombre descifrado salió vacío.

Era el mismo fallo del final de la clase anterior: los clientes usaban el `llave.key` del repositorio de Git y el servidor la llave recién generada. Lo resolvió descargando la llave del repositorio y copiándola al servidor con `scp llave.key 132.248.59.6:<ruta>`. Al reiniciar, el servidor ya descifró los nombres (Víctor, 6 bytes + 10 de relleno; Ángel, Miriam, Osvaldo, Juan Carlos, Cynthia).

Aclaró que quienes usaron Codespaces en el examen parcial obtuvieron otra hora con `date` porque ese entorno tiene otro huso horario.

Por qué importa: Es la regla básica del cifrado simétrico: aunque el transporte sea perfecto, con otra llave no se descifra.
Error común: tener otra versión de `llave.key` en el servidor; olvidar `-lssl -lcrypto`.

## 2. Diseño: cifrar archivos completos (`encriptador.c` y `desencriptador.c`)
Dos programas en C que cifran el contenido binario completo de cualquier archivo (.txt, .jpg, .mp3, .mp4, .pdf) por bloques de 4,096 bytes y lo reconstruyen sin alterar un solo byte.

!!! En simple
Es una mudanza: no cabe la casa en una caja, así que empacas en cajas estándar de 4,096 y pegas la etiqueta con el ajuste inicial de la cerradura (el IV) al principio de la primera caja, sin candado. Límite: si en la mudanza falta un plato, pierdes un plato; si a un PDF le falta un byte, todo el archivo queda corrupto.

El profesor abrió el PDF «Análisis del par de programas encriptador y desencriptador» (antes corrigió en su página la liga a la que le faltaba `.pdf`). Para AES todo archivo es una secuencia de bytes.

`encriptador` recibe el nombre del archivo, genera y guarda una llave nueva en `llave_archivo.key` (otro nombre para no pisar `llave.key`) y crea `archivo.encrypt`. `desencriptador` recibe el .encrypt, lee `llave_archivo.key` y crea `.decrypt`, idéntico al original.

**Reto 1, el tamaño:** un video de 2 GB no cabe en RAM como las cadenas de `crypto.c`. Se usa un `while` con un búfer de **4,096 bytes, el tamaño de una página de memoria**.

**Reto 2, el IV:** es aleatorio, así que el desencriptador no puede generar otro. En el cliente-servidor se mandaba en tres `send`; aquí el encriptador **escribe los 16 bytes del IV sin cifrar al principio del .encrypt** y después los bloques cifrados.

1. **Encriptador:** abrir el original y crear el .encrypt; generar y guardar la llave; escribir el IV al inicio; en un `while` leer hasta 4,096 bytes, cifrar y escribir; al final, el relleno y cerrar.
2. **Desencriptador:** abrir el .encrypt y crear el .decrypt; leer los primeros 16 bytes (el IV); leer la llave; en un `while` leer el resto, descifrar y escribir; cerrar.

Por qué importa: Une el cifrado de OpenSSL con el tamaño de página de memoria y con el manejo de archivos en disco.
Error común: querer cargar un archivo de gigas completo en RAM; creer que el IV se cifra o que se puede regenerar al descifrar.

## 3. Anatomía de un ataque de ransomware
Software malicioso que combina ingeniería social, exfiltración de archivos por sockets en segundo plano y cifrado de los archivos de la víctima para exigir un rescate a cambio de la llave.

!!! En simple
Alguien disfrazado de mensajero de tu universidad te deja un paquete; al abrirlo entra un ladrón que fotocopia tus documentos y los saca por la ventana, y luego guarda tus originales en una caja fuerte cuya llave solo él tiene. Límite: aunque tengas respaldos y no pagues, el atacante ya tiene copia de tus datos.

1. **Engaño (ingeniería social):** un correo con adjunto o liga adaptado a la víctima (a empleados, una factura; a estudiantes, un aviso falso de que su cuenta de ingenieria.unam.edu caduca o una liga para evaluar profesores). Los alumnos dijeron que revisan el remitente, pero el *From* puede venir falseado: usar «Mostrar original» o «Ver origen del mensaje» para ver los metadatos. «Se confía, pero se comprueba.»
2. **Infección:** la víctima abre el adjunto o la liga y se instala el ransomware.
3. **Exfiltración:** antes de cifrar, abre un socket en segundo plano y manda copia de los archivos al atacante (un síntoma es que la computadora se alenta).
4. **Cifrado y extorsión:** cifra los archivos y pide el rescate, normalmente en Bitcoin.

Tener respaldos (por ejemplo, de la medianoche anterior) evita perder la operación, pero queda el daño económico (si se paga, a veces ni mandan la llave) y el reputacional, porque los datos pueden venderse o exponerse. Tampoco hay que escanear códigos QR desconocidos.

Por qué importa: Junta los sockets y el par encriptador/desencriptador del curso con un ataque real.
Error común: confiar solo en el nombre del remitente; creer que con respaldos desaparece el daño; escanear cualquier QR.

## 4. Revisión de `encriptador.c` y prueba en vivo
La implementación en C con la API EVP de OpenSSL, E/S binaria (`fopen`, `fread`, `fwrite`, `fclose`) y `snprintf`.

!!! En simple
Es la empacadora por dentro: etiqueta las cajas sin salirse del espacio (`snprintf`), toma montones de hasta 4,096 de la banda (`fread`), los sella en una caja un poco más grande para que quepa el relleno y, cuando la banda se vacía, pone el sello final.

**Nombres:** un arreglo de 512 `char` para el nombre de salida, armado con `snprintf`, que recibe el búfer, el tamaño máximo (incluido el terminador), el formato y los argumentos; a diferencia de `sprintf`, no desborda.

**Llave, IV y archivos:** genera la llave y la guarda en `llave_archivo.key`; abre el original con `"rb"` y el .encrypt con `"wb"`, y escribe primero los 16 bytes del IV (no es secreto).

**Contexto y búferes:** `EVP_CIPHER_CTX_new()` (EVP = *envelope*); búfer de entrada de 4,096 bytes y de salida de `4096 + EVP_MAX_BLOCK_LENGTH`, para que quepa el relleno en cualquier distribución.

**Ciclo:** `fread` lee hasta 4,096 bytes y devuelve cuántos leyó (pueden ser menos, por ejemplo 1,024); mientras sea mayor que 0, cifra y escribe con `fwrite`. Al llegar a 0 sale, hace el paso final con el relleno, libera y cierra.

**Prueba:** `archivo.txt` con «Hola Mundo» (10 bytes; Linux lista 11 por el salto de línea). `gcc encriptador.c -o encriptador -lssl -lcrypto` y `./encriptador archivo.txt` generaron `llave_archivo.key` (32 bytes) y `archivo.txt.encrypt` de **32 bytes = 16 del IV + 16 del bloque**. Abierto como texto no se ven los 32 porque los valores 0 a 32 no son visibles: se lee byte por byte. Luego `./desencriptador archivo.txt.encrypt` creó `archivo.txt.encrypt.decrypt` con «Hola Mundo» intacto.

Por qué importa: Convierte la teoría en herramientas que funcionan; el código de `desencriptador.c` se revisa la siguiente clase.
Error común: correr los programas sin el nombre del archivo; olvidar `-lssl -lcrypto`; tratar el .encrypt como cadena de texto.

## Pendiente / próxima clase
- No hay tarea para entregar; repasar probando el encriptador, el desencriptador y el par cifrado.
- El profesor sigue sin terminar de calificar la Tarea 5 y compartirá el PDF de la presentación de ransomware.
- **Jueves:** análisis del código de `desencriptador.c`. Quedan dos semanas (5 clases) para terminar.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **En cifrado simétrico la llave debe ser idéntica en ambos extremos; compilar con `-lssl -lcrypto`.** dedicó el inicio a mostrar que los 16 bytes llegaban iguales pero el texto salía vacío por usar llaves distintas, y repitió la sintaxis de compilación.
- **Cifrar archivos por bloques de 4,096 bytes y dónde va el vector de inicialización.** explicó el PDF paso a paso, recordó por qué 4,096 (tamaño de página) y mostró que el .encrypt de «Hola Mundo» mide 32 bytes.
- **Abrir en binario (`"rb"`, `"wb"`) y leer byte por byte.** lo señaló varias veces en el código y explicó por qué no se ven los 32 bytes al abrir el archivo como texto.
- **`snprintf` y `EVP_MAX_BLOCK_LENGTH` para no desbordar búferes.** consultó la documentación de Open Group en clase.

!!! Puntos clave
- Cifrado simétrico: la misma llave en ambos extremos o el descifrado sale vacío.
- Archivos grandes: bloques de 4,096 bytes (tamaño de página) en un `while`.
- IV de 16 bytes escrito sin cifrar al inicio del .encrypt; «Hola Mundo» → 32 bytes.
- `"rb"` / `"wb"`, `snprintf` y `4096 + EVP_MAX_BLOCK_LENGTH`.
- Ransomware: engaño → infección → exfiltración por socket → cifrado y rescate.

## Ponte a prueba
1. **¿Cómo se compila `encriptador.c`?** `cc encriptador.c -o encriptador -lssl -lcrypto` (o con gcc).
2. **Los 16 bytes de «Carlos» llegaron iguales al servidor pero el nombre salió vacío. ¿Por qué y cómo se arregló?** El servidor tenía una llave distinta a la de los clientes; se copió la llave del repositorio al servidor con scp.
3. **«Buenas noches» mide 13 bytes. ¿Cuánto mide `nota.txt.encrypt`?** 32 bytes: 16 del IV sin cifrar más 16 del bloque (13 bytes + relleno).
4. **¿Por qué un búfer de 4,096 bytes y uno de salida de `4096 + EVP_MAX_BLOCK_LENGTH`?** Porque un archivo grande no cabe en RAM y 4,096 es el tamaño de página; lo extra es para el relleno.
5. **¿Cómo se comparte el IV en el cliente-servidor y en el par de archivos?** En el cliente-servidor, en el primero de tres `send`; en los archivos, escrito sin cifrar en los primeros 16 bytes del .encrypt.
6. **¿Qué pasa si falta un byte en un .txt y en un .pdf? ¿Qué diferencia hay entre `sprintf` y `snprintf`?** El .txt sale incompleto; el .pdf queda corrupto. `snprintf` recibe el tamaño máximo y evita desbordar.
7. **¿Por qué no hay que tomar los primeros 16 caracteres visibles del .encrypt como el IV?** Porque muchos bytes (0 a 32) no son visibles; hay que abrir en binario y leer byte por byte.
8. **¿Por qué los respaldos no eliminan todo el daño de un ransomware?** Porque antes de cifrar ya mandó copia de los archivos al atacante: queda el daño reputacional.
