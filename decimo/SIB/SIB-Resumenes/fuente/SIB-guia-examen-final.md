# **SIB · Guía para el examen final**

**Seguridad Informática Básica** · Semestre 2027-1 · 16 nov 2026  
*Hecha con NotebookLM a partir de todas las fuentes del cuaderno de la materia (audios de cada clase y material del profesor): hilo conductor del curso, unidades con sus conceptos explicados, lo que más probablemente viene y las conexiones entre conceptos. Acompáñala con el mapa mental (SIB-mapa-mental.pdf, en esta misma carpeta).*

## **HILO CONDUCTOR**

La historia de la materia parte de una verdad fundamental: **la seguridad no es un destino fijo ni garantiza un 100% de protección, sino un ciclo dinámico y continuo (PDCA)** donde toda organización busca proteger sus bienes mediante un esquema guiado por **tres preguntas en orden estricto**: *¿qué quiero proteger?*, *¿de qué lo quiero proteger?* y *¿cómo lo voy a proteger?*. Para evitar reinventar la rueda y poder demostrar cumplimiento mediante **auditorías** internas o externas, el curso primero ubica ese ciclo dentro de la evolución de la **normatividad y los estándares internacionales** —pasando de criterios militares rígidos centrados en productos (como TCSEC) a sistemas integrales de gestión de la información en toda la organización (como la familia ISO/IEC 27000, NIST y COBIT). Con ese marco normativo en mano, se baja a la operación respondiendo las tres preguntas en orden: primero se delimita el **entorno**, los **bienes** y las necesidades de protección (**servicios de seguridad**) junto con las herramientas (**mecanismos**) que las satisfacen; después se responde *¿de qué protegerlos?* analizando el choque entre **amenazas** externas o internas y **vulnerabilidades** u omisiones (medidas con bases y métricas como CVE, NVD y CVSS), choque que al concretarse produce **ataques** ejecutados por **perpetradores** mediante técnicas de intrusión.

## **Una vez comprendido qué proteger y contra qué, el curso cierra respondiendo *¿cómo protegerlo?* desde el gobierno institucional hasta la recuperación operativa. Primero se redactan políticas de seguridad claras, obligatorias y sin ambigüedades, y se formalizan mediante modelos de seguridad (de control de acceso, flujo de información e integridad) que dictan quién puede hacer qué sobre cada recurso. Como ninguna prevención evita el 100% de los incidentes, esas reglas se respaldan con planes de contingencia (DRP) divididos en subplanes temporales (*antes, durante y después*) para sobrevivir a desastres y recuperar la operación en el menor tiempo posible. Finalmente, el análisis y la gestión de riesgos cierra el círculo como la brújula que alimenta tanto a las políticas como a los planes de contingencia: prioriza infraestructuras y procesos críticos bajo una lógica económica (*que el ataque cueste más que el bien y la protección cueste menos que el bien*), combina métodos cuantitativos y cualitativos en matrices de riesgos consistentes y retroalimenta nuevamente al ciclo continuo cada vez que hay cambios significativos. *(Nota sobre fuentes: las Clases 1–10 y 12–20 provienen de audios y* *SIB-Clase2.pdf* *; el audio de la Clase 11 no está cargado porque correspondió a la aplicación del primer examen parcial).***

## **UNIDADES Y TEMAS DEL CURSO**

### **UNIDAD 1: Fundamentos, Ciclo de Vida de la Seguridad y Auditorías *(Clase 1\)***

**a) Qué problema resuelve y cómo se conecta:** Resuelve la idea falsa de que poner una contraseña o un candado basta para estar seguro para siempre, estableciendo que la seguridad es un proceso dinámico que requiere revisión periódica para no quedar obsoleta. Es el punto de partida del curso sobre el cual se montan los estándares, las evaluaciones y la mejora continua.  
**b) Conceptos clave:**

> * **Las tres preguntas de seguridad:** Son el núcleo de cualquier esquema de seguridad: 1\) *¿Qué quiero proteger?* (identificar y jerarquizar bienes), 2\) *¿De qué lo quiero proteger?* (amenazas y vulnerabilidades) y 3\) *¿Cómo lo voy a proteger?* (mecanismos y planes). *Analogía:* Antes de armar una maleta para un viaje, primero ves qué vas a llevar, luego qué clima habrá y al final eliges qué ropa empacar; si empacas primero sin saber a dónde vas, gastarás en abrigos inútiles. *Ejemplo de clase:* El ejercicio de reflexión donde alumnos protegían celulares, camas o motos olvidando su propio cuerpo o vista (bienes tangibles como el ojo/córnea frente a intangibles como la vista).  
> * **Contexto de seguridad y sus relaciones:** Conjunto de entidades que interactúan en todo proceso: **propietarios/dueños/responsables**, **bienes/activos** (tangibles o intangibles), **mecanismos de seguridad** (medidas de defensa o herramientas), **vulnerabilidades** (debilidades o puntos débiles), **amenazas**, **agentes amenazantes** (sujetos que pueden causar daño, incluyendo uno mismo) y **riesgos**. *Analogía:* Es el tablero completo de un partido: el dueño del balón, el balón, los defensas, los huecos en la defensa, las jugadas rivales y la probabilidad de gol. *Ejemplo de clase:* En el salón de clases somos *responsables* (no dueños) del cañón, pizarrón y sillas; una computadora mal aislada puede electrocutar a un empleado (donde el empleado es un bien y la PC actúa como agente amenazante), generando quemaduras internas y ausencias laborales sin retorno de inversión.  
> * **Pérdidas:** Se clasifican en **total**, **parcial** o **nula** (cuando hay una pérdida mínima o insignificante que la empresa puede absorber sin impacto grave).  
> * **Ciclo de vida de la seguridad (Ciclo PDCA):** Ciclo dinámico de mejora continua adoptado de los principios de calidad *(el nombre del "padre de la calidad" citado en el pizarrón aparece garabateado en la transcripción de* *SIB-Clase1.m4a* *como "Velquez" o "caridad", por lo que el nombre exacto no puede confirmarse solo con el audio)*, compuesto por **Planear, Hacer, Verificar y Actuar**. *Analogía:* Es la rutina de entrenamiento físico: planeas dieta y ejercicios, los haces un mes, verificas tu peso/condición y actúas ajustando la rutina si no funcionó. *Ejemplo de clase:* Tras el sismo del 19 de septiembre de 2017, verificar que hacer un simulacro al año no basta y cambiarlo a uno mensual obliga a volver a planear fechas, responsables y avisos.  
> * **Auditorías y hallazgos:** Revisión formal para verificar si el ciclo y los estándares se cumplen. Se dividen en **internas (primer nivel)**, hechas por personal de la misma entidad sin pago externo (ej. alguien de FES Aragón auditando a Ingeniería bajo la misma legislación UNAM), y **externas**, hechas por terceros: **segundo nivel** (otra institución que evalúa sin certificar, como el IPN revisando a Ingeniería) o **tercer nivel** (autoridad certificadora acreditada que emite el certificado). *Ejemplo numérico de clase:* Deben hacerse **mínimo 2 auditorías al año** (idealmente cada 6 meses, aunque a veces sea a los 4 o 5 meses); en la facultad se auditaban **31 laboratorios** buscando ampliar el alcance a **33** —si uno solo incumple, **toda la empresa pierde el certificado** — y una auditoría externa puede durar toda una semana de 10:00 a 18:00–19:00 horas.

**c) Comparación y pasos en tabla:**

| Ciclo PDCA (SIB-Clase1.m4a) | Qué se hace en cada fase | Hallazgos de Auditoría (SIB-Clase1.m4a) | Significado e impacto   |
| :---- | :---- | :---- | :---- |
| **P — Planear** | Identificar bienes, jerarquía, riesgos y diseñar el esquema de seguridad (recursos y presupuesto). | **Oportunidad de mejora** | El proceso cumple y funciona, pero el auditor sugiere optimizarlo (ej. digitalizar formatos); es opcional. |
| **D — Hacer (Implementar)** | Ejecutar lo planeado (ej. realizar realmente los simulacros). | **Observación** | Algo que dices hacer no se está haciendo o falla sin afectar aún el proceso; exige plan de corrección. |
| **C — Verificar** | Monitorear, reportar y auditar si los controles funcionan adecuadamente. | **No conformidad** | Incumplimiento grave que pone en riesgo el proceso; impide obtener, ampliar o mantener la certificación si no se subsana en el plazo dado. |
| **A — Actuar** | Tomar decisiones con base en conclusiones (cambiar, actualizar o retirar lo obsoleto) y reiniciar el ciclo. | — | — |

**d) Errores comunes y puntos de examen:**

> * Creer que existe la **seguridad al 100%** (falso: todos los bienes tienen vulnerabilidades) o ver la seguridad como **gasto** en vez de **inversión**.  
> * Olvidar que el **eslabón más débil** de la cadena de seguridad es el **ser humano**.  
> * Poner mecanismos sin criterio (ej. poner 50 chapas y barrotes en ventanas sin considerar salidas en un sismo maximiza la vulnerabilidad y viola el principio de profundidad).  
> * **Error señalado tras el 1er examen ( SIB-Clase14.m4a ):** Decir que el ciclo PDCA solo se aplica cuando hay auditorías; en realidad el PDCA es **continuo** y la auditoría es solo la herramienta para verificarlo.

### ---

**UNIDAD 2: Normatividad y Estándares de Seguridad *(Clases 2 \[PDF\], 3 y 4\)***

**a) Qué problema resuelve y cómo se conecta:** Después de entender el ciclo PDCA y las auditorías, surge la duda: *¿contra qué criterios objetivos se audita?*. La normatividad ofrece marcos reconocidos internacionalmente para no inventar criterios desde cero, generar confianza comercial y superar auditorías.  
**b) Conceptos clave:**

> * **Norma vs. Estándar:** Una **norma** es obligatoria por ley, mientras que un **estándar** es una recomendación adoptada voluntariamente (aunque en México se usan como sinónimos: la **NOM** es obligatoria y la **NMX** no es obligatoria). *Analogía:* El reglamento de tránsito (norma: multa si lo violas) frente a una guía de conducción eficiente (estándar: te conviene seguirla). *Ejemplo:* El modelo OSI (ISO 7498\) exige que todo *switch* nuevo cumpla la capa 2\.  
> * **Evolución de evaluación de productos hacia gestión empresarial:**  
  * **TCSEC ("Libro Naranja", EE. UU., 1983 / rev. 1985):** Criterios militares del Departamento de Defensa centrados de forma monolítica en la **confidencialidad** de sistemas operativos mediante la **TCB** (*Trusted Computing Base*). Niveles de menor a mayor: **D** (protección mínima, ej. MS-DOS), **C1–C2** (protección discrecional; C2 añade auditoría), **B1–B3** (seguridad mandatoria etiquetada MAC, módulos y dominios) y **A1** (verificación matemática formal); cancelado en **2002**.  
  * **ITSEC ("Libro Blanco", Europa, 1990 / v1.2 en 1991):** Armonizó criterios europeos separando **funcionalidad** (F1–F10) y **garantía/aseguramiento** (E0–E6), evaluando productos y sistemas completos contra el *Security Target* del fabricante.  
  * **CTCPEC (Canadá, 1988–1993):** Enfoque híbrido que incorporó toda la **tríada CIA** (confidencialidad, integridad, disponibilidad) más **controlabilidad ( accountability )**, auditoría de ciclo de vida y pruebas de caja blanca/negra. *(Nota de discrepancia entre fuentes:* *SIB-Clase2.pdf* *lista 7 niveles* *T-0* *a* *T-6* *, mientras que en* *SIB-Clase3.m4a* *un alumno mencionó 8 niveles* *T-0* *a* *T-7* *)*.  
  * **Common Criteria / ISO/IEC 15408 (1998/2000–actual):** Fusión de TCSEC, ITSEC y CTCPEC por EE. UU., Canadá, Reino Unido, Francia, Alemania y Países Bajos para evaluar productos TIC (*no empresas*). Maneja **TOE** (*Target of Evaluation* / objeto de evaluación), **PP** (*Protection Profile* / perfil de protección para una clase de productos), **ST** (*Security Target* / meta de seguridad), **7 niveles EAL ( EAL1 a EAL7 )** y **3 partes** (1: Introducción y modelo general, 2: Requerimientos de seguridad funcional, 3: Requerimientos de garantía/confianza; ampliada en ediciones 2022–2026).  
  * **De BS 7799 a la familia ISO/IEC 27000:** El estándar británico **BS 7799** (1995 parte 1 de buenas prácticas; 1998 parte 2 de certificación) dio el salto histórico de evaluar productos a gestionar la **información en toda la empresa** mediante un **SGSI / ISMS**.  
  * **BS 7799-1 → ISO/IEC 17799 (2000: 10 secciones; 2005: 11 secciones) → ISO/IEC 27002 (renombrada en 2007):** Guía de controles y buenas prácticas (**cómo hacerlo**; **no certificable**). Pasó de 14 dominios en 2013 a **4 secciones en febrero de 2022** (Organizacionales: 37, Humanos: 8, Físicos: 14, Tecnológicos: 34\) y 2 anexos.  
  * **BS 7799-2 → ISO/IEC 27001 (2005; actual octubre 2022 \+ enmienda 2024):** Establece los requisitos de un SGSI (**qué hacer**; **sí es certificable**; 10 cláusulas).  
  * **Otros marcos clave: HIPAA** (ley federal EE. UU. de 1996 para proteger información médica PHI/ePHI mediante salvaguardas administrativas, físicas y técnicas); **NIST** (instituto EE. UU. de 1901; series SP 800, *Cybersecurity Framework* CSF 2.0 de 2024 y referencia para matrices de riesgo); y **COBIT** (ISACA, 1996; versión vigente COBIT 2019; gobierno y gestión de TI con 5 dominios EDM, APO, BAI, DSS, MEA y niveles de capacidad 0–5).

**c) Comparación en tabla ( SIB-Clase2.pdf , SIB-Clase3.m4a , SIB-Clase4.m4a ):**

| Estándar / Norma | Enfoque | Niveles / Estructura | ¿Vigente? / ¿Certificable?   |
| :---- | :---- | :---- | :---- |
| **TCSEC (Libro Naranja)** | Sistemas operativos (militar EE. UU., confidencialidad) | Divisiones D, C1, C2, B1, B2, B3, A1 | No vigente (cancelado 2002\) |
| **ITSEC (Libro Blanco)** | Productos y sistemas (Europa) | Funcionalidad F1–F10 / Garantía E0–E6 | No vigente (absorbido en CC) |
| **CTCPEC** | Productos (Canadá, CIA \+ controlabilidad) | T0–T6 \[PDF\] / T0–T7 \[audio\] | No vigente (absorbido en CC) |
| **Common Criteria (ISO 15408\)** | Productos y sistemas TIC | EAL1–EAL7 / 3 áreas (PP, ST, TOE) | Vigente / Certifica productos |
| **ISO/IEC 27001** | Gestión de información empresarial (SGSI) | 10 cláusulas (enfoque basado en riesgos) | Vigente (2022) / **Certificable** |
| **ISO/IEC 27002** | Controles y buenas prácticas de SGSI | 2022: 4 secciones (93 controles) y 2 anexos | Vigente (2022) / **No certificable** |

**d) Errores comunes y puntos de examen:**

> * Confundir **ISO 27001** (derivada de BS 7799-2, dice *qué hacer*, **certificable**) con **ISO 27002** (derivada de BS 7799-1 e ISO 17799, dice *cómo hacerlo*, **no certificable**).  
> * En el cuestionario evaluado de SIB-Clase4.m4a, omitir el prefijo ISO/IEC (escribir solo 27000 o 27002\) valía **medio punto**, y confundir la sigla de **HIPAA** (*H-I-P-A-A*, no "IPA") o **CTCPEC** quitaba aciertos.

### ---

**UNIDAD 3: Esquemas, Entorno, Servicios y Mecanismos de Seguridad *(Clases 4, 5 y 14\)***

**a) Qué problema resuelve y cómo se conecta:** Con las normas claras (como *Common Criteria* y su lógica de perfiles), el siguiente paso es diseñar un **esquema de seguridad** real para responder primero *¿qué necesito proteger?* antes de salir a comprar tecnología a ciegas.  
**b) Conceptos clave:**

> * **Entorno de seguridad:** Todo lo que rodea físicamente y lógicamente al activo (edificación, techo, clima, hardware, software, usuarios, políticas y la misión/visión de la organización). *Ejemplo:* Proteger el cañón del salón con una reja y candado sin revisar si el techo tiene goteras o si el proyecto se calienta falla porque ignora el entorno.  
> * **Objetivos de seguridad:** Metas concretas derivadas del entorno; deben redactarse siempre como **acciones (con verbos)**, ser breves (**máximo dos renglones**) y especificar exactamente perfiles y horarios (ej. *"Solo el profesorado con clase en ese horario y el alumnado inscrito pueden manipular la PC"*).  
> * **Servicios de seguridad (= Necesidades):** Son las **necesidades de protección** de la organización. Hay **6 servicios** (mientras que el modelo OSI 7498 solo contempla 5 porque da por sentada la disponibilidad):  
  1. **Confidencialidad:** Mantener información en secreto solo para autorizados.  
  2. **Integridad:** Evitar modificaciones no autorizadas en información, bienes o incluso en la conducta/estado de las personas.  
  3. **Disponibilidad:** Garantizar acceso oportuno al servicio o bien cuando se necesita (como cuando falla el proyector Wi-Fi o el sistema de inscripciones).  
  4. **Control de acceso:** Permitir o restringir el paso o uso de un área, servicio o bien; **siempre va unido a la autenticación**.  
  5. **Autenticación (o autentificación):** Verificar identidades (de personas, servicios, procesos o bienes) mediante **3 factores**: *algo que se sabe* (contraseña), *algo que se tiene* (credencial, tarjeta, firma digital) y *algo que se es* (huella, iris, ID de proceso —hoy separados de "algo que se tiene" porque son únicos e irrepetibles—).  
  6. **No repudio:** Imposibilidad de negar haber realizado una acción (ej. firmar acuse de oficio verificado por perito calígrafo, o registrar comandos sudo ligados a llave SSH).  
> * **Equilibrio operacional:** Los servicios se gradúan según el giro del negocio (ej. Liverpool deja abierto su catálogo web al público para que compren, y solo pide usuario/contraseña cuando vas a pagar).  
> * **Fenómeno o síndrome del bolero:** Minimizar el peligro de personas cotidianas (boleros, personal de limpieza, desconocidos en el elevador) hablando de asuntos confidenciales frente a ellos, o publicando en redes (que se revisa con *egosurfing*).  
> * **Mecanismos de seguridad (Controles / Herramientas):** Cualquier aplicación, técnica, objeto, regla, animal (perro guardián) o persona que **satisface** uno o varios servicios de seguridad.  
> * **Principio de profundidad:** Usar múltiples capas o niveles de protección coordinados, cuidando que no se bloqueen ni vuelvan inútil al sistema (como olvidar una contraseña de una capa o instalar rejas en una casa de cartón o techo de asbesto).

**c) Clasificación de mecanismos y relación con servicios ( SIB-Clase14.m4a ):**

| Criterio de clasificación | Categorías | Ejemplo visto en clase   |
| :---- | :---- | :---- |
| **1\. Por el servicio que implementa** | Confidencialidad, Integridad, Disponibilidad, Control de acceso, Autenticación, No repudio. | Sensor biométrico \= Control de acceso \+ Autenticación; Puerta \= Control de acceso. |
| **2\. Por grado de importancia** | **Requeridos** (mínimos indispensables) vs. **Discrecionales** (complementarios para subir el nivel). | Puerta y 1 chapa \= requerido; poner 2 o 3 chapas extra o tomar vitamina C además de vacunarse \= discrecional. |
| **3\. Por cobertura (en modelo OSI)** | **Generales/Generalizados** (cobertura amplia a toda la entidad) vs. **Específicos** (para un área, capa o protocolo delimitado). | Gafete para todos los empleados y visitantes \= general; gafete solo para TI \= específico. |
| **4\. Por su acción/actividad** | **Preventivos** (evitan antes), **Correctivos** (resuelven durante/después), **Detectores/Detectives** (identifican anomalías) y **Disuasivos** (convencen de no actuar). | Un **antivirus** puede cumplir las 4 funciones; un cartel *"Si tomas no manejes"* \= disuasivo. |

**d) Errores comunes y puntos de examen:**

> * Confundir **servicios** (necesidades) con **mecanismos** (herramientas).  
> * En los **11 pasos** de perfiles de protección (SIB-Clase4.m4a), nunca imponer marcas o herramientas específicas (ej. *"pon una cerradura"*), sino la necesidad (*"controla el acceso"*), para evitar que te culpen si el modelo comprado falla.  
> * Comprar sensores biométricos baratos que no detectan pulso/vida (alguien podría usar un dedo cortado o una huella levantada).

### ---

**UNIDAD 4: Amenazas, Vulnerabilidades y Evaluación Técnica *(Clases 6, 7, 8, 9 y 10\)***

**a) Qué problema resuelve y cómo se conecta:** Una vez definidas las necesidades, hay que contestar la **2.ª pregunta de seguridad** (*¿de qué quiero proteger mis bienes?*) sin confundir lo que puede pasar (amenaza) con lo que nos falta (vulnerabilidad).  
**b) Conceptos clave:**

> * **Amenaza:** Actividad, evento o circunstancia **latente** que intenta o puede ocurrir y causar daño a la información o a cualquier bien. *Analogía:* Una nube cargada de lluvia sobre tu cabeza (todavía no te moja, pero está latente).  
> * **Riesgo:** Producto de la ocurrencia de la amenaza y su consecuencia (Riesgo \= Ocurrencia × Consecuencia); solo existe cuando una amenaza encuentra y explota una vulnerabilidad compatible.  
> * **Vulnerabilidad:** Debilidad, brecha, omisión o **"talón de Aquiles"** en un bien o procedimiento que puede ser explotado (aprovechado) accidental o intencionalmente por una o varias amenazas. *Prueba de fuego dada en clase:* Se identifica preguntando **¿qué me falta? / ¿qué omití? / ¿de qué carezco?** (ej. ante la amenaza de mojarse, la vulnerabilidad es *carecer de paraguas*; ante ser confiado, es *carecer de desconfianza*). *Relación:* Nunca es 1 a 1, sino **de uno a muchos**. *Ejercicio del escudo (* *SIB-Clase9.m4a* *):* Cada alumno dibujó un escudo grande con sus propias debilidades humanas (tacos, chocolates, impuntualidad, equipos deportivos, colores) para concientizarse sobre dónde pueden ser atacados.  
> * **Tipos de análisis de vulnerabilidades: Estático** (examinar cómo opera el sistema normalmente sin someterlo a pruebas de ejecución ni alterarlo; en código fuente es **SAST**), **Dinámico** (ejecutar el sistema bajo cargas extremas o datos atípicos para provocar fallos; en aplicaciones en ejecución es **DAST**), **Análisis de Composición de Software (SCA)** (revisar bibliotecas/dependencias obsoletas o sobrantes, ej. incluir 20 librerías cuando solo ocupabas 1\) y **Basado en red** (detectar *firmware* obsoleto y evaluar niveles de confianza alto/medio/bajo).  
> * **Bases y métricas de vulnerabilidades:**  
  * **CVE ( Common Vulnerabilities and Exposures ):** Catálogo público que asigna un ID único con formato CVE-AÑO-CONSECUTIVO (ej. CVE-2022-..., usando rangos asignados por fabricante o aplicación, como 10001 para Microsoft o 50000 para otro).  
  * **NVD ( National Vulnerability Database ):** Repositorio nacional del **NIST** (EE. UU.) que administra y pondera las vulnerabilidades identificadas por CVE usando **CVSS**.  
  * **CVSS ( Common Vulnerability Scoring System ):** Sistema de puntuación real de **0.0 a 10.0** (ej. 3.8, 8.1) que mide la severidad. En **CVSS v2** había 3 niveles (Bajo 0–3.9 verde, Mediano amarillo, Alto rojo), mientras que en **CVSS v3 y v4** la escala inicia en **0.1** y la categoría alta se divide en **Alto (naranja)** y **Crítico (rojo)** (7–8.9 y 9–10), lo que obliga a reclasificar riesgos antiguos como un 8.9. *(Nota: los límites decimales exactos de la categoría "mediano" en v3/v4 no se detallaron verbalmente en el audio).*

**c) Clasificaciones en tabla ( SIB-Clase6.m4a y SIB-Clase7.m4a ):**

| Dimensión | Categorías vistas en clase | Datos clave / Ejemplos   |
| :---- | :---- | :---- |
| **5 Fuentes de amenazas** | 1\) **Factor humano** *(principal)* , 2\) Fallas de hardware, 3\) Fallas de software, 4\) Red (como conjunto), 5\) Desastres naturales (*"actos de Dios"* ). | El humano configura, desarrolla y opera todo lo demás; un error de programación es amenaza interna. |
| **Clasificación general (flujo)** | **Intercepción** (ver/escuchar/leer sin tocar), **Interrupción/destrucción** (disponibilidad), **Modificación** (integridad) y **Suplantación/falsificación** (emisor falso). | Seguir a alguien del salón al metro para anotar su horario \= intercepción; alterar un 10 a 100 en una carta \= modificación. |
| **Por objetivo y por lugar** | **Intencionadas/Conscientes** vs. **No intencionadas/Inconscientes** ; **Internas** vs. **Externas** . | En organizaciones, **85% a 95%** son **intencionadas** e **internas** (o externas que logran entrar con ayuda interna, como una gotera o un correo abierto). |
| **6 Categorías de vulnerabilidades** | 1\) **Humanas** *(se cruzan con todas)* , 2\) Hardware, 3\) Red, 4\) Software, 5\) Naturales, 6\) **Físicas** (construcción/edificaciones). | Celular que se rompe → falta de funda, mica o cuidado; personas daltónicas armando cables de red sin detección previa. |

**d) Errores comunes y puntos de examen:**

> * Confundir vulnerabilidad con amenaza en ejercicios de oración (ej. decir que *"falta personal"* es una amenaza; falso, faltar personal es **vulnerabilidad**, la amenaza es que *alguien robe* por falta de vigilancia).  
> * Invertir la redacción de una vulnerabilidad negando (ej. en *"quedarse sin red por confiar en PC Puma"*, la vulnerabilidad es carecer de *desconfianza*, no de "confianza").  
> * Confiar en un solo escaneo de vulnerabilidades (pueden dar **falsos positivos y falsos negativos**) o usar números CVE inventados por una IA sin verificar en CVE/NVD.

### ---

**UNIDAD 5: Ataques, Perpetradores, Técnicas de Intrusión y Mitigación *(Clases 10, 12, 13 y 14\)***

**a) Qué problema resuelve y cómo se conecta:** Cuando una amenaza logra explotar una vulnerabilidad, nace el **ataque**. Conocer quién ataca y cómo irrumpe permite a la organización anticiparse y no actuar de forma improvisada cuando ya sufrió el daño.  
**b) Conceptos clave:**

> * **Ataque:** Culminación de una amenaza al explotar una o más vulnerabilidades; es todo aquello que **ya sucedió o está sucediendo** y generó un daño (total, parcial o nulo). Los ataques **lógicos** (ciberataques) pueden provocar ataques **físicos** (ej. difundir fotos íntimas provoca un paro cardíaco) y viceversa (que se caiga el techo destruye la PC aunque tenga contraseña de 15 caracteres). *Regla económica clave:* **Recuperarse del ataque es más costoso que prevenirlo** (por tiempo, dinero y personal desviado de sus labores; en **ransomware**, más del **50%** de las empresas pagan y **nunca** recuperan la clave).  
> * **Clasificación de ataques:** Por objetivo (**intencionados** vs. **no intencionados** por descuido o ignorancia), por lugar (**internos** vs. **externos**, que siempre requieren una ruta física o virtual para volverse internos y tocar el bien, ej. intrusión desde la India a una IP de la UNAM), por visibilidad (**pasivos** —observan/leen/escuchan sin notarse, ej. revisar redes sociales o *sniffing* — vs. **activos** —dañan de inmediato—) y por acción (**modificación, interrupción, intercepción y suplantación/falsificación**).  
> * **Etapas del ataque (3 en intencionados vs. 2 en no intencionados):**  
  1. **Planeación/Preparación (la más larga, semanas o meses; ligada a reconocimiento en MITRE ATT\&CK) :** Definir objetivo, recursos humanos, recursos monetarios (ej. en el ejercicio *Incidente en Salud Integral*, alumnos estimaron precios de expedientes médicos en mercado negro entre \$60 y \$300 por registro o paquetes masivos de $0.55–$0.60), fecha/hora y planes A–Z. *(Falta en ataques no intencionados)*.  
  2. **Activación:** Acción que dispara el ataque (un puerto abierto como el 22, una regla permit mal puesta arriba de deny, una bomba lógica, abrir un PDF malicioso y habilitar edición).  
  3. **Ejecución (Análisis de resultados):** Tanto el atacante como la organización analizan si funcionó, qué falló y qué corregir.  
> * **Perpetradores / Atacantes vs. Agente amenazante:** El **agente amenazante** *podría* dañar, pero el **atacante/perpetrador** es el sujeto que **ya comete o cometió** el ilícito (y un atacante no siempre es igual al tipo de ataque). Se dividen en **insiders** (internos, los más peligrosos porque conocen fallas y credenciales) y **outsiders** (externos, que dependen de internos para tener éxito). Tipos según actividad: *spammer* (correo masivo), *spoofer* (suplantación), *phisher* e *ingeniero social*, **cracker** (busca recompensa: dinero, equipo o fama), **hacktivista** (mencionado en audio como "activistas"), **lamer / script kiddy** (novato que ejecuta scripts sin saber y hasta se daña solo) y **carder** (clonación de tarjetas). Entre **hackers** existen sombrero **blanco** (éticos, buscan fallas para proteger), **negro** (atacan para dañar), **gris** (alternan ambas posturas) y **azul** (usado por Microsoft); en defensa se organizan en **Blue Team** (defensivo) y **Red Team** (ofensivo).

**c) Técnicas de intrusión y su mitigación ( SIB-Clase10.m4a , SIB-Clase13.m4a , SIB-Clase14.m4a ):**

| Categoría | Técnicas de intrusión vistas | Mitigación vista en clase   |
| :---- | :---- | :---- |
| **Redes** | **Escaneo de puertos** , **MITM** (*Man in the Middle* en Wi-Fi abierta como PC Puma), **Sniffing** (tráfico en modo promiscuo), **DoS / DDoS** (saturación; ej. salas A y B con 50–100 alumnos en la misma IP), **Hoax** (alertas falsas para borrar archivos del sistema). | Cerrar puertos innecesarios, reglas de filtrado en **firewall** , **IDS/IPS** , segmentar la red, verificar antes de borrar. |
| **Software y sistemas** | **Exploits** , **Desbordamiento de búfer** (*buffer overflow* ), **Inyección SQL** , software obsoleto sin recursos para migrar. | Actualizaciones, parches y pruebas en **sandbox** (entorno aislado, nunca directo en producción). |
| **Ingeniería social** | Llamadas intimidatorias/engaño (*"compra de \$30,000"* , *"mamá me secuestraron"* ), **Phishing** (masivo) vs. **Spear phishing** (dirigido con datos personales), **Pretexting** (escenario engañoso, ej. billete tirado junto al cajero). | **Autenticación multifactor (MFA)** , detectores de voz/iris, no regalar datos en redes, capacitación vivencial. |
| **Malware** | Virus, gusanos, **Troyanos** (aparentan ser PDF/audio/video), **Ransomware** (secuestro por rescate/clave), **Spyware** , **Rootkits** (ocultan y dan privilegios totales), ataques de diccionario (admin/admin o usuario \= contraseña). | **Un solo antivirus** (no 2 o 3 porque saturan), antimalware, **listas blancas** de apps, cuidar **listas negras** (ej. dominio Outlook baneado), cambiar credenciales por defecto. |
| **Físicos** | Robo de equipos, **keyloggers de hardware** , inyección de hardware (USB maliciosa), **robo hormiga** (cables, teclas, ratones). | Control de acceso físico (bitácoras, torniquetes, mochilas), cámaras, cifrado, bloqueo de sesión, rotación de contraseñas sin repetir (patito1/patito2), uniformes. |

**d) Errores comunes y puntos de examen:**

> * **Preguntado en el examen anterior ( SIB-Clase13.m4a ):** Confundir **agente amenazante** (sujeto con potencial de dañar), **atacante/perpetrador** (sujeto que ya ejecuta el ilícito) y **ataque** (la acción ejecutada).  
> * Subir un respaldo de una web comprometida (ej. index.html con carita feliz en unam.mx) sin detectar ni eliminar el script oculto o la carpeta que dispara el ataque.  
> * Instalar múltiples antivirus al mismo tiempo o creer que todos los hackers son malos.

### ---

**UNIDAD 6: Políticas de Seguridad y Modelos de Seguridad *(Clases 15, 16, 17 y 18\)***

**a) Qué problema resuelve y cómo se conecta:** Para responder la **3.ª pregunta ( ¿cómo proteger? )** de manera institucional y no improvisada, las organizaciones necesitan reglas obligatorias (**políticas**) que eliminen la excusa de la ignorancia, y estructuras lógicas o matemáticas (**modelos**) que traduzcan esas reglas en permisos verificables sobre sistemas y datos.  
**b) Conceptos clave — Políticas de Seguridad:**

> * **Definición y alcance:** Conjunto de reglas y procedimientos formales obligatorios que guían la protección de bienes y eliminan la excusa de la ignorancia; las **Políticas de Seguridad Informática / en Cómputo (PSI / PCI / PCC / PSC)** son un **subconjunto** de las políticas generales de seguridad.  
> * **Vigencia y actualización:** Tienen **vigencia permanente** y **no se actualizan por fechas fijas** (no cada semana, semestre o año), sino únicamente **cuando hay cambios significativos** (fusiones, nueva tecnología, cambio de giro, puestos, áreas o tras incidentes como el examen en línea de la UNAM).  
> * **Los 7 Principios Fundamentales (sin escribir su nombre en la política, sino reflejados en el texto) :**  
  1. **Autorización** (indicar claramente qué sí o no se permite y quién autoriza).  
  2. **Mínimo privilegio** (delimitar qué puesto hace qué).  
  3. **Separación de bienes/funciones** (no concentrar tareas críticas en una sola persona para evitar fraude o parálisis si falta).  
  4. **Reglas de auditoría** (definir cómo y quién revisa los procesos o aplica pruebas).  
  5. **Redundancia** (**positiva**: definir cómo, cuándo y quién hace respaldos; vs. **negativa**: respaldos caóticos tipo proyecto\_final\_bueno\_1 en una USB olvidada).  
  6. **Reducción del riesgo** (reglas para disminuir riesgos lo más posible).  
  7. **Responsabilidad individual** *(obligatoria en todas las políticas: indicar exactamente a quién aplica)*.  
> * **Filosofías y reglas de redacción ( SIB-Clase16.m4a ):**  
  * **Filosofía restrictiva (positiva):** *Todo está prohibido a excepción de lo que expresamente se permite* (se redacta con *"se permite / se puede"*; ej. *"Solo se permite comer manzanas"*).  
  * **Filosofía permisiva:** *Todo está permitido excepto lo que se prohíbe* (se redacta con *"se prohíbe"*; ej. *"Se prohíbe comer manzanas"*).  
  * Redactar en **tiempo presente**, **evitar la palabra "no"** (por psicología inversa/PNL: *"no corro"* hace que el cerebro lea *"corro"*; sustituir por *"evita correr"*), **indicar sujeto/dueño exacto** (incluir a **servicio social, prácticas profesionales, invitados y auditores** internos o pagados), usar lenguaje sin tecnicismos ni siglas sin definir la primera vez, incluir reglas de capacitación y respetar leyes superiores (como la Constitución).  
> * **Equipo multidisciplinario:** Nunca las redacta una sola persona; requiere **autoridad/líder**, **representante jurídico**, **apoyo de redacción/estilo**, **psicólogo laboral** (evita reglas que causen ansiedad o dañen autoestima), **administrador de sistemas** (solo cuando haya sistemas involucrados) y **usuario típico** de prueba.  
> * **Las 7 etapas en orden ( SIB-Clase17.m4a ):** 1\) Planteamiento de objetivos, 2\) Preparación (convocar y llegar con propuestas), 3\) Redacción (revisar alineación en junta), 4\) Edición y apoyo editorial (formato y ortografía), 5\) **Aprobación** (por comisión independiente con sello/QR/leyenda y **control de versiones** 01, 02, 03…), 6\) Difusión (física/digital, examen aprobatorio mínimo 8, pósters con texto e imagen) y 7\) Aplicación y revisión periódica.  
> * **Componentes de la documentación ( SIB-Clase17.m4a ):** Ámbito de aplicación (de media a 5 hojas), análisis de riesgos, enunciados por secciones, sanciones y premios (ej. 7.5 días de sueldo), **referencia a protocolos existentes sin reescribirlos** (ej. Comisión Local de Seguridad), usos éticos/FAQs, procedimientos de incidentes/contingencias (ej. ciberataque a refrigeradores en Francia/Finlandia con pérdidas dobles o triples sobre 50,000 €), **glosario de términos obligatorio en todas** y anexos necesarios.

**c) Conceptos clave — Modelos de Seguridad ( SIB-Clase17.m4a ):**

> * **Definición:** Representación conceptual o matemática de sujetos, recursos, operaciones y reglas que determinan los comportamientos autorizados mediante estados válidos y transiciones.  
> * **Modelo Abstracto vs. Concreto:** El **abstracto** describe reglas generales o matemáticas sin detalles de implementación (*"Sujeto A hace actividad 1"*); el **concreto** aterriza las reglas en el mundo real *"con nombres y apellidos"* (*"Juan puede crear bases de datos"*).  
> * **Comparación de modelos vistos en clase:**

| Categoría | Modelo | Cómo funciona y ejemplo real de clase   |
| :---- | :---- | :---- |
| **Control de acceso** | **Matriz de acceso** | Tabla bidimensional de sujetos vs. objetos cuya intersección indica derechos/obligaciones (ej. Lis usa la PC, Natalia nada, otra persona la limpia). |
| **Control de acceso** | **HRU** *(Harrison, Ruzzo, Ullman)* | Extensión matemática de la matriz que analiza cambios en el tiempo evaluando **condiciones** (ej. Lis usa la PC *solo si* trabaja ahí, en horario laboral y con Wi-Fi 7 disponible). |
| **Control de acceso** | **Take-Grant (TG)** | Grafo dirigido con 2 reglas: **Take** (un superior toma atribuciones del subordinado; ej. la jefa de depto asienta actas si la profesora falta) y **Grant** (un superior delega credenciales a un inferior; ej. jefe a secretaria). |
| **Control de acceso** | **Bell-LaPadula** | Política multinivel para **confidencialidad** (secreto, ultrasecreto, confidencial): jerarquías altas acceden a niveles bajos, pero un nivel inferior nunca accede arriba (ej. alumnos no asientan sus propias calificaciones). |
| **Flujo de información** | **Teoría de la Información / Entropía** | La **entropía** es el **grado de incertidumbre** , inversamente proporcional a la información disponible: a mayor incertidumbre, menos deduce un atacante (ej. cuestionari\_ \= baja entropía vs. \_\_\_\_a donde los alumnos dijeron salsa/araña/pizza y la profesora pensó **"torta"** ). Prohíbe contraseñas en *post-its* o Rodrigo/Rodrigo contra *shoulder surfing* . |
| **Integridad** | **Biba (1977)** | Política multinivel de integridad: sujeto y activo deben estar **exactamente al mismo nivel** para modificar datos (evita que secretarias autoricen compras por teléfono sin el director o suplantaciones con voz de IA). |
| **Integridad** | **Clark-Wilson** | Usa **transacciones bien formadas** y **separación de funciones** , combinando **integridad y confidencialidad** : tener el mismo nivel o puesto no permite leer ni modificar todo (respaldado con avisos de privacidad). |

**d) Errores comunes y puntos de examen ( SIB-Clase18.m4a ):**

> * **Retroalimentación crítica para el proyecto:** Escribir literalmente *"Principio fundamental: mínimo privilegio"* como título/etiqueta en la regla (debe ir **implícito en la redacción**); escribir *"una persona revisará las muestras"* sin cargo exacto; poner *"a menos que esté autorizado"* sin decir qué cargo autoriza; y olvidar a **servicio social, prácticas profesionales, invitados y auditores**.  
> * Omitir el **glosario de términos** (obligatorio en todas las documentaciones) o reescribir protocolos de emergencia que ya existen en la institución.

### ---

**UNIDAD 7: Planes de Contingencia / DRP *(Clases 17 y 18\)***

**a) Qué problema resuelve y cómo se conecta:** Incluso con buenas políticas y modelos, ocurrirán fallas o desastres; los **planes de contingencia** (que van referenciados en la sección de incidentes de las políticas y dependen del análisis de riesgos) aseguran que la organización sea **resiliente** y vuelva a operar en el menor tiempo posible sin caer en pánico.  
**b) Conceptos clave:**

> * **Plan de contingencias (DRP):** Conjunto de protocolos planeados y documentados (en plural porque cubren distintas eventualidades; sinónimos: **Disaster Recovery Plan**, protocolos de calidad, emergencia o recuperación) para recuperarse de desastres y retomar operaciones. Deben elaborarse en **1 a 2 meses** por un **equipo interno del área** (no externos ajenos ni otras áreas como finanzas haciendo el de cómputo) y **separarse por rubro** (sismos, incendios, bases de datos) sin revolverlos.  
> * **4 Fases de un plan de contingencias ( SIB-Clase17.m4a ):** 1\) **Evaluación** (revisar si hay planes o si quedaron obsoletos, ej. citando un "departamento H" inexistente), 2\) **Planeación** (basada obligatoriamente en el análisis de riesgos), 3\) **Ejecución** (aplicarlo en la crisis) y 4\) **Pruebas de viabilidad** (comprobar con simulacros si funciona; ej. el colapso del Colegio Rébsamen demostró un plan no viable por la estructura).  
> * **Procedimientos preventivos vs. correctivos ( SIB-Clase17.m4a ):** Los **preventivos** buscan evitar la eventualidad (verificar vigencia y tipo de extintor, dar cursos); los **correctivos** actúan cuando ya ocurrió y se dividen en **planificados** (persona certificada usando el extintor o cargando entre varios a quien se paralizó en la puerta) y **no planificados** (reacciones instintivas peligrosas del sismo de 2017: gritar, empujar, desmayarse, aventar agua a fuego eléctrico o un saco a alguien electrocutado).  
> * **Los 3 Subplanes temporales ( SIB-Clase18.m4a ):**  
  1. **Plan de Respaldo (Antes):** Preventivo (copias de respaldo en nube \+ control de versiones; localizar/revisar extintor y capacitar relevos A/B/C; contratar seguros de vida antes del siniestro; revisar cableado y cierre de llaves).  
  2. **Plan de Emergencia (Durante):** Correctivo planificado (desconectar servidor de la red y avisar a la extensión; que el titular o relevo accione el extintor; en incendio en casa: avisar, evacuar con mascotas/personas, avanzar agachado con paño húmedo, llamar al 911 afuera, y si arde la ropa **no correr: detenerse, tirarse y rodar**).  
  3. **Plan de Recuperación (Después):** Restablecer operación (encender servidor tras tiempo razonable, validar que cesó el borrado y restaurar último respaldo; recargar extintor, usar seguros o indemnizaciones; reingresar a casa solo tras dictamen de bomberos/protección civil, investigar causa y actualizar plan).  
> * **5 Pasos para planificar e implementar ( SIB-Clase18.m4a ):** 1\) Identificación / análisis de riesgos (3 preguntas), 2\) Evaluación de riesgos (estrategias de recuperación), 3\) Desarrollo de estrategias (prioridades; **una estrategia es planeada y no genera más problemas** —ej. saltar por la ventana para bajar rápido al sótano no es estrategia porque lleva al hospital o la muerte, mejor usar escaleras derechas o elevador según movilidad—), 4\) Desarrollo de procedimientos (recuperación rápida con lo disponible, ej. RTP y patrullas tras incendio en el metro) y 5\) Pruebas de entrenamiento, plan de mantenimiento y **ELABORACIÓN DE DOCUMENTACIÓN** (visual y escrita, sin desechar planes funcionales de administraciones previas).

**c) Ventajas y desventajas en tabla ( SIB-Clase18.m4a ):**

| Ventajas | Desventajas   |
| :---- | :---- |
| Elimina el caos y evita maniobras médicas improvisadas peligrosas. | Menor flexibilidad operativa al seguir un protocolo fijo. |
| Permite actuar aunque sea la primera vez que ocurre el siniestro. | Alto consumo de tiempo y recursos para capacitación y simulacros (especialmente al inicio o con personal nuevo inmediato). |
| Fomenta la cultura de seguridad, concientización y ética de reportar incidentes. | Imposibilidad de prever todos los escenarios (sesgo por experiencia limitada del autor). |
| Acerca la respuesta entre autoridades y personal, aumentando resiliencia y valorando bienes. | **Exceso de confianza** (falsa sensación de seguridad en papel sin probar tiempos ni capacidad física) y **desactualización** (ej. limpiar la bolita de un ratón mecánico). |
| — | **Asignar responsabilidades críticas a servicio social, practicantes o visitas** sin contrato laboral formal *(marcado como "importantísimo")* . |

**d) Errores comunes y puntos de examen:**

> * Pretender hacer copias de seguridad o contratar pólizas **durante o después** del siniestro, o restaurar una base de datos mientras sigue el borrado activo.  
> * Confiar en que las certificaciones sustituyen a los planes de contingencia (sin DRP, ante un fallo atípico las empresas quiebran).  
> * En emergencias de avión/evacuación: el adulto se pone el equipo antes que el menor para poder auxiliarlo.

### ---

**UNIDAD 8: Análisis y Gestión de Riesgos *(Clases 19 y 20\)***

**a) Qué problema resuelve y cómo se conecta:** Es el cimiento cuantitativo, cualitativo y estratégico que alimenta tanto a las **políticas de seguridad** como a los **planes de contingencia**, respondiendo con rigor en orden a las **3 preguntas de seguridad** para saber qué proteger primero, cuánto invertir y qué riesgos residuales aceptar.  
**b) Conceptos clave:**

> * **Terminología base ( SIB-Clase19.m4a ):**  
  * **Aceptación del riesgo:** Decisión consciente del dueño sobre si está dispuesto a tolerar que ocurra el problema y asumir sus consecuencias.  
  * **Manejo del riesgo:** Controles para minimizar riesgos no aceptados; **nunca debe costar más (en tiempo, dinero y esfuerzo) que el bien mismo**, salvo bienes sin precio como vidas humanas (protegidas con seguros de gastos médicos mayores).  
  * **Evaluación del riesgo:** Comparar contra metodologías/tablas o contra análisis previos —**si hay varios previos, tomar siempre el último realizado**, nunca el primero—.  
  * **Pérdidas esperadas:** Suponer siempre el **peor escenario** antes de que ocurra (dejando todo aviso grave **por escrito y con acuse/sello**).  
  * **Riesgo residual:** Nivel mínimo de riesgo que permanece tras aplicar controles y que se acepta (ej. vacunarse para tolerar una gripe leve en casa en vez de terminar intubado; o un seguro que cubre el 80%, dejando un 20% de riesgo residual).  
> * **Recopilación de información y apoyo directivo ( SIB-Clase19.m4a ):** Se usan entrevistas, cuestionarios y *checklists* con **lenguaje amigable** (no preguntar por "ciberataques" a quien no sabe informática), encuestas fluidas sin rangos sesgados (10–20, 30–40 omitiendo el 0), avisos de privacidad/confidencialidad y **evidencia comprobable** (videos o cuestionarios firmados con diferente formato/letra). Sin apoyo de la **alta dirección** (*"carta blanca"* con límites), la gente no coopera.  
> * **Análisis Cuantitativo vs. Cualitativo ( SIB-Clase19.m4a ):** El **cuantitativo** usa dinero, porcentajes, gráficas y fórmulas como **ALE (Expectativa de Pérdida Anual)** (ilustrado con fallos como *Pontiac Aztek* con \>80% de autos sin vender en 2003, último *VW* de Puebla y *Windows 8*); el **cualitativo** evalúa cualidades mediante **colores**, **figuras** (caritas, puntos) o **palabras** (alto/medio/bajo). **Deben usarse ambos juntos**.  
> * **Periodicidad, FODA y jerarquía de áreas ( SIB-Clase19.m4a ):** Se realiza **cada vez que hay cambios significativos** (igual que las políticas: fusiones, cambio de misión/visión, nuevas tecnologías, cambios de puestos). Áreas no técnicas usan la **matriz FODA** como resumen rápido. En entidades grandes (ej. Facultad de Ingeniería con 7 departamentos), se analiza **por departamento y de abajo hacia arriba** antes de subir a división.  
> * **Desigualdad económica de seguridad ( SIB-Clase20.m4a ):** Costo del ataque (dinero, tiempo, esfuerzo)\>Valor del bien (recurso)\>Costo de la protección *Ejemplos con números reales:* Si un celular cuesta **\$10,000**, robarlo debe costarle al atacante más de \$10,000 (salvo que obtenga \$20,000 de datos adentro), y protegerlo no debe costar \$50,000 o \$100,000 ("sale más caro el caldo que las albóndigas"); en IBM, si comprar dispositivos de \$23,000 y pagar $2,000a5personas($10,000) cuesta más que los \$5,000 que vale la BD en el mercado negro (o si el retraso empuja el ataque al día siguiente cuando los empleados vuelven de Nueva York), el ataque fracasa. En redes se inyecta tráfico constante las 24 h para elevar la incertidumbre y el costo en tiempo del atacante. *Excepción:* Las personas y empleados clave no tienen precio (*priceless*), por lo que la protección hacia ellos nunca es excesiva.  
> * **Gestión de riesgos, infraestructuras y procesos críticos y escenarios ( SIB-Clase20.m4a ):** La **gestión** administra los riesgos y enlaza con DRP. Las **infraestructuras críticas** son vitales para operar (en casa: internet, luz, agua, gas). Los **procesos críticos** son actividades esenciales jerarquizadas que no pueden parar en ningún escenario (ej. en McDonald's: **cobranza** —porque si regalan Cajitas Felices quiebran—, refrigeración, pedidos, preparación, inventarios, proveedores). Los **escenarios de riesgo** describen detalladamente amenazas, vulnerabilidades y respuestas ante lo peor (ej. quedarse sin agua y contratar pipa o cerrar).  
> * **5 Técnicas rápidas ( SIB-Clase20.m4a ):** 1\) **What if** (preguntas hipotéticas encadenadas), 2\) **APR (Análisis Preliminar de Riesgos)** (línea base al inicio por escrito para comparar *antes vs. después*), 3\) **Los cinco porqués** (**exactamente 5** preguntas sucesivas para hallar la causa raíz), 4\) **FMEA** (clasifica fallas midiendo **frecuencia, gravedad/impacto y quién/cómo las detectó**) y 5\) **Checklist** (lista detallada con incisos Sí/No verificables).  
> * **Matriz de riesgos NIST ( SIB-Clase20.m4a ):** Tabla donde Nivel de riesgo \= Probabilidad × Impacto (ej. matriz 5 × 5 del 1 al 25), usando colores **NIST** (rojo \= alto, amarillo/naranja \= moderado, verde \= muy bajo) y **rangos mutuamente excluyentes** con justificación escrita.

**c) Los 8 pasos del Análisis de Riesgos ( SIB-Clase19.m4a ) y ejemplo de Matriz NIST ( SIB-Clase20.m4a ):**

| Pregunta de seguridad | Pasos obligatorios si no se sigue una metodología específica (SIB-Clase19.m4a)   |
| :---- | :---- |
| **1\. ¿Qué proteger?** | **Paso 1:** Identificar bienes indispensables y evaluar su valor (cuantitativo, cualitativo o ambos) y jerarquía *(15 bienes en el proyecto)* . |
| **2\. ¿De qué proteger?** | **Pasos 2, 3 y 4:** Identificar y describir con claridad amenazas; identificar y describir con precisión vulnerabilidades; determinar impacto y frecuencia de ocurrencia (con estadísticas reales). |
| **3\. ¿Cómo proteger?** | **Pasos 5, 6 y 7:** Identificar controles actuales y qué hacen; determinar riesgos residuales (en conclusiones); emitir recomendaciones **sin marcas ni proveedores** (solo características o perfiles). |
| **Transversal** | **Paso 8:** Elaborar el **informe** con evidencias firmadas/grabadas, introducción, conclusiones, referencias, **sin poner las 3 preguntas literalmente como títulos** . |

*Ejemplo válido de rangos en Matriz NIST* *5 × 5* *(* *Probabilidad × Impacto* *):* **1 a 5 \= Bajo (Verde)**, **6 a 12 \= Medio (Amarillo)**, **15 a 25 \= Alto (Rojo)**.  
**d) Errores comunes y puntos de examen:**

> * En **matrices de riesgo**: traslapar rangos (1–5 y 5–12), pintar el mismo puntaje (4 o 5\) de dos colores distintos según criterio subjetivo ("de contentillo"), o quitar los números dejando solo palabras y colores.  
> * Hacer el análisis de riesgos en solitario (debe hacerse en **grupos con distintas capacidades**: observación, escucha, tacto) o comunicar hallazgos en "pláticas de café junto al microondas" sin dejarlo por escrito.  
> * En el **informe del proyecto**: incluir marcas/proveedores, olvidar evidencias, poner títulos literales de las 3 preguntas, o cotizar un trabajo sin revisar primero las condiciones de la empresa.

## ---

**LO QUE MÁS PROBABLEMENTE VIENE EN EL FINAL**

> 1. **Diagrama del contexto de seguridad y diferencia entre Agente Amenazante, Atacante y Ataque:** Volvió a aparecer en el primer examen parcial, y la profesora recalcó explícitamente en SIB-Clase13.m4a que suelen confundirlos (agente amenazante \= potencial, atacante \= sujeto en el ilícito, ataque \= acción consumada).  
> 2. **Ciclo PDCA continuo vs. Auditorías (internas/externas y hallazgos):** En SIB-Clase14.m4a corrigió explícitamente un error masivo del primer examen: el PDCA no se hace solo cuando hay auditoría, sino continuamente. Además, en SIB-Clase1.m4a explicó con detalle las auditorías de 1.º, 2.º y 3.º nivel y los tres tipos de hallazgos (oportunidad de mejora, observación, no conformidad).  
> 3. **Evolución e identificación de Normatividad y Estándares (en especial ISO 27001 vs. 27002 y Common Criteria):** Ya aplicó un examen rápido de 10 preguntas sobre estos estándares en SIB-Clase4.m4a y recalcó en SIB-Clase3.m4a la diferencia entre norma obligatoria vs. estándar, qué hacer (27001, certificable) vs. cómo hacerlo (27002, no certificable) y las partes/EAL de ISO 15408\.  
> 4. **Los 6 Servicios de seguridad (en especial los 3 factores de autenticación) y las 4 clasificaciones de Mecanismos \+ Principio de profundidad:** Ocupó dos clases teóricas completas y una práctica larga en parejas (SIB-Clase5.m4a y SIB-Clase14.m4a), enfatizando cómo los mecanismos satisfacen necesidades y por qué el modelo OSI solo considera 5 servicios.  
> 5. **Diferenciación estricta entre Amenaza y Vulnerabilidad (redacción "qué falta / de qué carezco") \+ CVSS/CVE/NVD:** Dedicó cuatro sesiones (SIB-Clase6.m4a a SIB-Clase10.m4a) con ejercicios de 20 reactivos para corregir la confusión entre acción dañina y carencia, y comparó las escalas de CVSS v2 vs. v3/v4.  
> 6. **Clasificación de ataques, las 3 etapas de ataques intencionados y mitigación:** Realizó un ejercicio en equipo sobre el hospital (*Salud Integral*, SIB-Clase12.m4a) para desglosar preparación, activación y ejecución, y remarcó que prevenir cuesta menos que recuperarse (SIB-Clase10.m4a, SIB-Clase13.m4a, SIB-Clase14.m4a).  
> 7. **Reglas de redacción de Políticas de Seguridad (principios sin nombrarlos, filosofías, sin "no", figuras fuera del organigrama y 7 etapas):** Evaluó minuciosamente una práctica de 15 políticas (SIB-Clase16.m4a), dedicó gran parte de SIB-Clase18.m4a a corregir errores y advirtió explícitamente que no deben repetirse en el proyecto.  
> 8. **Modelos de seguridad (Concretos vs. Abstractos, Matriz, HRU, Take-Grant, Bell-LaPadula, Entropía, Biba vs. Clark-Wilson):** Pidió definiciones para participación y resolvió ejemplos en el pizarrón para cada modelo (SIB-Clase17.m4a), contrastando en especial la entropía inversa, *Take* vs. *Grant* y Biba vs. Clark-Wilson.  
> 9. **Planes de contingencia (DRP): 4 fases, procedimientos preventivos/correctivos, 3 subplanes temporales y 5 pasos:** Resolvió ejercicios de bases de datos, extintores, bajar al sótano e incendios en casa (SIB-Clase17.m4a y SIB-Clase18.m4a), proyectó el esquema de 5 pasos y señaló como *"importantísimo"* no delegar roles críticos a servicio social.  
> 10. **Desigualdad económica de costos, 3 preguntas en orden, 8 pasos, 5 técnicas rápidas y Matriz de Riesgos NIST:** Concentró las últimas dos sesiones (SIB-Clase19.m4a y SIB-Clase20.m4a) en estos temas con ejercicios numéricos (celular de \$10,000, BD de IBM, McDonald's), anunció que en el proyecto van 15 bienes sin marcas y pidió repasar matrices NIST para otro ejercicio antes del final. *(Nota: la profesora aún definirá si el examen final será individual o en equipo y si se aplica martes o jueves de la última semana* *).*

## ---

**CONEXIONES CLAVE**

> 1. Tres preguntas de seguridad \-\> estructuran \-\> Esquema de seguridad y análisis de riesgos.  
> 2. Ciclo PDCA \-\> garantiza mediante mejora continua \-\> Dinamismo de la seguridad.  
> 3. Auditoría (1.º, 2.º y 3.º nivel) \-\> verifica \-\> Cumplimiento del ciclo PDCA y estándares.  
> 4. No conformidad en auditoría \-\> impide o revoca \-\> Certificación de la organización.  
> 5. TCSEC, ITSEC y CTCPEC \-\> convergen en \-\> Common Criteria (ISO/IEC 15408).  
> 6. BS 7799 (Partes 1 y 2\) \-\> evoluciona hacia \-\> ISO/IEC 27002 e ISO/IEC 27001\.  
> 7. ISO/IEC 27002 (no certificable) \-\> apoya la implementación de \-\> SGSI certificable de ISO/IEC 27001\.  
> 8. Entorno de seguridad \-\> condiciona \-\> Objetivos de seguridad y elección de controles.  
> 9. Servicios de seguridad (necesidades) \-\> son satisfechos por \-\> Mecanismos o controles de seguridad.  
> 10. Control de acceso \-\> requiere obligatoriamente \-\> Autenticación previa de identidad.  
> 11. Principio de profundidad \-\> combina múltiples capas de \-\> Mecanismos de seguridad compatibles.  
> 12. Factor humano \-\> representa \-\> Principal fuente de amenazas y eslabón más débil.  
> 13. Amenaza latente \-\> explota \-\> Una o varias vulnerabilidades (omisiones o carencias).  
> 14. Ocurrencia de amenaza × consecuencia \-\> determina \-\> Nivel de riesgo sobre un bien.  
> 15. Vulnerabilidad identificada en CVE \-\> recibe ponderación de severidad en \-\> NVD mediante CVSS.  
> 16. Agente amenazante \-\> se convierte en \-\> Perpetrador o atacante al cometer el ilícito.  
> 17. Ataque externo \-\> necesita ruta física o virtual (con ayuda interna) para \-\> Volverse interno y dañar el bien.  
> 18. Ataques intencionados \-\> siguen tres etapas \-\> Planeación, activación y ejecución/análisis.  
> 19. Prevención planificada \-\> cuesta menos en tiempo, dinero y personal que \-\> Recuperación tras un ataque.  
> 20. Cambios significativos \-\> detonan la actualización de \-\> Políticas de seguridad y análisis de riesgos.  
> 21. Principios fundamentales \-\> deben reflejarse implícitamente sin nombrarse en \-\> Redacción de políticas.  
> 22. Psicólogo laboral y representante jurídico \-\> previenen sesgos e ilegalidades en \-\> Equipo redactor de políticas.  
> 23. Modelo abstracto \-\> se aterriza con identidades reales en \-\> Modelo concreto.  
> 24. Matriz de acceso \-\> incorpora evaluación de condiciones temporales y tecnológicas en \-\> Modelo HRU.  
> 25. Alta entropía (incertidumbre) \-\> dificulta que un atacante deduzca secretos en \-\> Modelos de flujo de información.  
> 26. Modelo Biba (mismo nivel) \-\> se amplía con transacciones bien formadas y confidencialidad en \-\> Modelo Clark-Wilson.  
> 27. Análisis de riesgos \-\> sirve como base obligatoria (Paso 1\) para diseñar \-\> Planes de contingencia (DRP).  
> 28. Subplanes de Respaldo, Emergencia y Recuperación \-\> ordenan cronológicamente procedimientos \-\> Preventivos y correctivos.  
> 29. Desigualdad económica de seguridad \-\> exige que el costo del ataque supere al bien y \-\> Protecciones cuesten menos que el bien.  
> 30. Infraestructuras críticas \-\> soportan la operación continua de \-\> Procesos críticos jerarquizados.  
> 31. Técnicas rápidas (What if, APR, 5 porqués, FMEA, Checklist) \-\> alimentan con evidencias \-\> Matriz de riesgos NIST.  
> 32. Rangos mutuamente excluyentes (Probabilidad × Impacto) \-\> evitan evaluaciones subjetivas en \-\> Matriz de riesgos.

---

🎯 ¿Quieres que armemos un examen simulacro completo (con preguntas abiertas, casos de matrices NIST, clasificación de subplanes y detección de errores en políticas) para poner a prueba esta guía?