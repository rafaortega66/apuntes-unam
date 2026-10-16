"""
Ejercicio 1: Implementacion de K-Means
Practica 2 - Reconocimiento de Patrones
Rafael Ortega de la Paz (420054085) y Sebastian Andre Fuentes Poma (620271005)
"""

# # Práctica 2 – Ejercicio 1: Implementación de K-Means
#
# En este notebook se desarrolla exactamente el **Ejercicio 1** de la práctica.
#
# Se utilizará el dataset sintético indicado en el enunciado: **400 ejemplos, 2 características y 4 clases**.

# ## 2. Desarrollo – Generación de datos sintéticos
#
# Primero generamos los datos exactamente con el código proporcionado en la práctica.
#
# `make_blobs` genera 400 ejemplos distribuidos en 4 grupos, con una desviación estándar de 1.7 y `random_state=20`.

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y_true = make_blobs(
    n_samples=400,
    centers=4,
    cluster_std=1.7,
    random_state=20
)

plt.figure(figsize=(7, 5))
plt.scatter(X[:, 0], X[:, 1], c=y_true)
plt.title("Datos sintéticos")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

print("Número de ejemplos:", X.shape[0])
print("Número de características:", X.shape[1])
print("Número de clases:", len(set(y_true)))

# ## 2.1.1. Implementación K-Means
#
# Se implementará K-Means manualmente, considerando las condiciones solicitadas:
#
# - **Inicialización aleatoria:** se seleccionan `K` puntos al azar del dataset.
# - **K-Means++:** el primer centroide es aleatorio y los siguientes se seleccionan con probabilidad proporcional a la distancia al centroide más cercano.
# - **Convergencia:** se detiene cuando el cambio de los centroides es menor que una tolerancia.
# - **Inercia:** se guarda la inercia de cada iteración.

import numpy as np

def inicializacion_aleatoria(X, k, seed=None):
    # Seleccionar K puntos al azar del dataset
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(X), size=k, replace=False)
    return X[indices].copy()


def inicializacion_kmeans_plus_plus(X, k, seed=None):
    # Primer centroide aleatorio
    rng = np.random.default_rng(seed)

    primer_indice = rng.integers(len(X))
    centroides = [X[primer_indice].copy()]

    # Seleccionar los siguientes centroides
    for _ in range(1, k):

        centros = np.array(centroides)

        # Distancia cuadrática al centroide más cercano
        distancias = np.min(
            np.sum(
                (X[:, None, :] - centros[None, :, :]) ** 2,
                axis=2
            ),
            axis=1
        )

        # Probabilidad proporcional a la distancia cuadrática
        probabilidades = distancias / distancias.sum()

        nuevo_indice = rng.choice(
            len(X),
            p=probabilidades
        )

        centroides.append(X[nuevo_indice].copy())

    return np.array(centroides)


def kmeans(
    X,
    k,
    inicializacion="random",
    seed=None,
    max_iter=100,
    tol=1e-4
):

# 1. Inicialización
    if inicializacion == "random":
        centroides = inicializacion_aleatoria(
            X, k, seed
        )

    elif inicializacion == "kmeans++":
        centroides = inicializacion_kmeans_plus_plus(
            X, k, seed
        )

    else:
        raise ValueError(
            "La inicialización debe ser 'random' o 'kmeans++'"
        )

    historial_centroides = [centroides.copy()]
    historial_inercia = []

# 2. Iteraciones de K-Means
    for iteracion in range(max_iter):

        # Asignar cada punto al centroide más cercano
        distancias = np.sum(
            (X[:, None, :] - centroides[None, :, :]) ** 2,
            axis=2
        )

        etiquetas = np.argmin(
            distancias,
            axis=1
        )

        # Calcular nuevos centroides
        nuevos_centroides = centroides.copy()

        for j in range(k):

            puntos = X[etiquetas == j]

            # Si el cluster no está vacío
            if len(puntos) > 0:
                nuevos_centroides[j] = np.mean(
                    puntos,
                    axis=0
                )

   # 3. Calcular y guardar la inercia
        inercia = np.sum(
            (X - nuevos_centroides[etiquetas]) ** 2
        )

        historial_inercia.append(inercia)

        # Guardar centroides
        historial_centroides.append(
            nuevos_centroides.copy()
        )


    # 4. Criterio de convergencia
        cambio = np.max(
            np.linalg.norm(
                nuevos_centroides - centroides,
                axis=1
            )
        )

        centroides = nuevos_centroides

        if cambio < tol:
            break

    # Asignación final
    distancias = np.sum(
        (X[:, None, :] - centroides[None, :, :]) ** 2,
        axis=2
    )

    etiquetas = np.argmin(
        distancias,
        axis=1
    )

    return {
        "labels": etiquetas,
        "centroids": centroides,
        "centroid_history": historial_centroides,
        "inertia_history": historial_inercia,
        "iterations": len(historial_inercia)
    }

print("Función K-Means implementada correctamente.")

# ## 2.1.2.a. Ejecutar K-Means 6 veces
#
# La práctica solicita utilizar `k=4` y realizar:
#
# - 3 corridas con **inicialización aleatoria**.
# - 3 corridas con **K-Means++**.
#
# Se utilizarán las semillas `10`, `20` y `30` para cada método.

k = 4

resultados = []

# 3 corridas con inicialización aleatoria

for seed in [10, 20, 30]:

    resultado = kmeans(
        X,
        k=k,
        inicializacion="random",
        seed=seed
    )

    resultado["metodo"] = "Aleatoria"
    resultado["seed"] = seed

    resultados.append(resultado)


# 3 corridas con K-Means++

for seed in [10, 20, 30]:

    resultado = kmeans(
        X,
        k=k,
        inicializacion="kmeans++",
        seed=seed
    )

    resultado["metodo"] = "K-Means++"
    resultado["seed"] = seed

    resultados.append(resultado)


print("Número total de corridas:", len(resultados))

for i, r in enumerate(resultados, start=1):
    print(
        f"Corrida {i}: "
        f"{r['metodo']} | "
        f"seed={r['seed']} | "
        f"iteraciones={r['iterations']} | "
        f"inercia={r['inertia_history'][-1]:.4f}"
    )

# ## 2.1.2.b. Asignación de clusters y centroides finales
#
# Para cada una de las 6 corridas se muestra:
#
# - La asignación de los 400 puntos a sus clusters.
# - Los 4 centroides finales marcados con una `X`.

fig, axes = plt.subplots(
    2, 3,
    figsize=(15, 9)
)

for ax, resultado in zip(
    axes.ravel(),
    resultados
):

    ax.scatter(
        X[:, 0],
        X[:, 1],
        c=resultado["labels"],
        cmap="viridis",
        s=25
    )

    ax.scatter(
        resultado["centroids"][:, 0],
        resultado["centroids"][:, 1],
        marker="X",
        s=180,
        edgecolor="black",
        linewidth=1.5
    )

    ax.set_title(
        f"{resultado['metodo']} | "
        f"seed={resultado['seed']}"
    )

    ax.set_xlabel("Característica 1")
    ax.set_ylabel("Característica 2")

plt.suptitle(
    "Asignación de clusters y centroides finales",
    fontsize=16
)

plt.tight_layout()
plt.show()

# ## 2.1.2.c. Curva de inercia vs. número de iteración
#
# Se grafica el historial de inercia almacenado durante cada corrida.

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

fig, axes = plt.subplots(
    2, 3,
    figsize=(15, 8)
)

for ax, resultado in zip(
    axes.ravel(),
    resultados
):

    iteraciones = range(
        1,
        len(resultado["inertia_history"]) + 1
    )

    ax.plot(
        iteraciones,
        resultado["inertia_history"],
        marker="o"
    )

    ax.set_title(
        f"{resultado['metodo']} | "
        f"seed={resultado['seed']}"
    )

    ax.set_xlabel("Iteración")
    ax.set_ylabel("Inercia")

    # Solo enteros en el eje X
    ax.xaxis.set_major_locator(
        MaxNLocator(integer=True)
    )

    ax.grid(True)

plt.suptitle(
    "Inercia vs. número de iteración",
    fontsize=16
)

plt.tight_layout()
plt.show()

# ## 2.1.2.d. Inercia final promedio, mínima y máxima
#
# Se calcula la inercia final de cada una de las 6 corridas y posteriormente se obtiene:
#
# - Inercia final promedio.
# - Inercia final mínima.
# - Inercia final máxima.

inercias_finales = np.array([
    resultado["inertia_history"][-1]
    for resultado in resultados
])

print("INERCIAS FINALES DE LAS 6 CORRIDAS")
print("=" * 45)

for i, (resultado, inercia) in enumerate(
    zip(resultados, inercias_finales),
    start=1
):

    print(
        f"{i}. {resultado['metodo']:12s} "
        f"seed={resultado['seed']} -> "
        f"{inercia:.4f}"
    )

print("\nRESUMEN")
print("=" * 45)

print(
    f"Inercia final promedio: "
    f"{np.mean(inercias_finales):.4f}"
)

print(
    f"Inercia final mínima:   "
    f"{np.min(inercias_finales):.4f}"
)

print(
    f"Inercia final máxima:   "
    f"{np.max(inercias_finales):.4f}"
)

# ## Comparación de la inercia según la inicialización
#
# También podemos observar por separado las tres corridas de cada método para identificar cuánto varió la inercia final.

for metodo in ["Aleatoria", "K-Means++"]:

    valores = [
        r["inertia_history"][-1]
        for r in resultados
        if r["metodo"] == metodo
    ]

    print(f"\n{metodo}")
    print("-" * 30)
    print(f"Promedio: {np.mean(valores):.4f}")
    print(f"Mínima:   {np.min(valores):.4f}")
    print(f"Máxima:   {np.max(valores):.4f}")

# ## 2.1.2.e. Observaciones
#
# Esta celda genera automáticamente un resumen numérico para apoyar la respuesta del inciso (e).
#
# La interpretación debe centrarse en:
#
# 1. Si las corridas terminaron con valores de inercia similares o diferentes.
# 2. Cuánto cambió la inercia según la semilla.
# 3. Comparar la variación obtenida con inicialización aleatoria frente a K-Means++.
# 4. Observar si los centroides finales quedan en posiciones similares.
#
# **Nota:** la conclusión se basa en los resultados que produzca la ejecución del notebook.

for metodo in ["Aleatoria", "K-Means++"]:

    corridas_metodo = [
        r for r in resultados
        if r["metodo"] == metodo
    ]

    valores = np.array([
        r["inertia_history"][-1]
        for r in corridas_metodo
    ])

    print(
        f"{metodo}: "
        f"mín={valores.min():.4f}, "
        f"máx={valores.max():.4f}, "
        f"promedio={valores.mean():.4f}, "
        f"rango={valores.max()-valores.min():.4f}"
    )

print("\nObservación:")
print(
    "Compara el rango de inercia de ambos métodos y las "
    "posiciones de los centroides en las gráficas anteriores."
)

