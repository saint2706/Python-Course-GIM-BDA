# Python Course - GIM BDA

This repository contains learning materials, worked examples, and case studies for a Python course focused on data analysis and business analytics (BDA).

## Repository Structure

Course content is organized into sequential, numbered modules. Each module's notebooks are numbered in the order they should be worked through.

### 1️⃣ Python Fundamentals (`01_Python_Fundamentals/`)
Core Python building blocks:
- `01_variables_lists_and_dictionaries.ipynb` - Variables, lists, and dictionaries
- `02_tuples_sets_and_nested_data.ipynb` - Tuples, sets, and nested data structures
- `03_control_flow_if_else_and_loops.ipynb` - Conditionals and loops
- `04_list_comprehensions.ipynb` - List comprehensions
- `05_lambda_map_filter_and_reduce.ipynb` - Lambda functions, map, filter, reduce
- `06_functions.ipynb` - Function definitions and usage
- `07_previous_year_exam_paper_solved.ipynb` - Worked solutions to a previous exam paper

### 2️⃣ Pandas Essentials (`02_Pandas_Essentials/`)
Introduction to Pandas and core DataFrame operations:
- `01_series_and_dataframes.ipynb` - Series and DataFrames
- `02_essential_operations.ipynb` - Essential operations and manipulations
- `03_groupby_and_aggregation.ipynb` - Grouping and aggregation
- `04_merging_joining_concatenating.ipynb` - Combining DataFrames
- `05_subsetting_and_filtering.ipynb` - Data filtering and selection
- `06_importing_and_exporting_data.ipynb` - Reading and writing data files
- `07_pandas_business_practice_solved.ipynb` - Worked business-practice exercise
- `08_sf_salaries_case_study.ipynb` - San Francisco salaries case study

### 3️⃣ Data Cleaning (`03_Data_Cleaning/`)
Handling missing data, duplicates, and outliers:
- `01_missing_values_univariate.ipynb` - Univariate missing value handling
- `02_missing_values_on_a_large_dataset.ipynb` - Missing values at scale
- `03_regression_imputation.ipynb` - Regression-based imputation
- `04_duplicate_records.ipynb` - Detecting and handling duplicate records
- `05_outlier_detection_and_treatment.ipynb` - Outlier detection and treatment

### 4️⃣ Data Transformation (`04_Data_Transformation/`)
Preparing features for modeling:
- `01_binning_and_discretisation.ipynb` - Binning and discretisation
- `02_categorical_encoding_catalogue.ipynb` - Catalogue of categorical encoding techniques
- `03_label_and_onehot_encoding_worked.ipynb` - Worked label and one-hot encoding examples
- `04_scaling_normalisation_and_transformation.ipynb` - Scaling, normalisation, and transformation

### 5️⃣ Feature Engineering (`05_Feature_Engineering/`)
Advanced feature engineering workflows:
- `01_feature_extraction_and_engineering.ipynb` - Feature extraction and engineering
- `02_filtering_and_categorical_encoding.ipynb` - Filtering and categorical encoding
- `03_encoding_masterclass.ipynb` - Encoding masterclass
- `04_sales_case_study_full_pipeline.ipynb` - Sales dataset full pipeline case study
- `05_student_case_study_full_pipeline.ipynb` - Student dataset full pipeline case study
- `06_practical_feature_engineering_case_study.ipynb` - Missing values, encoding, scaling, date/time and geo features on real loan-default and delivery-logistics datasets

### 6️⃣ Statistics and Regression (`06_Statistics_and_Regression/`)
Statistical analysis and linear regression:
- `01_bivariate_analysis_and_transformations.ipynb` - Bivariate analysis and transformations
- `02_linear_regression_assumptions_step_by_step.ipynb` - Linear regression assumptions, step by step
- `03_spotting_violations_visually.ipynb` - Spotting assumption violations visually
- `04_fixing_assumption_violations.ipynb` - Fixing assumption violations

### 7️⃣ Model Preparation (`07_Model_Preparation/`)
Getting data ready for modeling:
- `01_duplicate_detection_before_splitting.ipynb` - Duplicate detection before splitting
- `02_train_validation_test_splitting.ipynb` - Train/validation/test splitting
- `03_model_building_cycle_case_studies.ipynb` - Model building cycle case studies

### 8️⃣ Case Studies (`08_Case_Studies/`)
End-to-end applied case studies:
- `01_physician_loyalty_analysis.ipynb` - Physician loyalty analysis
- `02_penguins_eda_solved.ipynb` - Penguins exploratory data analysis, solved
- `03_assignment_1_worked_solution.ipynb` - Worked solution for assignment 1
- `04_insurance_policy_renewal_automl_pycaret.ipynb` - AutoML data preparation case study: human-vs-AutoML data cleaning on a dirty insurance dataset, then a PyCaret classification pipeline to predict policy renewal

### 📊 Datasets (`datasets/`)
All datasets used across the notebooks above, kept in one place for easy reference (CSV, Excel, and text files).

### 📖 Reference Documents (`reference_documents/`)
Supplementary course materials:
- `Python_Guide_-_Session_1,2_and_3.pdf` - Course guide documentation
- `linear-regression-session-9-10.pdf` - Linear regression lecture materials
- `linear-regression-assumptions-fixes.docx` - Guide to fixing regression assumptions
- `treating-missing-values.pdf` - Reference guide for missing value treatment
- `automl-data-preparation-case-finserve.docx` - "The 94% Accuracy Trap" case study on AutoML data preparation and model trust
- `automl-pycaret-student-task.pptx` - Student task brief for the PyCaret AutoML data preparation case study

## Getting Started

1. Clone this repository
2. Install Jupyter Notebook or JupyterLab
3. Work through the numbered modules in order, starting with `01_Python_Fundamentals/`
4. Datasets referenced by the notebooks live in `datasets/`

## Prerequisites

- Python 3.x
- Jupyter Notebook/Lab
- pandas
- numpy
- scikit-learn (for some advanced examples)
- pycaret (optional, only for the AutoML case study in `08_Case_Studies/04_insurance_policy_renewal_automl_pycaret.ipynb`)

## Course Topics Covered

- Python Basics (data structures, control flow, functions)
- Pandas for Data Analysis
- Data Cleaning and Preprocessing
- Missing Value Handling
- Outlier Detection and Treatment
- Feature Engineering
- Categorical Encoding
- Data Transformation Techniques
- Statistics and Linear Regression
- Model Preparation and Train/Validation/Test Splitting
- Applied Case Studies

## Notes

- All `.ipynb_checkpoints` and temporary files are excluded via `.gitignore`
- Datasets are consolidated in `datasets/` and referenced by notebooks across modules
- Student assignment submissions are not tracked in this repository

## License

See [LICENSE](LICENSE) file for details.
