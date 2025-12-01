"""
Unit 1 - Example 5: Polynomial Regression
أساليب معالجة البيانات - مثال 5: الانحدار متعدد الحدود

This example demonstrates:
1. Polynomial Regression for non-linear relationships
2. Choosing optimal polynomial degree
3. Overfitting vs Underfitting
4. Visual comparison of different degrees
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

plt.style.use('seaborn-v0_8')

print("=" * 60)
print("Example 5: Polynomial Regression")
print("مثال 5: الانحدار متعدد الحدود")
print("=" * 60)

# 1. Generate Non-Linear Data
# إنشاء بيانات غير خطية
print("\n1. Generating non-linear data...")
print("إنشاء بيانات غير خطية...")

np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
# Non-linear relationship: y = x^2 + noise
y = 0.5 * X.ravel()**2 - 2 * X.ravel() + 3 + np.random.normal(0, 2, 100)

df = pd.DataFrame({'X': X.ravel(), 'y': y})
print(f"Data shape: {df.shape}")
print(df.head())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Linear Regression (for comparison)
# الانحدار الخطي (للمقارنة)
print("\n" + "=" * 60)
print("2. Linear Regression (Baseline)")
print("الانحدار الخطي (خط الأساس)")
print("=" * 60)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
y_pred_linear = linear_model.predict(X_test)

linear_mse = mean_squared_error(y_test, y_pred_linear)
linear_r2 = r2_score(y_test, y_pred_linear)

print(f"MSE: {linear_mse:.4f}")
print(f"R² Score: {linear_r2:.4f}")

# 3. Polynomial Regression - Degree 2
# الانحدار متعدد الحدود - الدرجة 2
print("\n" + "=" * 60)
print("3. Polynomial Regression - Degree 2")
print("الانحدار متعدد الحدود - الدرجة 2")
print("=" * 60)

poly_features_2 = PolynomialFeatures(degree=2)
X_train_poly_2 = poly_features_2.fit_transform(X_train)
X_test_poly_2 = poly_features_2.transform(X_test)

poly_model_2 = LinearRegression()
poly_model_2.fit(X_train_poly_2, y_train)
y_pred_poly_2 = poly_model_2.predict(X_test_poly_2)

poly2_mse = mean_squared_error(y_test, y_pred_poly_2)
poly2_r2 = r2_score(y_test, y_pred_poly_2)

print(f"MSE: {poly2_mse:.4f}")
print(f"R² Score: {poly2_r2:.4f}")
print(f"\nModel coefficients: {poly_model_2.coef_}")
print(f"Intercept: {poly_model_2.intercept_:.4f}")

# 4. Polynomial Regression - Degree 3
# الانحدار متعدد الحدود - الدرجة 3
print("\n" + "=" * 60)
print("4. Polynomial Regression - Degree 3")
print("الانحدار متعدد الحدود - الدرجة 3")
print("=" * 60)

poly_features_3 = PolynomialFeatures(degree=3)
X_train_poly_3 = poly_features_3.fit_transform(X_train)
X_test_poly_3 = poly_features_3.transform(X_test)

poly_model_3 = LinearRegression()
poly_model_3.fit(X_train_poly_3, y_train)
y_pred_poly_3 = poly_model_3.predict(X_test_poly_3)

poly3_mse = mean_squared_error(y_test, y_pred_poly_3)
poly3_r2 = r2_score(y_test, y_pred_poly_3)

print(f"MSE: {poly3_mse:.4f}")
print(f"R² Score: {poly3_r2:.4f}")

# 5. Polynomial Regression - Degree 10 (Overfitting Example)
# الانحدار متعدد الحدود - الدرجة 10 (مثال على الإفراط في التلائم)
print("\n" + "=" * 60)
print("5. Polynomial Regression - Degree 10 (Overfitting)")
print("الانحدار متعدد الحدود - الدرجة 10 (الإفراط في التلائم)")
print("=" * 60)

poly_features_10 = PolynomialFeatures(degree=10)
X_train_poly_10 = poly_features_10.fit_transform(X_train)
X_test_poly_10 = poly_features_10.transform(X_test)

poly_model_10 = LinearRegression()
poly_model_10.fit(X_train_poly_10, y_train)
y_pred_poly_10 = poly_model_10.predict(X_test_poly_10)

# Training metrics (will be very good)
train_pred_10 = poly_model_10.predict(X_train_poly_10)
train_mse_10 = mean_squared_error(y_train, train_pred_10)
train_r2_10 = r2_score(y_train, train_pred_10)

# Test metrics (will be worse)
poly10_mse = mean_squared_error(y_test, y_pred_poly_10)
poly10_r2 = r2_score(y_test, y_pred_poly_10)

print(f"Training MSE: {train_mse_10:.4f}")
print(f"Training R²: {train_r2_10:.4f}")
print(f"Test MSE: {poly10_mse:.4f}")
print(f"Test R²: {poly10_r2:.4f}")
print("\n⚠️ Notice: Large gap between train and test indicates overfitting!")
print("⚠️ لاحظ: الفجوة الكبيرة بين التدريب والاختبار تشير إلى الإفراط في التلائم!")

# 6. Comparison Table
# جدول المقارنة
print("\n" + "=" * 60)
print("6. Model Comparison")
print("مقارنة النماذج")
print("=" * 60)

comparison = pd.DataFrame({
    'Model': ['Linear', 'Polynomial (deg=2)', 'Polynomial (deg=3)', 'Polynomial (deg=10)'],
    'Test MSE': [linear_mse, poly2_mse, poly3_mse, poly10_mse],
    'Test R²': [linear_r2, poly2_r2, poly3_r2, poly10_r2]
})

print("\nComparison Table:")
print(comparison.to_string(index=False))

# 7. Visualization
# التصور
print("\n" + "=" * 60)
print("7. Visualization")
print("التصور")
print("=" * 60)

# Create smooth line for plotting
X_plot = np.linspace(0, 10, 200).reshape(-1, 1)

# Predictions for plotting
y_plot_linear = linear_model.predict(X_plot)

X_plot_poly_2 = poly_features_2.transform(X_plot)
y_plot_poly_2 = poly_model_2.predict(X_plot_poly_2)

X_plot_poly_3 = poly_features_3.transform(X_plot)
y_plot_poly_3 = poly_model_3.predict(X_plot_poly_3)

X_plot_poly_10 = poly_features_10.transform(X_plot)
y_plot_poly_10 = poly_model_10.predict(X_plot_poly_10)

# Plot all models
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Linear
axes[0, 0].scatter(X_test, y_test, alpha=0.6, label='Test Data', color='blue')
axes[0, 0].plot(X_plot, y_plot_linear, 'r-', linewidth=2, label='Linear Regression')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('y')
axes[0, 0].set_title(f'Linear Regression (R² = {linear_r2:.4f})')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Degree 2
axes[0, 1].scatter(X_test, y_test, alpha=0.6, label='Test Data', color='blue')
axes[0, 1].plot(X_plot, y_plot_poly_2, 'g-', linewidth=2, label='Polynomial (deg=2)')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('y')
axes[0, 1].set_title(f'Polynomial Regression - Degree 2 (R² = {poly2_r2:.4f})')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Degree 3
axes[1, 0].scatter(X_test, y_test, alpha=0.6, label='Test Data', color='blue')
axes[1, 0].plot(X_plot, y_plot_poly_3, 'orange', linewidth=2, label='Polynomial (deg=3)')
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('y')
axes[1, 0].set_title(f'Polynomial Regression - Degree 3 (R² = {poly3_r2:.4f})')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Degree 10 (Overfitting)
axes[1, 1].scatter(X_test, y_test, alpha=0.6, label='Test Data', color='blue')
axes[1, 1].plot(X_plot, y_plot_poly_10, 'purple', linewidth=2, label='Polynomial (deg=10)')
axes[1, 1].set_xlabel('X')
axes[1, 1].set_ylabel('y')
axes[1, 1].set_title(f'Polynomial Regression - Degree 10 (R² = {poly10_r2:.4f})\n⚠️ Overfitting')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('polynomial_regression_comparison.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'polynomial_regression_comparison.png'")
plt.close()

# 8. Finding Optimal Degree
# إيجاد الدرجة المثلى
print("\n" + "=" * 60)
print("8. Finding Optimal Polynomial Degree")
print("إيجاد الدرجة المثلى لمتعدد الحدود")
print("=" * 60)

degrees = range(1, 11)
train_scores = []
test_scores = []

for degree in degrees:
    poly_features = PolynomialFeatures(degree=degree)
    X_train_poly = poly_features.fit_transform(X_train)
    X_test_poly = poly_features.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    train_pred = model.predict(X_train_poly)
    test_pred = model.predict(X_test_poly)
    
    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)
    
    train_scores.append(train_r2)
    test_scores.append(test_r2)

# Find optimal degree (best test score)
optimal_degree = degrees[np.argmax(test_scores)]
print(f"\nOptimal Degree: {optimal_degree}")
print(f"الدرجة المثلى: {optimal_degree}")
print(f"Best Test R²: {max(test_scores):.4f}")

# Plot degree vs R² score
plt.figure(figsize=(10, 6))
plt.plot(degrees, train_scores, 'o-', label='Training R²', linewidth=2, markersize=8)
plt.plot(degrees, test_scores, 's-', label='Test R²', linewidth=2, markersize=8)
plt.axvline(optimal_degree, color='r', linestyle='--', label=f'Optimal Degree = {optimal_degree}')
plt.xlabel('Polynomial Degree')
plt.ylabel('R² Score')
plt.title('Finding Optimal Polynomial Degree')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('optimal_polynomial_degree.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'optimal_polynomial_degree.png'")
plt.close()

print("\n" + "=" * 60)
print("Example 5 Complete! ✓")
print("اكتمل المثال 5! ✓")
print("=" * 60)

