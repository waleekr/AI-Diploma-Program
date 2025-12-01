# AIAT 115 - Scalable Data Science | علم البيانات القابل للتوسع

## 🚀 NEW STUDENTS: START HERE! | الطلاب الجدد: ابدأ من هنا!

**👉 If you're a new student, read `START_HERE.md` FIRST!**  
**👉 إذا كنت طالباً جديداً، اقرأ `START_HERE.md` أولاً!**

The `START_HERE.md` file contains:
- ✅ Day 1 setup instructions
- ✅ Step-by-step installation guide
- ✅ Learning sequence
- ✅ Progress tracker
- ✅ Troubleshooting tips

**Don't skip it!** It will save you time and confusion.

---

## Course Overview | نظرة عامة على الدورة

This course provides comprehensive training in scalable data science techniques using Python and NVIDIA RAPIDS. Students will learn to process, clean, visualize, and model data at scale through hands-on coding examples and exercises.

**Course Code:** AIAT 115  
**Language:** Bilingual (Arabic/English)

---

## Prerequisites | المتطلبات الأساسية

**Python Version**: Python 3.8+ required (3.10 or 3.11 recommended)

**Knowledge**: Students should have:
- Basic Python programming knowledge (variables, functions, classes)
- Familiarity with NumPy and Pandas (helpful but will be covered)

**Setup**: See `DOCS/` folder for detailed guides and `requirements.txt` for dependencies

---

## 📁 Clean Folder Structure | هيكل المجلد النظيف

```
📦 Course Root
│
├── 📄 README.md                        📖 This file
├── 📄 START_HERE.md                    ⭐ READ THIS FIRST!
├── 📄 STUDENT_PROGRESS_CHECKLIST.md    ✅ Track progress
├── 📄 requirements.txt                 📦 Dependencies
│
├── 📂 unit1-introduction/              📚 Unit 1 (3 examples)
├── 📂 unit2-cleaning/                  📚 Unit 2 (3 examples)
├── 📂 unit3-visualization/             📚 Unit 3 (3 examples)
├── 📂 unit4-ml-intro/                 📚 Unit 4 (4 examples)
├── 📂 unit5-scaling/                   📚 Unit 5 (6 examples)
├── 📖 DOCS/                            📄 Documentation
└── 📊 META/                            📈 Course Metadata
```

**See `META/FOLDER_STRUCTURE.md` for complete structure details.**

---

## Quick Start | البدء السريع

1. **Read:** `START_HERE.md`
2. **Install:** Libraries (see `DOCS/SETUP_INSTRUCTIONS.md`)
3. **Start:** `unit1-introduction/examples/01_data_science_intro.py` (or `.ipynb`)
4. **Track:** Use `STUDENT_PROGRESS_CHECKLIST.md`

---

## 📚 Course Content | محتوى الدورة

### Unit 1: Introduction to Data Science | مقدمة في علم البيانات
**Folder**: `unit1-introduction/`

**Topics Covered**:
- Data science lifecycle
- Pandas DataFrame operations
- NumPy array operations
- cuDF introduction (GPU-accelerated DataFrame)
- Basic data exploration and statistics

**Start Here**: `unit1-introduction/examples/01_data_science_intro.py` (or `.ipynb`)

---

### Unit 2: Data Cleaning and Preparation | تنظيف البيانات وتحضيرها
**Folder**: `unit2-cleaning/`

**Topics Covered**:
- Advanced data loading techniques
- Missing value handling strategies
- Duplicate detection and removal
- Outlier detection and treatment
- Data transformation and normalization

---

### Unit 3: Data Visualization | تصوير البيانات
**Folder**: `unit3-visualization/`

**Topics Covered**:
- Matplotlib basics (static plots)
- Seaborn statistical visualizations
- Plotly interactive visualizations

---

### Unit 4: Introduction to Machine Learning | مقدمة في تعلم الآلة
**Folder**: `unit4-ml-intro/`

**Topics Covered**:
- Linear regression
- Classification algorithms
- Model evaluation and metrics
- CPU (scikit-learn) vs GPU (cuML) comparison
- Cross-validation

---

### Unit 5: Scaling Data Science | توسيع نطاق علم البيانات
**Folder**: `unit5-scaling/`

**Topics Covered**:
- Distributed computing with Dask
- RAPIDS GPU workflows
- Production pipeline design
- Performance optimization
- Handling large datasets
- Deployment strategies

---

## Learning Path | مسار التعلم

```
Python Basics (Prerequisites)
    ↓
Unit 1: Introduction to Data Science
    ↓
Unit 2: Data Cleaning and Preparation
    ↓
Unit 3: Data Visualization
    ↓
Unit 4: Introduction to Machine Learning
    ↓
Unit 5: Scaling Data Science
    ↓
Advanced Topics (Deep Learning, Big Data, etc.)
```

---

## 📖 Documentation | التوثيق

All documentation is in the `DOCS/` folder:

- **SETUP_INSTRUCTIONS.md** - Detailed installation instructions
- **STUDENT_LEARNING_GUIDE.md** - Learning path guide
- **INSTRUCTOR_GUIDE.md** - Teaching guide
- **TEACHING_WITH_PRESENTATIONS.md** - Using presentations with code

See `DOCS/README.md` for complete list.

---

## 📝 Assessment | التقييم

- **Quizzes:** `QUIZZES/` folder
- **Exercises:** Each unit contains exercises with solutions
- **Rubrics:** `ASSESSMENTS/` folder
- **Self-Assessment:** `SELF_ASSESSMENT/` folder

---

## 📦 Required Libraries | المكتبات المطلوبة

- **Data Processing:** pandas, numpy
- **GPU-Accelerated:** cudf, cuml (via RAPIDS)
- **Machine Learning:** scikit-learn
- **Visualization:** matplotlib, seaborn, plotly
- **Distributed Computing:** dask
- **Utilities:** jupyter, ipython

See `requirements.txt` for complete list with versions.

---

## 💻 GPU vs CPU

This course teaches both traditional CPU-based data science and modern GPU-accelerated approaches:

- **CPU Examples:** Use pandas, scikit-learn (works on any machine)
- **GPU Examples:** Use cuDF, cuML from RAPIDS (requires NVIDIA GPU)

Students without GPUs can follow along with CPU examples and understand GPU concepts theoretically.

---

## 🆘 Need Help? | تحتاج مساعدة?

- **Installation issues?** → Check `DOCS/` folder
- **Questions?** → See `START_HERE.md` troubleshooting section
- **Progress tracking?** → Use `STUDENT_PROGRESS_CHECKLIST.md`

---

## 📊 Course Status | حالة الدورة

**Status:** ✅ Complete

- ✅ All 5 units present with examples and exercises
- ✅ All documentation complete
- ✅ All assessment materials ready
- ✅ Clean folder structure

---

## 📄 License | الترخيص

Educational use - Tuwaiq Academy

---

**Created for**: AIAT 115 - Scalable Data Science  
**Language Support**: Arabic & English  
**Last Updated**: 2025
