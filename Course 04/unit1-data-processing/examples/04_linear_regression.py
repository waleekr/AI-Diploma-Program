"""
Unit 1 - Example 4: Linear Regression
أساليب معالجة البيانات - مثال 4: الانحدار الخطي

This example demonstrates:
1. Simple Linear Regression (one feature)
2. Multiple Linear Regression (multiple features)
3. Model evaluation metrics
4. Visualization of regression results
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set style for better plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=" * 60)
print("Example 4: Linear Regression")
print("مثال 4: الانحدار الخطي")
print("=" * 60)

# 1. Simple Linear Regression
# الانحدار الخطي البسيط
print("\n" + "=" * 60)
print("1. Simple Linear Regression (One Feature)")
print("الانحدار الخطي البسيط (ميزة واحدة)")
print("=" * 60)

# Generate sample data
# إنشاء بيانات نموذجية
np.random.seed(42)
house_size = np.linspace(1000, 4000, 100)
# Price = 50 * size + 100000 + noise
house_price = 50 * house_size + 100000 + np.random.normal(0, 30000, 100)

df_simple = pd.DataFrame({
    'size': house_size,
    'price': house_price
})

print("\nSample Data:")
print(df_simple.head())

# Prepare data
X = df_simple[['size']]
y = df_simple['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model_simple = LinearRegression()
model_simple.fit(X_train, y_train)

# Make predictions
y_train_pred = model_simple.predict(X_train)
y_test_pred = model_simple.predict(X_test)

# Model parameters
print("\nModel Parameters:")
print("معاملات النموذج:")
print(f"Intercept (bias): {model_simple.intercept_:.2f}")
print(f"Coefficient (slope): {model_simple.coef_[0]:.4f}")

# Evaluate model
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print("\nTraining Metrics:")
print("مقاييس التدريب:")
print(f"  MSE: {train_mse:,.2f}")
print(f"  MAE: {train_mae:,.2f}")
print(f"  R² Score: {train_r2:.4f}")

print("\nTest Metrics:")
print("مقاييس الاختبار:")
print(f"  MSE: {test_mse:,.2f}")
print(f"  MAE: {test_mae:,.2f}")
print(f"  R² Score: {test_r2:.4f}")

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Training data
axes[0].scatter(X_train, y_train, alpha=0.6, label='Training Data')
axes[0].plot(X_train, y_train_pred, 'r-', linewidth=2, label='Regression Line')
axes[0].set_xlabel('House Size (sq ft)')
axes[0].set_ylabel('Price ($)')
axes[0].set_title('Simple Linear Regression - Training Data')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Test data
axes[1].scatter(X_test, y_test, alpha=0.6, label='Test Data', color='green')
axes[1].plot(X_test, y_test_pred, 'r-', linewidth=2, label='Regression Line')
axes[1].set_xlabel('House Size (sq ft)')
axes[1].set_ylabel('Price ($)')
axes[1].set_title('Simple Linear Regression - Test Data')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('simple_linear_regression.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'simple_linear_regression.png'")
plt.close()

# 2. Multiple Linear Regression
# الانحدار الخطي المتعدد
print("\n" + "=" * 60)
print("2. Multiple Linear Regression (Multiple Features)")
print("الانحدار الخطي المتعدد (ميزات متعددة)")
print("=" * 60)

# Generate sample data with multiple features
np.random.seed(42)
n_samples = 200

data_multiple = {
    'size': np.random.uniform(1000, 4000, n_samples),
    'bedrooms': np.random.randint(2, 6, n_samples),
    'age': np.random.uniform(0, 30, n_samples),
    'location_score': np.random.uniform(1, 10, n_samples)
}

df_multiple = pd.DataFrame(data_multiple)

# Generate target: price based on multiple features
price = (50 * df_multiple['size'] + 
         30000 * df_multiple['bedrooms'] - 
         5000 * df_multiple['age'] + 
         15000 * df_multiple['location_score'] + 
         50000 + 
         np.random.normal(0, 40000, n_samples))

df_multiple['price'] = price

print("\nSample Data:")
print(df_multiple.head())

# Prepare data
X_multiple = df_multiple[['size', 'bedrooms', 'age', 'location_score']]
y_multiple = df_multiple['price']

# Split data
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multiple, y_multiple, test_size=0.2, random_state=42
)

# Create and train model
model_multiple = LinearRegression()
model_multiple.fit(X_train_m, y_train_m)

# Make predictions
y_train_pred_m = model_multiple.predict(X_train_m)
y_test_pred_m = model_multiple.predict(X_test_m)

# Model parameters
print("\nModel Parameters:")
print("معاملات النموذج:")
print(f"Intercept: {model_multiple.intercept_:.2f}")
print("\nCoefficients:")
print("المعاملات:")
for feature, coef in zip(X_multiple.columns, model_multiple.coef_):
    print(f"  {feature}: {coef:.4f}")

# Evaluate model
train_mse_m = mean_squared_error(y_train_m, y_train_pred_m)
test_mse_m = mean_squared_error(y_test_m, y_test_pred_m)
train_r2_m = r2_score(y_train_m, y_train_pred_m)
test_r2_m = r2_score(y_test_m, y_test_pred_m)

print("\nTraining Metrics:")
print("مقاييس التدريب:")
print(f"  MSE: {train_mse_m:,.2f}")
print(f"  RMSE: {np.sqrt(train_mse_m):,.2f}")
print(f"  R² Score: {train_r2_m:.4f}")

print("\nTest Metrics:")
print("مقاييس الاختبار:")
print(f"  MSE: {test_mse_m:,.2f}")
print(f"  RMSE: {np.sqrt(test_mse_m):,.2f}")
print(f"  R² Score: {test_r2_m:.4f}")

# Visualize predictions vs actual
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Training predictions
axes[0].scatter(y_train_m, y_train_pred_m, alpha=0.6)
axes[0].plot([y_train_m.min(), y_train_m.max()], 
             [y_train_m.min(), y_train_m.max()], 'r--', linewidth=2)
axes[0].set_xlabel('Actual Price ($)')
axes[0].set_ylabel('Predicted Price ($)')
axes[0].set_title(f'Training Set (R² = {train_r2_m:.4f})')
axes[0].grid(True, alpha=0.3)

# Test predictions
axes[1].scatter(y_test_m, y_test_pred_m, alpha=0.6, color='green')
axes[1].plot([y_test_m.min(), y_test_m.max()], 
             [y_test_m.min(), y_test_m.max()], 'r--', linewidth=2)
axes[1].set_xlabel('Actual Price ($)')
axes[1].set_ylabel('Predicted Price ($)')
axes[1].set_title(f'Test Set (R² = {test_r2_m:.4f})')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('multiple_linear_regression.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'multiple_linear_regression.png'")
plt.close()

# 3. Feature Importance (Coefficient Analysis)
# أهمية الميزات (تحليل المعاملات)
print("\n" + "=" * 60)
print("3. Feature Importance Analysis")
print("تحليل أهمية الميزات")
print("=" * 60)

feature_importance = pd.DataFrame({
    'Feature': X_multiple.columns,
    'Coefficient': model_multiple.coef_,
    'Abs_Coefficient': np.abs(model_multiple.coef_)
}).sort_values('Abs_Coefficient', ascending=False)

print("\nFeature Importance (by absolute coefficient):")
print("أهمية الميزات (حسب القيمة المطلقة للمعامل):")
print(feature_importance)

# Visualize coefficients
plt.figure(figsize=(10, 6))
sns.barplot(data=feature_importance, x='Coefficient', y='Feature', palette='viridis')
plt.title('Feature Coefficients in Multiple Linear Regression')
plt.xlabel('Coefficient Value')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'feature_importance.png'")
plt.close()

# 4. Residuals Analysis
# تحليل البواقي
print("\n" + "=" * 60)
print("4. Residuals Analysis")
print("تحليل البواقي")
print("=" * 60)

residuals = y_test_m - y_test_pred_m

print(f"\nResidual Statistics:")
print(f"إحصائيات البواقي:")
print(f"  Mean: {residuals.mean():.2f} (should be close to 0)")
print(f"  Std: {residuals.std():.2f}")
print(f"  Min: {residuals.min():.2f}")
print(f"  Max: {residuals.max():.2f}")

# Plot residuals
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Residuals distribution
axes[0].hist(residuals, bins=20, edgecolor='black', alpha=0.7)
axes[0].axvline(0, color='r', linestyle='--', linewidth=2)
axes[0].set_xlabel('Residuals')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Residuals Distribution')
axes[0].grid(True, alpha=0.3)

# Residuals vs Predicted
axes[1].scatter(y_test_pred_m, residuals, alpha=0.6)
axes[1].axhline(0, color='r', linestyle='--', linewidth=2)
axes[1].set_xlabel('Predicted Values')
axes[1].set_ylabel('Residuals')
axes[1].set_title('Residuals vs Predicted Values')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('residuals_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'residuals_analysis.png'")
plt.close()

print("\n" + "=" * 60)
print("Example 4 Complete! ✓")
print("اكتمل المثال 4! ✓")
print("=" * 60)

