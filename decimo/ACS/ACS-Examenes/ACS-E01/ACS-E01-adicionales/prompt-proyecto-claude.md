Vamos a resolver juntos el **examen parcial de Arquitectura Cliente-Servidor (semestre 2027-1, Ing. Carlos Román)**. Es un examen de casa, individual, y se entrega por correo a más tardar la **noche del lunes 19 de octubre de 2026**. Quiero entregar un código correcto y que **entienda cada línea**, porque es mi examen y tengo que poder explicarlo.

## Mi entorno
- Mac mini con Apple Silicon (macOS, compilo con `cc`/`clang` desde la Terminal). También tengo una computadora con Linux, por si algo solo funciona allá.
- Mi nombre, en el formato que pide el examen: **ORTEGA DE LA PAZ RAFAEL** (apellido paterno: ORTEGA; materno: DE LA PAZ; nombre: RAFAEL). *Ojo: el programa lo lee del teclado, no va fijo en el código.*

## Enunciado oficial (PDF que mandó el profesor; transcrito completo)
El examen parcial consiste en crear el par de programas Cliente-Servidor con base en el **par de programas 04** visto en clase (tema 3, sockets de Internet):
- Servidor: https://cromanzamitiz.github.io/arquitectura-cliente-servidor/tema3/programa04_servidor_internet.c
- Cliente: https://cromanzamitiz.github.io/arquitectura-cliente-servidor/tema3/programa04_cliente_internet.c

En el par original, una vez establecida la comunicación, el **servidor** envía un mensaje al cliente y ambos terminan.

**Actividades:**
1. Modificar el par para que, una vez establecida la comunicación, **el CLIENTE envíe un mensaje al SERVIDOR, el servidor le responda con un mensaje y ambos terminen**.
2. En el servidor, **el puerto se pasa desde la línea de comandos** (NO en código duro) y se usa **`htons()`**.
3. En el servidor, **capturar la IP desde la que se conecta el cliente**.
4. El mensaje del cliente es **mi nombre en formato APELLIDO_PATERNO APELLIDO_MATERNO NOMBRE(S)**, **leído desde el teclado**.
5. Para pruebas locales en la misma máquina, el cliente apunta a **127.0.0.1**.
6. **Captura 1 (prueba local):** las dos terminales **una al lado de la otra**, una con el cliente y otra con el servidor; **en la del servidor se imprime el nombre que recibió del cliente**.
7. **Prueba en producción:** lanzar mi cliente contra el servidor del profesor: **IP 132.248.59.6, puerto 4898**. Lo deja corriendo hasta la noche del lunes 19 de octubre.
8. **Captura 2:** después de que mi cliente termine, **en esa MISMA terminal** ejecutar `date` (para que queden la fecha y la hora) y capturar la pantalla.

**Entregable** (correo a **carlos.roman@ingenieria.unam.edu**):
1. Código fuente del cliente (`.c`). **No** mandar el ejecutable: el servidor de correo bloquea el mensaje.
2. Código fuente del servidor (`.c`). **No** mandar el ejecutable.
3. Captura de la prueba local (las dos terminales).
4. Captura del cliente apuntando a 132.248.59.6 con la salida de `date`.

## Lo que dijo el profesor en clase (Clases 14 y 15, según mis notas de NotebookLM)
- El examen «es muy parecido» a los programas 04 y 05 y a `compara_tiempos_buffers.c`. Del **Programa 05** sirve sobre todo cómo leer del teclado (`fgets` de `stdin`) y limpiar el buffer y el salto de línea.
- **Diferencia clave con el 04:** ahí escribía primero el servidor; en el examen **escribe primero el cliente**.
- El servidor remoto **registra IP, fecha, hora y nombre** de cada conexión. **Dos nombres distintos desde la misma IP se detectan como copia**, así que solo debo mandar mi nombre real, una vez y bien escrito.
- No hay parte teórica escrita: es solo código, pruebas y capturas.
- (Mis notas decían «puerto 4899» y «`date` antes del cliente»: **el PDF manda**, son **4898** y `date` **después**.)

## Código base del profesor (programa04, tal cual)
### programa04_servidor_internet.c
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>

#define PORT 4898

void main()
{
  struct sockaddr_in servidor;
  struct sockaddr_in cliente;
  struct hostent* info_cliente;
  int fd_s, fd_c;
  int longClient;
  char buf[128];

  printf( "1. Se llama a la funcion socket(...) y devuelve el file descriptor del servidor fd_s\n" );
  printf( "fd_s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);\n\n" );
  fd_s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	      
  printf( "2. Se inicializan los atributos de la variable struct sockaddr_in llamada servidor\n\n" );
  memset((char *) &servidor, 0, sizeof(servidor));
  servidor.sin_family = AF_INET;
  servidor.sin_addr.s_addr = INADDR_ANY;
  servidor.sin_port = htons((u_short) PORT);
  memset(&(servidor.sin_zero), '\0', 8);

  printf( "3. bind(fd_s, (struct sockaddr *) &servidor, sizeof(servidor));\n\n" );
  bind(fd_s, (struct sockaddr *) &servidor, sizeof(servidor));

  printf( "4. listen(fd_s, 1);\n\n" );
  listen(fd_s, 1);

  longClient = sizeof(cliente);

  printf( "5. La funcion accept() recibe como argumento el file descriptor del servidor y recibe tambien\n" );
  printf( "la struct sockaddr_in del cliente y devuelve el file descriptor del cliente\n" );
  printf( "fd_c = accept(fd_s, (struct sockaddr *) &cliente, &longClient);\n" );
  printf( "La funcion accept(...) se quedara ahi indefinidamente hasta que se conecte un cliente\n\n" );
  fd_c = accept(fd_s, (struct sockaddr *) &cliente, &longClient);

  printf( "6. Se llama a la funcion gethostbyaddr(...) para obtener la informacion\n" );
  printf( "propia del cliente y lo que devuelve la funcion, se asigna a la variable\n" );
  printf( "de tipo struct hostent* llamada info_cliente:\n" );
  printf( "info_cliente = gethostbyaddr((char *) &cliente.sin_addr, sizeof(struct in_addr), AF_INET);\n\n" );
  info_cliente = gethostbyaddr((char *) &cliente.sin_addr, sizeof(struct in_addr), AF_INET);

  printf( "7. Gracias a la sentencia anterior, por ejemplo, podemos saber el nombre del host cliente\n");
  printf( "info_cliente -> h_name\n" );
  printf("Conectado desde: %s\n\n", info_cliente -> h_name);

  printf( "8. Se le envia al cliente una frase \"El mensaje del servidor es: Conexion exitosa!\", con la funcion send(...)\n" );
  printf( "send(fd_c, buf, strlen(buf), 0);\n\n" );
  sprintf(buf, "El mensaje del servidor es: Conexion exitosa!\n");
  send(fd_c, buf, strlen(buf), 0);

  printf( "9. Se cierra el file descriptor del cliente\n" );
  printf( "close(fd_c);\n" );
  close(fd_c);

  printf( "10. Por ultimo, ahora si se cierra el file descriptor del servidor\n" );
  printf( "close(fd_s);\n" );
  close(fd_s);
  shutdown( fd_s, SHUT_RDWR );
  exit(0);
}
```
### programa04_cliente_internet.c
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>

void main(int argc, char *argv[])
{
  struct sockaddr_in socket_cliente;
  struct hostent *h;
  int fd;
  int n;
  char *host;
  char buf[128];

  printf( "1. Se llama a la funcion socket(...) y devuelve el file descriptor propio del cliente fd\n" );
  printf( "fd = socket(AF_INET, SOCK_STREAM, 0);\n" );
  fd = socket(AF_INET, SOCK_STREAM, 0);

  printf( "2. Se inicializan los atributos de la variable struct sockaddr_in llamada socket_cliente\n\n" );
  printf( "Pero se inicializan con datos del servidor, como son la IP y el puerto\n\n" );

  memset((char *) &socket_cliente, 0, sizeof(socket_cliente));
  socket_cliente.sin_family = AF_INET;
  socket_cliente.sin_port = htons((u_short) atoi(argv[2]) );
  h = gethostbyname( argv[1] );
  memcpy(&socket_cliente.sin_addr, h->h_addr, h->h_length);

  printf( "3. La funcion connect() es la que intenta conectarse al servidor\n" );
  printf( "Esta funcion se relaciona con la funcion accept(...) del servidor\n\n" );
  connect(fd, (struct sockaddr *) &socket_cliente, sizeof(socket_cliente));
    
  printf( "4. Como el servidor hace send(...) entonces el cliente hace recv(...)\n" );
  printf( "n = recv(fd, buf, sizeof(buf), 0);\n" );
  printf( "Lo recibido con recv(...) se va a imprimir a \"algun lado\" con la funcion write(...)\n" );
  printf( "write(1, buf, n);\n" );
  printf( "Revisa la documentacion de write(...), a donde manda el mensaje?\n\n" );
  n = recv(fd, buf, sizeof(buf), 0);
  printf("numero real de bytes leidos=%d\n",n);
  write(1, buf, n);
  printf( "\n" );

  printf( "5. Por ultimo, se cierra el file descriptor\n" );
  printf( "close(fd);\n" );
  close(fd);
  exit(0);
}
```

## Lo que te pido, en este orden
1. **Explícame primero el par original**: qué hace cada llamada (`socket`, `bind`, `listen`, `accept`, `gethostbyaddr`, `connect`, `send`, `recv`, `write`, `close`) y en qué orden se sincronizan cliente y servidor. Breve, pero que me quede claro.
2. **Escribe `examen_servidor.c` y `examen_cliente.c`** con **cambios mínimos sobre el 04**: que se note que salen de ahí, mismo estilo y comentarios/`printf` didácticos en español como los del profesor. Requisitos:
   - Servidor: `./examen_servidor <puerto>`, con `atoi(argv[1])` + `htons()`. Valida `argc` y muestra el modo de uso si falta el puerto.
   - Servidor: `accept` → **`recv` del nombre primero** → imprime **«Nombre recibido: …»** y **la IP del cliente** con `inet_ntoa(cliente.sin_addr)` (y el `h_name` de `gethostbyaddr` solo si no es NULL, para que no truene) → `send` de una respuesta (p. ej. «Servidor: registro recibido, <nombre>») → `close` de ambos descriptores.
   - Cliente: `./examen_cliente <ip> <puerto>`; valida `argc`; pide **«Escribe tu nombre (APELLIDO_PATERNO APELLIDO_MATERNO NOMBRE(S)):»**; lo lee con `fgets` y le quita el `\n`; **`send` primero** → `recv` de la respuesta → la imprime → `close`.
   - Revisa los valores de retorno de `socket`, `bind`, `listen`, `accept`, `connect`, `send` y `recv`, con `perror`, sin sobrecomplicar.
   - Usa `socklen_t` para la longitud del cliente y `int main` en lugar de `void main`, para que compile **sin warnings** en macOS (clang) y en Linux (gcc). Agrega `setsockopt(SO_REUSEADDR)` en el servidor para poder relanzarlo sin esperar a que se libere el puerto.
   - Termina con `\0` lo que llega por `recv` antes de imprimirlo como cadena.
3. **Señala cada cambio contra el 04** (una lista corta «antes → ahora») para que pueda explicarlo si me preguntan.
4. Dame los **comandos exactos** para:
   - compilar los dos programas (macOS y Linux);
   - la **prueba local**: terminal A `./examen_servidor 5000`, terminal B `./examen_cliente 127.0.0.1 5000`, y cómo poner las dos terminales lado a lado para la captura;
   - la **prueba remota**: `./examen_cliente 132.248.59.6 4898` y luego `date` **en la misma terminal**; qué debe verse en la captura.
5. Una **checklist final antes de mandar el correo**: los dos `.c` (sin binarios), las dos capturas, el nombre bien escrito, el puerto 4898 y el `date` después; más un **asunto y cuerpo de correo** breves y formales para el profesor (lo mando yo).
6. **Errores típicos y cómo resolverlos**: `Connection refused`, `Address already in use`, timeout si mi red bloquea el puerto, el nombre cortado por el tamaño del buffer o el `\n` sobrante.

No inventes requisitos que no estén arriba. Si algo del enunciado es ambiguo, dímelo y propón la interpretación más segura.
