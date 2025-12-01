# Unit 1: Introduction to Data Science
## مقدمة في علم البيانات


### Learning Objectives

By the end of this unit, students will be able to:
- Understand the data science lifecycle and workflow
- Load data from various sources using pandas
- Perform basic data exploration and statistical analysis
- Understand the fundamentals of GPU-accelerated data processing with cuDF
- Compare CPU and GPU approaches for data operations

---

## Topics Covered

1. **Data Science Lifecycle**
   - Problem definition
   - Data collection
   - Data exploration
   - Model building
   - Deployment and monitoring

2. **Python Data Science Tools**
   - Introduction to pandas
   - Introduction to NumPy
   - Data structures (Series, DataFrame)
   - Basic operations

3. **GPU-Accelerated Data Processing**
   - Introduction to cuDF (GPU DataFrame)
   - When to use GPU acceleration
   - Performance considerations

4. **Data Loading**
   - Reading CSV files
   - Reading Excel files
   - Reading JSON files
   - Loading from databases
   - Handling large files

5. **Data Exploration**
   - Viewing data (head, tail, sample)
   - Data types and structure
   - Basic statistics (describe, info)
   - Missing value inspection
   - Data shape and dimensions

6. **Statistical Analysis**
   - Descriptive statistics
   - Central tendencies (mean, median, mode)
   - Dispersion measures (std, variance)
   - Correlation analysis
   - Distribution analysis

---

## Files Structure

- `examples/`: Complete code examples with explanations
  - CPU-based examples using pandas
  - GPU-based examples using cuDF (optional)
- `exercises/`: Practice problems for students
- `solutions/`: Solutions to exercises
- `quizzes/`: Assessment questions
- `tests/`: Unit tests and validation

---

## Prerequisites

Before starting, ensure you have:
- Python 3.8+ installed
- All packages from `requirements.txt` installed
- Basic understanding of Python syntax
- Familiarity with command line (optional but helpful)

**For GPU examples:**
- NVIDIA GPU with CUDA support
- RAPIDS installed (see main README.md)

---

## How to Use This Unit

1. Start with `examples/` to understand concepts
2. Run each example and observe the output
3. Modify examples to experiment with different datasets
4. Complete exercises in `exercises/`
5. Check your solutions against `solutions/`
6. Take quizzes to test your understanding

---

## Key Concepts

### Data Science Workflow

```
1. Problem Definition → 2. Data Collection → 3. Data Exploration
         ↑                                                     ↓
8. Monitoring ← 7. Deployment ← 6. Model Evaluation ← 5. Model Building
```

### pandas vs cuDF

- **pandas**: CPU-based, works on any system
- **cuDF**: GPU-accelerated, requires NVIDIA GPU
- Both have similar APIs for easy transition
- GPU provides speedup for large datasets

---

## Example Workflow

1. **Load Data**
   ```python
   import pandas as pd
   df = pd.read_csv('data.csv')
   ```

2. **Explore Data**
   ```python
   df.head()
   df.info()
   df.describe()
   ```

3. **Analyze Data**
   ```python
   df['column'].mean()
   df.corr()
   ```

---

## Next Unit Preview

Unit 2 will build on these fundamentals to teach data cleaning and preparation techniques, including handling missing values, outliers, and data transformation.

