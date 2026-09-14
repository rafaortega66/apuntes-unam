"""
Practica 1 - PCA
Seccion 2.3: Dataset Wine
Autor: Rafael Ortega de la Paz - 420054085
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

OUTDIR = "."


def pca_svd(X, k):
    """
    PCA mediante descomposicion en valores singulares (SVD).

    Parametros
    ----------
    X : ndarray (n_muestras, n_variables)
        Matriz de datos (se centra dentro de la funcion).
    k : int
        Numero de componentes principales a conservar.

    Regresa
    -------
    Z : ndarray (n_muestras, k)
        Datos proyectados sobre las k componentes principales.
    eigvecs_k : ndarray (n_variables, k)
        Los k vectores propios (equivalentes) con mayor varianza (columnas).
    eigvals_k : ndarray (k,)
        Los k valores propios asociados, ordenados de mayor a menor.
    """
    Xc = X - X.mean(axis=0)
    n = Xc.shape[0]
    # Xc = U S V^T ; las columnas de V son los vectores propios de la
    # matriz de covarianza, y los valores propios son s_i^2 / (n-1)
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)

    # SVD ya entrega los valores singulares ordenados de mayor a menor,
    # lo que corresponde a la convencion PC1 = mayor varianza.
    eigvals = (S ** 2) / (n - 1)
    eigvecs = Vt.T

    eigvals_k = eigvals[:k]
    eigvecs_k = eigvecs[:, :k]
    Z = Xc @ eigvecs_k

    return Z, eigvecs_k, eigvals_k


def estandarizar(X):
    """Estandariza cada columna: media 0, desviacion estandar 1."""
    media = X.mean(axis=0)
    std = X.std(axis=0, ddof=0)
    return (X - media) / std


def varianza_y_acumulada(eigvals):
    ve = eigvals / eigvals.sum()
    return ve, np.cumsum(ve)


def graficar_scree(varianza_explicada, varianza_acumulada, titulo, nombre_archivo):
    k = len(varianza_explicada)
    componentes = np.arange(1, k + 1)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    axes[0].bar(componentes, varianza_explicada, color="steelblue")
    axes[0].set_xlabel("Componente principal")
    axes[0].set_ylabel("Proporcion de varianza explicada")
    axes[0].set_title(f"Scree plot - {titulo}")
    axes[0].set_xticks(componentes)
    axes[0].tick_params(axis="x", labelrotation=90)
    axes[0].grid(alpha=0.3)

    axes[1].plot(componentes, varianza_acumulada, marker="o", color="darkorange")
    axes[1].axhline(0.90, color="gray", linestyle="--", linewidth=1, label="90%")
    axes[1].axhline(0.95, color="gray", linestyle=":", linewidth=1, label="95%")
    axes[1].set_xlabel("Numero de componentes")
    axes[1].set_ylabel("Varianza explicada acumulada")
    axes[1].set_title(f"Varianza acumulada - {titulo}")
    axes[1].set_xticks(componentes)
    axes[1].tick_params(axis="x", labelrotation=90)
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/{nombre_archivo}", dpi=300)
    plt.close(fig)
    print(f"Figura guardada: {nombre_archivo}")


if __name__ == "__main__":
    print("=" * 60)
    print("2.3 Dataset Wine")
    print("=" * 60)

    wine = load_wine()
    X = wine.data
    p = X.shape[1]
    print(f"Forma de X: {X.shape} (13 caracteristicas)")

    # 2. Estandarizar
    X_std = estandarizar(X)

    # 3. Aplicar PCA con pca_svd (todas las componentes)
    Z, eigvecs, eigvals = pca_svd(X_std, p)

    print(f"\nValores propios (estandarizado, pca_svd):\n{eigvals}")
    print(f"\nVectores propios (columnas, estandarizado):\n{eigvecs}")

    # 4. Scree plot y varianza acumulada (estandarizado)
    ve_std, va_std = varianza_y_acumulada(eigvals)
    print(f"\nVarianza explicada (estandarizado): {ve_std}")
    print(f"Varianza explicada acumulada (estandarizado): {va_std}")
    graficar_scree(ve_std, va_std, "Wine estandarizado", "fig_2_3_wine_scree_estandarizado.png")

    # 5. Criterios de decision: codo, umbral de varianza, Kaiser
    n_90 = int(np.argmax(va_std >= 0.90) + 1)
    n_95 = int(np.argmax(va_std >= 0.95) + 1)
    n_kaiser = int(np.sum(eigvals > 1))  # criterio de Kaiser: autovalor > 1 (datos estandarizados)

    # regla del codo: en clase se definio como un criterio VISUAL/heuristico
    # ("donde ocurre el cambio mas abrupto y donde ese cambio comienza a
    # detenerse/aplanarse"), sin una formula rigurosa. Como aproximacion
    # numerica reproducible de esa inspeccion visual (util para no depender
    # de leer la grafica a ojo), se traza la recta que une el primer y el
    # ultimo punto del scree plot y se elige el componente cuyo punto
    # (k, eigval_k) tiene la mayor distancia perpendicular a esa recta.
    puntos = np.column_stack((np.arange(1, p + 1), eigvals))
    p1, p2 = puntos[0], puntos[-1]
    linea = p2 - p1
    linea_norm = linea / np.linalg.norm(linea)
    vecs_a_p1 = puntos - p1
    proyeccion = np.outer(vecs_a_p1 @ linea_norm, linea_norm)
    distancias = np.linalg.norm(vecs_a_p1 - proyeccion, axis=1)
    n_codo = int(np.argmax(distancias) + 1)

    print(f"\nCriterio umbral de varianza (>=90%): {n_90} componentes")
    print(f"Criterio umbral de varianza (>=95%): {n_95} componentes")
    print(f"Criterio de Kaiser (autovalor > 1, datos estandarizados): {n_kaiser} componentes")
    print(f"Regla del codo (visual/heuristica; aproximada numericamente con "
          f"distancia maxima a la cuerda del scree plot): {n_codo} componentes")

    # 6. PCA sin estandarizar
    Z_raw, eigvecs_raw, eigvals_raw = pca_svd(X, p)
    ve_raw, va_raw = varianza_y_acumulada(eigvals_raw)
    print(f"\nValores propios (SIN estandarizar):\n{eigvals_raw}")
    print(f"Varianza explicada (sin estandarizar): {ve_raw}")
    print(f"Varianza explicada acumulada (sin estandarizar): {va_raw}")
    graficar_scree(ve_raw, va_raw, "Wine sin estandarizar", "fig_2_3_wine_scree_sin_estandarizar.png")

    print(
        "\nComparacion estandarizado vs sin estandarizar: sin estandarizar, la "
        f"primera componente concentra {ve_raw[0]*100:.2f}% de la varianza total "
        "(dominada por la variable 'proline', cuya escala numerica -cientos a miles- "
        "es mucho mayor que la del resto de variables, p.ej. 'ash' en el rango 1-3). "
        f"Al estandarizar, la primera componente pasa a explicar solo {ve_std[0]*100:.2f}% "
        "y la varianza se reparte de forma mas equilibrada entre varias componentes. "
        "Esto ocurre porque PCA maximiza varianza en unidades originales: si no se "
        "estandariza, las variables con mayor escala (varianza numerica grande) "
        "dominan artificialmente los primeros componentes, sin que esto refleje "
        "necesariamente mayor relevancia estadistica o discriminativa de esa variable."
    )

    # 7. Reconstruccion y MSE para k=1..13 (usando datos estandarizados)
    mse_lista = []
    ks = list(range(1, p + 1))
    Xc_std = X_std - X_std.mean(axis=0)
    for k in ks:
        Zk, eigvecs_k, _ = pca_svd(X_std, k)
        X_reconstruida = Zk @ eigvecs_k.T + X_std.mean(axis=0)
        mse = np.mean((X_std - X_reconstruida) ** 2)
        mse_lista.append(mse)

    print("\nMSE de reconstruccion (datos estandarizados) para k=1..13:")
    for k, mse in zip(ks, mse_lista):
        print(f"  k={k:2d} -> MSE = {mse:.6f}")

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(ks, mse_lista, marker="o", color="firebrick")
    ax.set_xlabel("Numero de componentes (k)")
    ax.set_ylabel("MSE de reconstruccion")
    ax.set_title("Wine - MSE vs numero de componentes")
    ax.set_xticks(ks)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/fig_2_3_wine_mse_vs_k.png", dpi=300)
    plt.close(fig)
    print("\nFigura guardada: fig_2_3_wine_mse_vs_k.png")

    print("\nScript 2.3 finalizado correctamente.")
