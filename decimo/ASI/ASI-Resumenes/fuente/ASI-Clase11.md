% materia: Administración de Servicios de Internet
% titulo: Clase 11 · Análisis de la ENOE en Power BI
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · lunes 5 oct 2026 · Arquitectura de datos · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. ETL y Data Warehouse
!!! Definición
El **Data Warehouse** es un repositorio preparado para análisis y consultas históricas que integra distintos orígenes. De él se extraen reportes, pero **su información no se reingresa a la base de datos de origen** (se perdería la integridad).
| Fase ETL | Qué hace |
|---|---|
| **Extracción** | Lee de cualquier fuente: Excel, CSV, XML, JSON, PDF, MySQL, Postgres, Oracle, Azure, GitHub, Meta |
| **Transformación** | Limpieza, filtrado y modelado en Power Query |
| **Carga** | Al modelo analítico |
La base transaccional sirve para operar en tiempo real (saldo en un cajero); el DW es como fotografiar el expediente para analizar el pasado.

## 2. El entorno de Power BI Desktop
| Lado izquierdo (5 vistas) | Uso |
|---|---|
| Informe | Lienzo de gráficos |
| Tabla / Datos | Filas y columnas |
| Modelo | Entidad-relación y cardinalidades (1:1, 1:N) |
| DAX y TML | Campos y medidas personalizadas |
| Lado derecho (3 fichas) | Uso |
|---|---|
| Datos | Tablas y campos; **Σ** = campo numérico sumable |
| Visualizaciones | Catálogo de gráficos |
| Filtros | Restringir lo visible |
Pestañas inferiores para varias páginas. Flujo del profesor: Excel/Power Query (análisis básico) → Oracle (almacenamiento) → Power BI (tablero).

## 3. ENOE: edad e ingresos (suma vs. recuento)
ENOE = Encuesta Nacional de Ocupación y Empleo (INEGI). Con la ENOE 2017: Edad en X e Ingreso mensual en Y; Power BI aplica **Suma** por defecto.
- 12 años: 8 personas que trabajan y mantienen un hogar, suman $12,000. 98 años: 4 personas, $36,900 acumulados.
- La curva sube desde los 20–22, cae un poco entre 26 y 28, **pico acumulado a los 36** y repunte a los 42 (puestos ejecutivos).
!!! Trampa de la suma
El pico de la suma es el **acumulado de toda la población de esa edad**, no el sueldo de una persona. Cambiar a **Recuento** muestra cuántas personas hay; a **Promedio**, el ingreso individual.

## 4. Género
- Con suma, los hombres acumulan casi el doble (≈ $647 mil) que las mujeres.
- Con recuento: 6,300 hombres laborando vs. 4,000 mujeres. La mayor baja de mujeres es entre 25 y 35 años (maternidad).
La disparidad en la suma viene sobre todo del **volumen de población ocupada**; no afirmar una brecha solo con la suma.

## 5. Escolaridad
- El campo Nivel de estudios **agrupa Media Superior con Superior**: oculta diferencias. Mejor desglosar por **Años de estudio**.
- Picos de población en 6 (primaria), 9 (secundaria) y 12–17 años (prepa y universidad). La mayor **suma** está en secundaria por volumen.
- Maestría y doctorado: pocas personas (3, 6 o 9), pero con **Promedio** el doctorado sube a ≈ $45,000 mensuales (más becas): el posgrado sí aumenta el ingreso individual.

## 6. Geografía y formalidad
| Análisis | Resultado |
|---|---|
| Suma por estado | CDMX y Estado de México encabezan (densidad poblacional) |
| Promedio por estado | CDMX ni entra al Top 10; arriba Baja California, Nuevo León, Sinaloa, Coahuila, Sonora (norte y occidente) |
| Formal vs. informal | Nacional: el formal da más ingreso bruto. CDMX y Oaxaca: predomina el informal. Nuevo León y Quintana Roo: el formal (industria, hotelería) |
Al comparar formal (bruto) con informal, considerar los impuestos.

## 7. Actividades asignadas
Análisis de la ENOE y de la ENIGH en Power BI (ASI-T01, ya entregada).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Data Warehouse vs. transaccional.** El DW integra fuentes para análisis histórico (ETL: extraer, transformar en Power Query, cargar); sus datos **no regresan** a la base de origen.

**Power BI.** 5 vistas (Informe, Tabla, Modelo, DAX/TML) y 3 fichas (Datos, Visualizaciones, Filtros).

!!! Suma vs. recuento vs. promedio (examen)
La suma engaña: refleja cuántas personas hay. Revisar recuento y promedio antes de concluir (edad, género, escolaridad, estados).

| Hallazgo ENOE | Para recordar |
|---|---|
| Edad | Pico acumulado a los 36 |
| Género | Suma ≈ doble en hombres, pero 6,300 vs. 4,000 personas |
| Escolaridad | Categoría agrupada distorsiona; doctorado ≈ $45,000 promedio |
| Estados | CDMX gana en suma, no en promedio; el norte paga mejor |
| Formalidad | CDMX y Oaxaca informales; Nuevo León y Q. Roo formales |
