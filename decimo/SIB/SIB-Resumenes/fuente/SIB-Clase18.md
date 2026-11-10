% materia: Seguridad Informática Básica
% titulo: Clase 18 · Planes de contingencia: ventajas, tres subplanes y cinco pasos
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · jueves 5 nov 2026 · Tema 4 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Ventajas y desventajas de los planes de contingencia, retroalimentación de errores de redacción en políticas, los tres subplanes (respaldo, emergencia y recuperación), la metodología de cinco pasos y un ejercicio en parejas contra incendios en casa. Continúa la Clase 17.

!!! Fuente
NotebookLM (audio SIB-Clase18.m4a). No se anotan nombres de compañeros. Lo que no se pudo contrastar con el audio se marca como dudoso.

## 1. Ventajas y desventajas de un plan de contingencia
- **Ventajas:** quita el caos (indicaciones claras para que nadie estorbe o improvise maniobras que empeoran todo); crea cultura y obligación de reportar incidentes a tiempo; da resiliencia institucional.
- **Desventajas:** menos flexibilidad por seguir un protocolo rígido; consume tiempo y recursos (capacitar y hacer simulacros); sesgo de experiencia (no se prevé todo); falsa sensación de seguridad (el documento existe pero no se probó); desactualización (planes que ordenan cosas absurdas u obsoletas); y asignar responsabilidades a quien no tiene compromiso laboral (servicio social, becarios).
Error común: creer que un simulacro desperdicia extintores (se evalúa tiempo de reacción, técnica y condición del operador) o capacitar al personal nuevo hasta meses después de su ingreso.

## 2. Retroalimentación sobre la redacción de políticas
- **Omitir figuras fuera del organigrama:** servicio social, practicantes, visitantes a eventos y auditores (contratados o invitados).
- **Escribir el nombre del principio como título** («Mínimo privilegio», «Responsabilidad») en vez de reflejarlo en la redacción: el principio queda implícito en la regla.
- **Falta de sujeto:** «una persona revisará las muestras» deja entrar a cualquiera. Hay que decir el cargo o rol.
- **Autorización ambigua:** «se prohíbe X a menos que esté autorizado» sin decir quién autoriza.
Insumo directo del proyecto final: repetir estos errores resta calificación.

## 3. Los tres subplanes
!!! Examen
Un plan de contingencia (también protocolos de emergencia o recuperación; en inglés, Disaster Recovery Plan, DRP) se divide por el momento del siniestro: **Plan de Respaldo (antes), Plan de Emergencia (durante) y Plan de Recuperación (después)**. Se separan por tipo de siniestro: sismos, incendios, fallas médicas, bases de datos.
| Subplan | Cuándo y tipo | Base de datos | Extintor e instalaciones |
|---|---|---|---|
| Respaldo | Antes; preventivo | Respaldos periódicos en la nube, control de versiones | Ubicar el extintor, revisar manómetro y vigencia, capacitar; revisar cables, evitar charcos, cerraduras mecánicas al cierre |
| Emergencia | Durante; correctivo planificado | Desconectar el servidor de la red para frenar el borrado y llamar a la extensión del área | La persona designada y capacitada (con relevos A, B y C) ataca el fuego |
| Recuperación | Después; vuelta a la operación y prevención | Encender el servidor, verificar la integridad del respaldo y restaurar | Recargar o reemplazar el extintor, seguros, indemnizaciones, reparar equipos |
Error común: querer hacer el respaldo o contratar el seguro mientras el servidor se borra o el edificio arde; o restaurar la base mientras el ataque sigue.

## 4. Metodología de cinco pasos
1. **Identificación o análisis de riesgos:** responder las tres preguntas de seguridad: ¿qué quiero proteger?, ¿de qué lo protejo? y ¿cómo lo protejo?
2. **Evaluación de riesgos (estrategias de recuperación):** magnitud y probabilidad, para ver qué alternativas hay.
3. **Desarrollo de estrategias:** asignar prioridades. Una estrategia es **planeada y premeditada y no genera más problemas de los que resuelve**. Ejemplo en clase: bajar de un piso, la opción de las escaleras (con elevador para quien tenga discapacidad motriz) es estrategia; saltar por la ventana es lo más rápido pero termina en muerte o discapacidad.
4. **Desarrollo de procedimientos:** el paso a paso para recuperarse en el menor tiempo con los recursos disponibles. Ejemplo real: tras el incendio en las vías del metro del día anterior, el gobierno puso autobuses RTP e incluso patrullas para trasladar a los usuarios.
5. **Pruebas de entrenamiento, plan de mantenimiento y documentación:** documentar con diagramas y señalización, probar y actualizar ante cambios de tecnología, personal o instalaciones.
Error común: delegar el plan a una empresa externa o a un área ajena (finanzas haciendo el plan del centro de cómputo) o desechar planes previos solo porque los hizo otra administración.
- Regla de prioridad en emergencias: el adulto capacitado se asegura primero para poder auxiliar (la mascarilla de oxígeno en el avión).

## 5. Ejercicio en parejas: 15 procedimientos contra incendio en casa
- 30 minutos; 5 de respaldo, 5 de emergencia y 5 de recuperación; considerar personas, mascotas y bienes, y escenarios severos como una ofrenda de Día de Muertos con veladoras.
- **Respaldo:** extintor ABC, detectores de humo con baterías probadas cada mes, revisar instalaciones eléctricas y de gas, no sobrecargar contactos ni dejar planchas conectadas, punto de reunión exterior.
- **Emergencia:** dar la alarma, evacuar por la ruta más segura, avanzar agachado cubriendo nariz y boca con un paño húmedo, llamar al 911 desde un lugar seguro; si la ropa se prende, no correr: detenerse, tirarse al suelo y rodar.
- **Recuperación:** revisar lesiones, reingresar solo cuando bomberos o protección civil lo digan, avisar a la aseguradora, retirar escombros e investigar la causa para actualizar el plan.
Error común: mezclar emergencia con recuperación (evaluar pérdidas mientras el fuego sigue).

## Contexto — no examen
- Un manual obsoleto que ordenara «sacarle la bolita al ratón mecánico».
- Los «cerillitos» que empacaban en el súper y la práctica que se abolió.
- La plataforma de compras de la UNAM que escondió los botones de «siguiente».
- Simulacros en cruceros (chaleco y punto de reunión antes de zarpar) contra aviones, donde se ignora a los sobrecargos.
- Que los jóvenes tampoco deben confiarse: heredar sin testamento genera pleitos familiares.
- Comentarios sobre noticias, empresas y política (no se resumen aquí).

## Pendiente
- Entregar en la misma sesión la hoja de 15 procedimientos contra incendios en casa.
- La profesora seguirá calificando el ejercicio de políticas para retroalimentar el proyecto final.
- Próxima sesión: martes, tras el pase de lista.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Tema | Idea para recordar |
|---|---|
| Tres subplanes | Respaldo (antes), Emergencia (durante), Recuperación (después) |
| Cinco pasos | Riesgos, evaluación, estrategias, procedimientos, pruebas y mantenimiento |
| Tres preguntas | ¿Qué protejo?, ¿de qué?, ¿cómo? |
| Estrategia | Planeada y sin más daños que los que resuelve (no saltar por la ventana) |
| Ventajas | Menos caos, cultura de reporte, resiliencia |
| Desventajas | Rigidez, costo, falsa seguridad, desactualización |
| Errores de redacción | Sin sujeto, principios como título, olvidar figuras externas, autorización sin cargo |
| Prioridad | Asegurar primero a quien auxilia |

!!! Hilo conductor
Un plan de contingencia se arma por fases (riesgos, estrategias, procedimientos, pruebas) y se reparte en antes, durante y después; y funciona solo si está bien redactado, con sujetos claros, y se ensaya y actualiza.
