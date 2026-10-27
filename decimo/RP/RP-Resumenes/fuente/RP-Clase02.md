% materia: Reconocimiento de Patrones
% titulo: Clase 2 · Selección de características, PCA y SVD
% subtitulo: Reconocimiento de Patrones · Ing. Rubén Omar Azuara Domínguez · lunes 31 ago 2026 (sesión 5 del curso) · Tema 3 · Apuntes y resumen de estudio

# PARTE 1 · Apuntes completos

## 1. Métodos de filtrado
Evalúan cada característica **antes** de entrenar: medir relevancia → ordenar → quedarse con las k mejores.
- **Pearson:** r = Σ(xi − x̄)(yi − ȳ) / √(Σ(xi − x̄)²·Σ(yi − ȳ)²); r > 0 positiva, 0 sin relación lineal, < 0 negativa.
- **Chi-cuadrado:** χ² = Σ (O − E)²/E, con E = total fila × total columna / total.
!!! Ejemplo χ² (compra sí/no × hombre/mujer, 200 casos)
Esperados 55/45; χ² = 4.09 + 5.00 + 4.09 + 5.00 = **18.18**; gl = (2 − 1)(2 − 1) = 1; crítico (α = 0.05) = **3.841**. 18.18 > 3.841 → dependientes → característica **relevante**.
- **ANOVA F:** varianza entre grupos / varianza dentro; F alto = la variable aporta.
| Métrica | Característica | Objetivo |
|---|---|---|
| Pearson | Continua | Continua |
| χ² | Categórica | Categórica |
| ANOVA F | Continua | Categórica |
| Información mutua | Cualquiera | Cualquiera |

## 2. Métodos wrapper
Usan el clasificador como caja negra; el orden de las columnas no importa.
- **Forward:** de vacío (B → 70 %) añadir de una en una: B+A mejora; B+A+C → 80 %; B+A+C+D baja 1 % → óptimo **{B, A, C}**.
- **Backward:** de todas ({A,B,C,D} → 82 %) quitar de una en una: sin A → 83 %; sin D → 84 %; quitar B (−24 %) o C (−14 %) desploma → óptimo **{B, C}, 84 %**.
- **Exhaustive:** todas las combinaciones, **O(2^d)**; garantiza el óptimo global; inviable con más de **15–20** características (un modelo por combinación). No necesita filtrado previo.
| Método | Conviene | Desventaja |
|---|---|---|
| Forward | Pocas relevantes; barato | No quita lo ya añadido |
| Backward | Mayoría relevantes; capta interacciones | Costoso con miles |
| Exhaustive | Óptimo global | Solo con clasificador simple |

## 3. Métodos embebidos
- **Lasso (L1):** la pérdida suma Σ|Wj|; pesos que llegan a **0** descartan la variable.
- **Árboles:** umbrales Xj ≤ t; cada nodo elige la mayor reducción de impureza (Gini o entropía); importancia = Σ (muestras del nodo / total) × reducción; se normaliza a 1.0 y se toma un umbral o top-K.
- No hay regla fija: depende del cómputo; conviene comparar dos métodos.

## 4. Reducción de dimensionalidad y PCA
- Selección conserva las variables; **reducción** las proyecta a nuevas combinaciones (ya no son peso o edad). Motivo: tiempo, almacenamiento y **maldición de la dimensionalidad**.
- **PCA:** componentes no correlacionados ordenados por varianza; Z = A1X1 + A2X2 + …; **Av = λv**.
1. **Centrar** (y opcionalmente escalar): salarios de 15,000 a 1,000,000 dominarían a edades de 18 a 65.
2. Σ = (1/(N − 1)) XᵀX.
3. det(Σ − λI) = 0 → λ y v.
4. Ordenar λ descendente, tomar K vectores → W_K; X_nuevo = X·W_K (N×K).
PC1 = máxima varianza; PC2 ortogonal a PC1; todos ortogonales.

## 5. Ejemplos numéricos
| Σ | Ecuación | λ | Vectores |
|---|---|---|---|
| [[4, 2], [2, 3]] | λ² − 7λ + 8 = 0 (λ − 1)(λ − 8) | **8, 1** | (1/√5)[1, 2]; (1/√13)[2, −3] |
| [[4, 1], [2, 3]] | λ² − 7λ + 10 = 0 | **5, 2** | [1, 1]; [1, −2] |
Suma de λ = varianza total; acumulada = Σ λ (k primeras) / Σ λ (todas).

## 6. Elegir K
- **Codo:** donde la curva acumulada se aplana (13 componentes, codo en el 5.º → K = 5).
- **Umbral:** p. ej. 90 % (8 componentes = 91 %).
- **Kaiser:** λ > 1.

## 7. PCA por SVD
**X = UΣVᵀ**: V = direcciones principales; Σ diagonal con los valores singulares = √λ.
!!! Error típico de examen
Varianza explicada con SVD: **σi² / Σ σj²**. Si no se elevan al cuadrado los valores singulares, los resultados salen mal.
- Centrar X y aplicar SVD directo. Ventajas: estable, sirve con matrices no cuadradas, evita XᵀX, eficiente con N ≫ D o D ≫ N.

## Pendiente
Prácticas desde la siguiente semana (viernes a viernes); equipos de 3 y 2. Próxima: aplicación de PCA y LDA.

# PARTE 2 · Resumen para estudiar
~ Versión corta de lo que más probablemente se pregunta. Léela primero y vuelve a la Parte 1 si algo no queda claro.

| Concepto | Para recordar |
|---|---|
| Filtrado | Pearson, χ² (18.18 > 3.841), ANOVA F |
| Wrapper | Forward añade, Backward quita, Exhaustive O(2^d) |
| Embebido | Lasso (W = 0), importancia en árboles |
| PCA | Centrar → covarianza → det(Σ − λI) = 0 → ordenar → proyectar |
| Ejemplo | [[4,2],[2,3]] → λ = 8 y 1 |
| K | Codo, 90 %, Kaiser λ > 1 |
| SVD | X = UΣVᵀ; varianza con σ² |
