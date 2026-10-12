
# A7 — Data Cleaning: Revision Questions and Answers

## Q1. What is Data Cleaning?

Data Cleaning is the process of identifying and correcting data-quality problems.

## Q2. Why is Data Cleaning important?

It improves data quality and supports reliable analysis.

## Q3. What are missing values?

Values that are not available in a dataset.

## Q4. How do you check missing values in Pandas?

Use `df.isnull().sum()`.

## Q5. How do you remove rows with missing values?

Use `df.dropna()`.

## Q6. How do you fill missing values?

Use `df.fillna(value)` with a suitable value.

## Q7. What are duplicate records?

Records that repeat the same information.

## Q8. How do you count duplicate rows?

Use `df.duplicated().sum()`.

## Q9. How do you remove duplicate rows?

Use `df.drop_duplicates()`.

## Q10. Why should spaces be removed before checking duplicates?

Extra spaces can make identical text values appear different.

## Q11. How do you remove extra spaces from a text column?

Use `df["Name"].str.strip()`.

## Q12. What does `str.lower()` do?

It converts text to lowercase.

## Q13. What does `str.title()` do?

It converts text to title case.

## Q14. What is data standardization?

It makes data formats and representations consistent.

## Q15. What is an outlier?

A value that differs significantly from most other observations.

## Q16. Should every outlier be removed?

No. Investigate it before deciding whether to remove it.

## Q17. How do you check column data types?

Use `df.dtypes`.

## Q18. How do you convert a column to numeric values?

Use `pd.to_numeric()`.

## Q19. What does `errors="coerce"` do?

It converts invalid values to missing values during conversion.

## Q20. How do you check dataset dimensions?

Use `df.shape`.

## Q21. How do you display the first five rows?

Use `df.head()`.

## Q22. How do you display basic statistics?

Use `df.describe()`.

## Q23. Should missing values always be filled with zero?

No. Zero may represent a real value and change the data's meaning.

## Q24. How do you save cleaned data to CSV?

Use `df.to_csv("cleaned_data.csv", index=False)`.

## Q25. What should you do after cleaning?

Validate the results, check for remaining issues, and save the cleaned data.

## Key Revision Points

- Inspect the dataset before cleaning.
- Check missing values and duplicate records.
- Standardize text and formats.
- Correct data types and invalid values carefully.
- Verify the cleaned data before using it for analysis.
