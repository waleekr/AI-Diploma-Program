# Unit 2: Data Cleaning and Preparation
## تنظيف البيانات وتحضيرها


### Learning Objectives

By the end of this unit, students will be able to:
- Identify and handle missing values effectively
- Detect and remove duplicate records
- Identify and treat outliers
- Transform data types appropriately
- Perform feature engineering
- Normalize and standardize features
- Compare CPU (pandas) vs GPU (cuDF) performance for data cleaning

---

## Topics Covered

1. **Handling Missing Values**
   - Identifying missing data patterns
   - Deletion strategies (listwise, pairwise)
   - Imputation methods (mean, median, mode, forward fill)
   - Advanced imputation (KNN, regression-based)
   - Missing value visualization

2. **Duplicate Detection and Removal**
   - Identifying duplicate records
   - Partial duplicates
   - Duplicate removal strategies
   - Handling duplicates in large datasets

3. **Outlier Detection and Treatment**
   - Statistical methods (Z-score, IQR)
   - Visualization methods (box plots, scatter plots)
   - Outlier treatment strategies
   - Domain-specific outlier handling

4. **Data Type Conversion**
   - Converting between data types
   - Date and time parsing
   - Categorical encoding basics
   - Type optimization for memory

5. **Feature Engineering**
   - Creating new features
   - Feature transformations
   - Binning and discretization
   - Feature interactions

6. **Data Normalization and Standardization**
   - Min-Max normalization
   - Z-score standardization
   - Robust scaling
   - When to use each method

7. **Performance Optimization**
   - CPU vs GPU comparison
   - Memory-efficient operations
   - Chunking large datasets
   - Parallel processing basics

---

## Files Structure

- `examples/`: Complete code examples with explanations
  - Missing value handling examples
  - Outlier detection examples
  - Data transformation examples
  - CPU vs GPU performance comparisons
- `exercises/`: Practice problems for students
- `solutions/`: Solutions to exercises
- `quizzes/`: Assessment questions
- `tests/`: Unit tests and validation

---

## Prerequisites

Before starting this unit, you should have completed:
- Unit 1: Introduction to Data Science
- Understanding of pandas/cuDF basics
- Familiarity with data exploration techniques

---

## How to Use This Unit

1. Review examples for each cleaning technique
2. Run examples with different datasets
3. Experiment with different parameters
4. Complete exercises to practice
5. Compare your solutions with provided solutions
6. Take quizzes to assess understanding

---

## Key Concepts

### Missing Value Strategy Decision Tree

```
Missing Data
    ↓
Is missingness random?
    ├─ Yes → Impute
    │         ├─ Numerical → Mean/Median/Regression
    │         └─ Categorical → Mode/Classification
    └─ No → Analyze pattern
              └─ Consider deletion if systematic
```

### Outlier Detection Methods

1. **Statistical Methods**
   - Z-score: |z| > 3
   - IQR: Q1 - 1.5*IQR, Q3 + 1.5*IQR

2. **Visualization Methods**
   - Box plots
   - Scatter plots
   - Histograms

3. **Domain Knowledge**
   - Business rules
   - Data constraints
   - Expected ranges

### Data Cleaning Pipeline

```
1. Load Data
2. Identify Issues (missing, duplicates, outliers)
3. Handle Missing Values
4. Remove Duplicates
5. Treat Outliers
6. Transform Data Types
7. Feature Engineering
8. Normalize/Standardize
9. Validate Clean Data
```

---

## Example Workflow

1. **Check for Missing Values**
   ```python
   df.isnull().sum()
   df.isnull().mean() * 100  # Percentage
   ```

2. **Handle Missing Values**
   ```python
   df.fillna(df.mean())
   df.dropna()
   ```

3. **Detect Outliers**
   ```python
   from scipy import stats
   z_scores = stats.zscore(df['column'])
   outliers = (np.abs(z_scores) > 3)
   ```

4. **Normalize Data**
   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   df_scaled = scaler.fit_transform(df)
   ```

---

## Performance Tips

- Use `cuDF` for datasets > 1GB on GPU systems
- Process data in chunks for very large files
- Use appropriate data types to save memory
- Leverage vectorized operations instead of loops
- Profile your code to identify bottlenecks

---

## Next Unit Preview

Unit 3 will focus on data visualization techniques to explore and communicate insights from cleaned data effectively.

