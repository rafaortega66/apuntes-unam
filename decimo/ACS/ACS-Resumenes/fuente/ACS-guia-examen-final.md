# **ACS · Guía para el examen final**

**Arquitectura Cliente-Servidor** · Semestre 2027-1 · 16 nov 2026  
*Hecha con NotebookLM a partir de todas las fuentes del cuaderno de la materia (audios de cada clase y material del profesor): hilo conductor del curso, unidades con sus conceptos explicados, lo que más probablemente viene y las conexiones entre conceptos. Acompáñala con el mapa mental (ACS-mapa-mental.pdf, en esta misma carpeta).*  
*Clases que no estaban en el cuaderno: 5, 19, 20\. Su resumen va en el Anexo al final.*

## ***Nota sobre las fuentes consultadas: esta guía integra únicamente el contenido de las 20 clases disponibles en el cuaderno (*** ***ACS-Clase1.m4a* *a* *ACS-Clase4.m4a* *,* *ACS-Clase6.m4a* *a* *ACS-Clase18.m4a* *y* *ACS-Clase21.m4a* *a* *ACS-Clase23.m4a* *) y los fragmentos de presentaciones y código que el profesor mostró y leyó en ellas. No existen archivos PDF independientes adjuntos ni grabaciones de las Clases 5, 19 y 20 en el cuaderno, por lo que cualquier detalle exclusivo de esas tres sesiones (como el enunciado completo de la Tarea 5 o la revisión de* *desencriptador.c* *si ocurrió allí) no figura en las fuentes.***

## **HILO CONDUCTOR**

La materia parte de una idea central: antes de construir aplicaciones distribuidas en red, hay que entender qué es un proceso vivo dentro del sistema operativo Linux, cómo se organiza su memoria, con qué privilegios se ejecuta y cómo nace, se comunica o muere. Por eso el curso arranca estudiando la imagen de un proceso, sus segmentos en memoria y el control de permisos e identificadores de usuario (UID/eUID), para luego dominar el ciclo de vida de los procesos mediante llamadas al sistema (fork(), exec(), kill()) y señales (signal()), descubriendo el riesgo de bloqueos mutuos (*deadlock*), procesos huérfanos y procesos zombie. Con esa base de sistemas operativos dominada, el curso da el salto a la red definiendo la arquitectura cliente-servidor como procesos de software que dialogan a través de **sockets** (tratados en Unix/Linux como descriptores de archivo) usando direcciones IP y puertos lógicos.

## **A partir de ahí, el desarrollo avanza por capas incrementales de complejidad hasta culminar en una aplicación distribuida segura: primero se construye el flujo básico en C (socket–bind–listen–accept–connect–send/recv), luego se destripa el saludo de tres vías TCP, la cola de espera del kernel, los puertos efímeros y la fragmentación por tamaños de búfer. Después se resuelve la escalabilidad pasando de un servidor secuencial (uno a la vez) a servidores concurrentes con fork() y, al chocar con la memoria aislada de los hijos, a la multiplexación en un solo proceso con select() para chats grupales. Finalmente, al demostrar con un *sniffer* de capa 2 (SOCK\_RAW) que todo el texto y los archivos viajan expuestos en texto plano por la red, se introduce la criptografía simétrica con OpenSSL (AES-256-CBC y relleno PKCS) y la transferencia completa de directorios y archivos binarios, mostrando cómo los mismos módulos técnicos que permiten construir un FTP encriptado explican también el funcionamiento real de ataques como el *ransomware* y el DDoS.**

## **UNIDAD 1: LINUX, ANATOMÍA DE UN PROCESO, PERMISOS Y MANEJO DE ERRORES**

### **(a) Qué problema resuelve y cómo se conecta con el curso**

Un cliente y un servidor en C son **procesos de software en ejecución**. Antes de abrir conexiones de red, es indispensable comprender cómo el kernel asigna memoria a un ejecutable, cómo lo identifica y aísla, bajo qué usuario corre (privilegios) y cómo reporta errores de sistema cuando una llamada falla.

### **(b) Conceptos clave**

> * **Proceso e Imagen de un Proceso (Clase 1\)**  
  * **Definición:** Un proceso es un programa ejecutable en ejecución que permanece vivo mientras corre y muere al terminar. La imagen de un proceso es la fotografía o instantánea de la zona de memoria independiente (espacio de direcciones) que el sistema carga para ese binario en tiempo de ejecución, diferenciada del contexto del kernel o Bloque de Control de Procesos (PCB / BCP).  
  * **Analogía:** Es como la diferencia entre una receta impresa en un libro (el archivo ejecutable en disco) y la cocina activa con los ingredientes sobre la mesa mientras se prepara el platillo (la imagen del proceso en RAM).  
  * **Ejemplo de clase:** Al ejecutar el servidor sencillo en C pausado con getchar() en una terminal, se inspeccionó su memoria desde otra terminal antes de presionar Enter y liberar la memoria (PID observado en vivo: 14478).  
> * **Segmentos de la memoria del proceso: Text , Data , BSS , Heap y Stack (Clase 1\)**  
  * **Definición:** División lógica de la memoria del proceso en áreas estáticas y dinámicas. Text contiene el código ejecutable y literales de cadena (como los textos de printf); Data almacena variables globales inicializadas; BSS (*Block Started by Symbol*) guarda variables globales no inicializadas; Heap (montículo) gestiona memoria asignada dinámicamente en ejecución (con malloc); y Stack (pila) guarda variables locales cuyo alcance (*scope*) se limita a una función.  
  * **Analogía:** Una mochila con compartimentos fijos para las instrucciones y datos de partida (Text, Data, BSS) y dos bolsas expansibles que crecen en direcciones opuestas conforme se necesitan (Heap y Stack).  
  * **Ejemplo de clase:** El comando size mostró únicamente los tamaños en bytes de los segmentos estáticos (text 1767, data 592, bss 8, más sus sumas dec y hex), mientras que pmap \<PID\> consultó al kernel para mostrar las zonas dinámicas en múltiplos de páginas de memoria de 4 KB (4096 bytes), verificando que Heap y Stack carecen de permisos de ejecución para evitar inyección de código malicioso.  
> * **Árbol de procesos, PID/PPID, Tiempo Compartido y Demonios (Clase 1\)**  
  * **Definición:** Todo proceso tiene un identificador propio único (PID) y el identificador de su proceso padre (PPID). El proceso raíz del sistema tiene PID 1 (init en sistemas antiguos, systemd en distribuciones modernas). Linux es un sistema de tiempo compartido donde el planificador alterna turnos de CPU entre procesos. Los procesos sin terminal interactiva que corren en segundo plano se denominan *daemons* o demonios (suelen terminar en d, como systemd o watchdogd, y muestran ? en la columna TTY).  
  * **Analogía:** Un árbol genealógico donde cada persona tiene su acta propia y el número de acta de su padre, atendidos por turnos rápidos en una misma ventanilla.  
  * **Ejemplo de clase:** Con ps \-e \-o pid,ppid,user,stat,cmd (sin espacios tras las comas), el comando ps tuvo PID 14680 y PPID 14456, comprobándose que 14456 era el PID de la terminal bash que lo lanzó. El comando ls \-ltr ordena archivos por fecha en orden inverso dejando el más reciente pegado al *prompt*.  
> * **Permisos UGO, chmod octal, Bit SetUID y /etc/passwd vs /etc/shadow (Clases 2, 3\)**  
  * **Definición:** El modelo UGO asigna permisos en tres ternas: Usuario dueño (U), Grupo (G) y Otros (O), sumando lectura (4), escritura (2) y ejecución (1). El archivo /etc/passwd almacena usuarios del sistema separados por : (username:x:UID:GID:nombre:home:shell, usando /sbin/nologin en cuentas de sistema que no deben iniciar sesión), mientras /etc/shadow resguarda datos ocultos/de sistema cuando no aparecen en /etc/passwd. Un proceso posee un ID real (getuid()) del dueño en /etc/passwd y un ID efectivo (geteuid()) del usuario con cuyos privilegios corre. Al activar el **bit SetUID** con un cuarto dígito 4 a la izquierda en chmod (ej. 4511), cualquier usuario que ejecute el binario asume temporalmente el ID efectivo del dueño durante la ejecución.  
  * **Analogía:** Una credencial temporal de contratista que te da acceso de administrador únicamente mientras estás dentro de la sala de servidores realizando un trámite; al salir vuelves a ser visitante.  
  * **Ejemplo de clase (Tarea 2):** Con programa\_02\_ids.c corriendo como usuario codespace (UID 1000), getuid() y geteuid() devolvieron 1000 y 1000\. Tras cambiar el dueño a root:root con chown, aplicar chmod 700 arrojó *permiso denegado*. Al aplicar chmod 4511 (r-s--x--x, sombreado en rojo), el usuario codespace ejecutó el binario y obtuvo **Usuario Real 1000 y Usuario Efectivo 0 ( root )**. También se probó chmod 2511 (SetGID, cambia el grupo efectivo) y chmod 1511 (pone una T en otros sin efecto apreciable en getuid/getgid).  
> * **Códigos de error del sistema ( errno ), strerror() y perror() (Clases 3, 4\)**  
  * **Definición:** Variable global del sistema errno (no requiere declararse) que guarda el entero del último error ocurrido. El código 0 representa **éxito** (*Success*), mientras que de 1 en adelante representan errores estándar (como 2 / ENOENT: *No such file or directory*, EPERM, EIO). strerror(int) devuelve la cadena de texto descriptiva de un código, y perror("texto") imprime la cadena personalizada seguida de : y el mensaje de sistema del error.  
  * **Ejemplo de clase:** Con programa\_03\_codigos\_sistema.c iterando i de 0 a 150, el sitio web listaba 131 códigos, pero el Linux ejecutado en clase llegó hasta el 133 (con el 41 reservado/sin mensaje) y a partir del 134 imprimió Unknown error.

### **(c) Comparaciones y comandos clave (Unidad 1\)**

| Elemento / Comando | Función / Comportamiento | Detalles clave de clase   |
| :---- | :---- | :---- |
| size \<ejecutable\> | Análisis estático del binario. | Muestra text, data, bss, suma dec y hex; omite Heap y Stack. |
| pmap \<PID\> | Mapa dinámico desde el kernel. | Múltiplos de páginas de 4 KB; segmentos dinámicos sin permiso x. |
| top vs ps | Monitoreo en vivo vs instantánea. | top es dinámico (sale con q); ps es estático (ps, ps aux, ps \-e \-o ...). |
| chmod 644 vs 755 vs 4511 | Permisos UGO octales y SetUID. | 644: editable no ejecutable; 755: ejecutable normal; 4511: r-s--x--x (SetUID). |
| strerror(code) vs perror(msg) | Reporte de errores en C. | strerror traduce cualquier código entero a string; perror antepone msg: al error actual de errno. |

### **(d) Errores comunes y puntos recalcados para examen (Unidad 1\)**

> * Olvidar que para ejecutar un binario se requiere también permiso de lectura (5 \= 4 \+ 1), no solo 1\.  
> * Dejar activado el bit SetUID (4511) en binarios de root representa un grave riesgo de seguridad; en la Tarea 2 debía restaurarse a 755 al terminar.  
> * Colocar espacios después de las comas en ps \-e \-o pid,ppid,user,stat,cmd provoca error de sintaxis.  
> * Asumir que el número máximo de códigos de error es fijo (131 vs 133 según la distribución Linux).

## ---

**UNIDAD 2: CICLO DE VIDA, SINCRONIZACIÓN, SEÑALES Y PROCESOS ESPECIALES**

### **(a) Qué problema resuelve y cómo se conecta con el tema anterior**

Una vez entendida la imagen de un proceso aislado, un servidor de red necesita crear múltiples procesos para atender clientes en paralelo, reemplazar ejecutables, controlar cuándo y cómo terminan los hijos y evitar que dejen basura en la tabla de procesos del sistema.

### **(b) Conceptos clave**

> * **Creación de procesos con fork() , Condición de Carrera y Deadlock (Clases 2, 4\)**  
  * **Definición:** fork() clona el proceso invocante creando un hijo idéntico en código y variables, excepto en su PID, su PPID y el valor de retorno de fork() (de tipo pid\_t): al **padre** le devuelve el PID del hijo (\> 0), al **hijo** le devuelve 0, y en caso de error devuelve \-1. Ambos corren asíncronamente creando una **condición de carrera** (*race condition*); si el padre espera al hijo y el hijo espera al padre, ocurre un **bloqueo o abrazo mortal** (*deadlock*).  
  * **Analogía:** Una máquina fotocopiadora instantánea que duplica a un trabajador con su hoja de instrucciones; a cada uno le entrega un gafete distinto (0 al clon, número del clon al original) para que un if/else los mande por pasillos diferentes.  
  * **Ejemplo de clase:** En programa05\_fork\_v2.c, el padre tuvo PID 30405, el hijo 30406, el PPID del hijo fue 30405 y el PPID del padre fue el de la terminal bash. En programa\_08 (3 caminos: \-1, 0, \>0), se observó el caso en que el padre terminó antes que el hijo.  
> * **Proceso Huérfano y Subprocesos Reaper (Clase 4\)**  
  * **Definición:** Ocurre cuando el proceso padre termina o muere antes que el proceso hijo, dejando al hijo vivo sin padre. Como Linux no permite procesos huérfanos, el proceso con PID 1 (init/systemd) —o en distribuciones modernas un subproceso recogedor (*reaper*) dedicado a aliviar la carga del PID 1— lo adopta de inmediato.  
  * **Ejemplo de clase:** Al ejecutar programa\_08, en lugar de imprimir el PID del padre, getppid() del hijo imprimió 1 (y en la máquina Fedora moderna de un alumno imprimió otro PID perteneciente a un *reaper*).  
> * **Familia de funciones exec() (Clase 4\)**  
  * **Definición:** Familia de 6 funciones (execl, execv, execle, execve, execlp, execvp) que reemplazan la imagen completa del proceso actual por la de un nuevo ejecutable. A diferencia de fork(), no crea un proceso paralelo: si tiene éxito, el proceso original muere y solo queda el nuevo.  
  * **Analogía:** Un actor en escena que, al leer la palabra mágica, desaparece instantáneamente y en su misma silla aparece otra persona con otro libreto.  
  * **Ejemplo de clase ( programa\_10 ):** execl("/bin/ls", "/bin/ls", "-l", "/", NULL) repitió /bin/ls porque el primer argumento es la ruta absoluta (PATH) y el segundo es argv (el nombre del ejecutable), cerrando la lista con NULL. Al cambiarlo intencionalmente a /bin/lsa, falló devolviendo \-1 y perror("exec") imprimió No such file or directory; si no se pone exit(EXIT\_FAILURE) dentro del if, el código posterior ("esto no se imprime") termina ejecutándose erróneamente.  
> * **Señales, signal() , kill() y modos Foreground/Background (Clases 6, 7\)**  
  * **Definición:** Notificaciones asíncronas enviadas a un proceso (man 7 signal). Ante una señal hay tres escenarios: (1) **Ignorarla** (SIG\_IGN, programa\_04), (2) **Capturarla/Tratarla** con una función void handler(int sig) que lo deje vivo (programa\_05\_v1 con variable static) o lo termine con exit(0) tras N veces (programa\_05\_v2), o (3) **Señal imparable** (SIGKILL / 9 y SIGSTOP) que no puede ignorarse ni capturarse (programa\_06). Para detener un proceso en primer plano (*foreground*) se usa Ctrl+Z (SIGTSTP, 20), con bg pasa a segundo plano (*background*), jobs lista trabajos,, y fg \<num\> lo regresa a primer plano para poder matarlo con Ctrl+C (SIGINT, 2). En C, kill(pid, señal) envía señales programáticamente (programa\_11: el padre duerme 10 s mientras el hijo imprime cada 1 s y luego lo mata con SIGKILL).  
> * **Proceso Zombie ( Z+ / ) y soluciones (Clase 7\)**  
  * **Definición:** Proceso hijo que ya terminó de ejecutarse (exit(0)) y envió la señal SIGCHLD (17 en x86/ARM) a su padre, pero permanece en la tabla de procesos en un estado entre vivo y muerto porque el padre está ocupado (ej. dormido) y no ha recogido ni limpiado la señal de la cola.  
  * **Analogía:** Un empleado que ya terminó su turno y dejó su reporte de salida en la puerta, pero como el jefe está dormido, su ficha sigue marcada como pendiente en recepción.  
  * **Ejemplo de clase ( programa\_08 zombie):** El padre duerme 60 s y el hijo termina al instante; ps muestra al padre en S+ (*sleeping*) y al hijo en Z+ con \<defunct\> durante ese minuto hasta que el padre despierta y limpia la señal. El estatus X (muerto) existe en man ps pero jamás debe verse en salida. Soluciones en programa\_09: ignorar SIGCHLD con SIG\_IGN (como dejar pasar la pelota en béisbol) o implementar un manejador para SIGCHLD.

### **(c) Tablas comparativas (Unidad 2\)**

| Letra en exec\* | Significado | Forma de paso / Búsqueda   |
| :---- | :---- | :---- |
| l (execl, execle, execlp) | *List* | Argumentos individuales terminados en NULL. |
| v (execv, execve, execvp) | *Vector* | Arreglo de cadenas (char \*\[\]) terminado en NULL. |
| e (execle, execve) | *Environment* | Recibe arreglo de variables de entorno para esa ejecución. |
| p (execlp, execvp) | *PATH* | Busca el ejecutable por nombre en la variable PATH (no requiere ruta absoluta). |

| Señal clave | Número (x86/ARM) | ¿Se puede ignorar/tratar? | Origen o función principal   |
| :---- | :---- | :---- | :---- |
| SIGHUP | 1 | Sí | Colgado / recarga. |
| SIGINT | 2 | Sí (SIG\_IGN / handler) | Ctrl+C desde terminal. |
| SIGABRT | 6 | Sí (abort()) | El proceso se aborta a sí mismo. |
| SIGKILL | 9 | **NO** (siempre mata) | Equivalente al conjuro fulminante (kill \-9). |
| SIGTERM | 15 | Sí | Apagado ordenado del sistema (*shutdown* ). |
| SIGCHLD / SIGCLD | 17 (18 en otras arch.) | Sí (SIG\_IGN / handler) | Hijo avisa al padre que va a morir; si no se recoge, genera **zombie** . |
| SIGTSTP | 20 | Sí | Ctrl+Z (detener terminal, no mata). |

### **(d) Errores comunes y puntos recalcados para examen (Unidad 2\)**

> * Al usar kill entre distintas arquitecturas, usar el nombre de la macro (ej. \-SIGKILL o \-SIGBUS) porque los números pueden variar (SIGBUS es 7 en x86 y 10 en otras).  
> * Olvidar que sleep(5) en C recibe **segundos** (no milisegundos como en Java).  
> * No encerrar execl() en if (execl(...) \== \-1) con exit(EXIT\_FAILURE): si el comando está mal escrito, el código siguiente al execl() se ejecutará.  
> * Intentar matar con Ctrl+C un proceso que está en *background*: primero debe traerse a *foreground* con fg \<num\> (o enviar kill \-9 \<PID\>).

## ---

**UNIDAD 3: FUNDAMENTOS DE REDES Y SOCKETS TCP EN C (TEMA 3\)**

### **(a) Qué problema resuelve y cómo se conecta con el tema anterior**

Los procesos ya saben nacer y enviarse señales dentro de una misma máquina, pero en la realidad las aplicaciones (WhatsApp, Netflix, bancos) son procesos corriendo en computadoras distintas separadas por redes. Los **sockets** permiten comunicar esos procesos a través de la red reutilizando el mismo concepto Unix de descriptores de archivo.

### **(b) Conceptos clave**

> * *Arquitectura Cliente-Servidor, Socket, Descriptores y Familias AF\_ (Clases 7, 8\)*\*  
  * **Definición:** Modelo que divide tareas en **Cliente** (software que solicita un servicio con IP/dominio y puerto del servidor) y **Servidor** (software que provee el servicio). Un **socket** es cada extremo del canal de comunicación entre procesos y se maneja como un descriptor de archivo. Como 0 (entrada estándar/teclado), 1 (salida estándar/monitor) y 2 (error estándar/monitor, con prioridad de salida) están reservados, el primer socket abierto recibe el descriptor 3, el siguiente 4, etc..  
  * **Analogía:** El socket es como el casquillo donde enroscas el foco en casa, pero en lugar de foco enroscas un proceso.  
  * **Familias de socket:** AF\_INET (IPv4 de 4 bytes / 4 octetos de 0 a 255), AF\_INET6 (IPv6), AF\_UNIX (procesos en la misma máquina usando archivos del sistema, como MySQL/PostgreSQL por defecto), AF\_NETLINK (kernel-usuario), AF\_BLUETOOTH y AF\_PACKET (tramas crudas en capa 2 para *sniffers*).  
> * **Puertos lógicos, IANA y Tipos de Socket (Clases 7, 8, 9\)**  
  * **Definición:** Un puerto lógico es un identificador de 16 bits (216\=65,536 puertos, del 0 al 65,535). La **IANA** (*Internet Assigned Numbers Authority*) clasifica los primeros 1024 puertos (0–1023) como reservados para el administrador (root: SSH 22, correo 25, HTTP 80, HTTPS 443, MySQL 3306), y de 1024 a 65,535 para programas de usuario (como 4898 o 8080 de Apache/Tomcat). Tipos de socket: SOCK\_STREAM (TCP, capa 4, fiable y ordenado: ABC llega ABC) vs SOCK\_DGRAM (UDP, no confiable).  
> * **Estructuras sockaddr\_in , hostent , DNS Round-Robin y Conversiones (Clases 8, 9, 10, 11, 13\)**  
  * **struct sockaddr\_in :** Tiene 4 atributos (sin\_ \= *socket internet*): sin\_family (AF\_INET o su equivalente PF\_INET), sin\_port (puerto convertido de decimal a binario de red con htons() \= *Host To Network Short*), sin\_addr.s\_addr (IP binaria; en el servidor suele usarse INADDR\_ANY para escuchar por todas sus interfaces de red, incluida 127.0.0.1 loopback), y sin\_zero (8 ceros '\\0' con memset, opcional en Linux moderno).  
  * **struct hostent y DNS:** gethostbyname() consulta el DNS y devuelve struct hostent \* (o NULL si falla), con h\_name y h\_addr\_list (donde h\_addr es h\_addr\_list). En clase, consultar www\.google.com devolvió 8 IPs rotando por **DNS round-robin** (alta disponibilidad), mientras google.com devolvió 1 IP.  
  * **Conversiones de IP:** Donde aparece **n** (*network*) es binario de máquina; **a** (*ASCII/address*) o **p** (*presentation*) es texto legible por humanos. Así: inet\_aton() / inet\_addr() (texto → binario), inet\_ntoa() y inet\_ntop() (binario → texto). En clase se desmenuzó de adentro hacia afuera inet\_ntoa(\*(struct in\_addr \*)H-\>h\_addr\_list).  
> * **Ciclo completo de funciones Socket y doble socket del Servidor (Clases 9, 10, 11, 12, 13, 17\)**  
  * **Lado Servidor (2 estructuras sockaddr\_in y 2 descriptores):** 1\. socket(AF\_INET, SOCK\_STREAM, 0\) (o IPPROTO\_TCP): crea el socket y devuelve fd\_s (3). 1\. setsockopt(fd\_s, SOL\_SOCKET, SO\_REUSEADDR, &(int){1}, sizeof(int)): permite reusar el puerto inmediatamente aunque esté en estado TIME\_WAIT tras matar el servidor con Ctrl+C, evitando *"Address already in use"*. 1\. Inicializar con memset la estructura servidor. 1\. bind(fd\_s, (struct sockaddr \*)\&servidor, sizeof(servidor)): liga/nombra el socket con IP y puerto. 1\. listen(fd\_s, backlog): pone al servidor en escucha y define la cola de espera. 1\. accept(fd\_s, (struct sockaddr \*)\&cliente, \&long\_cliente): bloquea esperando un cliente, inicializa automáticamente la estructura cliente y devuelve el segundo descriptor **fdc** (4) para comunicarse. El servidor usa fd\_s para aceptar y fd\_c para send/recv, requiriendo dos close() (close(fd\_c) y close(fd\_s)).  
  * **Lado Cliente (1 estructura sockaddr\_in y 1 descriptor fd ):** socket() → inicializa servidor con IP (memcpy o inet\_addr) y puerto (htons) → connect() (devuelve 0 o \-1, por lo que puede meterse en un while con sleep() para reintentar) → send/recv → close(fd).  
  * **Intercambio síncrono y truncado de búferes:** Se deben emparejar send()/recv() o write()/read() sin mezclarlos. recv() devuelve n (bytes reales leídos); para imprimir exacto en pantalla se usa write(1, buff, n). En el chat secuencial (programa\_05), do-while limpia el búfer en cada ciclo con memset, trunca el salto de línea (buff\[n-1\] \= '\\0') y termina con "adiós" enviando el servidor una respuesta automática.  
> * **Saludo de 3 vías TCP, Doble Cola ( SYN y Accept ), sk\_acceptq\_is\_full() y Puertos Efímeros (Clases 12, 13, 18\)**  
  * **Definición:** Cuando el cliente llama connect(), ocurre el *Three-Way Handshake*: (1) cliente manda SYN (estado SYN\_SENT), (2) servidor responde SYN+ACK (SYN\_RECV) y mete la petición en la **cola SYN**, (3) cliente responde ACK (ESTABLISHED) y el servidor mueve la conexión a la **cola Accept** definida por backlog en listen().  
  * **Regla backlog \+ 1 :** La función del kernel sk\_acceptq\_is\_full() compara con \> en vez de \>= (1 \> 1 es falso), por lo que la cola acepta **backlog \+ 1** conexiones en espera (ej. con backlog \= 1 atiende a 1, encola 2 y rechaza hasta el cliente 4).  
  * **Puertos Efímeros y NAT (Tarea 4 y Clase 17/18):** Cuando varios clientes detrás de una misma IP pública (ej. PC Puma 132.247.100.226, bloque /16 \= 216\=65,536 nodos) salen al mismo servidor 132.248.59.6:4898, el SO asigna a cada cliente una puerta de salida temporal distinta llamada **puerto efímero** (observados en vivo con watch \-n1 "ss \-atnp": 49802, 48469, 49808, 46740, 49210, 51448).  
> * **Fragmentación TCP, Búferes y Servidor HTTP/PDF (Clases 14, 15\)**  
  * **Definición:** TCP no garantiza entregar mensajes grandes en una sola lectura; los segmenta según el búfer del kernel (/proc/sys/net/core/rmem\_default y rmem\_max \= 212,992), la latencia y los bytes enviados. Solución: leer en bucle while ((n \= read(...)) \> 0).  
  * **Ejemplo en vivo ( compara\_tiempos\_buffers.c ):** Consultando www\.google.com:80 con tamaños 1024, 4096 (teóricamente óptimo por ser 1 página de memoria), 8192, 16384 y 100000, en la práctica 8 KB, 16 KB y 100 KB fueron más rápidos (0.0011 s y 0.0004 s vs 0.0013 s de 4 KB), variando ligeramente los bytes recibidos (90,442, 90,378, 90,246) por diferencias dinámicas en las cabeceras HTTP.  
  * **programa\_08\_servidor\_pdf.c :** Despacha holamundo.pdf enviando cabeceras HTTP (200 OK, Content-Type: application/pdf vs 404 text/plain), usando recv(..., MSG\_DONTWAIT) para descartar las cabeceras del navegador sin bloquear clientes que no envían HTTP, y enviando bloques de 8192 bytes restando los bytes enviados de los restantes (left) con aritmética de punteros.  
> * **Evolución de Servidores: Secuencial ( 05 ) vs Concurrente fork() ( 06 ) vs Multiplexado select() ( 07 ) (Clases 16, 17, 18\)**  
  * **Servidor Concurrente ( programa\_06 ):** Tras accept(), llama a fork(). El **hijo** (if (pid \== 0)) declara localmente sus búferes para ahorrar RAM en el padre, ejecuta **close(fds)** (no acepta clientes), atiende al cliente y al terminar cierra fd\_c y muere; el **padre** (else) ejecuta **close(fdc)** (no conversa con clientes) y regresa al while(1) a accept(). Registra conexión usando time(), localtime() y struct tm (tm\_mon \+ 1, tm\_year \+ 1900). Limitación: los hijos tienen **memorias separadas** y no pueden reenviarse mensajes para un chat grupal.  
  * **Multiplexación con select() ( programa\_07\_servidor\_grupal.c ):** Un único proceso vigila múltiples descriptores en un arreglo client\_socket\[\] usando el conjunto fd\_set y 4 macros: FD\_ZERO (vacía el conjunto), FD\_SET (agrega un fd), FD\_CLR (elimina un fd) y FD\_ISSET (verifica actividad). select(max\_fd \+ 1, \&readfds, writefds, errorfds, timeout) bloquea sin consumir CPU hasta que algún descriptor esté listo. Si hay actividad en master\_socket, acepta y guarda al cliente; si es en un cliente y read() devuelve 0 (Ctrl+C en nc \-v), imprime desconexión y limpia su ranura; si trae texto, usa getpeername() \+ inet\_ntop() y hace **broadcast** a todos los demás clientes excepto al remitente.  
> * **Sockets Crudos ( SOCK\_RAW / AF\_PACKET ), Sniffer y Niveles de Seguridad (Clase 18\)**  
  * **Definición:** Sockets de capa 2 (socket(AF\_PACKET, SOCK\_RAW, htons(ETH\_P\_ALL))) que entregan tramas Ethernet y segmentos TCP completos sin que el kernel los procese. Requieren privilegios de superusuario (sudo/root) y colocar la tarjeta de red en **modo promiscuo** (los 3 modos de tarjeta son: *default*, *promiscuo* y *monitor* para Wi-Fi; no confundir con las "4 P's" de seguridad en redes: Paranoico, Prohibitivo, Permissivo y Promiscuo). Permite ataques *Man-in-the-Middle* para reconstruir texto plano o PDFs interceptados.

### **(c) Comparación de arquitecturas de servidor (Unidad 3\)**

| Programa | Modelo | Manejo de accept() y procesos | Comunicación entre clientes | Límite / Desventaja   |
| :---- | :---- | :---- | :---- | :---- |
| programa\_04 | Único cliente | Acepta 1 cliente, envía frase fija, cierra todo. | Nula. | Muere tras 1 cliente. |
| programa\_05 | Secuencial | while(1) con accept() y do-while interno. | Nula. | Bloquea a los demás en cola listen (backlog \+ 1). |
| programa\_06 | Concurrente (fork) | accept() crea hijo; hijo close(fd\_s), padre close(fd\_c). | Imposible directo (memorias aisladas). | No sirve para chat grupal sin *pipes* /IPC; costo de clonar procesos. |
| programa\_07 | Multiplexado (select) | 1 solo proceso; select(max\_fd \+ 1, ...) vigila fd\_set. | **Sí** (broadcast por arreglo client\_socket). | Limitado por tamaño de arreglo/fd\_set. |

### **(d) Errores comunes y puntos recalcados para examen (Unidad 3\)**

> * **Pregunta explícita de examen teórico (Clase 17):** ¿Cómo distinguir a simple vista el código de un servidor frente al de un cliente? El servidor tiene **dos** estructuras sockaddr\_in (propia y cliente) y dos descriptores (fd\_s y fd\_c), mientras que el cliente solo tiene **una** estructura sockaddr\_in y un descriptor.  
> * En programa\_06, olvidar close(fd\_s) en el hijo o close(fd\_c) en el padre deja descriptores fugados y colgados.  
> * No verificar if (info\_cliente \!= NULL) tras gethostbyaddr() provoca *segmentation fault* cuando el DNS no resuelve la IP del cliente.  
> * En programa\_05, omitir memset en cada ciclo del chat provoca que mensajes cortos se mezclen con sobrantes de mensajes largos anteriores (como ocurrió en vivo con "Hola, me llamo Víctor" \-\> "Soy ingeniero" \-\> "taco").  
> * En struct tm, olvidar sumar \+ 1 a tm\_mon (meses 0–11) y \+ 1900 a tm\_year.  
> * En select(), olvidar reiniciar FD\_ZERO y reinsertar descriptores en cada vuelta del while(1).  
> * Olvidar configurar tcp\_syncookies \= 0 y tcp\_syn\_retries \= 1 (en vez de 5 \= 63 s o 6 \= 180 s) al probar el rechazo por desbordamiento de cola en la Tarea 4\.

## ---

**UNIDAD 4: CRIPTOGRAFÍA SIMÉTRICA, TRANSFERENCIA DE ARCHIVOS Y CIBERSEGURIDAD (TEMA 4\)**

### **(a) Qué problema resuelve y cómo se conecta con el tema anterior**

Como demostró el *sniffer* de capa 2, enviar mensajes o PDFs en claro permite que cualquiera en la red reconstruya la información. Además, hasta la Unidad 3 no se había programado un cliente-servidor propio para transferir directorios y archivos binarios completos. Esta unidad une criptografía simétrica OpenSSL (EVP) con transferencia de archivos por bloques para obtener un FTP seguro y comprender el *ransomware*.

### **(b) Conceptos clave**

> * **Relleno ( Padding ) PKCS y Cifrado Simétrico AES-256-CBC con OpenSSL EVP (Clases 21, 22\)**  
  * **Definición:** AES opera sobre bloques fijos de 16 bytes (DES usaba 8). El relleno **PKCS** completa los k bytes faltantes hasta el siguiente múltiplo de 16 llenando cada byte faltante con el valor numérico k. Si la cadena ya mide exactamente 16 bytes, el algoritmo agrega un bloque entero adicional de 16 bytes con valor 16, subiendo a 32 bytes.  
  * **Analogía:** Tarimas de paquetería de 16 espacios: si mandas 10 cajas, llenas los 6 huecos con espuma marcada con el número "6"; si llenas los 16 espacios justos, debes mandar otra tarima vacía de 16 espumas marcadas con "16" para que el receptor sepa dónde acaba el mensaje real.  
  * **Ciclo EVP ( , ):** Utiliza una llave simétrica de 32 bytes (256 bits) guardada/leída en binario ("wb" / "rb") y un Vector de Inicialización (IV) aleatorio de 16 bytes (RAND\_bytes), que hace que una misma entrada produzca salidas distintas cada vez. Ciclo de cifrado: EVP\_CIPHER\_CTX\_new() → EVP\_EncryptInit\_ex(..., EVP\_aes\_256\_cbc(), NULL, key, iv) → EVP\_EncryptUpdate() → EVP\_EncryptFinal\_ex(). El descifrado usa las funciones simétricas DecryptInit\_ex, DecryptUpdate, DecryptFinal\_ex con **exactamente la misma llave y el mismo IV**.  
  * **Inspección de bytes ( bytes\_to\_bits en crypto\_v2.c ):** Un bloque cifrado de 16 bytes imprime 32 caracteres en hexadecimal (2 hex por byte). En ASCII (0–255), los primeros 33 valores (0 al 32, espacio) no son visibles en pantalla; los visibles empiezan en el 33 (\!). Si el bit más significativo del char es 1, el valor decimal sale negativo por complemento a dos.  
> * **Protocolo Cifrado Cliente-Servidor de 3 envíos ( servidor\_texto\_crypto.c / cliente\_texto\_crypto.c ) (Clases 21, 22\)**  
  * **Definición:** Como el IV de 16 bytes es aleatorio por ejecución y la longitud cifrada varía como múltiplo de 16, el cliente realiza **3 send()** y el servidor **3 recv()** en estricto orden: (1) IV de 16 bytes, (2) longitud del texto encriptado (para reservar memoria exacta), y (3) arreglo de bytes encriptados (longitud\_original \+ EVP\_MAX\_BLOCK\_LENGTH).  
  * **Compilación:** Requiere enlazar dos librerías al final: gcc archivo.c \-o archivo \-lssl \-lcrypto (con y).  
  * **Ejemplo de clase:** Al enviar "Carlos" (6 caracteres → 16 bytes cifrados), los 16 bytes (119, \-111, \-72,..., \-40) llegaron idénticos, pero al inicio el descifrado salía en blanco porque el servidor había regenerado un llave.key distinto al de GitHub; se corrigió copiando la llave con scp.  
> * **Encriptación de Archivos Completos ( encriptador.c / desencriptador.c ) (Clase 22\)**  
  * **Definición:** Cifrado de archivos arbitrarios (texto, PDF, MP4 de 2 GB) que no caben enteros en RAM, procesándolos por pedazos (*chunks*) en un bucle while con búfer de entrada de **4096 bytes** (tamaño de una página de memoria del SO) y búfer de salida de **4096 \+ EVP\_MAX\_BLOCK\_LENGTH**. Usa snprintf para construir \<archivo\>.encrypt evitando desbordamientos de búfer.  
  * **Sincronización del IV y llave:** Guarda la llave en llave\_archivo.key (32 bytes) y escribe los 16 bytes del **IV sin encriptar al inicio del archivo .encrypt** antes de escribir los bloques cifrados.  
  * **Ejemplo en vivo:** archivo.txt con "Hola Mundo" (10 bytes, 11 en Linux por el salto de línea \\n) generó archivo.txt.encrypt de **32 bytes** (16 del IV \+ 16 del bloque cifrado). Al pasarlo por desencriptador, generó .decrypt idéntico al original sin borrar archivos.  
> * **Listado de directorios ( ) y Transferencia de Archivos FTP ( cliente\_envia\_archivos.c / servidor\_recibe\_archivos.c ) (Clase 23\)**  
  * **Listado local ( listado\_archivos.c ):** Usa DIR \*carpeta \= opendir("."), recorre con while ((archivo \= readdir(carpeta)) \!= NULL) accediendo al nombre con operador flecha **archivo-\>d\_name** (por ser apuntador a struct dirent) y cierra con closedir().  
  * **Arquitectura FTP (3 envíos por archivo y accept() fuera del while(1) ):**  
  * **Cliente (4 argumentos: ./cliente ):** Recorre el directorio omitiendo "." (directorio actual) y ".." (directorio padre), y por cada archivo envía: (A) nombre (256 chars máx., límite del SO), (B) tamaño en tipo **long** (obtenido con stat st\_size, más amplio que int), y (C) contenido binario ("rb") en bloques de 1024 bytes con fread \+ send.  
  * **Servidor (2 argumentos: ./servidor ):** Coloca **accept() ANTES del while(1)** porque atiende a un solo cliente y usa el while(1) para recibir N archivos secuenciales en esa misma conexión. Paso A: recv nombre (si \<= 0 el cliente terminó \-\> break). Paso B: recv tamaño long y fopen(..., "wb"). Paso C: bucle while (total\_recibido \< tamano\_archivo) calculando a\_leer para no pasarse en el último bloque (if (tamano\_archivo \- total\_recibido \< 1024)), escribiendo con fwrite y cerrando con fclose.  
  * **Traza en vivo:** Archivo de 2048 bytes con búfer 1024 realiza exactamente 2 subciclos (0 \+ 1024 \= 1024 \< 2048 verdadero; 1024 \+ 1024 \= 2048 \< 2048 falso). Prueba desde Codespaces hacia 132.248.59.6:4898 transfiriendo archivo1.txt y archivo2.txt (21 bytes cada uno).  
> * **Anatomía de Ransomware y DDoS (Clases 22, 23\)**  
  * **Ransomware (4 pasos):** (1) Ingeniería social / phishing (revisar origen real del correo con *"Mostrar original"* / *"Ver origen del mensaje"*, no confiar solo en el campo From, ni escanear QR desconocidos); (2) Infección; (3) Exfiltración en segundo plano abriendo un socket (causa lentitud; los archivos pueden viajar en texto plano y luego cifrarse en la víctima, o cifrarse primero y enviarse ya cifrados); (4) Cifrado local y extorsión en Bitcoin. Tener respaldos evita parar operaciones, pero **no evita el daño reputacional ni el económico** porque el atacante ya robó copia de los datos.  
  * **DDoS / SYN Flood :** Botnets de dispositivos IoT saturan la cola SYN; valores altos en parámetros de red (tcp\_syn\_retries 5/6) generan muchos reintentos, mientras 0 y 1 (Tarea 4\) descartan rápido para no retener conexiones semiabiertas.

### **(c) Comparación del protocolo de 3 pasos en Cifrado vs FTP (Unidad 4\)**

| Aspecto | Cifrado Cliente-Servidor (texto\_crypto) | Encriptador de Archivos (encriptador) | FTP (envia / recibe\_archivos)   |
| :---- | :---- | :---- | :---- |
| **Metadatos iniciales** | Envío 1: IV (16 bytes). Envío 2: Longitud cifrada. | Primeros 16 bytes del archivo .encrypt guardan el IV sin cifrar. | Envío 1: Nombre (256 chars máx.). Envío 2: Tamaño (long). |
| **Transferencia / Proceso** | Envío 3: Texto encriptado (+ EVP\_MAX\_BLOCK\_LENGTH). | Bucle de lectura-cifrado-escritura en bloques de 4096 bytes. | Bucle total\_recibido \< tamano en bloques de 1024 bytes. |
| **Modos de archivo** | "rb" para leer llave.key (32 bytes). | "rb" origen, "wb" .encrypt y llave\_archivo.key. | "rb" en cliente, "wb" en servidor. |

### **(d) Errores comunes y puntos recalcados para examen (Unidad 4\)**

> * Creer que el relleno PKCS rellena con ceros o olvidar que una cadena exacta de 16 bytes crece a 32 bytes (agregando 16 bytes de valor 16).  
> * Confundir 32 caracteres hexadecimales con 32 bytes (32 hex \= 16 bytes) o intentar contar 32 caracteres visibles en .encrypt (los bytes ASCII 0–32 son no imprimibles).  
> * Compilar sin \-lssl \-lcrypto (o escribir cripto con i).  
> * Usar llaves distintas entre cliente y servidor: los bytes cifrados llegan idénticos, pero el descifrado sale vacío.  
> * No omitir "." y ".." al recorrer directorios con readdir(), usar int en lugar de long para el tamaño de archivo, o colocar accept() dentro del while(1) en el servidor receptor de múltiples archivos.

## ---

**LO QUE MÁS PROBABLEMENTE VIENE EN EL FINAL**

> 1. **Diferenciación entre Cliente y Servidor en código y gestión de los dos sockets ( fds vs fdc )**  
   * **Evidencia:** El profesor lo planteó explícitamente como *"pregunta de examen teórico"* en la Clase 17 (servidor tiene 2 sockaddr\_in y 2 descriptores; cliente solo 1\) y dijo en la Clase 10: *"Entendiendo esto ya prácticamente tienen aprobada la materia"*.  
> 2. **Cierre cruzado de descriptores tras fork() en servidores concurrentes ( programa\_06 )**  
   * **Evidencia:** Lo dibujó en pizarrón, lo repitió en la Clase 16 y en la Clase 17 advirtió que *"esto es lo complicado"*: el hijo ejecuta close(fd\_s) y usa fd\_c; el padre ejecuta close(fd\_c) y conserva fd\_s para regresar a accept().  
> 3. **Por qué fork() no sirve para chat grupal y cómo funciona select() con fd\_set ( programa\_07 )**  
   * **Evidencia:** Explicó en la Clase 17 que las memorias aisladas de los hijos impiden triangular mensajes, y en la Clase 18 desglosó los 5 argumentos de select() en Open Group y las 4 macros (FD\_ZERO, FD\_SET, FD\_CLR, FD\_ISSET).  
> 4. **Saludo de 3 vías TCP, colas SYN / Accept y regla backlog \+ 1 de sk\_acceptq\_is\_full()**  
   * **Evidencia:** Fue el núcleo de la Tarea 4 y se analizó en las Clases 12, 13 y 23 (operador \> en lugar de \>= en el kernel, ataque *SYN flood* y efecto de tcp\_syncookies \= 0 y tcp\_syn\_retries \= 1).  
> 5. **Conversiones de red ( htons , inet\_aton / inet\_addr , inet\_ntoa , inet\_ntop ) y macro INADDR\_ANY**  
   * **Evidencia:** Lo repitió desde la Clase 9 hasta la 23, dedicó un PDF completo en la Clase 13 a desmembrar inet\_ntoa(\*(struct in\_addr \*)H-\>h\_addr\_list) y exigió htons y captura de IP como requisitos obligatorios del examen parcial.  
> 6. **Bit SetUID ( chmod 4511 ), ID real vs efectivo ( getuid vs geteuid ) y /etc/passwd vs /etc/shadow**  
   * **Evidencia:** Fue la Tarea 2 completa (Clases 2 y 3), probada en vivo con programa\_02\_ids.c obteniendo Real 1000 y Efectivo 0 durante la ejecución.  
> 7. **Ciclo fork() , procesos huérfanos ( reaper ), procesos zombie ( Z+ ) y familia exec()**  
   * **Evidencia:** El profesor recalcó el manejo de error con if (... \== \-1) y exit(EXIT\_FAILURE) en execl() (Clase 4), resolvió en vivo los valores de getpid/getppid en fork() (Clase 2\) y dedicó el cierre del Tema 2 a provocar y evitar zombies mediante SIGCHLD (Clase 7).  
> 8. **Relleno PKCS a 16 bytes, ciclo EVP de OpenSSL ( \-lssl \-lcrypto ) y protocolo de 3 envíos (IV, longitud, cifrado)**  
   * **Evidencia:** Resolvió múltiples ejemplos numéricos de relleno en vivo (10, 11, 12 y 16 bytes \-\> 32 bytes) en la Clase 21, comparó lado a lado Encrypt\* vs Decrypt\*, y remarcó que son obligatoriamente 3 send / 3 recv y compilar con \-lssl \-lcrypto.  
> 9. **Cifrado de archivos por bloques de 4096 bytes y ubicación del IV al inicio de .encrypt**  
   * **Evidencia:** En la Clase 22 señaló explícitamente la pregunta teórica del PDF sobre por qué se usa 4096 bytes (tamaño de página de memoria), mostró snprintf y 4096 \+ EVP\_MAX\_BLOCK\_LENGTH, y demostró por qué "Hola Mundo" (10 bytes) resulta en un .encrypt de 32 bytes (16 IV \+ 16 bloque).  
> 10. **Transferencia FTP de directorios ( , omisión de "." y ".." , accept() antes de while(1) y traza de bloques de 1024 )**  
    * **Evidencia:** En la Clase 23 señaló con un comentario explícito la posición de accept() antes del while(1), preguntó al grupo qué atributos necesita el servidor (nombre, tamaño long, contenido) y resolvió paso a paso la traza numérica de 2048 bytes en bloques de 1024\.  
> 11. **Limpieza y truncado de búferes ( memset , buff\[n-1\] ), setsockopt(SO\_REUSEADDR) y fragmentación TCP**  
    * **Evidencia:** Demostró en vivo el desastre al comentar memset en el chat (Clase 13), explicó SO\_REUSEADDR advirtiendo que les servirá para el proyecto final (Clase 14\) y enfatizó el bucle while ((n \= read(...)) \> 0\) en TCP (Clases 14 y 15).

## ---

**CONEXIONES CLAVE**

> * Imagen del proceso \-\> divide memoria en \-\> Segmentos estáticos (Text, Data, BSS) y dinámicos (Heap, Stack)  
> * size \-\> inspecciona \-\> Segmentos estáticos del ejecutable en disco  
> * pmap \-\> consulta al kernel \-\> Páginas dinámicas de 4 KB sin permisos de ejecución  
> * /etc/passwd \-\> almacena \-\> Identidad real del usuario leída por getuid()  
> * Bit SetUID (chmod 4511\) \-\> eleva temporalmente \-\> Identidad efectiva (geteuid()) al dueño del binario  
> * fork() \-\> clona el proceso devolviendo \-\> PID del hijo al padre y 0 al hijo  
> * Ejecución asíncrona tras fork() \-\> puede provocar \-\> Condiciones de carrera y bloqueos mutuos (*deadlock*)  
> * Muerte prematura del padre \-\> convierte al hijo en \-\> Proceso huérfano adoptado por PID 1 o por un *reaper*  
> * Terminación del hijo \-\> envía \-\> Señal SIGCHLD (17) al padre para limpiar la tabla de procesos  
> * Padre dormido sin recoger SIGCHLD \-\> transforma al hijo en \-\> Proceso zombie (Z+ \<defunct\>)  
> * Familia exec() \-\> reemplaza \-\> La imagen del proceso invocante por un nuevo ejecutable  
> * Ctrl+Z (SIGTSTP) \+ bg \-\> mueven \-\> Un proceso de *foreground* a *background* controlado con jobs y fg  
> * SIGKILL (9) \-\> supera \-\> Cualquier intento de ignorar (SIG\_IGN) o capturar con signal()  
> * Descriptores reservados 0, 1, 2 \-\> dejan disponibles \-\> Descriptores 3, 4, 5 para nuevos sockets  
> * struct sockaddr\_in \-\> configura \-\> Familia (AF\_INET), puerto (htons) e IP (INADDR\_ANY / inet\_addr)  
> * gethostbyname() \-\> consulta DNS devolviendo \-\> struct hostent \* con múltiples IPs en *DNS round-robin*  
> * inet\_ntoa / inet\_ntop \-\> traducen \-\> Direcciones IP de binario de red (n) a texto legible (a/p)  
> * socket() \+ bind() \+ listen() \-\> preparan \-\> El socket servidor (fd\_s) para recibir conexiones en accept()  
> * setsockopt(SO\_REUSEADDR) \-\> evita \-\> El error de puerto ocupado en estado TIME\_WAIT al reiniciar el servidor  
> * Saludo de tres vías (SYN / SYN+ACK / ACK) \-\> alimenta \-\> La cola SYN y la cola Accept del kernel  
> * sk\_acceptq\_is\_full() con operador \> \-\> permite encolar \-\> backlog \+ 1 peticiones en espera en listen()  
> * accept() \-\> devuelve \-\> El descriptor fd\_c dedicado a send() y recv() con el cliente  
> * IP pública compartida (NAT) \-\> distingue clientes simultáneos mediante \-\> Puertos efímeros únicos asignados en el cliente  
> * Fragmentación TCP y búferes del kernel \-\> obligan a \-\> Leer mensajes grandes en bucle while hasta devolver 0  
> * Servidor concurrente (programa\_06) \-\> logra paralelismo mediante \-\> fork(), cerrando fd\_s en el hijo y fd\_c en el padre  
> * Memoria aislada de procesos hijos con fork() \-\> exige usar \-\> Multiplexación con select() y fd\_set para chats grupales  
> * SOCK\_RAW con AF\_PACKET \-\> intercepta en capa 2 \-\> Tramas Ethernet sin cifrar usando modo promiscuo  
> * Relleno PKCS \-\> expande los bloques \-\> Al siguiente múltiplo de 16 bytes (y de 16 a 32 bytes)  
> * Cifrado simétrico EVP (AES-256-CBC) \-\> requiere sincronizar \-\> La misma llave de 32 bytes (llave.key) y el mismo IV de 16 bytes  
> * cliente\_texto\_crypto \-\> transmite al servidor en orden \-\> IV (16 bytes), longitud cifrada y bloque cifrado (3 send/recv)  
> * encriptador.c \-\> procesa archivos arbitrarios \-\> En bloques de página de 4096 bytes anteponiendo el IV al archivo .encrypt  
> * \<dirent.h\> (opendir/readdir) \-\> permite recorrer \-\> Un directorio completo omitiendo "." y ".." para transferir archivos  
> * servidor\_recibe\_archivos.c \-\> coloca accept() antes de while(1) para \-\> Recibir múltiples archivos de un mismo cliente en bloques de 1024 bytes  
> * Sockets en segundo plano \+ encriptador \-\> reproducen la mecánica \-\> De exfiltración y secuestro de datos de un *ransomware*

## **Anexo · Clases que no estaban en el cuaderno de NotebookLM**

*Resumen para estudiar de cada una, tomado de los apuntes por clase del sitio (decimo/ACS/ACS-Resumenes/).*

### **Clase 5 · Estados de un proceso, señales, wait() y zombies (martes 8 sep 2026\)**

*Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.*

| Concepto | Para recordar   |
| :---- | :---- |
| Estados | 9; el 9 es zombie |
| Señales | Asíncronas; KILL 9 ineludible, TERM 15 manejable |
| SIGCHLD | 17 en x86/ARM (18 en la tabla System V) |
| wait() | Bloquea al padre; WIFEXITED, WEXITSTATUS, WIFSIGNALED, WTERMSIG |
| Zombie | Padre no llamó wait(); ps: Z+ defunct |
| \$? | ≥ 128 \= terminó por señal |

### **Clase 19 · El sniffer en capa 2 (reconstruida del material del profesor) (jueves 29 oct 2026\)**

*Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.*  
**Puntos clave**

> * Modo promiscuo \+ AF\_PACKET/SOCK\_RAW (root) \= trama completa desde capa 2\.  
> * Ethernet 14 B → IP ihl·4 → TCP doff·4 → payload; protocolo 6 \= TCP.  
> * Red \= big-endian; ntohs() al leer, htons() al mandar.  
> * El texto plano se lee tal cual: hay que cifrar.

#### **Ponte a prueba**

> 1. **¿Qué hace el modo promiscuo?** Que la tarjeta entregue todas las tramas del medio sin filtrar por MAC.  
> 2. **¿Qué socket crea el sniffer y por qué pide root?** socket(AF\_PACKET, SOCK\_RAW, htons(ETH\_P\_ALL)); los sockets crudos requieren CAP\_NET\_RAW.  
> 3. **Con ihl \= 5 y doff \= 5, ¿dónde empieza el payload?** 14 \+ 20 \+ 20 \= 54 bytes después del inicio.  
> 4. **¿Qué ve la CPU si lee el puerto 4898 sin ntohs()?** 0x2213 \= 8723\.  
> 5. **¿Qué máquina va en modo promiscuo si son tres distintas?** Solo la del sniffer.

### **Clase 20 · Criptografía simétrica con OpenSSL: AES-256-CBC (reconstruida) (martes 3 nov 2026\)**

*Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.*  
**Puntos clave**

> * Texto plano \= interceptación y modificación (X.800).  
> * AES-256: bloque de 16 B, llave de 32 B, 14 rondas; CBC con IV de 16 B; relleno PKCS\#7.  
> * EVP: new → init → update → final; descifrar con la misma llave y el mismo IV.  
> * RAND\_bytes y llave.key en "wb"; compilar con \-lcrypto.

#### **Ponte a prueba**

> 1. **¿Cuánto miden el bloque de AES, la llave de AES-256 y el IV?** 16 bytes, 32 bytes y 16 bytes.  
> 2. **¿Qué hace el modo CBC?** Combina cada bloque con XOR con el bloque cifrado anterior (el primero con el IV) para eliminar patrones.  
> 3. **¿Por qué se suma EVP\_MAX\_BLOCK\_LENGTH al arreglo cifrado?** Por el relleno PKCS\#7 del último bloque.  
> 4. **¿Por qué la llave se escribe con "wb"?** Porque los bytes crudos pueden contener 0x00 o 0x0A, que el modo texto corrompería.  
> 5. **¿Qué diferencia hay entre libssl y libcrypto?** libssl: protocolos TLS/DTLS; libcrypto: algoritmos, aleatorios y certificados.  
> 6. **Ordena el ciclo de cifrado EVP.** CTX\_new → EncryptInit\_ex → EncryptUpdate → EncryptFinal\_ex (→ CTX\_free).