# Installation Guide | دليل التثبيت

## ⚠️ IMPORTANT: Avoid Library Conflicts | مهم: تجنب تعارض المكتبات

This guide ensures you install all libraries **without conflicts** that could cause errors.

---

## ✅ Recommended: Use Virtual Environment | بيئة افتراضية (موصى بها)

**WHY?** Virtual environments prevent conflicts with other Python projects on your computer.

### Step 1: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Libraries

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Verify Installation

**Quick check:**
```bash
pip check
```
If you see "No broken requirements found", you're good! ✅

**Test imports:**
```bash
python -c "import pandas, numpy, matplotlib, sklearn; print('All libraries imported successfully!')"
```

---

## 🔄 Alternative: Install Without Virtual Environment

**WARNING**: Only if you don't have other Python projects.

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip check  # Verify no conflicts
```

---

## 📋 Manual Installation (If Needed)

If `requirements.txt` causes issues, install in this order:

```bash
# 1. Core libraries first
pip install numpy>=1.24.0
pip install pandas>=2.0.0

# 2. Visualization
pip install matplotlib>=3.7.0
pip install seaborn>=0.12.0

# 3. Machine Learning & Fairness
pip install scikit-learn>=1.3.0
pip install fairlearn>=0.9.0

# 4. Jupyter support
pip install jupyter notebook ipykernel

# 5. Additional utilities
pip install aif360>=0.5.0  # For fairness analysis
```

---

## ⚠️ Known Compatibility Notes | ملاحظات التوافق

### ✅ Compatible Versions:
- **Python 3.8, 3.9, 3.10, 3.11**: All supported
- **NumPy 1.24+**: Works with all other libraries
- **Pandas 2.0+**: Requires NumPy 1.21+
- **Matplotlib 3.7+**: Compatible with NumPy 1.24+
- **Scikit-learn 1.3+**: Requires NumPy 1.17+, SciPy 1.3+
- **Fairlearn 0.9+**: For fairness analysis tools

---

## 🐛 Troubleshooting | حل المشاكل

### Problem: "No module named 'X'"
**Solution:** The library isn't installed. Run:
```bash
pip install X
```

### Problem: "Package conflicts"
**Solution:** Use a virtual environment (see Step 1 above)

### Problem: "Permission denied"
**Solution:** On macOS/Linux, try:
```bash
pip install --user -r requirements.txt
```

### Problem: "pip not found"
**Solution:** Install pip first:
```bash
python -m ensurepip --upgrade
```

---

## ✅ Verification Checklist

After installation, verify:

- [ ] `python --version` shows 3.8 or higher
- [ ] `pip check` shows no conflicts
- [ ] Can import pandas: `python -c "import pandas"`
- [ ] Can import numpy: `python -c "import numpy"`
- [ ] Can import matplotlib: `python -c "import matplotlib"`
- [ ] Can import sklearn: `python -c "import sklearn"`
- [ ] Jupyter notebook starts: `jupyter notebook`

---

**Last Updated:** 2025  
**Course:** AIAT 116 - Ethics of Artificial Intelligence

