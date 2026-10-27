% materia: Minería de Datos
% titulo: Clase 11 · Clustering de clientes y regresión supervisada
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 8 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Exposiciones de la Práctica 3.1 (agrupación)
Segmentar un historial de ≈ **58,900 transacciones** de ventas en Python y RapidMiner.
1. **Limpieza:** textos a minúsculas, columnas 100 % nulas eliminadas, tratamiento de compras atípicas ($6,000 o 165 piezas de queso manchego).
2. **Agregación por cliente:** agrupando por `clave_cliente` quedan **524 clientes** con número de transacciones, monto total, recencia y frecuencia.
3. **Escalado:** `StandardScaler` (para que $6,000 no aplaste a "2 días de recencia") y **logaritmo** `np.log1p` de los montos para comprimir picos.
4. **Modelos:** K-Means con **K = 5** (o 4) por el método del codo + PCA a 2 componentes para graficar; DBSCAN calibrado con la gráfica de k-distancia (2 clusters, o 23.28 % de ruido); jerárquico con dendrogramas (más mezcla).
5. **RapidMiner:** Read CSV → Set Role (`clave_cliente` como id) → Normalize (Z-score) → K-Means (K = 5).
| Cluster | Perfil | Estrategia |
|---|---|---|
| 0 | Especialistas en quesos (poco frecuentes) | Promociones cruzadas con vinos o carnes |
| 1 | Mayoristas (compras masivas aisladas) | Trato VIP/B2B |
| 2 | Ocasionales (pocas compras, importe bajo) | Combos por volumen |
| 3 | Fieles / VIP (frecuencia e importe altos) | Programa de lealtad |
| 4 | Compradores de carnes | Promociones de rotación rápida |
Error común: no estandarizar ni aplicar logaritmo: una variable con números grandes distorsiona todos los centroides.

## 2. Datos para asociación vs. clustering
!!! Granularidad
**Clustering (3.1):** tabla agregada **por cliente** (524). **Asociación (3.2):** las **58,900+ transacciones crudas**, a nivel ticket y producto. Agregar por cliente destruiría la canasta de cada compra.

## 3. Regresión supervisada
!!! Definición
Algoritmo supervisado que modela la relación entre una **variable objetivo continua (Y)** y una o más explicativas (X₁, X₂, …) para entender el peso de cada X y predecir Y.
**Regresión vs. clasificación:** la regresión predice un valor continuo (ventas, precio); la clasificación una categoría discreta o binaria (fraude / no fraude). Error común: usar regresión lineal para una variable binaria.

## 4. Algoritmos de regresión
| Algoritmo | Idea |
|---|---|
| Lineal simple | Y = β₀ + β₁X. Ej.: Precio = 34 + 4.8X → para 90 m²: 34 + 4.8 × 90 = 34 + 432 = **466** |
| Lineal múltiple | Y = β₀ + β₁X₁ + … + βₙXₙ (superficie, habitaciones, antigüedad, ubicación) |
| Polinomial | Curvas con X², X³, …, X^d |
| **Ridge (L2)** | Maneja la **multicolinealidad** penalizando coeficientes grandes; **no elimina** variables, las suaviza |
| **Lasso (L1)** | **Selección automática:** lleva a cero los coeficientes poco significativos |
| SVR | Ajusta dentro de un margen o "tubo" de error ε (consumo eléctrico) |
| Random Forest Regressor | Promedia muchos árboles; robusto con datos complejos |

## 5. Métricas
| Métrica | Lectura |
|---|---|
| **R²** | Proporción de la varianza de Y explicada; cerca de 1 = confiable |
| **MSE** | Promedio de errores al cuadrado; castiga más los grandes |
| **RMSE** | Raíz del MSE: error en unidades de Y |
| **MAE** | Promedio de errores en valor absoluto |
**Debate: ¿y si R² = 0.59?**
1. Revisar estandarización y escala de las variables.
2. Selección de variables para quitar ruido.
3. Limpiar datos, outliers y eventos anómalos históricos.
4. Probar otros algoritmos (Lasso, SVR, Random Forest).
5. Si no hay relación real, descartar el modelo.

## 6. Los tres niveles de validación
1. **Técnica:** R², MSE, Silhouette, matriz de confusión.
2. **Negocio y operativos.**
3. **Estratégica, con la alta dirección.** En FEMSA pasaron las dos primeras, pero el director general solo quería "crecer un 50 % en tiendas": sin alinear el nivel 3, el proyecto se cae.

## Avisos
- Práctica 3.2 (asociación): entrega y exposición el martes. Práctica 3.3 (regresión): el jueves siguiente. Sigue clasificación y series de tiempo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Clustering de clientes.** 58,900 transacciones → 524 clientes; StandardScaler + log1p; K = 5 por el codo; 5 perfiles (quesos, mayoristas, ocasionales, VIP, carnes). Asociación usa transacciones crudas.

!!! Ridge vs. Lasso (examen)
Ridge (L2): penaliza coeficientes grandes, maneja multicolinealidad, no elimina variables. Lasso (L1): lleva coeficientes a cero = selección de variables.

| Concepto | Para recordar |
|---|---|
| Regresión vs. clasificación | Y continua vs. Y categórica |
| Lineal | 34 + 4.8 × 90 = 466 |
| SVR | Tubo ε |
| R², MSE, RMSE, MAE | Varianza explicada; errores² ; raíz; absolutos |
| Métricas malas | Escala, variables, limpieza, otro algoritmo, descartar |
| Validación | Técnica → negocio → alta dirección |
