% materia: Seguridad Informática Básica
% titulo: Clase 8 · Amenaza vs. vulnerabilidad: método y casos
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · jueves 24 sep 2026 · Tema 2 (2.2) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. El error más común: confundir vulnerabilidad con acción
Al regresar la actividad de la Clase 7, la profesora corrigió: la **amenaza** es "lo malo que podría pasar"; una **carencia** ya es una vulnerabilidad.
- "Falta personal" **no** es amenaza: es vulnerabilidad. Su amenaza: que alguien robe al no haber quien vigile.
- "Falta orden al manipular el material" → amenaza: que alguien resulte dañado o se pierdan cosas.
Repaso: la vulnerabilidad es la debilidad de los procedimientos ("talón de Aquiles"); se identifica preguntando **qué falta, qué no se ha hecho o qué se omitió**; puede ser humana, de hardware, de red, de software o física. Hay **riesgo** cuando una amenaza tiene una vulnerabilidad correspondiente.
!!! Las cinco reglas
1. Las amenazas **no** son vulnerabilidades.
2. Las amenazas **explotan** (aprovechan) vulnerabilidades.
3. Una amenaza puede explotar una o **varias** vulnerabilidades.
4. Una vulnerabilidad puede ser explotada por una o **varias** amenazas.
5. Las vulnerabilidades son **omisiones**: algo que falta o de lo que se carece.
"Exploits": en el ámbito profesional, programas o pruebas para identificar o aprovechar vulnerabilidades.

## 2. Reformular como "carencia de…" (activo: el celular)
**Amenazas** al celular: que se rompa, lo roben, se caiga al agua, se infle la batería y explote, se apague y no prenda, se formatee solo, se dañe la pantalla, roben las tarjetas por NFC. Que sean "malas" depende del contexto (apagarse no daña si no se iba a usar).
| Causa mal dicha | Vulnerabilidad bien dicha | Acción para reducirla |
|---|---|---|
| "Los materiales son malos" | Carece de materiales de buena calidad | Investigar marcas, pruebas de resistencia (tipo Profeco) |
| "No tenía funda" | Carece de funda de protección | Elegir funda adecuada (bordes acolchados, esquinas reforzadas) |
| "No tuve cuidado" | Carece de cuidado | Correas o amarres |
| "Se rayó" | Carece de mica protectora | Cristal templado |
| "Es bien confiado" | Carece de desconfianza | — |
| "Se enferma seguido" | Carece de buena salud | — |
Regla: si no se puede plantear como **"me falta…" / "carezco de…"**, no es vulnerabilidad.

## 3. Vulnerabilidades humanas: el eslabón más débil
Exceso de confianza, flojera, ingenuidad y falta de desconfianza:
- **Sesiones abiertas** en computadoras compartidas (las de la Facultad) o prestar el celular → falta de cuidado al cerrar sesión.
- **Modas de IA** (fotos estilo Studio Ghibli o años 80): la imagen pasa a la herramienta → falta de cuidado con la propia imagen.
- **Fotos de menores** en redes (primer día de clases, número de casa visible): facilitan ubicarlos y terminan en contextos de explotación.
- **Suplantación** con fotos robadas de perfiles públicos para dar credibilidad a perfiles falsos.
- **Prestigio irrecuperable:** lo que se sube no se retira por completo (caso de un canal familiar que ridiculizaba a sus hijos; Costa Rica regula más estrictamente).
- **Presión y miedo:** entregar contraseñas por teléfono "de parte del jefe" sin verificar.

## 4. Ejercicio de 20 reactivos (participación)
Completar con el elemento contrario. Selección:
| Dado | Se completa con |
|---|---|
| Que entren a mi Facebook (A) | No usar contraseña segura ni verificación en dos pasos (V) |
| No seguir normas de cableado estructurado (V) | Fallas de red, cortos, pérdida de conectividad (A) |
| No tener antivirus (V) | Que se infecte con malware (A) |
| Resbalarse en el pasillo (A) | Piso mojado sin señalización (V) |
| Confianza plena en un amigo (V) | Que me dé información falsa (A) |
| Perder el proyecto final (A) | No contar con respaldo (V) |
| Quedarse sin red en sesión en línea (A) | No tener respaldo de conexión (datos móviles) (V) |
| Perder la contraseña de un servicio (A) | No usar gestor de contraseñas (V) |
| Falta de pintura no inflamable (V) | Que un incendio se propague (A) |
| Omitir protecciones contra filtraciones (V) | Daño a equipos o documentos por agua (A) |
Conclusión: la vulnerabilidad se identifica preguntando **"¿qué NO se ha hecho?"**; al eliminarlas bajan los riesgos y los ataques.

## 5. Casos reales de vulnerabilidades no gestionadas
- **Línea 12 del Metro:** se descartó la ruta técnicamente más viable por razones políticas (inaugurar en la administración vigente); no se calculó bien el material de la ruta más larga y se rellenaron columnas con materiales inadecuados → fallas estructurales.
- **Recorte de seguros médicos** para ahorrar: graves consecuencias cuando alguien clave enferma o fallece.
- **Trampa en exámenes:** no prever que el alumnado use cierta tecnología (exceso de confianza en el proceso).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Definición operativa (examen)
**Vulnerabilidad = carencia u omisión** ("me falta…", "carezco de…"), nunca una acción ni el evento dañino. **Amenaza = lo malo que puede pasar**, que explota vulnerabilidades. Relación uno a muchos y muchos a muchos.

**Factor humano.** El eslabón más débil: sesiones abiertas, fotos a la IA, fotos de menores, suplantación, presión telefónica.

| Ejercicio tipo | Ejemplo |
|---|---|
| Reformular | "No tuve cuidado" → carece de cuidado |
| Completar A → V | Perder el proyecto → no tener respaldo |
| Completar V → A | Sin antivirus → infección por malware |
| Caso real | Línea 12: omisiones de planeación → colapso |

# PARTE 3 · Mis apuntes de clase
~ Mis apuntes originales de este día (24/09/2026), tal cual los escribí.
```
Vulnerabilidades
1. Amenazas NO son vulnerabilidades
2. Amenazas EXPLOTAN (APROVECHAN) Vulnerabilidades
3. Amenazas -> 1 vulnerabilidad o varias vulnerabilidades
4. 1 Amenaza -> 1 vulnerabilidad o varias vulnerabilidades
5. Las vulnerabilidades son omisiones, es algo que NO se ha tomado en cuenta, algo que falta, algo de lo que se carece

EJEMPLO
Activo				Amenaza(s)								Vulnerabilidades
Teléfono celular	Que se rompa							No tiene buenos materiales, no tiene funda, por descuido, carece de mica protectora
					Que lo roben
					Que se caiga al aggua
					Que se infle la batería y explote
					Que se apague y ya no prenda
					Que se formatee solo
					Que se prenda
					Que roben tarjetas

Conclusiones
-Una vulnerabilidad se identifica fácilmente si se analiza "qué es lo que NO se ha hecho?"
-En la medida que se eliminen vulnerabilidades, se correrán menos riesgos, se contrarrestarán amenazas y entonces disminuirán los ataques.

EJERCICIO. Si dice A se contesta con amenaza, si dice V contestar con vulnerabilidad
Complete las siguientes aseveraciones con una amenaza o una vulnerabilidad según se pida
Ej a) A No considerar cerrar bien la puera -> Que alguien pueda entrar a la casa y robar los bienes del interior
Ej b) V Caere de las escaleras -> no me sujeté del barandal

1.-V Que alguien entre en mi cuenta de Facebook -> No usar contraseña segura ni verificación de dos pasos

2.-V Que alguien me suplante al hablar por teléfono -> No verificar la identidad de quien llama antes de dar información

3.-A No seguir normas del cableado estructurado -> Que se generen fallas en la red, cortocircuitos o pérdida de conectividad.

4.-A No lavarse las manos antes de comer -> Que me enferme por contaminación con bacterias o virus

5.-A No tener en el dispositivo un antivirus -> Que el dispositivo se infecte con malware

6.-V Resbalarse  en el pasillo de la Facultad de Ingeniería -> El piso está mojado y no hay señalización de advertencia

7.-V Posibilidad de reprobrar algún examen -> No haber estudiado lo suficiente

8.-A Confianza plena en lo que me dice mi amigo -> Que me dé información falsa y tome una decisión equivocada

9.-V Llegar tarde a una cita -> No calcular bien el tiempo de traslado ni salir con anticipación

10.-V Perder el proyecto final que estaba almacenado en mi 
dispositivo -> No contar con un respaldo del proyecto

11.-A No tener cuidado al instalar un cierto software en el 
servidor -> Que el servidor se vea comprometido o infectado

12.-A No salir con cubrebocas a la calle cuando estoy enfermo -> Que contagie mi enfermedad a otras personas

13.-V Enfermarse de COVID -> No usar cubrebocas ni mantener sana distancia

14.-A No contar con un respaldo -> Que se pierda la información importante de forma definitiva

15.-V Perder el trabajo -> No cumplir con las responsabilidades laborales asignadas

16.-A Carecer de los medios económicos -> Que no pueda cubrir mis necesidades básicas

17.-V Quedarse sin red al momento de las sesiones en línea -> No contar con un respaldo de conexión (datos móviles)

18.-V Perder la contraseña para ingresar a ágar algún servicio en 
línea -> No usar un gestor de contraseñas ni guardarla de forma segura

19.-A Falta de pintura no flamable en las paredes de la organización -> Que un incendio se propague con mayor facilidad

20.-A Omitir las protecciones contra filtraciones en el techo -> Que se dañen equipos o documentos por filtraciones de agua
```
