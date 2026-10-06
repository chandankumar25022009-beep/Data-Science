# A9 — Exploratory Data Analysis (EDA)

## 1. What is Exploratory Data Analysis?

Exploratory Data Analysis (EDA) is the process of examining, summarizing, and visualizing data to understand its main characteristics, patterns, relationships, and problems.

### Easy Definition

EDA = Understanding the data before performing detailed analysis or building a machine learning model.

### Example

Suppose we have student data containing:

- Name
- Age
- Marks
- Attendance
- Study Hours

Using EDA, we can find:

- Average marks
- Highest and lowest marks
- Attendance patterns
- Relationship between study hours and marks
- Missing values
- Unusual values

---

## 2. Why is EDA Important?

EDA is important because it helps us:

1. Understand the dataset
2. Find patterns
3. Detect missing values
4. Detect duplicate data
5. Find unusual values
6. Understand relationships between variables
7. Choose useful features
8. Prepare data for further analysis
9. Understand whether the data is suitable for machine learning

### Key Point

Understand Data → Find Patterns → Make Better Decisions

---

## 3. Main Goals of EDA

The main goals of EDA are:

- Understand the structure of data
- Summarize important information
- Find patterns and trends
- Identify relationships
- Detect unusual values
- Find data quality problems
- Generate useful questions and insights

---

## 4. Types of EDA

EDA can involve different types of analysis.

### 1. Univariate Analysis

Analysis of one variable at a time.

Example:

Studying only the Marks column.

We can calculate:

- Mean
- Median
- Minimum
- Maximum

### 2. Bivariate Analysis

Analysis of two variables.

Example:

Study Hours and Marks.

We can investigate whether study hours are related to marks.

### 3. Multivariate Analysis

Analysis of more than two variables.

Example:

Study Hours + Attendance + Previous Marks + Final Marks.

---

## 5. Understanding the Dataset

Before analyzing data, we should understand its basic structure.

Important information includes:

- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate records

### Example

Suppose a dataset contains:

1000 rows

10 columns

This means the dataset contains 1000 records and 10 variables.

---

## 6. Descriptive Statistics

Descriptive Statistics summarizes important characteristics of numerical data.

Common measurements include:

- Mean
- Median
- Mode
- Minimum
- Maximum
- Range
- Standard Deviation

### Example

Marks:

60, 70, 80, 90, 100

Mean:

(60 + 70 + 80 + 90 + 100) / 5 = 80

So, the average marks are 80.

---

## 7. Mean

Mean is the average value of a dataset.

### Formula

Mean = Sum of all values / Number of values

### Example

Values:

10, 20, 30

Mean:

(10 + 20 + 30) / 3 = 20

### Easy Definition

Mean = Average value.

---

## 8. Median

Median is the middle value when data is arranged in order.

### Example

Values:

10, 20, 30, 40, 50

Median = 30

If there are an even number of values, the median is calculated using the average of the two middle values.

### Easy Definition

Median = Middle value of ordered data.

---

## 9. Mode

Mode is the value that appears most frequently.

### Example

Values:

10, 20, 20, 30, 40

Mode = 20

Because 20 appears most often.

### Easy Definition

Mode = Most frequently occurring value.

---

## 10. Minimum and Maximum

### Minimum

Minimum is the smallest value in the dataset.

### Maximum

Maximum is the largest value in the dataset.

### Example

Marks:

45, 60, 75, 90

Minimum = 45

Maximum = 90

---

## 11. Range

Range represents the difference between the maximum and minimum values.

### Formula

Range = Maximum - Minimum

### Example

Maximum = 90

Minimum = 45

Range = 90 - 45 = 45

---

## 12. Data Visualization in EDA

Visualization helps us understand data using charts and graphs.

Common charts include:

- Bar Chart
- Line Chart
- Histogram
- Pie Chart
- Scatter Plot
- Box Plot

### Example

A bar chart can compare the number of students in different departments.

A line chart can show sales over time.

A histogram can show the distribution of marks.

A scatter plot can show the relationship between study hours and marks.

---

## 13. Histogram

A histogram shows the distribution of numerical data using intervals or bins.

### Example

A histogram can show how student marks are distributed.

It can help us understand whether most students scored:

- Low marks
- Medium marks
- High marks

### Easy Definition

Histogram = Shows the distribution of numerical data.

---

## 14. Bar Chart

A bar chart is commonly used to compare categories.

### Example

Number of students:

CSE = 50

ECE = 40

Mechanical = 30

A bar chart can compare these values.

### Easy Definition

Bar Chart = Compares categories using bars.

---

## 15. Line Chart

A line chart is useful for showing changes or trends over time.

### Example

Monthly sales:

January = 10,000

February = 12,000

March = 15,000

A line chart can show how sales changed over the months.

### Easy Definition

Line Chart = Shows trends or changes over time.

---

## 16. Scatter Plot

A scatter plot shows the relationship between two numerical variables.

### Example

Study Hours and Marks.

If students who study more hours generally have higher marks, the scatter plot may show a positive relationship.

### Easy Definition

Scatter Plot = Shows the relationship between two numerical variables.

---

## 17. Box Plot

A box plot is used to understand the distribution of numerical data and identify potential outliers.

It can help show:

- Median
- Quartiles
- Spread
- Potential outliers

### Easy Definition

Box Plot = Shows distribution and potential outliers.

---

## 18. Correlation

Correlation describes the strength and direction of a relationship between two variables.

### Example

Study Hours and Marks.

If study hours increase and marks generally increase, there may be a positive relationship.

### Types

Positive Correlation → Both variables generally increase together.

Negative Correlation → One variable generally increases while the other decreases.

Little or No Correlation → No clear linear relationship.

### Important Point

Correlation does not automatically mean that one variable causes the other.

---

## 19. Outliers

An outlier is a value that is unusually different from most other values in a dataset.

### Example

Marks:

70, 72, 75, 78, 80, 10

10 may be an unusual value compared with the other marks.

However, an unusual value is not automatically an error. It should be investigated before deciding how to handle it.

### Easy Definition

Outlier = A value that is unusually different from other observations.

---

## 20. EDA Using Python

Python libraries commonly used for EDA include:

- Pandas
- NumPy
- Matplotlib
- Seaborn

### Example

import pandas as pd

data = pd.read_csv("students.csv")

print(data.head())

print(data.info())

print(data.describe())

These commands can help us inspect the dataset.

### Common Functions

data.head() → Shows the first few rows

data.info() → Shows information about columns and data types

data.describe() → Shows descriptive statistics for numerical columns

We will practice these commands later in the Python and Data Analysis sections.

---

## 21. EDA Process

A basic EDA process can be:

Load Data
    ↓
Understand Dataset
    ↓
Check Data Types
    ↓
Check Missing Values
    ↓
Check Duplicates
    ↓
Calculate Statistics
    ↓
Visualize Data
    ↓
Find Patterns
    ↓
Find Relationships
    ↓
Identify Outliers
    ↓
Generate Insights

---

## 22. Real-Life Example

Suppose an online shopping company has customer data containing:

- Age
- Gender
- City
- Income
- Products Purchased
- Purchase Amount

Using EDA, the company can investigate:

- Average purchase amount
- Most common customer age group
- Which city has more customers
- Relationship between income and purchase amount
- Unusual purchase values
- Missing or duplicate records

These insights can help the company make better decisions.

---

## 23. EDA in a Data Science Project

Data Collection
       ↓
Data Cleaning
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Data Visualization
       ↓
Feature Engineering
       ↓
Machine Learning
       ↓
Prediction
       ↓
Decision

---

# Interview Questions

## Q1. What is EDA?

Answer: Exploratory Data Analysis is the process of examining, summarizing, and visualizing data to understand its characteristics, patterns, relationships, and problems.

## Q2. Why is EDA important?

Answer: EDA helps us understand the dataset, find patterns, detect problems, identify relationships, and generate useful insights before further analysis or machine learning.

## Q3. What is Univariate Analysis?

Answer: Univariate Analysis is the analysis of one variable at a time.

## Q4. What is Bivariate Analysis?

Answer: Bivariate Analysis is the analysis of two variables to understand their relationship.

## Q5. What is Multivariate Analysis?

Answer: Multivariate Analysis is the analysis of more than two variables together.

## Q6. What is Mean?

Answer: Mean is the average value of a dataset.

## Q7. What is Median?

Answer: Median is the middle value when data is arranged in order.

## Q8. What is Mode?

Answer: Mode is the value that occurs most frequently in a dataset.

## Q9. What is an Outlier?

Answer: An Outlier is a value that is unusually different from most other observations in a dataset.

## Q10. Name four Python libraries commonly used in EDA.

Answer: Pandas, NumPy, Matplotlib, and Seaborn.

---

# Revision Questions

1. What is Exploratory Data Analysis?
2. Why is EDA important?
3. What are the main goals of EDA?
4. What is Univariate Analysis?
5. What is Bivariate Analysis?
6. What is Multivariate Analysis?
7. What is Mean?
8. What is Median?
9. What is Mode?
10. What is Range?
11. What is Data Visualization?
12. What is a Histogram?
13. What is a Bar Chart?
14. What is a Line Chart?
15. What is a Scatter Plot?
16. What is a Box Plot?
17. What is Correlation?
18. What is an Outlier?
19. Name four Python libraries used in EDA.
20. Write the basic steps of EDA.

---

# Remember

EDA → Understand the data

Mean → Average value

Median → Middle value

Mode → Most frequent value

Range → Maximum - Minimum

Histogram → Distribution of numerical data

Bar Chart → Comparison of categories

Line Chart → Trends over time

Scatter Plot → Relationship between two numerical variables

Box Plot → Distribution and potential outliers

Outlier → Unusually different observation

Correlation → Relationship between variables

---

# Key Point

Exploratory Data Analysis helps us understand data, discover patterns, identify relationships, detect unusual values, and generate useful insights before building models or making decisions.

Raw Data
    ↓
Data Cleaning
    ↓
Data Preprocessing
    ↓
EDA
    ↓
Patterns + Relationships + Insights
    ↓
Machine Learning / Decision Making