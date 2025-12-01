"""
Unit 1 - Example 2: Data Cleaning
أساليب معالجة البيانات - مثال 2: تنظيف البيانات

This example demonstrates:
1. Handling missing values (removal, imputation)
2. Removing duplicates
3. Handling outliers
4. Data type conversion
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("Example 2: Data Cleaning")
print("مثال 2: تنظيف البيانات")
print("=" * 60)

# Create sample data with issues for demonstration
# إنشاء بيانات نموذجية بمشاكل للتوضيح
print("\n1. Creating sample data with common issues...")
print("إنشاء بيانات نموذجية بمشاكل شائعة...")

np.random.seed(42)
data = {
    'id': range(1, 21),
    'name': [f'Person_{i}' for i in range(1, 21)],
    'age': [25, 30, None, 35, 40, None, 28, 32, 45, 50, 
            22, None, 38, 42, 29, 33, 48, None, 27, 31],  # Missing values
    'salary': [50000, 60000, 55000, 70000, 80000, 65000, 58000, 
               72000, 90000, 95000, 52000, 68000, 75000, 85000,
               57000, 73000, 92000, 62000, 54000, 71000],
    'department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR', 'IT',
                   'Finance', 'IT', 'HR', 'IT', None, 'Finance', 'IT',
                   'HR', 'IT', 'Finance', 'IT', None, 'HR'],  # Missing values
    'experience_years': [2, 5, 3, 8, 10, 4, 2.5, 6, 12, 15,
                         1, 5.5, 9, 11, 3, 7, 13, 4.5, 2, 6]
}

df = pd.DataFrame(data)

# Add some duplicates
df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)

# Add some outliers
df.loc[18, 'salary'] = 500000  # Extreme outlier
df.loc[19, 'age'] = 150  # Impossible value

print("\nOriginal Data Shape:", df.shape)
print("شكل البيانات الأصلية:", df.shape)
print("\nOriginal Data:")
print(df.head(10))

# 2. Handling Missing Values
# معالجة القيم المفقودة
print("\n" + "=" * 60)
print("2. Handling Missing Values")
print("معالجة القيم المفقودة")
print("=" * 60)

print("\nMissing values before cleaning:")
print("القيم المفقودة قبل التنظيف:")
print(df.isnull().sum())

# Method 1: Remove rows with missing values (if few missing values)
# الطريقة 1: حذف الصفوف ذات القيم المفقودة (إذا كانت قليلة)
print("\n--- Method 1: Remove rows with missing values ---")
print("--- الطريقة 1: حذف الصفوف ذات القيم المفقودة ---")
df_removed = df.dropna()
print(f"Rows after removal: {df_removed.shape[0]} (removed {df.shape[0] - df_removed.shape[0]} rows)")
print(f"الصفوف بعد الحذف: {df_removed.shape[0]} (تم حذف {df.shape[0] - df_removed.shape[0]} صف)")

# Method 2: Fill missing values (imputation)
# الطريقة 2: ملء القيم المفقودة (الاستبدال)
print("\n--- Method 2: Fill missing values ---")
print("--- الطريقة 2: ملء القيم المفقودة ---")

df_filled = df.copy()

# Fill numeric columns with mean
# ملء الأعمدة الرقمية بالمتوسط
df_filled['age'].fillna(df_filled['age'].mean(), inplace=True)

# Fill categorical columns with mode
# ملء الأعمدة الفئوية بالقيمة الأكثر تكراراً
df_filled['department'].fillna(df_filled['department'].mode()[0], inplace=True)

print("\nMissing values after filling:")
print("القيم المفقودة بعد الملء:")
print(df_filled.isnull().sum())

# 3. Removing Duplicates
# إزالة التكرارات
print("\n" + "=" * 60)
print("3. Removing Duplicates")
print("إزالة التكرارات")
print("=" * 60)

print(f"\nNumber of duplicates: {df_filled.duplicated().sum()}")
print(f"عدد التكرارات: {df_filled.duplicated().sum()}")

df_no_duplicates = df_filled.drop_duplicates()
print(f"Rows after removing duplicates: {df_no_duplicates.shape[0]}")
print(f"الصفوف بعد إزالة التكرارات: {df_no_duplicates.shape[0]}")

# 4. Handling Outliers
# معالجة القيم الشاذة
print("\n" + "=" * 60)
print("4. Handling Outliers")
print("معالجة القيم الشاذة")
print("=" * 60)

# Method 1: IQR (Interquartile Range) Method
# الطريقة 1: طريقة المدى الربيعي
print("\n--- IQR Method for Outlier Detection ---")
print("--- طريقة المدى الربيعي للكشف عن القيم الشاذة ---")

def detect_outliers_iqr(series):
    """Detect outliers using IQR method"""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (series < lower_bound) | (series > upper_bound)

# Check for outliers in salary
print("\nOutliers in salary column:")
print("القيم الشاذة في عمود الراتب:")
salary_outliers = detect_outliers_iqr(df_no_duplicates['salary'])
print(f"Number of outliers: {salary_outliers.sum()}")
print(df_no_duplicates[salary_outliers][['name', 'salary']])

# Remove outliers
df_clean = df_no_duplicates[~salary_outliers].copy()

# Also remove impossible age values
df_clean = df_clean[df_clean['age'] <= 100].copy()

print(f"\nRows after removing outliers: {df_clean.shape[0]}")
print(f"الصفوف بعد إزالة القيم الشاذة: {df_clean.shape[0]}")

# 5. Data Type Conversion
# تحويل أنواع البيانات
print("\n" + "=" * 60)
print("5. Data Type Conversion")
print("تحويل أنواع البيانات")
print("=" * 60)

print("\nData types before conversion:")
print("أنواع البيانات قبل التحويل:")
print(df_clean.dtypes)

# Convert experience_years to int (rounding)
df_clean['experience_years'] = df_clean['experience_years'].round().astype(int)

# Convert age to int
df_clean['age'] = df_clean['age'].round().astype(int)

print("\nData types after conversion:")
print("أنواع البيانات بعد التحويل:")
print(df_clean.dtypes)

# 6. Summary
# الملخص
print("\n" + "=" * 60)
print("6. Cleaning Summary")
print("ملخص التنظيف")
print("=" * 60)

print(f"\nOriginal rows: {df.shape[0]}")
print(f"الصفوف الأصلية: {df.shape[0]}")

print(f"Final cleaned rows: {df_clean.shape[0]}")
print(f"الصفوف النهائية بعد التنظيف: {df_clean.shape[0]}")

print(f"\nRows removed: {df.shape[0] - df_clean.shape[0]}")
print(f"الصفوف المحذوفة: {df.shape[0] - df_clean.shape[0]}")

print("\nCleaned Data:")
print("البيانات النظيفة:")
print(df_clean.head(10))

print("\n" + "=" * 60)
print("Example 2 Complete! ✓")
print("اكتمل المثال 2! ✓")
print("=" * 60)

