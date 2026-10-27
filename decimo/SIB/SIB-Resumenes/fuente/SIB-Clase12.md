% materia: Seguridad Informática Básica
% titulo: Clase 12 · Clasificación y etapas de los ataques
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · jueves 8 oct 2026 · Tema 3 (3.1.3–3.1.4) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 3.1.3 Clasificación de los ataques
### Por intención
| Intencionados | No intencionados |
|---|---|
| Objetivo planeado y voluntad de dañar; planeación cuidadosa (no se arman en 3 horas como en las series) con personas, vehículos, dinero, pagos | Descuidos, negligencia, falta de conocimiento o accidentes |
| Ej.: secuestro planeado durante semanas | Ej.: que se te caiga el mole en la playera; apretar todos los botones por curiosidad |

### Por lugar
| Internos | Externos |
|---|---|
| Ocurren dentro del espacio físico o lógico del bien | Se originan lejos del bien |
| Ej.: mancharte con la comida que tú comes | Ej.: COVID-19 (surgió en China y se volvió local por contagios); intrusiones a la UNAM en julio desde el extranjero |
!!! Regla de examen
Todo ataque externo **tiene que seguir una ruta física o virtual para acercarse al bien y volverse interno**; si no lo logra, no hace daño.

### Por evidencia
| Pasivos | Activos |
|---|---|
| Solo observan, escuchan o leen, sin alterar nada | Evidentes; alteran o destruyen de inmediato |
| Ej.: ver de reojo tu patrón de desbloqueo en el metro; deducir gustos por la ropa; información regalada en redes | Ej.: un tallón al coche, la caída de una reja, el atentado a las Torres Gemelas |
!!! Los pasivos pueden ser más peligrosos
Como no se notan, pasan meses antes de reaccionar ("nunca me doy cuenta que se llevaron a cabo"). Ej.: con IA generativa se fabrican videos falsos de una persona a partir de las fotos que ella misma subió. Error común: pensar que si el sistema funciona bien, no hubo ataque.

## 3.1.4 Etapas de un ataque
| Etapa | Cuándo | Qué pasa |
|---|---|---|
| **1. Preparación o planteamiento** | Antes (la más larga) | Definir objetivo (p. ej. secuestrar una base con ransomware), reclutar personas (incluso empleados internos engañados), fijar fecha y hora, planes A… Z, calcular la ganancia en el mercado negro. Seguridad debe pensar como el atacante (reconocimiento de MITRE ATT&CK) y ponerle trabas de tiempo, dinero y esfuerzo |
| **2. Activación** | Durante | La acción que **dispara** el ataque: un script, un troyano, una bomba de tiempo, un puerto 22 abierto, reglas de firewall mal ordenadas. Si cambian las condiciones (la víctima cambia de ruta), nunca se activa |
| **3. Ejecución** | Después | **No** es atacar: es el **análisis de resultados**. El atacante evalúa si repetir; la organización analiza fallas y decide (comprar, reconfigurar, cambiar personal — p. ej. cambios en la UNAM tras las fallas en la admisión en línea) |
!!! Intencionado vs. no intencionado
**Intencionado: 3 fases** (preparación → activación → ejecución). **No intencionado: 2 fases** (activación → ejecución), porque no hay preparación. Tras tirarte el mole, en la ejecución aprendes a usar plato o mandil.
Error común: confundir la activación (el disparo) con la ejecución (el análisis posterior).

## 3.1.5 Ejercicio en equipo: "Incidente en SaludIntegral" (SIB-EC03)
**Escenario:** red de clínicas con lentitud en citas, accesos desde ubicaciones raras, cierres de sesión inesperados, correos con adjuntos extraños, accesos nocturnos a historiales con cuentas de médicos, tráfico a IPs externas, expedientes alterados y respaldos retrasados.
- **Preparación:** lucro (extorsión o venta de historiales), actores externos y personal sin capacitación; varios días en horario laboral. Mercado negro: un expediente médico vale **60–300 USD** en venta selectiva (contra ≈ 17 USD una tarjeta de crédito); en bases masivas ≈ 0.55–0.60 USD.
- **Activación:** correos con adjuntos en apariencia inofensivos (PDF) que al abrirse instalaron malware y abrieron puertos.
- **Ejecución:** balance de pérdidas y afectación a pacientes; monitoreo, aislar la red y reestructurar respaldos.
Error común: olvidar estimar recursos y ganancias en la preparación.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Clasificación | Opciones |
|---|---|
| Por intención | Intencionado (planeado) / no intencionado (descuido, accidente) |
| Por lugar | Interno / externo (que debe volverse interno para dañar) |
| Por evidencia | Pasivo (solo observa; puede ser el más peligroso) / activo (evidente, altera) |

!!! Etapas (examen)
Intencionado: **preparación → activación → ejecución**. No intencionado: **activación → ejecución**. La ejecución es el **análisis de resultados**, no el ataque en sí.

**Preparación:** objetivo, recursos, personas, fechas, planes, ganancia (expediente médico 60–300 USD). **Activación:** el disparo (adjunto, script, puerto abierto). **Ejecución:** evaluar y decidir.

# PARTE 3 · Mis apuntes de clase
~ Mis apuntes originales de este día (08/10/2026), tal cual los escribí.
```
Apuntes SIB clase 11 08/10/26


--Pizarron-
Clasificación de los ataques
a) Por el objetivo o la intención
	1.-Intencionado
	2.-No intencionado
b) Con base en el lugar donde se presentan
	1.-Internos
	2.-Externo
c)Por lo evidente que son
	1.-Pasivos -> (observación, lectura y escucha)
	2.-Activos
d) Por el flujo del bien
	1.-Modificación
	2.-Interrupción
	3.-Interacción
	4.-Suplantación/Falsificación


---Proyector---
Estapas o fases de un ataque
Un ataque intencionado contempla tres etapas o fases principales:

1.-Preparación o planteamiento: el método de ataque se plantea u otras preparaciones se realizan.
Esta etapa se lleva a cabo ANTES de que se presente el ataque.
Es en ella donde:
a) Se identifican objetivos
b) Se establecen los recursos humanos que participarán en el ataque
c) Se decide hora, fecha y lugar para llevarlo a cabo
d) Se diseña uno o varios planes alternativos por si el planteamiento prinicipal no sale como se esperaba
e) Se consideran los recursos monetarios para auspiciar dicho ataque
f) Se analizan otros recursos que intervendrán en el ataque (tiempo, medios de transporte, medios de comunicación, otros bienes como de cómputo, discos duros, usb, credenciales, vestuario etc.)
g) Se define lo que se ganará con el ataque o lo que se perderá en caso de no ser exitoso

2.-Activación: en esta etapa se realizan actividades que activan o disparan el ataque y por ende causan algún tipo de pérdida.
Dichas actividades pueden ser muy significaticas o insignificativas aparentemente, sin embargo, pueden causar que se generen daños de manera encadenada.
Esta etapa se lleva a cabo DURANTE el ataque.

3.- Ejecución: en esta etapa se observan los resultados de llevar a cabo el ataque. 
En esta etapa se lleva a cabo DESPUÉS del ataque.

Un ataque no intencionado solo tiene 2 fases: activación y ejecución.

Analizar el siguiente texto con las etapas anteriores, concluir y dar recomendaciones.
Incidente en "SaludIntegral"
-Red privada de clínicas y hospitales que gestiona expedientes médicos electrónicos, citas, y durante varios días, el sistema de citas presenta lentitud intermitente y acceso desde ubicaciones inusuales.
-Personal médico reporta cierres de sesión inesperados y archivos que tardan en abrir.
-Algunos equipos muestran actividad extraña después de revisar correos adjuntos.
-Se detectan accesos a historiales clínicos en horarios no habituales con cuentas legítimas.
Los servidores comienzan a intercambiar información de forma poco común.
-Aparece tráfico constante hacia direcciones externas desconocidas.
-Algunos expedientes presentan errores o cambios en sus nombres.
-Los respaldos se retrasan sin explicación clara.
-registros de actividad aparecen incompletos o desaparecen.
-Finalmente, sistemas críticos se vuelven inestables y afectan la intención a paciente. 
```
