% materia: Minería de Datos
% titulo: Clase 9 · Pipeline de clustering, PCA, DBSCAN y asociación
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · jueves 1 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Metodología de la Práctica 1: Python vs. RapidMiner
- **RapidMiner:** importar, visualizar el comportamiento preliminar y capturar imágenes del modelo para las láminas.
- **Python:** el desarrollo analítico completo (filtrado, agregación, estandarización, PCA, algoritmos, validación).
!!! Nunca agrupar transacciones crudas
Las ≈ 59,000 filas transaccionales se **agregan primero** por la entidad a analizar: **por cliente** (1,000–3,000 perfiles con gasto total, ticket promedio, frecuencia, tipos de producto) o **por producto** (sublíneas, presentaciones, marcas).
El valor del científico de datos no es correr código (se consigue en minutos), sino seleccionar variables, estructurar los datos e interpretar con sentido de negocio.

## 2. StandardScaler y PCA
- **StandardScaler:** media 0 y varianza 1; obligatorio con variables heterogéneas (ingresos de $2,500 vs. edades de 20–50) para que las magnitudes grandes no dominen las distancias.
- **PCA:** transforma muchas variables correlacionadas en pocas componentes que conservan la máxima varianza (de 30–50 variables a 2–3).
**Ejemplo de clase:** 3 componentes con **47 % de varianza acumulada** ("excelente"):
| Componente | Cargas altas | Interpretación |
|---|---|---|
| PC1 | Incremento de ingresos e ingresos actuales (0.7, 0.5) | Factores financieros y desempeño del cliente |
| PC2 | Posición de campañas, tiempo en el sitio web | Penetración y actividad de marketing |
| PC3 | Fallas de servicio y antigüedad | Calidad de servicio y redención |
PCA antes del clustering acelera hasta **100 veces** y elimina ruido. Hay que **interpretar** cada componente, no entregar números.

## 3. Qué algoritmo según el dominio
| Algoritmo | Dominio |
|---|---|
| **K-Means** | Segmentación de clientes y marketing (datos tabulares) |
| **Jerárquico / aglomerativo** | Documentos, texto, comunidades |
| **DBSCAN** | Video, datos espaciales, formas irregulares, ruido |
| **GMM** (mezcla gaussiana) | Reconocimiento de voz, segmentación probabilística de imágenes |

## 4. Caso real: Túnel Emisor Oriente
- Agrupar los anillos de concreto del túnel (drena aguas residuales de la CDMX a Hidalgo) por propiedades mecánicas y geológicas. La tuneladora avanzaba ≈ 30 cm/día en roca y hasta 1 m/día en suelo blando.
- 500–600 sensores, ≈ 30 variables clave (frecuencia, varianza, presión de tierra, estrés) → **5 segmentos**.
- Con ingenieros civiles (2–3 meses, 3 científicos de datos): la variable decisiva en los clústers críticos (4 y 1) fue la **presión de tierra n.º 3** (lado derecho inferior), zonas de máximo estrés.
Lección: los clústers se interpretan **con el experto del dominio**.

## 5. Pipeline en Python y elección de ε
1. Limpieza (quitar variables no informativas, p. ej. gramaje).
2. Agregación → 89 perfiles de cliente.
3. StandardScaler.
4. PCA (PC1–PC3) y cargas.
5. K-Means con método del codo y coeficiente de silueta.
6. DBSCAN con prueba de ε.
7. Jerárquico con dendrograma.
8. Comparar siluetas: en ese caso ganó K-Means.
| ε en DBSCAN | Resultado |
|---|---|
| 0.3 | 100 % ruido (etiqueta −1), 0 clústers |
| 1.0 | Todo en 1 clúster |
| **1.2** | Separación óptima en **3 clústers** |
No fijar ε "a ojo": probar una cuadrícula de valores.

## 6. Introducción a reglas de asociación
Técnica **no supervisada** que busca **coocurrencias** de productos en tickets (Soriana, Walmart: millones al mes). Ticket 1 = pan, leche; ticket 2 = huevos, cerveza; ticket 3 = pan, leche.
- Acomodo de tienda (Walmart reorganizó pasillos para forzar el recorrido y la compra por impulso).
- Hallazgos no intuitivos (detergente + jugo de naranja) que disparan investigación de hora, zona y perfil.
- Algoritmos: Apriori y árboles de frecuencia. Base de recomendadores (Spotify, Amazon). Se desarrolla en la Clase 10.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Agregar antes de agrupar.** 59,000 transacciones → perfiles por cliente o por producto. Estandarizar siempre.

!!! PCA (examen)
Pocas componentes que retienen la máxima varianza (47 % con 3 en el ejemplo). Interpretar: PC1 financiero, PC2 marketing, PC3 calidad de servicio.

!!! ε en DBSCAN (examen)
0.3 → todo ruido; 1.0 → un solo clúster; 1.2 → 3 clústers. Probar varios valores.

| Dominio | Algoritmo |
|---|---|
| Clientes / marketing | K-Means |
| Texto / documentos | Jerárquico |
| Video / espacial / ruido | DBSCAN |
| Voz | GMM |
| Coocurrencias en tickets | Reglas de asociación (Apriori) |
