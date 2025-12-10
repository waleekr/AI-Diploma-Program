# Repository Cleanup Plan | خطة تنظيف المستودع

## Files/Folders to Remove (Not Student-Facing)

### 1. Internal Development Files
- META/ folders (internal metadata)
- SCRIPTS/ folders (development scripts)
- Fix/convert scripts (*_fix*.py, *convert*.py, etc.)
- Setup scripts (setup_course.py, create_notebooks.py, etc.)

### 2. Internal Documentation
- FINAL_STATUS.md files
- *REVIEW*.md files
- *NOTEBOOK_REVIEW*.md files
- Internal comparison/status files (except STRUCTURE_ALIGNMENT_VERIFICATION.md)

### 3. Development Artifacts
- .code-workspace files
- Internal JSON files in META/
- Temporary files

### 4. Source Files (if not needed)
- .pptx files (if extracted to notebooks)
- Duplicate PDFs in course-content/

## Files to Keep

### Student-Facing Content
- README.md files
- START_HERE.md files
- STUDENT_PROGRESS_CHECKLIST.md files
- All examples/ (both .py and .ipynb)
- All exercises/
- All solutions/
- All quizzes/
- All projects/
- DOCS/ (if student-facing)
- QUIZZES/ (root level)
- PROJECTS/ (root level)

### Important Documentation
- STRUCTURE_ALIGNMENT_VERIFICATION.md (useful reference)
- SEMESTER2_OFFICIAL_GOALS.md (useful reference)
- .gitignore
- .gitattributes
- requirements.txt

