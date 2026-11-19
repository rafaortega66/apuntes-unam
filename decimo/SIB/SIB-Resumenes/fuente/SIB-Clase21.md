% materia: Seguridad Informática Básica
% titulo: Clase 21 · Auditoría informática y ética informática
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · martes 17 nov 2026 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Qué es una auditoría informática, sus cuatro objetivos y sus ocho pasos, cómo comportarse ante un auditor; ética informática, códigos deontológicos, los 10 mandamientos del Computer Ethics Institute y un decálogo propio. La profesora confirmó el examen final: la próxima semana, individual y de todo el curso.

!!! Fuente
Fuente: NotebookLM (audio `SIB-Clase21.m4a`), 19 nov 2026. La sección de examen sale de lo que la profesora recalcó en la clase; la fecha, modalidad y alcance del examen los dijo explícitamente al final.

## 1. Auditoría informática: qué es, objetivos y marco normativo
Proceso estructurado que evalúa cómo se llevan a cabo los procesos de la organización para verificar si las actividades, planes y controles cumplen con los objetivos del negocio y evitan incidentes de seguridad. Es **preventiva**, no reactiva: no se hace para ver qué hacer después de un desastre, sino para impedir que ocurra.

!!! En simple
Como la verificación vehicular: no vas para que te arreglen el motor después de que se desbieló, sino para que un perito certifique que el coche cumple antes de circular. Límite: el verificentro solo da un holograma; la auditoría revisa manuales, contratos, capacitación, retorno de inversión y formatos vigentes en varios departamentos.

**Auditor de calidad ≠ auditor informático.** Haber tomado cursos de ISO 9000 (versiones 2015, 2018 o la nueva que incorpora temas ambientales) no capacita para auditar sistemas: en cómputo hay que capacitarse en la familia **ISO/IEC 27000**, la de los Sistemas de Gestión de Seguridad de la Información (SGSI).

**Los cuatro objetivos de la auditoría informática:**
1. **Control de los procesos informáticos:** que los procedimientos tecnológicos estén regulados y no se hagan al azar.
2. **Cumplimiento de los objetivos de la organización:** que los sistemas de TI de verdad apoyen la misión de la empresa.
3. **Cumplimiento de la normatividad:** con listas de verificación se valida qué cláusula del estándar cubre cada formato (p. ej., indicar en la matriz de riesgos si corresponde a planeación, a actuación o al numeral 3.4.9).
4. **Gestión eficaz de los recursos informáticos:** hardware, software, consumibles y formatos, con un retorno de inversión (ROI) real y no un gasto desmedido.

**Versiones de los formatos.** Si un departamento muestra la versión 3.1 de un formato cuando la organización ya emitió la 3.2 (p. ej., la nueva cambió «el empleado» por «el personal usuario» para usar lenguaje neutro), se registra una **observación**, que puede escalar a **no conformidad** si muestra una falla generalizada de comunicación interna. La organización también debe declarar qué áreas usan formatos digitales y cuáles papel, y respetar reglas internas (en la UNAM, por disposición oficial, la documentación no se engrapa).

Por qué importa: retoma las auditorías internas y externas y el SGSI de ISO 27001/27002 vistos en el curso.
Error común: creer que una auditoría de calidad cubre automáticamente los sistemas informáticos, o presentar formatos obsoletos.

## 2. Los ocho pasos de la auditoría y cómo comportarse ante el auditor
Metodología secuencial con la que una firma auditora planea, presupuesta, ejecuta y documenta la evaluación, más las reglas que debe seguir el personal auditado.

!!! En simple
Como un juicio oral: el tribunal no llega de sorpresa; agenda fechas con meses de anticipación, define qué va a juzgar, interroga solo a los testigos citados y levanta un acta final. Un testigo que habla de más le da argumentos a la contraparte. Límite: en un juicio se buscan culpables; en la auditoría se buscan evidencias de conformidad o desviaciones para dar o mantener un certificado.

**Los pasos:**
1. **Planeación y programas de trabajo:** acercamiento con la empresa para entender qué busca (un autodiagnóstico o una certificación).
2. **Entrevistas preliminares:** reuniones de coordinación. Las auditorías externas se planean hasta con un año de anticipación porque hay pocas certificadoras acreditadas y sus agendas están llenas.
3. **Investigación y diagnóstico preliminar:** organigramas, diagramas y **alcance**. No es lo mismo auditar toda la UNAM que la Facultad de Ingeniería o solo la División de Ingeniería Eléctrica; en la facultad se auditan 31 laboratorios, recién ampliados a 33, y eso dimensiona al equipo auditor.
4. **Plan de auditoría definitivo:** horarios, calendario, costos (si es externa) y qué auditor evalúa cada departamento.
5. a 8. **Ejecución, recolección de evidencia, reunión del equipo auditor e informe final:** se aplican listas de verificación, se observa y se entrevista; luego los auditores consensúan en privado los hallazgos y presentan el informe con oportunidades de mejora, observaciones o no conformidades, en los plazos previstos.

La profesora lo comparó con el informe del análisis de riesgos de la clase anterior.

**El equipo auditor:** auditor líder (coordina y consensúa el informe), auditores (entrevistan y revisan evidencias) y observadores (auditores en entrenamiento que solo observan y toman notas; no preguntan ni intervienen).

**Reglas al ser auditado** (las repitió varias veces):
- **Contestar solo lo que se pregunta.** A «¿qué formato usas para pedir un chequeo de servidores?» se responde «el formato 25» y nada más. Si agregas «lo lleno con pluma negra, se lo paso al jefe y tarda 3 días en firmar», el auditor preguntará si hay un indicador documentado para esos 3 días y abre otra observación. Lo comparó con los alumnos que, al preguntar cómo será el examen, le dan ideas para hacerlo más difícil: «no den ideas, contesten solo lo que es».
- **No contestar por un compañero.** Si el auditor dice «a ver, Lalo, contéstame tú», nadie lo rescata: el auditor evalúa la competencia de esa persona.
- **No prometer lo que la empresa no puede pagar.** No aceptar a la ligera recomendaciones como automatizar un proceso que requiere 50 programadores (puso de ejemplo al INE) si no hay presupuesto.
- Si no entiendes la pregunta, decirlo con calma («no entiendo a qué se refiere») en vez de inventar.

Error común: dar información de más, contestar por otro o decir que sí a todas las sugerencias sin revisar el presupuesto.

## 3. Ética informática y los riesgos de la tecnología actual
Rama de la ética aplicada que estudia los dilemas morales, responsabilidades y conductas que surgen del desarrollo y la difusión masiva de las tecnologías de la información.

!!! En simple
Como pasar de carretas a autopistas: el auto te lleva más lejos y más rápido, pero si lo usas para atropellar gente el problema no es el motor sino quien maneja. Límite: un auto daña a quien está en la misma calle; un video manipulado con IA da la vuelta al mundo en minutos.

La profesora contrastó la evolución: al principio (ARPANET) había pocos equipos y pocas redes; después redes locales con pocas aplicaciones masivas; hoy millones de equipos conectados con aplicaciones que viralizan contenido en segundos. Eso trae problemas éticos:

- **Monetizar el dolor ajeno y noticias falsas:** cuentas que difunden fichas falsas o descontextualizadas de personas desaparecidas para ganar vistas.
- **Clonación de voz e IA generativa:** quien regala muestras de su voz a apps de juego para hacer canciones puede ceder sus derechos biométricos; la voz se puede vender, sustituir a locutores o usarse en estafas de suplantación.
- **Imágenes de menores** publicadas sin autorización, con riesgo de demandas.

**Controles en las organizaciones:** bloquear internet a puestos que no lo necesitan (con oficio justificado si se requiere para pruebas), bloquear puertos, restringir privilegios para que el usuario común no instale software, y firmar acuerdos de confidencialidad y avisos de privacidad.

Error común: ceder datos biométricos a apps sin leer los términos o dar por cierto cualquier contenido viral.

## 4. Códigos deontológicos, leyes y convenios
Un **código deontológico** reúne los deberes, principios éticos y estándares de conducta que deben regir el ejercicio de una profesión para que su práctica aporte al bien común.

!!! En simple
El juramento de un gremio: así como el juramento hipocrático impide al médico dañar a un paciente, un código deontológico le prohíbe al ingeniero hacer software para estafar o descuidar sistemas de los que dependen vidas. Límite: el juramento médico es milenario; en computación la tecnología cambia tan rápido que los códigos deben actualizarse.

«Deontológico» **no tiene que ver con dientes** (bromeó la profesora): viene del deber moral profesional. En México no hay un código deontológico informático único publicado en el Diario Oficial que obligue a todo el país, pero organizaciones, gremios y universidades pueden redactar el suyo para dar pertenencia, motivación y prestigio.

Los códigos también sirven para **armonizar legislaciones y convenios** entre entidades. Ejemplos:
- **Convenio UNAM–Cisco:** tardó mucho porque Cisco lo veía con óptica comercial y la UNAM, institución pública, no podía aceptar cláusulas que violaran la legislación universitaria o los derechos de alumnos y profesores; los abogados tuvieron que ajustar cláusulas.
- **Autobuses de la Facultad de Ingeniería:** la compra tomó más de cuatro años de trámites desde la administración anterior para cumplir con la normatividad.

Error común: confundir «deontológico» con algo dental o suponer que hay un código de ética idéntico en todos los países.

## 5. Principios de la ética informática, los 10 mandamientos y el decálogo
Principios que orientan la conducta del profesional de la computación frente a usuarios, empresa y sociedad.

!!! En simple
Tu brújula cuando tienes acceso de superusuario a la nómina o a historiales médicos y nadie te vigila. Límite: una brújula solo marca el norte; la ética te pide equilibrar compromisos con la empresa, los usuarios, la ley y tu propia salud.

**Principios que expuso:**
- **Confidencialidad:** no platicar datos, proyectos ni arquitecturas internas.
- **Lealtad a la empresa y al usuario:** cumplir compromisos; cambiar de trabajo por mejores condiciones no es deslealtad. Contó el caso de un colega en HP, muy bien pagado, al que llamaban un domingo a las 11 p. m. para viajar y dar un curso a las 9 a. m., o a las 3 a. m. por servidores caídos; renunció para trabajar en la universidad ganando menos y recuperó su salud.
- **Bien común y sensibilidad pública:** el trabajo de ingeniería tiene impacto social (mencionó la Línea 12, las más de 134,000 personas desaparecidas en el país y citas de cáncer pospuestas por meses).
- **Capacitación continua** para no volverse obsoleto.
- **Integridad:** no bajar los estándares propios porque otros actúen mal.
- **Transmisión expedita de datos y disponibilidad:** entregar a tiempo. Si un profesor no sube actas a tiempo, a él no le pasa nada, pero al alumno le bloquean inscripción o becas por materias seriadas; también citó cuando la SEP tardó meses en emitir certificados de secundaria y muchos jóvenes no pudieron inscribirse al bachillerato.
- **Privacidad:** evitar invasiones con cámaras remotas mal configuradas.
- **Propiedad intelectual:** reconocer la autoría ajena; en México la ley protege obras literarias y artísticas pero tiene huecos en software, y hay quien registra sus proyectos en el extranjero.

Luego presentó los **10 mandamientos de la ética informática del Computer Ethics Institute** (EE. UU.). Son un referente, pero las organizaciones suelen sintetizar sus normas en **decálogos**: 10 puntos claros y obligatorios para un área, proyecto o profesión.

**Actividad entregada en clase:** cada alumno escribió en una hoja un decálogo con 10 conductas indispensables de un ingeniero o ingeniera en computación en una organización.

Error común: confundir lealtad con aguantar jornadas que destruyen la salud, o creer que la ética solo aplica a médicos y abogados.

## Contexto (no examen)
- Convenio UNAM–Cisco y la compra de los autobuses de la facultad (arriba, como ejemplos).
- El caso del colega de HP.
- Casos de atacantes que hackean cámaras en cuartos de niños para asustarlos de noche.
- En la UNAM los documentos oficiales no se entregan engrapados.
- Avisó que un día antes abrió la convocatoria del Diplomado en Ciberseguridad (portal de Redes y Seguridad de la facultad).

## Pendiente / próxima clase
- **Próxima clase:** Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP).
- **Examen final: la próxima semana (la última del semestre), individual y de todo el curso.** La profesora dijo que en equipo sería más difícil y que individual es rápido.
- Se entregó en clase el decálogo individual de 10 puntos.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

## Lo que probablemente viene en el examen
- **Auditoría de calidad (ISO 9000) contra auditoría informática (ISO/IEC 27000).** abrió la clase con eso.
- **Los cuatro objetivos de la auditoría informática y el caso de la versión 3.1 contra 3.2.** los explicó uno por uno y el caso de versiones con detalle.
- **Los ocho pasos de la auditoría.** los proyectó y los comparó con el informe de análisis de riesgos.
- **No dar información de más al auditor.** lo repitió varias veces con ejemplos.
- **Código deontológico y su función de armonizar convenios.** lo definió, bromeó con «no es dental» y dio el caso UNAM–Cisco; el decálogo se entregó en clase.

!!! Puntos clave
- Auditoría informática = evaluación preventiva de procesos y controles contra los objetivos del negocio.
- Cuatro objetivos: control de procesos, objetivos de la organización, normatividad (checklists por cláusula) y gestión eficaz de recursos (ROI).
- Formato desactualizado → observación → puede escalar a no conformidad.
- Equipo: auditor líder, auditores y observadores (estos no preguntan).
- Código deontológico = deberes éticos de una profesión; decálogo = 10 reglas obligatorias.
- Examen final: próxima semana, individual, todo el curso.

## Ponte a prueba
1. **¿Por qué un curso de ISO 9000 no te hace auditor informático?** Porque ISO 9000 es de calidad; para seguridad de TI se usa la familia ISO/IEC 27000 (SGSI).
2. **¿Cuáles son los cuatro objetivos de la auditoría informática?** Control de procesos informáticos, cumplimiento de objetivos de la organización, cumplimiento de la normatividad y gestión eficaz de los recursos con ROI.
3. **¿Por qué mostrar la versión 3.1 de un formato si ya existe la 3.2 puede ser no conformidad?** Porque evidencia falta de comunicación y control interno: los departamentos no trabajan con los mismos lineamientos.
4. **¿Cuál es la regla de oro al responder a un auditor?** Contestar solo lo que se pregunta; dar detalles extra le da ideas para abrir nuevas observaciones.
5. **Auditor líder, auditor y observador.** El líder coordina y consensúa el informe; los auditores entrevistan y revisan evidencias; los observadores están en entrenamiento y solo toman notas.
6. **El auditor le pregunta a tu compañero y él se queda callado; tú sabes la respuesta. ¿Qué haces?** Guardar silencio: el auditor evalúa la competencia de esa persona. Y no comprometer a la empresa a comprar herramientas sin presupuesto.
7. **¿Qué es un código deontológico y para qué sirve en un convenio?** Normas éticas de una profesión para el bien común; ayudan a armonizar las normas de entidades con objetivos distintos (UNAM–Cisco).
8. **Actas tardías del profesor y certificados tardíos de la SEP: ¿qué principio se viola?** La transmisión expedita y la disponibilidad: el daño cae en el alumno (inscripción, becas, un año perdido).
