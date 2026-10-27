% materia: Administración de Servicios de Internet
% titulo: Clase 5 · Formatos Scrum/Cascada, requisitos técnicos y los 10 proyectos
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · miércoles 9 sep 2026 · Proyecto final · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Scrum: formatos y seguimiento
- Actualización **cada 8 días** (por sprint) con un **incremento potencialmente entregable**. Cambiar "Hola Mundo" por "Hola Mundo Juan" **no** cuenta.
- Cada equipo eligió líder de proyecto en 5 minutos.
| Formato | Qué contiene |
|---|---|
| Ficha de inicio y visión del producto | Objetivos y meta final |
| Product Backlog | Historias y requerimientos priorizados |
| Historias de usuario + criterios de aceptación | Prioridad Alta/Media/Baja (estacionamiento: "Registrar el vehículo", "Consultar espacios", "Calcular el costo") |
| Sprint Backlog | Elementos del sprint en curso |
| Diario de experimentos | Juntas, acuerdos y bloqueos (licencias, configuración) |
| Sprint Review y Retrospective | Revisión del incremento y mejoras |
| Evidencias del incremento | Código, capturas, repositorios |
- También **Gantt** con término a mediados de noviembre.
- **Git obligatorio: mínimo 2 commits por semana por integrante.**

## 2. Cascada / PMBOK
- Alcance y requerimientos documentados **desde el inicio**; sin cambios arbitrarios (no cambiar una red neuronal por un chatbot a medio semestre). Cambio justificado = **Control de Cambios** con impacto documental y financiero.
- Solo **3 revisiones**: inicial, intermedia y final. Evita el "ya casi acabo".
- Documentos: problema, objetivos y alcances; factibilidad o estado del arte; **RF y RNF** (RF1 registrar entrada, RF2 registrar salida, RNF1 tiempo máximo de respuesta); casos de uso; diseño y BD; plan y casos de prueba; control de cambios.
- **Se excluye el Acta de Inicio** en este curso.

## 3. Requisitos técnicos para todos
!!! Infraestructura mínima
**2 a 3 máquinas virtuales.** Servidor (Ubuntu Server o Windows Server) y cliente del **sistema operativo contrario** (Windows Server ↔ cliente Linux; Ubuntu Server ↔ cliente Windows). Red, servicios, seguridad e integración.

## 4. Los 10 proyectos
| Proyecto | Alcance | Equipo |
|---|---|---|
| Intranet empresarial | DNS interno, Apache con virtual hosts, HTTPS | 4 (Scrum) |
| Correo empresarial | DNS propio, SMTP, POP3, IMAP | 3 |
| Acceso remoto seguro | SSH y SSL; usuarios y grupos | 5 |
| Servidor de archivos | Samba o NFS; grupos por departamento; rwx; **solo CLI** | 9 |
| Web con BD | PHP/Java/Python + BD (SQL Server prohibido); DNS (no localhost:8080); CRUD | 7 (Scrum) |
| Web con balanceo | Proxy inverso Apache/Nginx entre Web 1 y Web 2; espejo de alta disponibilidad | 1 |
| **Servicios para una escuela** | **DHCP y DNS, página informativa, Samba** | **10 (el mío)** |
| Web HTTPS | SSL/TLS, redirección HTTP → HTTPS, 2FA | 8 |
| Archivos y acceso multi-cliente | Samba, NFS, SSH, SFTP en Windows y Linux | 6 |
| Proxy y control de accesos | Reglas estrictas; triggers de bitácora (usuario, fecha, hora, método, acciones) | 2 |

## 5. Entregables y evaluación
- **Manual Técnico** (red, SO, comandos, archivos de configuración), **Manual de Usuario** y **video de máximo 15 min** con instalación y configuración en vivo.
- Sin exposiciones grupales. Revisión en la mesa del profesor con las VMs funcionando ("afuera sí jalaba" no vale).
- Pregunta individual al azar: si no responde, **reprueba todo el equipo**.

## 6. Reglas administrativas
- Proyecto individual permitido, mismo alcance; avisar a más tardar la siguiente clase.
- Cambio de tema por Classroom a más tardar el viernes, justificado y con 2–3 VMs (el Equipo 3 no puede). Sin propuesta, el tema queda definitivo.

## Pendiente
Ficha de inicio y visión (Scrum) o requerimientos (Cascada) del tema asignado.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| | Scrum | Cascada |
|---|---|---|
| Ritmo | Cada 8 días, incremento real | 3 revisiones |
| Documentos | Ficha, backlogs, HU, diario, review/retro, evidencias, Gantt | RF/RNF, casos de uso, diseño, pruebas, control de cambios (sin Acta de Inicio) |
| Control | 2 commits/semana en Git | Control de cambios formal |

!!! Para todos
2–3 VMs con SO cruzado. Entrega final: Manual Técnico, Manual de Usuario, video ≤ 15 min. Pregunta al azar: si falla uno, reprueba el equipo. Equipo 10: escuela (DHCP, DNS, web, Samba).
