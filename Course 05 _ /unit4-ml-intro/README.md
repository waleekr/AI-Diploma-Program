# Unit 4: Introduction to Machine Learning
## مقدمة في تعلم الآلة


### Learning Objectives

By the end of this unit, students will be able to:
- Understand supervised learning fundamentals
- Implement linear regression for regression tasks
- Implement classification algorithms (logistic regression, decision trees)
- Evaluate model performance using appropriate metrics
- Understand the difference between training and testing
- Compare CPU (scikit-learn) vs GPU (cuML) approaches
- Perform cross-validation for model validation

---

## Topics Covered

1. **Supervised Learning Fundamentals**
   - Types of machine learning (supervised, unsupervised, reinforcement)
   - Training vs testing data
   - Overfitting and underfitting
   - Bias-variance tradeoff
   - Model generalization

2. **Regression Algorithms**
   - Linear regression
   - Multiple linear regression
   - Polynomial regression
   - Evaluation metrics (MSE, MAE, R²)
   - Residual analysis

3. **Classification Algorithms**
   - Logistic regression
   - Decision trees
   - Random forest basics
   - Evaluation metrics (accuracy, precision, recall, F1)
   - Confusion matrix
   - ROC curves and AUC

4. **Model Evaluation**
   - Train-test split
   - Cross-validation (k-fold)
   - Performance metrics for regression
   - Performance metrics for classification
   - Model comparison

5. **Feature Engineering for ML**
   - Feature scaling importance
   - Handling categorical variables
   - Feature selection basics
   - Feature importance

6. **GPU-Accelerated Machine Learning**
   - Introduction to cuML
   - Performance comparison with scikit-learn
   - When to use GPU acceleration
   - Limitations and considerations

---

## Files Structure

- `examples/`: Complete code examples with explanations
  - Regression examples
  - Classification examples
  - Model evaluation examples
  - CPU vs GPU comparisons
- `exercises/`: Practice problems for students
- `solutions/`: Solutions to exercises
- `quizzes/`: Assessment questions
- `tests/`: Unit tests and validation

---

## Prerequisites

Before starting this unit, you should have completed:
- Unit 1: Introduction to Data Science
- Unit 2: Data Cleaning and Preparation
- Unit 3: Data Visualization
- Understanding of statistical concepts (mean, variance, correlation)

---

## How to Use This Unit

1. Start with regression examples
2. Progress to classification
3. Focus on model evaluation techniques
4. Practice with different datasets
5. Compare CPU vs GPU performance
6. Complete exercises and quizzes

---

## Key Concepts

### Machine Learning Workflow

```
1. Data Preparation
   ↓
2. Feature Engineering
   ↓
3. Train-Test Split
   ↓
4. Model Training
   ↓
5. Model Evaluation
   ↓
6. Model Tuning
   ↓
7. Final Model
```

### Supervised Learning Types

**Regression:**
- Predict continuous values
- Examples: house prices, temperature, sales

**Classification:**
- Predict discrete categories
- Examples: spam/not spam, disease/no disease, image recognition

### Evaluation Metrics

**Regression:**
- Mean Squared Error (MSE): Lower is better
- Mean Absolute Error (MAE): Lower is better
- R² Score: Higher is better (0-1 scale)

**Classification:**
- Accuracy: Overall correctness
- Precision: Of predicted positives, how many are correct
- Recall: Of actual positives, how many were found
- F1 Score: Harmonic mean of precision and recall

---

## Example Workflow

1. **Prepare Data**
   ```python
   from sklearn.model_selection import train_test_split
   X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.2, random_state=42
   )
   ```

2. **Train Model**
   ```python
   from sklearn.linear_model import LinearRegression
   model = LinearRegression()
   model.fit(X_train, y_train)
   ```

3. **Evaluate Model**
   ```python
   from sklearn.metrics import mean_squared_error, r2_score
   predictions = model.predict(X_test)
   mse = mean_squared_error(y_test, predictions)
   r2 = r2_score(y_test, predictions)
   ```

4. **Cross-Validation**
   ```python
   from sklearn.model_selection import cross_val_score
   scores = cross_val_score(model, X, y, cv=5)
   ```

---

## GPU Acceleration with cuML

### Benefits
- Faster training on large datasets
- Parallel processing capabilities
- Memory-efficient operations

### Considerations
- Requires NVIDIA GPU
- Similar API to scikit-learn
- Not all algorithms available
- Best for large datasets

### Example
```python
from cuml.linear_model import LinearRegression
gpu_model = LinearRegression()
gpu_model.fit(X_train, y_train)
```

---

## Common Pitfalls

1. **Data Leakage**
   - Scaling before train-test split
   - Using future information

2. **Overfitting**
   - Model too complex for data
   - Training score much higher than test score

3. **Improper Evaluation**
   - Evaluating on training data only
   - Not using cross-validation

4. **Feature Issues**
   - Not scaling features
   - Ignoring categorical variables
   - Too many features (curse of dimensionality)

---

## Model Selection Guidelines

- **Linear Regression**: Linear relationships, interpretability needed
- **Logistic Regression**: Binary classification, probability estimates
- **Decision Trees**: Non-linear relationships, interpretability
- **Random Forest**: Better performance, less interpretable

---

## Next Unit Preview

Unit 5 will focus on scaling data science workflows, including distributed computing, production pipelines, and advanced optimization techniques.

