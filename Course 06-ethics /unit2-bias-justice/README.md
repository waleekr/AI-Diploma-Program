# Unit 2: Bias, Justice, and Discrimination in AI
## التحيز والعدالة والتمييز في الذكاء الاصطناعي

### Learning Objectives

By the end of this unit, students will be able to:
- Identify different types of bias in AI systems (algorithmic, data, human)
- Understand and calculate fairness metrics (demographic parity, equalized odds, calibration)
- Detect bias in datasets and models using tools like fairlearn and aif360
- Analyze cases of algorithmic discrimination
- Implement bias mitigation techniques
- Evaluate trade-offs between different fairness definitions

---

## Topics Covered

1. **Types of Bias in AI**
   - Algorithmic bias
   - Data bias (historical, representation, measurement)
   - Human bias (confirmation, anchoring, selection)
   - Intersectional bias

2. **Fairness Metrics**
   - Demographic parity (statistical parity)
   - Equalized odds
   - Equal opportunity
   - Calibration
   - Individual fairness

3. **Bias Detection**
   - Dataset analysis for bias
   - Model output analysis
   - Using fairness toolkits (fairlearn, aif360)
   - Statistical tests for bias

4. **Algorithmic Discrimination**
   - Real-world case studies (COMPAS, facial recognition, hiring)
   - Protected attributes and sensitive features
   - Disparate impact vs. disparate treatment
   - Legal and social implications

5. **Bias Mitigation**
   - Pre-processing techniques (data balancing, reweighting)
   - In-processing techniques (fairness constraints, adversarial debiasing)
   - Post-processing techniques (calibration, threshold optimization)
   - Trade-offs and limitations

---

## Files Structure

- `examples/`: Bias detection code, fairness analysis examples, case studies
- `exercises/`: Practice problems on bias detection and mitigation
- `quizzes/`: Assessment quizzes
- `solutions/`: Solutions to exercises
- `tests/`: Unit tests and assessments

---

## Prerequisites

Before starting, ensure you have:
- Completed Unit 1 (Foundations of AI Ethics)
- Python 3.8+ installed
- All packages from `requirements.txt` installed (especially fairlearn, aif360)
- Basic understanding of machine learning models
- Familiarity with pandas and numpy

---

## How to Use This Unit

1. Start with `examples/` to see bias detection in action
2. Run code examples to understand fairness metrics
3. Analyze case studies of biased AI systems
4. Complete exercises in `exercises/` to practice bias detection
5. Check your solutions against `solutions/`
6. Take quizzes to assess your understanding

---

## Key Concepts

### Fairness Definitions

**Demographic Parity:** Equal positive prediction rates across groups
- Formula: P(Ŷ=1|A=a) = P(Ŷ=1|A=b) for all groups a, b

**Equalized Odds:** Equal true positive and false positive rates across groups
- Formula: P(Ŷ=1|Y=y, A=a) = P(Ŷ=1|Y=y, A=b) for all groups and outcomes

**Equal Opportunity:** Equal true positive rates across groups
- Formula: P(Ŷ=1|Y=1, A=a) = P(Ŷ=1|Y=1, A=b) for all groups

### Bias Types

- **Historical Bias:** Bias present in training data due to historical inequalities
- **Representation Bias:** Underrepresentation of certain groups in data
- **Measurement Bias:** Systematic errors in how data is collected
- **Aggregation Bias:** Using one model for diverse populations

---

## Learning Resources

### Recommended Reading
- "Weapons of Math Destruction" by Cathy O'Neil
- "Algorithmic Fairness" papers by various authors
- Fairlearn documentation
- AIF360 documentation

### Online Resources
- Algorithmic Justice League
- AI Now Institute
- Fairlearn GitHub repository
- AIF360 GitHub repository

### Tools
- **fairlearn:** Microsoft's fairness assessment and mitigation toolkit
- **aif360:** IBM's AI Fairness 360 toolkit
- **SHAP:** For understanding model predictions

---

## Assessment

- **Quiz 2:** Bias and Fairness (30 points)
- **Exercises:** Bias detection and fairness analysis
- **Test 2:** Bias Analysis (50 points)

---

## Next Steps

After completing this unit, you should:
- Be able to detect bias in AI systems
- Understand different fairness metrics
- Know how to implement bias mitigation techniques
- Be prepared to study privacy and security in Unit 3

