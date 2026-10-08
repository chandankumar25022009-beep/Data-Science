# A3 — Types of Data: Practical Questions and Answers

## Practical 1: Identify Numerical Data

**Question:** Identify the numerical data in the following values: age = 20, salary = 25000, city = "Meerut".

**Answer:**

* Age = 20 → Numerical
* Salary = 25000 → Numerical
* City = "Meerut" → Categorical

## Practical 2: Identify Categorical Data

**Question:** Identify the categorical data: color = "Blue", marks = 85, education = "Diploma".

**Answer:**

* Color = "Blue" → Categorical
* Marks = 85 → Numerical
* Education = "Diploma" → Categorical

## Practical 3: Identify Discrete Data

**Question:** A class has 45 students. What type of data is the number of students?

**Answer:** Discrete data, because students are counted in whole numbers.

## Practical 4: Identify Continuous Data

**Question:** A student's height is 5.8 feet. What type of data is height?

**Answer:** Continuous data, because height is measured and may contain decimal values.

## Practical 5: Identify Structured Data

**Question:** A spreadsheet stores students' names, ages, and marks in columns. What type of data is it?

**Answer:** Structured data, because it follows a predefined row-and-column format.

## Practical 6: Identify Unstructured Data

**Question:** A folder contains photos, videos, and audio recordings. What type of data is it?

**Answer:** Unstructured data, because these files do not follow a fixed tabular structure.

## Practical 7: Identify Semi-Structured Data

**Question:** A file stores information using JSON keys and values. What type of data is it?

**Answer:** Semi-structured data.

## Practical 8: Identify Nominal Data

**Question:** The colors Red, Blue, and Green are recorded in a dataset. Are they nominal or ordinal?

**Answer:** Nominal data, because the colors have no natural order.

## Practical 9: Identify Ordinal Data

**Question:** Customer feedback is recorded as Low, Medium, or High. What type of data is it?

**Answer:** Ordinal data, because the categories have a meaningful order.

## Practical 10: Check Data Types Using Python

**Question:** Write Python code to check the data types of an integer, decimal, and string.

**Answer:**

```python
age = 20
height = 5.8
city = "Meerut"

print(type(age))
print(type(height))
print(type(city))
```

**Expected Output:**

```text
<class 'int'>
<class 'float'>
<class 'str'>
```

## Practical 11: Create a Small Dataset

**Question:** Create a dataset containing age, salary, and city.

**Answer:**

```python
import pandas as pd

data = {
    "Age": [20, 22, 25],
    "Salary": [25000, 30000, 40000],
    "City": ["Meerut", "Delhi", "Agra"]
}

df = pd.DataFrame(data)
print(df)
```

## Practical 12: Count Numerical and Categorical Columns

**Question:** Given a DataFrame, identify numerical and categorical columns.

**Answer:**

```python
import pandas as pd

df = pd.DataFrame({
    "Age": [20, 22, 25],
    "Salary": [25000, 30000, 40000],
    "City": ["Meerut", "Delhi", "Agra"]
})

print("Numerical columns:")
print(df.select_dtypes(include="number").columns.tolist())

print("Categorical columns:")
print(df.select_dtypes(include="object").columns.tolist())
```

## Key Learning

Correctly identifying data types helps us choose suitable analysis, visualization, and Machine Learning methods.
