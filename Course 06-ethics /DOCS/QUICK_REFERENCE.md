# Quick Reference Guide | دليل المرجع السريع

## 🎯 Course Overview

**Course Code:** AIAT 116  
**Course Name:** Ethics of Artificial Intelligence | أخلاقيات الذكاء الاصطناعي  
**Units:** 5 units covering ethical foundations to governance

---

## 📚 Unit Summary

### Unit 1: Foundations of AI Ethics
- Ethical frameworks (utilitarianism, deontology, virtue ethics)
- Ethical decision-making
- Case studies

### Unit 2: Bias, Justice, and Discrimination
- Bias detection and metrics
- Fairness analysis
- Mitigation strategies

### Unit 3: Privacy, Security, and Data Protection
- Privacy principles
- GDPR compliance
- Privacy-preserving techniques

### Unit 4: Interpretability, Transparency, and Accountability
- Explainable AI (XAI)
- Model interpretability
- Accountability frameworks

### Unit 5: AI Governance, Regulations, and Future Challenges
- Governance models
- Regulatory frameworks
- Future challenges

---

## 🔑 Key Ethical Frameworks

### Utilitarianism
- **Focus:** Greatest good for greatest number
- **Application:** Maximize overall benefit

### Deontology
- **Focus:** Duty and rules
- **Application:** Follow ethical rules regardless of consequences

### Virtue Ethics
- **Focus:** Character and virtues
- **Application:** Develop virtuous character

---

## 📊 Fairness Metrics

### Demographic Parity
- Equal positive rates across groups
- Formula: P(Ŷ=1|A=a) = P(Ŷ=1|A=b)

### Equalized Odds
- Equal true positive and false positive rates
- Formula: TPR_a = TPR_b and FPR_a = FPR_b

### Calibration
- Equal positive predictive value across groups
- Formula: P(Y=1|Ŷ=1, A=a) = P(Y=1|Ŷ=1, A=b)

---

## 🔒 Privacy Principles

### GDPR Principles
1. Lawfulness, fairness, transparency
2. Purpose limitation
3. Data minimization
4. Accuracy
5. Storage limitation
6. Integrity and confidentiality
7. Accountability

### Privacy Techniques
- Differential privacy
- Federated learning
- Homomorphic encryption
- Secure multi-party computation

---

## 🔍 Interpretability Methods

### Model-Agnostic
- SHAP (SHapley Additive exPlanations)
- LIME (Local Interpretable Model-agnostic Explanations)
- Partial dependence plots

### Model-Specific
- Decision tree visualization
- Feature importance
- Attention mechanisms

---

## 📋 Common Python Libraries

```python
import pandas as pd          # Data manipulation
import numpy as np           # Numerical computing
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns        # Statistical visualization
from sklearn import ...      # Machine learning
from fairlearn import ...    # Fairness analysis
```

---

## 🚀 Quick Commands

### Setup
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Run Examples
```bash
# Jupyter notebook
jupyter notebook unit1-ethics-foundations/examples/01_ethical_frameworks.ipynb

# Python script
python unit1-ethics-foundations/examples/01_ethical_frameworks.py
```

### Verify Installation
```bash
pip check
python -c "import pandas, numpy, matplotlib, sklearn; print('OK')"
```

---

## 📁 File Structure Quick Reference

```
Course 06-ethics/
├── START_HERE.md                    # Read this first!
├── README.md                        # Course overview
├── STUDENT_PROGRESS_CHECKLIST.md    # Track progress
├── unit1-ethics-foundations/
│   ├── examples/                   # Code examples
│   ├── exercises/                  # Practice problems
│   ├── solutions/                  # Exercise solutions
│   └── quizzes/                    # Assessment quizzes
└── ... (similar for units 2-5)
```

---

## 💡 Study Tips

1. **Read unit README first** - Understand learning objectives
2. **Review examples** - See concepts in action
3. **Complete exercises** - Practice application
4. **Check solutions** - Learn from correct approaches
5. **Take quizzes** - Test understanding

---

**Last Updated:** 2025  
**Course:** AIAT 116 - Ethics of Artificial Intelligence

