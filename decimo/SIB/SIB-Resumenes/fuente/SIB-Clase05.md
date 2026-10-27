% materia: Seguridad Informática Básica
% titulo: Clase 5 · Los 6 servicios de seguridad a fondo y el fenómeno del bolero
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · jueves 10 sep 2026 · Tema 1 (1.4) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Seis servicios vs. el modelo OSI
- El estándar del modelo OSI contempla **5 servicios**: asume que la **disponibilidad** sale sola al tener autenticación, integridad, confidencialidad y control de acceso.
- La seguridad informática exige **6**: la disponibilidad se diseña a propósito (un equipo puede reiniciarse en pleno uso aunque haya control de acceso).
!!! Número del estándar
Los apuntes dicen "estándar 74"; al reconsultar el audio salió **7498** (ISO 7498-2, arquitectura de seguridad OSI).

## 2. Control de acceso y autenticación
- **Control de acceso:** permite o niega el paso de un bien (persona, proceso, dispositivo) a un área, servicio u otro bien. **Requiere autenticación previa.**
- **Autenticación:** comprobar que una entidad es quien dice ser; aplica a **personas, procesos, servicios, hardware y animales**. Ejemplos: chihuahua con señas específicas; gemelos o quintillizos con cicatrices o peinado.

## 3. Mecanismos de autenticación
| Categoría | Ejemplos | Notas |
|---|---|---|
| Algo que se **sabe** | Contraseñas, eventos pasados | Cambiar las de fábrica (admin123), rotar, no reutilizar; compartirla comparte la responsabilidad |
| Algo que se **tiene** | Lógico: inode, firma digital (~256 caracteres), extensión de archivo (doble extensión sospechosa). Físico: credencial, tarjeta | Transferible o duplicable |
| Algo que se **es** | Huella, iris; en procesos, un ID mutuamente excluyente | La huella antes se clasificaba como "algo que se tiene" |
**Biometría:**
- El rasgo debe ser estable en el tiempo (la huella se desgasta pero conserva su estructura).
- La **sangre no sirve** como biométrico continuo: se seca, cambia químicamente y el ADN se degrada.
- Sensores básicos se engañan con silicona o gel; los de **nivel de confianza 7** leen pulsaciones para verificar **tejido vivo**.

## 4. Confidencialidad y el fenómeno del bolero
- **Confidencialidad:** la información solo la ve el personal autorizado.
!!! Síndrome / fenómeno del bolero (examen)
**Minimizar la peligrosidad del entorno**: hablar o manejar información sensible creyendo que quien está cerca (bolero, personal de limpieza, gente del elevador) es inofensivo o no entiende.
- Llamadas en pasillos, elevadores y áreas de comida.
- Atacantes con uniforme (chaleco, escalera, empresa de energía) a quienes no se autentica.
- Espionaje pasivo de relevos y horarios para planear robos.
- Militares que publican rutas en Strava.
- **Egosurfing:** buscarse en buscadores; lo publicado persiste aunque se borre (visas, reclutamiento).

## 5. Integridad, también del factor humano
- Evita la modificación no autorizada de información e infraestructura **y** cuida la integridad de las personas que la operan.
- **Empleados descontentos:** la principal amenaza interna (borrar o alterar por venganza).
- Golpes en la cabeza o traumas de deportes de contacto (NFL, WWE) pueden causar conductas agresivas años después.

## 6. No repudio, disponibilidad y equilibrio
- **No repudio:** nadie puede negar la autoría de una acción: acuse de recibido, peritaje caligráfico, firma digital, logging de comandos de administradores.
- **Disponibilidad:** activos accesibles en los días y horarios estipulados; hay que definirlos con precisión.
- **Equilibrio operacional:** Liverpool: catálogo 24/7 sin autenticar; pago y Click and Collect con autenticación y no repudio.

## Ejercicio en parejas
Proponer mecanismos para los 6 servicios en la Facultad y en una casa.
| Facultad de Ingeniería | Casa |
|---|---|
| Torniquetes con QR en laboratorios | Wi-Fi de invitados |
| Cifrar BD de calificaciones | CCTV |
| Cerraduras electrónicas/biométricas | Respaldo local de documentos |
| HDMI alámbrico en proyectores (disponibilidad) | Control parental |
| Logging de `sudo` ligado a la llave SSH (no repudio) | UPS/generador y rejas |

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| OSI vs. seguridad | 5 servicios (disponibilidad automática) vs. 6 |
| Control de acceso | Siempre con autenticación previa |
| Autenticación | Personas, procesos, servicios, hardware, animales |
| Sabe / tiene / es | Contraseña / tarjeta, firma / huella, iris |
| Biometría fiable | Detecta que el sujeto está vivo (pulso); sangre no sirve |
| Integridad | Incluye al factor humano (empleados descontentos) |
| No repudio | No se puede negar la autoría |

!!! Fenómeno del bolero
Minimizar el riesgo del entorno al hablar de información sensible en público o frente a personal externo.
