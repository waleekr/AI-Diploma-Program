# Quiz 02: Data Cleaning and Preparation | اختبار 02: تنظيف البيانات وتحضيرها

## Instructions | التعليمات
- **Time Limit**: 30 minutes
- **Total Points**: 50 points
- **Format**: Multiple choice, short answer
- **Allowed Resources**: None (closed book)

---

## Part 1: Missing Values (15 points)

### Question 1 (5 points)
What is the best method to handle missing values in a normally distributed continuous variable?
- A) Delete rows with missing values
- B) Fill with mean
- C) Fill with median
- D) Fill with mode

**Answer:** B

---

### Question 2 (5 points)
What does `df.fillna(method='ffill')` do?
- A) Fills with forward values
- B) Fills with backward values
- C) Fills with mean
- D) Fills with zero

**Answer:** A

---

### Question 3 (5 points)
Which method is best for handling missing values in categorical data?
- A) Mean imputation
- B) Median imputation
- C) Mode imputation
- D) Delete rows

**Answer:** C

---

## Part 2: Duplicates (10 points)

### Question 4 (5 points)
What does `df.duplicated()` return?
- A) Number of duplicates
- B) Boolean Series indicating duplicates
- C) List of duplicate rows
- D) DataFrame without duplicates

**Answer:** B

---

### Question 5 (5 points)
How do you remove all duplicate rows from a DataFrame?
- A) `df.drop_duplicates()`
- B) `df.remove_duplicates()`
- C) `df.unique()`
- D) `df.deduplicate()`

**Answer:** A

---

## Part 3: Outliers (15 points)

### Question 6 (5 points)
What is the IQR (Interquartile Range)?
- A) Q3 - Q1
- B) Q1 - Q3
- C) Mean - Median
- D) Max - Min

**Answer:** A

---

### Question 7 (5 points)
In the IQR method, values outside what range are considered outliers?
- A) [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
- B) [Q1 - IQR, Q3 + IQR]
- C) [Mean - 2*Std, Mean + 2*Std]
- D) [Min, Max]

**Answer:** A

---

### Question 8 (5 points)
What Z-score threshold is commonly used to identify outliers?
- A) 1
- B) 2
- C) 3
- D) 4

**Answer:** C

---

## Part 4: Data Transformation (10 points)

### Question 9 (5 points)
What does Min-Max normalization do?
- A) Centers data around zero
- B) Scales data to [0, 1] range
- C) Standardizes to mean=0, std=1
- D) Log transforms data

**Answer:** B

---

### Question 10 (5 points)
What does Z-score standardization do?
- A) Scales to [0, 1]
- B) Transforms to mean=0, std=1
- C) Log transforms
- D) Square root transforms

**Answer:** B

---

## Answer Key | مفتاح الإجابات

1. B - Fill with mean (for normally distributed data)
2. A - Forward fill
3. C - Mode imputation
4. B - Boolean Series
5. A - `df.drop_duplicates()`
6. A - Q3 - Q1
7. A - [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
8. C - 3
9. B - Scales to [0, 1] range
10. B - Transforms to mean=0, std=1

---

**Good luck!** 🍀

