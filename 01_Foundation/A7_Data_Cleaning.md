# A7 — Data Cleaning

## 1. What is Data Cleaning?

Data Cleaning is the process of finding and handling incorrect, incomplete, duplicate, inconsistent, or invalid data.

### Easy Definition

Data Cleaning = Finding and fixing problems in data.

### Example

| Name | Age | Marks |
|---|---:|---:|
| Rahul | 18 | 85 |
| Chandan | 17 | |
| Rahul | 18 | 85 |
| Aman | 150 | 78 |

Problems:
- Marks is missing.
- Rahul's record is duplicated.
- Age 150 may be invalid.

After cleaning, the data becomes more suitable for analysis.


## 2. Why is Data Cleaning Important?

Data Cleaning is important because it helps us:

1. Remove errors
2. Handle missing values
3. Remove duplicate records
4. Correct inconsistent data
5. Improve data quality
6. Make analysis more reliable
7. Build better machine learning models

### Key Point

Clean Data → Better Analysis → Better Results


## 3. Common Data Cleaning Problems

Common problems include:

- Missing Data
- Duplicate Data
- Incorrect Data
- Inconsistent Data
- Invalid Data
- Outdated Data
- Wrong Data Format
- Extra Spaces


## 4. Missing Data

Missing Data means some values are not available.

### Example

| Name | Age | Marks |
|---|---:|---:|
| Rahul | 18 | 85 |
| Chandan | 17 | |
| Aman | 19 | 78 |

Chandan's Marks value is missing.

### How can we handle it?

Depending on the situation, we may:

- Fill the value
- Use mean, median, or mode
- Remove the record
- Keep it as missing

The correct method depends on the dataset and the purpose of analysis.


## 5. Duplicate Data

Duplicate Data means the same record appears more than once unnecessarily.

### Example

| ID | Name | Marks |
|---|---|---:|
| 1 | Rahul | 80 |
| 2 | Chandan | 85 |
| 1 | Rahul | 80 |

The Rahul record appears twice.

### Solution

Identify duplicate records and remove or handle them when appropriate.


## 6. Incorrect Data

Incorrect Data contains wrong information.

### Example

A student's actual age is 17, but the dataset contains:

Age = 71

This is incorrect data.

### Solution

Check the original source and correct the value if the correct value can be verified.

### Easy Definition

Incorrect Data = Data that does not represent the correct real-world value.


## 7. Inconsistent Data

Inconsistent Data means the same type of information is represented differently.

### Example

| Student |
|---|
| Chandan Kumar |
| chandan kumar |
| CHANDAN KUMAR |

These may represent the same person but use different capitalization.

Another example:

- Male
- male
- M

These may need standardization depending on the dataset.

### Easy Definition

Inconsistent Data = Data represented in different formats or forms.


## 8. Invalid Data

Invalid Data does not follow the required rules or allowed range.

### Example

If age should be between 1 and 100:

Age = 20 → Valid

Age = 500 → Invalid

### Solution

Identify values that violate the defined rules and correct, replace, or remove them when appropriate.

### Easy Definition

Invalid Data = Data that does not follow the required rules.


## 9. Wrong Data Format

Sometimes the data is correct but stored in an unsuitable format.

### Example

Date values:

- 01/10/2026
- 2026-10-01
- October 1, 2026

For analysis, it is often useful to standardize them into one consistent date format.

### Key Point

Standardized Format → Easier Analysis


## 10. Extra Spaces

Extra spaces can create problems while comparing or grouping text.

### Example

"Chandan"

" Chandan"

"Chandan "

These may look similar to a person but can be treated as different strings by a computer.

### Solution

Remove unnecessary spaces and standardize the text.


## 11. Main Steps of Data Cleaning

Raw Data
    ↓
Find Data Problems
    ↓
Handle Missing Values
    ↓
Remove Duplicates
    ↓
Correct Errors
    ↓
Standardize Data
    ↓
Validate Data
    ↓
Clean Data


## 12. Data Cleaning Using Python

Python libraries such as Pandas are commonly used for data cleaning.

Example:

import pandas as pd

data = pd.read_csv("students.csv")

print(data)

data = data.drop_duplicates()

print(data)

Here:

- pandas helps us work with tabular data.
- read_csv() reads a CSV file.
- drop_duplicates() removes duplicate rows.

We will learn these commands practically in the Python/Data Analysis section.


## 13. Data Cleaning in Data Science

Data Collection
       ↓
Data Quality Check
       ↓
Data Cleaning
       ↓
Data Analysis
       ↓
Data Visualization
       ↓
Machine Learning
       ↓
Prediction


## 14. Real-Life Example

Suppose an e-commerce company has customer data.

The dataset contains:

- Missing phone numbers
- Duplicate customers
- Incorrect ages
- Different spellings of the same city
- Different date formats

A Data Analyst can clean and standardize the data before analyzing customer behavior.


# Interview Questions

## Q1. What is Data Cleaning?

Answer: Data Cleaning is the process of finding and handling incorrect, incomplete, duplicate, inconsistent, or invalid data.

## Q2. Why is Data Cleaning important?

Answer: Data Cleaning improves data quality and helps produce more reliable analysis and machine learning results.

## Q3. What is Missing Data?

Answer: Missing Data means that some required values are not available in a dataset.

## Q4. What is Duplicate Data?

Answer: Duplicate Data means the same record appears more than once unnecessarily.

## Q5. What is Incorrect Data?

Answer: Incorrect Data contains values that do not represent the correct real-world information.

## Q6. What is Inconsistent Data?

Answer: Inconsistent Data represents the same type of information in different or conflicting formats.

## Q7. What is Invalid Data?

Answer: Invalid Data does not follow the required rules, format, or allowed range.

## Q8. Name some common Data Cleaning problems.

Answer: Missing data, duplicate data, incorrect data, inconsistent data, invalid data, and wrong data formats.

## Q9. Which Python library is commonly used for Data Cleaning?

Answer: Pandas is a commonly used Python library for Data Cleaning and Data Analysis.

## Q10. What is the goal of Data Cleaning?

Answer: The goal of Data Cleaning is to improve the quality and reliability of data so it can be used effectively for analysis and modeling.


# Revision Questions

1. What is Data Cleaning?
2. Why is Data Cleaning important?
3. What is Missing Data?
4. What is Duplicate Data?
5. What is Incorrect Data?
6. What is Inconsistent Data?
7. What is Invalid Data?
8. What is a wrong data format?
9. Why should extra spaces be removed?
10. Name five common Data Cleaning problems.
11. What is the role of Pandas in Data Cleaning?
12. Write the main steps of Data Cleaning.
13. Give one real-life example of Data Cleaning.
14. Why should data be cleaned before analysis?
15. What is the relationship between Data Quality and Data Cleaning?


# Remember

Missing Data → Required value is unavailable

Duplicate Data → Same record appears more than once

Incorrect Data → Wrong information

Inconsistent Data → Different representations

Invalid Data → Does not follow rules

Data Cleaning → Find and handle data problems


# Key Point

Data Cleaning is the process of finding and handling problems in raw data to improve its quality and make it suitable for analysis and machine learning.

Raw Data
   ↓
Data Cleaning
   ↓
Clean Data
   ↓
Data Analysis
   ↓
Better Results