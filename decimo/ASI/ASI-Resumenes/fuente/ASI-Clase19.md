% materia: Administración de Servicios de Internet
% titulo: Clase 19 · RFC 3898 (NIS en DHCPv6) y RFC 8446 (TLS 1.3)
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · miércoles 11 nov 2026 · Exposiciones de los RFC (2.ª parte) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Últimas exposiciones de RFC: el 3898 (opciones de NIS y NIS+ para DHCPv6) y el 8446 (TLS 1.3: handshake de 1-RTT, AEAD con AES-GCM y claves efímeras), actividad en clase y fechas: examen el miércoles 18 y presentación del proyecto el 23 y 25 nov.

!!! Fuente
Fuente: NotebookLM (audio `ASI-Clase19.m4a`, 19 min), 14 nov 2026. El contenido técnico es de los equipos; el profesor no intervino durante las exposiciones.

## 1. RFC 3898: opciones de NIS y NIS+ para DHCPv6
DHCP configura automáticamente los parámetros de red; NIS (*Network Information System*) administra la información de una red. El RFC 3898 (octubre de 2004) define cómo DHCPv6 entrega los datos para localizar servidores NIS y NIS+.

!!! En simple
Llegas a una oficina nueva y, en vez de que un técnico te anote a mano dónde está el archivo central de usuarios, tu computadora se lo pregunta al encargado de asignar escritorios (DHCPv6) con unos códigos del 27 al 30. Límite: el encargado no te da esos datos si no los pides explícitamente, y todo viaja sin cifrar.

| Opción | Entrega |
|---|---|
| 27 | Direcciones IP de servidores NIS |
| 28 | Direcciones IP de servidores NIS+ |
| 29 | Nombre de dominio NIS |
| 30 | Nombre de dominio NIS+ |

Cada opción indica tipo, longitud y contenido, y puede llevar varias direcciones (más disponibilidad). Suelen ir en pares (27 y 29, 28 y 30); si el cliente ya conoce la IP, puede pedir solo el dominio, o al revés.

1. El cliente envía una solicitud de búsqueda incluyendo los códigos 27–30.
2. El servidor responde con un anuncio (su identificador, servidores disponibles y la posible IP).
3. El cliente envía la petición formal y debe **volver a incluir** los códigos.
4. El servidor devuelve la información.

El RFC no implementa NIS: solo es el transporte por DHCPv6. Por su inseguridad (puede dirigir a servidores falsos y manda contraseñas sin cifrar), hoy se usa LDAP o Active Directory.
Error común: creer que DHCPv6 manda los datos de NIS sin pedirlos, o que basta pedirlos una vez; creer que el RFC implementa NIS.

## 2. RFC 8446: TLS 1.3
Especificación de la IETF de TLS 1.3 (sucesor de SSL), que reemplaza a TLS 1.2 (RFC 5246) para dar confidencialidad, integridad y autenticación entre cliente y servidor.

!!! En simple
Es el manual común de todos los bancos y navegadores para presentarse, comprobar con una identificación oficial que el banco es quien dice y abrir un canal privado en un solo saludo de ida y vuelta.

Interoperabilidad: cualquier navegador (Chrome, Firefox, donde ya es la versión recomendada) habla con cualquier servidor. Tres pilares contra el *man-in-the-middle*: confidencialidad, integridad y autenticación con certificado digital.

**Handshake:** TLS 1.2 necesitaba 2 RTT; TLS 1.3 solo **1 RTT**, e incluso un modo sin espera (0-RTT) donde los primeros datos quedan algo más expuestos. En una transacción bancaria por API REST, primero se acuerda el cifrado (AES-GCM) y las claves efímeras y el servidor presenta su certificado.

Eliminó algoritmos inseguros: MD5, SHA-1 y RC4.

**AEAD** (*Authenticated Encryption with Associated Data*): cifra y autentica a la vez. AES-GCM combina el contenido y el encabezado para producir un *authentication tag*; el servidor recalcula y compara, y si cambió un solo bit (por ejemplo el monto de una transferencia) descarta y cierra la conexión. Analogía del equipo: además de la caja fuerte, un sello de cera que se rompe si alguien la abre.

**Perfect forward secrecy:** claves efímeras por Diffie-Hellman que solo existen durante la sesión y se borran de la RAM al terminar; aunque alguien haya grabado el tráfico, después ya no puede descifrarlo (con claves estáticas sí podía).

Por qué importa: Es el estándar actual para la banca en línea y las APIs.

## Pendiente / próxima clase
- Actividad (infografía) para entregar ese día.
- **Lunes 16 nov: no hay clase.**
- **Miércoles 18 nov: examen** (cambia la fecha del 16 que se había dicho en la Clase 17).
- **Lunes 23 y miércoles 25 nov:** presentación del proyecto por número rifado, con preguntas y cambios en tiempo real; quien expone un día puede faltar el otro.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Presentación del proyecto (23 y 25 nov): preguntas técnicas y cambios en tiempo real.** el profesor dijo que hará preguntas y pedirá cambios en vivo, y pidió ponerse a estudiar.
- **RFC 8446 / TLS 1.3: 1-RTT, algoritmos eliminados, AEAD y claves efímeras.** evidencia débil para el examen escrito: fue el estándar más extenso de la sesión, sin comentarios del profesor.
- **RFC 3898: opciones 27–30 y el flujo de cuatro pasos.** evidencia débil: completa los RFC expuestos antes del examen.

!!! Puntos clave
- RFC 3898: DHCPv6 transporta los datos de NIS/NIS+ (opciones 27–30); obsoleto por inseguro (→ LDAP, Active Directory).
- TLS 1.3: 1-RTT, sin MD5/SHA-1/RC4, AEAD con AES-GCM, claves efímeras (forward secrecy).
- Examen: miércoles 18 nov. Proyecto: 23 y 25 nov con cambios en vivo.

## Ponte a prueba
1. **¿Qué entregan las opciones 27, 28, 29 y 30 del RFC 3898?** IP de NIS, IP de NIS+, dominio NIS y dominio NIS+.
2. **¿Por qué el cliente pide los códigos dos veces?** Porque el servidor no los entrega por defecto: van en la solicitud inicial y otra vez en la petición formal.
3. **¿Cuántos viajes de ida y vuelta necesita el handshake de TLS 1.2 y de TLS 1.3?** 2 RTT contra 1 RTT.
4. **¿Qué es AEAD y qué pasa si se altera un bit?** Cifrado autenticado (AES-GCM): el tag no coincide y el servidor descarta y cierra la conexión.
5. **¿Qué es el perfect forward secrecy?** Claves efímeras Diffie-Hellman que se borran al terminar la sesión; el tráfico grabado no se puede descifrar después.
