# ASI · Análisis de ENOE y ENIGH — tutorial paso a paso (Power BI Desktop)

Archivos: `enoe.xlsx` (10,280 personas, 12 columnas) y `viviendas.csv` (90,324 viviendas, 82 columnas, tabla de la ENIGH).
Carpeta con gráficas ya hechas en Python para que compares tus resultados: `~/Desktop/asi-enoe-enigh/*.png`.

> **Aviso importante:** Power BI Desktop **solo funciona en Windows 10/11**. Tu laptop usa Linux, así que necesitas una PC con Windows (por ejemplo, una del laboratorio, si te dejan instalar, o una máquina virtual). No hace falta cuenta de Microsoft para armar el reporte en Desktop; solo se necesita para publicarlo en la nube, y esta tarea no lo pide.

---

## Parte 0 — Instalar (5–10 min)

1. En la PC con Windows abre **Microsoft Store** → busca **Power BI Desktop** → *Obtener / Instalar*. (Alternativa: powerbi.microsoft.com/desktop → *Descargar*.)
2. Ábrelo. Si te pide iniciar sesión, puedes cerrar esa ventana con la X: no la necesitas.
3. Copia `enoe.xlsx` y `viviendas.csv` a una carpeta de esa PC (USB o tu correo).

---

## Parte 1 — Cargar la ENOE

1. Pantalla de inicio → **Obtener datos** → **Excel** → elige `enoe.xlsx` → marca **Sheet1** → **Transformar datos**.
2. En Power Query revisa los tipos de cada columna (icono a la izquierda del nombre):
   - `edad`, `anios_esc`, `hrsocup`, `ingreso_mensual` → **Número entero** (aparecen con el icono 123).
   - Las demás → **Texto**.
3. Corrige un error de captura de la base: columna `niv_edu` → clic derecho → **Reemplazar valores** → «Prrimaria completa» por «Primaria completa».
4. **Cerrar y aplicar** (arriba a la izquierda).
5. En el panel **Datos** (derecha) verás la tabla `Sheet1` con los campos. Los que tienen el símbolo **Σ** son numéricos y se pueden sumar.

**Cómo cambiar Suma / Recuento / Promedio:** en el panel *Visualizaciones*, en el cuadro de valores del gráfico, haz clic en la flechita del campo (por ejemplo `ingreso_mensual`) y elige **Suma**, **Promedio** o **Recuento**. Esto es justo lo que el profesor remarcó: la suma engaña cuando hay muchas personas.

**Consejo:** crea **una página por pregunta** (botón **+** en las pestañas de abajo) y ponle nombre («P1», «P2»…). El profesor dijo que no se amontone todo en una sola.

---

## Parte 2 — Actividad 1: las 8 preguntas (con las respuestas de esta base)

> Las cifras salen de tu `enoe.xlsx`. Úsalas para comprobar que tus gráficos de Power BI están bien. Cada respuesta debe ir **justificada con un gráfico o tabla**.

### P1. Criterios para elegir gráficos correctos
Crea una página con tres ejemplos y explica cuándo usar cada uno:
- **Barras (columnas agrupadas):** comparar categorías. Ejemplo: `niv_edu` en el eje y *Promedio de ingreso_mensual* en valores.
- **Líneas:** tendencia sobre algo continuo u ordenado. Ejemplo: `edad` en el eje y *Promedio de ingreso_mensual*.
- **Dispersión:** relación entre dos variables numéricas. Ejemplo: `anios_esc` (X) contra `ingreso_mensual` (Y).
- Otros: **histograma** (distribución de una variable), **matriz/tabla** (valores exactos), **mapa** (geografía), y **evitar el pastel** si hay más de 4–5 categorías.
Referencia ya hecha: `p1_criterios.png`.

### P2. ¿Qué estado tiene mayor ingreso y cuánto es formal?
1. Gráfico de **barras horizontales**: eje = `estado`, valores = **Suma** de `ingreso_mensual`. Ordena de mayor a menor (menú «…» del gráfico → *Ordenar eje*).
2. Para lo formal: **barras apiladas**, eje = `estado`, leyenda = `tipo_empleo`, valores = **Suma** de `ingreso_mensual`.
- **Resultado:** por **suma**, el mayor es **Coahuila de Zaragoza: $4,519,666**; de eso **$3,199,462 (70.8 %) es formal** y $1,320,204 informal.
- Aclara en tu respuesta que por **promedio** el primero es **Baja California Sur ($9,912)**, seguido de Nuevo León ($9,042) y Sinaloa ($9,007). El Distrito Federal queda en el lugar 15 por promedio.
- Ojo: esta base es una **muestra** (por eso Coahuila tiene 529 personas y el DF 179), no todo el país.
Referencia: `p2_estado_formal.png`.

### P3. ¿Hay brecha salarial entre hombres y mujeres?
Haz tres gráficos con `sex` en el eje: **Suma**, **Recuento** y **Promedio** de `ingreso_mensual`.
- **Suma:** hombres $50,960,865 contra mujeres $24,724,462 (≈2.06 veces).
- **Recuento:** 6,347 hombres contra 3,933 mujeres (≈1.61 veces). La suma se infla por el número de personas.
- **Promedio:** hombres **$8,029** contra mujeres **$6,286** (las mujeres ganan ≈22 % menos en promedio).
- Por **nivel de estudio** los hombres ganan más en todos los niveles (por ejemplo, medio superior y superior: $11,513 contra $9,260).
- Horas: hombres 46.6 h/semana contra mujeres 37.8 h; el ingreso **por hora** casi coincide (≈$45.4 contra $45.5). Es decir, **sí hay brecha en el ingreso mensual, y en esta muestra se explica sobre todo por menos horas trabajadas**, no por un pago por hora distinto.
Referencia: `p3_brecha_sexo.png`.

### P4. ¿Cuántas horas trabajan los que más laboran?
Histograma (o barras con `hrsocup` agrupada: clic derecho al campo → *Nuevo grupo* → tamaño de contenedor 10). Para ver los extremos, usa una **tabla** con `hrsocup` ordenada de mayor a menor.
- **Máximo: 140 horas por semana** (hombre de 52 años, Quintana Roo, informal), seguido de 126 h y 112 h (tres personas).
- 724 personas reportan **70 horas o más**; el promedio general es 43.2 h y la mediana 45 h; el 1 % que más trabaja reporta ≥ 84 h.
- Menciona que 140 h son 20 horas diarias los 7 días: es un valor **atípico** (posible error o reporte inflado).
Referencia: `p4_horas.png`.

### P5. ¿Relación entre horas e ingreso?
**Gráfico de dispersión:** X = `hrsocup`, Y = `ingreso_mensual` (activa «No resumir» en ambos campos). Además, barras de promedio por rango de horas.
- **Correlación 0.19: positiva pero débil.** Promedio de ingreso por rango: ≤20 h $3,861 · 21–35 h $6,618 · 36–48 h $7,966 · 49–60 h $8,057 · >60 h $8,444.
- Conclusión: al principio más horas sí suben el ingreso, pero a partir de ~40 h la ganancia es muy pequeña (trabajar 60+ horas casi no paga más).
Referencia: `p5_horas_ingreso.png`.

### P6. ¿Más estudio implica menos horas?
Barras: eje = `niv_edu`, valores = **Promedio** de `hrsocup`.
- Horas promedio: primaria incompleta 40.9 · primaria completa 43.4 · secundaria 44.6 · medio superior y superior 42.1. Correlación años de estudio–horas: **−0.03 (≈ nula)**.
- **No hay una relación clara** de que a mayor estudio se trabajen menos horas; los de medio superior/superior trabajan solo ~2.5 h menos que los de secundaria.
Referencia: `p6_estudio_horas.png`.

### P7. Edades extremas que mantienen hogar
Líneas con `edad` en el eje y **Suma**, **Recuento** y **Promedio** de `ingreso_mensual`; o una tabla filtrada por edad mínima y máxima.
- **Más joven: 12 años** (8 personas, suman $12,551; todas informales, ingresos de $1,032 a $2,150).
- **Más grande: 98 años** (4 personas, suman $36,980; dos mujeres de Oaxaca, una de Jalisco y un hombre de Baja California que gana $21,500).
- Estas cifras coinciden con lo que mostró el profesor en clase ($12,000 y $36,900 acumulados).
Referencia: `p7_edades.png`.

### P8. Gráfico/tabla combinada: ingreso mensual por sexo, nivel de estudio y número de empleos
Opción más fácil: visual **Matriz**.
- Filas: `sex` y luego `niv_edu` (arrástralos en ese orden).
- Columnas: `num_trabajos`.
- Valores: **Promedio** de `ingreso_mensual`.
Opción gráfica: columnas agrupadas con eje = `niv_edu`, leyenda = `num_trabajos` y **Múltiplos pequeños** = `sex`.
- La base solo tiene **«Uno» y «Dos»** empleos (no 3 ni 4). Dilo en la respuesta.
- Valores (promedio): ver `p8_tabla.csv`. Por ejemplo, hombres de medio superior/superior: $11,937 con dos empleos contra $11,474 con uno; mujeres: $9,036 contra $9,275. **Tener dos empleos casi no cambia el ingreso**; el sexo y el nivel de estudio pesan mucho más.
Referencia: `p8_combinada.png`.

---

## Parte 3 — Actividad 2: ENIGH (`viviendas.csv`)

### Cargar
1. **Obtener datos** → **Texto/CSV** → `viviendas.csv` → **Transformar datos**.
2. `folioviv` debe quedar como **Texto** (empieza con ceros; si es número, se pierden).
3. Crear la entidad: **Agregar columna** → **Extraer** → **Primeros caracteres** → 2 → renombra la columna a `cve_ent`. (Los 2 primeros dígitos del folio son la clave de la entidad: 01 Aguascalientes … 09 CDMX … 32 Zacatecas.) Opcional: crea una tabla pequeña de claves y nombres y relaciónala en la vista **Modelo**.
4. `renta`, `num_cuarto`, `focos` → número. **Cerrar y aplicar**.

### Explicar la ENIGH con tus palabras (puedes usar este texto)
> La ENIGH (Encuesta Nacional de Ingresos y Gastos de los Hogares) es una encuesta del INEGI que se levanta cada dos años y mide cuánto ganan y en qué gastan los hogares mexicanos, además de las características de las viviendas y de las personas. Está dividida en tablas (viviendas, hogares, personas, ingresos, gastos). Este archivo es la **tabla de viviendas**: una fila por vivienda (90,324) con 82 variables como material de paredes, techos y pisos, servicios (agua, drenaje, electricidad), número de cuartos, tenencia (rentada o propia), renta mensual y equipamiento. Sirve para entender las condiciones de vida y de vivienda de los hogares, y por separado se usa para analizar ingresos y gastos.

Nota: la base trae la columna `factor` (factor de expansión) que se usa para proyectar la muestra a todo el país; para esta tarea no hace falta. Para saber qué significa cada código (por ejemplo, `tenencia = 1`), consulta el **diccionario de datos** de la ENIGH en inegi.org.mx. El archivo no indica el año de levantamiento; el profesor pidió usar datos de 2017 o 2018, así que confirma con él si este es el archivo correcto.

### 3 gráficos útiles (aportan a una investigación)
1. **Renta mensual promedio por entidad** (solo viviendas rentadas): barras horizontales, eje = `cve_ent`, valores = **Promedio** de `renta`, con filtro `tenencia = 1` y `renta > 0`.
   - CDMX lidera con ≈ **$6,627**, luego Querétaro ($4,544), Baja California Sur ($4,284), Nuevo León ($4,046). Renta promedio nacional ≈ $3,227 (mediana $2,500). → `enigh_util1_renta_entidad.png`
2. **Viviendas según tenencia**: barras, eje = `tenencia`, valores = **Recuento** de `folioviv`.
   - Códigos de INEGI: 1 rentada (11,566), 2 prestada (10,484), 3 propia pero la están pagando (7,956), 4 propia (58,008), 5 intestada o en litigio (1,910), 6 otra (400). Casi dos de cada tres viviendas son propias. → `enigh_util2_tenencia.png`
3. **Viviendas por número de cuartos**: columnas, eje = `num_cuarto`, valores = **Recuento**. La moda es de 3 cuartos (26,394), después 4 (24,894). → `enigh_util3_cuartos.png`

### 2 gráficos «innecesarios» (de los que piden en empresas)
El profesor pide justamente ejemplos de gráficos que se piden mucho pero no aportan, como el estado civil. Dos opciones con esta base:
1. **Pastel de tipo de vivienda** (`tipo_viv`): categorías codificadas, sin una pregunta que responder. → `enigh_inutil1_pastel_tipo.png`
2. **Dispersión de focos por vivienda**, o cualquier gráfico del número de focos o de pandeos/grietas sin relacionarlo con nada. → `enigh_inutil2_focos.png`
Explica en una línea por qué son innecesarios (no responden una pregunta de negocio, no cambian ninguna decisión, hay demasiadas categorías o ninguna comparación).

---

## Parte 4 — Guardar y entregar

1. **Archivo → Guardar como** → `ASI_ENOE_ENIGH.pbix`.
2. **Archivo → Exportar → Exportar a PDF** (genera un PDF con todas las páginas del reporte).
3. Abre la tarea en Classroom → **Agregar o crear** → sube el `.pbix` y/o el PDF. El profesor no dijo el formato exacto: si tienes duda, súbelos **los dos** y deja un comentario privado diciendo qué subiste.
4. Pulsa **Entregar** antes de las **17:00**.

## Plan si te falta tiempo (prioridad)
1. Instala Power BI y carga `enoe.xlsx` (Parte 0 y 1).
2. Haz **P2, P3 y P8** primero: son las más fáciles de justificar y las que más se parecen a lo visto en clase.
3. Completa P4–P7 usando las referencias de este documento.
4. ENIGH al final: explicación + 3 gráficos útiles + 2 innecesarios.
