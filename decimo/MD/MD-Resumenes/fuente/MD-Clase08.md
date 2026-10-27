% materia: Minería de Datos
% titulo: Clase 8 · Algoritmos de agrupación (clustering)
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 29 sep 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Cierre de exposiciones: AWS y SAP HANA
- **AWS:** de e-commerce a dominar la nube. En una empresa se evalúan 3–4 proveedores con matrices de capacidad técnica e integración; **lo técnico no se regatea**, el regateo comercial solo con la opción ganadora.
- **SAP HANA:** procesa **en memoria RAM** (miles de veces más rápido que disco) y almacena **por columnas** (column-store) con un **diccionario de compresión** (si "México" se repite 10,000 veces, se guarda una).
| Componente | Función |
|---|---|
| SDI (Smart Data Integration) | Automatiza el proceso KDD |
| Apache Kafka / Spark | Ingesta en tiempo real / procesamiento masivo en memoria |
| Single Source of Truth | Estructurados (dashboards), no estructurados (Data Lake), históricos (HDFS) |
| PAL / APL | Algoritmos de clustering / modelos predictivos automatizados |
| SAP Analytics Cloud y Cockpit | Dashboards predictivos / rendimiento, memoria, particionamiento |
| Aislamiento de memoria | RAM dedicada para consultores externos sin tocar el núcleo |

## 2. Equipos y herramientas
12 equipos definitivos de 3. **Python** da control total de parámetros y volumen; **RapidMiner** es visual para explorar rápido (uno del equipo debe dominarlo y capacitar a los demás). No se sustituyen.

## 3. Fundamentos del clustering
Agrupar sin etiquetas los datos más parecidos. Criterios de calidad:
- **Homogeneidad intra-segmento** (parecidos dentro).
- **Heterogeneidad inter-segmentos** (bien separados).
- **Estabilidad y manejabilidad** en el tiempo.
!!! Criterio principal de evaluación
Correr el código toma minutos; lo valioso es **interpretar los segmentos, ponerles un nombre reconocible y extraer conocimiento de negocio**.

## 4. K-Means
Fronteras **esféricas** por distancia euclidiana.
1. Fijar **K** (probar el central y sus vecinos: 3, 4, 5).
2. Inicializar K centroides.
3. Asignar cada punto al más cercano, recalcular promedios y mover centroides; repetir (10–50 iteraciones suelen bastar).
4. Con volúmenes masivos (100,000) muestrear o filtrar por categóricas antes.
| Parámetro | Controla |
|---|---|
| `n_clusters` (K) | Número de grupos |
| `max_iter` | Iteraciones máximas |
| `n_init` | Inicializaciones distintas |
| `random_state` | Reproducibilidad |
**PCA y t-SNE:** proyecto con 250 variables → 25 → **3 componentes** (revisar varianza explicada acumulada) y K-Means sobre el espacio reducido. **t-SNE** para estructuras no lineales.
**Elegir K y evaluar:** **método del codo** (inercia o **WSS** vs. K; en clase el codo en K = 7), **coeficiente de silueta** (compacidad + separación), Davies-Bouldin, Dunn.

## 5. DBSCAN
Agrupa por **densidad y conectividad**, no obliga a todos los puntos a caer en una esfera.
- **ε:** radio de vecindad (se mostró con 0.1, 0.2 y 0.4). **min_samples:** mínimo de puntos para un núcleo denso.
- Marca automáticamente los aislados como **ruido** (outliers).
- Usos médicos: tumores en resonancias, irregularidades en la córnea.
!!! Criterio del profesor
**K-Means** para estudios comerciales y de mercadotecnia; **DBSCAN** para formas complejas e irregulares e imágenes médicas.

## 6. Clustering jerárquico
- **Aglomerativo** (ascendente: cada punto empieza solo y se unen los más cercanos) o **divisivo** (descendente). Se visualiza con un **dendrograma** y se decide la altura del corte.
- **Caso Coca-Cola FEMSA:** 31,600 tiendas de abarrotes en Monterrey, muestra de 12,000, en R (≈ 3 meses). Un segmento vendía muchísimas bebidas energéticas; estaban **cerca de escuelas o campos deportivos** o tenían refrigeradores muy visibles → refrigeradores y promociones solo para esas tiendas.

## 7. GMM, Mean-Shift e imágenes
- **GMM:** mezcla de gaussianas; admite **formas elípticas** y varianzas distintas; voz e imágenes por textura y color.
- **Mean-Shift:** desplaza una ventana hacia la mayor densidad; seguimiento en video (publicidad más cara en zonas de la cancha con más atención).
- **Imágenes RGB:** K-Means (K = 3) da regiones esféricas rígidas; DBSCAN capta ramas y sombras; GMM gradientes suaves.
!!! StandardScaler obligatorio
Con escalas dispares (ingresos ≥ $3,500 vs. edades 18–60) estandarizar a media 0 y desviación 1 **antes** de cualquier distancia euclidiana.

## Avisos
- **Práctica 1:** pipeline completo de clustering por equipos sobre ≈ 50,000 registros (StandardScaler, PCA/t-SNE, 3 algoritmos, WSS/silueta).

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Buen clustering.** Homogéneo dentro, heterogéneo entre, estable, y con **nombre y sentido de negocio**.

| Algoritmo | Para recordar |
|---|---|
| K-Means | Esferas; fijar K (probar vecinos); codo (WSS) y silueta; perillas n_clusters, max_iter, n_init, random_state |
| DBSCAN | Densidad con ε y min_samples; detecta ruido; formas irregulares e imágenes médicas |
| Jerárquico | Aglomerativo / divisivo; dendrograma (FEMSA) |
| GMM | Elipses; voz, textura |
| Mean-Shift | Hacia mayor densidad; video |

!!! Pipeline (Práctica 1)
StandardScaler → PCA/t-SNE → 3 algoritmos → evaluar (WSS, silueta) → interpretar y nombrar clústers.

**SAP HANA.** En RAM y por columnas con diccionario de compresión.
