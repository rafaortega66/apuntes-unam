# ACS-T04 — Tarea 4: ejemplo_listen.c (cola de listen) · indicaciones

ACS no usa Classroom. Fuente: NotebookLM, cuaderno ACS (audios de clase).
Programa del profesor: `../../ACS-Material/programas/tema3/ejemplo_listen.c`.
1. Investigar la función del kernel **`sk_acceptq_is_full`** y la teoría del desbordamiento de las colas **TCP SYN** y **ACCEPT**.
2. Investigar los parámetros **`tcp_syncookies`** y **`tcp_syn_retries`**.
3. Con root (`sudo sysctl -w`): `tcp_syncookies=0` y `tcp_syn_retries=1`.
4. Ejecutar el servidor `ejemplo_listen` (backlog 1 en `listen`) y conectar **4 o más clientes con `nc`** para mostrar cuántas conexiones se encolan antes de rechazarse.
- Entrega: **PDF por correo**, con la explicación teórica y **capturas de todas las terminales** (servidor, opcionalmente `watch -n1 ss …`, y los clientes).
- Fecha: antes del jueves de la semana siguiente a la clase en que se explicó.
