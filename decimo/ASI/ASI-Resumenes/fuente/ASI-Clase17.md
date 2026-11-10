% materia: Administración de Servicios de Internet
% titulo: Clase 17 · Cierre de exposiciones, estándares RFC y calendario de fin de semestre
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · miércoles 4 nov 2026 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Últimas exposiciones de «el empleo del futuro» (agricultura, taller automotriz, veterinaria y soporte de TI), el debate sobre calidad contra cantidad de datos, la asignación de un RFC por equipo y el calendario del final del semestre. Continúa la Clase 16.

!!! Fuente
NotebookLM (audio ASI-Clase17.m4a). Fue una sesión de presentaciones y avisos; no se anotan nombres de compañeros. Lo que no se pudo contrastar con el audio se marca como dudoso.

## 1. Los estándares RFC
- **RFC (Request for Comments):** documentos oficiales (del IETF) que describen las reglas, especificaciones, comportamientos y protocolos para implementar y comunicar servicios de Internet.
- El profesor aclaró con sarcasmo que aquí RFC **no** es el Registro Federal de Contribuyentes.
- El temario de la materia es 100% teórico y se apoya en los RFC (por eso metió prácticas de Linux, para no caer en la monotonía).
!!! Examen
«En el examen voy a añadir lo de los RFC… si observan cada una de las unidades del temario habla del RFC: 2081, 1939, 3501…»: el documento que describe las reglas y el protocolo.
### Asignación por equipo (10 a 15 minutos cada uno)
| Equipo | RFC |
|---|---|
| 1 | 1939 (POP3) |
| 2 | 2821 / 2081 (dudoso: SMTP o RIPv2) |
| 5 | 1034 (conceptos del DNS) |
| 6 | 3898 / 3501 (dudoso: IMAP4rev1) |
| 7 | 4511 / 451 (dudoso: LDAP) |
| 8 | 2616 (dudoso: HTTP/1.1) |
| 9 | 8446 (TLS 1.3) |
| 10 | 1700 (números y parámetros asignados; confirmado por el PDF del equipo) |
### Estructura obligatoria de la exposición
1. Identificar el estándar y el tipo de documento.
2. Decir si administra, protege o diseña un servicio de red.
3. Describir la arquitectura del protocolo, sus reglas y el modelo de comunicación entre extremos.
4. Dar un ejemplo técnico de su funcionamiento.
Error común: instalar paquetes sin conocer los mensajes de control que define el RFC.

## 2. Exposiciones del empleo del futuro (cierre)
- **Agricultura:** sensores de campo (embebidos), tablero web y marketing con IA generativa para pequeños productores. El profesor cuestionó la **página web**: en el campo se usa una **aplicación móvil nativa** (Flutter y Dart); «¿has comprado por Amazon abriendo Chrome o abres la app?». También notó que el proyecto se enfocó en ventas y descuidó la operación del agricultor (como drones de aspersión).
- **Diagnóstico automotriz con IA:** el mecánico conecta el escáner OBD, la IA correlaciona códigos y síntomas, propone comprobaciones, descarta ramas si la falla persiste y aprende de la solución. Contra-argumento del profesor: si es tan fácil, los dueños comprarán su propio escáner; el nicho está en quienes mantienen las bases de conocimiento.
- **IA en veterinaria:** diagnóstico de radiografías y redacción de informes. Contraste **SaaS/nube** (suscripción, poco cómputo local, depende de internet) contra **despliegue local** (inversión alta en servidores y GPU, autonomía ante caídas). El criterio del médico es irremplazable (empatía, decisiones éticas, riesgo de alucinación y sesgo).
- **Soporte de TI autónomo:** mantenimiento predictivo, resolución automática de tickets, aislamiento inmediato de equipos comprometidos y aprovisionamiento de empleados. Riesgos: falsos positivos, punto central con credenciales críticas y resistencia de los técnicos.

## 3. Calidad contra cantidad de datos
!!! Examen
Debate: no es cierto que a más datos siempre haya más precisión. «Lo que te da la precisión es la calidad»; hace falta un **protocolo** riguroso de captura y validación.
- Ejemplo del profesor: contactos del teléfono incompletos o con apodos arruinan la estructura de una base de datos (*garbage in, garbage out*).

## 4. El auditor de procesos y algoritmos
- Ante la automatización de mesas de ayuda y los despidos de operadores, el puesto que sí le llamó la atención es el de **auditor de TI**: vigila que procesos, documentación, ética y modelos automatizados cumplan las políticas de la organización.

## Contexto — no examen
- El «seis» que ofreció el primer día a quien quisiera desentenderse, y las peticiones de puntos por «regalo de graduación» o Navidad.
- Un alumno justificó su propuesta con un video de un productor japonés de matcha que no sabía vender.
- El comercio informal en las facultades, controlado por plazas y horarios.
- Alias en los nombres de entrega de Classroom por usar la misma cuenta que en YouTube.
- Empresas que despiden equipos completos esperando que la IA absorba los tickets.

## Pendiente (calendario)
- **Lunes 9 y miércoles 11 nov:** exposiciones de los RFC (10 a 15 min por equipo), formato libre, entrega digital en Classroom.
- **Lunes 16 nov: examen final**, individual, en hoja suelta, con código y teoría (incluidos los RFC asignados), sin celular.
- **Miércoles 18 nov:** sin sesión presencial; el profesor revisa exámenes y prácticas.
- **Viernes 20 nov: entrega del proyecto final.**
- **Semana del 23 al 27 nov:** revisión de actas y aclaraciones; un rol de atención divide al grupo (lunes 23 y miércoles 25).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Tema | Idea para recordar |
|---|---|
| RFC | Documento que describe reglas, comportamiento y protocolo; entra al examen |
| Exposición del RFC | Estándar, qué administra o protege, arquitectura y reglas, ejemplo |
| App vs web en campo | Se usa la app móvil nativa (Flutter y Dart) |
| Datos | La calidad y el protocolo de captura importan más que la cantidad |
| SaaS vs local | Suscripción y dependencia de internet vs inversión y autonomía |
| Auditor de TI | El puesto que crece tras automatizar el soporte |
| Examen final | 16 nov, individual, en papel, sin celular |

!!! Hilo conductor
Los servicios de Internet se rigen por RFC que hay que entender, no solo instalar; y con la IA automatizando tareas, lo que vale es la calidad de los datos, el despliegue adecuado y quien audita.
