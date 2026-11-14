% materia: Seguridad Informática Básica
% titulo: Clase 19 · Análisis de riesgos: terminología, métodos y los ocho pasos
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · martes 10 nov 2026 · Tema 5 (análisis de riesgos) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Inicio del análisis de riesgos: las tres preguntas en orden, terminología, cómo recopilar información, riesgo residual y pérdidas esperadas, análisis cuantitativo (ALE) y cualitativo, los ocho pasos del proceso, cada cuándo se hace y la matriz FODA.

!!! Fuente
Fuente: NotebookLM (audio `SIB-Clase19.m4a`), 14 nov 2026. Continúa la Clase 18.

## 1. Las tres preguntas y la terminología
El análisis de riesgos detecta problemáticas y qué tan seguido pueden pasar, respondiendo en orden: **1) ¿qué quiero proteger?, 2) ¿de qué lo quiero proteger? y 3) ¿cómo lo voy a proteger?** **Aceptación:** el dueño decide si está dispuesto a que pase y asume las consecuencias. **Manejo:** cómo controlar y minimizar los riesgos que no se aceptan. **Evaluación:** comparar con metodologías, tablas o análisis previos. **Pérdidas esperadas:** suponer siempre lo peor.

!!! En simple
Es revisar tu casa antes de un viaje: qué cosas valiosas tienes, qué les podría pasar, y si pones chapas o un seguro, sin gastar 50,000 pesos en un candado para una bici de 2,000. Límite: en casa decides de memoria; en una organización hay tablas, el último análisis documentado, costos y el respaldo de la alta dirección.

Los alumnos recordaron «¿qué?» y «¿cómo?»; la profesora corrigió el orden: cambiarlo lleva a comprar herramientas antes de conocer el problema.

Se identifican bienes y riesgos (posibilidad de daño y frecuencia) y se arman tablas métricas: frecuencia al año (0 = ninguna en verde; 1–10, 11–20…), qué es más caótico y pérdidas en dinero. Cinco incidencias al año pueden ser extremas en una empresa donde casi nunca pasa nada. Si la empresa ya tiene tablas, se usan esas.

Si no se acepta el riesgo, se maneja, y la regla de oro es que **el manejo no puede costar más (en tiempo, dinero y esfuerzo) que el bien**. Excepción: bienes sin precio de reposición, como una persona, para los que hay seguros de gastos médicos mayores.

Para evaluar: si nunca se ha hecho un análisis, se parte de cero; si hay varios, se toma **el último**, no el primero.

Problemas reales: lo piden «para ayer», la gente miente al dar información y hace falta el apoyo («el amor») de la alta dirección.

Por qué importa: Resume el semestre y alimenta las políticas (Clase 17) y los planes de contingencia (Clase 18).
Error común: cambiar el orden de las preguntas; tomar el primer análisis histórico; gastar más en el control que en el bien.

## 2. Recopilar información y el apoyo de la alta dirección
Entrevistas, cuestionarios (impresos o digitales) y listas de verificación para recabar datos reales de la organización.

!!! En simple
Si a un familiar mayor le preguntas «¿qué vulnerabilidades de capa de aplicación tiene tu sistema?», no te entiende; si le preguntas «¿se te apaga o se traba?», te da información útil.

- Lenguaje amigable según quién responde: preguntar qué problemas tiene con su PC, no por «ciberataques».
- Cuestionarios fluidos y cortos: las primeras 10 preguntas se contestan con ganas; después de la 20, al azar.
- No dejar el formulario días sin seguimiento (lo olvidan o lo contesta otra persona).
- Evitar preguntas sesgadas: rangos sin la opción cero o «menos de 10», sin «Otro (especifique)», o preguntas obligatorias que no aplican.

«La piedrita en el zapato»: la alta dirección debe emitir un oficio o hacer una junta autorizando la colaboración, con avisos de privacidad y confidencialidad. Si no respalda ni actúa, la empresa reaccionará con «el agua hasta el cuello» y cometerá errores como despedir gente sin quitarle el acceso remoto (los ataques más exitosos vienen de internos).
Error común: usar tecnicismos; cuestionarios eternos o con rangos cerrados; dejar que otro conteste; empezar sin oficio de la dirección.

## 3. Riesgo residual y pérdidas esperadas
El **riesgo residual** es el riesgo mínimo que queda después de aplicar controles y que el dueño acepta. Las **pérdidas esperadas** obligan a imaginar el peor escenario antes de que ocurra.

!!! En simple
Vacunarte es un control: aceptas el riesgo residual de un resfriado leve para no terminar intubado. Un seguro que te devuelve el 80 % te deja un riesgo residual del 20 %.

Sin controles asumes el 100 % de la pérdida. Nunca hay que subestimar el peor escenario ni avisar de palabra: si un servidor ya no admite actualizaciones, el analista debe advertirlo **por escrito y con sello**, o después le reclamarán «¿por qué no me avisaste?».

Ilustró «suponer lo peor» con casos de imprudencias fatales, accidentes sin seguro y la falta de exámenes médicos o perfiles psicológicos al contratar; también los costos de las reacciones no planificadas en una emergencia (romper una ventana con una silla).
Error común: decir «no pasa nada»; avisar riesgos graves solo de palabra; contratar sin exámenes por amistad.

## 4. Análisis cuantitativo (ALE) contra cualitativo
**Cuantitativo:** números, porcentajes, costos, fórmulas, tablas y gráficas; incluye la **ALE** (expectativa de pérdida anual), cuánto se perdería en un periodo y el costo de reponer. **Cualitativo:** cualidades sin cálculos, con colores, figuras o palabras.

!!! En simple
En el doctor, el cuantitativo es tu análisis de sangre («140 de glucosa, el tratamiento cuesta 2,500»); el cualitativo es el semáforo («estás en amarillo»). Límite: a un directivo, «foco rojo, carita triste» no le basta para aprobar presupuesto: necesita saber si son 10 pesos o un millón de dólares.

A la empresa no le sirve «tu pérdida será extrema» sin saber de cuánto se habla. Ejemplos de pérdidas mal estimadas: el Pontiac Aztek (abarataron el interior; en 2003 seguían sin vender más del 80 % de las unidades), el último vocho de Puebla con llantas cara blanca y Windows 8.

Cualitativo: verde = sin eventualidades, amarillo = en 1 o 2 áreas, rojo = en más de 3 (como las banderas de las playas); caritas; o palabras (alto, medio, bajo; nada, poco, muy o extremadamente sensible).

**Se usan juntos:** el cualitativo para lo que no tiene precio y para leer rápido; el cuantitativo para los costos reales, incluidos los ocultos (una falla que debía tomar 5 minutos y toma una hora porque olvidaron la contraseña).

Por qué importa: Prepara la matriz de riesgos con NIST de la siguiente clase.
Error común: entregar solo etiquetas cualitativas a directivos; creer que los métodos se excluyen.

## 5. Los 8 pasos del análisis de riesgos y el informe
Secuencia obligatoria cuando no se sigue una metodología específica (o que se complementa con los pasos de la metodología elegida).

!!! En simple
Es el diagnóstico de un mecánico: lista de piezas valiosas, qué fallas tienen y qué tan seguido, qué refacciones ya traen, cuánto riesgo queda, qué mejorar y el reporte firmado. Límite: el mecánico te recomienda marcas; en un análisis de riesgos ético está prohibido.

La profesora publicará en Classroom las metodologías más usadas. Los pasos, agrupados por pregunta:

1. **(¿Qué?)** Identificar los bienes indispensables y su valor y jerarquía. En una empresa no hay mínimo ni máximo; **en el proyecto, 15 bienes**.
2. **(¿De qué?)** Identificar y describir con claridad las amenazas de cada bien (también ambientales, como ratas o incendios).
3. Identificar y describir las vulnerabilidades con precisión (no «no contar con estándares», sino cuáles faltan).
4. Determinar el impacto y la frecuencia, con estadísticas cuando existan (sismos en septiembre, cortes de luz).
5. **(¿Cómo?)** Identificar los controles que ya existen y qué hacen.
6. Determinar los riesgos residuales.
7. Recomendaciones para aumentar la seguridad, **sin marcas ni proveedores**, solo características o perfiles.
8. **Informe final** con todo: introducción, conclusiones, referencias, imágenes y evidencia de cómo se recabó la información (entrevistas grabadas, cuestionarios firmados). Sin escribir literalmente las tres preguntas como títulos.

Por qué importa: Es la guía del proyecto del curso.
Error común: poner solo «las computadoras» como bienes; amenazas o vulnerabilidades de una palabra; informe sin evidencia; incluir marcas; titular con las tres preguntas.

## 6. Cada cuándo, la matriz FODA y cómo cotizar
Criterios para repetir el análisis, la matriz FODA como resumen rápido y cómo dividir y cotizar en organizaciones grandes.

!!! En simple
Actualizas el inventario y el seguro de tu casa cuando te mudas o compras un coche, no cada lunes. FODA es un post-it con lo bueno y lo malo: útil, pero no reemplaza el inventario.

«¿Cada cuándo se hace?» Una alumna: «cuando hay cambios». Igual que las políticas: cada que hay **cambios significativos** (fusiones, puestos, áreas, misión o visión, nuevas tecnologías).

La **FODA** (fortalezas, oportunidades, debilidades, amenazas) sirve para resúmenes rápidos, sin la profundidad de un análisis formal (que puede pasar de 30 hojas).

En organizaciones grandes se analiza por departamentos y de abajo hacia arriba (en la Facultad: un departamento, otro, los denominadores comunes y luego la división).

No cotizar a ciegas (10,000 pesos sin conocer el tamaño, la gente, traslados o equipo): investigar tarifas de mercado.
Error común: analizar una institución enorme de golpe; confundir FODA con análisis formal; cotizar sin conocer la organización.

## Pendiente / próxima clase
- La profesora publicará en Classroom las metodologías de análisis de riesgos más usadas.
- **Próxima clase:** ejercicio de matriz de riesgos con el *framework* de NIST.
- **Proyecto:** análisis de riesgos con 15 bienes, informe sin marcas.
- **Examen:** abarcará todo el contenido; probablemente en la última semana (martes o jueves), por definir si en equipo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Las tres preguntas de seguridad y su orden estricto.** las anotó y preguntó al grupo, corrigió que no se cambie el orden y las usó para estructurar los ocho pasos.
- **Terminología: aceptación, manejo, evaluación, pérdidas esperadas y riesgo residual.** dedicó el primer bloque a definirlos e insistió en el riesgo residual y en suponer siempre lo peor.
- **Análisis cuantitativo (ALE) contra cualitativo, y que se usan juntos.** los contrastó con ejemplos reales y recalcó que no se elige uno solo.
- **Los 8 pasos, la evidencia y la prohibición de recomendar marcas.** lo ligó al proyecto (15 bienes) y repitió que nunca se ponen marcas ni proveedores.
- **Cada cuándo se hace un análisis de riesgos y el papel de la alta dirección.** lo preguntó al grupo y advirtió que el próximo examen evaluará todo el contenido.

!!! Puntos clave
- Tres preguntas en orden: ¿qué?, ¿de qué?, ¿cómo?
- Aceptar o manejar el riesgo; el manejo no cuesta más que el bien; tomar el último análisis como base.
- Riesgo residual = lo que queda tras los controles; pérdidas esperadas = suponer lo peor, y avisar por escrito.
- Cuantitativo (ALE, costos) y cualitativo (colores, palabras), juntos.
- 8 pasos: bienes → amenazas → vulnerabilidades → impacto y frecuencia → controles → residual → recomendaciones sin marcas → informe con evidencia.

## Ponte a prueba
1. **¿Cuáles son las tres preguntas y por qué no se cambia el orden?** ¿Qué?, ¿de qué? y ¿cómo lo protejo?; si empiezas por el cómo, compras herramientas sin conocer los bienes ni los problemas.
2. **Una organización tiene tres análisis previos. ¿Cuál toma de base? ¿Y si no tiene ninguno?** El último; si no hay ninguno, parte de cero apoyándose en metodologías o en un especialista.
3. **¿Qué es el riesgo residual? Ejemplo de la vacuna o el seguro.** El riesgo mínimo aceptado tras los controles: un resfriado leve en vez de terapia intensiva; perder el 20 % con un seguro del 80 %.
4. **Cuantitativo contra cualitativo: ¿cuál conviene?** Ambos: cifras (ALE, costos) para decidir inversiones y colores o palabras para lo que no tiene precio y para leer rápido.
5. **Una clínica dental quiere los títulos «¿Qué quiero proteger?» en el informe, marcas de cámaras recomendadas, y su personal no conoce términos técnicos. ¿Qué corriges y cómo recabas la información?** Sin las preguntas como títulos, sin marcas (solo características), los 8 pasos con evidencia; oficio de la dirección con avisos de privacidad y cuestionarios en lenguaje amigable.
6. **¿Por qué el manejo no debe costar más que el bien y cuál es la excepción?** Porque sería ilógico; la excepción son las personas, que se cubren con seguros.
7. **Una empresa migra la nómina a la nube, fusiona áreas y cambia de misión. ¿Qué hace?** Rehacer las políticas y el análisis de riesgos, porque son cambios significativos.
