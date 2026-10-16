import numpy as np
import matplotlib.pyplot as plt

# ============================================
# 2.1 DATASET SINTÉTICO
# ============================================

# Generar datos
np.random.seed(0)
n = 200
x1 = np.random.normal(0, 1, n)
x2 = 2 * x1 + np.random.normal(0, 1.25, n)
X = np.column_stack((x1, x2))

print("Datos originales (primeras 5 filas):")
print(X[:5])
print(f"\nForma de X: {X.shape}")

# 1. CENTRAR LOS DATOS
X_centered = X - X.mean(axis=0)
print("\n" + "="*50)
print("1. DATOS CENTRADOS")
print("="*50)
print(f"Media original: {X.mean(axis=0)}")
print(f"Media después de centrar: {X_centered.mean(axis=0)}")

# 2. MATRIZ DE COVARIANZA, EIGENVALORES Y EIGENVECTORES
cov_matrix = np.cov(X_centered.T)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Ordenar de mayor a menor varianza (convención: PC1 = mayor eigenvalor)
idx_orden = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx_orden]
eigenvectors = eigenvectors[:, idx_orden]

print("\n" + "="*50)
print("2. MATRIZ DE COVARIANZA")
print("="*50)
print(cov_matrix)
print("\nEigenvalores:")
print(eigenvalues)
print("\nEigenvectores:")
print(eigenvectors)

# 3. GRAFICAR DATOS ORIGINALES + VECTORES PROPIOS
plt.figure(figsize=(10, 8))
plt.scatter(X_centered[:, 0], X_centered[:, 1], alpha=0.6, s=30, label='Datos centrados')

# Graficar eigenvectores ponderados por eigenvalores (como flechas desde el origen)
colors = ['red', 'blue']
for i in range(2):
    # Escalar el eigenvector por sqrt(eigenvalue) para que sea proporcional a la varianza
    scale = np.sqrt(eigenvalues[i]) * 3  # Factor 3 para hacerlos visibles
    plt.arrow(0, 0, eigenvectors[0, i] * scale, eigenvectors[1, i] * scale,
              head_width=0.2, head_length=0.2, fc=colors[i], ec=colors[i], linewidth=2,
              label=f'PC{i+1} (λ={eigenvalues[i]:.3f})')

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('2.1 - Datos Sintéticos + Vectores Propios Principales')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.tight_layout()
plt.savefig('2_1_datos_vectores.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. VERIFICAR ORTOGONALIDAD
print("\n" + "="*50)
print("4. VERIFICAR ORTOGONALIDAD")
print("="*50)
# Producto punto entre los dos eigenvectores debe ser ~0
dot_product = np.dot(eigenvectors[:, 0], eigenvectors[:, 1])
print(f"Producto punto entre PC1 y PC2: {dot_product:.6f}")
print(f"¿Son ortogonales? {np.isclose(dot_product, 0, atol=1e-10)}")