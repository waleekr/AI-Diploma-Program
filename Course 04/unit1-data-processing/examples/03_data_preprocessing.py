"""
Unit 1 - Example 3: Data Preprocessing
أساليب معالجة البيانات - مثال 3: المعالجة المسبقة للبيانات

This example demonstrates:
1. Feature scaling (Standardization, Normalization)
2. Encoding categorical variables (Label Encoding, One-Hot Encoding)
3. Train-test split
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

print("=" * 60)
print("Example 3: Data Preprocessing")
print("مثال 3: المعالجة المسبقة للبيانات")
print("=" * 60)

# Create sample data
# إنشاء بيانات نموذجية
print("\n1. Creating sample data...")
print("إنشاء بيانات نموذجية...")

np.random.seed(42)
data = {
    'age': np.random.randint(20, 60, 100),
    'salary': np.random.randint(30000, 100000, 100),
    'experience': np.random.uniform(0, 15, 100),
    'city': np.random.choice(['Riyadh', 'Jeddah', 'Dammam', 'Khobar'], 100),
    'education': np.random.choice(['Bachelor', 'Master', 'PhD'], 100),
    'target': np.random.choice([0, 1], 100)  # Binary target for classification
}

df = pd.DataFrame(data)
print("\nOriginal Data:")
print(df.head())
print(f"\nData Shape: {df.shape}")

# 2. Feature Scaling - Standardization (Z-score normalization)
# قياس الميزات - التوحيد المعياري
print("\n" + "=" * 60)
print("2. Feature Scaling - Standardization")
print("قياس الميزات - التوحيد المعياري")
print("=" * 60)

# Standardization: (x - mean) / std
# التوحيد المعياري: (x - المتوسط) / الانحراف المعياري
scaler_standard = StandardScaler()

# Select numeric columns for scaling
numeric_cols = ['age', 'salary', 'experience']
df_scaled_standard = df.copy()

# Fit and transform
df_scaled_standard[numeric_cols] = scaler_standard.fit_transform(df[numeric_cols])

print("\nAfter Standardization (mean=0, std=1):")
print("بعد التوحيد المعياري (متوسط=0، انحراف معياري=1):")
print(f"Age - Mean: {df_scaled_standard['age'].mean():.4f}, Std: {df_scaled_standard['age'].std():.4f}")
print(f"Salary - Mean: {df_scaled_standard['salary'].mean():.4f}, Std: {df_scaled_standard['salary'].std():.4f}")
print(df_scaled_standard[numeric_cols].head())

# 3. Feature Scaling - Normalization (Min-Max Scaling)
# قياس الميزات - التطبيع (قياس الأدنى-الأعلى)
print("\n" + "=" * 60)
print("3. Feature Scaling - Normalization (Min-Max)")
print("قياس الميزات - التطبيع (الأدنى-الأعلى)")
print("=" * 60)

# Normalization: (x - min) / (max - min) -> range [0, 1]
# التطبيع: (x - الأدنى) / (الأعلى - الأدنى) -> النطاق [0, 1]
scaler_minmax = MinMaxScaler()

df_scaled_minmax = df.copy()
df_scaled_minmax[numeric_cols] = scaler_minmax.fit_transform(df[numeric_cols])

print("\nAfter Min-Max Normalization (range 0-1):")
print("بعد التطبيع بالأدنى-الأعلى (النطاق 0-1):")
print(f"Age - Min: {df_scaled_minmax['age'].min():.4f}, Max: {df_scaled_minmax['age'].max():.4f}")
print(f"Salary - Min: {df_scaled_minmax['salary'].min():.4f}, Max: {df_scaled_minmax['salary'].max():.4f}")
print(df_scaled_minmax[numeric_cols].head())

# 4. Label Encoding (for ordinal categories)
# الترميز بالعلامات (للفئات الترتيبية)
print("\n" + "=" * 60)
print("4. Label Encoding")
print("الترميز بالعلامات")
print("=" * 60)

label_encoder = LabelEncoder()

# Encode education (if we assume ordinal: Bachelor < Master < PhD)
df_encoded = df.copy()
df_encoded['education_encoded'] = label_encoder.fit_transform(df['education'])

print("\nLabel Encoding for Education:")
print("الترميز بالعلامات للتعليم:")
print("Mapping / التعيين:")
for i, label in enumerate(label_encoder.classes_):
    print(f"  {label}: {i}")

print("\nEncoded values:")
print(df_encoded[['education', 'education_encoded']].head(10))

# 5. One-Hot Encoding (for nominal categories)
# الترميز الواحد-الساخن (للفئات الاسمية)
print("\n" + "=" * 60)
print("5. One-Hot Encoding")
print("الترميز الواحد-الساخن")
print("=" * 60)

# Using pandas get_dummies (easier)
# استخدام pandas get_dummies (أسهل)
df_onehot = pd.get_dummies(df, columns=['city', 'education'], prefix=['city', 'edu'])

print("\nOne-Hot Encoded columns:")
print("الأعمدة المشفرة بالواحد-الساخن:")
print(df_onehot.columns.tolist())
print("\nSample of One-Hot Encoded data:")
print(df_onehot[['age', 'salary'] + [col for col in df_onehot.columns if 'city_' in col or 'edu_' in col]].head())

# Using sklearn OneHotEncoder (for more control)
# استخدام sklearn OneHotEncoder (لمزيد من التحكم)
print("\n--- Using sklearn OneHotEncoder ---")
onehot_encoder = OneHotEncoder(sparse_output=False, drop='first')
city_encoded = onehot_encoder.fit_transform(df[['city']])

print("City encoding classes:")
print(onehot_encoder.categories_)
print(f"\nEncoded shape: {city_encoded.shape}")
print("First 5 encoded values:")
print(city_encoded[:5])

# 6. Train-Test Split
# تقسيم البيانات إلى تدريب واختبار
print("\n" + "=" * 60)
print("6. Train-Test Split")
print("تقسيم البيانات إلى تدريب واختبار")
print("=" * 60)

# Prepare features and target
X = df[['age', 'salary', 'experience']]
y = df['target']

# Split into train and test sets (80% train, 20% test)
# التقسيم إلى مجموعات تدريب واختبار (80% تدريب، 20% اختبار)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,
    stratify=y  # Maintain class distribution
)

print(f"\nOriginal data shape: {X.shape}")
print(f"شكل البيانات الأصلية: {X.shape}")

print(f"\nTraining set:")
print(f"مجموعة التدريب:")
print(f"  X_train: {X_train.shape}")
print(f"  y_train: {y_train.shape}")

print(f"\nTest set:")
print(f"مجموعة الاختبار:")
print(f"  X_test: {X_test.shape}")
print(f"  y_test: {y_test.shape}")

print(f"\nTrain percentage: {len(X_train) / len(X) * 100:.1f}%")
print(f"Test percentage: {len(X_test) / len(X) * 100:.1f}%")

# 7. Complete Preprocessing Pipeline Example
# مثال خط أنابيب المعالجة الكاملة
print("\n" + "=" * 60)
print("7. Complete Preprocessing Pipeline")
print("خط أنابيب المعالجة الكاملة")
print("=" * 60)

def preprocess_data(df, numeric_cols, categorical_cols, target_col, test_size=0.2):
    """
    Complete preprocessing pipeline
    خط أنابيب المعالجة الكاملة
    """
    # Separate features and target
    X = df[numeric_cols + categorical_cols].copy()
    y = df[target_col].copy()
    
    # One-hot encode categorical variables
    X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    # Scale numeric features
    scaler = StandardScaler()
    X_encoded[numeric_cols] = scaler.fit_transform(X_encoded[numeric_cols])
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y, test_size=test_size, random_state=42, stratify=y
    )
    
    return X_train, X_test, y_train, y_test, scaler

# Example usage
numeric_features = ['age', 'salary', 'experience']
categorical_features = ['city', 'education']

X_train_final, X_test_final, y_train_final, y_test_final, scaler_final = preprocess_data(
    df, numeric_features, categorical_features, 'target'
)

print("\nPreprocessed training data shape:")
print("شكل بيانات التدريب المعالجة:")
print(f"X_train: {X_train_final.shape}")
print(f"y_train: {y_train_final.shape}")

print("\nPreprocessed test data shape:")
print("شكل بيانات الاختبار المعالجة:")
print(f"X_test: {X_test_final.shape}")
print(f"y_test: {y_test_final.shape}")

print("\n" + "=" * 60)
print("Example 3 Complete! ✓")
print("اكتمل المثال 3! ✓")
print("=" * 60)

