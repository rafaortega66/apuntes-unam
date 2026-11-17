# **ASI · Guía para el examen final**

**Administración de Servicios de Internet** · Semestre 2027-1 · 16 nov 2026  
*Hecha con NotebookLM a partir de todas las fuentes del cuaderno de la materia (audios de cada clase y material del profesor): hilo conductor del curso, unidades con sus conceptos explicados, lo que más probablemente viene y las conexiones entre conceptos. Acompáñala con el mapa mental (ASI-mapa-mental.pdf, en esta misma carpeta).*  
*Clases que no estaban en el cuaderno: 12\. Su resumen va en el Anexo al final.*  
**Nota sobre las fuentes:** Todas las fuentes disponibles en el cuaderno corresponden a las grabaciones de las 18 clases (ASI-Clase1.mp3 a ASI-Clase11.m4a y ASI-Clase13.m4a a ASI-Clase19.m4a; no hay grabación de Clase 12 ni presentaciones/PDFs independientes cargados del profesor). Cuando algún dato visual de diapositivas no quedó verbalizado en el audio, se indica expresamente.

## ---

**1\. HILO CONDUCTOR**

El curso parte desde la base física y lógica de la máquina hasta los estándares globales que gobiernan internet: primero se entiende cómo ejecuta instrucciones un procesador, cómo se elimina el cuello de botella de Von Neumann mediante arquitecturas RISC con *pipeline* y cómo se organiza y administra un sistema operativo Linux por consola (permisos, directorios y procesos), porque todo servicio de internet corre en última instancia sobre hardware y un sistema operativo (Clase 1). Una vez dominada la máquina local, antes de levantar cualquier infraestructura, se aprende a planificar y controlar el trabajo de ingeniería eligiendo entre metodologías tradicionales (Cascada/PMBOK) y ágiles (Scrum), definiendo qué hace un servidor frente a un simple repositorio, levantando requerimientos (funcionales, no funcionales y de sistema) y modelando la arquitectura en UML para que el código coincida con el diseño (Clases 2, 3, 5, 6, 7).  
Con el proyecto planificado y los requerimientos claros, se construye y protege la infraestructura: primero se despliegan servicios en la nube (controlando presupuestos y alertas en dólares) y servicios esenciales de red local/corporativa (DHCP y DNS) para automatizar el direccionamiento y evitar conflictos (Clases 3, 4); luego se evalúa la seguridad real de esos servidores mediante pentesting (Metasploit y Nmap en Kali Linux) y se blinda la capa de datos auditando quién modifica la información mediante usuarios, roles, privilegios y *triggers* en Oracle (Clases 8, 9, 14). A partir de esos datos ya resguardados y auditados, se da el salto analítico para convertir datos crudos en decisiones ejecutivas usando cubos OLAP, Data Warehouse, Power BI y encuestas reales como la ENOE (Clases 10, 11, 13); finalmente, el curso conecta la tecnología con el negocio y la normatividad: analiza cómo la transformación digital, la IA y el *Big Data* redefinen las profesiones sin reemplazar el criterio de calidad y auditoría humana, y cierra regresando a la raíz teórica oficial del temario mediante los **RFCs**, que documentan las reglas exactas de cada protocolo visto en el semestre (HTTP, IMAP, POP3, LDAP, IANA, Telnet, DNS, DHCPv6/NIS y TLS 1.3) (Clases 15, 16, 17, 18, 19).

## ---

**2\. UNIDADES Y TEMAS DEL CURSO**

### **UNIDAD 1: Fundamentos de Arquitectura Computacional y Administración en Linux (Clase 1\)**

#### **(a) Problema que resuelve y conexión con el curso**

Explica por qué los procesadores reales necesitan arquitecturas eficientes más allá de las matemáticas ideales y cómo operar por línea de comandos el sistema operativo base (Linux) donde se instalarán los servidores de las unidades siguientes (Clase 1).

#### **(b) Conceptos clave**

> * **Procesador, Máquina de Turing y Arquitectura de Von Neumann (Clase 1\)**  
  * *Definición:* Un procesador es el elemento central de la computadora encargado de realizar cálculos de información tomando algoritmos y valores desde la memoria principal. La Máquina de Turing es un autómata de doble pila con cinta infinita y operaciones básicas (moverse a izquierda/derecha, leer y escribir) capaz de resolver cualquier algoritmo. La arquitectura de Von Neumann implementa electrónicamente ese modelo con un **controlador**, un **registro de estado**, un **registro de propósito general**, un **contador de programa** y una **ALU**, operando sobre una memoria única que contiene programa, datos y pila.  
  * *Analogía:* Es como una cocina donde un solo chef (la ALU/procesador) tiene que caminar hasta una única despensa (la memoria) por la receta, luego volver por los ingredientes, cocinarlos y regresar a guardar el platillo en el mismo estante; funciona para cualquier receta, pero todos los demás utensilios quedan parados mientras él camina.  
  * *Ejemplo concreto:* En clase se analizó un bucle for (i \= 0; i \< n; i++) en estilo CISC: para set (i \= 0\) hay 3 accesos a memoria, para JL (salta si menor) hay 4 accesos a memoria (instrucción, i, n y dirección de salto), y en el incremento vuelve a leer de memoria, cargar a ALU y escribir, dejando inactivos el bus, el decodificador o la ALU en cada paso.  
> * **Arquitectura Harvard RISC, Modelo *Load/Store* y *Pipeline* (Clase 1\)**  
  * *Definición:* Propuesta estudiada por Patterson (mencionado como Peterson) que parte la cinta única de Von Neumann en dos memorias separadas —una de instrucciones (solo lectura) y otra de datos (lectura/escritura)— para trabajar con instrucciones simples de carga/almacenamiento (*load/store*) y ejecutar etapas en paralelo mediante *pipeline* (Fetch, Decode, Execute, Write Back).  
  * *Analogía:* Es convertir la cocina en una línea de ensamblaje de hamburguesas con cuatro estaciones: mientras el plato 1 pasa a cocinarse (*Execute*), el plato 2 ya se está preparando (*Decode*) y el pedido 3 ya se está leyendo (*Fetch*).  
  * *Ejemplo concreto:* Al reescribir el bucle en RISC, el profesor calculó el porcentaje de uso real de la ALU: en el primer bloque de **3 instrucciones** (LDA, LDC, STA), solo **1** usa la ALU (**33% de uso, 66% de desperdicio**); en el segundo bloque de **5 instrucciones**, solo **1** usa la ALU (**20% de uso, 80% de no cómputo**). Al alinear todas las operaciones al mismo tiempo en *pipeline* de 4 etapas, tras el arranque inicial se obtiene **1 instrucción terminada por cada ciclo de reloj**.  
> * **Jerarquía de directorios y distribuciones de Linux (Clase 1\)**  
  * *Definición:* Estructura jerárquica a partir de / (*root*) que separa binarios, arranque, dispositivos, configuraciones, usuarios y temporales, y variantes (distribuciones) adaptadas a distintos niveles de estabilidad o uso.  
  * *Analogía:* Es un edificio corporativo donde la recepción y dirección general (/root) controlan el acceso maestro, el cuarto de máquinas (/boot y /dev) maneja la energía y periféricos, el archivo de planos (/etc) guarda las reglas del edificio y los cubículos personales (/home) pertenecen a cada empleado.  
  * *Ejemplo concreto:* Se explicó la diferencia entre /var (temporales que se eliminan al momento) y /tmp (temporales donde un error puede recuperarse mediante *recovery* mientras no se reinicie el equipo y se sobrescriba la RAM), y cómo /opt guarda software adicional instalado por un usuario.  
> * **Permisos, procesos y flujo en consola Linux (Clase 1\)**  
  * *Definición:* Sistema de control de acceso dividido en 4 partes (tipo/directorio, propietario, grupo y otros) con tres permisos básicos —r (leer), w (escribir) y x (ejecutar)— junto con comandos de gestión de archivos, búsqueda y monitoreo de procesos (PID, TTY, TIME, CMD).  
  * *Analogía:* Es el gafete de una oficina con zonas restringidas: los de sistemas forman un **grupo**, tú eres el **propietario** de tu escritorio, y los visitantes en la red de invitados son **otros** (a quienes jamás debes dar llave maestra 777).  
  * *Ejemplo concreto:* mkdir reprobaditos crea una carpeta casi 777 (salvo escritura para otros); dar permiso x a otros en archivos/carpetas permite entrar o ejecutar código malicioso. Con mkdir \-m 700 reprobados21 solo el propietario lee, escribe y ejecuta.

#### **(c) Tablas de referencia técnica (Clase 1\)**

**Directorios clave de Linux:**

| Directorio | Función principal explicada en clase | Prioridad / Nota clave   |
| :---- | :---- | :---- |
| / (root) | Ruta base inicial del sistema | Dirige todo el sistema |
| /boot | Arranque del sistema y *kernel* | Alta; no confundir con /bin |
| /bin | Comandos esenciales ejecutables por usuarios (cd, ls) | Alta; equivalente crítico a System32 |
| /dev | Dispositivos externos e internos (*drivers*) | Clave para discos, impresoras, escáneres |
| /etc | Archivos de configuración del sistema y aplicaciones | Alta |
| /home | Carpetas personales de los usuarios | Alta; organización por usuario |
| /var | Temporales y archivos ocultos que se eliminan al instante | Media |
| /usr | Programas, bibliotecas, documentación y archivos estáticos | Alta |
| /tmp | Temporales recuperables antes de reiniciar (antes de liberar RAM) | Baja |
| /root, /lib, /opt | Directorio del superusuario, librerías y software adicional de usuario | /root media |

**Distribuciones de Linux según uso:**

| Distribución | Uso recomendado en clase | Observación clave   |
| :---- | :---- | :---- |
| **Linux Mint / Ubuntu** | Principiantes / usuario final | Interfaz parecida a Windows; Ubuntu cambia mucho de versión/parches |
| **Debian** | Servidores (alta estabilidad) | Muy estable |
| **Fedora** | Desarrollo y programación | Soporte rápido a hardware reciente (Bluetooth, inalámbricos) |
| **CentOS \-\> AlmaLinux** | Servidores de almacenamiento | Copias gratuitas de **Red Hat** (de pago); CentOS sin soporte desde 2017–2019 |
| **Arch Linux** | Usuarios avanzados (instalación manual personalizada) | No vale la pena si se instala con "siguiente, siguiente" |
| **Kali Linux** | 100% ciberseguridad | Más de 600 herramientas precargadas (Clases 1, 8\) |

**Comandos de Linux vistos en clase:**

| Comando | Qué hace exactamente según la clase   |
| :---- | :---- |
| whereis \<cmd\> vs which \<cmd\> | whereis muestra todas las carpetas del paquete; which muestra únicamente la ruta del ejecutable (útil para migraciones o buscar ejecutables como en Oracle). |
| pwd | Imprime el directorio actual completo (evita encadenar cd ..). |
| man \<cmd\> | Muestra el manual del comando offline (Ctrl+Z / salir). |
| ps / ps aux / kill / top | Lista procesos (PID, TTY terminal origen, TIME, CMD); en ps aux: a todos los usuarios, u recursos CPU/RAM, x procesos sin terminal asociada (primero a revisar si entra un virus); kill mata por PID; top muestra procesos en tiempo real. |
| nano | Editor de texto en terminal; se sale con Ctrl+X. |
| cat / cat \-n / \> | Visualiza archivos; \-n numera líneas; cat a.txt b.txt \> todito.txt concatena en un nuevo archivo respetando el orden de los argumentos. |
| ls \-l / \-a / \-s / \-lsa | \-l detalles (permisos, propietario, peso, fecha); \-a incluye ocultos (inician con .); \-s peso en KB; se combinan como ls \-lsa. |
| mkdir \-m \<modo\> / mkdir \-p / tree | \-m asigna permisos al crear (ej. 644, 700); \-p crea árbol completo de carpetas; tree muestra la estructura de árbol. |
| Otros pedidos en resultados | mv, rm, ls con \-d/-h/-R mayúscula, grep, wc, touch, cambio de permisos/propietario en archivos y carpetas (chmod/chown mencionados como instrucciones distintas para archivos y carpetas). |

#### **(d) Errores comunes y puntos de examen (Clase 1\)**

> * Confundir /usr con carpeta de usuarios (es para programas y bibliotecas estáticas, los usuarios van en /home).  
> * Usar mkdir carpeta1/carpeta2/carpeta3 sin \-p (falla si las carpetas padre no existen) ni confundir \-m (modo/permisos) con \-p (ruta padre).  
> * Usar permiso 777 o dejar permiso x abierto a otros usuarios.  
> * Creer que whereis y which devuelven lo mismo, o que cat solo sirve para leer un archivo.

### ---

**UNIDAD 2: Gestión, Requerimientos y Modelado de Proyectos de Servicios (Clases 2, 3, 5, 6, 7\)**

#### **(a) Problema que resuelve y conexión con el tema anterior**

Antes de configurar servicios sobre Linux, un equipo de ingeniería debe decidir cómo planificar entregas, presupuesto, responsabilidades, requisitos y planos técnicos para no perder alcance, dinero ni coherencia entre lo diseñado y lo programado (Clases 2, 3, 5, 7).

#### **(b) Conceptos clave**

> * **Metodología Tradicional (Cascada / PMBOK) (Clases 2, 5\)**  
  * *Definición:* Enfoque predictivo basado en fases secuenciales (análisis, diseño, implementación, pruebas, mantenimiento), planificación anticipada, requisitos fijos desde el inicio, documentación extensa y entrega única al final, gobernado por el **triángulo de hierro** (alcance, costo y tiempo). PMBOK (PMI, "libro rojo") abarca inicio, planificación, ejecución, monitoreo/control y cierre sobre 10 áreas de conocimiento (integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones e interesados) bajo un **Project Manager**.  
  * *Analogía:* Construir una casa con planos arquitectónicos aprobados: no puedes levantar el segundo piso si no terminaste los cimientos, y si a media obra el cliente quiere quitar una columna, se recalcula todo y se cobra aparte.  
  * *Ejemplo concreto:* Caso de la página de vacunación COVID en España que se cayó a los 10 minutos por saltar la etapa de pruebas al salir a producción; en clase se aplicó en Microsoft Project con fechas límite fijas (16 de noviembre inicialmente).  
> * **Metodologías Ágiles y Scrum (Clases 2, 5, 6\)**  
  * *Definición:* Ágil es la metodología (nacida del Manifiesto Ágil de 2001\) basada en cuatro pilares —**iterativo, incremental, colaborativo y adaptable**— y **Scrum** es un marco que la implementa mediante ciclos cortos llamados *sprints* (2 a 4 semanas) que producen incrementos potencialmente utilizables.  
  * *Analogía:* Entregar una aplicación por partes funcionales: en la junta 1 muestras el *layout* y altas; en la 2 altas y bajas; en la 3 altas, bajas y cambios. Si en la arquitectura se exagera la complacencia al cliente, terminas poniendo un candelabro en el Metro Hidalgo que no sirve funcionalmente pero cumple lo que pidió el cliente.  
  * *Ejemplo concreto:* En el curso, los equipos en Scrum debían hacer *Daily* (15 min) con bitácora y al menos **2 avances semanales en Git** (lunes y miércoles) más reporte semanal. En proyectos ágiles el profesor recomendó sumar **\+15% de margen al presupuesto** por cambios (ej. si cuesta 1 millón, cotizar \+15%). Mencionó como malos ejemplos de adaptación excesiva la Línea 12 del Metro e Infonavit.  
> * **Planificación en Microsoft Project (Recursos y Costos) (Clase 2\)**  
  * *Definición:* Herramienta de diagramas de Gantt que vincula predecesoras (ej. 4CC \= comienzo a comienzo) y asigna tres tipos de recursos: **Trabajo** (personas/equipos por tiempo), **Material** (bienes que se compran/entregan una vez al cliente) y **Costo** (gastos fijos permanentes como luz, internet o renta, independientemente de si hay proyecto).  
  * *Analogía:* Una computadora puede ser **Trabajo** (ahorras \$3/semana por desgaste), **Material** (compras una Mac Mini de \$27,000 o terminal de Oxxo y se la cobras/entregas al cliente) o **Costo** (el trabajador usa su propia PC en casa).  
  * *Ejemplo concreto:* En vivo, al asignar todos los recursos al nivel 1 del proyecto, Project arrojó **51.13 días \= 3,272 horas-hombre y \$34,000**; al asignar correctamente por tarea (Luisa análisis, Paola requerimientos funcionales, Fernando no funcionales —sin traslapar dos tareas simultáneas a Paola—), bajó a **304 horas y \$812.50**.  
> * **Levantamiento de Requerimientos y UML (Clases 3, 5, 7\)**  
  * *Definición:* Existen exactamente tres tipos de requerimientos: **de Sistema** (hardware, servidores, ancho de banda), **Funcionales** (*qué* hace el sistema: entradas/salidas/interacción) y **No Funcionales** (*cómo* se mide: eficiencia, rapidez, facilidad de uso). **UML** (*Lenguaje Unificado de Modelado*) documenta la estructura y comportamiento del software (incluyendo componentes, despliegue y casos de uso).  
  * *Analogía:* Si vas a una agencia por un auto, "que tenga 4 llantas y motor" es de sistema; "que frene cuando piso el pedal" es funcional; "que frene en menos de 2 segundos" es no funcional.  
  * *Ejemplo concreto:* Ejercicios resueltos en clase: *"El usuario debe loguearse"* \-\> **Funcional**; *"Tiempo de respuesta muy corto"* \-\> **No funcional** (mide); *"Múltiples servidores para disponibilidad"* \-\> **Sistema**; *"Amplio ancho de banda para streaming"* \-\> **Sistema**; *"Enviar email semanal"* \-\> **Funcional**; *"Interfaz sencilla y fácil de usar"* \-\> **No funcional**.  
> * **Especificaciones del Proyecto Final (Clases 5, 6, 7, 17, 19\)**  
  * *Definición:* Implementación de servicios reales sobre **2 a 3 máquinas virtuales** combinando Linux y Windows (si el servidor es Ubuntu Server, el cliente es Windows; si es Windows Server, el cliente es Linux) con red, servicios, seguridad y evidencias.  
  * *Analogía:* Un simulacro empresarial completo donde no basta que el sistema funcione en tu laptop: debes entregar los planos de instalación (manual técnico), el instructivo para empleados (manual de usuario) y la grabación probando que tus propios planos sí levantan el servicio.  
  * *Ejemplo concreto:* Los 10 proyectos asignados abarcan: 1\) Intranet empresarial (DNS interno \+ Apache \+ HTTPS), 2\) Correo (DNS \+ SMTP \+ POP3 \+ IMAP \+ autenticación), 3\) Acceso remoto seguro (SSH \+ grupos/permisos \+ FTP), 4\) Archivos Samba por CLI, 5\) Web con BD (PHP/Java/Python \+ BD excepto SQL Server por licencias; CRUD), 6\) Web con balanceo de cargas / espejo, 7\) Infraestructura escolar (DHCP \+ DNS \+ Web \+ Samba), 8\) Web HTTPS (SSL/TLS \+ 2FA), 9\) Archivos y remoto multiplataforma (Windows/Linux), 10\) Proxy con control de accesos y *triggers*/bitácora.

#### **(c) Comparación Tradicional / PMBOK vs. Ágil / Scrum (Clases 2, 5, 6\)**

| Criterio | Tradicional / Cascada / PMBOK | Ágil / Scrum   |
| :---- | :---- | :---- |
| **Planificación y requisitos** | Detallada y anticipada; requisitos fijos desde el inicio | Iterativa y continua; evoluciona durante el proyecto |
| **Entregas** | Única entrega al final (3 revisiones en clase: inicio, mitad, final) | Frecuentes e incrementales (sprints 2–4 sem; en clase 2 avances/sem en Git \+ reporte semanal) |
| **Participación del cliente** | Puntual (inicio, mitad y entrega) | Constante (Daily, Review) |
| **Documentación** | Extensa (Acta inicio, RF/RNF, Casos uso, BD, Pruebas, Control cambios) | Ligera/esencial (Visión, Product Backlog con HU, Sprint Backlog, bitácora Git) |
| **Cambios** | Costosos, requieren control formal y nueva factura | Bienvenidos; Scrum no reajusta precio fácilmente (añadir \+15% colchón) |
| **Rol central** | Project Manager (responsable único) | Scrum Master \+ Product Owner \+ Equipo |

#### **(d) Errores comunes y puntos de examen (Clases 2, 3, 5, 6, 7\)**

> * **Decir que "Scrum es la metodología":** El profesor recalcó que **Ágil** es la metodología y **Scrum** es quien la implementa (como redes vs Cisco).  
> * **Confundir requerimientos:** Escribir un requerimiento sin separar qué es *Sistema* (hardware/red), *Funcional* (acción) y *No Funcional* (métrica).  
> * **Inconsistencia UML–Código:** El profesor advirtió que si los diagramas UML entregados no coinciden con la programación del proyecto, estará mal.  
> * **Cambiar de metodología a medio curso:** Automáticamente reprobado. En la evaluación final del proyecto, si un integrante no sabe responder, reprueba todo el equipo.  
> * *(Nota de transparencia: En el audio de Clase 7 solo se nombran explícitamente los diagramas de componentes, despliegue y casos de uso; la lista completa de la diapositiva proyectada no fue leída en voz alta \`\`.)*

### ---

**UNIDAD 3: Servidores, Nube y Servicios Esenciales de Red (DHCP y DNS) (Clases 3, 4\)**

#### **(a) Problema que resuelve y conexión con el tema anterior**

Una vez definidos los requerimientos de sistema, debemos elegir dónde hospedar la infraestructura (local o nube como Azure) y automatizar la comunicación entre clientes y servidores sin configurar direcciones IP a mano ni confundir almacenamiento pasivo con procesamiento activo (Clases 3, 4).

#### **(b) Conceptos clave**

> * **Servidor vs. Repositorio y Pirámide DIK (Clase 3\)**  
  * *Definición:* Un **servidor** es un equipo hardware o software (proceso computacional) que ofrece y comparte servicios o recursos —y ejecuta procesos como CRUD, simulaciones o redes neuronales— a uno o más clientes a través de una red (internet o intranet local). Un **repositorio** (ej. Git) solo almacena datos estructurados o no estructurados sin ejecutarlos por sí mismo. La pirámide **DIK** transforma **Datos** (nivel más bajo) \-\> **Información** (al darles contexto) \-\> **Conocimiento** (decisiones basadas en estadística/algoritmos).  
  * *Analogía:* Un repositorio es una bodega de cajas donde guardas ingredientes o planos (como Git); un servidor es el taller/restaurante activo que recibe pedidos, cocina con esos ingredientes y entrega el plato al cliente.  
  * *Ejemplo concreto:* Si subes código Python o SQL a Git, ahí no corre; en un servidor de BD tú te conectas con SQL Plus (cliente) y toda la carga y consultas corren en el servidor. El profesor mostró que las redes sociales convierten tus datos (ej. a qué hora ves páginas) en información y luego en conocimiento para mandarte publicidad.  
> * **Principios de Seguridad CID en Servidores (Clase 3\)**  
  * *Definición:* Todo servidor en su enfoque de seguridad debe garantizar **Disponibilidad** (siempre accesible cuando se ocupe), **Integridad** (los datos se guardan exactamente como deben y las tramas llegan íntegras con encabezado y cola) y **Confidencialidad** (solo acceden personas autorizadas y los paquetes viajan protegidos).  
  * *Analogía:* Tu cuenta bancaria: que puedas entrar al cajero a la hora que sea (**Disponibilidad**), que si tenías \$75 sigan siendo \$75 (**Integridad**) y que tu vecino no pueda ver tu saldo ni leer tu carta sellada (**Confidencialidad**).  
  * *Ejemplo concreto:* Caso de caídas en apps bancarias (como Bancomer) que impiden sacar \$100 cuando se necesitan, o el saldo de \$75 que no debe alterarse en dos o tres días.  
> * **Infraestructura en la Nube y Presupuestos (Azure) (Clase 3\)**  
  * *Definición:* Provisión de máquinas virtuales, almacenamiento y servicios gestionados por un proveedor (Microsoft Azure, AWS, Google Cloud) donde la facturación no tiene tarifa fija sino que depende de **consumo, almacenamiento y tipo de ingreso/acceso** (frecuente vs esporádico).  
  * *Analogía:* Renta de bodega vs departamento: una bodega solo cobra por guardar cajas (almacenamiento), pero un departamento cobra por vivir y usar agua/luz dentro (ejecutar cómputo por tiempo conectado).  
  * *Ejemplo concreto:* Los presupuestos en nube son siempre en **dólares estadounidenses**. El profesor configuró un presupuesto de **\$5,000 USD** con dos alertas: previsto en 0.40 (40%) y costo real en 0.50 (50% \= **\$2,500 USD**). Caso real de una papelería en CDMX que gastó **\$45,000** en un pico de marzo por elegir Azure sin análisis de requerimientos.  
> * **DNS y DHCP (Proceso DORA y Componentes) (Clase 4\)**  
  * *Definición:* **DNS** traduce nombres de dominio legibles a direcciones IP numéricas. **DHCP** (*Dynamic Host Configuration Protocol*) asigna automáticamente IP, máscara de subred, puerta de enlace y DNS mediante el proceso **DORA**: *Discover* (difusión buscando servidor), *Offer* (oferta de IP), *Request* (solicitud formal) y *Acknowledge* (confirmación).  
  * *Analogía:* DNS es la agenda de contactos de tu celular (guardas "Princesita" en vez de memorizar el número); DHCP era antes una operadora de Telmex conectando cables a mano y hoy es un recepcionista automático que asigna extensión temporal.  
  * *Ejemplo concreto:* **RIU** en la UNAM asignaba configuraciones manuales fijas y se saturó porque nadie liberaba las IPs; **PC Puma** usa DHCP, asigna IP al conectar y la libera cuando te desconectas.  
> * **Seguridad en DHCP/DNS y Kea DHCP vs. ISC DHCP (Clase 4\)**  
  * *Definición:* Riesgos principales del DHCP/DNS: (1) **DoS** por agotamiento del ámbito combinado con inyección SQL al reiniciar módems, (2) **DHCP falso / DNS suplantado** (ej. sustituir m por rn), (3) **exposición de red interna** si das IPs directas sin DNS/VPN. Para mitigarlos se usan **firewalls, DMZ y VPN** ("una red que no es una red"). **Kea DHCP** es el sucesor moderno de código abierto de **ISC DHCP** (sin mantenimiento desde fines de 2022).  
  * *Ejemplo concreto:* En Ubuntu (en modo puente o NAT para que la VM esté en el rango) se configura isc-dhcp-server en texto plano (192.168.1.0, rango .100–.200, router .1, DNS 8.8.8.8/8.8.4.4, interfaz ens33) y luego **Kea** (kea-dhcp4-server versión **2.4**, evitando la 2.6 por ser beta/última) que configura en JSON, soporta IPv4/IPv6, APIs, alta disponibilidad y es **multihilo**. Se mencionó el caso de una empresa que sufrió pérdidas diarias durante 3 días por ataque (la cifra exacta inicial de dólares quedó cortada en el audio: ",00000 dólar").

#### **(c) Componentes del ámbito DHCP (Clase 4\) y comparativa ISC vs. Kea**

| Componente DHCP | Regla / Ejemplo visto en clase   |
| :---- | :---- |
| **1\. Ámbito** | Rango de IPs asignables (ej. .1 a .254, excluyendo .0 red y .255 broadcast); en empresas se segmenta por área (ej. 10–20 conta, 20–40 finanzas, 50–200 ventas). |
| **2\. Tiempo de concesión (*Lease*)** | Periodo válido de la IP (segundos en redes de paso como Infinitum móvil, minutos/horas/1 día). |
| **3\. Puerta de enlace (*Gateway*)** | Dirección del router de salida; **solo una puerta de enlace** (poner varias multiplica puntos de ataque). |
| **4\. Servidor DNS** | IPs que resuelven nombres (ej. 8.8.8.8, 8.8.4.4). |
| **5\. Reservas** | IP fija ligada a dirección MAC; solo para superadministradores o impresoras viejas (no para todos). |
| **6\. Exclusiones** | IPs del rango que nunca deben asignarse automáticamente (ej. 127.x.x.x). |

| Característica | ISC DHCP Server | Kea DHCP (kea-dhcp4-server)   |
| :---- | :---- | :---- |
| **Estado** | Descontinuado desde finales de **2022** | Sucesor oficial activo (usar v2.4, no 2.6) |
| **Soporte** | Solo IPv4 (versión vista) | IPv4 e IPv6, APIs y bases de datos (ej. MySQL) |
| **Formato y arquitectura** | Texto plano, **un solo hilo** (secuencial) | Archivos **JSON**, **multihilo** (procesos simultáneos) y alta disponibilidad |

#### **(d) Errores comunes y puntos de examen (Clases 3, 4\)**

> * **Definir "servidor" usando la palabra "servidor"** (definición circular) o **confundir servidor con repositorio**. El profesor enfatizó que la definición exacta de servidor suele ponerse mal en el examen.  
> * **No definir requerimientos antes de recomendar una nube** (como en el caso Avante Textil) u olvidar que los presupuestos en nube están en **dólares**.  
> * **Configurar múltiples *gateways*** buscando velocidad (multiplica la superficie de ataque) o no reiniciar el servicio tras editar el archivo de configuración DHCP.

### ---

**UNIDAD 4: Ciberseguridad Práctica (Kali, Metasploit, Nmap) y Auditoría de Bases de Datos (Oracle) (Clases 8, 9, 14\)**

#### **(a) Problema que resuelve y conexión con el tema anterior**

Una vez desplegados los servicios web y de red, hay que verificar qué puertos e información exponen hacia afuera (auditoría externa) y proteger e investigar quién inserta, modifica o elimina datos dentro del servidor de base de datos (auditoría interna) (Clases 8, 9, 14).

#### **(b) Conceptos clave**

> * **Roles en Ciberseguridad y Servicios Profesionales (Clase 8\)**  
  * *Definición:* **Hackers**: *Blanco* (ético/defensivo), *Negro* (malicioso) y *Gris* (aprendizaje, donde deberían estar los estudiantes). **Pentester**: especialista en pruebas y detección de errores (incluso sin programar). **CISO**: máximo responsable de seguridad. **Ingeniero forense**: recupera información física de discos/USB (máximo **80%** recuperable). **Asesoría** (enseñas al personal interno, más barata) vs. **Consultoría** (resuelves y entregas sin enseñar el cómo, más cara y rápida).  
  * *Analogía:* Un forense es como un perito que abre una caja negra dañada para saber qué murió y rescatar lo posible; en asesoría contratas a un entrenador para tu equipo, en consultoría contratas a un cerrajero que cambia la chapa y se va.  
> * **Metasploit Framework y Escaneo Web (Clases 8, 9\)**  
  * *Definición:* *Framework* de código abierto en consola (msfconsole) con módulos de *exploits* y *auxiliares* para pruebas de penetración, recolección de datos y análisis de vulnerabilidades.  
  * *Analogía:* Como un electrocardiograma con líquido radiactivo: inyectas tráfico por un puerto hacia una IP para iluminar qué caminos existen y dónde está expuesto o bloqueado el sistema.  
  * *Ejemplo concreto:* Comandos usados: use auxiliary/scanner/http/... (equivalente a un import en Java/Python), set RHOSTS www\... (asigna objetivo), show options, exploit. En vivo se observó: CECyT 9 en un solo CPU con puerto 80 abierto sin seguridad; IPN protegido en Azure (error 404/bloqueo); UNITEC con 4 servicios en IPs públicas; Tec de Monterrey con 2 servicios en nube; Google devolviendo 16 hosts y usando servidores espejo en un **ciclo cerrado de seguridad** para hacer perder tiempo al atacante.  
> * **Nmap (Network Mapper) (Clases 8, 9\)**  
  * *Definición:* Herramienta de análisis de red que descubre hosts activos, puertos abiertos/cerrados/filtrados, servicios, versiones y sistema operativo.  
  * *Analogía:* Tocar todas las puertas y ventanas de un edificio para ver cuáles están abiertas, cuáles cerradas con llave y cuáles tienen un guardia bloqueándote el paso (*filtered*).  
  * *Ejemplo concreto:* Tras ver red local con ip a (127.0.0.1 loopback, .255 broadcast) y conectividad con ping, escanear una máquina virtual mostró puertos como 3306 (MySQL), 1521 (Oracle), 445 (Microsoft/NetBIOS), 21 (FTP), 22 (SSH), 23 (Telnet), 80 (HTTP) y 443 (HTTPS). Con nmap \-sn \<IP\> solo detectó 4 hosts activos en 8 segundos; con /24 (255.255.255.0) sacó direcciones MAC y latencias.  
> * **Seguridad y Auditoría de Bases de Datos en Oracle (Clase 14\)**  
  * *Definición:* Administración segura en servidores empresariales (Oracle elegido por ser estándar de producción frente a MySQL) siguiendo la jerarquía **Usuario \-\> Rol \-\> Privilegios**, más disparadores (**Triggers**) que se ejecutan automáticamente antes (BEFORE) o después (AFTER) de un INSERT, UPDATE o DELETE.  
  * *Analogía:* El **Rol** es el gafete de "becario" con sus llaves incluidas (GRANT); el **Tablespace** es la carpeta privada de cada usuario; el **COMMIT** es como el git push (si no confirmas la transacción, nadie más ve tus cambios); y el **Trigger** es una cámara de seguridad automática que anota quién entró y qué cambió en la bitácora.  
  * *Ejemplo concreto:* En Oracle local: 1\) Habilitar creación de usuario común: ALTER SESSION SET "\_ORACLE\_SCRIPT"=true;. 2\) CREATE USER rafa IDENTIFIED BY 123; \-\> CREATE ROLE becario; \-\> GRANT CREATE SESSION, CREATE TABLE, INSERT ANY TABLE, SELECT ANY TABLE, CREATE TRIGGER TO becario; \-\> GRANT becario TO rafa;. 3\) Permisos de sistema operativo directo al usuario (no basta el rol): GRANT UNLIMITED TABLESPACE TO rafa;. 4\) Acceso global entre usuarios: SELECT \* FROM rafa.reprobaditos; (tras COMMIT). Nótese que DROP TABLE NO requiere COMMIT. 5\) SYSDATE guardado en columna DATE devuelve solo fecha; en TIMESTAMP devuelve fecha, hora y **nanosegundos** (clave para rastrear operaciones en el mismo segundo). 6\) Trigger de auditoría: CREATE OR REPLACE TRIGGER i\_auditoria AFTER INSERT ON rafa.condicion FOR EACH ROW BEGIN INSERT INTO auditoria VALUES (USER, 'Insertó', SYSDATE); END; (diferenciando USER función vs SHOW USER comando). Para la práctica, integrar en **un solo trigger** INSERTING, UPDATING y DELETING usando las variables :OLD (dato anterior) y :NEW (dato nuevo), además de conectar SQL Developer a **Oracle Free/Live SQL** en la nube (puerto 1521 abierto vs 2484 seguro).

#### **(c) Banderas de Nmap (Clase 9\)**

| Comando / Bandera Nmap | Qué hace   |
| :---- | :---- |
| nmap \-sn \<red/24\> | Descubre únicamente qué hosts están activos (*up*) |
| nmap \-sS \<IP\> | Escaneo **sigiloso** (puede automatizarse en bash cada hora) |
| nmap \-sV \<IP\> | Detecta **versiones** y servicios corriendo en los puertos abiertos |
| nmap \-O \<IP\> | Detecta el **sistema operativo** (vulnerabilidades asociadas) |
| nmap \-A \<IP\> | Escaneo **agresivo / completo** (máxima precisión, pero fácil de detectar y deja rastro) |

#### **(d) Errores comunes y puntos de examen (Clases 8, 9, 14\)**

> * Ejecutar pruebas de Metasploit o Nmap desde tu equipo real sin máquina virtual ni autorización (deja rastro de IP).  
> * Dar privilegios directo al usuario saltándose los **Roles**, o olvidar que UNLIMITED TABLESPACE sí va directo al usuario y no por rol.  
> * Creer que SYSDATE solo devuelve la fecha (depende del tipo de columna: DATE vs TIMESTAMP), o olvidar COMMIT al consultar desde otro usuario.  
> * Confundir **Trigger** (automático ante INSERT/UPDATE/DELETE) con **Procedimiento almacenado** (se invoca manualmente), o hacer 3 triggers separados cuando el profesor pidió 1 solo usando INSERTING/UPDATING/DELETING con :OLD y :NEW.

### ---

**UNIDAD 5: Servicios de Datos, Cubos OLAP, Data Warehouse e Inteligencia de Negocios (Clases 10, 11, 13\)**

#### **(a) Problema que resuelve y conexión con el tema anterior**

Con los datos almacenados y auditados en Oracle, las organizaciones necesitan analizar históricos desde múltiples perspectivas sin frenar las bases operativas ni caer en consultas JOIN lentas o en gráficos estadísticos engañosos (Clases 10, 11, 13).

#### **(b) Conceptos clave**

> * **Roles en Datos y Proceso ETL (Clases 10, 11\)**  
  * *Definición:* Cuatro puestos clave: **Modelador/Diseñador** (cardinalidades, restricciones), **Arquitecto de datos** (optimización/*tuning*, software+hardware, CREATE TABLESPACE calculado por registros), **DBA** (seguridad, usuarios, roles, GRANT/REVOKE) y **Analista de datos** (qué/cómo/cuándo; distinto del Científico de datos que usa estadística inferencial, ecuaciones diferenciales y Laplace). **ETL** significa **Extracción** (de ERP, CRM, Excel, PDF, JSON), **Transformación** (limpieza en Power Query) y **Carga**.  
  * *Analogía:* En una cocina industrial, el Modelador diseña los estantes, el Arquitecto calcula el tamaño del refrigerador (CREATE TABLESPACE), el DBA controla quién tiene llave y el Analista decide qué platillos se venden más.  
> * **Cubo de Información (OLAP), Medidas y Dimensiones (Clase 10\)**  
  * *Definición:* **OLAP** (*Online Analytical Processing*) es una **estructura conceptual** (no un archivo físico) que organiza **medidas numéricas** alrededor de **dimensiones** para responder una **pregunta** u objetivo. Las dimensiones tienen **jerarquías** de lo general a lo particular (Tiempo: Año \-\> Trimestre \-\> Mes \-\> Día; Geografía: País \-\> Estado \-\> Ciudad \-\> Sucursal; Producto: Categoría \-\> Subcategoría \-\> Producto). Las medidas se dividen en **Aditivas** (sumables en todas dimensiones: ventas, costos), **Semiaditivas** (sumables en unas dimensiones pero no en todas, ej. saldo bancario por cliente pero no por tiempo; suelen combinar string \+ número) y **No aditivas** (calculadas con fórmulas/campos derivados: porcentajes, promedios, precio con IVA, sueldo bruto/neto).  
  * *Analogía:* Un dado donde cada cara es una dimensión (tiempo, producto, sucursal, cliente): puedes girar el dado para responder cuánto vendiste sin importar desde qué cara empieces.  
  * *Ejemplo concreto:* En Power Maps, buscar "Monterrey" sin jerarquía devuelve 3 lugares (México y Venezuela), y "León" aparece en México y España; por eso se requiere la jerarquía completa. Ejemplo de clase: Ventas \= \$1,250,000 (medida) por sucursal (Ecatepec vs Santa Fe) en 2026 Q1.  
> * **Data Warehouse y Esquemas Analíticos (Clases 10, 11\)**  
  * *Definición:* **Data Warehouse** es un **repositorio** (no una BD transaccional común) orientado al análisis, integrado desde múltiples fuentes e **histórico** en el tiempo. **Regla crítica:** nunca regresar datos del Data Warehouse a la base de datos transaccional porque rompe la integridad. Sus operaciones analíticas alimentan un **EIS** (Sistema de Información Ejecutiva / *Dashboards*): *Slice* (una rebanada, ej. solo 2026), *Dice* (varias condiciones, ej. laptops en CDMX en Q2) y *Drill-down* (bajar al detalle: año \-\> mes \-\> día).  
  * *Analogía:* La BD transaccional es la caja registradora en vivo; el Data Warehouse es la hemeroteca histórica de reportes donde solo consultas hacia adelante para el tablero del director.  
> * **Análisis Crítico en Power BI con ENOE/ENIGH y Gobernanza (Clases 10, 11, 13\)**  
  * *Definición:* Flujo **Excel (básico / Power Query) \-\> Oracle (almacenamiento DW \+ SQL con funciones OLAP como RANK y OVER) \-\> Power BI Desktop (modelos semánticos y dashboards)**. Por **gobernanza de datos**, no deben usarse/compartirse datos públicos de los últimos **5 años** sin permiso (en 2026, restringidos 2021–2025; se usó ENOE 2017).  
  * *Ejemplo concreto:* Con la **ENOE** (Encuesta Nacional de Ocupación y Empleo, teóricamente ≥15 años) se demostró en vivo que en 2017 había **8 niños de 12 años** y **4 personas de 98 años** trabajando para mantener hogares; el pico más alto de suma de ingresos está a los **36 años**. Al analizar **brecha salarial**, sumar ingresos totales mostraba casi el doble para hombres, pero al cambiar a **recuento** había \~6,300 hombres vs \~4,000 mujeres (y 175 hombres vs casi la mitad de mujeres en un pico de edad). En **escolaridad**, el sistema juntó Media Superior \+ Superior frente a Secundaria completa; en **promedio salarial**, 6 de los top 10 estados son del norte (Baja California, Nuevo León, Sinaloa, Coahuila, Sonora) y no CDMX; el empleo **formal** gana más antes de impuestos, pero en CDMX y Oaxaca predomina lo **informal** frente a Nuevo León y Quintana Roo (hoteles).

#### **(c) Esquemas de Data Warehouse (Clase 10\)**

| Esquema | Forma Normal | Estructura de tablas | Ventaja / Uso   |
| :---- | :---- | :---- | :---- |
| **Estrella** | **1FN** mínimo (atomicidad, sin grupos repetidos, llaves primarias) | **1 tabla de hechos** central (llave primaria compuesta por foráneas de todas las dimensiones) \+ dimensiones directas | Sencillo, una sola consulta centralizada; evita JOINs pesados (Explain Plan) |
| **Copo de Nieve** | **2FN** | **1 tabla de hechos**, pero las dimensiones se normalizan en **subdimensiones** (ej. Producto \-\> Categoría / Marca) | Reduce redundancia manteniendo relación 1:N hacia la tabla de hechos |
| **Constelación** | **3FN** | **Más de 1 tabla de hechos** compartiendo dimensiones (y posibles subdimensiones) | Cubre múltiples procesos analíticos complejos |

#### **(d) Errores comunes y puntos de examen (Clases 10, 11, 13\)**

> * **Empezar un cubo por la pregunta y al final buscar la medida:** Se debe definir primero **Medida \+ Dimensiones** y luego responder la pregunta del cliente.  
> * **Creer que "cubo de información" es un archivo físico** (es un concepto) o decir que "edad" es el único campo calculado sin entender medidas no aditivas/derivadas.  
> * **Gráficos engañosos:** Usar **suma** en lugar de **promedio o recuento** (crea falsas brechas por tamaño poblacional) o elegir el gráfico "más bonito" sin saber cuándo usar barras, líneas o dispersión.  
> * **No revisar el modelo relacional antes de responder:** En la Clase 13 advirtió explícitamente que si no armas bien el modelo entidad-relación entre los 5 archivos, todas las respuestas salen mal. *(Los cubos OLAP fueron explícitamente anunciados para el examen parcial previo \`\`, por lo que siguen siendo base del examen final integral.)*

### ---

**UNIDAD 6: Transformación Digital, Nuevas Tecnologías e IA en Profesiones (Clases 15, 16, 17\)**

#### **(a) Problema que resuelve y conexión con el tema anterior**

Los datos y modelos analíticos culminan en automatización e inteligencia artificial; esta unidad evalúa cómo integrarlas estratégicamente en empresas y oficios reales sin perder el negocio, el criterio humano ni la calidad de los datos (Clases 15, 16, 17).

#### **(b) Conceptos clave**

> * **Digitalizar vs. Digitalizar Procesos vs. Transformación Digital (Clase 15\)**  
  * *Definición:* **Digitalizar** es convertir papel a formato digital (escanear); **digitalizar procesos** es usar herramientas digitales para mejorar tareas actuales (facturas electrónicas, ERP como SAP); **transformación digital** es integrar tecnologías para rediseñar el modelo de negocio, cultura, procesos y forma de entregar valor.  
  * *Analogía:* Pasar tus apuntes a PDF es *digitalizar*; usar una app para generar recibos automáticos es *digitalizar procesos*; cambiar por completo cómo vendes y entregas tu servicio sin cargar infraestructura ajena es *transformación digital*.  
  * *Ejemplo concreto:* **Netflix**: empezó rentando DVDs, pasó a *streaming* queriendo operar todos sus servidores y subtítulos ("el clásico yo-yo"), y se transformó delegando infraestructura a la nube (Google/AWS) para enfocarse en contenido propio y análisis de datos de usuarios. Caso **Avante**: despidió a un departamento entero (mencionado como 19 o \~28 personas) dejando solo a quienes sabían usar IA.  
> * **IA como Herramienta, *Prompts* y Áreas Tecnológicas (Clases 15, 16, 17\)**  
  * *Definición:* La IA no es objetiva (se basa en probabilidades/porcentajes, recompensa sin penalización al alucinar y en el perfil del usuario) y es un apoyo, no un reemplazo. Escribir un *prompt* efectivo equivale a escribir un **algoritmo** detallado.  
  * *Ejemplo concreto:* En las exposiciones (Clases 16, 17\) se analizaron casos reales:  
  * *Contaduría:* Automatización de CFDI/XML/PDF en SAP/QuickBooks, evitando contacto directo riesgoso contador-cliente y operaciones a terceros (refacturación ilegal).  
  * *Agricultura:* Drones DJI Agras (más de **\$500,000 MXN**), sensores de flujo óptico y láseres cuando falla el GPS; en PyMEs agrícolas, usar app móvil mejor que web para campo (aclarando que **Flutter** es el aplicativo y **Dart** el lenguaje).  
  * *Transporte autónomo y Medicina:* Vehículos autónomos (Waymo) exigen nuevos roles (programador, mecánico eléctrico, médico en módulos, **ciberseguridad** porque ha habido muertes por hackeo); medicina usa modelo ***human-in-the-loop*** y verificador de recetas contra autorrecetas/falsificación.  
  * *Mecánica y Soporte TI:* Asistente de IA con escáner automotriz (riesgo de autodiagnóstico del cliente, oportunidad en quien alimenta datos); soporte predictivo autónomo de 4 rubros donde el profesor destacó como único aporte clave el rol del **auditor** de procesos y documentación.  
> * **Big Data y Calidad vs. Cantidad de Datos (Clase 17\)**  
  * *Definición:* **Big Data** es una "gran cantidad de datos"; sin embargo, el profesor recalcó que **a mayor cantidad de datos NO hay necesariamente mayor precisión: la precisión la da la calidad y seguir un protocolo estricto de captura**.  
  * *Analogía:* La agenda del teléfono celular: aunque tengas campos separados para nombre, apellido paterno y materno, si todos ponen apodos en el campo de nombre, por miles de contactos que tengas las búsquedas fallarán.  
  * *Ejemplo concreto:* Base de datos de radiografías/ecografías veterinarias (nube vs local): si las redes neuronales confunden perro con gato o los datos se capturan sin protocolo, arrojan diagnósticos erróneos.

#### **(c) Errores comunes y puntos de examen (Clases 15, 16, 17\)**

> * Confundir digitalizar (escanear) con transformar digitalmente el negocio.  
> * Creer que *Big Data* garantiza mayor precisión por volumen y que basta "contratar a alguien" para llenar datos sin establecer un **protocolo**.  
> * Negar el desplazamiento laboral en la explicación oral cuando en la propia diapositiva o diseño dicen que una máquina hace el trabajo de 5 personas o es 100% autónoma.  
> * Usar IA sin supervisión humana (especialmente en finanzas/dineros, decisiones médicas o enviando prácticas sin quitar la línea del chat de IA), o que los empleados usen IA por su cuenta sin políticas ni auditoría de la empresa.

### ---

**UNIDAD 7: Estándares Oficiales de Internet (RFCs) y Protocolos Fundamentales (Clases 17, 18, 19\)**

#### **(a) Problema que resuelve y conexión con el tema anterior**

Todo servicio visto en el semestre (Linux, HTTP, correo, directorios, IP/puertos, acceso remoto, DNS, DHCP y cifrado) no funciona por improvisación: la **IETF** estandariza sus reglas en documentos públicos llamados **RFC** para garantizar interoperabilidad mundial entre sistemas distintos (Clases 17, 18, 19).

#### **(b) Conceptos clave**

> * **¿Qué es un RFC? (Clases 17, 18\)**  
  * *Definición:* *Request for Comments* (iniciado por Steve Crocker en ARPANET en 1969): documentos técnicos públicos, gratuitos e **inmutables** (no se editan; solo evolucionan publicando un nuevo RFC que reemplaza o actualiza al anterior) que definen reglas de protocolos, formatos, mensajes, palabras clave (MUST, SHOULD, MAY) y registros ante **IANA**. Categorías: *Standard Track*, *BCP*, *Informational*, *Experimental* e *Historic*.  
  * *(Nota sobre asignación en Clase 17 vs exposición en Clases 18–19: En Clase 17 se mencionaron 1939, 281, 1034, 3898, 451, 261, 8446, 1700 —y 2081/3501 en temario—, no quedando claros en el audio los números de los equipos 3 y 4\. En las Clases 18 y 19 los equipos expusieron exactamente 9 RFCs: **2616, 3501, 1939, 4510, 1700, 854, 1034, 3898 y 8446**.)*  
> * **RFC 2616 — HTTP/1.1 (Clase 18\)**  
  * *Definición:* Publicado en junio de 1999 por la IETF; define HTTP 1.1 como protocolo **petición-respuesta sin estado** (*stateless*) sobre TCP (puerto 80).  
  * *Analogía:* Ventanilla sin memoria: cada petición lleva línea inicial/final, cabeceras y cuerpo opcional, y recibe código 1xx (info), 2xx (éxito), 3xx (redirección), 4xx (error cliente) o 5xx (error servidor).  
  * *Ejemplo concreto:* Métodos como GET (seguro, solo lectura), POST, PUT, DELETE (idempotentes), OPTIONS, CONNECT. Mejoró a RFC 1945 (solo "yo recomiendo") y 2068 (vacíos) añadiendo conexiones persistentes, cabecera obligatoria (Virtual Hosting), *Chunked Transfer Encoding* y caché. Por ser **monolítico (176 hojas)**, quedó obsoleto en **2014** al dividirse en **RFC 7230–7235**, refactorizarse en **2022** y dar paso a HTTP/2 (multiplexación) y HTTP/3 (sobre QUIC).  
> * **RFC 3501 — IMAP4rev1 (Clase 18\)**  
  * *Definición:* Creado en 2003 por Mark Crispin; protocolo de capa 7 (puertos **143** normal, **993** cifrado) para acceder y manipular correos directamente en el servidor desde múltiples dispositivos.  
  * *Analogía:* Archivero central en la oficina donde lees y sellas cartas sin llevártelas a casa.  
  * *Ejemplo concreto:* Comandos con etiqueta (A001 LOGIN usuario clave) \-\> respuestas OK, NO, BAD y datos sin etiqueta \*. **4 estados:** No autenticado (LOGIN) \-\> Autenticado (SELECT) \-\> Seleccionado \-\> Cierre (LOGOUT). Banderas: \\Seen, \\Answered, \\Flagged, \\Deleted (requiere EXPUNGE para borrar definitivo), \\Draft, \\Recent. En ejemplo real, se conectó al puerto 993 viendo 172 mensajes (1 reciente) y descargó solo cabeceras con FETCH. Desventajas: dependencia total del servidor (como la caída de **300 bancos en Japón**) y crecimiento continuo de almacenamiento.  
> * **RFC 1939 — POP3 (Clase 18\)**  
  * *Definición:* Publicado en mayo de 1996 (reemplaza RFC 1725); protocolo simple sobre TCP (puerto **110** normal, **995** POP3S con SSL/TLS) donde el cliente descarga correos localmente y se borran del servidor.  
  * *Analogía:* Buzón físico afuera de tu casa: el cartero (SMTP) deposita, tú sacas todo a tu escritorio y el buzón queda vacío.  
  * *Ejemplo concreto:* Respuestas \+OK, \-ERR y . al final de listas. **3 estados:** Autorización (USER, PASS, APOP con MD5) \-\> Transacción (STAT, LIST, RETR n, DELE n, RSET desmarca, NOOP) \-\> *Update* (QUIT, única forma en que DELE borra definitivamente). Timeout de **10 minutos** y bloqueo exclusivo del buzón.  
> * **RFC 4510 — LDAPv3 (Clase 18\)**  
  * *Definición:* Documento de 6 páginas (junio 2006, Kurt Zeilenga / OpenLDAP, *Standard Track*) que actúa como **mapa de ruta normativo** de **LDAPv3**, alternativa ligera ("X.500 *light*") a X.500 (que exigía toda la pila OSI) para gestionar usuarios, contraseñas y permisos en red.  
  * *Ejemplo concreto:* Sustituyó al RFC 3377 y organiza la familia **4511** (operaciones *Bind/Search/Modify/Delete*), **4512** (modelos), **4513** (SASL/TLS), **4514–4519** (nombres, filtros, URLs, esquemas como uid/mail), **4520** (registros IANA) y **4521** (extensiones).  
> * **RFC 1700 — Números Asignados / IANA (Clase 18\)**  
  * *Definición:* Documento histórico de 1994 (Joyce Reynolds y Jon Postel) que recopiló en tablas los identificadores de protocolos y **puertos bien conocidos** de IANA para interoperabilidad entre arquitecturas (x86/x64, ARM).  
  * *Ejemplo concreto:* En IPv4, protocolo **6 \= TCP** y **17 \= UDP**. Puertos esenciales: **20** (FTP datos), **21** (FTP control), **22** (SSH), **25** (SMTP), **53** (DNS TCP/UDP), **80** (HTTP). Por ser estático y lento para actualizar por consenso, pasó a histórico y lo sustituyó el **RFC 3232** (2002, base en línea) y hoy los registros IANA en tiempo real.  
> * **RFC 854 — Telnet (Clase 18\)**  
  * *Definición:* Publicado en 1983 (Postel y Reynolds, estatus **STD 8**); abarca el documento, el protocolo de control de 8 bits independiente del SO y el programa cliente (ej. PuTTY) como terminal remota interactiva sobre TCP **puerto 23**.  
  * *Ejemplo concreto:* Creó **NVT (*Network Virtual Terminal*)** en **ASCII de 7 bits \+ octavo bit de control** como traductor entre hosts distintos; negocia opciones con **WILL, WONT, DO, DONT** y IAC (*Interpret As Command*, bit 155, ej. ocultar eco de contraseñas). Modularidad con RFC 856 (binarios), bidireccionalidad y RFC 1091 (colores/cursores). Por enviar todo **sin cifrar**, fue reemplazado en producción por **SSH (RFC 4251\)** en puerto 22\.  
> * **RFC 1034 — DNS (Clase 18\)**  
  * *Definición:* Publicado (1984 según exposición) por la IETF; especifica arquitectura, formato, resolución global jerárquica y escalabilidad distribuida del DNS en **capa 7, puerto 53**.  
  * *Ejemplo concreto:* Traduce youtube.com o estructuras .com.mx/.unam en servidores como **BIND** y dirige correos. Descentralizado (evita caídas por servidor único), aunque inicialmente vulnerable y sujeto a retrasos de propagación/caché.  
> * **RFC 3898 — Opciones NIS/NIS+ en DHCPv6 (Clase 19\)**  
  * *Definición:* Publicado en octubre de 2004; transporte para que DHCPv6 entregue parámetros de servidores NIS/NIS+ mediante cuatro códigos (**27 al 30**).  
  * *Ejemplo concreto:* **27** (IP NIS) \+ **29** (dominio NIS); **28** (IP NIS+) \+ **30** (dominio NIS+) en tablas de 16 bits. Flujo de 4 pasos (el servidor no entrega NIS por defecto: el cliente pide códigos en búsqueda inicial \-\> servidor envía anuncio \-\> cliente reenvía códigos en *request* \-\> servidor entrega configuración). Obsoleto por transmitir **sin cifrar** y riesgo de servidores falsos; sustituido por **LDAP / Active Directory**.  
> * **RFC 8446 — TLS 1.3 (Clase 19\)**  
  * *Definición:* Especificación vigente de *Transport Layer Security* 1.3 (reemplaza TLS 1.2 RFC 5246 y RFC 507; actualiza 5705 y 7961\) que garantiza **confidencialidad, integridad e identificación** (certificado digital) contra ataques ***Man-in-the-Middle***.  
  * *Analogía:* **AEAD** es como guardar dinero en una caja fuerte (AES) y además sellarla con un **sello de cera** (*authentication tag*): si alguien altera un solo bit del contenido o del encabezado, el sello se rompe y el servidor aborta la transacción al instante.  
  * *Ejemplo concreto:* Reduce *handshake* de **2 RTT** (TLS 1.2) a **1 RTT**; elimina **MD5, SHA-1 y RC4**. Impone dos restricciones obligatorias: (1) **AEAD** (predilecto **AES-GCM**, etiqueta sobre *payload* \+ encabezado) y (2) ***Perfect Forward Secrecy*** con **claves efímeras Diffie-Hellman** que **se borran de la RAM** al cerrar sesión (dejando paquetes capturados ilegibles).

#### **(c) Tabla resumen de puertos y estado de los RFCs (Clases 18, 19\)**

| RFC | Protocolo / Tema | Capa / Transporte / Puertos | Estado actual / Reemplazo   |
| :---- | :---- | :---- | :---- |
| **2616** | HTTP/1.1 | Aplicación / TCP / **80** | Obsoleto (2014 \-\> **7230–7235** \-\> 2022 / HTTP/2, HTTP/3) |
| **3501** | IMAP4rev1 | Capa 7 / TCP / **143** (normal), **993** (cifrado) | Base clásica (sustituido por rev. posterior citada como 951\) |
| **1939** | POP3 | Capa transporte/app / TCP / **110** (normal), **995** (POP3S) | Vigente en descargas locales (con POP3S cifrado) |
| **4510** | LDAPv3 (hoja de ruta) | Aplicación / Familia 4511–4521 | Vigente en directorios empresariales |
| **1700** | Números IANA | Red/Transporte (6=TCP, 17=UDP; 20/21, 22, 25, 53, 80\) | Histórico (2002 \-\> **RFC 3232** \-\> registros IANA en vivo) |
| **854** | Telnet | Aplicación / TCP / **23** | Obsoleto en producción por falta de cifrado (-\> **SSH RFC 4251**, puerto 22\) |
| **1034** | DNS | Capa 7 / TCP-UDP / **53** | Arquitectura base vigente (actualizada por nuevos RFCs de seguridad) |
| **3898** | Opciones NIS en DHCPv6 | Red/App / Códigos **27–30** | Obsoleto por inseguridad (-\> **LDAP / Active Directory**) |
| **8446** | TLS 1.3 | Capa de transporte segura (**1 RTT**) | Vigente recomendado (Chrome/Firefox); reemplaza **5246** |

#### **(d) Errores comunes y puntos de examen (Clases 17, 18, 19\)**

> * Confundir el protocolo con el RFC (ej. en Clase 18 el profesor preguntó explícitamente si **LDAP** es el protocolo o el RFC: LDAP es el **protocolo** y el RFC 4510 es el documento normativo que lo organiza).  
> * Confundir las siglas **RFC** (documentación oficial de reglas técnicas de internet, no el Registro Federal de Contribuyentes).  
> * Creer que en POP3 DELE borra los correos de inmediato (solo marca; borra en estado *Update* al ejecutar QUIT, y RSET lo revierte).  
> * Olvidar que en el RFC 3898 los códigos 27–30 deben enviarse **dos veces** (en la búsqueda inicial y en el *request* formal) y que el RFC no implementa NIS, solo lo transporta.

## ---

**3\. LO QUE MÁS PROBABLEMENTE VIENE EN EL FINAL**

*(Fecha del examen final confirmada en Clase 19: **miércoles 18 de noviembre**, individual, en hojas blancas, sin celular, abarcando todo el curso.)*

> 1. **Definición precisa de Servidor vs. Repositorio y tipos de Requerimientos:** *Evidencia fuerte* — en Clase 3, el profesor advirtió explícitamente *"parece muy obvio, pero luego en el examen me ponen ahí cada barbaridad"* al dar la definición de servidor, y resolvió 5 ejercicios en vivo diferenciando requerimientos funcionales, no funcionales y de sistema.  
> 2. **Escritura de código y comandos en papel (basado en examen extraordinario):** *Evidencia fuerte* — en Clase 17 le preguntaron si había que sacar hoja y escribir código, y el profesor confirmó: *"El extra estuvo manchado. Yo creo me voy a basar en el \[extra\]"*. Incluye comandos de Linux (ls, cat, mkdir \-m/-p, ps aux, which/whereis) (Clase 1), SQL/Oracle (CREATE USER, ROLE, GRANT, UNLIMITED TABLESPACE, TRIGGER con :OLD/:NEW) (Clase 14\) y scripts/comandos de red o ciberseguridad (Nmap, Metasploit, Kea/DHCP) (Clases 4, 8, 9).  
> 3. **Los RFCs expuestos y qué es un RFC:** *Evidencia fuerte y explícita* — en Clase 17, el profesor afirmó: *"en el examen voy a añadir los de los RFCs"* y destacó que toda la materia y el temario se basan en ellos. Especial atención a HTTP/1.1 (2616 y GET/POST preguntados en Clase 18), IMAP (3501) vs POP3 (1939) (preguntados en Clase 18), LDAP (4510, preguntado si era protocolo o RFC), IANA (1700 puertos y protocolo 6/17), Telnet (854 vs SSH), DNS (1034), DHCPv6/NIS (3898) y TLS 1.3 (8446: 1-RTT, AEAD/AES-GCM, Diffie-Hellman efímero).  
> 4. **Cubos de información (OLAP), Data Warehouse y Esquemas (Estrella 1FN, Copo de nieve 2FN, Constelación 3FN):** *Evidencia fuerte* — en Clase 10 dijo explícitamente *"de ahí sí podemos sacar un buen para su examen"*, en Clase 13 señaló que salieron mal en ese parcial (máximo 7\) y les puso actividad de reposición enfatizando revisar primero el modelo relacional, y en Clase 17 confirmó que el final cubre *"todo, todo, todo, todo"*.  
> 5. **Auditoría en Oracle: Usuarios \-\> Roles \-\> Privilegios, COMMIT, SYSDATE/TIMESTAMP y Triggers (:OLD / :NEW):** *Evidencia fuerte* — en Clase 14 el profesor repitió *"Yo pondría mucha alta atención"*, apostó calificaciones en vivo con SYSDATE y acceso usuario.tabla, y enfatizó la diferencia entre USER vs SHOW USER y el uso de :OLD y :NEW en un solo disparador.  
> 6. **Metodologías de Proyectos (Tradicional/PMBOK vs. Ágil/Scrum) y Tipos de Recursos en Project:** *Evidencia moderada/fuerte* — ocupó dos sesiones completas con cuadro comparativo formal, cálculo de horas y costos en vivo en MS Project (Trabajo, Material, Costo) y la distinción clave de que Scrum implementa a la metodología ágil (Clases 2, 5).  
> 7. **Servicios de Red (DHCP proceso DORA, componentes del ámbito, Kea vs. ISC y Seguridad DoS/SQLi/DMZ/VPN):** *Evidencia moderada* — incluyó ejercicios prácticos de red (192.168.1.100–200, exclusión 127.x.x.x, una sola puerta de enlace) y comparativa técnica ISC vs Kea (Clase 4).  
> 8. **Big Data (Calidad vs. Cantidad de datos y necesidad de Protocolos):** *Evidencia moderada* — en Clase 17 el profesor interrumpió la exposición de veterinaria para interrogar a todo el grupo sobre si más datos dan mayor precisión y refutarlo enfatizando protocolos de captura.  
> 9. **Arquitectura Von Neumann vs. Harvard RISC y Cálculo de uso de ALU en *Pipeline*:** *Evidencia moderada* — fue el único ejercicio matemático-arquitectónico resuelto en pizarrón/clase con porcentajes exactos (33% y 20% de uso de ALU) al arranque del curso (Clase 1).  
> 10. **Principios CID en servidores, Presupuestos en Nube (dólares y alertas) y Banderas de Nmap / Metasploit:** *Evidencia moderada* — temas repetidos en múltiples clases (CID en Clase 3; alertas 0.40/0.50 en Clase 3; banderas \-sn, \-sS, \-sV, \-O, \-A resumidas al cierre de Clase 9 y conectadas en Clase 14 para rastrear IP del atacante desde el *trigger*).

## ---

**4\. CONEXIONES CLAVE**

Procesador Von Neumann \-\> genera \-\> Cuello de botella en acceso único a memoria (Clase 1\) Arquitectura Harvard RISC \-\> separa \-\> Memorias de instrucciones y datos para lograr pipeline (Clase 1\) Sistema operativo Linux \-\> aloja \-\> Servicios de red con permisos, usuarios y procesos (Clase 1\) Metodología tradicional PMBOK \-\> fija \-\> Alcance, costo y tiempo con cambios formales costosos (Clase 2\) Metodología ágil \-\> implementa \-\> Entregas incrementales mediante el marco Scrum (Clase 2\) Microsoft Project \-\> clasifica \-\> Recursos en trabajo, material y costo fijo (Clase 2\) Levantamiento de requerimientos \-\> distingue \-\> Qué hace el sistema (funcional) de cómo se mide (no funcional) (Clase 3\) Diagramas UML \-\> obligan \-\> Coherencia exacta con el código del proyecto final (Clase 7\) Repositorio \-\> almacena \-\> Datos brutos que un servidor sí procesa y comparte en red (Clase 3\) Principios CID \-\> garantizan \-\> Disponibilidad, integridad y confidencialidad de todo servidor (Clase 3\) Servicios en la nube \-\> requieren \-\> Presupuestos en dólares con alertas de costo previsto y real (Clase 3\) Servidor DHCP \-\> automatiza \-\> Asignación de IP, máscara, gateway y DNS mediante proceso DORA (Clase 4\) Kea DHCP \-\> sustituye \-\> Al obsoleto ISC DHCP aportando configuración JSON y multihilo (Clase 4\) Firewall, DMZ y VPN \-\> mitigan \-\> Ataques DoS, inyección SQL y servidores DHCP/DNS falsos (Clase 4\) Metasploit \-\> inyecta \-\> Tráfico auxiliar para descubrir puertos, IPs y arquitectura expuesta (Clases 8, 9\) Nmap \-\> mapea \-\> Hosts activos, puertos, versiones, SO y vulnerabilidades de una red (Clase 9\) Jerarquía Oracle \-\> ordena \-\> Seguridad creando primero usuario, luego rol y luego privilegios (Clase 14\) Tablespace en Oracle \-\> requiere \-\> Privilegio UNLIMITED TABLESPACE directo al usuario (Clase 14\) Trigger de auditoría \-\> registra \-\> Usuario, fecha nanosegundos, :OLD y :NEW ante DML (Clase 14\) Proceso ETL \-\> alimenta \-\> Cubos OLAP y Data Warehouse desde orígenes heterogéneos (Clases 10, 11\) Data Warehouse \-\> prohíbe \-\> Regresar datos a la BD transaccional para preservar integridad (Clases 10, 11\) Esquemas analíticos \-\> normalizan \-\> Estrella (1FN), Copo de nieve (2FN) y Constelación (3FN) (Clase 10\) Medidas no aditivas \-\> calculan \-\> Valores derivados mediante fórmulas que no deben sumarse directo (Clase 10\) Power BI sobre ENOE \-\> revela \-\> Sesgos entre sumas totales, promedios y recuentos reales (Clase 11\) Transformación digital \-\> rediseña \-\> El modelo de negocio más allá de solo escanear o digitalizar procesos (Clase 15\) Big Data \-\> depende \-\> De calidad y protocolos de captura más que de cantidad de datos (Clase 17\) Automatización con IA \-\> exige \-\> Supervisión *human-in-the-loop* y rol de auditoría humana (Clases 16, 17\) Documentos RFC \-\> estandarizan \-\> Reglas inmutables de protocolos e identificadores IANA (Clases 17, 18\) HTTP/1.1 (RFC 2616\) \-\> evoluciona \-\> Hacia series 7230–7235, HTTP/2 y HTTP/3 al dividirse por monolítico (Clase 18\) POP3 (RFC 1939\) \-\> descarga \-\> Correos localmente borrándolos del servidor frente a IMAP (RFC 3501\) (Clase 18\) Telnet (RFC 854\) \-\> cede \-\> Ante SSH (RFC 4251\) por transmitir tráfico remoto sin cifrado (Clase 18\) TLS 1.3 (RFC 8446\) \-\> protege \-\> Comunicaciones en 1-RTT mediante AEAD (AES-GCM) y claves efímeras Diffie-Hellman (Clase 19\)  
---

💡 Si quieres repasar antes del miércoles 18, puedo armarte un **simulador de examen final tipo extraordinario** (con ejercicios de código en papel en Linux, Oracle SQL/Triggers, cálculo de pipeline/project y preguntas trampa de RFCs y OLAP) para que lo resuelvas y lo revisemos juntos.

## **Anexo · Clases que no estaban en el cuaderno de NotebookLM**

*Resumen para estudiar de cada una, tomado de los apuntes por clase del sitio (decimo/ASI/ASI-Resumenes/).*

### **Clase 12 · Examen (miércoles 7 oct 2026\)**

Si tienes el enunciado o tu calificación, agrégalos en decimo/ASI/ para completar este resumen.