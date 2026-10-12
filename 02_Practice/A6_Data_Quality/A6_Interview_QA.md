
# A6 — Data Quality: Interview Questions and Answers

## Q1. What is Data Quality?

Data Quality means how accurate, complete, consistent, and reliable data is.

## Q2. Why is Data Quality important?

It helps us make correct decisions and produce reliable analysis.

## Q3. What is data accuracy?

Accuracy means data correctly represents the real-world information.

## Q4. What is data completeness?

Completeness means the required data values are present.

## Q5. What is data consistency?

Consistency means data follows the same rules and formats across datasets.

## Q6. What is data validity?

Validity means data follows defined rules, formats, and acceptable ranges.

## Q7. What is data uniqueness?

Uniqueness means records do not contain unwanted duplicates.

## Q8. What is data reliability?

Reliability means data can be trusted for its intended purpose.

## Q9. What is missing data?

Missing data means some expected values are not available.

## Q10. What is duplicate data?

Duplicate data means the same record appears more than once.

## Q11. What is an outlier?

An outlier is a value that is unusually different from other observations.

## Q12. How can you check missing values in Pandas?

Use `df.isnull().sum()`.

## Q13. How can you find duplicate rows in Pandas?

Use `df.duplicated().sum()`.

## Q14. How can you remove duplicate rows?

Use `df.drop_duplicates()`.

## Q15. How can you fill missing values?

Use `df.fillna(value)` or fill a specific column with a suitable value.

## Q16. What is data validation?

Data validation checks whether data meets specified rules and requirements.

## Q17. What is data cleaning?

Data cleaning identifies and fixes inaccurate, incomplete, duplicated, or inconsistent data.

## Q18. What is the difference between data quality and data cleaning?

Data quality describes how good the data is. Data cleaning is the process of improving it.

## Q19. What problems can poor data quality cause?

It can cause incorrect analysis, misleading results, and poor decisions.

## Q20. How can you improve data quality?

Check accuracy, completeness, consistency, validity, duplicates, and missing values.

## Q21. What is a data type error?

It occurs when a value has an inappropriate type, such as text stored where a number is expected.

## Q22. What is a format inconsistency?

It occurs when the same type of information uses different formats, such as dates written differently.

## Q23. Should every missing value be replaced with zero?

No. Zero may have a different meaning from missing data.

## Q24. Should every outlier be removed?

No. First investigate whether the outlier is an error or a genuine observation.

## Q25. What is a data quality check?

It is a test used to identify issues such as missing values, duplicates, invalid values, and inconsistent formats.

## Key Learning

Good data quality is essential for trustworthy Data Analysis and Machine Learning.
