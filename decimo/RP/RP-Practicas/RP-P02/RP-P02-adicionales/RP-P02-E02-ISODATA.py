"""
Ejercicio 2: Implementacion de ISODATA
Practica 2 - Reconocimiento de Patrones
Rafael Ortega de la Paz (420054085) y Sebastian Andre Fuentes Poma (620271005)
"""

# # Práctica 2 — Ejercicio 2: Implementación ISODATA
#
# En este ejercicio se implementa manualmente el algoritmo **ISODATA**, siguiendo las condiciones indicadas en el enunciado.
#
# Se utilizarán **los mismos datos del Ejercicio 1**:
# - 400 ejemplos.
# - 2 características.
# - 4 clases.
# - `random_state=20`.

# ## Datos sintéticos
#
# Se genera exactamente el mismo conjunto de datos utilizado en el Ejercicio 1.

from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt

X, y_true = make_blobs(
    n_samples=400,
    centers=4,
    cluster_std=1.7,
    random_state=20
)

plt.figure(figsize=(7, 5))
plt.scatter(X[:, 0], X[:, 1], c=y_true, cmap="viridis", s=30)
plt.title("Datos sintéticos del Ejercicio 1")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# # 2.2.1. Implementación ISODATA
#
# ### a) Eliminación de clusters
#
# En cada iteración se eliminan los clusters que contienen menos de `Nmin` puntos.
#
# ### b) División
#
# Para cada cluster se calcula la desviación estándar de cada dimensión y se selecciona la mayor. Se divide el cluster si:
#
# - `σk > σmax`
# - y el número actual de clusters es menor que `kmax`.
#
# ### c) Fusión
#
# Se calculan las distancias entre centroides y se fusionan pares que cumplen:
#
# - `d(mi, mj) < dmin`
# - y el número de fusiones realizadas en la iteración es menor que `θc`.
#
# ### d) Convergencia
#
# Se utiliza el cambio máximo entre centroides como criterio de convergencia.
#
# ### e) Historial de inercia
#
# Se guarda la inercia al final de cada iteración.

def asignar_clusters(X, centroides):
    distancias = np.sum(
        (X[:, None, :] - centroides[None, :, :]) ** 2,
        axis=2
    )
    etiquetas = np.argmin(distancias, axis=1)
    inercia = np.sum(np.min(distancias, axis=1))
    return etiquetas, inercia


def cambio_centroides(centroides_anteriores, centroides_nuevos):
    # Si cambia el número de clusters, todavía no puede considerarse
    # convergencia por cambio de centroides.
    if len(centroides_anteriores) != len(centroides_nuevos):
        return np.inf

    # Se compara cada centro anterior con el centro nuevo más cercano.
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
            distancia = np.linalg.norm(centroides[i] - centroides[j])
            pares.append((distancia, i, j))

    pares.sort(key=lambda x: x[0])

    fusionados = set()
    nuevos_centroides = []
    numero_fusiones = 0

    for distancia, i, j in pares:
        if numero_fusiones >= theta_c:
            break

        if distancia < dmin and i not in fusionados and j not in fusionados:
            puntos_i = np.sum(etiquetas == i)
            puntos_j = np.sum(etiquetas == j)

            if puntos_i + puntos_j > 0:
                nuevo = (
                    puntos_i * centroides[i] +
                    puntos_j * centroides[j]
                ) / (puntos_i + puntos_j)
            else:
                nuevo = (centroides[i] + centroides[j]) / 2

            nuevos_centroides.append(nuevo)
            fusionados.add(i)
            fusionados.add(j)
            numero_fusiones += 1

    for i in range(len(centroides)):
        if i not in fusionados:
            nuevos_centroides.append(centroides[i])

    return np.array(nuevos_centroides), numero_fusiones


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

    # Inicialización: seleccionar Kinit puntos aleatorios del dataset.
    indices = rng.choice(len(X), size=kinit, replace=False)
    centroides = X[indices].copy()

    historial_inercia = []
    historial_clusters = [len(centroides)]

    for iteracion in range(max_iter):

        centroides_anteriores = centroides.copy()

        # 1. Asignación inicial
        etiquetas, _ = asignar_clusters(X, centroides)

        # 2. Eliminar clusters con menos de Nmin puntos
        conteos = np.bincount(
            etiquetas,
            minlength=len(centroides)
        )

        mantener = conteos >= Nmin

        if not np.all(mantener):
            mapa = -np.ones(len(centroides), dtype=int)
            mapa[mantener] = np.arange(np.sum(mantener))

            etiquetas_filtradas = mapa[etiquetas]
            validos = etiquetas_filtradas >= 0

            X_filtrado = X[validos]
            etiquetas_filtradas = etiquetas_filtradas[validos]

            centroides = centroides[mantener]
            etiquetas = etiquetas_filtradas
        else:
            X_filtrado = X

        # Recalcular centroides después de eliminar clusters
        nuevos = []
        for j in range(len(centroides)):
            puntos = X_filtrado[etiquetas == j]

            if len(puntos) > 0:
                nuevos.append(np.mean(puntos, axis=0))
            else:
                nuevos.append(centroides[j])

        centroides = np.array(nuevos)

        # 3. División de clusters
        if len(centroides) < kmax:
            candidatos_division = []

            for j in range(len(centroides)):
                puntos = X_filtrado[etiquetas == j]

                if len(puntos) >= 2:
                    desviaciones = np.std(puntos, axis=0)
                    dimension = np.argmax(desviaciones)
                    sigma_k = desviaciones[dimension]

                    if sigma_k > sigma_max:
                        candidatos_division.append(
                            (j, dimension, sigma_k)
                        )

            nuevos = []

            for j, centro in enumerate(centroides):
                candidato = next(
                    (c for c in candidatos_division if c[0] == j),
                    None
                )

                if candidato is not None and len(centroides) + len(nuevos) < kmax:
                    _, dimension, sigma_k = candidato

                    delta = np.zeros(X.shape[1])
                    delta[dimension] = 0.5 * sigma_k

                    nuevos.append(centro + delta)
                    nuevos.append(centro - delta)
                else:
                    nuevos.append(centro)

            centroides = np.array(nuevos)

        # Reasignar después de las divisiones
        etiquetas, _ = asignar_clusters(X, centroides)

        # 4. Fusión de clusters
        centroides, numero_fusiones = fusionar_centroides(
            centroides,
            etiquetas,
            dmin,
            theta_c
        )
        # Guardar cuántos clusters quedaron
        historial_clusters.append(len(centroides))

        # Reasignar después de las fusiones
        etiquetas, inercia = asignar_clusters(X, centroides)

        historial_inercia.append(inercia)

        # 5. Convergencia basada en cambio de centroides
        cambio = cambio_centroides(
            centroides_anteriores,
            centroides
        )

        if cambio < tol:
            break

    return {
        "centroides": centroides,
        "etiquetas": etiquetas,
        "historial_inercia": historial_inercia,
        "historial_clusters": historial_clusters,
        "iteraciones": len(historial_inercia)
    }

# ## Parámetros utilizados
#
# Se fijan los siguientes parámetros para poder observar tanto divisiones como fusiones:
#
# - `Nmin = 10`
# - `sigma_max = 2.0`
# - `dmin = 3.5`
# - `theta_c = 2`
# - `kmax = 6`
# - `tol = 1e-3`
#
# Estos valores se mantienen iguales en las dos ejecuciones solicitadas, cambiando únicamente `Kinit`.

PARAMETROS_ISODATA = {
    "Nmin": 10,
    "sigma_max": 2.0,
    "dmin": 3.5,
    "theta_c": 2,
    "kmax": 6,
    "tol": 1e-3,
    "max_iter": 30,
    "seed": 20
}

# # 2.2.2 a) Aplicar ISODATA con Kinit = 6 y Kinit = 3
#
# Se ejecuta ISODATA dos veces utilizando exactamente los mismos datos.

resultado_k6 = isodata(
    X,
    kinit=6,
    **PARAMETROS_ISODATA
)

resultado_k3 = isodata(
    X,
    kinit=3,
    **PARAMETROS_ISODATA
)

print("ISODATA con Kinit=6")
print("Clusters finales:", len(resultado_k6["centroides"]))
print("Iteraciones:", resultado_k6["iteraciones"])
print("Inercia final:", resultado_k6["historial_inercia"][-1])

print("\nISODATA con Kinit=3")
print("Clusters finales:", len(resultado_k3["centroides"]))
print("Iteraciones:", resultado_k3["iteraciones"])
print("Inercia final:", resultado_k3["historial_inercia"][-1])

# ## 2.2.2 b) Verificar el número de clusters
#
# El dataset fue generado con 4 grupos. Por ello, se verifica si ISODATA termina con 4 clusters en ambos casos.

print("Kinit=6 -> clusters finales:", len(resultado_k6["centroides"]))
print("Kinit=3 -> clusters finales:", len(resultado_k3["centroides"]))
print("Número esperado de clusters: 4")

# ## 2.2.2 c) Evolución del número de clusters
#
# Se grafica el número de clusters obtenido en cada iteración para las dos inicializaciones.

from matplotlib.ticker import MaxNLocator

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Kinit = 6
axes[0].plot(
    range(len(resultado_k6["historial_clusters"])),
    resultado_k6["historial_clusters"],
    marker="o"
)

axes[0].axhline(4, linestyle="--", label="Número esperado = 4")
axes[0].set_title("ISODATA - Kinit=6")
axes[0].set_xlabel("Iteración")
axes[0].set_ylabel("Número de clusters")

# Enteros en ambos ejes
axes[0].xaxis.set_major_locator(MaxNLocator(integer=True))
axes[0].yaxis.set_major_locator(MaxNLocator(integer=True))

axes[0].legend()


# Kinit = 3
axes[1].plot(
    range(len(resultado_k3["historial_clusters"])),
    resultado_k3["historial_clusters"],
    marker="o"
)

axes[1].axhline(4, linestyle="--", label="Número esperado = 4")
axes[1].set_title("ISODATA - Kinit=3")
axes[1].set_xlabel("Iteración")
axes[1].set_ylabel("Número de clusters")

# Enteros en ambos ejes
axes[1].xaxis.set_major_locator(MaxNLocator(integer=True))
axes[1].yaxis.set_major_locator(MaxNLocator(integer=True))

axes[1].legend()

plt.tight_layout()
plt.show()

# ## Inercia por iteración
#
# Aunque el inciso c) solicita específicamente la evolución del número de clusters, también se conserva el historial de inercia solicitado en 2.2.1.

plt.figure(figsize=(8, 5))

plt.plot(
    resultado_k6["historial_inercia"],
    marker="o",
    label="Kinit=6"
)

plt.plot(
    resultado_k3["historial_inercia"],
    marker="o",
    label="Kinit=3"
)

plt.xlabel("Iteración")
plt.ylabel("Inercia")
plt.title("ISODATA: inercia por iteración")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# ## Visualización de los clusters finales

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, resultado, titulo in [
    (axes[0], resultado_k6, "ISODATA - Kinit=6"),
    (axes[1], resultado_k3, "ISODATA - Kinit=3")
]:
    ax.scatter(
        X[:, 0],
        X[:, 1],
        c=resultado["etiquetas"],
        cmap="viridis",
        s=30
    )

    ax.scatter(
        resultado["centroides"][:, 0],
        resultado["centroides"][:, 1],
        marker="X",
        s=180,
        c="red",
        edgecolors="black",
        label="Centroides"
    )

    ax.set_title(titulo)
    ax.set_xlabel("Característica 1")
    ax.set_ylabel("Característica 2")
    ax.legend()

plt.tight_layout()
plt.show()

# # 2.2.2 d) Comparación con K-Means
#
# Para realizar la comparación se ejecuta K-Means con `k=4`, utilizando la misma información del Ejercicio 1.
#
# Se comparan:
# - número de clusters;
# - centroides finales;
# - inercia final.

# K-Means manual para la comparación

def kmeans_manual(X, k, seed=10, tol=1e-4, max_iter=100):
    rng = np.random.default_rng(seed)
    centroides = X[rng.choice(len(X), size=k, replace=False)].copy()
    historial = []

    for _ in range(max_iter):
        etiquetas, inercia = asignar_clusters(X, centroides)
        historial.append(inercia)

        nuevos = np.array([
            X[etiquetas == j].mean(axis=0)
            if np.any(etiquetas == j)
            else centroides[j]
            for j in range(k)
        ])

        cambio = np.max(
            np.linalg.norm(nuevos - centroides, axis=1)
        )

        centroides = nuevos

        if cambio < tol:
            break

    etiquetas, inercia = asignar_clusters(X, centroides)

    return {
        "centroides": centroides,
        "etiquetas": etiquetas,
        "historial_inercia": historial,
        "inercia_final": inercia
    }


resultado_kmeans = kmeans_manual(X, k=4, seed=10)

print("K-Means")
print("Clusters:", len(resultado_kmeans["centroides"]))
print("Inercia final:", resultado_kmeans["inercia_final"])
print("Centroides finales:")
print(resultado_kmeans["centroides"])

print("\nISODATA Kinit=6")
print("Inercia final:", resultado_k6["historial_inercia"][-1])
print(resultado_k6["centroides"])

print("\nISODATA Kinit=3")
print("Inercia final:", resultado_k3["historial_inercia"][-1])
print(resultado_k3["centroides"])

# ### Comparación final
#
# La comparación permite observar cómo ISODATA puede modificar automáticamente el número de clusters mediante las operaciones de eliminación, división y fusión, mientras que K-Means mantiene fijo `k=4`.
#
# En este conjunto de datos, se verifica si las dos inicializaciones de ISODATA terminan con el número esperado de grupos y qué tan cerca queda su inercia de la obtenida por K-Means.

