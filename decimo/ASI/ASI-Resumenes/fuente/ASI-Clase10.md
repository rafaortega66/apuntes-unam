% materia: Administración de Servicios de Internet
% titulo: Clase 10 · Cubos OLAP, Data Warehouse y tableros
% subtitulo: Administración de Servicios de Internet · Mtro. Juan Ángel Calvillo Pérez · miércoles 30 sep 2026 · Arquitectura de datos · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ "De ahí sí podemos sacar un buen tema para su examen."

## 1. Los cuatro puestos en bases de datos
| Puesto | Qué hace |
|---|---|
| **Modelador / diseñador** | Diseño lógico: tablas, cardinalidades, modalidades y constraints |
| **Arquitecto de datos** (tuning y performance) | Optimiza conociendo software y hardware; calcula el tamaño inicial del almacenamiento (en Oracle el primer paso real es `CREATE TABLESPACE`, no `CREATE DATABASE`) |
| **Administrador (DBA)** | Solo administración y seguridad: usuarios, roles, permisos, `GRANT` y `REVOKE` |
| **Analista de datos** | Define qué datos, cómo, cuándo y cómo se migran para análisis |
El **científico de datos** es otro perfil: estadística inferencial, probabilidad, modelos matemáticos, PL/SQL. Error común: creer que el DBA diseña las tablas (lo hace el modelador).

## 2. Cubo de información (OLAP)
!!! Definición
Un **cubo de información** es una **estructura conceptual** (no un archivo "cubo.ext") para analizar datos desde **varias dimensiones**; pertenece a **OLAP** (Online Analytical Processing). Es N-dimensional.
Se alimenta con **ETL**: Extracción de cualquier origen (ERP, CRM, Excel, PDF) → Transformación → Carga en un solo repositorio.

## 3. Componentes: medidas, dimensiones y pregunta
| Componente | Qué es | Ejemplo |
|---|---|---|
| **Medidas** | Los números a analizar | Ventas, costos, utilidades, margen, impuestos |
| **Dimensiones** | Contexto que filtra las medidas | Tiempo, sucursal, vendedor, cliente, producto |
| **Pregunta / objetivo** | Lo que el cliente quiere saber | "¿Cuánto vendimos por sucursal en 2026?" |
**Jerarquías** (general → detalle): Tiempo: año → trimestre → mes → día. Geografía: país → estado → ciudad (sin país, "Monterrey" aparece también en Venezuela). Producto: categoría → subcategoría → presentación (cigarros → Marlboro → blanco/rojo).
| Tipo de medida | Regla | Ejemplos |
|---|---|---|
| **Aditiva** | Se suma en todas las dimensiones | Ventas, unidades, costos |
| **Semiaditiva** | Se suma en algunas dimensiones, no en todas | Saldo bancario: por cliente sí, a lo largo del tiempo no |
| **No aditiva** | No se suma: campo calculado o derivado | Porcentajes, promedios, sueldo bruto/neto, precio con/sin IVA, edad |
Errores: diseñar empezando por la pregunta y buscar la medida al final; calcular la edad restando solo años.

## 4. Data Warehouse
Repositorio preparado para **consultas, análisis e historia**, con un objetivo de análisis específico; integra CSV, PDF, JSON, web, ERP, CRM y se conecta con machine learning (la caja registradora es la base transaccional; el DW es el archivo histórico).
!!! Regla de integridad
Los datos salen de la base transaccional al DW, pero **nunca regresan del DW a la base de producción**: se perdería la integridad operativa.

## 5. Esquemas estrella, copo de nieve y constelación
| Esquema | Forma normal (según el profesor) | Estructura |
|---|---|---|
| **Estrella** | 1FN (atomicidad) | Una tabla de hechos al centro y todas las dimensiones conectadas directo |
| **Copo de nieve** | 2FN | Una tabla de hechos; las dimensiones tienen subdimensiones (Producto → Categoría, Marca) |
| **Constelación** | 3FN | Varias tablas de hechos que comparten dimensiones |
- La **tabla de hechos** guarda las medidas y una **llave primaria compuesta** por las llaves foráneas de las dimensiones (id_producto, id_date, id_customer, id_employee); cualquier dimensión se consulta con un JOIN sencillo (menor costo en EXPLAIN PLAN).
- Ojo: en la bibliografía de Kimball la estrella es desnormalizada y el copo de nieve normaliza las dimensiones, sin asignar 1FN/2FN/3FN. Para el examen, la clasificación del profesor.

## 6. Tableros ejecutivos (EIS)
EIS (Executive Information System) o dashboard: datos internos y externos resumidos y visuales para la alta gerencia.
| Operación | Qué hace | Ejemplo |
|---|---|---|
| **Slice** | Filtra con una condición | Ventas de 2026 |
| **Dice** | Filtra con varias condiciones | Laptops en CDMX en el Q2 |
| **Drill-down** | Baja en la jerarquía | Año → Q1–Q4 → mes → semana → día |
Herramientas: Excel (tablas dinámicas recomendadas desde 2013, luego Power Query con modelado 1:1, 1:N), **Power BI** (motor de Power Query, más volumen), Python/Spark (más allá de Power BI), SQL/Oracle (`RANK()`, `OVER()`).

## 7. Costos y alertas en Azure
- La nube cobra por **consumo, almacenamiento** (estándar/premium, frecuente/esporádico) y **tiempo de ejecución**; presupuestos en USD.
- **Alerta de costo previsto:** avisa antes, cuando la tendencia indica que se llegará a un porcentaje (ej. 40 %). **Alerta de costo real:** cuando ya se gastó (ej. 50 % de 5,000 USD).
- Caso: una papelería con un pico de 45,000 USD en marzo por mala configuración.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Puestos.** Modelador (diseño), arquitecto (tamaño y rendimiento, TABLESPACE), DBA (seguridad, GRANT/REVOKE), analista (qué, cómo, cuándo migrar).

!!! Cubo OLAP (examen)
Estructura conceptual N-dimensional alimentada por ETL. Tres componentes: **medidas** (números), **dimensiones** (contexto con jerarquías) y **pregunta**. Medidas aditivas (ventas), semiaditivas (saldo) y no aditivas (porcentajes, IVA, edad).

| Esquema | Para recordar |
|---|---|
| Estrella (1FN) | 1 tabla de hechos + dimensiones directas; PK compuesta de FK |
| Copo de nieve (2FN) | Dimensiones con subdimensiones |
| Constelación (3FN) | Varias tablas de hechos |

**DW.** Histórico para análisis; los datos **no regresan** a producción. **EIS:** slice, dice, drill-down. **Azure:** alerta de costo previsto vs. real.
