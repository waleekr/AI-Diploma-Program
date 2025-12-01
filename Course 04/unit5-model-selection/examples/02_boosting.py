"""
Unit 5 - Example 2: Gradient Boosting (XGBoost, LightGBM)
اختيار النموذج والتعزيز - مثال 2: التعزيز المتدرج (XGBoost, LightGBM)

This example demonstrates:
1. XGBoost classifier
2. LightGBM classifier
3. Comparison with Random Forest
4. Feature importance
5. Hyperparameter tuning for boosting
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                            confusion_matrix, roc_auc_score, roc_curve)
from sklearn.datasets import make_classification

try:
    import xgboost as xgb
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False
    print("Warning: XGBoost not installed. Install with: pip install xgboost")

try:
    import lightgbm as lgb
    LIGHTGBM_AVAILABLE = True
except ImportError:
    LIGHTGBM_AVAILABLE = False
    print("Warning: LightGBM not installed. Install with: pip install lightgbm")

print("=" * 60)
print("Example 2: Gradient Boosting (XGBoost, LightGBM)")
print("مثال 2: التعزيز المتدرج (XGBoost, LightGBM)")
print("=" * 60)

# Generate sample classification data
# إنشاء بيانات تصنيف نموذجية
np.random.seed(42)
X, y = make_classification(
    n_samples=2000,
    n_features=20,
    n_informative=10,
    n_redundant=5,
    n_clusters_per_class=1,
    random_state=42
)

df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(20)])
df['target'] = y

print(f"\nData Shape: {df.shape}")
print(f"Target distribution:")
print(df['target'].value_counts())

# Split data
X_data = df.drop('target', axis=1)
y_data = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_data, y_data, test_size=0.2, random_state=42, stratify=y_data
)

# 1. Random Forest (Baseline)
print("\n" + "=" * 60)
print("1. Random Forest (Baseline)")
print("الغابة العشوائية (خط الأساس)")
print("=" * 60)

rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

y_train_pred_rf = rf.predict(X_train)
y_test_pred_rf = rf.predict(X_test)

train_acc_rf = accuracy_score(y_train, y_train_pred_rf)
test_acc_rf = accuracy_score(y_test, y_test_pred_rf)

print(f"Training Accuracy: {train_acc_rf:.4f}")
print(f"Test Accuracy: {test_acc_rf:.4f}")

# 2. XGBoost
print("\n" + "=" * 60)
print("2. XGBoost")
print("XGBoost")
print("=" * 60)

if XGBOOST_AVAILABLE:
    xgb_model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        random_state=42,
        eval_metric='logloss'
    )
    
    xgb_model.fit(X_train, y_train)
    
    y_train_pred_xgb = xgb_model.predict(X_train)
    y_test_pred_xgb = xgb_model.predict(X_test)
    
    train_acc_xgb = accuracy_score(y_train, y_train_pred_xgb)
    test_acc_xgb = accuracy_score(y_test, y_test_pred_xgb)
    
    print(f"Training Accuracy: {train_acc_xgb:.4f}")
    print(f"Test Accuracy: {test_acc_xgb:.4f}")
    
    # Probability predictions
    y_test_proba_xgb = xgb_model.predict_proba(X_test)[:, 1]
else:
    print("XGBoost not available - skipping")
    train_acc_xgb = test_acc_xgb = 0
    y_test_proba_xgb = None

# 3. LightGBM
print("\n" + "=" * 60)
print("3. LightGBM")
print("LightGBM")
print("=" * 60)

if LIGHTGBM_AVAILABLE:
    lgb_model = lgb.LGBMClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        random_state=42,
        verbose=-1
    )
    
    lgb_model.fit(X_train, y_train)
    
    y_train_pred_lgb = lgb_model.predict(X_train)
    y_test_pred_lgb = lgb_model.predict(X_test)
    
    train_acc_lgb = accuracy_score(y_train, y_train_pred_lgb)
    test_acc_lgb = accuracy_score(y_test, y_test_pred_lgb)
    
    print(f"Training Accuracy: {train_acc_lgb:.4f}")
    print(f"Test Accuracy: {test_acc_lgb:.4f}")
    
    # Probability predictions
    y_test_proba_lgb = lgb_model.predict_proba(X_test)[:, 1]
else:
    print("LightGBM not available - skipping")
    train_acc_lgb = test_acc_lgb = 0
    y_test_proba_lgb = None

# 4. Model Comparison
print("\n" + "=" * 60)
print("4. Model Comparison")
print("مقارنة النماذج")
print("=" * 60)

comparison_data = {
    'Model': ['Random Forest'],
    'Train Accuracy': [train_acc_rf],
    'Test Accuracy': [test_acc_rf]
}

if XGBOOST_AVAILABLE:
    comparison_data['Model'].append('XGBoost')
    comparison_data['Train Accuracy'].append(train_acc_xgb)
    comparison_data['Test Accuracy'].append(test_acc_xgb)

if LIGHTGBM_AVAILABLE:
    comparison_data['Model'].append('LightGBM')
    comparison_data['Train Accuracy'].append(train_acc_lgb)
    comparison_data['Test Accuracy'].append(test_acc_lgb)

comparison_df = pd.DataFrame(comparison_data)
print("\nModel Comparison:")
print(comparison_df.to_string(index=False))

# 5. Feature Importance Comparison
print("\n" + "=" * 60)
print("5. Feature Importance Comparison")
print("مقارنة أهمية الميزات")
print("=" * 60)

if XGBOOST_AVAILABLE or LIGHTGBM_AVAILABLE:
    importance_data = {
        'Feature': X_data.columns,
        'Random Forest': rf.feature_importances_
    }
    
    if XGBOOST_AVAILABLE:
        importance_data['XGBoost'] = xgb_model.feature_importances_
    
    if LIGHTGBM_AVAILABLE:
        importance_data['LightGBM'] = lgb_model.feature_importances_
    
    importance_df = pd.DataFrame(importance_data)
    importance_df = importance_df.sort_values('Random Forest', ascending=False)
    
    print("\nTop 10 Most Important Features:")
    print(importance_df.head(10).to_string(index=False))
    
    # Visualize feature importance
    if XGBOOST_AVAILABLE or LIGHTGBM_AVAILABLE:
        top_n = 10
        top_features = importance_df.head(top_n)
        
        fig, axes = plt.subplots(1, 2 if (XGBOOST_AVAILABLE and LIGHTGBM_AVAILABLE) else 1, 
                                figsize=(15, 6))
        if not isinstance(axes, np.ndarray):
            axes = [axes]
        
        idx = 0
        
        # Random Forest
        axes[idx].barh(range(top_n), top_features['Random Forest'].values[::-1], alpha=0.7)
        axes[idx].set_yticks(range(top_n))
        axes[idx].set_yticklabels(top_features['Feature'].values[::-1])
        axes[idx].set_xlabel('Importance')
        axes[idx].set_title('Random Forest - Top 10 Features')
        axes[idx].grid(True, alpha=0.3, axis='x')
        idx += 1
        
        if XGBOOST_AVAILABLE:
            axes[idx].barh(range(top_n), top_features['XGBoost'].values[::-1], 
                          alpha=0.7, color='orange')
            axes[idx].set_yticks(range(top_n))
            axes[idx].set_yticklabels(top_features['Feature'].values[::-1])
            axes[idx].set_xlabel('Importance')
            axes[idx].set_title('XGBoost - Top 10 Features')
            axes[idx].grid(True, alpha=0.3, axis='x')
            idx += 1
        
        plt.tight_layout()
        plt.savefig('boosting_feature_importance.png', dpi=300, bbox_inches='tight')
        print("\n✓ Plot saved as 'boosting_feature_importance.png'")
        plt.close()

# 6. ROC Curves Comparison
print("\n" + "=" * 60)
print("6. ROC Curves Comparison")
print("مقارنة منحنيات ROC")
print("=" * 60)

plt.figure(figsize=(10, 8))

# Random Forest
y_test_proba_rf = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_test_proba_rf)
auc_rf = roc_auc_score(y_test, y_test_proba_rf)
plt.plot(fpr_rf, tpr_rf, linewidth=2, label=f'Random Forest (AUC = {auc_rf:.4f})')

if XGBOOST_AVAILABLE and y_test_proba_xgb is not None:
    fpr_xgb, tpr_xgb, _ = roc_curve(y_test, y_test_proba_xgb)
    auc_xgb = roc_auc_score(y_test, y_test_proba_xgb)
    plt.plot(fpr_xgb, tpr_xgb, linewidth=2, label=f'XGBoost (AUC = {auc_xgb:.4f})')

if LIGHTGBM_AVAILABLE and y_test_proba_lgb is not None:
    fpr_lgb, tpr_lgb, _ = roc_curve(y_test, y_test_proba_lgb)
    auc_lgb = roc_auc_score(y_test, y_test_proba_lgb)
    plt.plot(fpr_lgb, tpr_lgb, linewidth=2, label=f'LightGBM (AUC = {auc_lgb:.4f})')

plt.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves Comparison')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('boosting_roc_curves.png', dpi=300, bbox_inches='tight')
print("\n✓ Plot saved as 'boosting_roc_curves.png'")
plt.close()

# 7. Learning Curve (XGBoost)
print("\n" + "=" * 60)
print("7. Learning Curve Example (XGBoost)")
print("مثال منحنى التعلم (XGBoost)")
print("=" * 60)

if XGBOOST_AVAILABLE:
    # Train with different number of estimators
    n_estimators_range = range(10, 201, 20)
    train_scores = []
    test_scores = []
    
    for n_est in n_estimators_range:
        xgb_temp = xgb.XGBClassifier(
            n_estimators=n_est,
            max_depth=5,
            learning_rate=0.1,
            random_state=42,
            eval_metric='logloss'
        )
        xgb_temp.fit(X_train, y_train)
        train_scores.append(accuracy_score(y_train, xgb_temp.predict(X_train)))
        test_scores.append(accuracy_score(y_test, xgb_temp.predict(X_test)))
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_estimators_range, train_scores, 'o-', label='Training Accuracy', linewidth=2)
    plt.plot(n_estimators_range, test_scores, 's-', label='Test Accuracy', linewidth=2)
    plt.xlabel('Number of Estimators')
    plt.ylabel('Accuracy')
    plt.title('XGBoost Learning Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('xgb_learning_curve.png', dpi=300, bbox_inches='tight')
    print("\n✓ Plot saved as 'xgb_learning_curve.png'")
    plt.close()

print("\n" + "=" * 60)
print("Example 2 Complete! ✓")
print("اكتمل المثال 2! ✓")
print("=" * 60)

if not XGBOOST_AVAILABLE or not LIGHTGBM_AVAILABLE:
    print("\nNote: Install missing packages for full functionality:")
    if not XGBOOST_AVAILABLE:
        print("  pip install xgboost")
    if not LIGHTGBM_AVAILABLE:
        print("  pip install lightgbm")

