# Instructor Guide - AIAT 115
## دليل المدرس - علم البيانات القابل للتوسع

### Quick Start Guide

This curriculum is designed for teaching Scalable Data Science using Python with NVIDIA RAPIDS for GPU acceleration. All materials are bilingual (Arabic/English).

---

## Course Structure Overview

### Unit 1: Introduction to Data Science (مقدمة في علم البيانات)
**Duration:** 2-3 weeks

**Key Topics:**
- Data science lifecycle and workflow
- Introduction to pandas and NumPy
- Introduction to cuDF (GPU-accelerated DataFrame)
- Data loading and exploration
- Statistical analysis

**Teaching Tips:**
1. Start with traditional pandas before introducing cuDF
2. Emphasize the data science workflow
3. Use real datasets for exploration
4. Show statistical summary techniques

---

### Unit 2: Data Cleaning and Preparation (تنظيف البيانات وتحضيرها)
**Duration:** 3-4 weeks

**Key Topics:**
- Handling missing values
- Removing duplicates
- Outlier detection and treatment
- Data transformation
- Feature engineering
- CPU vs GPU performance comparison

**Teaching Tips:**
1. Show real-world messy data examples
2. Compare different cleaning approaches
3. Demonstrate GPU speedup with large datasets
4. Emphasize data quality importance

---

### Unit 3: Data Visualization (تصوير البيانات)
**Duration:** 2-3 weeks

**Key Topics:**
- Matplotlib and Seaborn basics
- Interactive visualizations with Plotly
- Statistical visualizations
- Large dataset visualization techniques

**Teaching Tips:**
1. Start with basic plots before interactive ones
2. Show how to choose appropriate visualizations
3. Demonstrate plot customization
4. Address visualization of large datasets

---

### Unit 4: Introduction to Machine Learning (مقدمة في تعلم الآلة)
**Duration:** 3-4 weeks

**Key Topics:**
- Supervised learning basics
- Linear regression and classification
- Model training and evaluation
- scikit-learn vs cuML comparison
- Cross-validation

**Teaching Tips:**
1. Start with simple regression before classification
2. Emphasize model evaluation metrics
3. Compare CPU vs GPU performance
4. Show production considerations

---

### Unit 5: Scaling Data Science (توسيع نطاق علم البيانات)
**Duration:** 3-4 weeks

**Key Topics:**
- Distributed computing with Dask
- GPU-accelerated workflows
- Production-ready pipelines
- Performance optimization
- Memory management

**Teaching Tips:**
1. Emphasize scalability challenges
2. Show distributed computing concepts
3. Compare different scaling approaches
4. Focus on production deployment

---

## Teaching Methodology

### Recommended Approach

1. **Theory First (15-20 minutes)**
   - Explain concepts using slides or whiteboard
   - Use Arabic for key concepts, English for technical terms
   - Connect to real-world applications

2. **Live Coding (30-40 minutes)**
   - Walk through examples step by step
   - Explain each line of code
   - Show both CPU and GPU versions when applicable
   - Answer questions as you go

3. **Hands-On Practice (20-30 minutes)**
   - Students modify examples
   - Try exercises
   - Work in pairs for complex problems
   - Experiment with different parameters

4. **Review and Q&A (10-15 minutes)**
   - Review key concepts
   - Answer questions
   - Preview next topic
   - Discuss performance implications

### Best Practices

1. **Code Organization**
   - Always run examples before class
   - Test on both CPU and GPU (if available)
   - Prepare solutions in advance
   - Have fallback CPU versions for GPU examples

2. **Student Engagement**
   - Use real-world datasets when possible
   - Connect concepts to production scenarios
   - Encourage experimentation
   - Show performance comparisons

3. **Assessment**
   - Use exercises as homework
   - Create projects combining multiple units
   - Conduct quizzes on key concepts
   - Include scalability in final projects

---

## Technical Setup

### Prerequisites for Students

- Python 3.8+ installed
- Basic Python knowledge (variables, loops, functions)
- Familiarity with NumPy and Pandas helpful but not required
- **Optional:** NVIDIA GPU for GPU-accelerated examples

### Environment Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install CPU packages
pip install -r requirements.txt
```

### NVIDIA RAPIDS Installation (GPU)

#### Option 1: Conda Installation (Recommended)

```bash
# Create conda environment with RAPIDS
conda create -n rapids-env -c rapidsai -c conda-forge -c nvidia \
    cudf=23.08 cuml=23.08 python=3.10 cudatoolkit=11.8

conda activate rapids-env
```

#### Option 2: Docker Installation

```bash
# Pull RAPIDS container
docker pull rapidsai/rapidsai:23.08-cuda11.8-runtime-ubuntu22.04-py3.10

# Run container
docker run --gpus all --rm -it \
    -p 8888:8888 -p 8787:8787 -p 8786:8786 \
    rapidsai/rapidsai:23.08-cuda11.8-runtime-ubuntu22.04-py3.10
```

#### Option 3: pip Installation (Limited)

```bash
pip install cudf-cu11 cuml-cu11 --extra-index-url=https://pypi.nvidia.com
```

**Note:** Full RAPIDS functionality requires conda installation. Check [RAPIDS Installation Guide](https://rapids.ai/start.html) for latest instructions.

### Common Issues

1. **GPU Not Available**
   - Use CPU versions of examples
   - Explain GPU concepts theoretically
   - Consider cloud GPU options (Google Colab Pro, AWS)

2. **Import Errors**
   - Ensure all packages are installed
   - Check Python version compatibility (3.8+)
   - Verify CUDA version for RAPIDS

3. **Memory Issues**
   - Start with smaller datasets
   - Use chunking for large files
   - Monitor memory usage

4. **Visualization Issues**
   - Use `plt.show()` if plots don't display
   - Install Qt backend for better plots: `pip install PyQt5`
   - For notebooks, use `%matplotlib inline`

---

## Recommended Schedule

### 16-Week Semester Structure

**Weeks 1-3:** Unit 1 (Introduction to Data Science)
- Week 1: Data science lifecycle, pandas basics
- Week 2: Data loading and exploration
- Week 3: Introduction to cuDF, statistical analysis

**Weeks 4-7:** Unit 2 (Data Cleaning and Preparation)
- Week 4: Handling missing values and duplicates
- Week 5: Outlier detection and data transformation
- Week 6: Feature engineering
- Week 7: CPU vs GPU performance, review

**Weeks 8-10:** Unit 3 (Data Visualization)
- Week 8: Matplotlib and Seaborn
- Week 9: Interactive visualizations (Plotly)
- Week 10: Large dataset visualization

**Weeks 11-14:** Unit 4 (Introduction to Machine Learning)
- Week 11: Supervised learning basics, regression
- Week 12: Classification algorithms
- Week 13: Model evaluation and metrics
- Week 14: scikit-learn vs cuML comparison

**Weeks 15-16:** Unit 5 (Scaling Data Science)
- Week 15: Distributed computing with Dask
- Week 16: GPU workflows, production pipelines, final projects

---

## Additional Resources

### Suggested Datasets

1. **House Prices** (for regression and scaling)
   - Kaggle: House Prices Dataset
   - Good for demonstrating scalability

2. **Large-scale E-commerce** (for distributed computing)
   - Transaction data
   - Customer behavior data

3. **Financial Data** (for time series and scaling)
   - Stock prices
   - Market data

4. **Synthetic Large Datasets** (for GPU demonstration)
   - Generate with NumPy/cuPy
   - Control size for performance testing

### Useful Links

- **RAPIDS Documentation:** https://rapids.ai/docs.html
- **cuDF Documentation:** https://docs.rapids.ai/api/cudf/stable/
- **cuML Documentation:** https://docs.rapids.ai/api/cuml/stable/
- **Dask Documentation:** https://docs.dask.org/
- **Scikit-learn Documentation:** https://scikit-learn.org/
- **Pandas Documentation:** https://pandas.pydata.org/

---

## Assessment Suggestions

1. **Weekly Exercises** (30%)
   - Complete exercises from each unit
   - Submit solutions via code repository
   - Include performance comparisons

2. **Midterm Project** (25%)
   - Apply Unit 1-2 concepts
   - Clean and prepare real dataset
   - Compare CPU vs GPU performance

3. **Final Project** (35%)
   - Complete scalable data science pipeline
   - Handle large dataset
   - Deploy to production-like environment
   - Performance optimization report

4. **Participation** (10%)
   - Class attendance and engagement
   - Code reviews and discussions
   - Performance optimization suggestions

---

## GPU Access Options

If students don't have GPUs, consider:

1. **Cloud Options:**
   - Google Colab Pro (GPU access)
   - AWS SageMaker (free tier available)
   - Azure ML (free tier available)

2. **Institutional Options:**
   - University GPU clusters
   - Lab computers with GPUs
   - Remote GPU servers

3. **Learning Without GPU:**
   - Focus on CPU examples
   - Understand GPU concepts theoretically
   - Use small datasets for practice
   - Review GPU code without running

---

## Contact and Support

For questions about curriculum:
- Review example code and comments
- Check solutions directory
- Consult main README.md

For technical issues:
- Ensure all dependencies are installed
- Check Python version compatibility
- Verify CUDA version for RAPIDS
- Test examples before class

For RAPIDS-specific issues:
- Visit RAPIDS documentation
- Check RAPIDS GitHub issues
- Consult RAPIDS community forums

---

## Notes for Future Enhancement

Consider adding:
- Jupyter Notebook versions of examples
- Video tutorials for complex topics
- More real-world datasets
- Project templates
- Automated testing scripts
- Docker containers with pre-installed RAPIDS
- Performance benchmarking exercises

---

**Last Updated:** 2024  
**Version:** 1.0

