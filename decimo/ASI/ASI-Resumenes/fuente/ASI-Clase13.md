% materia: Administración de Servicios de Internet
% titulo: Clase 13 · Examen de reposición: modelo de datos en BI
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · lunes 12 oct 2026 · Arquitectura de datos · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ La sesión fue el examen de reposición individual (entrega registrada como ASI-R01). Aquí queda lo que se evaluó y cómo resolverlo.

## 1. Formato del examen
| Aspecto | Detalle |
|---|---|
| Dónde | Apartado "reposición" de Teams |
| Modalidad | Individual, práctica, **una hora** (más tolerancia para subir el archivo) |
| Insumos | **Cinco archivos** de datos relacionados (según Classroom: mortalidad infantil, esperanza de vida, países y población) |
| Herramienta | La de BI que prefieras: Power BI, Tableau o Looker Studio |
| Preguntas | Abiertas, sin opción múltiple; **cada una con su especificación** (cómo se calculó) |
Las preguntas pedían justificar dónde vivir, dónde es mejor tener hijos, dónde mueren más adolescentes y si hay correlación entre esperanza de vida y mortalidad infantil.

## 2. El modelo de datos primero
!!! Regla del profesor
"Si no hacen bien el modelo, las respuestas de las preguntas van a estar mal." Primero se importan los cinco archivos y se construyen **las relaciones entre tablas** (llaves y cardinalidades según el negocio); después se contesta.
Un modelo de datos es como un rompecabezas de cinco piezas: si se unen mal dos tablas, todo cálculo sale mal (sumas duplicadas, registros mezclados).
1. Abrir cada archivo y leerlo para ver **cómo se relaciona** con los demás.
2. **Traducir encabezados** en inglés (por ejemplo en Power Query) para no relacionar columnas que no significan lo mismo.
3. Definir relaciones a mano: no esperar que la herramienta las cree sola.
4. Calcular y contestar, justificando cada respuesta.

## 3. Con qué se conecta
Aplica Data Warehouse, ETL y tableros de las Clases 10 y 11: sin un modelo integrado no hay análisis confiable.
Errores comunes: contestar sin revisar las relaciones; confiar en la detección automática; no escribir la especificación.

## Avisos
- Sobre el examen anterior: "el más alto lleva siete". La reposición ya se entregó (Classroom: 13 oct, 03:00). Sigue: reportes semanales del proyecto final y manuales técnico y de usuario.

# PARTE 2 · Resumen para estudiar

!!! Lo que se evaluó
Construir un **modelo de datos** correcto con cinco archivos en una herramienta de BI y responder preguntas abiertas **justificadas**.

| Paso | Para recordar |
|---|---|
| 1 | Leer los archivos y ver cómo se relacionan |
| 2 | Traducir encabezados si vienen en inglés |
| 3 | Relaciones correctas (llaves, cardinalidad) antes de calcular |
| 4 | Cada respuesta con su especificación |
