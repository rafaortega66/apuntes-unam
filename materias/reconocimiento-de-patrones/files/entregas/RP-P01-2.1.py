"""
Practica 1 - PCA
Seccion 2.1: Dataset sintetico de dos variables
Autor: Rafael Ortega de la Paz - 420054085
"""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

OUTDIR = "."

# --- Generacion del dataset sintetico (codigo dado por el enunciado) ---
np.random.seed(0)
n = 200
x1 = np.random.normal(0, 1, n)
x2 = 2 * x1 + np.random.normal(0, 1.25, n)
X = np.column_stack((x1, x2))

print("=" * 60)
print("2.1 Dataset sintetico de dos variables")
print("=" * 60)
print(f"Forma de X: {X.shape}")

# 1. Centrar los datos usando la media
media = X.mean(axis=0)
X_centrado = X - media
print(f"\nMedia original: {media}")
print(f"Media despues de centrar: {X_centrado.mean(axis=0)}")

# 2. Matriz de covarianza, valores y vectores propios
# rowvar=False porque las variables son las columnas
cov_matrix = np.cov(X_centrado, rowvar=False)
eigvals, eigvecs = np.linalg.eigh(cov_matrix)

# ordenar de mayor a menor varianza (convencion PC1 = mayor varianza)
orden = np.argsort(eigvals)[::-1]
eigvals = eigvals[orden]
eigvecs = eigvecs[:, orden]

print("\nMatriz de covarianza:")
print(cov_matrix)
print("\nValores propios (ordenados de mayor a menor varianza):")
print(eigvals)
print("\nVectores propios (cada columna es un vector propio):")
print(eigvecs)

# 4. Verificar ortogonalidad de los vectores propios
producto_punto = np.dot(eigvecs[:, 0], eigvecs[:, 1])
print(f"\nProducto punto entre v1 y v2 (0 => ortogonales): {producto_punto:.2e}")
gram = eigvecs.T @ eigvecs
print("Matriz V^T V (debe ser ~identidad si son ortonormales):")
print(gram)
son_ortogonales = np.isclose(producto_punto, 0, atol=1e-10)
print(f"¿Son los vectores propios ortogonales entre si? {son_ortogonales}")

# 3. Graficar los datos originales y los vectores propios como direcciones
#    principales ponderadas por sus valores propios
fig, ax = plt.subplots(figsize=(7, 6))
ax.scatter(X[:, 0], X[:, 1], alpha=0.5, s=25, color="steelblue", label="Datos originales")

colores = ["crimson", "darkorange"]
# Se escala cada vector propio por su valor propio (raiz cuadrada da una escala
# proporcional a la desviacion estandar en esa direccion) para que la longitud
# graficada refleje la varianza explicada por esa direccion.
escala = 2  # factor visual para que las flechas sean claramente visibles
for i in range(eigvecs.shape[1]):
    vec = eigvecs[:, i] * np.sqrt(eigvals[i]) * escala
    ax.annotate(
        "",
        xy=(media[0] + vec[0], media[1] + vec[1]),
        xytext=(media[0], media[1]),
        arrowprops=dict(arrowstyle="->", color=colores[i], linewidth=2.5),
    )
    ax.plot([], [], color=colores[i], linewidth=2.5, label=f"PC{i+1} (λ={eigvals[i]:.2f})")

ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_title("Datos sinteticos y direcciones principales (PCA)")
ax.legend()
ax.axis("equal")
ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(f"{OUTDIR}/fig_2_1_datos_y_vectores_propios.png", dpi=300)
plt.close(fig)

print("\nFigura guardada: fig_2_1_datos_y_vectores_propios.png")
print("\nScript 2.1 finalizado correctamente.")
