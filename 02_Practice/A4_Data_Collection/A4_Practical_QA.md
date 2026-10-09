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