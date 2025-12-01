"""
Unit 4 - Example 3: Principal Component Analysis (PCA)
التجميع وتقليل الأبعاد - مثال 3: تحليل المكونات الرئيسية (PCA)

This example demonstrates:
1. PCA for dimensionality reduction
2. Explained variance
3. Visualizing principal components
4. Choosing optimal number of components
5. PCA for data visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

print("=" * 60)
print("Example 3: Principal Component Analysis (PCA)")
print("مثال 3: تحليل المكونات الرئيسية (PCA)")
print("=" * 60)

# Load Iris dataset as example
# تحميل مجموعة بيانات Iris كمثال
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names

df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

print(f"\nOriginal Data Shape: {df.shape}")
print(df.head())

# Scale features (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. PCA - All Components
print("\n" + "=" * 60)
print("1. PCA - All Components")
print("PCA - جميع المكونات")
print("=" * 60)

pca_full = PCA()
X_pca_full = pca_full.fit_transform(X_scaled)

print(f"\nExplained Variance Ratio:")
print("نسبة التباين الموضحة:")
for i, var_ratio in enumerate(pca_full.explained_variance_ratio_):
    print(f"  PC{i+1}: {var_ratio:.4f} ({var_ratio*100:.2f}%)")

print(f"\nCumulative Explained Variance:")
print("التباين التراكمي الموضح:")
cumsum = np.cumsum(pca_full.explained_variance_ratio_)
for i, cum_var in enumerate(cumsum):
    print(f"  PC1-PC{i+1}: {cum_var:.4f} ({cum_var*100:.2f}%)")

# 2. Visualize Explained Variance
print("\n" + "=" * 60)
print("2. Visualize Explained Variance")
print("تصور التباين الموضح")
print("=" * 60)

plt.figure(figsize=(12, 5))

# Explained variance ratio
plt.subplot(1, 2, 1)
plt.bar(range(1, len(pca_full.explained_variance_ratio_) + 1),
        pca_full.explained_variance_ratio_, alpha=0.7, edgecolor='black')
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance by Principal Component')
plt.grid(True, alpha=0.3, axis='y')

# Cumulative explained variance
plt.subplot(1, 2, 2)
plt.plot(range(1, len(cumsum) + 1), cumsum, 'o-', linewidth=2, markersize=8)
plt.axhline(0.95, color='r', linestyle='--', label='95% Variance')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pca_explained_variance.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'pca_explained_variance.png'")
plt.close()

# 3. PCA with 2 Components (for visualization)
print("\n" + "=" * 60)
print("3. PCA with 2 Components (for visualization)")
print("PCA مع مكونين (للتخيل)")
print("=" * 60)

pca_2d = PCA(n_components=2)
X_pca_2d = pca_2d.fit_transform(X_scaled)

print(f"\nExplained Variance (2 components):")
print(f"  PC1: {pca_2d.explained_variance_ratio_[0]:.4f} ({pca_2d.explained_variance_ratio_[0]*100:.2f}%)")
print(f"  PC2: {pca_2d.explained_variance_ratio_[1]:.4f} ({pca_2d.explained_variance_ratio_[1]*100:.2f}%)")
print(f"  Total: {sum(pca_2d.explained_variance_ratio_):.4f} ({sum(pca_2d.explained_variance_ratio_)*100:.2f}%)")

# Visualize 2D projection
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=y, 
                     cmap='viridis', edgecolors='black', s=100, alpha=0.7)
plt.xlabel(f'First Principal Component ({pca_2d.explained_variance_ratio_[0]*100:.2f}% variance)')
plt.ylabel(f'Second Principal Component ({pca_2d.explained_variance_ratio_[1]*100:.2f}% variance)')
plt.title('PCA: 2D Projection of Iris Dataset')
plt.colorbar(scatter, label='Class')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('pca_2d_projection.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'pca_2d_projection.png'")
plt.close()

# 4. Compare Original vs PCA Transformed Data
print("\n" + "=" * 60)
print("4. Compare Original vs PCA Transformed Data")
print("مقارنة البيانات الأصلية مقابل البيانات المحولة بـ PCA")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Original data (first 2 features)
axes[0].scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', 
               edgecolors='black', s=100, alpha=0.7)
axes[0].set_xlabel(feature_names[0])
axes[0].set_ylabel(feature_names[1])
axes[0].set_title('Original Data (First 2 Features)')
axes[0].grid(True, alpha=0.3)

# PCA transformed data
scatter = axes[1].scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=y, 
                         cmap='viridis', edgecolors='black', s=100, alpha=0.7)
axes[1].set_xlabel(f'PC1 ({pca_2d.explained_variance_ratio_[0]*100:.1f}% variance)')
axes[1].set_ylabel(f'PC2 ({pca_2d.explained_variance_ratio_[1]*100:.1f}% variance)')
axes[1].set_title('PCA Transformed Data (2 Components)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pca_comparison.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'pca_comparison.png'")
plt.close()

# 5. Principal Components as Linear Combinations
print("\n" + "=" * 60)
print("5. Principal Components as Linear Combinations")
print("المكونات الرئيسية كتركيبات خطية")
print("=" * 60)

components_df = pd.DataFrame(
    pca_2d.components_.T,
    columns=['PC1', 'PC2'],
    index=feature_names
)

print("\nPrincipal Components (as linear combinations of original features):")
print("المكونات الرئيسية (كتركيبات خطية للميزات الأصلية):")
print(components_df.round(4))

# Visualize component weights
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for idx, pc in enumerate(['PC1', 'PC2']):
    axes[idx].barh(range(len(feature_names)), components_df[pc], alpha=0.7, edgecolor='black')
    axes[idx].set_yticks(range(len(feature_names)))
    axes[idx].set_yticklabels(feature_names)
    axes[idx].set_xlabel('Component Weight')
    axes[idx].set_title(f'{pc} - Feature Contributions')
    axes[idx].axvline(0, color='black', linestyle='-', linewidth=0.5)
    axes[idx].grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('pca_components_weights.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'pca_components_weights.png'")
plt.close()

# 6. Choosing Optimal Number of Components
print("\n" + "=" * 60)
print("6. Choosing Optimal Number of Components")
print("اختيار العدد الأمثل للمكونات")
print("=" * 60)

n_components_range = range(1, len(feature_names) + 1)
explained_variances = []
cumulative_variances = []

for n in n_components_range:
    pca_temp = PCA(n_components=n)
    pca_temp.fit(X_scaled)
    explained_variances.append(pca_temp.explained_variance_ratio_[-1])
    cumulative_variances.append(sum(pca_temp.explained_variance_ratio_))

# Find number of components for 95% variance
n_components_95 = next((i+1 for i, var in enumerate(cumulative_variances) if var >= 0.95), len(feature_names))
print(f"\nNumber of components for 95% variance: {n_components_95}")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n_components_range, cumulative_variances, 'o-', linewidth=2, markersize=8, label='Cumulative Variance')
plt.axhline(0.95, color='r', linestyle='--', label='95% Variance Threshold')
plt.axvline(n_components_95, color='g', linestyle='--', label=f'{n_components_95} Components')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Choosing Optimal Number of PCA Components')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('pca_optimal_components.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'pca_optimal_components.png'")
plt.close()

# 7. PCA for Data Compression
print("\n" + "=" * 60)
print("7. PCA for Data Compression")
print("PCA لضغط البيانات")
print("=" * 60)

print(f"\nOriginal dimensions: {X_scaled.shape[1]}")
print(f"الأبعاد الأصلية: {X_scaled.shape[1]}")

n_comp = 2
pca_compress = PCA(n_components=n_comp)
X_compressed = pca_compress.fit_transform(X_scaled)
X_reconstructed = pca_compress.inverse_transform(X_compressed)

print(f"Compressed dimensions: {X_compressed.shape[1]}")
print(f"الأبعاد المضغوطة: {X_compressed.shape[1]}")
print(f"Compression ratio: {X_compressed.shape[1] / X_scaled.shape[1]:.2%}")
print(f"نسبة الضغط: {X_compressed.shape[1] / X_scaled.shape[1]:.2%}")

# Calculate reconstruction error
reconstruction_error = np.mean((X_scaled - X_reconstructed) ** 2)
print(f"\nReconstruction Error (MSE): {reconstruction_error:.4f}")
print(f"خطأ إعادة البناء (MSE): {reconstruction_error:.4f}")

print("\n" + "=" * 60)
print("Example 3 Complete! ✓")
print("اكتمل المثال 3! ✓")
print("=" * 60)

