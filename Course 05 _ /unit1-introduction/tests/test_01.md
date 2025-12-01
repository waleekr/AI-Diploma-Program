# Test 1: Introduction to Data Science
## امتحان 1: مقدمة في علم البيانات

**Time Limit:** 60 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use pandas, numpy, matplotlib, and seaborn

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is a DataFrame in pandas?
- A) A single column of data
- B) A two-dimensional labeled data structure
- C) A one-dimensional array
- D) A Python dictionary

**Answer:** B

---

### Question 2 (3 points)
Which library is primarily used for numerical computing in Python?
- A) pandas
- B) NumPy
- C) matplotlib
- D) seaborn

**Answer:** B

---

### Question 3 (3 points)
What does the data science lifecycle start with?
- A) Data Collection
- B) Model Building
- C) Problem Definition
- D) Data Exploration

**Answer:** C

---

### Question 4 (3 points)
What is the purpose of `df.corr()`?
- A) Count rows
- B) Calculate correlation matrix
- C) Find missing values
- D) Get data types

**Answer:** B

---

### Question 5 (3 points)
Which method groups data by a column and applies an aggregation function?
- A) `df.filter()`
- B) `df.groupby()`
- C) `df.sort()`
- D) `df.merge()`

**Answer:** B

---

## Part 2: Code Completion (20 points)

### Question 6 (10 points)
Complete the code to:
1. Load a CSV file named 'data.csv'
2. Display the first 10 rows
3. Calculate the mean of column 'score'
4. Filter rows where 'age' > 25

```python
import pandas as pd

# Load the CSV file
df = ________________

# Display first 10 rows
print(________________)

# Calculate mean of 'score' column
mean_score = ________________

# Filter rows where age > 25
filtered_df = ________________
```

**Answer:**
```python
import pandas as pd

# Load the CSV file
df = pd.read_csv('data.csv')

# Display first 10 rows
print(df.head(10))

# Calculate mean of 'score' column
mean_score = df['score'].mean()

# Filter rows where age > 25
filtered_df = df[df['age'] > 25]
```

---

### Question 7 (10 points)
Write code to:
1. Create a DataFrame with columns: 'name', 'age', 'score'
2. Add 5 rows of sample data
3. Calculate statistics (mean, median, std) for 'score'
4. Create a bar chart of 'score' values

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'score': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)

# Calculate statistics
mean_score = df['score'].mean()
median_score = df['score'].median()
std_score = df['score'].std()

print(f"Mean: {mean_score:.2f}")
print(f"Median: {median_score:.2f}")
print(f"Std: {std_score:.2f}")

# Create bar chart
plt.bar(df['name'], df['score'])
plt.title('Scores by Name')
plt.xlabel('Name')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## Part 3: Data Analysis (15 points)

### Question 8 (15 points)
Given the following dataset, write code to:
1. Load and explore the data
2. Calculate average score by department
3. Find the department with highest average score
4. Create a visualization showing scores by department

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F'],
    'department': ['CS', 'CS', 'Engineering', 'Engineering', 'Business', 'Business'],
    'score': [85, 90, 78, 82, 88, 85]
}
df = pd.DataFrame(data)

# Your code here
# 1. Explore data
print("Data Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# 2. Calculate average by department
dept_avg = df.groupby('department')['score'].mean()
print("\nAverage score by department:")
print(dept_avg)

# 3. Find department with highest average
best_dept = dept_avg.idxmax()
best_score = dept_avg.max()
print(f"\nDepartment with highest average: {best_dept} ({best_score:.2f})")

# 4. Visualization
plt.bar(dept_avg.index, dept_avg.values, color='steelblue')
plt.title('Average Score by Department')
plt.xlabel('Department')
plt.ylabel('Average Score')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()
```

---

## Grading Rubric | معايير التقييم

### Multiple Choice (15 points)
- 3 points per question
- No partial credit

### Code Completion (20 points)
- Question 6: 2.5 points per correct line (10 total)
- Question 7: 2 points per correct section (10 total)

### Data Analysis (15 points)
- Exploration: 3 points
- Grouping and calculation: 5 points
- Finding maximum: 2 points
- Visualization: 5 points

---

**Total: 50 points**

---

**Good luck!** 🍀  
**حظاً موفقاً!**

