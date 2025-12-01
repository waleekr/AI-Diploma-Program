"""
Unit 2 - Example 2: Cross-Validation for Model Evaluation
تقنيات الانحدار المتقدمة - مثال 2: التحقق المتقاطع لتقييم النماذج

This example demonstrates:
1. K-Fold Cross-Validation
2. Stratified K-Fold
3. Leave-One-Out Cross-Validation
4. Cross-validation for model selection
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import (KFold, StratifiedKFold, LeaveOneOut,
                                    cross_val_score, cross_validate)
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, make_scorer

print("=" * 60)
print("Example 2: Cross-Validation for Model Evaluation")
print("مثال 2: التحقق المتقاطع لتقييم النماذج")
print("=" * 60)

# Generate sample data
# إنشاء بيانات نموذجية
np.random.seed(42)
n_samples = 200

X = np.random.randn(n_samples, 5)
y = (2 * X[:, 0] + 1.5 * X[:, 1] - X[:, 2] + 
     3 * X[:, 3] + np.random.normal(0, 0.5, n_samples))

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
df['target'] = y

print(f"\nData Shape: {df.shape}")
print(df.head())

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 1. Simple Train-Test Split (Baseline)
print("\n" + "=" * 60)
print("1. Simple Train-Test Split (Baseline)")
print("التقسيم البسيط تدريب-اختبار (خط الأساس)")
print("=" * 60)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model_simple = LinearRegression()
model_simple.fit(X_train, y_train)
y_pred = model_simple.predict(X_test)

mse_simple = mean_squared_error(y_test, y_pred)
r2_simple = r2_score(y_test, y_pred)

print(f"Test MSE: {mse_simple:.4f}")
print(f"Test R²: {r2_simple:.4f}")

# 2. K-Fold Cross-Validation
print("\n" + "=" * 60)
print("2. K-Fold Cross-Validation")
print("التحقق المتقاطع K-Fold")
print("=" * 60)

kfold = KFold(n_splits=5, shuffle=True, random_state=42)

model_kfold = LinearRegression()

# Perform cross-validation
cv_scores_mse = cross_val_score(model_kfold, X_scaled, y, 
                                cv=kfold, scoring='neg_mean_squared_error')
cv_scores_r2 = cross_val_score(model_kfold, X_scaled, y, 
                               cv=kfold, scoring='r2')

print(f"\n5-Fold Cross-Validation Results:")
print(f"نتائج التحقق المتقاطع 5-Fold:")

print("\nMSE Scores (negative):")
for i, score in enumerate(cv_scores_mse):
    print(f"  Fold {i+1}: {-score:.4f}")

print("\nR² Scores:")
for i, score in enumerate(cv_scores_r2):
    print(f"  Fold {i+1}: {score:.4f}")

print(f"\nMean MSE: {-cv_scores_mse.mean():.4f} (+/- {cv_scores_mse.std() * 2:.4f})")
print(f"Mean R²: {cv_scores_r2.mean():.4f} (+/- {cv_scores_r2.std() * 2:.4f})")

# 3. Cross-Validate with Multiple Metrics
print("\n" + "=" * 60)
print("3. Cross-Validate with Multiple Metrics")
print("التحقق المتقاطع بمقاييس متعددة")
print("=" * 60)

scoring = {
    'mse': 'neg_mean_squared_error',
    'mae': 'neg_mean_absolute_error',
    'r2': 'r2'
}

cv_results = cross_validate(model_kfold, X_scaled, y, 
                           cv=kfold, scoring=scoring, return_train_score=True)

print("\nCross-Validation Results (Multiple Metrics):")
print("نتائج التحقق المتقاطع (مقاييس متعددة):")

print(f"\nTest MSE: {-cv_results['test_mse'].mean():.4f} (+/- {cv_results['test_mse'].std() * 2:.4f})")
print(f"Test MAE: {-cv_results['test_mae'].mean():.4f} (+/- {cv_results['test_mae'].std() * 2:.4f})")
print(f"Test R²: {cv_results['test_r2'].mean():.4f} (+/- {cv_results['test_r2'].std() * 2:.4f})")

# 4. Comparing Different Models with Cross-Validation
print("\n" + "=" * 60)
print("4. Comparing Different Models with Cross-Validation")
print("مقارنة نماذج مختلفة باستخدام التحقق المتقاطع")
print("=" * 60)

models = {
    'Linear Regression': LinearRegression(),
    'Ridge (α=1)': Ridge(alpha=1.0),
    'Ridge (α=10)': Ridge(alpha=10.0),
    'Lasso (α=0.1)': Lasso(alpha=0.1),
    'Lasso (α=1)': Lasso(alpha=1.0)
}

results = []

for name, model in models.items():
    cv_scores = cross_val_score(model, X_scaled, y, 
                                cv=kfold, scoring='neg_mean_squared_error')
    results.append({
        'Model': name,
        'Mean MSE': -cv_scores.mean(),
        'Std MSE': cv_scores.std(),
        'Mean R²': cross_val_score(model, X_scaled, y, cv=kfold, scoring='r2').mean()
    })

results_df = pd.DataFrame(results)
print("\nModel Comparison:")
print(results_df.to_string(index=False))

# Find best model
best_model_name = results_df.loc[results_df['Mean MSE'].idxmin(), 'Model']
print(f"\nBest Model (lowest MSE): {best_model_name}")

# 5. K-Fold Visualization
print("\n" + "=" * 60)
print("5. K-Fold Visualization")
print("تصور K-Fold")
print("=" * 60)

# Visualize K-Fold splits
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.ravel()

kfold_viz = KFold(n_splits=5, shuffle=True, random_state=42)

for fold_idx, (train_idx, val_idx) in enumerate(kfold_viz.split(X_scaled)):
    ax = axes[fold_idx]
    
    # Plot training data
    ax.scatter(X_scaled[train_idx, 0], X_scaled[train_idx, 1], 
              alpha=0.5, label='Train', s=30)
    # Plot validation data
    ax.scatter(X_scaled[val_idx, 0], X_scaled[val_idx, 1], 
              alpha=0.8, label='Validation', s=50, marker='x')
    
    ax.set_title(f'Fold {fold_idx + 1}')
    ax.set_xlabel('Feature 0')
    ax.set_ylabel('Feature 1')
    ax.legend()
    ax.grid(True, alpha=0.3)

axes[-1].axis('off')
plt.tight_layout()
plt.savefig('kfold_visualization.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'kfold_visualization.png'")
plt.close()

# 6. Leave-One-Out Cross-Validation (LOOCV)
print("\n" + "=" * 60)
print("6. Leave-One-Out Cross-Validation (LOOCV)")
print("التحقق المتقاطع بإخراج واحد (LOOCV)")
print("=" * 60)

print("\nNote: LOOCV is computationally expensive for large datasets")
print("ملاحظة: LOOCV مكلف حسابياً لمجموعات البيانات الكبيرة")

# Use smaller sample for demonstration
X_small = X_scaled[:50]
y_small = y[:50]

loocv = LeaveOneOut()
loocv_scores = cross_val_score(LinearRegression(), X_small, y_small, 
                               cv=loocv, scoring='r2')

print(f"\nLOOCV Results (n={len(y_small)}):")
print(f"Mean R²: {loocv_scores.mean():.4f}")
print(f"Std R²: {loocv_scores.std():.4f}")
print(f"Min R²: {loocv_scores.min():.4f}")
print(f"Max R²: {loocv_scores.max():.4f}")

# 7. Cross-Validation Score Distribution
print("\n" + "=" * 60)
print("7. Cross-Validation Score Distribution")
print("توزيع نتائج التحقق المتقاطع")
print("=" * 60)

# Get scores for all folds
all_scores = []
for train_idx, val_idx in kfold.split(X_scaled):
    model_temp = LinearRegression()
    model_temp.fit(X_scaled[train_idx], y[train_idx])
    pred = model_temp.predict(X_scaled[val_idx])
    score = r2_score(y[val_idx], pred)
    all_scores.append(score)

# Visualize score distribution
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(all_scores) + 1), all_scores, alpha=0.7, edgecolor='black')
plt.axhline(np.mean(all_scores), color='r', linestyle='--', 
           label=f'Mean: {np.mean(all_scores):.4f}')
plt.xlabel('Fold Number')
plt.ylabel('R² Score')
plt.title('Cross-Validation Score Distribution')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('cv_score_distribution.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'cv_score_distribution.png'")
plt.close()

print("\n" + "=" * 60)
print("Example 2 Complete! ✓")
print("اكتمل المثال 2! ✓")
print("=" * 60)

