"""
Unit 5 - Example 1: Grid Search and Random Search for Hyperparameter Tuning
اختيار النموذج والتعزيز - مثال 1: البحث الشبكي والبحث العشوائي لضبط المعاملات

This example demonstrates:
1. Grid Search for hyperparameter tuning
2. Random Search for hyperparameter tuning
3. Comparison of both methods
4. Cross-validation in hyperparameter tuning
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import (GridSearchCV, RandomizedSearchCV,
                                    train_test_split)
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("Example 1: Grid Search and Random Search")
print("مثال 1: البحث الشبكي والبحث العشوائي")
print("=" * 60)

# Generate sample classification data
# إنشاء بيانات تصنيف نموذجية
np.random.seed(42)
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    random_state=42
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
df['target'] = y

print(f"\nData Shape: {df.shape}")
print(f"Target distribution:")
print(df['target'].value_counts())

# Split data
X_data = df.drop('target', axis=1)
y_data = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42, stratify=y_data
)

# Scale features (for SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Grid Search for Random Forest
print("\n" + "=" * 60)
print("1. Grid Search for Random Forest")
print("البحث الشبكي للغابة العشوائية")
print("=" * 60)

# Define parameter grid
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

print(f"\nParameter Grid:")
print(f"  Total combinations: {np.prod([len(v) for v in param_grid_rf.values()])}")
print(f"  المجموعات الإجمالية: {np.prod([len(v) for v in param_grid_rf.values()])}")

# Perform Grid Search
rf = RandomForestClassifier(random_state=42)
grid_search_rf = GridSearchCV(
    rf, param_grid_rf, cv=5, scoring='accuracy',
    n_jobs=-1, verbose=1
)

print("\nStarting Grid Search...")
print("بدء البحث الشبكي...")
grid_search_rf.fit(X_train, y_train)

print(f"\nBest Parameters:")
print(f"أفضل المعاملات:")
for param, value in grid_search_rf.best_params_.items():
    print(f"  {param}: {value}")

print(f"\nBest CV Score: {grid_search_rf.best_score_:.4f}")
print(f"أفضل درجة CV: {grid_search_rf.best_score_:.4f}")

# Test on test set
y_pred_rf = grid_search_rf.best_estimator_.predict(X_test)
test_acc_rf = accuracy_score(y_test, y_pred_rf)
print(f"Test Accuracy: {test_acc_rf:.4f}")
print(f"دقة الاختبار: {test_acc_rf:.4f}")

# 2. Random Search for Random Forest
print("\n" + "=" * 60)
print("2. Random Search for Random Forest")
print("البحث العشوائي للغابة العشوائية")
print("=" * 60)

# Same parameter grid
param_distributions_rf = {
    'n_estimators': [50, 100, 200, 300],
    'max_depth': [3, 5, 7, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Perform Random Search (try fewer combinations)
n_iter = 20  # Try only 20 random combinations
print(f"\nRandom Search will try {n_iter} random combinations")
print(f"سيجرب البحث العشوائي {n_iter} تركيبة عشوائية")

random_search_rf = RandomizedSearchCV(
    rf, param_distributions_rf, n_iter=n_iter, cv=5,
    scoring='accuracy', n_jobs=-1, random_state=42, verbose=1
)

print("\nStarting Random Search...")
print("بدء البحث العشوائي...")
random_search_rf.fit(X_train, y_train)

print(f"\nBest Parameters:")
print(f"أفضل المعاملات:")
for param, value in random_search_rf.best_params_.items():
    print(f"  {param}: {value}")

print(f"\nBest CV Score: {random_search_rf.best_score_:.4f}")
print(f"أفضل درجة CV: {random_search_rf.best_score_:.4f}")

# Test on test set
y_pred_rf_rs = random_search_rf.best_estimator_.predict(X_test)
test_acc_rf_rs = accuracy_score(y_test, y_pred_rf_rs)
print(f"Test Accuracy: {test_acc_rf_rs:.4f}")
print(f"دقة الاختبار: {test_acc_rf_rs:.4f}")

# 3. Grid Search for SVM
print("\n" + "=" * 60)
print("3. Grid Search for SVM")
print("البحث الشبكي لـ SVM")
print("=" * 60)

param_grid_svm = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto', 0.001, 0.01, 0.1, 1],
    'kernel': ['rbf', 'poly', 'sigmoid']
}

print(f"\nParameter Grid:")
print(f"  Total combinations: {np.prod([len(v) for v in param_grid_svm.values()])}")

svm = SVC(random_state=42, probability=True)
grid_search_svm = GridSearchCV(
    svm, param_grid_svm, cv=5, scoring='accuracy',
    n_jobs=-1, verbose=1
)

print("\nStarting Grid Search for SVM...")
grid_search_svm.fit(X_train_scaled, y_train)

print(f"\nBest Parameters:")
for param, value in grid_search_svm.best_params_.items():
    print(f"  {param}: {value}")

print(f"\nBest CV Score: {grid_search_svm.best_score_:.4f}")

y_pred_svm = grid_search_svm.best_estimator_.predict(X_test_scaled)
test_acc_svm = accuracy_score(y_test, y_pred_svm)
print(f"Test Accuracy: {test_acc_svm:.4f}")

# 4. Comparison Table
print("\n" + "=" * 60)
print("4. Comparison of Methods")
print("مقارنة الطرق")
print("=" * 60)

comparison = pd.DataFrame({
    'Method': ['Grid Search (RF)', 'Random Search (RF)', 'Grid Search (SVM)'],
    'Best CV Score': [
        grid_search_rf.best_score_,
        random_search_rf.best_score_,
        grid_search_svm.best_score_
    ],
    'Test Accuracy': [
        test_acc_rf,
        test_acc_rf_rs,
        test_acc_svm
    ],
    'Total Combinations Tried': [
        grid_search_rf.cv_results_['params'].__len__(),
        n_iter,
        grid_search_svm.cv_results_['params'].__len__()
    ]
})

print("\nComparison Table:")
print(comparison.to_string(index=False))

# 5. Visualize Grid Search Results (SVM)
print("\n" + "=" * 60)
print("5. Visualize Grid Search Results")
print("تصور نتائج البحث الشبكي")
print("=" * 60)

# Extract results for visualization
results_df = pd.DataFrame(grid_search_svm.cv_results_)

# Filter for RBF kernel
rbf_results = results_df[results_df['param_kernel'] == 'rbf']

if len(rbf_results) > 0:
    # Create heatmap of C vs gamma
    pivot_table = rbf_results.pivot_table(
        values='mean_test_score',
        index='param_gamma',
        columns='param_C'
    )
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_table, annot=True, fmt='.3f', cmap='viridis', cbar_kws={'label': 'Mean CV Score'})
    plt.title('Grid Search Results: SVM (RBF Kernel)\nC vs Gamma')
    plt.xlabel('C')
    plt.ylabel('Gamma')
    plt.tight_layout()
    plt.savefig('grid_search_heatmap.png', dpi=300, bbox_inches='tight')
    print("\n✓ Plot saved as 'grid_search_heatmap.png'")
    plt.close()

# 6. Compare Computation Time
print("\n" + "=" * 60)
print("6. Computation Time Comparison")
print("مقارنة وقت الحساب")
print("=" * 60)

import time

# Grid Search timing (use smaller grid for demo)
small_param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [3, 5],
    'min_samples_split': [2, 5]
}

rf_small = RandomForestClassifier(random_state=42)
grid_small = GridSearchCV(rf_small, small_param_grid, cv=3, n_jobs=-1)

start_time = time.time()
grid_small.fit(X_train[:500], y_train[:500])  # Use subset for speed
grid_time = time.time() - start_time

# Random Search timing
random_small = RandomizedSearchCV(rf_small, small_param_grid, n_iter=4, cv=3, n_jobs=-1, random_state=42)

start_time = time.time()
random_small.fit(X_train[:500], y_train[:500])
random_time = time.time() - start_time

print(f"\nGrid Search Time: {grid_time:.2f} seconds")
print(f"Random Search Time: {random_time:.2f} seconds")
print(f"Speedup: {grid_time/random_time:.2f}x")

print("\n" + "=" * 60)
print("Example 1 Complete! ✓")
print("اكتمل المثال 1! ✓")
print("=" * 60)

