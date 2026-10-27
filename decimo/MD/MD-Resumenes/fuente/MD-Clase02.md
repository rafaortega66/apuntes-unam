% materia: Minería de Datos
% titulo: Clase 2 · Repositorios, Data Warehouse, Data Mart, ERP y Data Lake
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 3 sep 2026 · Tema 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Repositorios y gobernanza
- **Repositorio:** contenedor de grandes volúmenes (TB o PB) con **metadatos**, información **histórica** y gobernanza más amplia que una base de datos.
- **Gobernanza:** acceso por **rol, tabla, columna y horario**; control del tiempo de respuesta.
- **Two-Phase Commit (2PC):** asegura que una transacción distribuida no quede a medias entre nodos.
!!! Para examen y proyectos
Saber diseñar el **esquema de arquitectura de datos**: redes, servidores, firewalls y acceso restringido por roles y horarios.

## 2. Data Warehouse, Data Mart y virtualización
| Concepto | Qué es |
|---|---|
| **Data Warehouse** | Repositorio central de datos actuales e históricos de muchas fuentes; la **única fuente confiable** de la verdad |
| **Data Mart** | Repositorio de **un área** (RR. HH., Finanzas), con usuarios de esa área |
| **Virtualización** | Consultar los datos **en su origen en tiempo real** sin moverlos; el usuario ve 14 campos aunque el origen tenga 180. **≈ 70 %** de los datos se manejan así |
| ETL / ELT | Una de las formas de alimentar el Warehouse |
Error común: creer que un Warehouse tarda años; con tecnología moderna se hace elástico en 2–3 meses (Bancomer gastó 5 millones de dólares y 3 años con Teradata y fracasó).

## 3. ERP
Núcleo de la empresa (p. ej. **SAP**): finanzas, nómina, facturación, inventarios. Alimenta la minería.

## 4. Data Lake
Datos **no estructurados** (imágenes, audio, documentos, redes sociales) en su **formato nativo**, sin reglas estrictas: se guardan petabytes rápido, pero es más difícil encontrar y explotar la información. No reemplaza al Warehouse: requiere etiquetado y catalogación.
**Jerarquía:** base de datos (transaccional) → repositorio (histórico, gobernanza) → Data Warehouse (empresarial) → Data Lake (crudo).

## 5. Casos KDD de los equipos
| Equipo / caso | Problema | Limpieza y transformación | Algoritmos |
|---|---|---|---|
| 9 · Scitum/Telmex | Falsos positivos en el SOC | **No** borrar faltantes ni outliers (pueden ser ataques); solo duplicados; "intentos fallidos por minuto" | Clasificación; series de tiempo |
| 13 · LEGO | Empaques sobredimensionados y piezas de más | Quitar sets atípicos (65,000 piezas); ID único | K-Means (3 clases) + Silhouette; Random Forest para manuales digitales |
| 12 · SmartFit | Churn por saturación en hora pico | Quitar biométricos dobles; imputar con la media del usuario; normalizar 0–1; discretizar horas | Naïve Bayes; K-Means de perfiles |
| 11 · CEMEX | Agua potable en el concreto | Faltantes = media de la hora anterior y siguiente; separar error de lectura de fuga | K-Means; **Z-Score** para fugas; regresión múltiple; Silhouette |
Errores de presentación: faltas de ortografía (un cliente canceló por eso), láminas saturadas, JSON/CSV en la presentación ejecutiva, no tener *elevator pitch* (1–2 min).

## Pendiente
- Más presentaciones el martes.
- **Proyecto 2:** cada equipo recibe un proveedor (Oracle, Amazon, Google…) y lo "vende" técnicamente.
- Investigar por cuenta propia Data Warehouse y Data Lake.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Repositorio | Metadatos, histórico, TB–PB, gobernanza |
| Gobernanza | Rol, tabla, columna, horario |
| Warehouse / Mart | Toda la empresa (única verdad) / un área |
| Virtualización | Consulta en origen, sin mover; ≈ 70 % |
| Data Lake | Crudo, no estructurado, formato nativo |
| ERP | Núcleo transaccional (SAP) |
| 2PC | Transacciones distribuidas consistentes |
