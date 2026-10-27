% materia: Arquitectura Cliente-Servidor
% titulo: Clase 15 · Servidor que despacha un PDF e indicaciones del parcial
% subtitulo: Arquitectura Cliente-Servidor · Mtro. Carlos Alberto Román Zamitiz · jueves 15 oct 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Por qué varía el total de bytes de una respuesta HTTP
Duda de la Clase 14: cada petición a www.google.com devolvía un total distinto (91,351, 91,271, 90,508 bytes…).
!!! Respuesta
La variación viene de las **cabeceras HTTP**, que cambian ligeramente entre peticiones o entre IP; es muy raro que dos respuestas traigan los mismos metadatos. **No es pérdida de paquetes.**
Servidores como Apache Tomcat usan el **puerto 8080** cuando corren sin privilegios de root y el **80** en producción o con root.

## 2. programa_08_servidor_pdf.c
Servidor TCP en C que lee un archivo binario (`holamundo.pdf`) y lo manda por bloques a un cliente (por ejemplo, un navegador).
1. Dos `sockaddr_in` (servidor y cliente) y dos descriptores (`fd_servidor`, `fd_cliente`).
2. `socket(AF_INET, SOCK_STREAM, 0)` validando −1; `setsockopt` con `SO_REUSEADDR`.
3. `memset`, `sin_family = AF_INET`, `sin_addr.s_addr = INADDR_ANY`, puerto con `htons`; `bind`, `listen`, `accept`.
4. IP del cliente con `gethostbyaddr` (o `inet_ntoa(cliente.sin_addr)`).
5. Descartar la petición del navegador: `recv` con **`MSG_DONTWAIT`** para vaciar el búfer sin bloquearse.
6. `open(PDF_PATH, O_RDONLY)`:
- - Si da −1 → **404 Not Found** con `Content-Type: text/plain` ("archivo no encontrado").
- - Si abre → **200 OK** con `Content-Type: application/pdf`.
7. Transferencia por bloques y cierre:
```
while ((r = read(fd_archivo, buffer, sizeof(buffer))) > 0)
    send(fd_cliente, buffer, r, 0);   /* exactamente los r bytes leídos */
close(fd_cliente); close(fd_servidor);
```
En clase corrió en 132.248.59.6:4898; el primer alumno recibió el PDF y el servidor terminó ("PDF enviado correctamente"). Para atender a varios seguidos hace falta un **`while(1)` alrededor de `accept`**.
!!! Idea clave
Para un socket TCP no hay diferencia entre texto y binario: todo es un flujo de bytes que se manda en bloques con un bucle.
Errores comunes: nombre de archivo mal escrito (→ 404); mandar un archivo grande con un solo `send`; olvidar el `while(1)`.

## 3. Indicaciones del examen parcial (ACS-E01, ya entregado)
Basado en el Programa 04, pero **invirtiendo el flujo**: el cliente envía primero su nombre, el servidor lo recibe, lo imprime y responde con una confirmación; luego ambos terminan.
| Parte | Requisito |
|---|---|
| Servidor | Puerto por **línea de comandos** (nunca en código duro) con `htons`; imprimir la IP del cliente |
| Cliente | IP y puerto del servidor por línea de comandos; nombre por teclado (`fgets`) en formato APELLIDO_PATERNO APELLIDO_MATERNO NOMBRE(S) |
| Prueba local | Dos terminales, cliente contra 127.0.0.1; captura del envío, la impresión y la respuesta |
| Prueba remota | Contra 132.248.59.6 (4898 o 4899); ejecutar `date` en la misma terminal; captura. El servidor guardaba IP, fecha, hora y nombre |
| Entrega | Por correo, los `.c` y capturas (PNG o PDF con conclusiones), del jueves 15 al lunes. **Sin ejecutables** (el correo los filtra) |

## 4. cron
Las 5 columnas de crontab: **minuto, hora, día del mes, mes, día de la semana**. `30 8 15 10 *` lanzó su servidor el 15 de octubre a las 8:30.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Bytes que varían.** Por las cabeceras HTTP, no por pérdida de paquetes. Tomcat: 8080 sin root, 80 con root.

!!! Enviar un binario (examen)
`open` → si −1, 404 `text/plain`; si no, 200 `application/pdf` → `while ((r = read(...)) > 0) send(fd, buffer, r, 0)` → cerrar. Para varios clientes, `while(1)` sobre `accept`.

| Detalle | Para recordar |
|---|---|
| `MSG_DONTWAIT` | Vaciar la petición del navegador sin bloquearse |
| `SO_REUSEADDR` | Reutilizar el puerto al relanzar |
| Puerto | Por `argv` y `htons`, nunca en código duro |
| crontab | min · hora · día · mes · día de semana |
