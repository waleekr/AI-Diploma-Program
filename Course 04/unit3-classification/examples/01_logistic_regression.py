"""
Unit 3 - Example 1: Logistic Regression and Classification Metrics
تقنيات التصنيف المتقدمة - مثال 1: الانحدار اللوجستي ومقاييس التصنيف

This example demonstrates:
1. Logistic Regression for binary classification
2. Classification evaluation metrics
3. Confusion Matrix
4. ROC Curve and AUC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                            f1_score, confusion_matrix, classification_report,
                            roc_curve, roc_auc_score)

print("=" * 60)
print("Example 1: Logistic Regression and Classification Metrics")
print("مثال 1: الانحدار اللوجستي ومقاييس التصنيف")
print("=" * 60)

# Generate sample binary classification data
# إنشاء بيانات تصنيف ثنائية نموذجية
np.random.seed(42)
n_samples = 500

# Features
X1 = np.random.normal(2, 1.5, n_samples)
X2 = np.random.normal(3, 1.5, n_samples)

# Combine features
X = np.column_stack([X1, X2])

# Create target (binary): based on decision boundary
# إنشاء الهدف (ثنائي): بناءً على حدود القرار
y = ((X1 - 2)**2 + (X2 - 3)**2 < 4).astype(int)
y = y + np.random.binomial(1, 0.1, n_samples)  # Add noise
y = np.clip(y, 0, 1)  # Ensure binary

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

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Train Logistic Regression Model
print("\n" + "=" * 60)
print("1. Training Logistic Regression Model")
print("تدريب نموذج الانحدار اللوجستي")
print("=" * 60)

logistic_model = LogisticRegression(random_state=42, max_iter=1000)
logistic_model.fit(X_train_scaled, y_train)

# Make predictions
y_train_pred = logistic_model.predict(X_train_scaled)
y_test_pred = logistic_model.predict(X_test_scaled)

# Probability predictions
y_train_proba = logistic_model.predict_proba(X_train_scaled)[:, 1]
y_test_proba = logistic_model.predict_proba(X_test_scaled)[:, 1]

print("Model trained successfully!")
print(f"Coefficients: {logistic_model.coef_[0]}")
print(f"Intercept: {logistic_model.intercept_[0]:.4f}")

# 2. Evaluation Metrics
print("\n" + "=" * 60)
print("2. Evaluation Metrics")
print("مقاييس التقييم")
print("=" * 60)

# Accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

# Precision
train_precision = precision_score(y_train, y_train_pred)
test_precision = precision_score(y_test, y_test_pred)

# Recall
train_recall = recall_score(y_train, y_train_pred)
test_recall = recall_score(y_test, y_test_pred)

# F1 Score
train_f1 = f1_score(y_train, y_train_pred)
test_f1 = f1_score(y_test, y_test_pred)

print("\nTraining Metrics:")
print(f"  Accuracy:  {train_accuracy:.4f}")
print(f"  Precision: {train_precision:.4f}")
print(f"  Recall:    {train_recall:.4f}")
print(f"  F1 Score:  {train_f1:.4f}")

print("\nTest Metrics:")
print(f"  Accuracy:  {test_accuracy:.4f}")
print(f"  Precision: {test_precision:.4f}")
print(f"  Recall:    {test_recall:.4f}")
print(f"  F1 Score:  {test_f1:.4f}")

# Classification Report
print("\nClassification Report (Test Set):")
print(classification_report(y_test, y_test_pred, 
                          target_names=['Class 0', 'Class 1']))

# 3. Confusion Matrix
print("\n" + "=" * 60)
print("3. Confusion Matrix")
print("مصفوفة الارتباك")
print("=" * 60)

cm = confusion_matrix(y_test, y_test_pred)
print("\nConfusion Matrix:")
print(cm)

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Class 0', 'Class 1'],
            yticklabels=['Class 0', 'Class 1'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'confusion_matrix.png'")
plt.close()

# 4. ROC Curve and AUC
print("\n" + "=" * 60)
print("4. ROC Curve and AUC")
print("منحنى ROC و AUC")
print("=" * 60)

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_test_proba)
auc_score = roc_auc_score(y_test, y_test_proba)

print(f"\nAUC Score: {auc_score:.4f}")

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, linewidth=2, label=f'ROC Curve (AUC = {auc_score:.4f})')
plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('roc_curve.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'roc_curve.png'")
plt.close()

# 5. Decision Boundary Visualization
print("\n" + "=" * 60)
print("5. Decision Boundary Visualization")
print("تصور حدود القرار")
print("=" * 60)

# Create a mesh
h = 0.02
x_min, x_max = X_test_scaled[:, 0].min() - 1, X_test_scaled[:, 0].max() + 1
y_min, y_max = X_test_scaled[:, 1].min() - 1, X_test_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Predict for mesh points
Z = logistic_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='RdYlBu')
scatter = plt.scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], 
                     c=y_test, cmap='RdYlBu', edgecolors='black', s=50)
plt.colorbar(scatter)
plt.xlabel('Feature 1 (Scaled)')
plt.ylabel('Feature 2 (Scaled)')
plt.title('Decision Boundary and Test Data')
plt.tight_layout()
plt.savefig('decision_boundary.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'decision_boundary.png'")
plt.close()

print("\n" + "=" * 60)
print("Example 1 Complete! ✓")
print("اكتمل المثال 1! ✓")
print("=" * 60)

