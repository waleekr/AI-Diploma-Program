# ✅ SVM predict_proba() Error - Explanation
## شرح خطأ predict_proba() في SVM

---

## Error / الخطأ

```
AttributeError: predict_proba is not available when probability=False
```

## Cause / السبب

This error happens when you try to use `predict_proba()` on an SVM model that was created **without** `probability=True`.

### Why It Happens / لماذا يحدث

1. **Cell Execution Order**: You ran Cell 11 before Cell 10
2. **Cell 10** creates the model: `svm_rbf = SVC(..., probability=True, ...)`
3. **Cell 11** uses the model: `svm_rbf.predict_proba(...)`
4. If Cell 10 wasn't executed, the model doesn't exist or wasn't created with `probability=True`

---

## Solution / الحل

### ✅ **Run Cells in Order**

1. **Run Cell 10 FIRST** (creates `svm_rbf` with `probability=True`)
2. **Then run Cell 11** (uses `predict_proba()`)

### ✅ **Or Restart Kernel and Run All**

1. **Kernel → Restart Kernel**
2. **Cell → Run All**

This ensures all cells execute in the correct order.

---

## Verification / التحقق

The notebook structure is **CORRECT**:

- ✅ Cell 10: Creates `svm_rbf = SVC(..., probability=True, ...)`
- ✅ Cell 11: Uses `svm_rbf.predict_proba(...)`
- ✅ All models that need `predict_proba()` have `probability=True`

---

## Important Note / ملاحظة مهمة

**All SVM models in the notebook are correctly configured:**

- ✅ `svm_linear` - has `probability=True`
- ✅ `svm_rbf` - has `probability=True`  
- ✅ `svm_poly` - has `probability=True`

The error is a **runtime/execution order issue**, not a code problem.

---

**✅ Fix: Run cells in order, or restart kernel and run all!**
**الإصلاح: قم بتشغيل الخلايا بالترتيب، أو أعد تشغيل النواة وقم بتشغيل الكل!**

