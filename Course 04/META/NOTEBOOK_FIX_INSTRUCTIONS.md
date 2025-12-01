# Quick Fix for Notebook Error
## إصلاح سريع لخطأ الدفتر

## Problem / المشكلة
Cell 20 tries to use `categorical_cols` but it's not defined because the function code was split across cells.

## Solution / الحل

### Option 1: Delete Cell 20 and Combine with Cell 19

**Steps:**
1. Delete Cell 20 (the one with the error)
2. Edit Cell 19 to include the complete function:

```python
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
```

3. Delete Cell 21 and 22 (they're part of the function)
4. Keep Cell 24 as is (it uses the function)

### Option 2: Quick Fix - Just Define Variables

If you want to keep cells separate, add this at the start of Cell 20:

```python
# Define variables for demonstration
numeric_cols = ['age', 'salary', 'experience']
categorical_cols = ['city', 'education']
X = df[numeric_cols + categorical_cols].copy()

# One-hot encode categorical variables
X_encoded = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
```

But Option 1 is recommended - the function should be in one cell!

