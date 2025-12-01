"""
Unit 1 - Example 1: Data Loading and Exploration
أساليب معالجة البيانات - مثال 1: تحميل واستكشاف البيانات

This example demonstrates how to:
1. Load data from different sources (CSV, Excel)
2. Explore data structure and basic statistics
3. Understand data types and dimensions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set display options for better output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("=" * 60)
print("Example 1: Data Loading and Exploration")
print("مثال 1: تحميل واستكشاف البيانات")
print("=" * 60)

# 1. Loading Data from CSV
# تحميل البيانات من ملف CSV
print("\n1. Loading data from CSV file...")
print("تحميل البيانات من ملف CSV...")

# Create sample data for demonstration
# إنشاء بيانات نموذجية للتوضيح
data = {
    'house_size': [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3500],
    'bedrooms': [2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    'age': [5, 10, 8, 15, 3, 20, 12, 25, 7, 30],
    'price': [250000, 280000, 320000, 380000, 420000, 450000, 520000, 580000, 620000, 750000],
    'location': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A']
}

df = pd.DataFrame(data)

# Save to CSV for demonstration
df.to_csv('sample_housing_data.csv', index=False)

# Load from CSV
df_loaded = pd.read_csv('sample_housing_data.csv')
print("\nData loaded successfully!")
print("تم تحميل البيانات بنجاح!")

# 2. Basic Data Inspection
# الفحص الأساسي للبيانات
print("\n" + "=" * 60)
print("2. Basic Data Inspection")
print("الفحص الأساسي للبيانات")
print("=" * 60)

# Display first few rows
print("\nFirst 5 rows / الصفوف الخمسة الأولى:")
print(df_loaded.head())

# Display last few rows
print("\nLast 5 rows / الصفوف الخمسة الأخيرة:")
print(df_loaded.tail())

# Data shape (rows, columns)
print("\nData Shape / شكل البيانات (صفوف، أعمدة):")
print(f"Rows: {df_loaded.shape[0]}, Columns: {df_loaded.shape[1]}")
print(f"الصفوف: {df_loaded.shape[0]}, الأعمدة: {df_loaded.shape[1]}")

# Data types
print("\nData Types / أنواع البيانات:")
print(df_loaded.dtypes)

# Data information summary
print("\nData Info / معلومات البيانات:")
print(df_loaded.info())

# 3. Statistical Summary
# الملخص الإحصائي
print("\n" + "=" * 60)
print("3. Statistical Summary")
print("الملخص الإحصائي")
print("=" * 60)

print("\nDescriptive Statistics / الإحصائيات الوصفية:")
print(df_loaded.describe())

# 4. Check for Missing Values
# التحقق من القيم المفقودة
print("\n" + "=" * 60)
print("4. Missing Values Check")
print("التحقق من القيم المفقودة")
print("=" * 60)

missing_values = df_loaded.isnull().sum()
print("\nMissing values per column / القيم المفقودة لكل عمود:")
print(missing_values)

if missing_values.sum() == 0:
    print("\n✓ No missing values found / لا توجد قيم مفقودة")

# 5. Check for Duplicates
# التحقق من التكرارات
print("\n" + "=" * 60)
print("5. Duplicate Check")
print("التحقق من التكرارات")
print("=" * 60)

duplicates = df_loaded.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")
print(f"عدد الصفوف المكررة: {duplicates}")

if duplicates == 0:
    print("✓ No duplicates found / لا توجد تكرارات")

# 6. Basic Statistics for Specific Columns
# الإحصائيات الأساسية لأعمدة محددة
print("\n" + "=" * 60)
print("6. Column-specific Statistics")
print("الإحصائيات الخاصة بالأعمدة")
print("=" * 60)

print("\nPrice statistics / إحصائيات السعر:")
print(f"Mean: {df_loaded['price'].mean():.2f}")
print(f"Median: {df_loaded['price'].median():.2f}")
print(f"Standard Deviation: {df_loaded['price'].std():.2f}")
print(f"Min: {df_loaded['price'].min():.2f}")
print(f"Max: {df_loaded['price'].max():.2f}")

# 7. Value Counts for Categorical Data
# عدد القيم للبيانات الفئوية
print("\n" + "=" * 60)
print("7. Categorical Data Analysis")
print("تحليل البيانات الفئوية")
print("=" * 60)

print("\nLocation distribution / توزيع الموقع:")
print(df_loaded['location'].value_counts())

print("\nBedroom distribution / توزيع عدد الغرف:")
print(df_loaded['bedrooms'].value_counts().sort_index())

print("\n" + "=" * 60)
print("Example 1 Complete! ✓")
print("اكتمل المثال 1! ✓")
print("=" * 60)

