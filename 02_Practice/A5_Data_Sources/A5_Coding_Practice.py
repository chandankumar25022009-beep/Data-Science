# A5: Data Sources - Coding practice

# 1. Data using variables
name = "chandan"
age = "17"

print("Name:", name)
print("Age:", age)


# 2. Data using a list
cities = ["Meerut", "Delhi", "Agra"]

print("\nCities:")
for city in cities:
    print(city)

#3, Data using a dictionary
student = {
    "name": "Rahul",
    "marks": 85,
    "course": "CSE"
}

print("\nStudent Data:")
print(student)


# 4. Create a DataFrame using pandas
import pandas as pd

data = {
    "Name": ["Aman", "Rahul", "Chandan"],
    "Marks": [75, 82, 90]
}

df = pd.DataFrame(data)

print("\nStudent Dataset:")
print(df)


# 5. Save data into a CSV file
df.to_csv("student.csv", index=False)

print("\nData saved to students.csv")


# 6. Read data from the CSV file
df_read = pd.read_csv("student.csv")

print("\nData read from CSV:")
print(df_read)

# 7. Display dataset informatuon
print("\nNumber of rows:", len(df_read))
print("Column names:", df_read.columns.tolist())