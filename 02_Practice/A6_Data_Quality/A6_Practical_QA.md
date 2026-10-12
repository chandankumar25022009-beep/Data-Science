
# A6 — Data Quality: Practical Questions and Answers

## Q1. How do you check the number of rows and columns in a dataset?

**Question:** A dataset is stored in a Pandas DataFrame called `df`. How do you check its dimensions?

**Answer:**
```python
print(df.shape)
```

## Q2. How do you check missing values?

**Question:** Find the number of missing values in each column.

**Answer:**
```python
print(df.isnull().sum())
```

## Q3. How do you count duplicate rows?

**Question:** Count the duplicate rows in a DataFrame.

**Answer:**
```python
print(df.duplicated().sum())
```

## Q4. How do you remove duplicate rows?

**Question:** Remove duplicate rows from a dataset.

**Answer:**
```python
df = df.drop_duplicates()
```

## Q5. How do you fill missing values with zero?

**Question:** Replace all missing values with zero when zero is appropriate.

**Answer:**
```python
df = df.fillna(0)
```

## Q6. How do you fill missing values with a column mean?

**Question:** Fill missing values in the `Marks` column using its mean.

**Answer:**
```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

## Q7. How do you inspect data types?

**Question:** Display the data type of every column.

**Answer:**
```python
print(df.dtypes)
```

## Q8. How do you display basic statistics?

**Question:** Show descriptive statistics for numeric columns.

**Answer:**
```python
print(df.describe())
```

## Q9. How do you check the first five rows?

**Question:** Display the first five records.

**Answer:**
```python
print(df.head())
```

## Q10. How do you check the last five rows?

**Question:** Display the last five records.

**Answer:**
```python
print(df.tail())
```

## Q11. How do you find rows with missing ages?

**Question:** Display all rows where `Age` is missing.

**Answer:**
```python
print(df[df["Age"].isnull()])
```

## Q12. How do you find rows with marks below 40?

**Question:** Display students whose marks are below 40.

**Answer:**
```python
print(df[df["Marks"] < 40])
```

## Q13. How do you check whether a column contains missing values?

**Question:** Check if any value in the `Age` column is missing.

**Answer:**
```python
print(df["Age"].isnull().any())
```

## Q14. How do you count unique values?

**Question:** Count the different values in the `Name` column.

**Answer:**
```python
print(df["Name"].nunique())
```

## Q15. How do you check for invalid ages?

**Question:** Find records where age is less than zero.

**Answer:**
```python
print(df[df["Age"] < 0])
```

## Q16. How do you standardize text values?

**Question:** Remove extra spaces and make names lowercase.

**Answer:**
```python
df["Name"] = df["Name"].str.strip().str.lower()
```

## Q17. How do you check the number of unique values in each column?

**Answer:**
```python
print(df.nunique())
```

## Q18. How do you identify missing-value percentages?

**Answer:**
```python
missing_percent = df.isnull().mean() * 100
print(missing_percent)
```

## Q19. How do you check whether a dataset has duplicate records?

**Answer:**
```python
print(df.duplicated().any())
```

## Q20. How do you save a cleaned dataset to CSV?

**Answer:**
```python
df.to_csv("cleaned_data.csv", index=False)
```

## Key Learning

Always inspect data before cleaning it. Choose a correction method based on the meaning and quality of the data.
