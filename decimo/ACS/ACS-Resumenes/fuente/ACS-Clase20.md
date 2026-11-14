% materia: Arquitectura Cliente-Servidor
% titulo: Clase 20 · Criptografía simétrica con OpenSSL: AES-256-CBC (reconstruida)
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · martes 3 nov 2026 · Tema 4 (criptografía simétrica con OpenSSL) · clase reconstruida · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ El problema del texto plano, AES-256, modo CBC, vector de inicialización y relleno PKCS#7, la interfaz EVP de OpenSSL, `RAND_bytes` y `llave.key`, y el programa `cripto.c`.

!!! Fuente
Fuente: material oficial del profesor en su sitio (Tema 4): presentación «Criptografía simétrica en C con OpenSSL» y `cripto.c`. ⚠️ **No asistí a esta clase y no hay audio.** El contenido se reconstruyó con la presentación del profesor, cuya última diapositiva anuncia como siguiente sesión la integración con el cliente-servidor (lo que se vio en la Clase 21). No está confirmado qué se vio exactamente ese día.

## 1. El problema del texto plano
`send()`, `recv()`, `write()` y `read()` pasan los bytes de la RAM a la pila TCP/IP sin ninguna protección.

Amenazas según UIT-T X.800: **interceptación** (confidencialidad: un sniffer en modo promiscuo, Clase 19) y **modificación** (integridad: un *man-in-the-middle* que altera bytes).

Objetivo: transformar el búfer local (`textoOriginal` → `textoEncriptado`) y proteger la llave antes de integrarlo al cliente-servidor.

## 2. AES-256, modo CBC, IV y relleno
Criptografía simétrica: la misma llave cifra y descifra. AES (FIPS 197) usa bloques de **128 bits (16 bytes)**; AES-256 usa una llave de **256 bits (32 bytes)** y 14 rondas.

En C, `unsigned char` mide 1 byte: `unsigned char llave[32];` (256 bits) y `unsigned char iv[16];` (128 bits).

**CBC** (*Cipher Block Chaining*): cada bloque de texto se combina con XOR con el bloque cifrado anterior, para eliminar patrones repetidos. El **IV** es un bloque aleatorio de 16 bytes que se combina con el primer bloque.

**Relleno PKCS#7:** completa el último bloque cuando el mensaje no es múltiplo de 16; por eso al arreglo `textoEncriptado` se le suma `EVP_MAX_BLOCK_LENGTH`.

## 3. OpenSSL: bibliotecas, EVP y la llave
OpenSSL tiene dos bibliotecas: `libssl` (protocolos TLS/DTLS) y `libcrypto` (algoritmos, generador aleatorio seguro y certificados).

Cabeceras de `cripto.c`: `<openssl/evp.h>` (interfaz de alto nivel EVP, *envelope*, que reemplaza APIs obsoletas y aprovecha AES-NI) y `<openssl/rand.h>` (generador pseudoaleatorio criptográficamente seguro).

`RAND_bytes()` toma entropía del kernel para llenar la llave y el IV. La llave se guarda en `llave.key` en modo **`"wb"`**, porque los bytes crudos pueden incluir 0x00 o 0x0A, que el modo texto corrompería.

```
if (!RAND_bytes(llave, sizeof(llave)) || !RAND_bytes(iv, sizeof(iv))) manejarErrores();
FILE *archivoLlave = fopen("llave.key", "wb");
fwrite(llave, 1, sizeof(llave), archivoLlave);
fclose(archivoLlave);
```

## 4. El ciclo EVP: cifrar y descifrar
Una máquina de estados sobre un contexto `ctx`.

1. `EVP_CIPHER_CTX_new()`: reserva el contexto en el *heap*.
2. `EVP_EncryptInit_ex(ctx, EVP_aes_256_cbc(), NULL, llave, iv)`.
3. `EVP_EncryptUpdate`: cifra y guarda los bytes escritos en `longitudPaso`.
4. `EVP_EncryptFinal_ex(ctx, textoEncriptado + longitudPaso, &longitudPaso)`: con aritmética de punteros agrega el bloque final con el relleno.

Descifrar: `EVP_DecryptInit_ex` con la **misma llave y el mismo IV**, `EVP_DecryptUpdate` y `EVP_DecryptFinal_ex`, que verifica y quita el relleno (si la llave o el texto se alteraron, no devuelve 1 y se llama a `manejarErrores()`). Se agrega `'\0'` para imprimir con `%s` y se libera con `EVP_CIPHER_CTX_free`.

Práctica guiada: `gcc -Wall cripto.c -o cripto -lcrypto`, `./cripto "Mensaje confidencial…"`, y comprobar que `llave.key` mide 32 bytes con `ls -l` y `hexdump -C`.
Error común: descifrar con otro IV u otra llave; abrir la llave en modo texto; olvidar `-lcrypto`.

## Pendiente / próxima clase
- Según la presentación, la siguiente sesión integra `cripto.c` y `llave.key` al cliente-servidor por TCP (Clase 21).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Puntos clave
- Texto plano = interceptación y modificación (X.800).
- AES-256: bloque de 16 B, llave de 32 B, 14 rondas; CBC con IV de 16 B; relleno PKCS#7.
- EVP: new → init → update → final; descifrar con la misma llave y el mismo IV.
- `RAND_bytes` y `llave.key` en `"wb"`; compilar con `-lcrypto`.

## Ponte a prueba
1. **¿Cuánto miden el bloque de AES, la llave de AES-256 y el IV?** 16 bytes, 32 bytes y 16 bytes.
2. **¿Qué hace el modo CBC?** Combina cada bloque con XOR con el bloque cifrado anterior (el primero con el IV) para eliminar patrones.
3. **¿Por qué se suma `EVP_MAX_BLOCK_LENGTH` al arreglo cifrado?** Por el relleno PKCS#7 del último bloque.
4. **¿Por qué la llave se escribe con `"wb"`?** Porque los bytes crudos pueden contener 0x00 o 0x0A, que el modo texto corrompería.
5. **¿Qué diferencia hay entre libssl y libcrypto?** libssl: protocolos TLS/DTLS; libcrypto: algoritmos, aleatorios y certificados.
6. **Ordena el ciclo de cifrado EVP.** CTX_new → EncryptInit_ex → EncryptUpdate → EncryptFinal_ex (→ CTX_free).
