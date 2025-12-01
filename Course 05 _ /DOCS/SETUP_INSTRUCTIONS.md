# Quick Setup Instructions
## تعليمات الإعداد السريع

### The Problem
The error shows you're running Python files with the **system Python** (`/usr/bin/python3`) instead of your **conda environment Python** where packages are installed.

### The Solution

#### Option 1: Use Conda Python Directly (Recommended)

Instead of:
```bash
/usr/bin/python3 file.py
```

Use:
```bash
python file.py
```

Or specify the conda Python path:
```bash
/opt/anaconda3/bin/python file.py
```

#### Option 2: Activate Conda Environment First

```bash
# Activate your conda environment (if you have one)
conda activate course2  # or your environment name

# Then run the script
python unit1-introduction/examples/02_pandas_numpy_basics.py
```

#### Option 3: Install Packages in System Python (Not Recommended)

If you want to use system Python, install packages there:
```bash
/usr/bin/python3 -m pip install pandas numpy matplotlib seaborn
```

### Verify Installation

Check if pandas is available:
```bash
python -c "import pandas; print('✓ pandas is installed')"
```

### Running Jupyter Notebooks

For notebooks, make sure to:
1. Activate your conda environment
2. Start Jupyter from that environment:
   ```bash
   conda activate course2  # or your env
   jupyter notebook
   ```
3. Select the correct kernel in Jupyter

### Quick Test

Try running this command to test:
```bash
cd "/Users/abdullah/Downloads/Course 05 _ "
python unit1-introduction/examples/02_pandas_numpy_basics.py
```

If you see an error, check:
1. ✅ Are you using `python` (conda) or `/usr/bin/python3` (system)?
2. ✅ Are packages installed in the Python you're using?
3. ✅ Is your conda environment activated?

---

## Installation Status

✅ **Conda Base Environment:** Packages are installed here
❌ **System Python:** Packages are NOT installed here

**Solution:** Always use conda Python (`python`) instead of system Python (`/usr/bin/python3`)

