"""
Unit 4 - Example 1: K-Means Clustering
التجميع وتقليل الأبعاد - مثال 1: تجميع K-Means

This example demonstrates:
1. K-Means clustering
2. Finding optimal number of clusters (Elbow Method, Silhouette Score)
3. Visualizing clusters
4. Evaluating cluster quality
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

print("=" * 60)
print("Example 1: K-Means Clustering")
print("مثال 1: تجميع K-Means")
print("=" * 60)

# Generate sample data with clear clusters
# إنشاء بيانات نموذجية مع مجموعات واضحة
np.random.seed(42)

# Cluster 1
cluster1 = np.random.normal([2, 2], 0.5, (100, 2))
# Cluster 2
cluster2 = np.random.normal([6, 6], 0.5, (100, 2))
# Cluster 3
cluster3 = np.random.normal([2, 6], 0.5, (100, 2))

# Combine clusters
X = np.vstack([cluster1, cluster2, cluster3])

# Shuffle data
indices = np.random.permutation(len(X))
X = X[indices]

df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])
print(f"\nData Shape: {df.shape}")
print(df.head())

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. Visualize Original Data
print("\n" + "=" * 60)
print("1. Original Data Visualization")
print("تصور البيانات الأصلية")
print("=" * 60)

plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.6, s=50)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Original Data (Unlabeled)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('original_data.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'original_data.png'")
plt.close()

# 2. K-Means with K=3 (known optimal)
print("\n" + "=" * 60)
print("2. K-Means Clustering (K=3)")
print("تجميع K-Means (K=3)")
print("=" * 60)

kmeans_3 = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_3 = kmeans_3.fit_predict(X_scaled)

print(f"Inertia (within-cluster sum of squares): {kmeans_3.inertia_:.2f}")
print(f"Silhouette Score: {silhouette_score(X_scaled, labels_3):.4f}")

# Visualize clusters
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X[:, 0], X[:, 1], c=labels_3, cmap='viridis', 
                     edgecolors='black', s=50, alpha=0.7)
plt.scatter(kmeans_3.cluster_centers_[:, 0], 
           scaler.inverse_transform(kmeans_3.cluster_centers_)[:, 1],
           c='red', marker='X', s=200, label='Centroids', 
           edgecolors='black', linewidths=2)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-Means Clustering (K=3)')
plt.legend()
plt.colorbar(scatter)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('kmeans_k3.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'kmeans_k3.png'")
plt.close()

# 3. Finding Optimal K - Elbow Method
print("\n" + "=" * 60)
print("3. Finding Optimal K - Elbow Method")
print("إيجاد K المثلى - طريقة المرفق")
print("=" * 60)

k_range = range(1, 11)
inertias = []
silhouette_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    inertias.append(kmeans.inertia_)
    if k > 1:  # Silhouette score requires at least 2 clusters
        silhouette_scores.append(silhouette_score(X_scaled, labels))
    else:
        silhouette_scores.append(0)

# Plot Elbow Method
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(k_range, inertias, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal K')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(k_range, silhouette_scores, 'ro-', linewidth=2, markersize=8)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score vs K')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('optimal_k.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'optimal_k.png'")
plt.close()

# Find optimal K
optimal_k_elbow = k_range[np.argmax(np.diff(inertias) < -50)]  # Simplified
optimal_k_silhouette = k_range[np.argmax(silhouette_scores)]

print(f"\nOptimal K (Elbow Method): ~{optimal_k_elbow}")
print(f"Optimal K (Silhouette Score): {optimal_k_silhouette}")
print(f"  Best Silhouette Score: {max(silhouette_scores):.4f}")

# 4. Compare Different K Values
print("\n" + "=" * 60)
print("4. Compare Different K Values")
print("مقارنة قيم K المختلفة")
print("=" * 60)

k_values = [2, 3, 4, 5]
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

for idx, k in enumerate(k_values):
    row = idx // 2
    col = idx % 2
    
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    axes[row, col].scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis',
                          edgecolors='black', s=50, alpha=0.7)
    centers = scaler.inverse_transform(kmeans.cluster_centers_)
    axes[row, col].scatter(centers[:, 0], centers[:, 1],
                          c='red', marker='X', s=200,
                          edgecolors='black', linewidths=2)
    axes[row, col].set_xlabel('Feature 1')
    axes[row, col].set_ylabel('Feature 2')
    silhouette = silhouette_score(X_scaled, labels)
    axes[row, col].set_title(f'K={k} (Silhouette: {silhouette:.3f})')
    axes[row, col].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('kmeans_comparison.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'kmeans_comparison.png'")
plt.close()

# 5. Summary Table
print("\n" + "=" * 60)
print("5. Clustering Summary")
print("ملخص التجميع")
print("=" * 60)

summary_data = {
    'K': k_range,
    'Inertia': [f"{x:.2f}" for x in inertias],
    'Silhouette Score': [f"{x:.4f}" for x in silhouette_scores]
}

summary_df = pd.DataFrame(summary_data)
print("\nClustering Metrics for Different K:")
print(summary_df.to_string(index=False))

print("\n" + "=" * 60)
print("Example 1 Complete! ✓")
print("اكتمل المثال 1! ✓")
print("=" * 60)

