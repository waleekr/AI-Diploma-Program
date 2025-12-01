# Test 5: Scaling Data Science
## امتحان 5: توسيع نطاق علم البيانات

**Time Limit:** 60 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use pandas, numpy, time

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is the primary benefit of processing data in chunks?
- A) Better accuracy
- B) Reduced memory usage
- C) Faster visualization
- D) Better models

**Answer:** B

---

### Question 2 (3 points)
What does optimizing data types help achieve?
- A) Better model performance
- B) Reduced memory footprint
- C) Faster visualization
- D) More features

**Answer:** B

---

### Question 3 (3 points)
What is Dask primarily used for?
- A) Data visualization
- B) Distributed and parallel computing
- C) Model training
- D) Data cleaning

**Answer:** B

---

### Question 4 (3 points)
What is profiling?
- A) Data cleaning
- B) Measuring code performance
- C) Model evaluation
- D) Data visualization

**Answer:** B

---

### Question 5 (3 points)
Why is error handling important in production?
- A) To make code faster
- B) To ensure reliability and graceful failure
- C) To improve accuracy
- D) To reduce memory

**Answer:** B

---

## Part 2: Code Completion (20 points)

### Question 6 (10 points)
Write code to process a large dataset in chunks:

```python
import pandas as pd
import numpy as np
import time

# Generate large dataset
np.random.seed(42)
large_data = pd.DataFrame({
    'id': range(1, 100001),
    'value': np.random.randn(100000),
    'category': np.random.choice(['A', 'B', 'C'], 100000)
})

# Process in chunks
chunk_size = 10000
start_time = time.time()

results = []
for chunk in np.array_split(large_data, len(large_data) // chunk_size):
    chunk_mean = chunk['value'].mean()
    results.append(chunk_mean)

overall_mean = np.mean(results)
processing_time = time.time() - start_time

print(f"Processed in {processing_time:.4f} seconds")
print(f"Overall mean: {overall_mean:.4f}")
```

---

### Question 7 (10 points)
Write code to optimize memory usage:

```python
import pandas as pd
import numpy as np

# Sample data
data = pd.DataFrame({
    'id': range(1, 10001),
    'category': np.random.choice(['A', 'B', 'C'], 10000),
    'value': np.random.uniform(0, 100, 10000)
})

# Check original memory
original_memory = data.memory_usage(deep=True).sum() / 1024**2
print(f"Original memory: {original_memory:.2f} MB")

# Optimize
data['id'] = data['id'].astype('int32')
data['category'] = data['category'].astype('category')
data['value'] = data['value'].astype('float32')

# Check optimized memory
optimized_memory = data.memory_usage(deep=True).sum() / 1024**2
print(f"Optimized memory: {optimized_memory:.2f} MB")
print(f"Memory saved: {original_memory - optimized_memory:.2f} MB")
```

---

## Part 3: Performance Analysis (15 points)

### Question 8 (15 points)
Write code to profile and optimize operations:

```python
import pandas as pd
import numpy as np
import time

# Generate data
np.random.seed(42)
data = pd.DataFrame({
    'id': range(1, 50001),
    'value1': np.random.randn(50000),
    'value2': np.random.randn(50000),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 50000)
})

# Profile operations
operations = {
    'Mean': lambda: data['value1'].mean(),
    'GroupBy': lambda: data.groupby('category')['value1'].mean(),
    'Filter': lambda: data[data['value1'] > 0],
    'Sort': lambda: data.sort_values('value1')
}

results = {}
for op_name, op_func in operations.items():
    start = time.time()
    result = op_func()
    elapsed = time.time() - start
    results[op_name] = elapsed
    print(f"{op_name}: {elapsed:.4f} seconds")

# Find slowest operation
slowest = max(results, key=results.get)
print(f"\nSlowest operation: {slowest} ({results[slowest]:.4f} seconds)")

# Optimize: Use vectorized operations
start = time.time()
optimized_filter = data.loc[data['value1'] > 0]
optimized_time = time.time() - start
print(f"\nOptimized filter time: {optimized_time:.4f} seconds")
```

---

## Grading Rubric | معايير التقييم

### Multiple Choice (15 points)
- 3 points per question

### Code Completion (20 points)
- Question 6: 2.5 points per section (10 total)
- Question 7: 2.5 points per section (10 total)

### Performance Analysis (15 points)
- Profiling: 5 points
- Optimization: 5 points
- Analysis: 5 points

---

**Total: 50 points**

---

**Good luck!** 🍀

