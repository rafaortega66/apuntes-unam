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
