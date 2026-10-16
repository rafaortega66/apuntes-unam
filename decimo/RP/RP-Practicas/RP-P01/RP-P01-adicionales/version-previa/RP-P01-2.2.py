import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

# ============================================
# 2.2 DATASET IRIS
# ============================================

# Cargar Iris
iris = load_iris()
X_iris = iris.data          # (150, 4) - 4 características
y_iris = iris.target        # (150,) - clases (0, 1, 2)
feature_names = iris.feature_names
class_names = iris.target_names

print(f"Forma de X_iris: {X_iris.shape}")
print(f"Características: {feature_names}")
print(f"Clases: {class_names}")

# 1. PAIRPLOT
df_iris = pd.DataFrame(X_iris, columns=feature_names)
df_iris['species'] = [class_names[i] for i in y_iris]

sns.pairplot(df_iris, hue='species', diag_kind='hist')
plt.savefig('2_2_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. CENTRAR LOS DATOS
X_iris_centered = X_iris - X_iris.mean(axis=0)
print(f"\nMedia después de centrar: {X_iris_centered.mean(axis=0)}")

# 3. FUNCIÓN pca_cov()
def pca_cov(X, k):
    """
    PCA mediante matriz de covarianza.
    X: matriz de datos (n muestras x p características), ya centrada
    k: número de componentes principales a retener
    
    Retorna:
    Z: datos proyectados (n x k)
    eigenvectors_k: los k eigenvectores principales (p x k)
    eigenvalues_k: los k eigenvalores asociados (k,)
    """
    # Matriz de covarianza
    cov_matrix = np.cov(X.T)
    
    # Eigenvalores y eigenvectores
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Ordenar de mayor a menor
    idx_orden = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx_orden]
    eigenvectors = eigenvectors[:, idx_orden]
    
    # Tomar los k principales
    eigenvalues_k = eigenvalues[:k]
    eigenvectors_k = eigenvectors[:, :k]
    
    # Proyectar los datos
    Z = X @ eigenvectors_k
    
    return Z, eigenvectors_k, eigenvalues_k

# 4. APLICAR PCA SOBRE IRIS (con las 4 componentes, para el scree plot)
Z_iris, eigvecs_iris, eigvals_iris = pca_cov(X_iris_centered, k=4)

print("\n" + "="*50)
print("PCA sobre Iris - Eigenvalores (los 4)")
print("="*50)
print(eigvals_iris)

# 5. SCREE PLOT Y VARIANZA EXPLICADA ACUMULADA
varianza_explicada = eigvals_iris / np.sum(eigvals_iris)
varianza_acumulada = np.cumsum(varianza_explicada)

print("\n" + "="*50)
print("VARIANZA EXPLICADA")
print("="*50)
for i in range(4):
    print(f"PC{i+1}: {varianza_explicada[i]*100:.2f}% (acumulada: {varianza_acumulada[i]*100:.2f}%)")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Scree plot
axes[0].plot(range(1, 5), eigvals_iris, 'o-', linewidth=2, markersize=8)
axes[0].set_xlabel('Componente Principal')
axes[0].set_ylabel('Eigenvalor')
axes[0].set_title('Scree Plot')
axes[0].set_xticks(range(1, 5))
axes[0].grid(True, alpha=0.3)

# Varianza acumulada
axes[1].plot(range(1, 5), varianza_acumulada * 100, 'o-', linewidth=2, markersize=8, color='green')
axes[1].axhline(y=90, color='red', linestyle='--', label='90%')
axes[1].axhline(y=95, color='orange', linestyle='--', label='95%')
axes[1].set_xlabel('Número de Componentes')
axes[1].set_ylabel('Varianza Explicada Acumulada (%)')
axes[1].set_title('Varianza Acumulada')
axes[1].set_xticks(range(1, 5))
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('2_2_scree_varianza.png', dpi=300, bbox_inches='tight')
plt.show()

# 6. ¿CUÁNTOS COMPONENTES PARA 90-95%?
n_componentes_90 = np.argmax(varianza_acumulada >= 0.90) + 1
n_componentes_95 = np.argmax(varianza_acumulada >= 0.95) + 1
print(f"\nComponentes necesarios para 90%: {n_componentes_90}")
print(f"Componentes necesarios para 95%: {n_componentes_95}")
print(f"\nVector(es) elegido(s) para 90-95%: PC1" + (f" a PC{n_componentes_95}" if n_componentes_95 > 1 else ""))

# 7. PROYECTAR A 2 COMPONENTES PRINCIPALES
Z_iris_2d, eigvecs_2d, eigvals_2d = pca_cov(X_iris_centered, k=2)

plt.figure(figsize=(9, 7))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, class_name in enumerate(class_names):
    mask = y_iris == i
    plt.scatter(Z_iris_2d[mask, 0], Z_iris_2d[mask, 1],
                c=colors[i], label=class_name, alpha=0.7, s=50)

plt.xlabel(f'PC1 ({varianza_explicada[0]*100:.1f}% varianza)')
plt.ylabel(f'PC2 ({varianza_explicada[1]*100:.1f}% varianza)')
plt.title('Iris proyectado en las 2 Componentes Principales')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('2_2_proyeccion_2d.png', dpi=300, bbox_inches='tight')
plt.show()