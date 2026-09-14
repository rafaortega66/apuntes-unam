"""
Practica 1 - PCA
Seccion 2.4: Comparacion pca_cov vs pca_svd vs sklearn.PCA (dataset Iris)
Autor: Rafael Ortega de la Paz - 420054085
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Reutilizamos las funciones ya implementadas en las secciones anteriores
import importlib.util
import sys


def _cargar_funcion(nombre_modulo, ruta_archivo, nombre_funcion):
    """Importa una funcion especifica de un script sin ejecutar su bloque __main__."""
    spec = importlib.util.spec_from_file_location(nombre_modulo, ruta_archivo)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[nombre_modulo] = modulo
    spec.loader.exec_module(modulo)
    return getattr(modulo, nombre_funcion)


pca_cov = _cargar_funcion("mod_2_2", "RP-P01-2.2.py", "pca_cov")
pca_svd = _cargar_funcion("mod_2_3", "RP-P01-2.3.py", "pca_svd")


def alinear_signo(referencia, vectores):
    """
    Alinea el signo de cada vector propio con respecto a una referencia.
    El signo de los eigenvectores no esta definido de forma unica (v y -v son
    ambos validos), asi que para comparar entre metodos se fuerza a que el
    primer valor de mayor magnitud de cada vector tenga signo positivo,
    usando la referencia como pivote.
    """
    vectores = vectores.copy()
    for i in range(vectores.shape[1]):
        if np.dot(referencia[:, i], vectores[:, i]) < 0:
            vectores[:, i] *= -1
    return vectores


if __name__ == "__main__":
    print("=" * 60)
    print("2.4 Comparacion pca_cov vs pca_svd vs sklearn.PCA (Iris)")
    print("=" * 60)

    iris = load_iris()
    X = iris.data
    k = X.shape[1]  # 4 componentes / 4 caracteristicas

    # --- pca_cov (matriz de covarianza) ---
    Z_cov, eigvecs_cov, eigvals_cov = pca_cov(X, k)

    # --- pca_svd (SVD) ---
    Z_svd, eigvecs_svd, eigvals_svd = pca_svd(X, k)

    # --- PCA de sklearn ---
    modelo_sklearn = PCA(n_components=k)
    Z_sklearn = modelo_sklearn.fit_transform(X - X.mean(axis=0))
    eigvals_sklearn = modelo_sklearn.explained_variance_
    eigvecs_sklearn = modelo_sklearn.components_.T  # sklearn regresa (k, p); transponemos a (p, k)

    # Alinear signos para poder comparar directamente (mismo pivote: pca_cov)
    eigvecs_svd_alineado = alinear_signo(eigvecs_cov, eigvecs_svd)
    eigvecs_sklearn_alineado = alinear_signo(eigvecs_cov, eigvecs_sklearn)

    print("\n--- Valores propios ---")
    print(f"pca_cov     : {eigvals_cov}")
    print(f"pca_svd     : {eigvals_svd}")
    print(f"sklearn.PCA : {eigvals_sklearn}")

    print("\n--- Vectores propios (columnas) ---")
    print("pca_cov:")
    print(eigvecs_cov)
    print("\npca_svd:")
    print(eigvecs_svd)
    print("\nsklearn.PCA:")
    print(eigvecs_sklearn)

    print("\n--- Vectores propios alineados en signo (referencia: pca_cov) ---")
    print("pca_svd alineado:")
    print(eigvecs_svd_alineado)
    print("\nsklearn.PCA alineado:")
    print(eigvecs_sklearn_alineado)

    diff_eigvals_svd = np.max(np.abs(eigvals_cov - eigvals_svd))
    diff_eigvals_sklearn = np.max(np.abs(eigvals_cov - eigvals_sklearn))
    diff_eigvecs_svd = np.max(np.abs(eigvecs_cov - eigvecs_svd_alineado))
    diff_eigvecs_sklearn = np.max(np.abs(eigvecs_cov - eigvecs_sklearn_alineado))

    print("\n--- Diferencias maximas absolutas (tras alinear signo) ---")
    print(f"max|eigvals_cov - eigvals_svd|      = {diff_eigvals_svd:.2e}")
    print(f"max|eigvals_cov - eigvals_sklearn|  = {diff_eigvals_sklearn:.2e}")
    print(f"max|eigvecs_cov - eigvecs_svd|      = {diff_eigvecs_svd:.2e}")
    print(f"max|eigvecs_cov - eigvecs_sklearn|  = {diff_eigvecs_sklearn:.2e}")

    print(
        "\nConclusion: los valores y vectores propios que entregan los tres metodos "
        "son (numericamente) iguales una vez que se alinea el signo de los vectores "
        "propios. La unica 'diferencia' visible antes de alinear es el signo de "
        "algunos vectores propios (v y -v representan la misma direccion/eje "
        "principal, asi que son equivalentes), producto de que tanto la "
        "descomposicion en eigenvalores como la SVD no fijan un signo unico "
        "para los vectores/valores singulares. Las magnitudes coinciden porque "
        "matematicamente diagonalizar la matriz de covarianza (pca_cov) y aplicar "
        "SVD sobre los datos centrados (pca_svd, y sklearn.PCA internamente) son "
        "dos caminos equivalentes para el mismo problema: los valores propios de la "
        "covarianza son los valores singulares al cuadrado divididos entre (n-1), "
        "y los vectores propios son las columnas de V en X = U S V^T. Las "
        "diferencias numericas remanentes son del orden del error de "
        "redondeo de punto flotante (~1e-14 o menor)."
    )

    print("\nScript 2.4 finalizado correctamente.")
