"""
Unit 3 - Example 3: Support Vector Machines (SVM)
تقنيات التصنيف المتقدمة - مثال 3: آلات ناقلات الدعم (SVM)

This example demonstrates:
1. Linear SVM
2. RBF (Radial Basis Function) Kernel SVM
3. Polynomial Kernel SVM
4. Hyperparameter tuning (C, gamma)
5. Decision boundaries visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, classification_report,
                            confusion_matrix, roc_auc_score, roc_curve)

print("=" * 60)
print("Example 3: Support Vector Machines (SVM)")
print("مثال 3: آلات ناقلات الدعم (SVM)")
print("=" * 60)

# Generate sample classification data
# إنشاء بيانات تصنيف نموذجية
np.random.seed(42)

# Create non-linearly separable data
n_samples = 300

# Generate concentric circles pattern
t = np.linspace(0, 2 * np.pi, n_samples // 2)
r1 = np.random.normal(2, 0.5, n_samples // 2)
r2 = np.random.normal(5, 0.5, n_samples // 2)

X1 = np.column_stack([r1 * np.cos(t), r1 * np.sin(t)])
X2 = np.column_stack([r2 * np.cos(t), r2 * np.sin(t)])

X = np.vstack([X1, X2])
y = np.hstack([np.zeros(n_samples // 2), np.ones(n_samples // 2)])

# Shuffle
indices = np.random.permutation(len(X))
X = X[indices]
y = y[indices]

df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])
df['target'] = y

print(f"\nData Shape: {df.shape}")
print(df.head())
print(f"\nTarget distribution:")
print(df['target'].value_counts())

# Split data
X_data = df[['feature_1', 'feature_2']]
y_data = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42, stratify=y_data
)

# Scale features (important for SVM)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Linear SVM
print("\n" + "=" * 60)
print("1. Linear SVM")
print("SVM الخطي")
print("=" * 60)

svm_linear = SVC(kernel='linear', C=1.0, probability=True, random_state=42)
svm_linear.fit(X_train_scaled, y_train)

y_train_pred_linear = svm_linear.predict(X_train_scaled)
y_test_pred_linear = svm_linear.predict(X_test_scaled)

train_acc_linear = accuracy_score(y_train, y_train_pred_linear)
test_acc_linear = accuracy_score(y_test, y_test_pred_linear)

print(f"Training Accuracy: {train_acc_linear:.4f}")
print(f"Test Accuracy: {test_acc_linear:.4f}")

# 2. RBF Kernel SVM
print("\n" + "=" * 60)
print("2. RBF Kernel SVM")
print("SVM مع نواة RBF")
print("=" * 60)

svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
svm_rbf.fit(X_train_scaled, y_train)

y_train_pred_rbf = svm_rbf.predict(X_train_scaled)
y_test_pred_rbf = svm_rbf.predict(X_test_scaled)

train_acc_rbf = accuracy_score(y_train, y_train_pred_rbf)
test_acc_rbf = accuracy_score(y_test, y_test_pred_rbf)

print(f"Training Accuracy: {train_acc_rbf:.4f}")
print(f"Test Accuracy: {test_acc_rbf:.4f}")

# Probability predictions
y_test_proba_rbf = svm_rbf.predict_proba(X_test_scaled)[:, 1]

# 3. Polynomial Kernel SVM
print("\n" + "=" * 60)
print("3. Polynomial Kernel SVM")
print("SVM مع نواة متعددة الحدود")
print("=" * 60)

svm_poly = SVC(kernel='poly', degree=3, C=1.0, probability=True, random_state=42)
svm_poly.fit(X_train_scaled, y_train)

y_train_pred_poly = svm_poly.predict(X_train_scaled)
y_test_pred_poly = svm_poly.predict(X_test_scaled)

train_acc_poly = accuracy_score(y_train, y_train_pred_poly)
test_acc_poly = accuracy_score(y_test, y_test_pred_poly)

print(f"Training Accuracy: {train_acc_poly:.4f}")
print(f"Test Accuracy: {test_acc_poly:.4f}")

# 4. Model Comparison
print("\n" + "=" * 60)
print("4. Model Comparison")
print("مقارنة النماذج")
print("=" * 60)

comparison = pd.DataFrame({
    'Kernel': ['Linear', 'RBF', 'Polynomial'],
    'Train Accuracy': [train_acc_linear, train_acc_rbf, train_acc_poly],
    'Test Accuracy': [test_acc_linear, test_acc_rbf, test_acc_poly]
})

print("\nSVM Kernel Comparison:")
print(comparison.to_string(index=False))

# 5. Hyperparameter Tuning - C parameter
print("\n" + "=" * 60)
print("5. Hyperparameter Tuning - C Parameter")
print("ضبط المعاملات - معامل C")
print("=" * 60)

C_values = [0.01, 0.1, 1, 10, 100]
train_scores_c = []
test_scores_c = []

for C in C_values:
    svm_temp = SVC(kernel='rbf', C=C, gamma='scale', random_state=42)
    svm_temp.fit(X_train_scaled, y_train)
    train_scores_c.append(accuracy_score(y_train, svm_temp.predict(X_train_scaled)))
    test_scores_c.append(accuracy_score(y_test, svm_temp.predict(X_test_scaled)))

# Plot C parameter effect
plt.figure(figsize=(10, 6))
plt.semilogx(C_values, train_scores_c, 'o-', label='Training Accuracy', linewidth=2)
plt.semilogx(C_values, test_scores_c, 's-', label='Test Accuracy', linewidth=2)
plt.xlabel('C (Regularization Parameter)')
plt.ylabel('Accuracy')
plt.title('SVM: C Parameter vs Performance')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('svm_c_parameter.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'svm_c_parameter.png'")
plt.close()

# 6. Hyperparameter Tuning - Gamma parameter
print("\n" + "=" * 60)
print("6. Hyperparameter Tuning - Gamma Parameter")
print("ضبط المعاملات - معامل Gamma")
print("=" * 60)

gamma_values = [0.001, 0.01, 0.1, 1, 10]
train_scores_gamma = []
test_scores_gamma = []

for gamma in gamma_values:
    svm_temp = SVC(kernel='rbf', C=1.0, gamma=gamma, random_state=42)
    svm_temp.fit(X_train_scaled, y_train)
    train_scores_gamma.append(accuracy_score(y_train, svm_temp.predict(X_train_scaled)))
    test_scores_gamma.append(accuracy_score(y_test, svm_temp.predict(X_test_scaled)))

# Plot gamma parameter effect
plt.figure(figsize=(10, 6))
plt.semilogx(gamma_values, train_scores_gamma, 'o-', label='Training Accuracy', linewidth=2)
plt.semilogx(gamma_values, test_scores_gamma, 's-', label='Test Accuracy', linewidth=2)
plt.xlabel('Gamma')
plt.ylabel('Accuracy')
plt.title('SVM: Gamma Parameter vs Performance')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('svm_gamma_parameter.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'svm_gamma_parameter.png'")
plt.close()

# 7. Decision Boundaries Visualization
print("\n" + "=" * 60)
print("7. Decision Boundaries Visualization")
print("تصور حدود القرار")
print("=" * 60)

def plot_decision_boundary(X, y, model, title, ax):
    """Plot decision boundary for 2D data"""
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    ax.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu')
    scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlBu', 
                        edgecolors='black', s=50)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.set_title(title)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

models_for_plot = [
    (svm_linear, 'Linear SVM', X_train_scaled),
    (svm_rbf, 'RBF Kernel SVM', X_train_scaled),
    (svm_poly, 'Polynomial Kernel SVM', X_train_scaled)
]

for idx, (model, title, X_plot) in enumerate(models_for_plot):
    plot_decision_boundary(X_plot, y_train, model, title, axes[idx])

plt.tight_layout()
plt.savefig('svm_decision_boundaries.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'svm_decision_boundaries.png'")
plt.close()

# 8. Support Vectors
print("\n" + "=" * 60)
print("8. Support Vectors Analysis")
print("تحليل ناقلات الدعم")
print("=" * 60)

print(f"\nNumber of Support Vectors (Linear): {len(svm_linear.support_vectors_)}")
print(f"Number of Support Vectors (RBF): {len(svm_rbf.support_vectors_)}")
print(f"Number of Support Vectors (Polynomial): {len(svm_poly.support_vectors_)}")

# Visualize support vectors
plt.figure(figsize=(10, 8))
plt.scatter(X_train_scaled[:, 0], X_train_scaled[:, 1], 
           c=y_train, cmap='RdYlBu', alpha=0.5, s=50, edgecolors='black')
plt.scatter(svm_rbf.support_vectors_[:, 0], svm_rbf.support_vectors_[:, 1],
           facecolors='none', edgecolors='red', s=200, linewidths=2,
           label='Support Vectors')
plt.xlabel('Feature 1 (Scaled)')
plt.ylabel('Feature 2 (Scaled)')
plt.title('Support Vectors (RBF Kernel)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('support_vectors.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'support_vectors.png'")
plt.close()

# 9. ROC Curves Comparison
print("\n" + "=" * 60)
print("9. ROC Curves Comparison")
print("مقارنة منحنيات ROC")
print("=" * 60)

# Calculate ROC curves
y_test_proba_linear = svm_linear.predict_proba(X_test_scaled)[:, 1]
y_test_proba_poly = svm_poly.predict_proba(X_test_scaled)[:, 1]

fpr_linear, tpr_linear, _ = roc_curve(y_test, y_test_proba_linear)
fpr_rbf, tpr_rbf, _ = roc_curve(y_test, y_test_proba_rbf)
fpr_poly, tpr_poly, _ = roc_curve(y_test, y_test_proba_poly)

auc_linear = roc_auc_score(y_test, y_test_proba_linear)
auc_rbf = roc_auc_score(y_test, y_test_proba_rbf)
auc_poly = roc_auc_score(y_test, y_test_proba_poly)

print(f"\nAUC Scores:")
print(f"Linear: {auc_linear:.4f}")
print(f"RBF: {auc_rbf:.4f}")
print(f"Polynomial: {auc_poly:.4f}")

# Plot ROC curves
plt.figure(figsize=(10, 8))
plt.plot(fpr_linear, tpr_linear, linewidth=2, label=f'Linear (AUC = {auc_linear:.4f})')
plt.plot(fpr_rbf, tpr_rbf, linewidth=2, label=f'RBF (AUC = {auc_rbf:.4f})')
plt.plot(fpr_poly, tpr_poly, linewidth=2, label=f'Polynomial (AUC = {auc_poly:.4f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('SVM ROC Curves Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('svm_roc_curves.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'svm_roc_curves.png'")
plt.close()

print("\n" + "=" * 60)
print("Example 3 Complete! ✓")
print("اكتمل المثال 3! ✓")
print("=" * 60)

