# Test 3: Privacy, Security, and Data Protection
## امتحان 3: الخصوصية والأمان وحماية البيانات

**Time Limit:** 60 minutes | **Marks:** 50 points

---

## Instructions
- Answer all questions
- Provide detailed explanations where required

---

## Part 1: Multiple Choice (15 points)

### Question 1 (3 points)
What is the main goal of differential privacy?
- A) Complete anonymity
- B) Protect individual privacy while allowing useful analysis
- C) No privacy
- D) Public data

**Answer:** B

---

### Question 2 (3 points)
What is a membership inference attack?
- A) Model improvement
- B) Determining if specific data was in training set
- C) Data cleaning
- D) Model training

**Answer:** B

---

### Question 3 (3 points)
What is homomorphic encryption?
- A) No encryption
- B) Computing on encrypted data without decryption
- C) Simple encryption
- D) Public encryption

**Answer:** B

---

### Question 4 (3 points)
What is the purpose of data anonymization?
- A) To identify individuals
- B) To protect privacy by removing identifiers
- C) To improve accuracy
- D) To speed up processing

**Answer:** B

---

### Question 5 (3 points)
What is secure multi-party computation?
- A) Single party computation
- B) Computing on data from multiple parties without revealing it
- C) Public computation
- D) No computation

**Answer:** B

---

## Part 2: Short Answer (20 points)

### Question 6 (10 points)
Explain differential privacy and its importance in AI. What is ε (epsilon) in differential privacy?

**Answer:**
Differential privacy is a mathematical framework that provides strong privacy guarantees. It ensures that the output of an analysis is roughly the same whether or not any individual's data is included. ε (epsilon) is the privacy parameter - smaller values mean stronger privacy but may reduce utility. It's important in AI to protect individual privacy while enabling useful machine learning.

---

### Question 7 (10 points)
Describe three types of security attacks on AI systems and how to defend against them.

**Answer:**
1. **Adversarial attacks**: Malicious inputs designed to fool models. Defense: Adversarial training, input validation
2. **Model inversion**: Reconstructing training data from model outputs. Defense: Differential privacy, output perturbation
3. **Data poisoning**: Injecting malicious training data. Defense: Data validation, anomaly detection, robust training

---

## Part 3: Case Study (15 points)

### Question 8 (15 points)
A healthcare AI system needs patient data for training. Discuss privacy-preserving approaches that could be used while maintaining model utility.

**Answer:**
1. **Differential Privacy**: Add noise to training process or outputs
2. **Federated Learning**: Train on distributed data without centralizing
3. **Homomorphic Encryption**: Train on encrypted data
4. **Data Anonymization**: Remove identifiers, use k-anonymity
5. **Secure Multi-party Computation**: Collaborate without sharing raw data
6. **Synthetic Data**: Generate privacy-preserving synthetic datasets
7. **Access Controls**: Strict access management and audit logs
8. **Regular Audits**: Monitor for privacy violations

---

## Grading Rubric | معايير التقييم

### Multiple Choice (15 points)
- 3 points per question

### Short Answer (20 points)
- Question 6: Explanation (6 points), Epsilon (4 points)
- Question 7: Three attacks (6 points), Defenses (4 points)

### Case Study (15 points)
- Approaches (10 points), Analysis (5 points)

---

**Total: 50 points**

---

**Good luck!** 🍀

