# Quick Run Guide
## دليل التشغيل السريع

### ✅ You're Ready!

You're in the `(course2)` conda environment and packages are installed. You can now run any example file!

### 🚀 Running Example Files

#### Option 1: Run a Python Script
```bash
# Example 1: Introduction to Data Science
python unit1-introduction/examples/01_data_science_intro.py

# Example 2: pandas & NumPy Basics
python unit1-introduction/examples/02_pandas_numpy_basics.py

# Example 3: cuDF Introduction
python unit1-introduction/examples/03_cudf_introduction.py
```

#### Option 2: Run a Jupyter Notebook
```bash
# Start Jupyter Notebook server
jupyter notebook

# Then open any .ipynb file in the browser
# Example: unit1-introduction/examples/01_data_science_intro.ipynb
```

#### Option 3: Use JupyterLab (if installed)
```bash
jupyter lab
```

### 📊 All Available Examples

#### Unit 1: Introduction to Data Science
- `01_data_science_intro.py` / `.ipynb` - Data science lifecycle
- `02_pandas_numpy_basics.py` / `.ipynb` - pandas & NumPy basics
- `03_cudf_introduction.py` / `.ipynb` - GPU-accelerated DataFrames

#### Unit 2: Data Cleaning and Preparation
- `04_data_loading.py` / `.ipynb` - Advanced data loading
- `05_missing_values_duplicates.py` / `.ipynb` - Missing values & duplicates
- `06_outliers_transformation.py` / `.ipynb` - Outliers & transformations

#### Unit 3: Data Visualization
- `07_matplotlib_basics.py` / `.ipynb` - Matplotlib fundamentals
- `08_seaborn_plots.py` / `.ipynb` - Seaborn statistical plots
- `09_plotly_interactive.py` / `.ipynb` - Interactive Plotly

#### Unit 4: Machine Learning
- `10_linear_regression.py` / `.ipynb` - Linear regression
- `11_classification.py` / `.ipynb` - Classification algorithms
- `12_model_evaluation.py` / `.ipynb` - Model evaluation metrics
- `13_cpu_vs_gpu_ml.py` / `.ipynb` - CPU vs GPU ML comparison

#### Unit 5: Scaling Data Science
- `14_dask_distributed.py` / `.ipynb` - Dask distributed computing
- `15_rapids_workflows.py` / `.ipynb` - RAPIDS workflows
- `16_production_pipelines.py` / `.ipynb` - Production pipelines
- `17_performance_optimization.py` / `.ipynb` - Performance optimization
- `18_large_datasets.py` / `.ipynb` - Large dataset handling
- `19_deployment.py` / `.ipynb` - Deployment strategies

### 💡 Tips

1. **Start with Unit 1** - Examples build on each other
2. **Use Jupyter Notebooks** - Better for learning and experimentation
3. **Check outputs** - Each example generates visualizations (saved as PNG files)
4. **Read comments** - All files have bilingual comments (Arabic/English)

### 🐛 Troubleshooting

If you get an import error:
```bash
# Make sure you're in the conda environment
conda activate course2

# Verify packages
python -c "import pandas; print('OK')"
```

If Arabic text doesn't display in plots:
- Check `ARABIC_FONT_FIX.md` for font setup
- The font configuration is already in all files!

### 📁 File Structure

```
Course 05 _ /
├── unit1-introduction/examples/    # 3 examples
├── unit2-cleaning/examples/        # 3 examples
├── unit3-visualization/examples/   # 3 examples
├── unit4-ml-intro/examples/        # 4 examples
└── unit5-scaling/examples/         # 6 examples
```

Each example has:
- ✅ Python script (`.py`)
- ✅ Jupyter notebook (`.ipynb`)
- ✅ Arabic font support
- ✅ Bilingual comments
- ✅ Visualizations

---

**Ready to start?** Try running:
```bash
python unit1-introduction/examples/01_data_science_intro.py
```

