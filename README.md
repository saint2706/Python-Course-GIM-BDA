# Python Course - GIM BDA

This repository contains learning materials, exercises, and examples for a Python course focused on data analysis and business analytics.

## Repository Structure

### 📚 Exercises (`exercises/`)
Practice notebooks and exercises covering Python fundamentals, organized with sequential numbering:
- `01-basics-list-dict-questions.ipynb` - Basic data structures: Lists, dictionaries, tuples, sets
- `02-nested-tuple-set-questions.ipynb` - Advanced nested data structures
- `03-control-flow-questions.ipynb` - Conditionals and loops
- `03-list-comprehension-questions.ipynb` - List comprehensions
- `04-list-lambda-map-filter-questions.ipynb` - Lambda functions, map, filter operations
- `05-python-functions-questions.ipynb` - Function definitions and usage
- `06-previous-year-questions.ipynb` - Practice questions from previous exams
- `07-08-sf-salaries-exercise.ipynb` - San Francisco salaries exercise
- `penguins-eda-questions-valid.ipynb` - Exploratory Data Analysis exercise
- **solved/**: Solutions to class problems and exercises with standardized naming

### 📝 Assignments (`assignments/`)
Student assignment submissions organized by assignment number:
- **assignment-1/**: First assignment submissions from different students

### 🐼 Pandas Basics (`pandas-basics/`)
Introduction to Pandas and fundamental operations, organized sequentially:
- `01-introduction-to-pandas.ipynb` - Getting started with Pandas
- `02-operations.ipynb` - Basic operations and manipulations
- `03-groupby.ipynb` - Grouping and aggregation operations
- `04-data-input-output.ipynb` - Reading and writing data files
- `05-merging-joining-concatenating.ipynb` - Combining DataFrames

### 🔧 Data Processing (`data-processing/`)
Notebooks and examples for data manipulation and cleaning:
- **subsetting-in-pandas.ipynb**: Data filtering and selection techniques
- **duplicates.ipynb**: Detection and handling of duplicate records
- **outlier-detection-treatment.ipynb**: Outlier detection and treatment
- **missing-values.ipynb**: Basic missing value handling
- **missing-value-regression.ipynb**: Advanced imputation techniques
- **missing-values/** subdirectory:
  - `handling-missing-values.ipynb` - Comprehensive missing data techniques
  - `missing-data.ipynb` - Missing data patterns and strategies
- **import-export/** subdirectory: Data import/export operations with various formats (CSV, Excel, text)

### ⚙️ Feature Engineering (`feature-engineering/`)
Advanced data transformation and feature engineering techniques:
- `categorical-encoding-techniques.ipynb` - Label encoding and one-hot encoding
- `label-onehot-encoding.ipynb` - Encoding categorical variables
- `binning.ipynb` - Data discretization and bucketing strategies
- `data-transform.ipynb` - Normalization, standardization, logarithmic transforms
- `data-descritisation-bucketing.txt` - Notes on discretization techniques
- **examples/** subdirectory: Practical examples with sales and student datasets
  - Feature extraction workflows
  - Feature splitting techniques
  - Label encoding demonstrations

### 📊 Statistics (`statistics/`)
Statistical analysis and linear regression:
- `bivariate-and-transformations.ipynb` - Bivariate analysis and data transformations
- `linear-assumptions-violations.ipynb` - Violations of linear regression assumptions
- `linear-regression-assumptions-fixes-mpg.ipynb` - Fixing assumption violations with MPG dataset
- `step-by-step-assumptions-linear-regression.ipynb` - Step-by-step guide to regression assumptions

### 📖 Resources (`resources/`)
Course materials and reference files:
- `Python_Guide - Session 1,2 and 3.pdf` - Course guide documentation
- `customer_data.csv` - Sample dataset for exercises

### 📄 Documentation (`documentation/`)
Additional course documentation and references:
- `linear-regression-session-9-10.pdf` - Linear regression lecture materials
- `linear-regression-assumptions-fixes.docx` - Guide to fixing regression assumptions
- `treating-missing-values.pdf` - Reference guide for missing value treatment

## Getting Started

1. Clone this repository
2. Install Jupyter Notebook or JupyterLab
3. Navigate to the appropriate directory based on your learning objectives
4. Open and run the notebooks

## Prerequisites

- Python 3.x
- Jupyter Notebook/Lab
- pandas
- numpy
- scikit-learn (for some advanced examples)

## Course Topics Covered

- Python Basics (data structures, control flow, functions)
- Pandas for Data Analysis
- Data Cleaning and Preprocessing
- Missing Value Handling
- Outlier Detection and Treatment
- Feature Engineering
- Categorical Encoding
- Data Transformation Techniques

## Notes

- All `.ipynb_checkpoints` and temporary files are excluded via `.gitignore`
- Datasets are included in their respective topic directories for easy reference
- Solutions to exercises can be found in `exercises/solved/`

## License

See [LICENSE](LICENSE) file for details.
