"""
Unit 3 - Example 2: Decision Trees and Random Forest
تقنيات التصنيف المتقدمة - مثال 2: أشجار القرار والغابة العشوائية

This example demonstrates:
1. Decision Tree Classifier
2. Random Forest Classifier
3. Feature importance
4. Overfitting in Decision Trees
5. Comparison of different tree-based models
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, classification_report,
                            confusion_matrix, roc_auc_score, roc_curve)
from sklearn.datasets import make_classification

print("=" * 60)
print("Example 2: Decision Trees and Random Forest")
print("مثال 2: أشجار القرار والغابة العشوائية")
print("=" * 60)

# Generate sample classification data
# إنشاء بيانات تصنيف نموذجية
np.random.seed(42)
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    n_clusters_per_class=1,
    random_state=42
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
df['target'] = y

print(f"\nData Shape: {df.shape}")
print(df.head())
print(f"\nTarget distribution:")
print(df['target'].value_counts())

# Split data
X_data = df.drop('target', axis=1)
y_data = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42, stratify=y_data
)

# Note: Tree-based models don't require scaling, but we show it for consistency
# ملاحظة: نماذج الأشجار لا تحتاج قياس، لكننا نعرضها للاتساق

# 1. Decision Tree - Default Parameters
print("\n" + "=" * 60)
print("1. Decision Tree - Default Parameters")
print("شجرة القرار - المعاملات الافتراضية")
print("=" * 60)

dt_default = DecisionTreeClassifier(random_state=42)
dt_default.fit(X_train, y_train)

y_train_pred_dt = dt_default.predict(X_train)
y_test_pred_dt = dt_default.predict(X_test)

train_acc_dt = accuracy_score(y_train, y_train_pred_dt)
test_acc_dt = accuracy_score(y_test, y_test_pred_dt)

print(f"Training Accuracy: {train_acc_dt:.4f}")
print(f"Test Accuracy: {test_acc_dt:.4f}")

if train_acc_dt > test_acc_dt + 0.1:
    print("\n⚠️ Large gap indicates overfitting!")
    print("⚠️ الفجوة الكبيرة تشير إلى الإفراط في التلائم!")

# 2. Decision Tree - Pruned (with max_depth)
print("\n" + "=" * 60)
print("2. Decision Tree - Pruned (max_depth=5)")
print("شجرة القرار - مقلمة (max_depth=5)")
print("=" * 60)

dt_pruned = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_pruned.fit(X_train, y_train)

y_train_pred_pruned = dt_pruned.predict(X_train)
y_test_pred_pruned = dt_pruned.predict(X_test)

train_acc_pruned = accuracy_score(y_train, y_train_pred_pruned)
test_acc_pruned = accuracy_score(y_test, y_test_pred_pruned)

print(f"Training Accuracy: {train_acc_pruned:.4f}")
print(f"Test Accuracy: {test_acc_pruned:.4f}")

# 3. Random Forest
print("\n" + "=" * 60)
print("3. Random Forest")
print("الغابة العشوائية")
print("=" * 60)

rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

y_train_pred_rf = rf.predict(X_train)
y_test_pred_rf = rf.predict(X_test)

train_acc_rf = accuracy_score(y_train, y_train_pred_rf)
test_acc_rf = accuracy_score(y_test, y_test_pred_rf)

print(f"Training Accuracy: {train_acc_rf:.4f}")
print(f"Test Accuracy: {test_acc_rf:.4f}")

# Probability predictions for ROC curve
y_test_proba_rf = rf.predict_proba(X_test)[:, 1]

# 4. Model Comparison
print("\n" + "=" * 60)
print("4. Model Comparison")
print("مقارنة النماذج")
print("=" * 60)

comparison = pd.DataFrame({
    'Model': ['Decision Tree (Default)', 'Decision Tree (Pruned)', 'Random Forest'],
    'Train Accuracy': [train_acc_dt, train_acc_pruned, train_acc_rf],
    'Test Accuracy': [test_acc_dt, test_acc_pruned, test_acc_rf],
    'Overfitting Gap': [
        train_acc_dt - test_acc_dt,
        train_acc_pruned - test_acc_pruned,
        train_acc_rf - test_acc_rf
    ]
})

print("\nModel Comparison:")
print(comparison.to_string(index=False))

# 5. Feature Importance
print("\n" + "=" * 60)
print("5. Feature Importance")
print("أهمية الميزات")
print("=" * 60)

feature_importance_dt = pd.DataFrame({
    'Feature': X_data.columns,
    'Importance_DT': dt_pruned.feature_importances_,
    'Importance_RF': rf.feature_importances_
}).sort_values('Importance_RF', ascending=False)

print("\nTop 5 Most Important Features (Random Forest):")
print("أهم 5 ميزات (الغابة العشوائية):")
print(feature_importance_dt.head().to_string(index=False))

# Visualize feature importance
plt.figure(figsize=(12, 6))
x_pos = np.arange(len(feature_importance_dt))
width = 0.35

plt.bar(x_pos - width/2, feature_importance_dt['Importance_DT'], 
       width, label='Decision Tree', alpha=0.8)
plt.bar(x_pos + width/2, feature_importance_dt['Importance_RF'], 
       width, label='Random Forest', alpha=0.8)

plt.xlabel('Features')
plt.ylabel('Importance')
plt.title('Feature Importance Comparison')
plt.xticks(x_pos, feature_importance_dt['Feature'], rotation=45)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('feature_importance_trees.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'feature_importance_trees.png'")
plt.close()

# 6. Confusion Matrices
print("\n" + "=" * 60)
print("6. Confusion Matrices")
print("مصفوفات الارتباك")
print("=" * 60)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

models_to_plot = [
    (dt_default, 'Decision Tree (Default)', y_test_pred_dt),
    (dt_pruned, 'Decision Tree (Pruned)', y_test_pred_pruned),
    (rf, 'Random Forest', y_test_pred_rf)
]

for idx, (model, title, predictions) in enumerate(models_to_plot):
    cm = confusion_matrix(y_test, predictions)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                xticklabels=['Class 0', 'Class 1'],
                yticklabels=['Class 0', 'Class 1'])
    axes[idx].set_xlabel('Predicted')
    axes[idx].set_ylabel('Actual')
    axes[idx].set_title(title)

plt.tight_layout()
plt.savefig('confusion_matrices_trees.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'confusion_matrices_trees.png'")
plt.close()

# 7. ROC Curve Comparison
print("\n" + "=" * 60)
print("7. ROC Curve Comparison")
print("مقارنة منحنى ROC")
print("=" * 60)

# Get probabilities for all models
y_test_proba_dt = dt_default.predict_proba(X_test)[:, 1]
y_test_proba_pruned = dt_pruned.predict_proba(X_test)[:, 1]

# Calculate ROC curves
fpr_dt, tpr_dt, _ = roc_curve(y_test, y_test_proba_dt)
fpr_pruned, tpr_pruned, _ = roc_curve(y_test, y_test_proba_pruned)
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_test_proba_rf)

# Calculate AUC scores
auc_dt = roc_auc_score(y_test, y_test_proba_dt)
auc_pruned = roc_auc_score(y_test, y_test_proba_pruned)
auc_rf = roc_auc_score(y_test, y_test_proba_rf)

print(f"\nAUC Scores:")
print(f"Decision Tree (Default): {auc_dt:.4f}")
print(f"Decision Tree (Pruned): {auc_pruned:.4f}")
print(f"Random Forest: {auc_rf:.4f}")

# Plot ROC curves
plt.figure(figsize=(10, 8))
plt.plot(fpr_dt, tpr_dt, linewidth=2, label=f'DT Default (AUC = {auc_dt:.4f})')
plt.plot(fpr_pruned, tpr_pruned, linewidth=2, label=f'DT Pruned (AUC = {auc_pruned:.4f})')
plt.plot(fpr_rf, tpr_rf, linewidth=2, label=f'Random Forest (AUC = {auc_rf:.4f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('roc_curve_trees.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'roc_curve_trees.png'")
plt.close()

# 8. Effect of Tree Depth
print("\n" + "=" * 60)
print("8. Effect of Tree Depth on Performance")
print("تأثير عمق الشجرة على الأداء")
print("=" * 60)

max_depths = range(1, 16)
train_scores = []
test_scores = []

for depth in max_depths:
    dt_temp = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt_temp.fit(X_train, y_train)
    train_scores.append(accuracy_score(y_train, dt_temp.predict(X_train)))
    test_scores.append(accuracy_score(y_test, dt_temp.predict(X_test)))

# Plot learning curve
plt.figure(figsize=(10, 6))
plt.plot(max_depths, train_scores, 'o-', label='Training Accuracy', linewidth=2)
plt.plot(max_depths, test_scores, 's-', label='Test Accuracy', linewidth=2)
plt.xlabel('Max Depth')
plt.ylabel('Accuracy')
plt.title('Decision Tree: Depth vs Performance')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('tree_depth_effect.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'tree_depth_effect.png'")
plt.close()

# Find optimal depth
optimal_depth = max_depths[np.argmax(test_scores)]
print(f"\nOptimal Max Depth: {optimal_depth}")
print(f"Best Test Accuracy: {max(test_scores):.4f}")

print("\n" + "=" * 60)
print("Example 2 Complete! ✓")
print("اكتمل المثال 2! ✓")
print("=" * 60)

