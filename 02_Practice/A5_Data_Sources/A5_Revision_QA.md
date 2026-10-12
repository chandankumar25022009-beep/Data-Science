# A5 — Data Sources: Revision Questions and Answers

## Q1. What is a Data Source?
A place or system from which data is obtained.

## Q2. Name five common Data Sources.
Files, databases, websites, APIs, and sensors.

## Q3. What is a CSV File?
A text file format used to store tabular data separated by commas.

## Q4. What is a Database?
An organized collection of data that can be stored and managed.

## Q5. What is SQL?
A language used to manage and retrieve data from relational databases.

## Q6. What is an API?
An interface that allows software applications to communicate and exchange data.

## Q7. What is Web Scraping?
Extracting information from website pages using software tools.

## Q8. What is Sensor Data?
Data collected by devices that measure physical conditions.

## Q9. What is Real-Time Data?
Data collected as events happen.

## Q10. What is Historical Data?
Data collected and stored from the past.

## Q11. What is Structured Data?
Data organized in a predefined format, such as rows and columns.

## Q12. What is Unstructured Data?
Data without a fixed tabular structure, such as images and videos.

## Q13. What is Semi-Structured Data?
Data with some organizational elements, such as JSON or XML.

## Q14. What is Primary Data?
Data collected directly for a specific purpose.

## Q15. What is Secondary Data?
Data previously collected by another person or organization.

## Q16. What is Pandas?
A Python library used to manipulate and analyze data.

## Q17. What is a DataFrame?
A two-dimensional data structure organized into rows and columns.

## Q18. How do you read a CSV file in Pandas?
Use `pd.read_csv("students.csv")`.

## Q19. How do you save a DataFrame as a CSV file?
Use `df.to_csv("students.csv", index=False)`.

## Q20. What does `index=False` do?
It prevents the DataFrame row index from being written as an extra CSV column.

## Q21. How do you count DataFrame rows?
Use `len(df)` or `df.shape[0]`.

## Q22. How do you display column names?
Use `df.columns.tolist()`.

## Q23. How do you check column data types?
Use `df.dtypes`.

## Q24. How do you count missing values?
Use `df.isnull().sum()`.

## Q25. How do you inspect DataFrame information?
Use `df.info()`.

## Q26. What makes a Data Source reliable?
Accuracy, consistency, trustworthy origin, and appropriate documentation.

## Q27. What is Data Accessibility?
How easily authorized users can obtain and use data.

## Q28. What is Data Privacy?
The proper protection and handling of personal or sensitive information.

## Q29. What is Open Data?
Data made available for public access and reuse under specified terms.

## Q30. What should you check before selecting a Data Source?
Reliability, accuracy, completeness, relevance, freshness, privacy, and license.

## Quick Revision
- CSV → Tabular text file
- Database → Organized data storage
- SQL → Relational database language
- API → Software communication interface
- Web Scraping → Extracting data from web pages
- Pandas → Python data analysis library
- DataFrame → Rows and columns
- `read_csv()` → Reads CSV data
- `to_csv()` → Saves CSV data
- `df.info()` → Displays DataFrame information
- `df.dtypes` → Shows column data types
- `df.isnull().sum()` → Counts missing values
