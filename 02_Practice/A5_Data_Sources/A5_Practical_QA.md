# A5 — Data Sources: Practical Questions and Answers

## Q1. Identify the Data Source

**Question:** A student reads information from a CSV file. What is the data source?

**Answer:** The CSV file is the data source.

## Q2. Read a CSV File Using Python

**Question:** Write Python code to read a CSV file using Pandas.

**Answer:**
```python
import pandas as pd

df = pd.read_csv("students.csv")
print(df)
```

## Q3. Create a DataFrame

**Question:** Create a DataFrame containing student names and marks.

**Answer:**
```python
import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Chandan"],
    "Marks": [75, 82, 90]
}

df = pd.DataFrame(data)
print(df)
```

## Q4. Save Data to a CSV File

**Question:** How do you save a DataFrame to a CSV file?

**Answer:**
```python
df.to_csv("students.csv", index=False)
```

## Q5. Display the Number of Rows

**Question:** How do you count the rows in a DataFrame?

**Answer:**
```python
print(len(df))
```

## Q6. Display Column Names

**Question:** How do you display all column names in a DataFrame?

**Answer:**
```python
print(df.columns.tolist())
```

## Q7. Check Data Types

**Question:** How can you check the data types of DataFrame columns?

**Answer:**
```python
print(df.dtypes)
```

## Q8. Check Missing Values

**Question:** How can you count missing values in each column?

**Answer:**
```python
print(df.isnull().sum())
```

## Q9. Display Basic Dataset Information

**Question:** How can you inspect a DataFrame's structure?

**Answer:**
```python
df.info()
```

## Q10. Identify a Database Source

**Question:** A company stores customer information in a relational database. What is the data source?

**Answer:** The relational database is the data source.

## Q11. Identify an API Source

**Question:** A Python application retrieves weather information through an API. What is the data source?

**Answer:** The weather service's API is the access point for the data.

## Q12. Identify Web Scraping

**Question:** A program extracts publicly available product names from website pages. Which technique is being used?

**Answer:** Web scraping, subject to the website's rules and applicable permissions.

## Q13. Compare Two Data Sources

**Question:** You have a recent official government dataset and an old, unknown website dataset. Which should you investigate first?

**Answer:** Investigate the official government dataset first, while checking its relevance, quality, date, and license.

## Q14. Identify Historical Data

**Question:** A company analyzes its sales records from the previous five years. What type of data is being used?

**Answer:** Historical data.

## Q15. Identify Real-Time Data

**Question:** A dashboard displays traffic conditions as they change. What type of data is it?

**Answer:** Real-time data.

## Q16. Check Whether a CSV File Exists

**Question:** Write Python code to check whether `students.csv` exists.

**Answer:**
```python
from pathlib import Path

file_path = Path("students.csv")
print(file_path.exists())
```

## Q17. Handle a Missing CSV File

**Question:** How can you handle a missing CSV file when reading it?

**Answer:**
```python
import pandas as pd

try:
    df = pd.read_csv("students.csv")
    print(df)
except FileNotFoundError:
    print("CSV file not found.")
```

## Q18. Identify Data Privacy Risks

**Question:** A dataset contains people's names, phone numbers, and addresses. What should you check before using it?

**Answer:** Check authorization, privacy requirements, security, and whether the personal information is necessary.

## Q19. Choose a Suitable Data Source

**Question:** You need population statistics for a research project. How should you choose a source?

**Answer:** Prefer a relevant, reliable official source and verify its date, methodology, and license.

## Q20. Mini Practical: Create and Read a Dataset

**Question:** Create a student dataset, save it to CSV, and read it back.

**Answer:**
```python
import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Chandan"],
    "Marks": [75, 82, 90]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

loaded_df = pd.read_csv("students.csv")
print(loaded_df)
```

## Key Learning

Always check the source, quality, relevance, privacy, and permitted use of data before analysis.
