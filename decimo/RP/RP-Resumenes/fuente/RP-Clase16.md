% materia: Reconocimiento de Patrones
% titulo: Clase 16 · Árboles de decisión y Random Forest
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 19 oct 2026 (sesión 19 del curso) · Tema 8 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos
~ Casi todo se resolvió con números en el pizarrón. Diapositivas: deck 14 del profesor («CART y Random Forest»).

## 1. Repaso: SVM
Busca el hiperplano que **maximiza el margen** (distancia mínima a los puntos más cercanos, los **vectores de soporte**). La versión básica supone datos linealmente separables; si no lo son:
- **Variables de holgura** ξᵢ con el parámetro **C**: permiten cierta cantidad de violaciones al margen.
- **Truco del kernel:** proyecta implícitamente a un espacio de mayor dimensión donde sí se separan.
- Multiclase: uno contra uno o uno contra el resto.

## 2. Árbol de decisión
Método supervisado **no paramétrico** que divide el espacio jerárquicamente con reglas "si… entonces…" (como "Adivina Quién").
| Parte | Qué es |
|---|---|
| Nodo raíz | Primera pregunta, sobre el atributo más informativo |
| Nodos internos | Evalúan una condición sobre una característica |
| Hojas | Contienen la clase predicha |
| Rama | Camino de la raíz a una hoja |
Cada corte es **perpendicular a un eje**: el espacio queda en regiones hiperrectangulares. No calcula distancias ni combinaciones lineales, así que **no necesita estandarizar**. Acepta variables **categóricas** directamente (sin one-hot obligatorio).

## 3. Impureza: Gini y entropía
!!! Fórmulas
**Gini(t) = 1 − Σ pᵢ²** (probabilidad de clasificar mal un elemento al azar). **Entropía H(t) = −Σ pᵢ log₂ pᵢ**. En binario: Gini 0 = puro, **0.5 = máxima impureza**; la entropía máxima es 1.
Ejemplo: 10 ejemplos, 7 A y 3 B → Gini = 1 − 0.49 − 0.09 = **0.42**. ¿70/30 es aceptable? No: todavía es mucha impureza; se busca acercarse a 0 (95/5, 100/0). El algoritmo **voraz** elige en cada nodo el corte que más reduce la impureza.

## 4. Umbrales en atributos continuos
Se ordenan los valores y se prueban solo los **puntos medios** entre consecutivos: Tᵢ = (xᵢ + xᵢ₊₁)/2.
Ejemplo (5 personas, ¿compran?, corte en edad 35):
| Lado | Ejemplos | Gini |
|---|---|---|
| Edad ≤ 35 | 2 (1 sí, 1 no) | 1 − 0.25 − 0.25 = 0.5 |
| Edad > 35 | 3 (1 sí, 2 no) | 1 − 0.111 − 0.444 = 0.444 |
| **Ponderado** | (2/5)(0.5) + (3/5)(0.444) | **0.466** |
Categóricos con muchos valores: se evalúan particiones binarias en subconjuntos.

## 5. Ejercicio: diagnóstico con 8 pacientes
8 pacientes (4 enfermos, 4 sanos); atributos fiebre, tos, dolor de cabeza.
1. **Raíz:** Gini₀ = 1 − (4/8)² − (4/8)² = 0.5.
2. **Fiebre:** alta 4 (3 sí, 1 no) → 0.375; baja 4 (1 sí, 3 no) → 0.375; ponderado 0.375; reducción 0.125.
3. Tos y dolor de cabeza dieron **lo mismo**. **Desempate: gana la primera característica evaluada → fiebre en la raíz.**
4. **Segundo nivel (tos):** fiebre alta + tos → 2 enfermos, Gini 0, hoja; fiebre alta sin tos → 1 y 1, Gini 0.5. Fiebre baja sin tos → 2 sanos, hoja; fiebre baja con tos → 1 y 1, Gini 0.5.
5. **Tercer nivel:** dolor de cabeza separa cada par mixto en dos hojas puras.
Resultado: **6 hojas**. En cuanto un nodo llega a Gini 0 se vuelve hoja y ya no se expande. Pero hojas de un paciente son memoria, no aprendizaje.

## 6. Sobreajuste y poda por costo-complejidad
Sobreajuste: el árbol memoriza hojas de 1–2 ejemplos (100 % en entrenamiento, se desploma en prueba).
- **Pre-poda:** limitar al construir (`max_depth`, `min_samples_split`, `min_samples_leaf`).
- **Post-poda:** construir completo y recortar con α.
!!! α crítico
**α_crítico = [R(t) − R(T)] / (|T_t| − 1)**. R(T) = error del subárbol; R(t) = error si se colapsa a una hoja; |T_t| = hojas del subárbol. Si α_crítico < α global → **se poda**.
Ejercicio (N = 40; subárbol de 2 hojas):
| Paso | Cálculo |
|---|---|
| Hoja 1: 10 (8 A, 2 B) | error 0.2 |
| Hoja 2: 10 (7 A, 3 B) | error 0.3 |
| R(T) | (10/40)(0.2) + (10/40)(0.3) = 0.05 + 0.075 = 0.125 |
| Colapsado: 20 (15 A, 5 B), predice A | R(t) = 5/40 = 0.125 |
| α_crítico | (0.125 − 0.125)/(2 − 1) = **0** < 0.1 → **se poda** |

## 7. Random Forest
Ensamble de árboles independientes: **voto mayoritario** (clasificación) o **promedio** (regresión).
**1. Bagging** (bootstrap aggregating): cada árbol con una muestra de tamaño N **con reemplazo**.
!!! Demostración del 36.8 % OOB
P(elegir una muestra en una extracción) = 1/N → no elegirla = 1 − 1/N → no elegirla en N extracciones = (1 − 1/N)ᴺ → lím = **e⁻¹ ≈ 0.368**. Cada árbol ve ≈ 63.2 % de datos distintos; el 36.8 % fuera de la bolsa (**OOB**) es validación interna.
**2. Subespacios aleatorios:** en cada corte solo se evalúan m ≪ D características (p. ej. m = √D), para que los árboles no salgan iguales.
**Resultado en clase:** un árbol CART 0.91 de exactitud; Random Forest de 40 árboles **0.95** (menos varianza). Costo: se pierde la interpretabilidad.

## Avisos
- Tarea 2 (Classroom, vence viernes 23 oct, 7:00): DBSCAN a mano (núcleo, frontera, ruido), Bayes ingenuo discreto y Bayes gaussiano continuo.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Fórmula / regla | Para recordar |
|---|---|
| Gini | 1 − Σp²; binario: 0 puro, 0.5 máximo (70/30 → 0.42) |
| Entropía | −Σ p log₂ p; máximo binario 1 |
| Umbral continuo | Punto medio entre valores consecutivos ordenados |
| Gini ponderado | Σ (n_hijo/n)·Gini_hijo (edad ≤ 35 → 0.466) |
| Empate | Gana el primer atributo evaluado |
| Hoja | Nodo con Gini 0: ya no se divide |

!!! Poda (examen)
α_crítico = [R(t) − R(T)] / (|T_t| − 1). Si es menor que el α global, la rama no mejora el error y se poda (ejemplo: 0 < 0.1).

**Random Forest.** Bagging con reemplazo: (1 − 1/N)ᴺ → e⁻¹ ≈ 36.8 % OOB. Más subespacios aleatorios (m ≈ √D). Reduce varianza: 0.91 → 0.95. Pierde interpretabilidad.

**Árboles vs. otros.** No requieren estandarizar y aceptan categóricas. SVM: margen máximo, holgura C y kernel.
