#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>

/*
 * Examen parcial - Arquitectura Cliente-Servidor 2027-1
 * Cliente basado en programa04_cliente_internet.c
 * Alumno: ORTEGA DE LA PAZ RAFAEL
 *
 * Cambio principal respecto al 04: ahora el CLIENTE escribe primero.
 * Lee el nombre desde el teclado, lo envia con send(...),
 * recibe la respuesta del servidor con recv(...), la imprime y termina.
 *
 * Uso: ./examen_cliente <ip_servidor> <puerto>
 */

int main(int argc, char *argv[])
{
  struct sockaddr_in socket_cliente;
  struct hostent *h;
  int fd;
  int n;
  size_t len;
  char nombre[128];
  char buf[128];

  if (argc != 3) {
    printf( "Modo de uso: %s <ip_servidor> <puerto>\n", argv[0] );
    printf( "Ejemplo:     %s 127.0.0.1 5000\n", argv[0] );
    exit(1);
  }

  printf( "1. Se lee el nombre desde el teclado con fgets(...) (como en el programa 05)\n" );
  printf( "Primero se limpia el buffer con memset(...) y despues se quita el '\\n' del Enter\n\n" );
  printf( "Escribe tu nombre (APELLIDO_PATERNO APELLIDO_MATERNO NOMBRE(S)): " );
  fflush(stdout);
  memset(nombre, 0, sizeof(nombre));
  if (fgets(nombre, sizeof(nombre), stdin) == NULL) {
    printf( "\nNo se leyo ningun nombre\n" );
    exit(1);
  }
  len = strlen(nombre);
  if (len > 0 && nombre[len - 1] == '\n') {
    nombre[len - 1] = '\0';
    len--;
  }
  printf( "\n" );

  printf( "2. Se llama a la funcion socket(...) y devuelve el file descriptor propio del cliente fd\n" );
  printf( "fd = socket(AF_INET, SOCK_STREAM, 0);\n\n" );
  fd = socket(AF_INET, SOCK_STREAM, 0);
  if (fd == -1) {
    perror("socket");
    exit(1);
  }

  printf( "3. Se inicializan los atributos de la variable struct sockaddr_in llamada socket_cliente\n" );
  printf( "Pero se inicializan con datos del servidor, como son la IP y el puerto\n\n" );
  memset((char *) &socket_cliente, 0, sizeof(socket_cliente));
  socket_cliente.sin_family = AF_INET;
  socket_cliente.sin_port = htons((u_short) atoi(argv[2]) );
  h = gethostbyname( argv[1] );
  if (h == NULL) {
    printf( "No se pudo resolver el host %s\n", argv[1] );
    close(fd);
    exit(1);
  }
  memcpy(&socket_cliente.sin_addr, h->h_addr, h->h_length);

  printf( "4. La funcion connect() es la que intenta conectarse al servidor\n" );
  printf( "Esta funcion se relaciona con la funcion accept(...) del servidor\n\n" );
  if (connect(fd, (struct sockaddr *) &socket_cliente, sizeof(socket_cliente)) == -1) {
    perror("connect");
    close(fd);
    exit(1);
  }

  printf( "5. Ahora el CLIENTE escribe primero: envia su nombre con send(...)\n" );
  printf( "send(fd, nombre, strlen(nombre) + 1, 0);   (el +1 incluye el '\\0' final)\n\n" );
  if (send(fd, nombre, len + 1, 0) == -1) {
    perror("send");
    close(fd);
    exit(1);
  }

  printf( "6. Como el servidor ahora hace send(...), el cliente hace recv(...)\n" );
  printf( "n = recv(fd, buf, sizeof(buf) - 1, 0);\n\n" );
  memset(buf, 0, sizeof(buf));
  n = recv(fd, buf, sizeof(buf) - 1, 0);
  if (n == -1) {
    perror("recv");
    close(fd);
    exit(1);
  }
  buf[n] = '\0';   /* se termina la cadena antes de imprimirla */
  printf( "numero real de bytes leidos=%d\n", n );
  printf( "%s", buf );
  if (strlen(buf) == 0 || buf[strlen(buf) - 1] != '\n')
    printf( "\n" );

  printf( "7. Por ultimo, se cierra el file descriptor\n" );
  printf( "close(fd);\n" );
  close(fd);
  return 0;
}
