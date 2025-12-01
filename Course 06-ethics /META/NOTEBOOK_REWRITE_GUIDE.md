# Notebook Rewrite Guide | دليل إعادة كتابة الدفاتر

## Status | الحالة

The "how and why" methodology has been partially applied to `01_ethical_frameworks.ipynb`. The notebook structure needs to be completed with proper cell separation.

---

## What Has Been Done | ما تم إنجازه

✅ **Cell 0 (Markdown)**: Complete with:
- Prerequisites section
- "Where This Fits" section  
- "The Story" section
- Learning Objectives

✅ **Cell 1 (Markdown)**: Part 1: Setting the Scene with BEFORE/AFTER

✅ **Cell 2 (Python)**: Library imports with detailed WHAT/WHY comments

✅ **Cell 3 (Markdown)**: Part 2: Understanding Ethical Frameworks with prerequisites, relationship, and story

✅ **Cell 4 (Python)**: Framework definitions with detailed inline comments

---

## What Still Needs to Be Done | ما يحتاج إلى إنجاز

### 1. Fix Cell Structure
- Cell 3 currently has markdown mixed with Python code
- Need to separate into proper markdown and code cells

### 2. Add Visualization Functions with HOW/WHY Comments
The visualization functions need to be rewritten with:
- Detailed docstrings explaining HOW IT WORKS
- Inline comments for every line (WHAT/WHY)
- Print statements showing progress
- BEFORE/AFTER visualization explanations

### 3. Add More Parts Following Course02 Pattern

**Part 3: Comparing Frameworks**
- BEFORE: We have frameworks but don't know how to compare them
- AFTER: We can visualize and compare framework strengths/weaknesses
- Code: Framework comparison visualization with detailed comments

**Part 4: Applying Frameworks to AI Scenarios**
- BEFORE: We know frameworks but don't know how to apply them
- AFTER: We can evaluate AI scenarios using different frameworks
- Code: Scenario analysis with step-by-step framework application

**Part 5: Summary and Takeaways**
- Summary of what we learned
- Key takeaways
- Next steps

---

## Template for Each Code Cell | قالب لكل خلية كود

```python
# Step X: [What this step does]
# [WHY this step is needed] - [WHAT it does]

# BEFORE: [State before this step]
# AFTER: [State after this step]

print("🔍 Starting [process]...")  # Start message: [WHAT] - [WHY]

# Initialize: [WHAT] - [WHY]
variable = value  # Purpose: [WHAT this does] - [WHY it's needed]

# Process: [WHAT] - [WHY]
for item in data:  # Loop through: [WHAT] - [WHY]
    result.append(item)  # Add to result: [WHAT] - [WHY]

print("✅ Step completed!")  # Success message: [WHAT] - [WHY]
```

---

## Template for Visualization Functions | قالب لوظائف التصور

```python
def visualize_comparison(data):
    """
    Visualize framework comparison.
    
    HOW IT WORKS:
    1. Extract data from frameworks dictionary
    2. Create bar chart with multiple series
    3. Add labels and formatting
    4. Save visualization
    
    ⏰ WHEN to use: After defining frameworks - see how they compare
    💡 WHY use: Visual understanding helps identify which frameworks are strongest
    """
    # Extract data: [WHAT] - [WHY]
    framework_names = [f['name_en'] for f in frameworks.values()]  # Get names: [WHAT] - [WHY]
    strengths = [f['strength'] for f in frameworks.values()]  # Get strengths: [WHAT] - [WHY]
    
    # Create figure: [WHAT] - [WHY]
    fig, ax = plt.subplots(figsize=(14, 8))  # Create plot: [WHAT] - [WHY]
    
    # Create bars: [WHAT] - [WHY]
    bars = ax.bar(x, strengths, width, label='Strengths', color='#2ecc71', alpha=0.8)  # Draw bars: [WHAT] - [WHY]
    
    # Add labels: [WHAT] - [WHY]
    ax.set_xlabel('Ethical Framework', fontsize=12, fontweight='bold')  # X-axis label: [WHAT] - [WHY]
    
    # Save: [WHAT] - [WHY]
    plt.savefig(output_path, dpi=300, bbox_inches='tight')  # Save image: [WHAT] - [WHY]
    print("✅ Saved: comparison.png")  # Success message: [WHAT] - [WHY]
```

---

## Next Steps | الخطوات التالية

1. **Complete `01_ethical_frameworks.ipynb`** following the template above
2. **Apply same methodology to other notebooks**:
   - `02_ethical_decision_making.ipynb`
   - `03_case_study_analysis.ipynb`
   - All Unit 2 examples
   - All Unit 3 examples
   - etc.

3. **Use the methodology guide** (`META/HOW_AND_WHY_METHODOLOGY.md`) as reference

---

**Last Updated:** 2025  
**Status:** In Progress - Methodology Guide Created, Example Notebook Partially Updated

