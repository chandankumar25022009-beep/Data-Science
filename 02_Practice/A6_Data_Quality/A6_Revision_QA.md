
# A6 — Data Quality: Revision Questions and Answers

## Q1. What is Data Quality?

Data Quality describes how accurate, complete, consistent, and reliable data is.

## Q2. Why is Data Quality important?

It helps produce trustworthy analysis and better decisions.

## Q3. Name five dimensions of Data Quality.

Accuracy, completeness, consistency, validity, and uniqueness.

## Q4. What is accuracy?

Accuracy means data correctly represents the real-world value.

## Q5. What is completeness?

Completeness means required values are present.

## Q6. What is consistency?

Consistency means data follows the same rules and formats.

## Q7. What is validity?

Validity means data follows defined rules and acceptable ranges.

## Q8. What is uniqueness?

Uniqueness means there are no unwanted duplicate records.

## Q9. What are missing values?

Values that are not available in a dataset.

## Q10. What are duplicate records?

Records that appear more than once.

## Q11. What is an outlier?

A value that is unusually different from other observations.

## Q12. How do you count missing values in Pandas?

Use `df.isnull().sum()`.

## Q13. How do you count duplicate rows?

Use `df.duplicated().sum()`.

## Q14. How do you remove duplicates?

Use `df.drop_duplicates()`.

## Q15. How can missing values be handled?

They can be filled with suitable values or the affected rows or columns can be removed when justified.

## Q16. Why should missing values not always be replaced with zero?

Zero may represent a real value and change the meaning of the data.

## Q17. What is data validation?

Checking whether data follows defined rules and requirements.

## Q18. What is data cleaning?

Finding and correcting data-quality problems.

## Q19. How do you check data types?

Use `df.dtypes`.

## Q20. How do you view basic statistics?

Use `df.describe()`.

## Q21. How do you check dataset dimensions?

Use `df.shape`.

## Q22. How do you display the first five rows?

Use `df.head()`.

## Q23. What is a data type error?

A value has an inappropriate data type for its intended use.

## Q24. Should all outliers be removed?

No. Investigate them before deciding whether to keep or remove them.

## Q25. What is the result of poor Data Quality?

It can lead to misleading analysis and incorrect decisions.

## Key Revision Points

- Inspect data before cleaning.
- Check missing values and duplicates.
- Validate data types, formats, and ranges.
- Choose cleaning methods based on context.
- Keep the original data when possible.
