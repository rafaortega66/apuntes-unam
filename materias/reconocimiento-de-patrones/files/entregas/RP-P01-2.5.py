"""
Practica 1 - PCA
Seccion 2.5: EigenFaces (dataset Olivetti Faces)
Autor: Rafael Ortega de la Paz - 420054085
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces

import importlib.util
import sys


def _cargar_funcion(nombre_modulo, ruta_archivo, nombre_funcion):
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[nombre_modulo] = modulo
    spec.loader.exec_module(modulo)
    return getattr(modulo, nombre_funcion)


pca_svd = _cargar_funcion("mod_2_3_faces", "RP-P01-2.3.py", "pca_svd")

OUTDIR = "."

if __name__ == "__main__":
    print("=" * 60)
    print("2.5 EigenFaces - dataset Olivetti Faces")
    print("=" * 60)

    faces = fetch_olivetti_faces(shuffle=True, random_state=0)
    alto, ancho = faces.images.shape[1], faces.images.shape[2]

    # 1. Matriz X de (n x p): n imagenes, p pixeles
    X = faces.data  # ya viene aplanada como (400, 4096), valores en [0,1]
    n, p = X.shape
    print(f"Forma de X: {X.shape}  (n={n} imagenes, p={p} pixeles, {alto}x{ancho})")

    # 2. Centrar la matriz X
    media = X.mean(axis=0)
    X_centrado = X - media

    # 3. Aplicar PCA con pca_svd. Usamos min(n,p)-1 componentes como maximo util.
    k_max = min(n, p)
    Z, eigenfaces, eigvals = pca_svd(X, k_max)
    print(f"\nSe calcularon {k_max} componentes principales (eigenfaces).")
    print(f"Primeros 10 valores propios: {eigvals[:10]}")

    # 4. Rostro promedio
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(media.reshape(alto, ancho), cmap="gray")
    ax.set_title("Rostro promedio")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/fig_2_5_rostro_promedio.png", dpi=300)
    plt.close(fig)
    print("\nFigura guardada: fig_2_5_rostro_promedio.png")

    # 5. Primeras 10 y ultimas 10 eigenfaces
    def graficar_eigenfaces(indices, titulo, nombre_archivo):
        fig, axes = plt.subplots(2, 5, figsize=(12, 5.2))
        for ax, idx in zip(axes.ravel(), indices):
            ef = eigenfaces[:, idx].reshape(alto, ancho)
            ax.imshow(ef, cmap="gray")
            ax.set_title(f"PC{idx+1}", fontsize=9)
            ax.axis("off")
        fig.suptitle(titulo)
        fig.tight_layout()
        fig.savefig(f"{OUTDIR}/{nombre_archivo}", dpi=300)
        plt.close(fig)
        print(f"Figura guardada: {nombre_archivo}")

    primeras_10 = list(range(10))
    ultimas_10 = list(range(k_max - 10, k_max))
    graficar_eigenfaces(primeras_10, "Primeras 10 eigenfaces (mayor varianza)", "fig_2_5_primeras_10_eigenfaces.png")
    graficar_eigenfaces(ultimas_10, "Ultimas 10 eigenfaces (menor varianza)", "fig_2_5_ultimas_10_eigenfaces.png")

    # 6. Reconstruccion de una imagen con 10,50,100,200,300 eigenvectores
    idx_imagen = 0
    imagen_original = X[idx_imagen]
    ks_reconstruccion = [10, 50, 100, 200, 300]

    fig, axes = plt.subplots(1, len(ks_reconstruccion) + 1, figsize=(3 * (len(ks_reconstruccion) + 1), 3.3))
    axes[0].imshow(imagen_original.reshape(alto, ancho), cmap="gray")
    axes[0].set_title("Original")
    axes[0].axis("off")

    for i, k in enumerate(ks_reconstruccion, start=1):
        proy = (imagen_original - media) @ eigenfaces[:, :k]
        reconstruida = proy @ eigenfaces[:, :k].T + media
        axes[i].imshow(reconstruida.reshape(alto, ancho), cmap="gray")
        axes[i].set_title(f"k={k}")
        axes[i].axis("off")

    fig.suptitle("Reconstruccion de una imagen con distinto numero de eigenfaces")
    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/fig_2_5_reconstruccion_por_k.png", dpi=300)
    plt.close(fig)
    print("\nFigura guardada: fig_2_5_reconstruccion_por_k.png")

    # 7. MSE vs numero de componentes, en intervalos de 20 (usando todo el dataset)
    ks_mse = list(range(20, k_max + 1, 20))
    if ks_mse[-1] != k_max:
        ks_mse.append(k_max)

    mse_lista = []
    for k in ks_mse:
        Zk = X_centrado @ eigenfaces[:, :k]
        X_reconstruida = Zk @ eigenfaces[:, :k].T + media
        mse = np.mean((X - X_reconstruida) ** 2)
        mse_lista.append(mse)

    print("\nMSE de reconstruccion (todo el dataset) para distintos k:")
    for k, mse in zip(ks_mse, mse_lista):
        print(f"  k={k:3d} -> MSE = {mse:.6f}")

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(ks_mse, mse_lista, marker="o", color="firebrick")
    ax.set_xlabel("Numero de componentes (k)")
    ax.set_ylabel("MSE de reconstruccion")
    ax.set_title("Olivetti Faces - MSE vs numero de componentes")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{OUTDIR}/fig_2_5_mse_vs_k.png", dpi=300)
    plt.close(fig)
    print("\nFigura guardada: fig_2_5_mse_vs_k.png")

    varianza_total = eigvals.sum()
    varianza_explicada_acumulada = np.cumsum(eigvals) / varianza_total
    print(f"\nVarianza explicada acumulada en k=300: {varianza_explicada_acumulada[299]*100:.4f}%")
    print(f"Varianza descartada en k=300: {(1 - varianza_explicada_acumulada[299])*100:.4f}%")

    print(
        "\nEl error de reconstruccion (MSE) disminuye al aumentar el numero de "
        "componentes k porque cada eigenvector adicional que se incorpora aporta "
        "la varianza (informacion) asociada a su valor propio, la cual antes se "
        "estaba descartando. El MSE de reconstruccion es, salvo un factor de "
        "escala, exactamente la suma de los valores propios NO utilizados (la "
        "varianza descartada): al usar los k componentes de mayor varianza, el "
        "error residual es proporcional a la suma de los eigvals de las "
        "componentes k+1, k+2, ..., p. Como el algoritmo SVD/PCA ordena las "
        "componentes de mayor a menor varianza, cada componente adicional que se "
        "agrega es la que mas reduce ese residuo posible en ese paso; por eso el "
        "MSE decrece monotonamente y de forma cada vez mas lenta (la curva se "
        "aplana) conforme los eigenvalores restantes son cada vez mas pequenos."
    )

    print("\nScript 2.5 finalizado correctamente.")
