# Test 4: Interpretability, Transparency, and Accountability
## امتحان 4: قابلية التفسير والشفافية والمسؤولية

**Time Limit:** 60 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Provide detailed explanations where required

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is the main purpose of explainable AI?
- A) To improve accuracy
- B) To make AI decisions understandable
- C) To increase speed
- D) To reduce costs

**Answer:** B

---

### Question 2 (3 points)
What is the difference between post-hoc and inherently interpretable models?
- A) No difference
- B) Post-hoc explains after training, inherently interpretable are naturally explainable
- C) Both are the same
- D) Post-hoc is better

**Answer:** B

---

### Question 3 (3 points)
What does SHAP use to explain predictions?
- A) Random values
- B) Game theory (Shapley values)
- C) Simple averages
- D) No theory

**Answer:** B

---

### Question 4 (3 points)
When is interpretability most critical?
- A) Never
- B) High-stakes decisions (healthcare, finance, criminal justice)
- C) Always
- D) Only for simple models

**Answer:** B

---

### Question 5 (3 points)
What is an accountability framework?
- A) Model architecture
- B) Structure defining responsibility for AI decisions
- C) Data structure
- D) Training method

**Answer:** B

---

## Part 2: Short Answer (20 points)

### Question 6 (10 points)
Explain SHAP and LIME. What are their differences and when would you use each?

**Answer:**
- **SHAP**: Uses Shapley values from game theory to explain feature contributions. Provides consistent, theoretically grounded explanations. Better for understanding overall feature importance.
- **LIME**: Creates local linear approximations around individual predictions. Simpler, faster, but may be less consistent. Better for quick local explanations.
- Use SHAP for comprehensive analysis, LIME for quick local insights.

---

### Question 7 (10 points)
Describe the importance of transparency in different AI application domains. Provide examples.

**Answer:**
- **Healthcare**: Patients and doctors need to understand diagnoses and treatment recommendations
- **Finance**: Regulators and customers need to understand credit/lending decisions
- **Criminal Justice**: Defendants and judges need to understand risk assessments
- **Hiring**: Candidates need to understand why they were/weren't selected
- Transparency builds trust and enables accountability in all these domains.

---

## Part 3: Case Study (15 points)

### Question 8 (15 points)
A bank uses an AI system for loan approval. Design an accountability framework that ensures transparency and responsibility.

**Answer:**
1. **Documentation**: Clear documentation of model, data, and decision process
2. **Explainability**: Provide explanations for each decision (SHAP/LIME)
3. **Human Oversight**: Human review for edge cases and appeals
4. **Monitoring**: Regular audits of decisions and outcomes
5. **Bias Testing**: Regular fairness audits
6. **Appeal Process**: Clear process for challenging decisions
7. **Training**: Staff training on system limitations
8. **Compliance**: Adherence to regulations (fair lending, etc.)
9. **Transparency Reports**: Regular public reporting on system performance
10. **Responsibility Chain**: Clear assignment of responsibility at each level

---

## Grading Rubric | معايير التقييم

### Multiple Choice (15 points)
- 3 points per question

### Short Answer (20 points)
- Question 6: SHAP (3 points), LIME (3 points), Differences (2 points), When to use (2 points)
- Question 7: Importance (5 points), Examples (5 points)

### Case Study (15 points)
- Framework components (10 points), Depth of analysis (5 points)

---

**Total: 50 points**

---

**Good luck!** 🍀

