% materia: Arquitectura Cliente-Servidor
% titulo: Clase 19 · El sniffer en capa 2 (reconstruida del material del profesor)
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · jueves 29 oct 2026 · Tema 3 (sniffer con sockets crudos) · clase reconstruida · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Análisis de tramas en capa 2 con sockets crudos: modo promiscuo, AF_PACKET + SOCK_RAW, encapsulamiento Ethernet–IPv4–TCP, orden de bytes de red, extracción del payload y la Tarea 5.

!!! Fuente
Fuente: material oficial del profesor en su sitio (Tema 3): presentación «Análisis de tramas en capa 2, desencapsulamiento TCP/IP y raw sockets», `sniffer.c` y el requerimiento de la Tarea 5. ⚠️ **No asistí a esta clase y no hay audio.** El contenido se reconstruyó con el material del profesor. Que esta sesión haya sido la del sniffer se deduce del orden del material (la Clase 18 lo introdujo y la Clase 21 ya era de cifrado); no está confirmado qué se vio exactamente ese día.

## 1. De los sockets de aplicación a los sockets crudos
Con `SOCK_STREAM` sobre `AF_INET` parece haber un «tubo directo» entre cliente y servidor: el kernel agrega y quita las cabeceras TCP, IP y Ethernet, y la tarjeta de red descarta las tramas cuya MAC destino no es la suya. Un sniffer rompe esa abstracción.

**Modo promiscuo:** el driver de la tarjeta entrega al CPU todas las tramas del medio, sin filtrar por MAC.

**Sockets crudos** (`AF_PACKET` + `SOCK_RAW`): el kernel no desarma el paquete; se recibe la trama completa desde la capa 2. Requieren root (`CAP_NET_RAW`).

```
raw_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
if (raw_socket < 0) { perror("Error (¿Ejecutaste con sudo?)"); return 1; }
```

## 2. Encapsulamiento y aritmética de punteros
El paquete capturado se recorre superponiendo estructuras sobre un búfer y sumando desplazamientos.

`malloc(65536)`: 64 KB, el tamaño máximo teórico de un paquete IP (2¹⁶). `recvfrom()` copia la trama al búfer y devuelve cuántos bytes llegaron.

Secuencia: **Ethernet (14 B) → IPv4 (20–60 B) → TCP (20–60 B) → datos de aplicación**.

**Ethernet** (`struct ethhdr`, en el byte 0): MAC destino (6 B), MAC origen (6 B) y EtherType (2 B; `ETH_P_IP` = 0x0800 es IPv4).

**IPv4** (`buffer + sizeof(struct ethhdr)`): `iph->ihl` mide la cabecera en palabras de 4 bytes (5 × 4 = 20 B); `iph->protocol == 6` es TCP (1 = ICMP, 17 = UDP).

**TCP** (tras 14 + longitud IP): `tcph->doff * 4` es la longitud de la cabecera TCP. Se filtra el puerto 4898.

## 3. Orden de bytes de red
TCP/IP transmite primero el byte más significativo (*big-endian*); x86 guarda primero el menos significativo (*little-endian*).

El puerto 4898 = 0x1322 viaja como 0x13 y luego 0x22. Si se lee sin convertir, la CPU ve 0x2213 = 8723.

`htons()` al mandar valores de 16 bits al socket (`htons(ETH_P_ALL)`); `ntohs()` al leer `h_proto`, `tcph->source` y `tcph->dest`.
Error común: leer puertos o EtherType sin `ntohs()`.

## 4. El payload y el riesgo del texto plano
Los datos de usuario empiezan después de todas las cabeceras.

```
int tcp_header_len = tcph->doff * 4;
int total_headers_size = sizeof(struct ethhdr) + iphdrlen + tcp_header_len;
unsigned char *payload = buffer + total_headers_size;
int payload_size = data_size - total_headers_size;
if (payload_size > 0) printf("%.*s\n", payload_size, payload);
```

Si `payload_size == 0` es un paquete de control (SYN, ACK, FIN) y se ignora. `%.*s` imprime exactamente `payload_size` bytes (evita leer de más).

Conclusión: un cliente-servidor sobre TCP puro expone contraseñas y comandos en la red local; la mitigación es cifrar en tránsito (TLS), que es lo que sigue en el Tema 4.

## 5. Tarea 5: probar el sniffer en tres terminales
Guía de laboratorio del profesor.

1. **Terminal 1 (root):** `ip link set eth0 promisc on` (o `lo` en loopback; comprobar con `ifconfig`), `gcc sniffer.c -o sniffer` y `./sniffer`.
2. **Terminal 2:** servidor en el 4898 (programa 04 o 05): `./programa04_servidor_internet 4898`.
3. **Terminal 3:** cliente: `./programa04_cliente_internet 127.0.0.1 4898`.

La terminal 1 intercepta la trama, desencapsula IP y TCP e imprime el payload en claro. Si se usan máquinas distintas, **solo la del sniffer** va en modo promiscuo, porque es la observadora pasiva.

## Pendiente / próxima clase
- Tarea 5: probar el sniffer en tres terminales y entregar capturas (requerimiento en el sitio del profesor).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Puntos clave
- Modo promiscuo + `AF_PACKET`/`SOCK_RAW` (root) = trama completa desde capa 2.
- Ethernet 14 B → IP `ihl·4` → TCP `doff·4` → payload; protocolo 6 = TCP.
- Red = big-endian; `ntohs()` al leer, `htons()` al mandar.
- El texto plano se lee tal cual: hay que cifrar.

## Ponte a prueba
1. **¿Qué hace el modo promiscuo?** Que la tarjeta entregue todas las tramas del medio sin filtrar por MAC.
2. **¿Qué socket crea el sniffer y por qué pide root?** `socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))`; los sockets crudos requieren `CAP_NET_RAW`.
3. **Con `ihl = 5` y `doff = 5`, ¿dónde empieza el payload?** 14 + 20 + 20 = 54 bytes después del inicio.
4. **¿Qué ve la CPU si lee el puerto 4898 sin `ntohs()`?** 0x2213 = 8723.
5. **¿Qué máquina va en modo promiscuo si son tres distintas?** Solo la del sniffer.
