# ACS-E01 — Examen parcial (programa cliente-servidor con sockets TCP) · indicaciones

ACS no usa Classroom. Fuente: NotebookLM, cuaderno ACS (audios ACS-Clase14 y ACS-Clase15), consultado el 18 oct 2026.
Base: `../../ACS-Material/programas/tema3/programa04_servidor_internet.c` y `programa04_cliente_internet.c`.

- **Modalidad:** examen de casa, práctico, individual, en C. Se asignó el **jueves 15 oct (Clase 15), 8:30**;
  se entrega por **correo el lunes 19 oct en la noche** (hora exacta no especificada en las fuentes).
- **Valor en la calificación:** no aparece en las fuentes.

## Qué hay que hacer
1. Servidor y cliente TCP en C (`socket`, `bind`, `listen`, `accept`, `connect`, `send`/`recv`), basados en el Programa 04.
2. **Diferencia clave con el Programa 04:** en el examen **el cliente escribe primero** (manda el nombre del alumno).
3. El servidor recibe el **puerto por línea de comandos** (nada fijo en el código) y lo convierte con `htons`
   (NotebookLM lo transcribe como «H2NS»).
4. El cliente lee el **nombre completo desde el teclado**, en formato *Apellido Paterno Apellido Materno Nombre(s)*.
5. El servidor obtiene la **IP de origen del cliente** (`sin_addr` de la estructura del cliente o `gethostbyaddr`)
   y le **responde confirmando el registro**.
6. **Prueba local:** dos terminales en la misma máquina (servidor y cliente lado a lado).
7. **Prueba remota:** contra el servidor del profesor, **132.248.59.6, puerto 4899**, ejecutando antes `date` en la terminal del cliente.

## Qué se entrega (por correo)
- `.c` del servidor y `.c` del cliente.
- Capturas (PNG o en un PDF) de la prueba local y de la prueba remota (con la salida de `date` visible).
- **Nunca** adjuntar ejecutables: el servidor de correo los rechaza como malware.

## Avisos del profesor
- El servidor remoto registra IP, fecha, hora y nombre; dos nombres distintos desde la misma IP se detectan como copia.
- «El examen es muy parecido» a los programas 04 y 05 y a `compara_tiempos_buffers.c` (Clase 14). No confiarse por ser de casa.
- No entra teoría escrita ni cuestionario.
