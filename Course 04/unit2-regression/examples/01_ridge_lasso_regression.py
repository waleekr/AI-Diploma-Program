"""
Unit 2 - Example 1: Ridge and Lasso Regression
تقنيات الانحدار المتقدمة - مثال 1: الانحدار ريدج ولاسو

This example demonstrates:
1. Ridge Regression (L2 regularization)
2. Lasso Regression (L1 regularization)
3. Comparison with Linear Regression
4. Hyperparameter tuning (alpha)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 60)
print("Example 1: Ridge and Lasso Regression")
print("مثال 1: الانحدار ريدج ولاسو")
print("=" * 60)

# Generate sample data with multicollinearity
# إنشاء بيانات نموذجية مع ارتباط متعدد
np.random.seed(42)
n_samples = 200

# Create features with some correlation
X = np.random.randn(n_samples, 10)
# Make some features correlated
X[:, 2] = X[:, 0] + 0.5 * np.random.randn(n_samples)
X[:, 3] = X[:, 1] + 0.5 * np.random.randn(n_samples)

# Target with noise
y = (2 * X[:, 0] + 1.5 * X[:, 1] - 1 * X[:, 2] + 
     3 * X[:, 3] + np.random.normal(0, 0.5, n_samples))

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])
df['target'] = y

print(f"\nData Shape: {df.shape}")
print(df.head())

# Split data
X_data = df.drop('target', axis=1)
y_data = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42
)

# Scale features (important for regularization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. Linear Regression (Baseline)
print("\n" + "=" * 60)
print("1. Linear Regression (Baseline)")
print("الانحدار الخطي (خط الأساس)")
print("=" * 60)

lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
lr_pred = lr.predict(X_test_scaled)

lr_mse = mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

print(f"MSE: {lr_mse:.4f}")
print(f"R² Score: {lr_r2:.4f}")
print(f"\nCoefficients: {lr.coef_[:5]}...")  # Show first 5

# 2. Ridge Regression (L2 Regularization)
print("\n" + "=" * 60)
print("2. Ridge Regression (L2 Regularization)")
print("الانحدار ريدج (التنظيم L2)")
print("=" * 60)

# Try different alpha values
alphas = [0.01, 0.1, 1.0, 10.0, 100.0]
ridge_results = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train_scaled, y_train)
    ridge_pred = ridge.predict(X_test_scaled)
    
    mse = mean_squared_error(y_test, ridge_pred)
    r2 = r2_score(y_test, ridge_pred)
    
    ridge_results.append({
        'alpha': alpha,
        'mse': mse,
        'r2': r2,
        'model': ridge
    })

# Find best alpha
best_ridge = min(ridge_results, key=lambda x: x['mse'])
print(f"\nBest Alpha: {best_ridge['alpha']}")
print(f"Best MSE: {best_ridge['mse']:.4f}")
print(f"Best R²: {best_ridge['r2']:.4f}")

# 3. Lasso Regression (L1 Regularization)
print("\n" + "=" * 60)
print("3. Lasso Regression (L1 Regularization)")
print("الانحدار لاسو (التنظيم L1)")
print("=" * 60)

lasso_results = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train_scaled, y_train)
    lasso_pred = lasso.predict(X_test_scaled)
    
    mse = mean_squared_error(y_test, lasso_pred)
    r2 = r2_score(y_test, lasso_pred)
    n_features = np.sum(np.abs(lasso.coef_) > 0.01)  # Non-zero coefficients
    
    lasso_results.append({
        'alpha': alpha,
        'mse': mse,
        'r2': r2,
        'n_features': n_features,
        'model': lasso
    })

# Find best alpha
best_lasso = min(lasso_results, key=lambda x: x['mse'])
print(f"\nBest Alpha: {best_lasso['alpha']}")
print(f"Best MSE: {best_lasso['mse']:.4f}")
print(f"Best R²: {best_lasso['r2']:.4f}")
print(f"Features used: {best_lasso['n_features']}/10")

# 4. Comparison
print("\n" + "=" * 60)
print("4. Model Comparison")
print("مقارنة النماذج")
print("=" * 60)

comparison = pd.DataFrame({
    'Model': ['Linear Regression', f'Ridge (α={best_ridge["alpha"]})', 
              f'Lasso (α={best_lasso["alpha"]})'],
    'Test MSE': [lr_mse, best_ridge['mse'], best_lasso['mse']],
    'Test R²': [lr_r2, best_ridge['r2'], best_lasso['r2']]
})

print("\nComparison Table:")
print(comparison.to_string(index=False))

# 5. Coefficient Comparison
print("\n" + "=" * 60)
print("5. Coefficient Comparison")
print("مقارنة المعاملات")
print("=" * 60)

coef_comparison = pd.DataFrame({
    'Feature': X_data.columns,
    'Linear': lr.coef_,
    'Ridge': best_ridge['model'].coef_,
    'Lasso': best_lasso['model'].coef_
})

print("\nCoefficient Comparison (first 5 features):")
print(coef_comparison.head().to_string(index=False))

print("\nLasso shrinks many coefficients to zero (feature selection)")
print("لاسو يقلص العديد من المعاملات إلى الصفر (اختيار الميزات)")

# 6. Visualization
print("\n" + "=" * 60)
print("6. Visualization")
print("التصور")
print("=" * 60)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Alpha vs MSE
axes[0].semilogx([r['alpha'] for r in ridge_results], 
                 [r['mse'] for r in ridge_results], 
                 'o-', label='Ridge', linewidth=2)
axes[0].semilogx([l['alpha'] for l in lasso_results], 
                 [l['mse'] for l in lasso_results], 
                 's-', label='Lasso', linewidth=2)
axes[0].axhline(lr_mse, color='r', linestyle='--', label='Linear Regression')
axes[0].set_xlabel('Alpha (Regularization Strength)')
axes[0].set_ylabel('Test MSE')
axes[0].set_title('Regularization vs Model Performance')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Coefficient magnitudes
axes[1].bar(range(10), np.abs(lr.coef_), alpha=0.7, label='Linear', width=0.25)
axes[1].bar([i + 0.25 for i in range(10)], np.abs(best_ridge['model'].coef_), 
            alpha=0.7, label='Ridge', width=0.25)
axes[1].bar([i + 0.5 for i in range(10)], np.abs(best_lasso['model'].coef_), 
            alpha=0.7, label='Lasso', width=0.25)
axes[1].set_xlabel('Feature Index')
axes[1].set_ylabel('Absolute Coefficient Value')
axes[1].set_title('Coefficient Comparison')
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('ridge_lasso_comparison.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'ridge_lasso_comparison.png'")
plt.close()

print("\n" + "=" * 60)
print("Example 1 Complete! ✓")
print("اكتمل المثال 1! ✓")
print("=" * 60)

