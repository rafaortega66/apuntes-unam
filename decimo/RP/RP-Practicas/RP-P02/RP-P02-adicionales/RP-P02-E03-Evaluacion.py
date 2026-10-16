"""
Ejercicio 3: Metricas de evaluacion (Silhouette, DBI, ARI)
Practica 2 - Reconocimiento de Patrones
Rafael Ortega de la Paz (420054085) y Sebastian Andre Fuentes Poma (620271005)
"""

# # Práctica 2 — Ejercicio 3: Evaluación de los clusters
#
# En este ejercicio se selecciona el mejor caso de cada algoritmo y se calculan las métricas solicitadas:
#
# - Coeficiente de Silhouette.
# - Índice Davies-Bouldin (DBI).
# - Adjusted Rand Index (ARI).
#
# Se utilizan nuevamente **los mismos datos del Ejercicio 1**, generados con `random_state=20`.

# ## Datos sintéticos
#
# Se reconstruye exactamente el dataset utilizado en los Ejercicios 1 y 2.

from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    adjusted_rand_score
)

X, y_true = make_blobs(
    n_samples=400,
    centers=4,
    cluster_std=1.7,
    random_state=20
)

plt.figure(figsize=(7, 5))
plt.scatter(X[:, 0], X[:, 1], c=y_true, cmap="viridis", s=30)
plt.title("Datos sintéticos")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# # Selección del mejor caso de K-Means
#
# Para mantener el criterio del Ejercicio 1, se ejecutan las seis corridas utilizadas allí y se selecciona como mejor caso el que tenga la **menor inercia final**.
#
# Esto permite que la selección sea reproducible y basada en el resultado del algoritmo, no en las métricas que se evaluarán posteriormente.

def asignar_clusters(X, centroides):
    distancias = np.sum(
        (X[:, None, :] - centroides[None, :, :]) ** 2,
        axis=2
    )
    etiquetas = np.argmin(distancias, axis=1)
    inercia = np.sum(np.min(distancias, axis=1))
    return etiquetas, inercia


def inicializacion_aleatoria(X, k, seed):
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(X), size=k, replace=False)
    return X[indices].copy()


def inicializacion_kmeans_plus_plus(X, k, seed):
    rng = np.random.default_rng(seed)

    primer_indice = rng.integers(len(X))
    centroides = [X[primer_indice].copy()]

    for _ in range(1, k):
        centros = np.array(centroides)

        distancias = np.min(
            np.sum(
                (X[:, None, :] - centros[None, :, :]) ** 2,
                axis=2
            ),
            axis=1
        )

        probabilidades = distancias / distancias.sum()

        nuevo_indice = rng.choice(
            len(X),
            p=probabilidades
        )

        centroides.append(X[nuevo_indice].copy())

    return np.array(centroides)


def kmeans_manual(
    X,
    k,
    metodo="aleatoria",
    seed=10,
    tol=1e-4,
    max_iter=100
):
    if metodo == "aleatoria":
        centroides = inicializacion_aleatoria(X, k, seed)
    else:
        centroides = inicializacion_kmeans_plus_plus(X, k, seed)

    historial_inercia = []

    for _ in range(max_iter):
        etiquetas, inercia = asignar_clusters(X, centroides)
        historial_inercia.append(inercia)

        nuevos_centroides = np.array([
            X[etiquetas == j].mean(axis=0)
            if np.any(etiquetas == j)
            else centroides[j]
            for j in range(k)
        ])

        cambio = np.max(
            np.linalg.norm(
                nuevos_centroides - centroides,
                axis=1
            )
        )

        centroides = nuevos_centroides

        if cambio < tol:
            break

    etiquetas, inercia = asignar_clusters(X, centroides)

    return {
        "centroides": centroides,
        "etiquetas": etiquetas,
        "inercia": inercia,
        "historial_inercia": historial_inercia,
        "metodo": metodo,
        "seed": seed
    }


resultados_kmeans = []

for metodo in ["aleatoria", "kmeans++"]:
    for seed in [10, 20, 30]:
        resultado = kmeans_manual(
            X,
            k=4,
            metodo=metodo,
            seed=seed
        )
        resultados_kmeans.append(resultado)

mejor_kmeans = min(
    resultados_kmeans,
    key=lambda r: r["inercia"]
)

print("Mejor caso de K-Means")
print("Método:", mejor_kmeans["metodo"])
print("Seed:", mejor_kmeans["seed"])
print("Inercia:", mejor_kmeans["inercia"])

# # Selección del mejor caso de ISODATA
#
# Se ejecutan los dos casos solicitados en el Ejercicio 2:
#
# - `Kinit=6`
# - `Kinit=3`
#
# Se selecciona como mejor caso el de menor inercia final.

def cambio_centroides(centroides_anteriores, centroides_nuevos):
    if len(centroides_anteriores) != len(centroides_nuevos):
        return np.inf

    distancias = np.linalg.norm(
        centroides_anteriores[:, None, :] -
        centroides_nuevos[None, :, :],
        axis=2
    )

    return np.max(np.min(distancias, axis=1))


def fusionar_centroides(centroides, etiquetas, dmin, theta_c):
    pares = []

    for i in range(len(centroides)):
        for j in range(i + 1, len(centroides)):
            distancia = np.linalg.norm(
                centroides[i] - centroides[j]
            )
            pares.append((distancia, i, j))

    pares.sort(key=lambda x: x[0])

    fusionados = set()
    nuevos = []
    fusiones = 0

    for distancia, i, j in pares:
        if fusiones >= theta_c:
            break

        if distancia < dmin and i not in fusionados and j not in fusionados:
            ni = np.sum(etiquetas == i)
            nj = np.sum(etiquetas == j)

            if ni + nj > 0:
                centro = (
                    ni * centroides[i] +
                    nj * centroides[j]
                ) / (ni + nj)
            else:
                centro = (centroides[i] + centroides[j]) / 2

            nuevos.append(centro)
            fusionados.update([i, j])
            fusiones += 1

    for i in range(len(centroides)):
        if i not in fusionados:
            nuevos.append(centroides[i])

    return np.array(nuevos)


def isodata(
    X,
    kinit,
    Nmin=10,
    sigma_max=2.0,
    dmin=3.5,
    theta_c=2,
    kmax=6,
    tol=1e-3,
    max_iter=30,
    seed=20
):
    rng = np.random.default_rng(seed)

    indices = rng.choice(
        len(X),
        size=kinit,
        replace=False
    )

    centroides = X[indices].copy()
    historial_inercia = []

    for _ in range(max_iter):

        centroides_anteriores = centroides.copy()

        etiquetas, _ = asignar_clusters(X, centroides)

        conteos = np.bincount(
            etiquetas,
            minlength=len(centroides)
        )

        mantener = conteos >= Nmin

        if not np.all(mantener):
            mapa = -np.ones(len(centroides), dtype=int)
            mapa[mantener] = np.arange(np.sum(mantener))

            etiquetas_nuevas = mapa[etiquetas]
            validos = etiquetas_nuevas >= 0

            X_temp = X[validos]
            etiquetas_temp = etiquetas_nuevas[validos]

            centroides = centroides[mantener]
            etiquetas = etiquetas_temp
        else:
            X_temp = X

        centroides = np.array([
            X_temp[etiquetas == j].mean(axis=0)
            if np.any(etiquetas == j)
            else centroides[j]
            for j in range(len(centroides))
        ])

        # División
        if len(centroides) < kmax:
            candidatos = []

            for j in range(len(centroides)):
                puntos = X_temp[etiquetas == j]

                if len(puntos) >= 2:
                    sigmas = np.std(puntos, axis=0)
                    dimension = np.argmax(sigmas)

                    if sigmas[dimension] > sigma_max:
                        candidatos.append(
                            (j, dimension, sigmas[dimension])
                        )

            nuevos = []

            for j, centro in enumerate(centroides):
                candidato = next(
                    (c for c in candidatos if c[0] == j),
                    None
                )

                if candidato is not None and len(centroides) + len(nuevos) < kmax:
                    _, dimension, sigma = candidato

                    delta = np.zeros(X.shape[1])
                    delta[dimension] = 0.5 * sigma

                    nuevos.extend([
                        centro + delta,
                        centro - delta
                    ])
                else:
                    nuevos.append(centro)

            centroides = np.array(nuevos)

        etiquetas, _ = asignar_clusters(X, centroides)

        # Fusión
        centroides = fusionar_centroides(
            centroides,
            etiquetas,
            dmin,
            theta_c
        )

        etiquetas, inercia = asignar_clusters(X, centroides)
        historial_inercia.append(inercia)

        cambio = cambio_centroides(
            centroides_anteriores,
            centroides
        )

        if cambio < tol:
            break

    return {
        "centroides": centroides,
        "etiquetas": etiquetas,
        "inercia": historial_inercia[-1],
        "historial_inercia": historial_inercia,
        "kinit": kinit
    }


resultado_iso6 = isodata(X, kinit=6)
resultado_iso3 = isodata(X, kinit=3)

mejor_isodata = min(
    [resultado_iso6, resultado_iso3],
    key=lambda r: r["inercia"]
)

print("Mejor caso de ISODATA")
print("Kinit:", mejor_isodata["kinit"])
print("Clusters finales:", len(mejor_isodata["centroides"]))
print("Inercia:", mejor_isodata["inercia"])

# # Métricas de evaluación
#
# Se calculan las tres métricas solicitadas en el enunciado.
#
# ### 1. Coeficiente de Silhouette
#
# Mide qué tan similares son los elementos dentro de su propio cluster frente a los elementos de otros clusters. Un valor mayor indica una mejor separación y cohesión.
#
# ### 2. Índice Davies-Bouldin (DBI)
#
# Relaciona la dispersión interna de los clusters con la separación entre ellos. En esta métrica, valores menores indican una mejor separación relativa.
#
# ### 3. Adjusted Rand Index (ARI)
#
# Compara las etiquetas obtenidas por el algoritmo con las clases reales `y_true`. Un valor cercano a 1 indica una alta correspondencia entre ambas particiones.

def calcular_metricas(X, etiquetas, y_true):
    return {
        "Silhouette": silhouette_score(X, etiquetas),
        "Davies-Bouldin": davies_bouldin_score(X, etiquetas),
        "ARI": adjusted_rand_score(y_true, etiquetas)
    }


metricas_kmeans = calcular_metricas(
    X,
    mejor_kmeans["etiquetas"],
    y_true
)

metricas_isodata = calcular_metricas(
    X,
    mejor_isodata["etiquetas"],
    y_true
)

print("Métricas - K-Means")
for nombre, valor in metricas_kmeans.items():
    print(f"{nombre}: {valor:.4f}")

print("\nMétricas - ISODATA")
for nombre, valor in metricas_isodata.items():
    print(f"{nombre}: {valor:.4f}")

# # Tabla comparativa
#
# Se presentan los resultados de las tres métricas solicitadas junto con la inercia final y el número de clusters obtenido.

import pandas as pd

tabla = pd.DataFrame({
    "Algoritmo": ["K-Means", "ISODATA"],
    "Inercia final": [
        mejor_kmeans["inercia"],
        mejor_isodata["inercia"]
    ],
    "Clusters finales": [
        len(mejor_kmeans["centroides"]),
        len(mejor_isodata["centroides"])
    ],
    "Silhouette": [
        metricas_kmeans["Silhouette"],
        metricas_isodata["Silhouette"]
    ],
    "Davies-Bouldin": [
        metricas_kmeans["Davies-Bouldin"],
        metricas_isodata["Davies-Bouldin"]
    ],
    "ARI": [
        metricas_kmeans["ARI"],
        metricas_isodata["ARI"]
    ]
})

tabla

# # Análisis comparativo
#
# Para interpretar la tabla se deben considerar conjuntamente las tres métricas:
#
# - **Silhouette:** valores mayores son preferibles.
# - **Davies-Bouldin:** valores menores son preferibles.
# - **ARI:** valores mayores indican mayor coincidencia con las clases reales.
#
# La conclusión debe basarse en los valores obtenidos y no únicamente en una sola métrica. Si un algoritmo presenta una ventaja en una métrica y el otro en otra, se debe describir esa diferencia en lugar de considerar una sola medida de forma aislada.

print("Conclusión basada en las métricas obtenidas:")

if (
    metricas_kmeans["Silhouette"] > metricas_isodata["Silhouette"]
    and metricas_kmeans["Davies-Bouldin"] < metricas_isodata["Davies-Bouldin"]
    and metricas_kmeans["ARI"] > metricas_isodata["ARI"]
):
    print(
        "En este conjunto de datos, K-Means obtiene mejores valores "
        "en las tres métricas evaluadas."
    )
elif (
    metricas_isodata["Silhouette"] > metricas_kmeans["Silhouette"]
    and metricas_isodata["Davies-Bouldin"] < metricas_kmeans["Davies-Bouldin"]
    and metricas_isodata["ARI"] > metricas_kmeans["ARI"]
):
    print(
        "En este conjunto de datos, ISODATA obtiene mejores valores "
        "en las tres métricas evaluadas."
    )
elif (
    metricas_kmeans["Silhouette"] == metricas_isodata["Silhouette"]
    and metricas_kmeans["Davies-Bouldin"] == metricas_isodata["Davies-Bouldin"]
    and metricas_kmeans["ARI"] == metricas_isodata["ARI"]
):
    print(
        "Ambos algoritmos obtuvieron métricas idénticas: convergieron "
        "a la misma partición de clusters."
    )
else:
    print(
        "Los resultados son mixtos: las métricas no favorecen "
        "al mismo algoritmo en todos los criterios. La comparación "
        "debe explicar qué ventaja presenta cada algoritmo."
    )

