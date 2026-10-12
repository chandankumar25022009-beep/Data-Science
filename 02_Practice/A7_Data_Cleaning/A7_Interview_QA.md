
# A7 — Data Cleaning: Interview Questions and Answers

## Q1. What is Data Cleaning?

Data Cleaning is the process of identifying and correcting inaccurate, incomplete, duplicate, or inconsistent data.

## Q2. Why is Data Cleaning important?

It improves data quality and helps produce reliable analysis.

## Q3. What are missing values?

Missing values are data values that are not available in a dataset.

## Q4. How can you detect missing values in Pandas?

Use `df.isnull().sum()`.

## Q5. How can you remove rows containing missing values?

Use `df.dropna()`.

## Q6. How can you fill missing values?

Use `df.fillna(value)` or fill a specific column with an appropriate value.

## Q7. What are duplicate records?

Duplicate records are rows that repeat the same information.

## Q8. How can you detect duplicate rows?

Use `df.duplicated().sum()`.

## Q9. How can you remove duplicate rows?

Use `df.drop_duplicates()`.

## Q10. What is data standardization?

Data standardization makes values consistent in format, spelling, or representation.

## Q11. What does `str.strip()` do?

It removes leading and trailing whitespace from text values.

## Q12. What does `str.lower()` do?

It converts text values to lowercase.

## Q13. What does `str.title()` do?

It converts text into title case.

## Q14. What is an outlier?

An outlier is a value that differs significantly from most other observations.

## Q15. Should all outliers be removed?

No. Investigate them first because some outliers are genuine observations.

## Q16. What is data type conversion?

It changes a value or column from one data type to another.

## Q17. How can you convert a column to numeric data?

Use `pd.to_numeric()` with the appropriate error-handling option.

## Q18. What is inconsistent data?

Data that uses different formats or representations for the same kind of information.

## Q19. What is the difference between `dropna()` and `fillna()`?

`dropna()` removes rows or columns with missing values. `fillna()` replaces missing values.

## Q20. What is the difference between `duplicated()` and `drop_duplicates()`?

`duplicated()` identifies duplicate rows. `drop_duplicates()` removes them.

## Q21. Why should the original dataset be preserved?

It allows us to compare results and recover the original information if needed.

## Q22. What is data validation?

Data validation checks whether values meet defined rules and requirements.

## Q23. What is a common risk when filling missing values with the mean?

The mean may distort the data, especially when values are skewed or outliers are present.

## Q24. How can you save cleaned data to a CSV file?

Use `df.to_csv("cleaned_data.csv", index=False)`.

## Q25. What are the main steps in Data Cleaning?

Inspect data, identify issues, correct errors, handle missing values, remove duplicates, validate results, and save the cleaned dataset.

## Key Learning

Always inspect the data before cleaning it. Choose cleaning methods according to the data's meaning and purpose.
