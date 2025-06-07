# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PRATEEKSHA RAI

*INTERN ID*: CT04DN723

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## Project Overview

This project demonstrates a simple yet effective ETL (Extract, Transform, Load) pipeline built using Python. The goal is to clean and prepare raw student or customer-related data for downstream tasks like analysis, visualization, or machine learning. The entire process is automated using Python libraries such as pandas, scikit-learn, and LabelEncoder, and the output is saved as a new, transformed CSV file.

Think of this project as a beginner-friendly data engineering tool: You start with messy data, and through a series of well-defined steps, you end up with a clean and consistent dataset. This is a crucial skill in the data world, especially when you're working with real-world datasets that often contain missing values, mixed types, and other inconsistencies.


## About the Dataset

The raw dataset used in this project is a small CSV file named data.csv. It contains personal information about individuals, including:

* Name (string)
* Age (numeric, with missing values)
* Gender (categorical, with missing values)
* Salary (numeric, with missing values)
* Purchased (categorical: Yes/No)


## Technologies Used

This project uses the following Python libraries:

* pandas – for loading and manipulating tabular data
* scikit-learn – for handling missing values, encoding, and scaling
* LabelEncoder – for converting categorical values into numeric format


## How the ETL Pipeline Works

### 1. Extract

The script starts by reading the raw CSV file (data.csv) using pandas. This is your starting point where the data is loaded into a DataFrame for further processing.

### 2. Transform

This is the core step of the pipeline where the data is cleaned and made machine-friendly:

* *Handling Missing Values*

  * Missing values in the Age and Salary columns are filled using the mean of their respective columns.
  * Missing values in the Gender and Purchased columns are filled by converting them using Label Encoding.
* *Encoding Categorical Variables*

  * Gender and Purchased columns are encoded as numbers using LabelEncoder.
* *Scaling Numeric Features*

  * Age and Salary columns are scaled using StandardScaler, so their values have mean = 0 and standard deviation = 1. This is important for many ML algorithms that rely on the scale of features.

### 3. Load

After transformation, the cleaned dataset is written into a new CSV file named processed_output.csv. This final file is ready for visualization, analysis, or feeding into a machine learning model.


## How to Run the Project

1. Clone or download this project folder.
2. Open it in VS Code or any IDE of your choice.
3. Make sure you have Python 3.x installed.
4. Install the required packages:
   
   pip install pandas scikit-learn
   
6. Make sure data.csv is in the same directory as the script.
7. Run the script:

   python data_pipeline.py
   
8. Check the output file processed_output.csv.


## Why This Matters

Having a clean dataset is foundational to any data science or machine learning project. This ETL process ensures that:

* There are no missing values to crash your algorithms.
* All categorical data is converted to numeric.
* Numerical features are standardized for optimal performance.

Even with this simple dataset, you’re learning important preprocessing techniques used in real-world data science workflows.


## Future Improvements

* Use more advanced imputation techniques like KNN or Iterative Imputer.
* Separate numerical and categorical transformations into reusable functions or pipelines.
* Include logging and exception handling for better debugging.
* Expand the script to handle larger datasets or different schemas.

## Conclusion

This ETL project demonstrates the entire lifecycle of preparing messy CSV data for analysis. It shows how to automate a repeatable, reliable data cleaning process using simple Python tools. Whether you're a beginner looking to practice or someone building a real application, this workflow is a solid foundation.

