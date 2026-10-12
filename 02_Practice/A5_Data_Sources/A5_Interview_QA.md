 # A5 — Data Sources: Interview Questions and Answers

## Q1. What is a Data Source?
A data source is a place or system from which data is obtained.

## Q2. Why are Data Sources important in Data Science?
Data sources provide the information required for data analysis and Machine Learning.

## Q3. What are the common types of Data Sources?
Common data sources include files, databases, websites, APIs, sensors, and surveys.

## Q4. What is a File-Based Data Source?
A file-based data source stores data in files such as CSV, JSON, Excel, or text files.

## Q5. What is a CSV File?
CSV stands for Comma-Separated Values. It stores tabular data as text.

## Q6. What is a Database?
A database is an organized collection of data that can be stored, accessed, and managed.

## Q7. What is SQL?
SQL stands for Structured Query Language. It is used to manage and retrieve data from relational databases.

## Q8. What is an API?
An API allows different software applications to communicate and exchange data.

## Q9. What is Web Scraping?
Web scraping is the process of extracting data from websites using software tools.

## Q10. What is a Website as a Data Source?
A website can provide information such as product details, news, reviews, and public statistics.

## Q11. What is Sensor Data?
Sensor data is information collected by devices that measure conditions such as temperature, pressure, or movement.

## Q12. What is Real-Time Data?
Real-time data is generated or collected as events happen.

**Example:** Live traffic information.

## Q13. What is Historical Data?
Historical data is information collected and stored in the past.

**Example:** Previous years' sales records.

## Q14. What is Primary Data?
Primary data is collected directly for a specific research or analysis purpose.

**Example:** Conducting a new customer survey.

## Q15. What is Secondary Data?
Secondary data is data that was previously collected by someone else.

**Example:** Using a published government report.

## Q16. What is Structured Data?
Structured data follows a predefined format, commonly rows and columns.

**Example:** A relational database table.

## Q17. What is Unstructured Data?
Unstructured data does not follow a fixed tabular structure.

**Example:** Images, audio, videos, and free-form text.

## Q18. What is Semi-Structured Data?
Semi-structured data has organizational elements but does not follow a strict relational table structure.

**Example:** JSON and XML files.

## Q19. What is a Dataset?
A dataset is a collection of related data used for analysis.

## Q20. What is Pandas?
Pandas is a Python library used to manipulate and analyze tabular data.

## Q21. What is a DataFrame?
A DataFrame is a two-dimensional Pandas data structure arranged in rows and columns.

## Q22. How do you create a DataFrame in Python?
Use `pd.DataFrame()`.

**Example:**
```python
import pandas as pd

data = {"Name": ["Aman", "Rahul"], "Marks": [75, 82]}
df = pd.DataFrame(data)

print(df)
```

## Q23. How do you read a CSV file using Pandas?
Use `pd.read_csv()`.

**Example:**
```python
import pandas as pd

df = pd.read_csv("students.csv")
print(df)
```

## Q24. How do you save a DataFrame to a CSV file?
Use `df.to_csv()`.

**Example:**
```python
df.to_csv("students.csv", index=False)
```

## Q25. What does `index=False` mean in `to_csv()`?
It prevents Pandas from writing the DataFrame's row index as an extra CSV column.

## Q26. How do you find the number of rows in a DataFrame?
Use `len(df)` or `df.shape[0]`.

## Q27. How do you get column names from a DataFrame?
Use `df.columns`.

## Q28. How do you check the structure of a DataFrame?
Use `df.info()` to view column names, data types, and non-null counts.

## Q29. How do you check missing values in a DataFrame?
Use `df.isnull().sum()` to count missing values in each column.

## Q30. What factors should you consider when choosing a Data Source?
Consider reliability, accuracy, completeness, relevance, freshness, accessibility, privacy, and permitted use.

## Q31. What is Data Reliability?
Data reliability refers to how consistently and dependably a source provides trustworthy information.

## Q32. What is Data Accessibility?
Data accessibility describes how easily authorized users can obtain and use data.

## Q33. What is Data Privacy?
Data privacy concerns the proper handling and protection of personal or sensitive information.

## Q34. What is Data Bias?
Data bias occurs when collected data systematically misrepresents a population or situation.

## Q35. What is the difference between a CSV file and a database?
A CSV file stores tabular data in a text file, while a database provides systems for storing, querying, and managing data.

## Q36. What is the difference between an API and Web Scraping?
An API provides a defined interface for accessing data. Web scraping extracts information from website pages.

## Q37. Can a Data Source contain incorrect data?
Yes. A source may contain errors, missing values, duplicates, or outdated information.

## Q38. How can you verify a Data Source?
Check its origin, documentation, update date, accuracy, completeness, and consistency with trusted sources.

## Q39. What is Open Data?
Open data is data made available for public access and reuse under specified terms or licenses.

## Q40. Give an example of Data Sources in a Data Science project.
A sales prediction project might use historical sales CSV files, a business database, and relevant calendar information.

## Quick Revision
- Data Source: Where data comes from
- CSV: Comma-Separated Values
- Database: Organized collection of data
- SQL: Language for relational databases
- API: Defined software communication interface
- Web Scraping: Extracting information from web pages
- Pandas: Python data analysis library
- DataFrame: Rows and columns
- `read_csv()`: Reads a CSV file
- `to_csv()`: Saves a DataFrame to CSV
- Reliable Data: Trustworthy information
- Data Privacy: Protecting personal information
