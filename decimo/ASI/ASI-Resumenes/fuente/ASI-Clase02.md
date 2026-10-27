% materia: Administración de Servicios de Internet
% titulo: Clase 2 · Cascada/PMBOK vs. Scrum y Gantt en Microsoft Project
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · lunes 31 ago 2026 · Metodología del proyecto · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Fechas del curso
- Semestre termina el **28 de noviembre**; aquí se fijó entrega del proyecto el **16 de noviembre**, "inamovible".
!!! Actualización
Esa fecha única la reemplazó el calendario de 3 entregas negociado en la Clase 6: **20 sep, 18 oct y 22 nov**.

## 2. Metodología tradicional: Cascada / PMBOK
- Planeación exhaustiva; una fase al 100 % antes de la siguiente: **análisis, diseño, implementación, pruebas, mantenimiento**.
- Ventajas: **trazabilidad**, entregas puntuales; control por el **triángulo de hierro** (alcance, costo, tiempo). Exige requerimientos **funcionales, no funcionales y de sistema**.
- Desventajas: inflexible; el cliente ve resultados hasta el final; errores detectados tarde.

## 3. Metodología ágil y Manifiesto Ágil (2001)
**Scrum no es una metodología**: la metodología es ágil; Scrum es un **marco** (framework).
- Pilares: **iterativo, incremental, colaborativo, respuesta al cambio**.
- Valores: individuos sobre procesos; software funcionando sobre documentación; colaboración con el cliente sobre contratos; respuesta al cambio sobre el plan.
- Desventajas: mucha disciplina; costo menos predecible (**+15 %** de margen); difícil de escalar; poca documentación.

## 4. Comparativo
| Criterio | Tradicional | Ágil |
|---|---|---|
| Planificación | Exhaustiva al inicio | Iterativa y continua |
| Requerimientos | Fijos | Cambiantes |
| Entrega | Única, al final | Incrementos frecuentes |
| Cliente | Puntual | Constante |
| Documentación | Extensa | Mínima |
| Cambio | Costoso, control formal | Bienvenido |

## 5. Scrum y PMBOK a detalle
- **Sprints** de 2–4 semanas con incremento utilizable. Roles: **Product Owner**, **Scrum Master**, **Equipo de desarrollo**.
- Eventos: Sprint Planning, **Daily (máx. 15 min)**, Sprint Review, Retrospective. Artefactos: Product Backlog, Sprint Backlog, Incremento.
- **PMBOK** (PMI): **5 grupos de procesos** (inicio, planificación, ejecución, monitoreo/control, cierre) y **10 áreas** (integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones, interesados). Rol central: **Project Manager**; cambios por junta formal.

## 6. Gantt en Microsoft Project (también GanttProject o Jira)
1. Cambiar a **Programación automática**.
2. Fases: análisis, diseño, implementación, pruebas, cierre.
3. Tarea resumen ("Proyectito ADS") + **Aplicar sangría** → calcula la duración total (56.13 días desde el 31 ago).
4. Subtareas de análisis: requerimientos funcionales, no funcionales y de sistema.
5. **Vincular tareas** (Ctrl+F2) fin-a-comienzo; comienzo-a-comienzo escribiendo **4CC** en predecesoras.
6. Si termina después del límite (salió 1 dic), ajustar duraciones.

## 7. Recursos: Trabajo, Material, Costo
| Tipo | Qué es | Tarifa |
|---|---|---|
| **Trabajo** | Personas o máquinas con desgaste | Por hora, día, semana; capacidad % |
| **Material** | Compras de gasto único que se cobran | Costo unitario |
| **Costo** | Gastos fijos (internet, luz) | Sin tarifa por hora |
Ejemplo: Paola $12/h, Luisa $10/h, becario $1/sem, Scrum Master $150/día (Trabajo); Internet/Luz (Costo); PC1 $3/sem (Trabajo); Mac Mini $27,000 (Material); PC3 del alumno (Costo).
!!! Error de asignación (examen)
Asignar recursos a la **tarea resumen** multiplica tarifas por todo el proyecto: **3,272 horas y más de $34,000 USD**. Asignándolos a cada **subtarea**: **304 horas y $812.50 USD**.

## Pendiente
Elegir metodología y roles; entregar el Gantt con dependencias y recursos; la siguiente clase se asignan los temas.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Scrum | Marco, no metodología; sprints 2–4 semanas; PO, SM, equipo; daily 15 min |
| PMBOK | 5 grupos de procesos, 10 áreas; Project Manager |
| Ágil | Iterativo, incremental, colaborativo, respuesta al cambio (2001) |
| Cascada | Triángulo de hierro; fase completa antes de la siguiente |
| Recursos | Trabajo, Material, Costo |
| Error | Recursos en la tarea resumen: $34,000 vs. $812.50 |
