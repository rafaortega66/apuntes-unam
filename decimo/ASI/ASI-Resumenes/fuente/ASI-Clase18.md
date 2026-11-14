% materia: Administración de Servicios de Internet
% titulo: Clase 18 · Exposiciones de RFC: HTTP/1.1, IMAP, POP3, LDAP, IANA, Telnet y DNS
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · lunes 9 nov 2026 · Exposiciones de los RFC (1.ª parte) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Exposiciones por equipo de RFC fundamentales: HTTP/1.1 (2616), IMAP4rev1 (3501), POP3 (1939), LDAPv3 (4510), números asignados de IANA (1700, nuestro equipo), Telnet (854) y DNS (1034), con las preguntas del profesor.

!!! Fuente
Fuente: NotebookLM (audio `ASI-Clase18.m4a`), 14 nov 2026. El contenido técnico es de las exposiciones de los equipos; las preguntas y comentarios son del profesor. Los RFC entran en el examen final (16 nov), según la Clase 17.

## 1. RFC 2616: HTTP/1.1 (equipo 8)
Especificación de junio de 1999 (IETF) del protocolo HTTP 1.1: comunicación cliente-servidor petición-respuesta, sin estado, sobre TCP.

!!! En simple
Pedir en la ventanilla de una taquería donde nadie te recuerda: cada pedido va en una hoja con el mismo formato y te regresan un ticket con un número que dice si salió bien o qué falló. Límite: en HTTP/1.1 la ventanilla deja el canal abierto para no hacer fila otra vez (conexión persistente).

Cada transacción es independiente. Mensaje en tres partes: línea inicial, cabeceras y cuerpo opcional. Métodos GET, POST, PUT, DELETE, OPTIONS, CONNECT…; los **seguros** solo leen y los **idempotentes** producen lo mismo con una o varias peticiones. Códigos: 1xx información, 2xx éxito, 3xx redirección, 4xx error del cliente, 5xx error del servidor.

Novedades de 1.1: conexiones persistentes, cabecera obligatoria que permitió el *virtual hosting*, *chunked transfer encoding* y mejor caché. Corrigió al RFC 1945 (solo informativo) y al 2068. Su desventaja: un documento monolítico de 176 páginas; en 2014 se dividió en los RFC 7230–7235 y después llegaron HTTP/2 (multiplexación) y HTTP/3 (sobre QUIC).

El profesor preguntó cómo se aplica con GET o POST: GET pide información al servidor; POST le envía información y recibe respuesta. El RFC solo describe los pasos de la comunicación.

## 2. Qué es un RFC y el RFC 3501: IMAP (equipo 3)
**RFC** (*Request for Comments*): documentos técnicos de la IETF, inmutables (no se editan; evolucionan con un RFC nuevo), que especifican protocolos y normas. **RFC 3501** (2003, Mark Crispin, Universidad de Washington): IMAP4rev1, para leer y manipular el correo en el servidor sin descargarlo.

!!! En simple
Las cartas viven en un archivero central: desde el celular ves la lista, abres una y le pones el sello de «leído»; al llegar a la oficina ya tiene el sello, porque nunca salió del archivero. Límite: si se cae el servidor o la conexión, no puedes trabajar.

Capa 7; puerto **143** sin cifrar y **993** con cifrado. Cada comando lleva una etiqueta (A001) y el servidor responde OK, NO (falló) o BAD (comando mal escrito), más líneas con asterisco.

Cuatro estados: no autenticado (→ LOGIN), autenticado (→ SELECT), seleccionado (se trabaja con los mensajes) y cierre (LOGOUT). Comandos: LIST, SELECT, FETCH (descarga selectiva, primero solo encabezados), SEARCH, CREATE, RENAME, DELETE, STORE (banderas), EXPUNGE (borra lo marcado). Banderas: \Seen, \Answered, \Flagged, \Deleted, \Draft, \Recent.

Ejemplo: en el camión, puerto 993, `A001 LOGIN` → OK; `SELECT INBOX` → 172 mensajes, 1 reciente; FETCH solo de encabezados; al abrir uno, STORE pone \Seen; en la oficina ya no aparece como nuevo.

El profesor preguntó cuál recomiendan y qué desventaja tiene: IMAP por ver el correo en varios dispositivos, pero si se pierde el servidor no se trabaja. Recordó que esa semana en Japón se cayeron unos 300 bancos por depender de un mismo servidor, y que IMAP obliga a crecer el almacenamiento del servidor; por eso muchos siguen descargando con POP.

## 3. RFC 1939: POP3 (equipo 1)
Mayo de 1996 (John Myers y Marshall Rose, reemplaza al 1725): protocolo simple para conectarse, descargar el correo al dispositivo y borrarlo del servidor.

!!! En simple
El buzón afuera de tu casa: el cartero (SMTP) deja las cartas, tú las sacas todas con tu llave y el buzón queda vacío. Límite: si quieres releer la carta desde otro escritorio, ya no está en el buzón.

SMTP deposita el correo en el buzón del servidor; POP3 lo recoge por TCP en el puerto **110** (o **995** con SSL/TLS). Respuestas: `+OK` o `-ERR`; las multilínea terminan con un punto en una línea.

Tres estados: **autorización** (USER, PASS, APOP), **transacción** (STAT, LIST, RETR n, DELE n, RSET, NOOP) y **actualización** (al enviar QUIT se borra lo marcado). Bloqueo exclusivo del buzón y *timeout* de 10 minutos; DELE solo marca.

Ejemplo: STAT da 2 mensajes; DELE de uno → STAT da 1; RSET → vuelve a 2; QUIT.

Seguridad: el original mandaba usuario y contraseña en texto plano (expuesto a *man-in-the-middle*); luego APOP (reto-respuesta con MD5) y hoy POP3S por el 995. POP3 consume pocos recursos y sirve para uso local.

## 4. RFC 4510: LDAPv3 (equipo 7)
Junio de 2006 (Kurt Zeilenga, OpenLDAP), 6 páginas, Standard Track: la hoja de ruta de LDAP versión 3, el protocolo para gestionar usuarios, contraseñas y permisos de forma centralizada.

!!! En simple
El directorio y libro de llaves de una empresa: todas las puertas consultan el mismo directorio en vez de tener su propia lista. El RFC 4510 es el índice de ese manual.

Repaso de los RFC: Steve Crocker en ARPANET (1969), públicos y gratuitos en rfc-editor.org, inmutables, cinco categorías (Standard Track, BCP, Informational, Experimental, Historic) y palabras clave normalizadas (MUST, SHOULD, MAY).

LDAP nació como un «X.500 light», porque X.500 exigía toda la pila OSI. El 4510 reemplaza al 3377 y organiza la familia: 4511 (operaciones Bind, Search, Modify, Delete), 4512 (modelos), 4513 (autenticación SASL/TLS), 4514 (nombres distinguidos), 4515 (filtros), 4516 (URL), 4517 (sintaxis), 4518 (cadenas internacionalizadas), 4519 (esquema: uid, mail); 4520 y 4521 para registros y extensiones.

El profesor preguntó: «¿Cómo resumes el LDAP? ¿Es un protocolo o es el RFC?». Respuesta: es un protocolo, organizado por el RFC.
Error común: confundir el protocolo (LDAP) con el documento que lo especifica (RFC 4510).

## 5. RFC 1700: números asignados de IANA (equipo 10: Ortega, Valdés y García)
1994 (Joyce Reynolds y Jon Postel), hoy histórico: las tablas oficiales de IANA con los números de protocolo, las clases de direcciones IP y los puertos bien conocidos, para que dispositivos distintos se entiendan.

!!! En simple
El catálogo de códigos postales y ventanillas: además de la calle (la IP), el paquete dice qué transporte lo lleva (TCP o UDP) y a qué ventanilla va (80 web, 25 correo). Límite: un catálogo impreso envejece; por eso se reemplazó por un registro en línea.

La información viaja encapsulada en paquetes por capas; el RFC 1700 estandarizó los números para que cualquier sistema (x86, ARM) interprete qué protocolo y servicio trae cada paquete.

En la cabecera IP, **protocolo 6 = TCP** y **17 = UDP**. Puertos: 20 (FTP datos), 21 (FTP control), 22 (SSH), 25 (SMTP), 53 (DNS), 80 (HTTP).

Limitación: al ser un documento estático, cada cambio exigía una nueva publicación. En 2002 lo sustituyó el **RFC 3232**, que pasó las asignaciones a una base de datos en línea; hoy los registros de IANA se consultan y actualizan en tiempo real.

## 6. RFC 854: Telnet (equipo 4)
1983 (Postel y Reynolds, STD 8): documento, protocolo independiente del hardware para negociar señales de control, y programa cliente (PuTTY, `telnet`) que da una terminal remota.

!!! En simple
Un control remoto universal con traductor para manejar desde casa la pantalla de una computadora de la escuela. Límite: todo lo que tecleas, incluidas las contraseñas, viaja sin cifrar.

Capa de aplicación sobre TCP, puerto **23**. La **NVT** (*Network Virtual Terminal*) es un traductor común en ASCII de 7 bits con el octavo bit para control. Negociación con WILL, WONT, DO y DONT; sin acuerdo, se queda en la NVT estándar. Ejemplo: el comando IAC para negociar el eco (el servidor oculta lo que se teclea en una contraseña).

Es modular: extensiones como el RFC 856 (binario de 8 bits) y el 1091 (tipo de terminal). Su falla es la seguridad; hoy solo se usa en equipos viejos o redes locales y lo reemplazó **SSH** (RFC 4251, puerto 22).
Error común: confundir el documento, el protocolo y el programa cliente.

## 7. RFC 1034: DNS (equipo 5)
La arquitectura y especificación del sistema de nombres de dominio, que traduce nombres a direcciones IP (1984 según el equipo; ⚠️ el RFC 1034 es de 1987).

!!! En simple
La agenda telefónica de internet: escribes youtube.com y busca el número exacto, igual desde México que desde Japón. Límite: si cambias el número en la agenda central, tarda en propagarse a las copias en caché.

Capa 7, puerto **53**. Funciones: traducir nombres a IP, ser un estándar global de resolución y dar escalabilidad con una estructura jerárquica y distribuida (.com, .mx, .unam).

Ventajas: amigable, jerárquico y descentralizado (sin depender de un solo servidor, como en el caso de Japón). Desventajas: era vulnerable a ataques (mitigados con RFC posteriores), dependencia si cae un servidor y retrasos de propagación. Usos: navegadores, servidores como BIND y el enrutamiento de correo.

## Pendiente / próxima clase
- Las exposiciones terminan la siguiente clase (11 nov), con los equipos que faltan. Máximo 10 minutos por equipo.
- **Examen final: lunes 16 nov.**

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Los RFC expuestos: qué protocolo describen, sus estados, comandos y puertos.** en la Clase 17 el profesor dijo que el examen final incluye preguntas de los RFC; en esta clase no dictó temario de examen.
- **HTTP: métodos GET y POST y que el RFC 2616 solo describe la comunicación.** evidencia moderada: lo preguntó directamente al equipo de HTTP.
- **IMAP contra POP3 y el riesgo de depender de un servidor.** evidencia moderada: interrumpió para preguntar cuál recomiendan y lo ligó con la caída de bancos en Japón.
- **Protocolo, estándar y RFC no son lo mismo (LDAP / RFC 4510).** evidencia débil-moderada: preguntó «¿es un protocolo o es el RFC?».
- **Puertos bien conocidos y números de protocolo (TCP = 6, UDP = 17).** se repitieron en casi todas las exposiciones.

!!! Puntos clave
- HTTP/1.1 (2616): sin estado, persistente, métodos seguros e idempotentes, códigos 1xx–5xx; puerto 80.
- IMAP (3501): correo en el servidor, 143/993, cuatro estados. POP3 (1939): descarga y borra, 110/995, tres estados; DELE solo marca hasta QUIT.
- LDAP (4510): protocolo de directorio; el RFC es su hoja de ruta. Telnet (854): NVT, puerto 23, sin cifrado → SSH.
- IANA (1700 → 3232): TCP = 6, UDP = 17; puertos 20, 21, 22, 25, 53, 80. DNS (1034): puerto 53, jerárquico y distribuido.

## Ponte a prueba
1. **¿Cuáles son los cuatro estados de una sesión IMAP y con qué comando se avanza?** No autenticado (LOGIN) → autenticado (SELECT) → seleccionado → cierre (LOGOUT).
2. **Partes de un mensaje HTTP/1.1 y significado de los códigos 1xx a 5xx.** Línea inicial, cabeceras y cuerpo opcional; información, éxito, redirección, error del cliente, error del servidor.
3. **¿Por qué el RFC 2616 se reemplazó en 2014?** Porque era monolítico (176 páginas) y no precisaba cómo combinar módulos; se dividió en los RFC 7230–7235.
4. **¿Por qué LDAP es un «X.500 light» y en qué se distingue del RFC 4510?** X.500 exigía toda la pila OSI; LDAP es el protocolo y el RFC 4510 el documento que lo organiza.
5. **Paquetes con protocolo 6 y puertos 110 y 23: ¿qué son y qué los reemplaza?** TCP; POP3 sin cifrar (→ POP3S, 995) y Telnet (→ SSH, 22).
6. **POP3 con 3 correos: DELE 2, STAT, RSET y se corta la conexión antes de QUIT. ¿Qué pasa?** STAT da 2, RSET desmarca (vuelven a 3) y sin QUIT no hay actualización: quedan los 3 en el servidor.
7. **IMAP contra POP3.** IMAP (143/993): correos en el servidor, sincronizados, más almacenamiento y dependencia del servidor. POP3 (110/995): se descargan y se borran, pocos recursos, sin sincronización.
8. **¿Qué papel tiene la NVT en Telnet y por qué se usa SSH?** Traductor común en ASCII de 7 bits; SSH da las mismas funciones con cifrado y autenticación.
