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
 * Servidor basado en programa04_servidor_internet.c
 * Alumno: ORTEGA DE LA PAZ RAFAEL
 *
 * Cambio principal respecto al 04: ahora el CLIENTE escribe primero.
 * El servidor recibe el nombre, lo imprime junto con la IP del cliente,
 * le responde con un mensaje y ambos terminan.
 *
 * Uso: ./examen_servidor <puerto>
 */

int main(int argc, char *argv[])
{
  struct sockaddr_in servidor;
  struct sockaddr_in cliente;
  struct hostent* info_cliente;
  int fd_s, fd_c;
  socklen_t longClient;
  int puerto;
  int opcion = 1;
  int n;
  char buf[128];
  char respuesta[256];

  /* El puerto ya no esta en codigo duro: se recibe desde la linea de comandos */
  if (argc != 2) {
    printf( "Modo de uso: %s <puerto>\n", argv[0] );
    printf( "Ejemplo:     %s 5000\n", argv[0] );
    exit(1);
  }
  puerto = atoi(argv[1]);
  if (puerto <= 0 || puerto > 65535) {
    printf( "Puerto invalido: %s (debe estar entre 1 y 65535)\n", argv[1] );
    exit(1);
  }

  printf( "1. Se llama a la funcion socket(...) y devuelve el file descriptor del servidor fd_s\n" );
  printf( "fd_s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);\n\n" );
  fd_s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
  if (fd_s == -1) {
    perror("socket");
    exit(1);
  }

  printf( "1.1 Con setsockopt(...SO_REUSEADDR...) se permite relanzar el servidor\n" );
  printf( "sin esperar a que el sistema operativo libere el puerto\n\n" );
  if (setsockopt(fd_s, SOL_SOCKET, SO_REUSEADDR, &opcion, sizeof(opcion)) == -1) {
    perror("setsockopt");
    close(fd_s);
    exit(1);
  }

  printf( "2. Se inicializan los atributos de la variable struct sockaddr_in llamada servidor\n" );
  printf( "El puerto se toma de argv[1] y se convierte al orden de red con htons()\n" );
  printf( "servidor.sin_port = htons((u_short) puerto);   puerto = %d\n\n", puerto );
  memset((char *) &servidor, 0, sizeof(servidor));
  servidor.sin_family = AF_INET;
  servidor.sin_addr.s_addr = INADDR_ANY;
  servidor.sin_port = htons((u_short) puerto);
  memset(&(servidor.sin_zero), '\0', 8);

  printf( "3. bind(fd_s, (struct sockaddr *) &servidor, sizeof(servidor));\n\n" );
  if (bind(fd_s, (struct sockaddr *) &servidor, sizeof(servidor)) == -1) {
    perror("bind");
    close(fd_s);
    exit(1);
  }

  printf( "4. listen(fd_s, 1);\n\n" );
  if (listen(fd_s, 1) == -1) {
    perror("listen");
    close(fd_s);
    exit(1);
  }

  longClient = sizeof(cliente);

  printf( "5. La funcion accept() recibe como argumento el file descriptor del servidor y recibe tambien\n" );
  printf( "la struct sockaddr_in del cliente y devuelve el file descriptor del cliente\n" );
  printf( "fd_c = accept(fd_s, (struct sockaddr *) &cliente, &longClient);\n" );
  printf( "La funcion accept(...) se quedara ahi indefinidamente hasta que se conecte un cliente\n\n" );
  fd_c = accept(fd_s, (struct sockaddr *) &cliente, &longClient);
  if (fd_c == -1) {
    perror("accept");
    close(fd_s);
    exit(1);
  }

  printf( "6. Se captura la IP desde la que se conecta el cliente.\n" );
  printf( "accept(...) la dejo guardada en cliente.sin_addr; inet_ntoa(...) la convierte a texto\n" );
  printf( "IP del cliente: %s\n\n", inet_ntoa(cliente.sin_addr) );

  printf( "7. Se llama a la funcion gethostbyaddr(...) para obtener el nombre del host cliente\n" );
  printf( "info_cliente = gethostbyaddr((char *) &cliente.sin_addr, sizeof(struct in_addr), AF_INET);\n" );
  info_cliente = gethostbyaddr((char *) &cliente.sin_addr, sizeof(struct in_addr), AF_INET);
  if (info_cliente != NULL)
    printf( "Conectado desde: %s\n\n", info_cliente -> h_name );
  else
    printf( "gethostbyaddr(...) no pudo resolver el nombre del host (devolvio NULL); ya tenemos la IP\n\n" );

  printf( "8. Ahora el CLIENTE escribe primero, asi que el servidor hace recv(...)\n" );
  printf( "n = recv(fd_c, buf, sizeof(buf) - 1, 0);\n\n" );
  memset(buf, 0, sizeof(buf));
  n = recv(fd_c, buf, sizeof(buf) - 1, 0);
  if (n == -1) {
    perror("recv");
    close(fd_c);
    close(fd_s);
    exit(1);
  }
  buf[n] = '\0';   /* se termina la cadena antes de imprimirla */
  printf( "Nombre recibido: %s\n\n", buf );

  printf( "9. El servidor le responde al cliente con la funcion send(...)\n" );
  printf( "send(fd_c, respuesta, strlen(respuesta), 0);\n\n" );
  snprintf(respuesta, sizeof(respuesta), "Servidor: registro recibido, %s\n", buf);
  if (send(fd_c, respuesta, strlen(respuesta), 0) == -1)
    perror("send");

  printf( "10. Se cierra el file descriptor del cliente\n" );
  printf( "close(fd_c);\n" );
  close(fd_c);

  printf( "11. Por ultimo, ahora si se cierra el file descriptor del servidor\n" );
  printf( "close(fd_s);\n" );
  close(fd_s);
  return 0;
}
