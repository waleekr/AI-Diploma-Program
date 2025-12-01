# Test 4: Introduction to Machine Learning
## امتحان 4: مقدمة في تعلم الآلة

**Time Limit:** 60 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use sklearn, pandas, numpy, matplotlib

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is the goal of machine learning?
- A) To write explicit programs
- B) To learn patterns from data
- C) To store data
- D) To visualize data

**Answer:** B

---

### Question 2 (3 points)
What is the difference between training and testing?
- A) Training uses test data, testing uses train data
- B) Training learns patterns, testing evaluates performance
- C) No difference
- D) Training is faster

**Answer:** B

---

### Question 3 (3 points)
What does MSE stand for?
- A) Mean Squared Error
- B) Maximum Standard Error
- C) Minimum Squared Error
- D) Mean Standard Error

**Answer:** A

---

### Question 4 (3 points)
What is cross-validation used for?
- A) To split data
- B) To evaluate model performance more reliably
- C) To train models
- D) To clean data

**Answer:** B

---

### Question 5 (3 points)
What is feature scaling?
- A) Removing features
- B) Normalizing feature values to similar ranges
- C) Adding features
- D) Selecting features

**Answer:** B

---

## Part 2: Code Completion (20 points)

### Question 6 (10 points)
Write code to build and evaluate a linear regression model:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Generate sample data
np.random.seed(42)
X = np.random.randn(100, 2)
y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.randn(100) * 0.5

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"R² Score: {r2:.4f}")
```

---

### Question 7 (10 points)
Write code to build and evaluate a classification model:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

# Generate sample data
np.random.seed(42)
X = np.random.randn(100, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"\nConfusion Matrix:\n{cm}")
print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")
```

---

## Part 3: Model Building (15 points)

### Question 8 (15 points)
Build a complete ML pipeline:
1. Load/prepare data
2. Split into train/test
3. Train regression and classification models
4. Evaluate both
5. Compare performance

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import numpy as np
import pandas as pd

# Generate data
np.random.seed(42)
n = 200

# Regression data
X_reg = np.random.randn(n, 3)
y_reg = 2 * X_reg[:, 0] + 1.5 * X_reg[:, 1] + np.random.randn(n) * 0.3

# Classification data
X_clf = np.random.randn(n, 2)
y_clf = (X_clf[:, 0] + X_clf[:, 1] > 0).astype(int)

# Regression
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)
lr = LinearRegression()
lr.fit(X_train_reg, y_train_reg)
y_pred_reg = lr.predict(X_test_reg)
mse = mean_squared_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

# Classification
X_train_clf, X_test_clf, y_train_clf, y_test_clf = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42, stratify=y_clf
)
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train_clf, y_train_clf)
y_pred_clf = log_reg.predict(X_test_clf)
acc = accuracy_score(y_test_clf, y_pred_clf)

print("Regression Results:")
print(f"MSE: {mse:.4f}, R²: {r2:.4f}")
print("\nClassification Results:")
print(f"Accuracy: {acc:.4f}")
```

---

## Grading Rubric | معايير التقييم

### Multiple Choice (15 points)
- 3 points per question

### Code Completion (20 points)
- Question 6: 2 points per section (10 total)
- Question 7: 2.5 points per section (10 total)

### Model Building (15 points)
- Data preparation: 3 points
- Model training: 5 points
- Evaluation: 4 points
- Comparison: 3 points

---

**Total: 50 points**

---

**Good luck!** 🍀

