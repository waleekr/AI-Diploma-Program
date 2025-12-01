# ✅ SVM AttributeError Fixed
## إصلاح خطأ AttributeError في SVM

---

## Problem / المشكلة

The SVM models were created without `probability=True`, causing an AttributeError when trying to use `predict_proba()`:

```python
AttributeError: predict_proba is not available when probability=False
```

### Root Cause / السبب الجذري

SVC models need `probability=True` to enable probability estimation:
- Without it, only `predict()` works
- With it, both `predict()` and `predict_proba()` work

---

## Solution / الحل

✅ **Added `probability=True` to all SVC models** that use `predict_proba()`:

1. **svm_linear**: `SVC(kernel='linear', C=1.0, probability=True, random_state=42)`
2. **svm_rbf**: `SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)`
3. **svm_poly**: `SVC(kernel='poly', degree=3, C=1.0, probability=True, random_state=42)`

---

## Fixed Notebook / الدفتر المعدل

✅ **`unit3-classification/examples/03_svm.ipynb`**

### Changes Made / التغييرات:

1. ✅ Added `probability=True` to all SVC models
2. ✅ Fixed missing newlines in plotting cells
3. ✅ All cells properly formatted

---

## Verification / التحقق

### Before:
```python
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
y_test_proba_rbf = svm_rbf.predict_proba(X_test_scaled)[:, 1]  # ❌ Error!
```

### After:
```python
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True, random_state=42)
y_test_proba_rbf = svm_rbf.predict_proba(X_test_scaled)[:, 1]  # ✅ Works!
```

---

## Result / النتيجة

✅ **AttributeError resolved**
✅ **All SVC models can now use `predict_proba()`**
✅ **ROC curves and probability-based metrics will work**

---

**✅ The SVM notebook is now fully functional!**
**دفتر SVM يعمل الآن بشكل كامل!**

