"""
Practica 1 - PCA
Seccion 2.2: Dataset Iris
Autor: Rafael Ortega de la Paz - 420054085
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

OUTDIR = "."


def pca_cov(X, k):
    """
    PCA mediante la matriz de covarianza.

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
        Los k vectores propios con mayor varianza (columnas).
    eigvals_k : ndarray (k,)
        Los k valores propios asociados, ordenados de mayor a menor.
    """
    Xc = X - X.mean(axis=0)
    cov_matrix = np.cov(Xc, rowvar=False)
    eigvals, eigvecs = np.linalg.eigh(cov_matrix)

    # ordenar de mayor a menor varianza
    orden = np.argsort(eigvals)[::-1]
    eigvals = eigvals[orden]
    eigvecs = eigvecs[:, orden]

    eigvals_k = eigvals[:k]
    eigvecs_k = eigvecs[:, :k]
    Z = Xc @ eigvecs_k

    return Z, eigvecs_k, eigvals_k


if __name__ == "__main__":
    print("=" * 60)
    print("2.2 Dataset Iris")
    print("=" * 60)

    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    df = pd.DataFrame(X, columns=feature_names)
    df["especie"] = pd.Categorical.from_codes(y, target_names)

    # 1. Pairplot
    pp = sns.pairplot(df, hue="especie", diag_kind="hist", palette="Set2")
    pp.fig.suptitle("Iris - Pairplot por especie", y=1.02)
    pp.savefig(f"{OUTDIR}/fig_2_2_iris_pairplot.png", dpi=300)
    plt.close(pp.fig)
    print("\nFigura guardada: fig_2_2_iris_pairplot.png")
    print(
        "\nInspeccion de pares de caracteristicas: 'petal length' y 'petal width' "
        "muestran la separacion mas clara entre las 3 clases (setosa se separa "
        "totalmente de versicolor/virginica, y estas dos se traslapan poco)."
    )

    # 2. Centrar los datos
    X_centrado = X - X.mean(axis=0)

    # 3 y 4. Aplicar pca_cov con todas las componentes (k=4)
    k = X.shape[1]
    Z, eigvecs, eigvals = pca_cov(X, k)

    print(f"\nValores propios (pca_cov), ordenados de mayor a menor:\n{eigvals}")
    print(f"\nVectores propios (columnas, pca_cov):\n{eigvecs}")
    print(f"\nDatos proyectados Z, forma: {Z.shape}")

    # 5. Varianza explicada y varianza explicada acumulada
    varianza_explicada = eigvals / eigvals.sum()
    varianza_acumulada = np.cumsum(varianza_explicada)

    print(f"\nVarianza explicada por componente: {varianza_explicada}")
    print(f"Varianza explicada acumulada: {varianza_acumulada}")

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    componentes = np.arange(1, k + 1)

    axes[0].bar(componentes, varianza_explicada, color="steelblue")
    axes[0].set_xlabel("Componente principal")
    axes[0].set_ylabel("Proporcion de varianza explicada")
    axes[0].set_title("Scree plot - Iris")
    axes[0].set_xticks(componentes)
    axes[0].grid(alpha=0.3)

    axes[1].plot(componentes, varianza_acumulada, marker="o", color="darkorange")
    axes[1].axhline(0.90, color="gray", linestyle="--", linewidth=1, label="90%")
    axes[1].axhline(0.95, color="gray", linestyle=":", linewidth=1, label="95%")
    axes[1].set_xlabel("Numero de componentes")
    axes[1].set_ylabel("Varianza explicada acumulada")
    axes[1].set_title("Varianza acumulada - Iris")
    axes[1].set_xticks(componentes)
    axes[1].legend()
    axes[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/fig_2_2_iris_scree_plot.png", dpi=300)
    plt.close(fig)
    print("\nFigura guardada: fig_2_2_iris_scree_plot.png")

    # 6. Numero de componentes para 90-95% de varianza
    n_90 = int(np.argmax(varianza_acumulada >= 0.90) + 1)
    n_95 = int(np.argmax(varianza_acumulada >= 0.95) + 1)
    print(f"\nComponentes necesarios para >=90% de varianza: {n_90}")
    print(f"Componentes necesarios para >=95% de varianza: {n_95}")
    print(f"Vectores propios elegidos (primeras {n_95} columnas de eigvecs):")
    print(eigvecs[:, :n_95])

    # 7. Proyeccion a 2 componentes principales, coloreada por clase
    Z2, eigvecs2, eigvals2 = pca_cov(X, 2)

    fig, ax = plt.subplots(figsize=(7, 6))
    colores = ["#4C72B0", "#DD8452", "#55A868"]
    for i, nombre in enumerate(target_names):
        mask = y == i
        ax.scatter(Z2[mask, 0], Z2[mask, 1], label=nombre, alpha=0.75, s=35, color=colores[i])
    ax.set_xlabel(f"PC1 ({varianza_explicada[0]*100:.1f}% var.)")
    ax.set_ylabel(f"PC2 ({varianza_explicada[1]*100:.1f}% var.)")
    ax.set_title("Iris proyectado en las 2 primeras componentes principales")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/fig_2_2_iris_pca_2d.png", dpi=300)
    plt.close(fig)
    print("\nFigura guardada: fig_2_2_iris_pca_2d.png")

    print(
        "\nObservacion sobre la separacion en el espacio PCA: en el plano PC1-PC2 "
        "la clase 'setosa' queda claramente separada del resto, mientras que "
        "'versicolor' y 'virginica' se traslapan ligeramente, de forma muy similar "
        "a lo observado en el pairplot original con petal length/width. "
        "PCA no elimina caracteristicas originales ni crea variables medibles fisicamente: "
        "crea NUEVAS variables (combinaciones lineales de las originales) que concentran "
        "la mayor varianza posible; las caracteristicas originales dejan de usarse "
        "directamente pero su informacion se conserva (comprimida) en las componentes."
    )

    print("\nScript 2.2 finalizado correctamente.")
