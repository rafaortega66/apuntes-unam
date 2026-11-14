% materia: Seguridad Informática Básica
% titulo: Clase 20 · Costos en seguridad, procesos críticos, técnicas rápidas y matriz de riesgos
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · jueves 12 nov 2026 · Tema 5 (análisis y gestión de riesgos) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ La desigualdad de costos (ataque, bien y protección), gestión de riesgos con infraestructuras y procesos críticos y escenarios, cinco técnicas rápidas (What if, APR, cinco porqués, FMEA y checklist), la matriz de riesgos con NIST y un ejercicio individual sobre el salón.

!!! Fuente
Fuente: NotebookLM (audio `SIB-Clase20.m4a`), 14 nov 2026. Continúa la Clase 19.

## 1. Repaso y la regla de evidencias
Los alumnos recordaron lo de la Clase 19: cuantitativo contra cualitativo, activo, riesgo, aceptación y análisis, cada cuándo se hace, las tres preguntas, tablas de frecuencia, entrevistas, cuestionarios y checklists con apoyo de la dirección.

Insistió en guardar evidencia de todo: si todos los cuestionarios tienen la misma letra y tamaño, parece que el analista los llenó solo; ante «¿de dónde lo sacaste?», la evidencia prueba que no se inventó.

## 2. La desigualdad de costos en seguridad
**Costo del ataque > valor del bien > costo de la protección.** Al atacante le debe costar más (en dinero, tiempo y esfuerzo) que lo que obtendría, y la protección no debe costar más que el bien.

!!! En simple
Con una bici de 2,000 pesos quieres un candado que le cueste al ladrón más de 2,000 romper, pero no compras una caja fuerte de 50,000: «sale más caro el caldo que las albóndigas». Límite: las personas no tienen precio («priceless»).

**Dinero:** si para entrar a una base de datos de IBM el atacante paga 2,000 a cinco personas (10,000) y compra equipos de 23,000, pero la base se vende en 5,000 en el mercado negro, no le conviene. **Tiempo:** si quiere las direcciones de empleados que están hoy en un congreso, cualquier retraso frustra su objetivo.

Un celular de 10,000: robarlo debe costarle más de 10,000; pero si lo que hay dentro vale 20,000, sí le conviene.

En redes se inyecta tráfico aparente las 24 horas: si solo hubiera tráfico de 10 a.m. a 5 p.m., el atacante sabría cuándo atacar; con tráfico constante tendría que vigilar todo el día.

Gastar 50,000 o 100,000 en proteger ese celular no conviene. Excepción: las personas; un seguro de vida no devuelve a nadie, y perder a un empleado clave puede hacer que clientes cancelen contratos.

Por qué importa: Retoma la regla de la Clase 19: el control no puede costar más que el bien.
Error común: pensar solo en el dinero y olvidar el tiempo, el esfuerzo y el personal clave.

## 3. Gestión de riesgos: infraestructuras y procesos críticos y escenarios
**Gestión de riesgos:** administrar los riesgos detectados (quién los maneja y cómo se recupera la organización). **Infraestructuras críticas:** lo vital para que operen los procesos. **Procesos críticos:** actividades que no pueden dejar de hacerse. **Escenarios de riesgo:** descripción detallada de qué pasaría si se materializa un riesgo.

!!! En simple
En un restaurante: luz, agua y gas son la infraestructura crítica; cocinar y cobrar, los procesos críticos; imaginar qué hacer si se corta el agua a medio servicio, el escenario; decidir quién llama a la pipa, la gestión.

La gestión conecta con los planes de contingencia. En casa, la infraestructura crítica según los alumnos: internet (que depende de la luz), agua y gas.

**¿Qué no puede dejar de hacer McDonald's?** Refrigeración, registro de pedidos, preparación, inventarios, proveedores y cobranza. Destacó la **cobranza**: si regalan la Cajita Feliz, quiebran. Los procesos se jerarquizan por criticidad.

Los escenarios suponen lo peor (sin agua o sin gas) y describen todo: consecuencias, amenazas, vulnerabilidades y opciones (cerrar o contratar una pipa de emergencia).
Error común: escribir un escenario de una sola frase («se va el gas»).

## 4. Cinco técnicas rápidas para analizar riesgos
What if, Análisis Preliminar de Riesgos (APR), los cinco porqués, FMEA y listas de verificación.

!!! En simple
Cinco lupas para revisar una bici antes del viaje: ¿y si llueve?; anotar cómo están los frenos para comparar en tres meses; preguntar cinco veces por qué rechina la cadena; listar qué piezas fallan más y qué tan grave es; palomear una lista. Límite: en una empresa no se hace solo: se trabaja en grupo con perfiles distintos.

| Técnica | Qué es | Ejemplo de clase |
|---|---|---|
| **What if** | Preguntas hipotéticas encadenadas sobre eventualidades que solemos ignorar. | ¿Y si se va el gas? ¿Y si es una fuga? ¿Y si nadie contesta? ¿Y si contrato sin investigar a un atacante? |
| **APR** | Al inicio, detectar los problemas actuales para comparar antes y después (a los 3–4 meses o al año). | Registrar las fallas por escrito, no en pláticas junto al microondas. |
| **Cinco porqués** | **Exactamente cinco** «¿por qué?» sucesivos hasta la causa raíz (más de cinco ya no es la técnica). | Aparecieron cuentas de usuario creadas: ¿por qué nadie avisó?… |
| **FMEA** | Detectar, describir y clasificar fallas por frecuencia, gravedad y cómo se detectaron, para definir acciones. | Alguien da de alta usuarios sin avisar: ¿el jefe o un intruso con credenciales robadas? → reglas de quién da altas y a quién avisar. |
| **Checklist** | Lista detallada verificada con Sí / No. | En auditorías se desglosa cada punto en incisos (5.1.3 inciso A, B…). A algunos no les gusta por escueta. |
Error común: usar más o menos de cinco preguntas y llamarlo cinco porqués; checklists ambiguos sin incisos; comunicar riesgos de palabra; analizar en solitario.

## 5. La matriz de riesgos (enfoque NIST)
Tabla donde el nivel de riesgo = **probabilidad × impacto**, con rangos numéricos asociados a colores.

!!! En simple
Un semáforo en cuadrícula: cruzas qué tan seguido pasa contra qué tanto duele; casi nunca y no duele, verde; seguido y catastrófico, rojo. Límite: la matriz formal necesita la fórmula, rangos excluyentes y una definición escrita de cada nivel.

**Colores NIST:** rojo = alto, amarillo = moderado (naranja si hace falta un cuarto nivel), verde = muy bajo. Se pueden usar otros colores, pero en un informe formal conviene NIST.

Ejemplo 5×5: probabilidad 1–5 por impacto 1–5 (5 × 1 = 5, hasta 25). La escala 1–5 es común, no obligatoria (2–10, 10–50, 1–100).

| Rango | Nivel | Significado |
|---|---|---|
| 1 a 5 | Bajo (verde) | Probablemente no pase y, si pasa, sin consecuencias significativas. |
| 6 a 12 | Medio (amarillo) | Molestia, contratiempos. |
| 15 a 25 | Alto (rojo) | Consecuencias graves (pérdida de personas o de la organización). |

Un alumno preguntó si dentro del mismo rango se pueden usar tonos más claros y más fuertes del mismo color: sí, mientras sea el mismo nivel.

**Errores en matrices de internet:** rangos traslapados (1–5, 5–12, 10–25: el 5 y el 10 caen en dos niveles); el mismo número pintado de distinto color en celdas distintas; mostrar solo palabras y colores sin los números.
Error común: los tres anteriores.

## 6. Ejercicio individual: análisis de riesgos del salón
Actividad de una hora en hoja blanca («Ejercicio de clase», fecha 12, nombre y número de cuenta) sobre el propio salón.

1. Definir los procesos críticos del salón.
2. Al menos 5 activos (las personas cuentan, con su función).
3. Al menos 2 amenazas y 2 vulnerabilidades por activo (pueden repetirse).
4. Al menos 2 escenarios de riesgo; elegir uno y plantear las preguntas de una técnica (What if, checklist o exactamente 5 porqués, sin responder).
5. La matriz de riesgos del escenario (sin plumas de color, anotar el color entre paréntesis).

La matriz depende del contexto: no es igual que falte gas en una casa que en una panadería.

## Pendiente / próxima clase
- La profesora ya publicó en Classroom las metodologías de análisis de riesgos.
- Repasar análisis de riesgos y matrices: la próxima clase hay un ejercicio práctico completo.
- **Examen:** todo el contenido; en la última semana (martes o jueves), por definir si en equipo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **La desigualdad de costos: ataque, valor del bien y protección.** la proyectó, la ligó con el tiempo, dinero y esfuerzo de la clase anterior y la ilustró con números.
- **Construir una matriz de riesgos (probabilidad × impacto, rangos excluyentes) y detectar sus errores.** fue el bloque central, entró en el ejercicio y anunció otro ejercicio de esto.
- **Las cinco técnicas rápidas: What if, APR, cinco porqués, FMEA y checklist.** las explicó con ejemplos y pidió desarrollar una en el ejercicio.
- **Infraestructuras críticas, procesos críticos y escenarios de riesgo.** hizo un ejercicio participativo (casa, McDonald's) y fueron los primeros incisos del ejercicio.
- **Evidencia en el análisis y el examen final completo.** repitió la regla de evidencias y pidió ir estudiando todo.

!!! Puntos clave
- Costo del ataque > valor del bien > costo de la protección; las personas no tienen precio.
- Infraestructura crítica → procesos críticos (jerarquizados) → escenarios descritos a detalle → gestión.
- What if, APR (antes y después), cinco porqués (exactamente 5), FMEA (frecuencia, gravedad, detección), checklist (Sí/No con incisos).
- Matriz: probabilidad × impacto; colores NIST; rangos sin traslape (1–5 verde, 6–12 amarillo, 15–25 rojo); siempre con números.

## Ponte a prueba
1. **Escribe la desigualdad de costos y su excepción.** Costo del ataque > valor del bien > costo de la protección; excepción: las personas.
2. **¿Por qué se inyecta tráfico aparente las 24 horas?** Para que el atacante no sepa cuándo atacar y le cueste más tiempo vigilar.
3. **¿Qué proceso de McDonald's destacó la profesora y por qué?** La cobranza: si regalan la comida, quiebran aunque todo lo demás funcione.
4. **¿Cuántas preguntas tiene la técnica de los cinco porqués?** Exactamente cinco.
5. **¿Para qué sirve el APR?** Para registrar al inicio los problemas actuales y comparar antes y después.
6. **¿Qué está mal en una matriz con rangos 1–5, 5–12 y 10–25?** Se traslapan: el 5 y el 10 caen en dos niveles.
7. **Probabilidad 3 e impacto 4 en la matriz de clase: ¿nivel?** 12 → medio (amarillo).
