% materia: Administración de Servicios de Internet
% titulo: Clase 3 · Qué es un servidor, CIA, requerimientos y costos en Azure
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · miércoles 2 sep 2026 · Tema 1 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Metodologías confirmadas
- **PMBOK/Cascada:** equipos 2, 5 y 6. **Scrum:** 1, 3, 4, 7, 8, 9 y 10 (reportes semanales de sprint y bitácora de dailies de 15 min).
- **Cambiar de metodología a mitad del semestre = reprobación automática.**

## 2. Qué es un servidor
- Definición circular (incorrecta): "dispositivo dentro de un modelo cliente-servidor…".
- Correcta: **computadora con hardware especial y alta potencia** que comparte recursos de software, hardware y dispositivos.
- No es servidor cualquier PC que comparte una carpeta (ni una laptop con 1 TB y 16 GB).

## 3. Pirámide DIC y repositorio vs. servidor
| Nivel | Qué es | Ejemplo (redes sociales) |
|---|---|---|
| **Datos** | Lo que guarda un repositorio | Búsquedas de 1 a 3 AM |
| **Información** | Datos con **contexto** para el usuario | Patrón de "consumo nocturno" |
| **Conocimiento** | Información + matemáticas, algoritmos, estadística → decisiones | Publicidad en esa ventana |
- **Repositorio** (GitHub): guarda archivos pero **no los ejecuta**. **Servidor:** almacena y **ejecuta** (scripts, redes neuronales, IA). En un SGBD, las consultas corren en el servidor; la PC local es solo cliente (IP y credenciales).
- **No requiere Internet:** puede operar en una Intranet (cable cruzado, ping, SSH).

## 4. Definición formal y tríada CIA
Cualquier proceso que procese y comparta recursos o haga **CRUD** para otros equipos actúa como servidor. Reto central: **alta disponibilidad**.
| Pilar | Definición | Ejemplo |
|---|---|---|
| Disponibilidad | Servicios y datos siempre accesibles | Infraestructura redundante |
| Integridad | Datos exactos y sin alteraciones | Si tengo $75, al reconsultar sigo con $75 |
| Confidencialidad | Solo usuarios autorizados | Privilegios, cifrado |
Los mensajes se fragmentan en tramas; pilas y colas los reensamblan completos (integridad).

## 5. Tipos de servidor y puertos
Web, archivos (FTP), correo, base de datos, autenticación. Puertos: **80 HTTP, 443 HTTPS, 22 SSH**.

## 6. Requerimientos
| Tipo | Qué define |
|---|---|
| **Funcional** | Qué hace el sistema (entradas, salidas, procesos) |
| **No funcional** | Calidad: rendimiento, tiempo de respuesta, seguridad, usabilidad |
| **De sistema** | Hardware, red, servidores |
!!! Ejercicio resuelto en clase
Loguearse antes de entrar → **funcional**. Respuesta muy corta → **no funcional**. Varios servidores para disponibilidad → **de sistema**. Ancho de banda para streaming → **de sistema**. Enviar informe semanal por email → **funcional**. Interfaz sencilla → **no funcional**.

## 7. Azure: servicios y costos
- Active Directory con grupos; VMs (Ubuntu Server, Oracle Linux, Windows Server): más seguridad o cómputo = más costo; reglas de entrada en 80, 443 y 22.
- **No hay tarifa fija:** consumo, almacenamiento (bodega barata vs. departamento caro), frecuencia de acceso (frío: guardar barato, leer caro) y seguridad de enrutamiento. Todo en **USD**.
- **Alerta prevista (forecasted):** cuando la proyección alcanzará el umbral. **Alerta de costo real:** cuando el gasto real lo toca.
- Caso: una papelería llegó a **$45,000 USD** en marzo porque el hijo del dueño migró a la nube sin alertas.

## Pendiente: tarea Avante Textil
Una cuartilla individual: giro y Capital Humano; requerimientos funcionales, no funcionales y de sistema; recomendar Azure, AWS o Google Cloud con justificación; costos en USD si se puede. Lunes antes de las 17:00 en Classroom.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Servidor | Computadora especial que comparte y **ejecuta**; no necesita Internet |
| DIC | Datos → información (contexto) → conocimiento (algoritmos) |
| CIA | Disponibilidad, integridad, confidencialidad |
| Requerimientos | Funcional (qué), no funcional (qué tan bien), sistema (con qué hardware) |
| Puertos | 80, 443, 22 |
| Nube | Sin tarifa fija; alertas prevista y real |
