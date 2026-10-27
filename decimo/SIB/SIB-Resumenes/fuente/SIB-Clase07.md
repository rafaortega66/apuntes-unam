% materia: Seguridad Informática Básica
% titulo: Clase 7 · Vulnerabilidades: definición y clasificación
% subtitulo: Seguridad Informática Básica · Dra. Cintia Quezada Reyes · martes 22 sep 2026 · Tema 2 (2.2) · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Actividad individual: activos y amenazas (SIB-EC06)
- Frente de la hoja: foto personal y, alrededor, todas las amenazas a la persona y sus rutinas (que un perro muerda, pulgas al pasearlo).
- Reverso: foto de la fachada de la casa (sin número ni dirección) y los eventos dañinos que podría sufrir.
- Propósito: responder la **primera pregunta** de la seguridad, **"¿qué quiero proteger?"**, y ver el espectro completo de amenazas, incluidas pérdidas totales.

## 2. Concepto formal de vulnerabilidad
!!! Definición
Una **vulnerabilidad** es una **debilidad en los procedimientos de seguridad, diseño, implementación o control interno** que podría ser explotada (accidental o intencionalmente) y que resulta en una brecha de seguridad o una violación de la política de seguridad. Es el **"talón de Aquiles"** del bien.
- **Las vulnerabilidades no son amenazas** (error frecuente en internet). Identificarlas responde a la **segunda pregunta**: "¿de qué se quiere proteger?".
- **Riesgo:** existe cuando una amenaza tiene una vulnerabilidad correspondiente que le permite concretarse. Puede haber alta vulnerabilidad sin consecuencia si ninguna amenaza la explota.
- **Sin vulnerabilidad, la amenaza nunca se materializa.**
- No hay relación uno a uno: un bien puede tener 2, 20 o 50 vulnerabilidades.

## 3. El factor humano y el exceso de confianza
- Es un error pensar que todo ataque vendrá de fuera: hay que tener controles para detectar intenciones dañinas **dentro** de la organización.
- Herramientas: **perfilación de conductas** y **simulacros** que evalúan la reacción del personal ("en arca abierta el justo peca").
- La **fuente humana** es el origen más recurrente de amenazas y la **mayor vulnerabilidad**, por **exceso de confianza** (suponer que alguien no hará daño porque saluda sonriente; un campus sin controles de acceso).

## 4. Las seis clasificaciones de vulnerabilidades
| Clase | Ejemplos |
|---|---|
| **Humanas** | Conductas, omisiones, exceso de confianza |
| **Hardware** | Fallas en componentes físicos |
| **Software** | Errores de código, aplicaciones, sistemas operativos |
| **Red** | Debilidades de la infraestructura de comunicaciones |
| **Naturales** | Inclemencias ambientales, fenómenos climáticos |
| **Físicas o de edificaciones** | Construcción donde se alojan los activos (salón A301: filtraciones de agua en lluvias) |
(Las amenazas tienen cinco fuentes de origen, Clase 6; las vulnerabilidades, seis clasificaciones.) De nada sirve capacitar o poner candados si la infraestructura es deficiente.

## 5. La "pregunta de carencia"
| Para identificar | Se pregunta |
|---|---|
| **Amenaza** | "¿Qué malo me podría pasar?" |
| **Vulnerabilidad** | "¿Qué hace falta?", "¿qué no se ha hecho, implementado o considerado?", "¿qué no se tiene?", "¿qué se ha omitido?" |
!!! Ejemplos de la profesora
Amenaza: que llueva y me moje → vulnerabilidad: **carecer de paraguas**. Amenaza: que los tacos al pastor me caigan mal → vulnerabilidad: **carecer de buena digestión** (o de anticuerpos).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

!!! Vulnerabilidad (examen)
Debilidad en procedimientos, diseño, implementación o control interno que puede explotarse y causar una brecha. No es una amenaza. Sin vulnerabilidad no hay daño; riesgo = amenaza que coincide con una vulnerabilidad.

| Concepto | Para recordar |
|---|---|
| Preguntas de la seguridad | 1.ª ¿qué proteger? (activos) · 2.ª ¿de qué protegerlo? |
| Seis clases | Humanas, hardware, software, red, naturales, físicas/edificaciones |
| Mayor vulnerabilidad | El factor humano por exceso de confianza |
| Identificar | Amenaza: "¿qué malo pasa?"; vulnerabilidad: "¿de qué carezco?" |

# PARTE 3 · Mis apuntes de clase
~ Mis apuntes originales de este día (22/09/2026), tal cual los escribí.
```
Apuntes sib 22/09/26

Vulnerabilidades

Identificar las vulnerabilidades
-¿De qué se quiere proteger? (pregunta2)
-El nivel de riesgo se determina analizando la relación entre las amenazas y las vulnerabilidades.
-Un riesgo existe cuando una amenaza tiene una vulnerabilidad correspondiente, aunque hay áreas de alta vulnerabilidad que no tienen consecuencia si no presenta amenazas. 


Definiciones 

Vulnerabilidad:
-Debilidad en los procedimientos de seguridad, diseño, implementación o control interno que podría ser explotada (accidental o intencionalmente) y que resulta en una brecha de seguridad o una violación de la política de seguridad de sistemas. 
-Punto débil de cualquier bien
-Talón de aquiles


Tipo de vulnerabilidades

Debilidades o aspectos atacables en un sistema, -> Humana, Red, Natural, Hardware, Software, Física


¿Como identificar vulnerabilidades?
-¿Qué hizo/hace falta?
-¿Qué no se ha hecho/implementado/considerado?
-¿Qué es lo que no se tiene?
-¿Qué es lo que se ha omitida/se omitió?
```
