# Project 02: Multi-Class Classification System | المشروع 02: نظام التصنيف متعدد الفئات

## Overview | نظرة عامة

Build a comprehensive classification system that implements and compares multiple classification algorithms on a real-world dataset.

**Learning Objectives:**
- Implement multiple classification algorithms
- Compare algorithm performance
- Apply proper evaluation metrics
- Perform hyperparameter tuning
- Create classification visualizations

---

## Requirements | المتطلبات

### Functional Requirements
1. **Data Preparation**
   - Load classification dataset
   - Perform EDA
   - Handle class imbalance (if present)
   - Split into train/validation/test sets

2. **Algorithm Implementation**
   - Logistic Regression
   - Decision Tree Classifier
   - Support Vector Machine (SVM)
   - (Optional) Random Forest, Naive Bayes

3. **Model Training**
   - Train all algorithms
   - Implement cross-validation
   - Perform hyperparameter tuning (GridSearchCV)
   - Handle class imbalance (SMOTE, class weights)

4. **Model Evaluation**
   - Calculate accuracy, precision, recall, F1-score
   - Generate confusion matrices
   - Create ROC curves and AUC scores
   - Generate classification reports

5. **Comparison and Visualization**
   - Compare all models side-by-side
   - Create performance comparison charts
   - Visualize decision boundaries (for 2D data)
   - Generate feature importance plots

### Technical Requirements
- Use Python 3.8+
- Use scikit-learn for algorithms
- Use imbalanced-learn for handling imbalance
- Use matplotlib/seaborn for visualization
- Implement proper error handling
- Add comprehensive logging

---

## Deliverables | المخرجات

1. **Source Code**
   - `data_preparation.py` - Data loading and preprocessing
   - `classifiers.py` - Classification algorithms
   - `evaluator.py` - Model evaluation
   - `comparison.py` - Model comparison
   - `visualizer.py` - Visualization functions
   - `main.py` - Main program

2. **Documentation**
   - README.md
   - Code comments
   - Results analysis

3. **Results**
   - Performance metrics table
   - Confusion matrices
   - ROC curves
   - Comparison charts

---

## Dataset Suggestions | اقتراحات مجموعات البيانات

- **Iris Dataset** (3 classes)
- **Wine Quality** (Multi-class)
- **Digits Dataset** (10 classes)
- **Customer Churn** (Binary or multi-class)
- **Spam Detection** (Binary)

---

## Evaluation Criteria | معايير التقييم

- Algorithm implementation (30%)
- Model performance (25%)
- Code quality (20%)
- Visualization quality (15%)
- Documentation (10%)

---

**Created**: 2025  
**For**: Machine Learning Algorithms and Applications - AIAT 114

