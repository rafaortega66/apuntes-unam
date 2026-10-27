% materia: Minería de Datos
% titulo: Clase 10 · Market Basket Analysis y reglas de asociación
% subtitulo: Minería de Datos · M.C. José Concepción Roberto Olvera López · martes 6 oct 2026 · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Formato de los entregables
- **Python:** notebook desglosado paso por paso, deteniéndose en los puntos clave.
- **RapidMiner:** diapositivas (PPT o PDF) con capturas del flujo y comentarios.
- Prórroga de la práctica de clustering: jueves a mediodía.

## 2. Market Basket Analysis
!!! Definición
Técnica que analiza transacciones o tickets para descubrir qué productos o eventos **se relacionan o se compran juntos**. Cada regla tiene **antecedente (X)** y **consecuente (Y)**: si compra pan y huevos (X), ¿qué probabilidad hay de que lleve leche (Y)?
Busca relaciones obvias y también **patrones raros** con frecuencia significativa (detergente + jugo de naranja). Comprar juntos no significa causalidad.
| Sector | Ejemplo |
|---|---|
| Retail | Acomodo de estantes, paquetes, venta cruzada (Amazon, Mercado Libre) |
| Manufactura | Temperatura alta + vibración alta → falla de sensor (mantenimiento preventivo) |
| Salud | Hipertensión + diabetes → control de glucosa (HbA1c); dolor de pecho → electrocardiograma |
| Telecomunicaciones | Sugerir líneas o paquetes de streaming según la velocidad de internet |

## 3. Soporte, confianza y lift
| Métrica | Fórmula | Pregunta |
|---|---|---|
| **Soporte** | Transacciones con X e Y ÷ total | ¿Qué tan popular es la combinación? |
| **Confianza** | Transacciones con X e Y ÷ transacciones con X | Si ya llevo X, ¿qué tan seguro es que agregue Y? |
| **Lift** | Confianza(X→Y) ÷ Soporte(Y) = Sop(X∪Y) ÷ [Sop(X)·Sop(Y)] | ¿Cuánto más probable que al azar? |
**Ejemplo:** cepillo de dientes (X) aparece en 14 transacciones y junto con leche en 10 → confianza = 10/14 = **0.7 (70 %)**. Valores atractivos de confianza: > 0.7, mejor > 0.8.
**Lift en Python:** yogur griego de fresa → yogur de fresa **9.28**; jamón de pavo → chorizo de pavo **8.39**. Lift alto (sobre todo > 4.5) = relación muy fuerte y rentable.
!!! El lift es el indicador más fino
Compara contra una compra al azar. Guiarse solo por la confianza infla productos masivos que se venden solos.

## 4. Apriori, ECLAT y FP-Growth
| Algoritmo | Cómo trabaja | Ventajas | Desventajas |
|---|---|---|---|
| **Apriori** | Cuenta artículos individuales, elimina los que no llegan al soporte mínimo, combina sobrevivientes de 2 en 2, 3 en 3… | Simple | Muchos escaneos: con millones de registros "se duerme" |
| **ECLAT** | Listas de identificadores de transacción (**TID-lists**) por artículo; la asociación es la **intersección** de listas | Menos cómputo; muy bueno con datos dispersos | Mucha RAM; pierde eficiencia con datos densos |
| **FP-Growth** | 1.er escaneo: contar y ordenar de mayor a menor; 2.º: construir el **FP-Tree** comprimido y podar ramas bajo el soporte | **Solo 2 escaneos**; eficiente con grandes volúmenes; el más usado | — |
Ejemplo Apriori en vivo (min_support = 2): en {A, C, D}, D tuvo frecuencia 1 < 2 → "adiós, fuera"; {B, C, D} tuvo 2 → se mantiene. Error común: Apriori en bases masivas de producción.

## 5. Los tres niveles de validación ("es pregunta de examen")
1. **Técnica:** el científico de datos mide las métricas (soporte, confianza, lift).
2. **Operativa:** con quienes operan el día a día (gerentes de tienda, supervisores, médicos): ¿tiene sentido práctico?
3. **Directiva:** con la alta dirección, alineada a la estrategia (p. ej. crecer 50 % en tiendas).
Si una etapa falla, el modelo no se implementa (como una receta: el chef la prueba, los meseros ven si se puede servir, el dueño ve si deja ganancia).

## 6. Caso "comidas preparadas" (Práctica 2)
- Dataset de **55,000 registros** de tickets; soporte mínimo **0.01 (1 %)**.
- Enfoque en comidas preparadas (burritos, flautas, pizzas, pechugas rellenas) para encontrar **productos ancla** que arrastren la compra de otros.
- Pechugas rellenas ↔ pizzas, salchichas y frijoles; queso americano ↔ burritos y pasta; chorizo + queso americano + queso fresco → crema dulce, pasta y salchicha (lift 8.39).
- Comparar Apriori vs. FP-Growth en Python y RapidMiner.
Error común: soporte demasiado bajo (0.0001) satura con más de 90 reglas irrelevantes.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

**Market Basket.** Reglas X → Y sobre tickets; valen las obvias y sobre todo las sorprendentes frecuentes.

| Métrica | Fórmula |
|---|---|
| Soporte | n(X∪Y) / N |
| Confianza | n(X∪Y) / n(X) — 10/14 = 0.7; buena > 0.7–0.8 |
| Lift | Conf / Sop(Y) — > 1 asociación; > 4.5 muy fuerte |

!!! Algoritmos (examen)
Apriori: muchos escaneos, lento con volumen. ECLAT: TID-lists e intersecciones, bueno en datos dispersos, mucha RAM. FP-Growth: FP-Tree con 2 escaneos, el más usado.

!!! Tres niveles de validación (examen)
Técnica (métricas) → operativa (personal de piso) → directiva (estrategia).
