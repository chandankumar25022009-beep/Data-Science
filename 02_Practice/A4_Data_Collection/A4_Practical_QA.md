# A4 — Data Collection: Practical Questions and Answers

## Q1. Identify Primary Data

**Question:** A company surveys its customers directly. What type of data is collected?

**Answer:** Primary data, because the company collects it directly.

## Q2. Identify Secondary Data

**Question:** A student uses data from a government report for analysis. What type of data is it?

**Answer:** Secondary data, because the data was already collected by another organization.

## Q3. Collect User Data in Python

**Question:** Write Python code to collect a user's name and city.

**Answer:**
```python
name = input("Enter your name: ")
city = input("Enter your city: ")

print("Name:", name)
print("City:", city)



Q4. Create a Small Dataset

Question: Create a small student dataset using Python.

Answer:

import pandas as pd

data = {
    "Name": ["Rahul , "Aman", "Chandan"]
    "Age": [18, 19, 17],
    "City": ["Delhi", "Agra", "meerut"]
}

df = pd.DataFrame(data)
print(df)



Q5. Collect Multiple Values

Question: Create a list containing names of five students.

Answer:

students = ["Rahul", "Aman", "Chandan", "Vikas", "Rohit"]
print(students)


Q6. Store a student's name,age,and course using a dictionary.


Answer:

     </> python

     student = {
        "name": "Chandan"
        "age":17,
        "Course: "Diplome Cse"

     }

print(student)

Q7. Collect Data Using Pandas

Question: Create a DataFrame from collected student information.

Answer:


import pandas as pd

data ={
    "Name": ["Aman", "Rahul", "chandan"]
    Marks":[75, 82, 90]
}

df = ps.DataFrame(data)
print(df)



Q8. Check Dataset Information

Question: How can you check the basic information of a Pandas DataFrame?

Answer:

print(df.info())


Q9. Identify Missing Data

Question: How can you check missing values in a DataFrame?

Answer:

print(df.isnull().sum)

Q10. Identify a Data Source

Question: A dataset is downloaded from a government website. What is its data source?

Answer: The government website is the data source.

Q11. Survey Example

Question: A college asks 100 students about their preferred programming language. What data collection method is used?

Answer: Survey.

Q12. Observation Example

Question: A researcher records how many students enter a library every hour by watching them. What method is used?

Answer: Observation.

Q13. Experiment Example

Question: A company tests two website designs to see which one users prefer. What data collection method is used?

Answer: Experiment.

Q14. API Data Collection

Question: A Python program gets weather information from an online service through an API. What method is used?

Answer: API-based data collection.

Q15. Data Collection Checklist

Question: What should you check before using collected data?

Answer:

Source reliability
Data relevance
Data completeness
Duplicate records
Missing values
Possible bias
Legal and ethical use
Key Learning

Good Data Collection provides reliable and useful data for Data Analysis and Machine Learning.