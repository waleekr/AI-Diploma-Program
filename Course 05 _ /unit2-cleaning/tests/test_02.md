# Test 2: Data Cleaning and Preparation
## امتحان 2: تنظيف البيانات وتحضيرها

**Time Limit:** 60 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use pandas, numpy, scipy, sklearn

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
Which method is most appropriate for handling missing values in a skewed distribution?
- A) Mean imputation
- B) Median imputation
- C) Mode imputation
- D) Forward fill

**Answer:** B

---

### Question 2 (3 points)
What does `df.isnull().sum()` return?
- A) Total number of missing values
- B) Count of missing values per column
- C) Boolean mask
- D) Percentage of missing values

**Answer:** B

---

### Question 3 (3 points)
In outlier detection, what does a Z-score of 3.5 indicate?
- A) Normal value
- B) Mild outlier
- C) Extreme outlier
- D) Missing value

**Answer:** C

---

### Question 4 (3 points)
What is the purpose of data normalization?
- A) Remove outliers
- B) Scale features to similar ranges
- C) Remove duplicates
- D) Handle missing values

**Answer:** B

---

### Question 5 (3 points)
Which transformation is best for features with different scales?
- A) Log transformation
- B) Standardization
- C) Deletion
- D) Forward fill

**Answer:** B

---

## Part 2: Code Completion (20 points)

### Question 6 (10 points)
Write code to:
1. Load a dataset with missing values
2. Identify missing values
3. Fill missing numeric values with median
4. Fill missing categorical values with mode
5. Remove duplicates

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Identify missing values
print("Missing values:")
print(df.isnull().sum())

# Fill numeric columns with median
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Remove duplicates
df = df.drop_duplicates()

print(f"\nFinal shape: {df.shape}")
```

---

### Question 7 (10 points)
Write code to detect and handle outliers using IQR method:

```python
import pandas as pd
import numpy as np

# Sample data
df = pd.DataFrame({'value': np.random.normal(100, 15, 1000)})
df.loc[0] = 500  # Add outlier

# Detect outliers using IQR
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]
print(f"Number of outliers: {len(outliers)}")

# Cap outliers
df.loc[df['value'] > upper_bound, 'value'] = upper_bound
df.loc[df['value'] < lower_bound, 'value'] = lower_bound

print(f"Value range after capping: {df['value'].min():.2f} - {df['value'].max():.2f}")
```

---

## Part 3: Data Analysis (15 points)

### Question 8 (15 points)
Given a dataset with data quality issues, write code to:
1. Load and explore the data
2. Handle all missing values appropriately
3. Remove duplicates
4. Detect and handle outliers
5. Normalize one numeric column

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Sample data with issues
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'score': [85, 90, np.nan, 78, 92, 88, 500, 75, 80, 85],
    'category': ['A', 'B', 'A', np.nan, 'B', 'A', 'A', 'B', 'A', 'A']
}
df = pd.DataFrame(data)
df = pd.concat([df, df.iloc[[0, 1]]], ignore_index=True)  # Add duplicates

# 1. Explore
print("Initial data:")
print(df)
print(f"\nMissing values:\n{df.isnull().sum()}")

# 2. Handle missing values
df['score'].fillna(df['score'].median(), inplace=True)
df['category'].fillna(df['category'].mode()[0], inplace=True)

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Handle outliers (IQR method)
Q1 = df['score'].quantile(0.25)
Q3 = df['score'].quantile(0.75)
IQR = Q3 - Q1
upper_bound = Q3 + 1.5 * IQR
df.loc[df['score'] > upper_bound, 'score'] = upper_bound

# 5. Normalize
scaler = MinMaxScaler()
df['score_normalized'] = scaler.fit_transform(df[['score']])

print("\nFinal cleaned data:")
print(df)
```

---

## Grading Rubric | معايير التقييم

### Multiple Choice (15 points)
- 3 points per question

### Code Completion (20 points)
- Question 6: 2 points per section (10 total)
- Question 7: 2.5 points per section (10 total)

### Data Analysis (15 points)
- Exploration: 2 points
- Missing values: 4 points
- Duplicates: 2 points
- Outliers: 4 points
- Normalization: 3 points

---

**Total: 50 points**

---

**Good luck!** 🍀

