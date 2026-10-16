"""
Ejercicio 4: Dataset Wine con PCA
Practica 2 - Reconocimiento de Patrones
Rafael Ortega de la Paz (420054085) y Sebastian Andre Fuentes Poma (620271005)
"""

# # Práctica 2 — Wine: reducción dimensional con PCA
#
# Camino alternativo: estandarizar las 13 variables y aplicar PCA, conservando el mínimo número de componentes que explique al menos 95 % de la varianza. Después se aplican K-Means e ISODATA.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score, adjusted_rand_score

# --- Funciones manuales de K-Means (idénticas al Ejercicio 1) ---

def inicializacion_aleatoria(X, k, seed=None):
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(X), size=k, replace=False)
    return X[indices].copy()


def inicializacion_kmeans_plus_plus(X, k, seed=None):
    rng = np.random.default_rng(seed)
    primer_indice = rng.integers(len(X))
    centroides = [X[primer_indice].copy()]
    for _ in range(1, k):
        centros = np.array(centroides)
        distancias = np.min(
            np.sum((X[:, None, :] - centros[None, :, :]) ** 2, axis=2),
            axis=1
        )
        probabilidades = distancias / distancias.sum()
        nuevo_indice = rng.choice(len(X), p=probabilidades)
        centroides.append(X[nuevo_indice].copy())
    return np.array(centroides)


def kmeans(X, k, inicializacion="random", seed=None, max_iter=100, tol=1e-4):
    if inicializacion == "random":
        centroides = inicializacion_aleatoria(X, k, seed)
    elif inicializacion == "kmeans++":
        centroides = inicializacion_kmeans_plus_plus(X, k, seed)
    else:
        raise ValueError("La inicialización debe ser 'random' o 'kmeans++'")

    historial_inercia = []

    for iteracion in range(max_iter):
        distancias = np.sum((X[:, None, :] - centroides[None, :, :]) ** 2, axis=2)
        etiquetas = np.argmin(distancias, axis=1)

        nuevos_centroides = centroides.copy()
        for j in range(k):
            puntos = X[etiquetas == j]
            if len(puntos) > 0:
                nuevos_centroides[j] = np.mean(puntos, axis=0)

        inercia = np.sum((X - nuevos_centroides[etiquetas]) ** 2)
        historial_inercia.append(inercia)

        cambio = np.max(np.linalg.norm(nuevos_centroides - centroides, axis=1))
        centroides = nuevos_centroides
        if cambio < tol:
            break

    distancias = np.sum((X[:, None, :] - centroides[None, :, :]) ** 2, axis=2)
    etiquetas = np.argmin(distancias, axis=1)

    return {
        "labels": etiquetas,
        "centroids": centroides,
        "inertia_history": historial_inercia,
        "iterations": len(historial_inercia)
    }

print("Función K-Means (manual, Ejercicio 1) cargada correctamente.")

wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y_true = wine.target
scaler = StandardScaler()
X_std = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
print("Datos:", X.shape)
print(X.head())

# ## 1. PCA y varianza explicada

pca_full = PCA()
Z_full = pca_full.fit_transform(X_std)

var = pca_full.explained_variance_ratio_
cum = np.cumsum(var)
print(pd.DataFrame({"Componente":range(1,14),
                      "Varianza":var,
                      "Acumulada":cum}))

plt.figure(figsize=(8,5))
plt.plot(range(1,14), cum, marker="o")
plt.axhline(.95, linestyle="--", label="95%")
plt.xlabel("Componentes"); plt.ylabel("Varianza acumulada")
plt.title("PCA — varianza explicada")
plt.xticks(range(1,14)); plt.grid(); plt.legend(); plt.show()

ncomp = np.argmax(cum >= .95) + 1
pca = PCA(n_components=ncomp)
Z = pca.fit_transform(X_std)
print("Componentes conservadas:", ncomp)
print("Varianza acumulada:", pca.explained_variance_ratio_.sum())

# ## 2. Cargas de las componentes

print(pd.DataFrame(
    pca.components_.T,
    index=X.columns,
    columns=[f"PC{i+1}" for i in range(ncomp)]
))

# ## 3. K-Means en el espacio PCA

km = kmeans(Z, k=3, inicializacion="kmeans++", seed=20)
lab_km = km["labels"]
print("Inercia:", km["inertia_history"][-1])
print("Silhouette:", silhouette_score(Z, lab_km))
print("Davies-Bouldin:", davies_bouldin_score(Z, lab_km))
print("ARI:", adjusted_rand_score(y_true, lab_km))

# ## 4. ISODATA en el espacio PCA

# --- Funciones manuales de ISODATA (idénticas al Ejercicio 2) ---

def asignar_clusters(X, centroides):
    distancias = np.sum((X[:, None, :] - centroides[None, :, :]) ** 2, axis=2)
    etiquetas = np.argmin(distancias, axis=1)
    inercia = np.sum(np.min(distancias, axis=1))
    return etiquetas, inercia


def cambio_centroides(centroides_anteriores, centroides_nuevos):
    if len(centroides_anteriores) != len(centroides_nuevos):
        return np.inf
    distancias = np.linalg.norm(
        centroides_anteriores[:, None, :] - centroides_nuevos[None, :, :],
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
                nuevo = (puntos_i * centroides[i] + puntos_j * centroides[j]) / (puntos_i + puntos_j)
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


def isodata(X, kinit, Nmin=10, sigma_max=2.0, dmin=3.5, theta_c=2, kmax=6, tol=1e-3, max_iter=30, seed=20):
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(X), size=kinit, replace=False)
    centroides = X[indices].copy()

    historial_inercia = []
    historial_clusters = [len(centroides)]

    for iteracion in range(max_iter):
        centroides_anteriores = centroides.copy()

        etiquetas, _ = asignar_clusters(X, centroides)

        conteos = np.bincount(etiquetas, minlength=len(centroides))
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

        nuevos = []
        for j in range(len(centroides)):
            puntos = X_filtrado[etiquetas == j]
            nuevos.append(np.mean(puntos, axis=0) if len(puntos) > 0 else centroides[j])
        centroides = np.array(nuevos)

        if len(centroides) < kmax:
            candidatos_division = []
            for j in range(len(centroides)):
                puntos = X_filtrado[etiquetas == j]
                if len(puntos) >= 2:
                    desviaciones = np.std(puntos, axis=0)
                    dimension = np.argmax(desviaciones)
                    sigma_k = desviaciones[dimension]
                    if sigma_k > sigma_max:
                        candidatos_division.append((j, dimension, sigma_k))

            nuevos = []
            for j, centro in enumerate(centroides):
                candidato = next((c for c in candidatos_division if c[0] == j), None)
                if candidato is not None and len(centroides) + len(nuevos) < kmax:
                    _, dimension, sigma_k = candidato
                    delta = np.zeros(X.shape[1])
                    delta[dimension] = 0.5 * sigma_k
                    nuevos.append(centro + delta)
                    nuevos.append(centro - delta)
                else:
                    nuevos.append(centro)
            centroides = np.array(nuevos)

        etiquetas, _ = asignar_clusters(X, centroides)
        centroides, numero_fusiones = fusionar_centroides(centroides, etiquetas, dmin, theta_c)
        historial_clusters.append(len(centroides))

        etiquetas, inercia = asignar_clusters(X, centroides)
        historial_inercia.append(inercia)

        cambio = cambio_centroides(centroides_anteriores, centroides)
        if cambio < tol:
            break

    return {
        "centroides": centroides,
        "etiquetas": etiquetas,
        "historial_inercia": historial_inercia,
        "historial_clusters": historial_clusters,
        "iteraciones": len(historial_inercia)
    }

print("Función ISODATA (manual, Ejercicio 2) cargada correctamente.")

res = isodata(Z, kinit=5, Nmin=8, sigma_max=1.6, dmin=2.2, theta_c=2, kmax=6, tol=1e-3, seed=20)
lab_iso = res["etiquetas"]
print("Clusters finales:", len(res["centroides"]))
print("Inercia:", res["historial_inercia"][-1])
print("Silhouette:", silhouette_score(Z, lab_iso))
print("Davies-Bouldin:", davies_bouldin_score(Z, lab_iso))
print("ARI:", adjusted_rand_score(y_true, lab_iso))

fig, ax = plt.subplots(1,2,figsize=(12,4))
ax[0].plot(res["historial_inercia"], marker="o"); ax[0].set_title("ISODATA — Inercia")
ax[0].set_xlabel("Iteración"); ax[0].set_ylabel("Inercia"); ax[0].grid()
ax[1].plot(res["historial_clusters"], marker="o"); ax[1].set_title("ISODATA — Número de clusters")
ax[1].set_xlabel("Iteración"); ax[1].set_ylabel("Clusters"); ax[1].grid()
plt.tight_layout(); plt.show()

# ## 5. Visualización PC1–PC2

plt.figure(figsize=(8,6))
plt.scatter(Z[:,0], Z[:,1], c=lab_km, alpha=.75)
plt.xlabel("PC1"); plt.ylabel("PC2")
plt.title("K-Means en el espacio PCA"); plt.grid(); plt.show()

# ## 6. Tabla clase–cluster

def tabla(y, labels):
    return pd.crosstab(pd.Series(labels, name="Cluster"), pd.Series(y, name="Clase"))
print("K-Means"); print(tabla(y_true, lab_km))
print("ISODATA"); print(tabla(y_true, lab_iso))

# ## Conclusión
#
# PCA reduce dimensionalidad y puede aliviar redundancia y problemas asociados a muchas variables, pero los centroides dejan de estar expresados directamente en las 13 características originales. Comparar Silhouette, DBI, ARI e inercia con el enfoque original permite evaluar el efecto de PCA.

