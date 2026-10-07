# Retomar: tarea ASI «Análisis de ENOE y ENIGH» (cambio de Linux a Windows)

**Estado al 7 oct 2026:** el usuario cambia de laptop (Linux → Windows) para poder usar Power BI Desktop (solo existe en Windows).
Vence **hoy mié 7 oct, 17:00** (Classroom, 100 pts, grupo 27-1 ASI). Formato/medio de entrega no dicho por el profesor: subir `.pbix` y/o PDF y dejar comentario privado.

## Qué ya está hecho
- Apuntes de la clase: `materias/administracion-de-servicios-de-internet/clase-11.html` (sección `#c11-pendiente` con las dos actividades).
- Página de la tarea: `tareas/asi-c11-prep.html` (datos en `assets/tareas-detalle.json`, clave `asi-c11-prep`).
- Tutorial paso a paso (instalar Power BI, cargar datos, las 8 preguntas con sus respuestas, ENIGH): `TUTORIAL.md` en esta carpeta.
- Gráficas de referencia hechas en Python (NO es la entrega; el profesor pidió Power BI): `p1`…`p8_*.png`, `enigh_*.png`, `p8_tabla.csv`, `resultados_enoe.txt`.
- Scripts: `analisis.py` (ENOE) y `enigh.py` (ENIGH). Necesitan `pandas openpyxl matplotlib` y los archivos `enoe.xlsx` / `viviendas.csv` en la carpeta de trabajo.

## Archivos de datos (NO están en el repo, pesan 16 MB)
`enoe.xlsx` (10,280 personas, 12 cols) y `viviendas.csv` (90,324 viviendas, 82 cols, tabla de la ENIGH): el usuario los bajó de Classroom (estaban en `~/Downloads` en Linux). En Windows hay que volver a bajarlos de Classroom o copiarlos.

## Datos clave para verificar en Power BI
- P2: Coahuila lidera por suma ($4,519,666; 70.8 % formal); por promedio, Baja California Sur ($9,912).
- P3: promedio hombres $8,029 vs mujeres $6,286; recuento 6,347 vs 3,933; ingreso/hora ≈ igual (≈$45), horas 46.6 vs 37.8.
- P4: máx. 140 h/semana; 724 personas ≥ 70 h. P5: correlación horas–ingreso 0.19. P6: correlación estudio–horas −0.03.
- P7: 12 años (8 personas, $12,551) y 98 años (4 personas, $36,980). P8: la base solo tiene 1 o 2 empleos.
- Corregir en Power Query: «Prrimaria completa» → «Primaria completa».

## Qué pedir a Claude al retomar en Windows
«Sigue con la tarea de ASI (ENOE/ENIGH)»: leer este archivo y `TUTORIAL.md`, y acompañar paso a paso en Power BI Desktop (cargar datos, armar cada visual, guardar `.pbix`, exportar PDF, entregar en Classroom).
