# Test 3: Data Visualization
## امتحان 3: تصوير البيانات

**Time Limit:** 60 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Show your work for code questions
- Use proper comments in your code
- You may use matplotlib, seaborn, pandas, numpy

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is the primary purpose of data visualization?
- A) To store data
- B) To communicate insights effectively
- C) To clean data
- D) To process data

**Answer:** B

---

### Question 2 (3 points)
Which library is built on top of matplotlib for statistical visualization?
- A) pandas
- B) seaborn
- C) numpy
- D) scipy

**Answer:** B

---

### Question 3 (3 points)
What does a box plot show?
- A) Only mean values
- B) Distribution, quartiles, and outliers
- C) Only maximum values
- D) Correlation coefficients

**Answer:** B

---

### Question 4 (3 points)
When should you use a scatter plot?
- A) To show trends over time
- B) To compare categories
- C) To show relationships between two variables
- D) To show distributions

**Answer:** C

---

### Question 5 (3 points)
What does `plt.subplots(2, 2)` create?
- A) One plot
- B) A 2x2 grid of subplots
- C) Two separate figures
- D) A 3D plot

**Answer:** B

---

## Part 2: Code Completion (20 points)

### Question 6 (10 points)
Create a complete visualization with:
1. Line plot of sales over time
2. Proper labels and title
3. Grid
4. Save to file

```python
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'sales': [100, 150, 200, 180]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df['month'], df['sales'], marker='o', linewidth=2, color='blue')
plt.title('Monthly Sales', fontsize=14, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sales_plot.png', dpi=150)
plt.show()
```

---

### Question 7 (10 points)
Create a seaborn visualization with:
1. Distribution plot with KDE
2. Box plot by category
3. Proper styling

```python
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'value': np.random.normal(100, 15, 200),
    'category': np.random.choice(['A', 'B', 'C'], 200)
})

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(data['value'], kde=True, ax=axes[0])
axes[0].set_title('Distribution Plot')

sns.boxplot(data=data, x='category', y='value', ax=axes[1])
axes[1].set_title('Box Plot by Category')

plt.tight_layout()
plt.savefig('seaborn_plots.png', dpi=150)
plt.show()
```

---

## Part 3: Data Visualization (15 points)

### Question 8 (15 points)
Given a dataset, create a comprehensive visualization dashboard with:
1. Multiple subplots (2x2)
2. Different chart types
3. Proper customization
4. Save to file

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'sales': [1200, 1500, 1800, 1600, 2000, 2200],
    'region': np.random.choice(['North', 'South'], 6),
    'value': np.random.uniform(50, 100, 6)
})

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Line plot
axes[0, 0].plot(data['month'], data['sales'], marker='o')
axes[0, 0].set_title('Sales Over Time')
axes[0, 0].grid(True, alpha=0.3)

# Bar chart
region_sales = data.groupby('region')['sales'].sum()
axes[0, 1].bar(region_sales.index, region_sales.values)
axes[0, 1].set_title('Sales by Region')

# Histogram
axes[1, 0].hist(data['value'], bins=10, edgecolor='black')
axes[1, 0].set_title('Value Distribution')

# Scatter plot
axes[1, 1].scatter(data['sales'], data['value'], alpha=0.6)
axes[1, 1].set_title('Sales vs Value')
axes[1, 1].set_xlabel('Sales')
axes[1, 1].set_ylabel('Value')

fig.suptitle('Sales Dashboard', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('dashboard.png', dpi=150)
plt.show()
```

---

## Grading Rubric | معايير التقييم

### Multiple Choice (15 points)
- 3 points per question

### Code Completion (20 points)
- Question 6: 2.5 points per section (10 total)
- Question 7: 5 points per plot (10 total)

### Data Visualization (15 points)
- Subplot creation: 3 points
- Different chart types: 6 points
- Customization: 3 points
- File saving: 3 points

---

**Total: 50 points**

---

**Good luck!** 🍀

