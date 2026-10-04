# A6 — Data Quality

## 1. What is Data Quality?

Data Quality refers to how accurate, complete, consistent, valid, and useful the data is for a particular purpose.

### Easy Definition

Data Quality = How good and reliable the data is.

### Example

| Name | Age | Marks |
|---|---:|---:|
| Rahul | 18 | 85 |
| Chandan | 17 | 90 |
| Aman | 19 | 78 |

If the information is correct and complete, the data has good quality.


## 2. Why is Data Quality Important?

Good-quality data helps us:

1. Make better decisions
2. Perform accurate analysis
3. Build reliable machine learning models
4. Find correct patterns
5. Reduce errors
6. Save time
7. Improve business results

### Key Point

Good Data → Better Analysis → Better Decisions


## 3. Main Characteristics of Good Data

Important characteristics of good-quality data include:

1. Accuracy
2. Completeness
3. Consistency
4. Validity
5. Timeliness
6. Uniqueness


## 4. Accuracy

Accuracy means the data correctly represents the real-world value.

### Example

If a student's actual marks are 85 and the database contains 85, the data is accurate.

If the database contains 58 instead of 85, the data is inaccurate.

### Easy Definition

Accuracy = Data is correct.


## 5. Completeness

Completeness means that all required data is available.

### Example

Suppose a student record requires:

- Name
- Age
- Course
- Marks

If the Marks field is missing, the record is incomplete.

### Easy Definition

Completeness = Required data is not missing.


## 6. Consistency

Consistency means that the same data does not conflict across different systems or records.

### Example

Suppose a student's name is:

Chandan Kumar

in one database, but:

Chandan K.

in another database.

This may create a consistency problem if both records are supposed to represent the same student.

### Easy Definition

Consistency = Data should not have conflicting values.


## 7. Validity

Validity means that data follows the required format, rules, or allowed values.

### Example

If an age field should contain a number from 1 to 100, then:

Age = 20 → Valid

Age = 500 → Invalid

### Another Example

If an email should follow a valid email format:

chandan@example.com → Valid format

chandan@ → Invalid format

### Easy Definition

Validity = Data follows the required rules or format.


## 8. Timeliness

Timeliness means that data is available and updated when it is needed.

### Example

A weather application needs current weather information.

Old weather information may not be useful for showing the current weather.

### Easy Definition

Timeliness = Data is available at the right time.


## 9. Uniqueness

Uniqueness means that the same record should not appear unnecessarily multiple times.

### Example

| Customer ID | Name |
|---|---|
| 101 | Rahul |
| 102 | Aman |
| 101 | Rahul |

The record with Customer ID 101 appears twice.

This is a duplicate record.

### Easy Definition

Uniqueness = No unnecessary duplicate records.


## 10. Missing Data

Missing Data means some values are not available in a dataset.

### Example

| Name | Age | Marks |
|---|---:|---:|
| Rahul | 18 | 85 |
| Chandan | 17 | |
| Aman | 19 | 78 |

Chandan's Marks value is missing.

### Common Reasons

- User did not provide information
- Data collection problem
- System error
- Incorrect data entry

### Key Point

Missing data should be identified and handled before analysis.


## 11. Duplicate Data

Duplicate Data means the same record appears more than once unnecessarily.

### Example

| ID | Name | Marks |
|---|---|---:|
| 1 | Rahul | 80 |
| 2 | Chandan | 85 |
| 1 | Rahul | 80 |

The first and third records are duplicates.

### Problem

Duplicate data can produce incorrect analysis and misleading results.

### Key Point

Duplicate records should be detected and handled during data cleaning.


## 12. Incorrect Data

Incorrect Data contains wrong information.

### Example

Suppose a student's actual age is 17, but the dataset contains:

Age = 71

This is incorrect data.

### Easy Definition

Incorrect Data = Data that does not represent the correct real-world value.


## 13. Data Quality Problems

Common data quality problems include:

- Missing data
- Duplicate data
- Incorrect data
- Inconsistent data
- Invalid data
- Outdated data

### Diagram

DATA QUALITY PROBLEMS
        |
-----------------------------------------
|        |        |       |       |     |
Missing Duplicate Incorrect Inconsistent Invalid Outdated


## 14. Data Quality and Data Cleaning

Data Quality is closely related to Data Cleaning.

### Data Cleaning

Data Cleaning is the process of finding and correcting or handling problems in data.

### Example

Raw Data
    ↓
Missing Values
    ↓
Duplicate Records
    ↓
Incorrect Values
    ↓
Inconsistent Values
    ↓
Clean Data

### Key Point

Data Quality tells us how good the data is.

Data Cleaning helps improve the quality of data.


## 15. Real-Life Example

Suppose a college has a student dataset containing:

- Student Name
- Age
- Course
- Marks
- Attendance

The dataset contains:

- Missing marks
- Duplicate student records
- Incorrect ages
- Different names for the same student
- Old student information

A Data Analyst or Data Scientist can identify these problems and clean the data before performing analysis.


## 16. Data Quality in a Data Science Project

Data Sources
      ↓
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
Prediction / Decision

Data Quality checking helps ensure that the data is suitable for analysis and modeling.


# Interview Questions

## Q1. What is Data Quality?

Answer: Data Quality refers to how accurate, complete, consistent, valid, timely, and useful data is for a particular purpose.

## Q2. Why is Data Quality important?

Answer: Data Quality is important because good-quality data helps produce accurate analysis, reliable models, and better decisions.

## Q3. What is Accuracy?

Answer: Accuracy means that the data correctly represents the real-world value.

## Q4. What is Completeness?

Answer: Completeness means that all required data is available and important values are not missing.

## Q5. What is Consistency?

Answer: Consistency means that data does not contain conflicting values across records or systems.

## Q6. What is Validity?

Answer: Validity means that data follows the required rules, format, or allowed values.

## Q7. What is Timeliness?

Answer: Timeliness means that data is available and updated when it is needed.

## Q8. What is Duplicate Data?

Answer: Duplicate Data means the same record appears more than once unnecessarily.

## Q9. What is Missing Data?

Answer: Missing Data means that some required values are not available in a dataset.

## Q10. What is the relationship between Data Quality and Data Cleaning?

Answer: Data Quality measures how good the data is, while Data Cleaning helps identify and handle problems to improve data quality.


# Revision Questions

1. What is Data Quality?
2. Why is Data Quality important?
3. What is Accuracy?
4. What is Completeness?
5. What is Consistency?
6. What is Validity?
7. What is Timeliness?
8. What is Uniqueness?
9. What is Missing Data?
10. What is Duplicate Data?
11. What is Incorrect Data?
12. What are common Data Quality problems?
13. What is Data Cleaning?
14. Why should data quality be checked before analysis?
15. Give one real-life example of poor data quality.


# Remember

Accuracy → Data is correct

Completeness → Required data is available

Consistency → Data has no conflicting values

Validity → Data follows required rules

Timeliness → Data is available at the right time

Uniqueness → No unnecessary duplicate records

Missing Data → Required value is unavailable

Duplicate Data → Same record appears more than once


# Key Point

Good Data Quality is important for reliable Data Science.

Good Data
    ↓
Better Data Quality
    ↓
Better Data Cleaning
    ↓
Better Analysis
    ↓
Better Machine Learning
    ↓
Better Decisions