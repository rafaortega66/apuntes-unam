% materia: Minería de Datos
% titulo: Clase 1 · Proceso KDD, casos de estudio e inicio de la arquitectura de datos
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 1 sep 2026 · Temas 1 y 2 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Las tres tareas y la cadena de valor
| Tarea | Para qué |
|---|---|
| **Regresión** | Cómo las variables afectan a una variable **numérica** (ventas vs. demanda) |
| **Clustering** | Agrupar productos o sucursales con comportamiento semejante |
| **Clasificación** | Asignar categorías (demanda alta, media o baja); árboles de decisión |
**Datos crudos → modelos → patrones → predicciones → mejores decisiones.**

## 2. Datos internos y externos (pastes de Pachuca)
- **Internos:** fecha, producto, cantidad, precio, sucursal, inventario, promociones.
- **Externos:** días festivos, **clima** (frío = más pastes), eventos.
Error común: pronosticar solo con el historial interno.

## 3. Preparación de datos
- **Limpieza:** duplicados con una **regla de unicidad** (fecha + lugar + tipo de compra); faltantes por extrapolación o eliminación.
- **Outliers:** **no son errores**, son eventos distintos (pico cuando juegan los Tuzos); tratamiento aparte.
- **Transformación:** **generalización** (días → semanas, meses), **suavizado** (picos), **normalización** a [0, 1].

## 4. Validación según el modelo
- Regresión: error **≤ 10 %** (evitar mermas o sobreproducción).
- Clustering: grupos consistentes con cada sucursal.
- Operación: cubrir demanda alta, media y baja. Interfaces amigables para la gerencia.

## 5. Casos KDD de los equipos
| Caso | Problema | Algoritmos | Validación |
|---|---|---|---|
| Retail (Eq. 7) | Sobrestock y desabasto | **FP-Growth** (canasta, venta cruzada); regresión | Reglas, ROI |
| Netflix (Eq. 2) | Churn en los primeros 30 días; *cold start* | Regresión logística, K-Means, Apriori | Cancelación de 20 % a 12 %; +20 % reproducción |
| Jugos Boing | ¿A qué país expandirse? (EE. UU. = 41 % de exportaciones) | K-Means, Apriori, árboles/logística, series de tiempo, prescriptivo (NOM-051) | Recall, Lift, MAE < 20 %, CV, SHAP/LIME, baseline |
| Mercado Libre | Última milla en zonas rurales | Muestreo estratificado, **EM** (GPS perdido), PCA, clustering jerárquico, SARIMA, VRP | MAE, RMSE, silueta, backtesting |
| Zara (Eq. 8) | Equilibrio de stock | Series de tiempo, regresión lineal, árboles; indicador de rotación | Precisión + rentabilidad |
Netflix: tiempo de decisión = inicio de reproducción − inicio de sesión; tasa de finalización = minutos vistos / duración.

## 6. Tema 2: arquitectura (arranque)
- Minería de datos: "proceso de análisis de grandes conjuntos de datos".
- Ecosistema mixto (AWS, Google Cloud, Azure, SAP, Oracle, SQL Server, Excel, Hadoop); **≈ 70 %** de la información corporativa ya vive en la nube.
| Base especializada | Uso |
|---|---|
| Blockchain | Cadena de bloques |
| Espacial | Coordenadas, distancias, áreas |
| Columnar | Analítica masiva (Redshift); 2PC |
| Gráfica | Relaciones |
| Documental | Historiales, leyes, libros; búsqueda conceptual |
| Series de tiempo | Datos fechados |
| Vectorial | Similitud de imágenes y textos; base de la IA |
| En memoria | Toda en RAM |

## 7. Seguridad y repositorios
- **Gobernanza:** acceso por usuario **y por columna** (ve nombres, no salarios), por horario (9:00–10:00), firewalls, auditoría con alarmas.
- Tiempo real en finanzas, retail, bolsa, IoT.
| | Base relacional | Repositorio |
|---|---|---|
| Escala | Hasta GB | TB–PB |
| Datos | Tablas | Estructurados y no estructurados |
| Uso | Transaccional | Histórico, miles de usuarios, **metadata obligatoria** |

## Pendiente
- Examen: saber dibujar el **diagrama de arquitectura** (se verán 4–5 de referencia).
- **Proyecto 2:** cada equipo "vende" un proveedor de BD; los demás califican viabilidad, costo y propuesta.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Tareas | Regresión (número), clustering (grupos), clasificación (categoría) |
| Datos | Internos (control propio) y externos (clima, eventos) |
| Limpieza | Unicidad para duplicados; outliers no son errores |
| Transformación | Generalizar, suavizar, normalizar [0,1] |
| Validación | Regresión ≤ 10 % de error |
| Repositorio | TB–PB, metadata, gobernanza por rol, columna y horario |
