# Instructor Guide - AIAT 114
## دليل الم instructor

### Quick Start Guide

This curriculum is designed for teaching Machine Learning Algorithms and Applications using Python. All materials are bilingual (Arabic/English).

---

## Course Structure Overview

### Unit 1: Basic Data Processing Methods and Regression
**Duration:** 3-4 weeks

**Key Topics:**
- Data loading and exploration
- Data cleaning and preprocessing
- Linear and Polynomial Regression

**Files:**
- `unit1-data-processing/examples/` - 5 complete examples
- `unit1-data-processing/exercises/` - Practice problems
- `unit1-data-processing/solutions/` - Complete solutions

**Teaching Tips:**
1. Start with Example 1 (data loading) to ensure students understand pandas basics
2. Use Example 2 (data cleaning) to demonstrate real-world data issues
3. Progress through regression examples sequentially
4. Assign exercises after completing examples

---

### Unit 2: Advanced Regression Techniques and Model Evaluation
**Duration:** 2-3 weeks

**Key Topics:**
- Ridge and Lasso Regression
- Cross-validation
- Model evaluation metrics

**Files:**
- `unit2-regression/examples/01_ridge_lasso_regression.py`
- Additional examples can be added

**Teaching Tips:**
1. Emphasize the difference between L1 and L2 regularization
2. Use visualization to show coefficient shrinkage
3. Explain overfitting concepts clearly

---

### Unit 3: Advanced Classification Techniques and Model Evaluation
**Duration:** 3-4 weeks

**Key Topics:**
- Logistic Regression
- Decision Trees and Random Forest
- Classification metrics (Precision, Recall, F1, ROC-AUC)

**Files:**
- `unit3-classification/examples/01_logistic_regression.py`
- Additional examples can be added

**Teaching Tips:**
1. Start with binary classification before multi-class
2. Explain confusion matrix thoroughly
3. Use ROC curves to show model performance
4. Compare different classification algorithms

---

### Unit 4: Clustering and Dimensionality Reduction
**Duration:** 2-3 weeks

**Key Topics:**
- K-Means Clustering
- Hierarchical Clustering
- PCA (Principal Component Analysis)

**Files:**
- `unit4-clustering/examples/01_kmeans_clustering.py`
- Additional examples can be added

**Teaching Tips:**
1. Demonstrate Elbow Method for choosing K
2. Use visualization extensively for clustering
3. Explain when to use clustering vs classification
4. Show PCA's role in dimensionality reduction

---

### Unit 5: Model Selection and Boosting
**Duration:** 2-3 weeks

**Key Topics:**
- Hyperparameter tuning (Grid Search, Random Search)
- Gradient Boosting (XGBoost, LightGBM)
- Ensemble methods

**Files:**
- `unit5-model-selection/README.md` - Structure ready
- Examples can be added

**Teaching Tips:**
1. Emphasize the importance of hyperparameter tuning
2. Compare different boosting algorithms
3. Show ensemble methods' advantages

---

## Teaching Methodology

### Recommended Approach

1. **Theory First (15-20 minutes)**
   - Explain concepts using slides or whiteboard
   - Use Arabic for key concepts, English for technical terms

2. **Live Coding (30-40 minutes)**
   - Walk through examples step by step
   - Explain each line of code
   - Answer questions as you go

3. **Hands-On Practice (20-30 minutes)**
   - Students modify examples
   - Try exercises
   - Work in pairs for complex problems

4. **Review and Q&A (10-15 minutes)**
   - Review key concepts
   - Answer questions
   - Preview next topic

### Best Practices

1. **Code Organization**
   - Always run examples before class
   - Test on different Python versions
   - Prepare solutions in advance

2. **Student Engagement**
   - Use real-world datasets when possible
   - Connect concepts to applications
   - Encourage experimentation

3. **Assessment**
   - Use exercises as homework
   - Create projects combining multiple units
   - Conduct quizzes on key concepts

---

## Technical Setup

### Prerequisites for Students

- Python 3.8+ installed
- Basic Python knowledge (variables, loops, functions)
- Familiarity with NumPy and Pandas helpful but not required

### Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Common Issues

1. **Import Errors**
   - Ensure all packages are installed
   - Check Python version compatibility

2. **Visualization Issues**
   - Some systems may need: `pip install matplotlib --upgrade`
   - Use `plt.show()` if plots don't display

3. **Data Generation**
   - All examples use generated data
   - Students can modify seed values for different results

---

## Recommended Schedule

### 16-Week Semester Structure

**Weeks 1-4:** Unit 1 (Data Processing and Basic Regression)
- Week 1: Data loading and exploration
- Week 2: Data cleaning and preprocessing
- Week 3: Linear Regression
- Week 4: Polynomial Regression + Review

**Weeks 5-7:** Unit 2 (Advanced Regression)
- Week 5: Ridge and Lasso
- Week 6: Cross-validation and metrics
- Week 7: Review and exercises

**Weeks 8-11:** Unit 3 (Classification)
- Week 8: Logistic Regression
- Week 9: Decision Trees and Random Forest
- Week 10: SVM and other classifiers
- Week 11: Classification metrics and review

**Weeks 12-14:** Unit 4 (Clustering and Dimensionality Reduction)
- Week 12: K-Means Clustering
- Week 13: Hierarchical Clustering
- Week 14: PCA and dimensionality reduction

**Weeks 15-16:** Unit 5 (Model Selection and Boosting)
- Week 15: Hyperparameter tuning
- Week 16: Boosting algorithms and final projects

---

## Additional Resources

### Suggested Datasets

1. **House Prices** (for regression)
   - Kaggle: House Prices Dataset
   - Or use generated data in examples

2. **Iris Dataset** (for classification)
   - Built into sklearn: `from sklearn.datasets import load_iris`

3. **Customer Segmentation** (for clustering)
   - Mall Customer Dataset
   - Or generate synthetic data

### Useful Links

- Scikit-learn Documentation: https://scikit-learn.org/
- Pandas Documentation: https://pandas.pydata.org/
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/

---

## Assessment Suggestions

1. **Weekly Exercises** (30%)
   - Complete exercises from each unit
   - Submit solutions via code repository

2. **Midterm Project** (25%)
   - Apply Unit 1-2 concepts
   - Predict house prices or similar regression task

3. **Final Project** (35%)
   - Complete ML pipeline: data → model → evaluation
   - Use classification or clustering

4. **Participation** (10%)
   - Class attendance and engagement
   - Code reviews and discussions

---

## Contact and Support

For questions about curriculum:
- Review example code and comments
- Check solutions directory
- Consult main README.md

For technical issues:
- Ensure all dependencies are installed
- Check Python version compatibility
- Verify data files are accessible

---

## Notes for Future Enhancement

Consider adding:
- Jupyter Notebook versions of examples
- Video tutorials for complex topics
- More real-world datasets
- Project templates
- Automated testing scripts

---

**Last Updated:** 2024
**Version:** 1.0

