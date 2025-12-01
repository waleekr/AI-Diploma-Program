"""
Unit 4 - Example 2: Hierarchical Clustering
التجميع وتقليل الأبعاد - مثال 2: التجميع الهرمي

This example demonstrates:
1. Agglomerative Hierarchical Clustering
2. Different linkage methods
3. Dendrogram visualization
4. Cutting dendrogram to get clusters
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import seaborn as sns

print("=" * 60)
print("Example 2: Hierarchical Clustering")
print("مثال 2: التجميع الهرمي")
print("=" * 60)

# Generate sample data
# إنشاء بيانات نموذجية
np.random.seed(42)

# Create distinct clusters
cluster1 = np.random.normal([2, 2], 0.5, (50, 2))
cluster2 = np.random.normal([6, 6], 0.5, (50, 2))
cluster3 = np.random.normal([2, 6], 0.5, (50, 2))

X = np.vstack([cluster1, cluster2, cluster3])

# Shuffle
indices = np.random.permutation(len(X))
X = X[indices]

df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])
print(f"\nData Shape: {df.shape}")
print(df.head())

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. Different Linkage Methods
print("\n" + "=" * 60)
print("1. Different Linkage Methods")
print("طرق الربط المختلفة")
print("=" * 60)

linkage_methods = ['ward', 'complete', 'average', 'single']

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
axes = axes.ravel()

for idx, method in enumerate(linkage_methods):
    # Perform hierarchical clustering
    Z = linkage(X_scaled, method=method)
    
    # Plot dendrogram
    dendrogram(Z, ax=axes[idx], truncate_mode='level', p=5)
    axes[idx].set_title(f'Dendrogram - {method.capitalize()} Linkage')
    axes[idx].set_xlabel('Sample Index')
    axes[idx].set_ylabel('Distance')

plt.tight_layout()
plt.savefig('hierarchical_dendrograms.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'hierarchical_dendrograms.png'")
plt.close()

# 2. Detailed Dendrogram with Ward Linkage
print("\n" + "=" * 60)
print("2. Detailed Dendrogram (Ward Linkage)")
print("الرسم الشجري التفصيلي (ربط Ward)")
print("=" * 60)

Z = linkage(X_scaled, method='ward')

plt.figure(figsize=(12, 8))
dendrogram(Z, truncate_mode='level', p=5, 
          show_leaf_counts=True, leaf_rotation=90, leaf_font_size=12)
plt.xlabel('Sample Index or (Cluster Size)')
plt.ylabel('Distance')
plt.title('Hierarchical Clustering Dendrogram (Ward Linkage)')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('detailed_dendrogram.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'detailed_dendrogram.png'")
plt.close()

# 3. Cutting Dendrogram to Get Clusters
print("\n" + "=" * 60)
print("3. Cutting Dendrogram to Get Clusters")
print("قطع الرسم الشجري للحصول على مجموعات")
print("=" * 60)

n_clusters = 3

# Method 1: Using distance threshold
distance_threshold = 3.0
labels_distance = fcluster(Z, distance_threshold, criterion='distance')

# Method 2: Using number of clusters
labels_n_clusters = fcluster(Z, n_clusters, criterion='maxclust')

print(f"\nClusters with distance threshold {distance_threshold}:")
print(f"عدد المجموعات: {len(np.unique(labels_distance))}")

print(f"\nClusters with n_clusters={n_clusters}:")
print(f"عدد المجموعات: {len(np.unique(labels_n_clusters))}")

# 4. Visualize Clusters
print("\n" + "=" * 60)
print("4. Visualize Clusters")
print("تصور المجموعات")
print("=" * 60)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Original data
axes[0].scatter(X[:, 0], X[:, 1], alpha=0.6, s=50, edgecolors='black')
axes[0].set_xlabel('Feature 1')
axes[0].set_ylabel('Feature 2')
axes[0].set_title('Original Data')
axes[0].grid(True, alpha=0.3)

# Distance threshold clusters
scatter1 = axes[1].scatter(X[:, 0], X[:, 1], c=labels_distance, 
                          cmap='viridis', alpha=0.7, s=50, edgecolors='black')
axes[1].set_xlabel('Feature 1')
axes[1].set_ylabel('Feature 2')
axes[1].set_title(f'Clusters (Distance Threshold = {distance_threshold})')
axes[1].grid(True, alpha=0.3)
plt.colorbar(scatter1, ax=axes[1])

# N clusters
scatter2 = axes[2].scatter(X[:, 0], X[:, 1], c=labels_n_clusters, 
                          cmap='viridis', alpha=0.7, s=50, edgecolors='black')
axes[2].set_xlabel('Feature 1')
axes[2].set_ylabel('Feature 2')
axes[2].set_title(f'Clusters (n_clusters = {n_clusters})')
axes[2].grid(True, alpha=0.3)
plt.colorbar(scatter2, ax=axes[2])

plt.tight_layout()
plt.savefig('hierarchical_clusters.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'hierarchical_clusters.png'")
plt.close()

# 5. Using AgglomerativeClustering from sklearn
print("\n" + "=" * 60)
print("5. Using AgglomerativeClustering (sklearn)")
print("استخدام AgglomerativeClustering (sklearn)")
print("=" * 60)

agg_cluster = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels_agg = agg_cluster.fit_predict(X_scaled)

print(f"Number of clusters: {len(np.unique(labels_agg))}")
print(f"Silhouette Score: {silhouette_score(X_scaled, labels_agg):.4f}")

# 6. Compare Different Numbers of Clusters
print("\n" + "=" * 60)
print("6. Compare Different Numbers of Clusters")
print("مقارنة أعداد مختلفة من المجموعات")
print("=" * 60)

n_clusters_range = range(2, 7)
silhouette_scores = []

for n in n_clusters_range:
    agg_temp = AgglomerativeClustering(n_clusters=n, linkage='ward')
    labels_temp = agg_temp.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels_temp)
    silhouette_scores.append(score)

# Find optimal number
optimal_n = n_clusters_range[np.argmax(silhouette_scores)]
print(f"\nOptimal number of clusters: {optimal_n}")
print(f"Best Silhouette Score: {max(silhouette_scores):.4f}")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n_clusters_range, silhouette_scores, 'o-', linewidth=2, markersize=8)
plt.axvline(optimal_n, color='r', linestyle='--', label=f'Optimal: {optimal_n}')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.title('Hierarchical Clustering: Number of Clusters vs Silhouette Score')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('hierarchical_silhouette.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'hierarchical_silhouette.png'")
plt.close()

# 7. Compare Linkage Methods
print("\n" + "=" * 60)
print("7. Compare Linkage Methods")
print("مقارنة طرق الربط")
print("=" * 60)

linkage_methods = ['ward', 'complete', 'average']
n_clusters = 3

results = []

for method in linkage_methods:
    agg_temp = AgglomerativeClustering(n_clusters=n_clusters, linkage=method)
    labels_temp = agg_temp.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels_temp)
    results.append({
        'Linkage': method,
        'Silhouette Score': score
    })

results_df = pd.DataFrame(results)
print("\nLinkage Methods Comparison:")
print(results_df.to_string(index=False))

print("\n" + "=" * 60)
print("Example 2 Complete! ✓")
print("اكتمل المثال 2! ✓")
print("=" * 60)

