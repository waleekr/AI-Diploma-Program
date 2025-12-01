# Teaching Guide: Using Presentations with Code Examples
## دليل التدريس: استخدام العروض التقديمية مع أمثلة الكود

### 🎯 Overview

This guide explains how to effectively teach Course 05 using the **PPTX/PDF presentation files** together with **matching code examples** to ensure students learn both theory and practice.

---

## 📚 Teaching Methodology

### Two-Part Learning Approach

1. **Theory (Presentations)**: Students study PPTX/PDF files
2. **Practice (Code)**: Students run matching code examples

This ensures students:
- ✅ Understand concepts (from presentations)
- ✅ See implementations (from code)
- ✅ Practice skills (hands-on coding)
- ✅ Visualize results (plots matching presentations)

---

## 🗺️ Presentation-to-Code Mapping

### Unit 1: Introduction to Data Science

| Session | Presentation | Code Example | Duration |
|---------|-------------|--------------|----------|
| 1 | `01.pptx` | `unit1-introduction/examples/01_data_science_intro.py` | 60-90 min |
| 2 | `02.pptx` | `unit1-introduction/examples/02_pandas_numpy_basics.py` | 60-90 min |
| 3 | `03.pptx` | `unit1-introduction/examples/03_cudf_introduction.py` | 60-90 min |

---

### Unit 2: Data Cleaning and Preparation

| Session | Presentation | Code Example | Duration |
|---------|-------------|--------------|----------|
| 4 | `04.pptx` | `unit2-cleaning/examples/04_data_loading.py` | 60-90 min |
| 5 | `05.pptx` | `unit2-cleaning/examples/05_missing_values_duplicates.py` | 60-90 min |
| 6 | `06.pptx` | `unit2-cleaning/examples/06_outliers_transformation.py` | 60-90 min |

---

### Unit 3: Data Visualization

| Session | Presentation | Code Example | Duration |
|---------|-------------|--------------|----------|
| 7 | `07.pptx` | `unit3-visualization/examples/07_matplotlib_basics.py` | 60-90 min |
| 8 | `08.pptx` | `unit3-visualization/examples/08_seaborn_plots.py` | 60-90 min |
| 9 | `09.pptx` | `unit3-visualization/examples/09_plotly_interactive.py` | 60-90 min |

---

### Unit 4: Introduction to Machine Learning

| Session | Presentation | Code Example | Duration |
|---------|-------------|--------------|----------|
| 10 | `10.pptx` | `unit4-ml-intro/examples/10_linear_regression.py` | 90 min |
| 11 | `11.pptx` | `unit4-ml-intro/examples/11_classification.py` | 90 min |
| 12 | `12.pptx` | `unit4-ml-intro/examples/12_model_evaluation.py` | 90 min |
| 13 | `13.pptx` | `unit4-ml-intro/examples/13_cpu_vs_gpu_ml.py` | 90 min |

---

### Unit 5: Scaling Data Science

| Session | Presentation | Code Example | Duration |
|---------|-------------|--------------|----------|
| 14 | `14.pptx` | `unit5-scaling/examples/14_dask_distributed.py` | 90 min |
| 15 | `15.pptx` | `unit5-scaling/examples/15_rapids_workflows.py` | 90 min |
| 16 | `16.pdf` | `unit5-scaling/examples/16_production_pipelines.py` | 90 min |
| 17 | `17.pdf` | `unit5-scaling/examples/17_performance_optimization.py` | 90 min |
| 18 | `18.pdf` | `unit5-scaling/examples/18_large_datasets.py` | 90 min |
| 19 | `19.pdf` | `unit5-scaling/examples/19_deployment.py` | 90 min |

---

## 📋 Recommended Teaching Flow

### For Each Session (90 minutes)

#### Part 1: Theory Presentation (30-40 minutes)
1. **Present the PPTX/PDF**
   - Explain concepts from slides
   - Use Arabic for explanations, English for technical terms
   - Answer questions

2. **Key Points to Emphasize**
   - Main concepts from presentation
   - Why these concepts matter
   - Real-world applications

#### Part 2: Code Demonstration (30-40 minutes)
1. **Open the matching code file**
   - Walk through code line by line
   - Explain each section
   - Run the code live

2. **Show Outputs**
   - Compare code output with presentation slides
   - Point out visualizations matching presentation
   - Explain results

#### Part 3: Hands-On Practice (15-20 minutes)
1. **Students modify code**
   - Try different parameters
   - Experiment with examples
   - Ask questions

2. **Troubleshoot together**
   - Help with errors
   - Explain common issues
   - Provide tips

---

## 💡 Teaching Tips

### 1. **Preparation**
- ✅ Review presentation file before class
- ✅ Run code examples yourself first
- ✅ Prepare questions to ask students
- ✅ Have solutions ready

### 2. **During Presentation**
- Use presentation as your guide
- Pause for questions
- Relate to real-world examples
- Check understanding periodically

### 3. **During Code Demo**
- Type code live (don't just show finished file)
- Explain each section
- Run code multiple times with different inputs
- Show errors and how to fix them

### 4. **Student Engagement**
- Ask students to predict outputs
- Have students type along
- Encourage experimentation
- Pair students for complex tasks

---

## 🎯 Learning Objectives Alignment

Each code example should:
- ✅ Match presentation content
- ✅ Demonstrate concepts from slides
- ✅ Generate visualizations shown in presentations
- ✅ Include bilingual comments
- ✅ Reference the presentation file number

---

## 📝 Example Code Template

Every code file should start with:

```python
"""
Unit X - Example Y: [Topic Name]
[Arabic Title]

This example corresponds to: [XX].pptx or [XX].pdf
This file demonstrates concepts covered in that presentation.

Key Topics from Presentation:
- Topic 1
- Topic 2
- Topic 3
"""

# Code implementation here
```

---

## ✅ Assessment Alignment

### Quizzes
- Questions based on presentation content
- Concepts from slides
- Applications from code examples

### Exercises
- Practice tasks related to presentation topics
- Build on code examples shown
- Apply concepts from slides

### Projects
- Combine multiple presentations/units
- Real-world applications
- Show mastery of concepts

---

## 🔄 Weekly Schedule Example

### Week 1: Unit 1 - Introduction to Data Science

**Monday:**
- Presentation: `01.pptx` (Data Science Introduction)
- Code: `01_data_science_intro.py`
- Exercise: Basic data science workflow

**Wednesday:**
- Presentation: `02.pptx` (pandas & NumPy)
- Code: `02_pandas_numpy_basics.py`
- Exercise: Data manipulation practice

**Friday:**
- Presentation: `03.pptx` (cuDF Introduction)
- Code: `03_cudf_introduction.py`
- Exercise: CPU vs GPU comparison

---

## 📊 Progress Tracking

Track which presentations have been:
- ✅ Presented in class
- ✅ Code examples demonstrated
- ✅ Exercises completed
- ✅ Quizzes taken

---

## 🆘 Common Issues

### Issue: Students don't see connection between PPTX and code
**Solution:** Explicitly reference slides while coding, show side-by-side

### Issue: Code doesn't match presentation content
**Solution:** Ensure code examples align with presentation topics, update as needed

### Issue: Students struggle with concepts
**Solution:** Use presentation for theory, code for practice, exercises for application

---

## 🎓 Success Metrics

Students should be able to:
- ✅ Explain concepts from presentations
- ✅ Implement concepts in code
- ✅ Modify examples independently
- ✅ Apply to new problems
- ✅ Create visualizations matching presentations

---

**Remember: Presentations provide theory, Code provides practice - Together they create complete learning!** ✅

