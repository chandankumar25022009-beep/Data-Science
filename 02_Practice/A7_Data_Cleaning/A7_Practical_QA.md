
# A7 — Data Cleaning: Practical Questions and Answers

## Q1. How do you find missing values in a dataset?

**Answer:**
```python
print(df.isnull().sum())
```

## Q2. How do you remove rows with missing values?

**Answer:**
```python
df = df.dropna()
```

## Q3. How do you fill missing values with zero?

**Answer:**
```python
df = df.fillna(0)
```

## Q4. How do you fill missing marks with the column mean?

**Answer:**
```python
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
```

## Q5. How do you count duplicate rows?

**Answer:**
```python
print(df.duplicated().sum())
```

## Q6. How do you remove duplicate rows?

**Answer:**
```python
df = df.drop_duplicates()
```

## Q7. Why should extra spaces be removed before deleting duplicates?

**Answer:** Extra spaces can make otherwise identical text values appear different.

```python
df["Name"] = df["Name"].str.strip()
df = df.drop_duplicates()
```

## Q8. How do you convert names to lowercase?

**Answer:**
```python
df["Name"] = df["Name"].str.lower()
```

## Q9. How do you standardize names using title case?

**Answer:**
```python
df["Name"] = df["Name"].str.title()
```

## Q10. How do you check the data types of columns?

**Answer:**
```python
print(df.dtypes)
```

## Q11. How do you convert a column to numeric values?

**Answer:**
```python
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
```

## Q12. What does `errors="coerce"` do?

**Answer:** Invalid values are converted to missing values instead of raising a conversion error.

## Q13. How do you display rows where age is missing?

**Answer:**
```python
print(df[df["Age"].isnull()])
```

## Q14. How do you find records with negative ages?

**Answer:**
```python
print(df[df["Age"] < 0])
```

## Q15. How do you replace negative ages with missing values?

**Answer:**
```python
df.loc[df["Age"] < 0, "Age"] = float("nan")
```

## Q16. How do you check the number of rows and columns?

**Answer:**
```python
print(df.shape)
```

## Q17. How do you display basic statistics?

**Answer:**
```python
print(df.describe())
```

## Q18. How do you check the first five rows?

**Answer:**
```python
print(df.head())
```

## Q19. How do you save cleaned data to a CSV file?

**Answer:**
```python
df.to_csv("cleaned_data.csv", index=False)
```

## Q20. How do you verify that duplicates were removed?

**Answer:**
```python
print(df.duplicated().sum())
```

## Q21. How do you check missing values after cleaning?

**Answer:**
```python
print(df.isnull().sum())
```

## Q22. How do you remove leading and trailing spaces from every text column?

**Answer:**
```python
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()
```

## Q23. Why should you inspect data before cleaning?

**Answer:** Inspection helps identify problems and choose an appropriate cleaning method.

## Q24. Should missing values always be replaced by the mean?

**Answer:** No. The mean may be unsuitable for categorical data or skewed numerical data.

## Q25. What should you do after cleaning a dataset?

**Answer:** Validate the results, check for remaining issues, and save the cleaned data.

## Key Learning

Clean data carefully, validate every important change, and preserve the original dataset when possible.
