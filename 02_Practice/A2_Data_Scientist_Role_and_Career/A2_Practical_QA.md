# A2 – Data Scientist Role and Career

# Practical Questions & Answers

## Q1. Create a list of Data Science skills.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]
print(skills)
```

## Q2. Print all Data Science skills.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

for skill in skills:
    print(skill)
```

## Q3. Count the total number of skills.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

print("Total Skills:", len(skills))
```

## Q4. Add Power BI to the skills list.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

skills.append("Power BI")
print(skills)
```

## Q5. Check whether Python is available.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

if "Python" in skills:
    print("Python is available")
```

## Q6. Remove SQL from the skills list.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

skills.remove("SQL")
print(skills)
```

## Q7. Find the longest skill name.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

longest = max(skills, key=len)
print("Longest Skill:", longest)
```

## Q8. Find the length of every skill.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

for skill in skills:
    print(skill, "->", len(skill))
```

## Q9. Print skills having more than 5 characters.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

for skill in skills:
    if len(skill) > 5:
        print(skill)
```

## Q10. Count skills having more than 5 characters.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

count = 0

for skill in skills:
    if len(skill) > 5:
        count += 1

print("Count:", count)
```

## Q11. Create a Data Scientist profile using a dictionary.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

print(profile)
```

## Q12. Access the name from the profile.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

print(profile["name"])
```

## Q13. Access the main skill.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

print(profile["main_skill"])
```

## Q14. Add a learning field to the profile.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

profile["learning"] = "Data Science"

print(profile)
```

## Q15. Count profile fields.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python",
    "learning": "Data Science"
}

print("Profile Fields:", len(profile))
```

## Q16. Print all profile fields.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python",
    "learning": "Data Science"
}

for key, value in profile.items():
    print(key, ":", value)
```

## Q17. Check whether Python is the main skill.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

if profile["main_skill"] == "Python":
    print("Python is the main skill")
```

## Q18. Create a student profile.

**Answer:**

```python
student = {
    "name": "Chandan",
    "course": "CSE",
    "year": 2026
}

print(student)
```

## Q19. Add a skill to the student profile.

**Answer:**

```python
student = {
    "name": "Chandan",
    "course": "CSE",
    "year": 2026
}

student["skill"] = "Python"

print(student)
```

## Q20. Check the student's course.

**Answer:**

```python
student = {
    "name": "Chandan",
    "course": "CSE",
    "year": 2026
}

if student["course"] == "CSE":
    print("Student is studying CSE")
```

## Q21. Create a list of multiple students.

**Answer:**

```python
students = ["Chandan", "Rahul", "Aman", "Rohit"]

print(students)
```

## Q22. Count the students.

**Answer:**

```python
students = ["Chandan", "Rahul", "Aman", "Rohit"]

print("Total Students:", len(students))
```

## Q23. Check whether Chandan is present.

**Answer:**

```python
students = ["Chandan", "Rahul", "Aman", "Rohit"]

if "Chandan" in students:
    print("Chandan is present")
```

## Q24. Print every student.

**Answer:**

```python
students = ["Chandan", "Rahul", "Aman", "Rohit"]

for student in students:
    print(student)
```

## Q25. Create a dictionary of student marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

print(marks)
```

## Q26. Print Chandan's marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

print("Chandan Marks:", marks["Chandan"])
```

## Q27. Find students with marks of 80 or more.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

for name, mark in marks.items():
    if mark >= 80:
        print(name, mark)
```

## Q28. Calculate average marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

average = sum(marks.values()) / len(marks)

print("Average Marks:", average)
```

## Q29. Find the highest marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

highest = max(marks.values())

print("Highest Marks:", highest)
```

## Q30. Find the student with the highest marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

top_student = max(marks, key=marks.get)

print("Top Student:", top_student)
print("Marks:", marks[top_student])
```

## Q31. Count skills starting with S.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

count = 0

for skill in skills:
    if skill.startswith("S"):
        count += 1

print("Skills starting with S:", count)
```

## Q32. Print skills starting with S.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

for skill in skills:
    if skill.startswith("S"):
        print(skill)
```

## Q33. Find whether SQL is available.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

if "SQL" in skills:
    print("SQL is available")
else:
    print("SQL is not available")
```

## Q34. Add Data Visualization.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning"]

skills.append("Data Visualization")

print(skills)
```

## Q35. Remove Excel.

**Answer:**

```python
skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

skills.remove("Excel")

print(skills)
```

## Q36. Create a complete Data Scientist profile.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"],
    "learning": "Machine Learning"
}

print(profile)
```

## Q37. Print all skills from the profile.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

for skill in profile["skills"]:
    print(skill)
```

## Q38. Count profile skills.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

print("Skill Count:", len(profile["skills"]))
```

## Q39. Add Machine Learning to profile skills.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

profile["skills"].append("Machine Learning")

print(profile)
```

## Q40. Check whether Python is in profile skills.

**Answer:**

```python
profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

if "Python" in profile["skills"]:
    print("Python is available")
```

## Q41. Create a list of Data Science tools.

**Answer:**

```python
tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

print(tools)
```

## Q42. Count Data Science tools.

**Answer:**

```python
tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

print("Total Tools:", len(tools))
```

## Q43. Print every Data Science tool.

**Answer:**

```python
tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

for tool in tools:
    print(tool)
```

## Q44. Find the longest tool name.

**Answer:**

```python
tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

longest = max(tools, key=len)

print("Longest Tool:", longest)
```

## Q45. Create a career roadmap list.

**Answer:**

```python
roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

print(roadmap)
```

## Q46. Print the career roadmap step by step.

**Answer:**

```python
roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

for step in roadmap:
    print(step)
```

## Q47. Count roadmap steps.

**Answer:**

```python
roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

print("Roadmap Steps:", len(roadmap))
```

## Q48. Check whether Machine Learning is included.

**Answer:**

```python
roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

if "Machine Learning" in roadmap:
    print("Machine Learning is included")
```

## Q49. Create a job skills dictionary.

**Answer:**

```python
job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required",
    "Statistics": "Required"
}

print(job)
```

## Q50. Print all job requirements.

**Answer:**

```python
job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required",
    "Statistics": "Required"
}

for key, value in job.items():
    print(key, ":", value)
```

## Q51. Count job requirements.

**Answer:**

```python
job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required",
    "Statistics": "Required"
}

print("Requirements:", len(job))
```

## Q52. Check whether Python is required.

**Answer:**

```python
job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required"
}

if job["Python"] == "Required":
    print("Python is required")
```

## Q53. Create marks for five students.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

print(marks)
```

## Q54. Print all student marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

for name, mark in marks.items():
    print(name, ":", mark)
```

## Q55. Count students scoring 80 or more.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

count = 0

for mark in marks.values():
    if mark >= 80:
        count += 1

print("Students:", count)
```

## Q56. Calculate total marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

total = sum(marks.values())

print("Total Marks:", total)
```

## Q57. Calculate average marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

average = sum(marks.values()) / len(marks)

print("Average:", average)
```

## Q58. Find the lowest marks.

**Answer:**

```python
marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

lowest = min(marks.values())

print("Lowest Marks:", lowest)
```

##Q58. Find the lowest marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

lowest = min(marks.values())

print("Lowest Marks:", lowest)

Q59. Find the student with the lowest marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

lowest_student = min(marks, key=marks.get)

print("Lowest Student:", lowest_student)
print("Marks:", marks[lowest_student])

Q60. Print students who passed with 40 or more.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

for name, mark in marks.items():
    if mark >= 40:
        print(name, "Passed")

Q61. Create a list of Data Science tasks.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

print(tasks)

Q62. Print Data Science tasks.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

for task in tasks:
    print(task)

Q63. Count Data Science tasks.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

print("Tasks:", len(tasks))

Q64. Check whether data cleaning is included.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

if "Clean Data" in tasks:
    print("Data cleaning is included")

Q65. Create a simple Data Scientist project.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas",
    "output": "Data Insights"
}

print(project)

Q66. Print project name.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas"
}

print(project["name"])

Q67. Print project technology.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas"
}

print(project["language"])

Q68. Add visualization to the project.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas"
}

project["visualization"] = "Matplotlib"

print(project)

Q69. Count project fields.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas",
    "visualization": "Matplotlib"
}

print("Project Fields:", len(project))

Q70. Print complete project information.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas",
    "visualization": "Matplotlib"
}

for key, value in project.items():
    print(key, ":", value)

Q71. Create a list of Data Scientist responsibilities.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

print(responsibilities)

Q72. Print responsibilities.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

for responsibility in responsibilities:
    print(responsibility)

Q73. Count responsibilities.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

print(len(responsibilities))

Q74. Check whether analysis is a responsibility.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

if "Analyze Data" in responsibilities:
    print("Analysis is a responsibility")

Q75. Create a list of career roles.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

print(roles)

Q76. Print all career roles.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

for role in roles:
    print(role)

Q77. Count career roles.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

print("Roles:", len(roles))

Q78. Check whether Data Scientist exists.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

if "Data Scientist" in roles:
    print("Data Scientist exists")

Q79. Create a learning progress dictionary.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress",
    "Machine Learning": "Not Started"
}

print(progress)

Q80. Print learning progress.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress",
    "Machine Learning": "Not Started"
}

for skill, status in progress.items():
    print(skill, ":", status)

Q81. Check whether Python is completed.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress"
}

if progress["Python"] == "Completed":
    print("Python completed")

Q82. Change SQL status to Completed.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress"
}

progress["SQL"] = "Completed"

print(progress)

Q83. Count completed skills.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "Completed",
    "Statistics": "In Progress",
    "Machine Learning": "Not Started"
}

count = 0

for status in progress.values():
    if status == "Completed":
        count += 1

print("Completed Skills:", count)

Q84. Create a simple company data dictionary.

Answer:

company = {
    "name": "ABC Company",
    "industry": "Technology",
    "role": "Data Scientist",
    "location": "India"
}

print(company)

Q85. Print company information.

Answer:

company = {
    "name": "ABC Company",
    "industry": "Technology",
    "role": "Data Scientist",
    "location": "India"
}

for key, value in company.items():
    print(key, ":", value)

Q86. Check company industry.

Answer:

company = {
    "name": "ABC Company",
    "industry": "Technology"
}

if company["industry"] == "Technology":
    print("Technology company")

Q87. Create a salary list.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

print(salaries)

Q88. Calculate average salary.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

average = sum(salaries) / len(salaries)

print("Average Salary:", average)

Q89. Find the highest salary.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

print("Highest Salary:", max(salaries))

Q90. Find the lowest salary.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

print("Lowest Salary:", min(salaries))

Q91. Create a Data Science learning plan.

Answer:

learning_plan = {
    "Step 1": "Python",
    "Step 2": "SQL",
    "Step 3": "Statistics",
    "Step 4": "Data Analysis",
    "Step 5": "Machine Learning",
    "Step 6": "Projects"
}

print(learning_plan)

Q92. Print the learning plan.

Answer:

learning_plan = {
    "Step 1": "Python",
    "Step 2": "SQL",
    "Step 3": "Statistics",
    "Step 4": "Data Analysis",
    "Step 5": "Machine Learning",
    "Step 6": "Projects"
}

for step, topic in learning_plan.items():
    print(step, ":", topic)

Q93. Count learning plan steps.

Answer:

learning_plan = {
    "Step 1": "Python",
    "Step 2": "SQL",
    "Step 3": "Statistics",
    "Step 4": "Data Analysis",
    "Step 5": "Machine Learning",
    "Step 6": "Projects"
}

print("Total Steps:", len(learning_plan))

Q94. Create a list of project ideas.

Answer:

projects = [
    "Student Performance Analysis",
    "Sales Analysis",
    "Customer Analysis",
    "House Price Prediction"
]

print(projects)

Q95. Count project ideas.

Answer:

projects = [
    "Student Performance Analysis",
    "Sales Analysis",
    "Customer Analysis",
    "House Price Prediction"
]

print("Project Ideas:", len(projects))

Q96. Check whether Sales Analysis exists.

Answer:

projects = [
    "Student Performance Analysis",
    "Sales Analysis",
    "Customer Analysis",
    "House Price Prediction"
]

if "Sales Analysis" in projects:
    print("Sales Analysis is available")

Q97. Create a final Data Scientist skill profile.

Answer:

data_scientist = {
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ]
}

print(data_scientist)

Q98. Print all final skills.

Answer:

data_scientist = {
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ]
}

for skill in data_scientist["skills"]:
    print(skill)

Q99. Count final Data Scientist skills.

Answer:

data_scientist = {
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ]
}

print("Total Skills:", len(data_scientist["skills"]))

Q100. Build a complete simple Data Science profile.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ],
    "project": "Student Performance Analysis"
}

print("Name:", profile["name"])
print("Role:", profile["role"])
print("Project:", profile["project"])

print("Skills:")
for skill in profile["skills"]:
    print("-", skill)

Q13. Access the main skill.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

print(profile["main_skill"])

Q14. Add a learning field to the profile.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

profile["learning"] = "Data Science"

print(profile)

Q15. Count profile fields.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python",
    "learning": "Data Science"
}

print("Profile Fields:", len(profile))

Q16. Print all profile fields.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python",
    "learning": "Data Science"
}

for key, value in profile.items():
    print(key, ":", value)

Q17. Check whether Python is the main skill.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "main_skill": "Python"
}

if profile["main_skill"] == "Python":
    print("Python is the main skill")

Q18. Create a student profile.

Answer:

student = {
    "name": "Chandan",
    "course": "CSE",
    "year": 2026
}

print(student)

Q19. Add a skill to the student profile.

Answer:

student = {
    "name": "Chandan",
    "course": "CSE",
    "year": 2026
}

student["skill"] = "Python"

print(student)

Q20. Check the student's course.

Answer:

student = {
    "name": "Chandan",
    "course": "CSE",
    "year": 2026
}

if student["course"] == "CSE":
    print("Student is studying CSE")

Q21. Create a list of multiple students.

Answer:

students = ["Chandan", "Rahul", "Aman", "Rohit"]

print(students)

Q22. Count the students.

Answer:

students = ["Chandan", "Rahul", "Aman", "Rohit"]

print("Total Students:", len(students))

Q23. Check whether Chandan is present.

Answer:

students = ["Chandan", "Rahul", "Aman", "Rohit"]

if "Chandan" in students:
    print("Chandan is present")

Q24. Print every student.

Answer:

students = ["Chandan", "Rahul", "Aman", "Rohit"]

for student in students:
    print(student)

Q25. Create a dictionary of student marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

print(marks)

Q26. Print Chandan's marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

print("Chandan Marks:", marks["Chandan"])

Q27. Find students with marks of 80 or more.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

for name, mark in marks.items():
    if mark >= 80:
        print(name, mark)

Q28. Calculate average marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

average = sum(marks.values()) / len(marks)

print("Average Marks:", average)

Q29. Find the highest marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

highest = max(marks.values())

print("Highest Marks:", highest)

Q30. Find the student with the highest marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67
}

top_student = max(marks, key=marks.get)

print("Top Student:", top_student)
print("Marks:", marks[top_student])

Q31. Count skills starting with S.

Answer:

skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

count = 0

for skill in skills:
    if skill.startswith("S"):
        count += 1

print("Skills starting with S:", count)

Q32. Print skills starting with S.

Answer:

skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

for skill in skills:
    if skill.startswith("S"):
        print(skill)

Q33. Find whether SQL is available.

Answer:

skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

if "SQL" in skills:
    print("SQL is available")
else:
    print("SQL is not available")

Q34. Add Data Visualization.

Answer:

skills = ["Python", "SQL", "Statistics", "Machine Learning"]

skills.append("Data Visualization")

print(skills)

Q35. Remove Excel.

Answer:

skills = ["Python", "SQL", "Statistics", "Machine Learning", "Excel"]

skills.remove("Excel")

print(skills)

Q36. Create a complete Data Scientist profile.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"],
    "learning": "Machine Learning"
}

print(profile)

Q37. Print all skills from the profile.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

for skill in profile["skills"]:
    print(skill)

Q38. Count profile skills.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

print("Skill Count:", len(profile["skills"]))

Q39. Add Machine Learning to profile skills.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

profile["skills"].append("Machine Learning")

print(profile)

Q40. Check whether Python is in profile skills.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": ["Python", "SQL", "Statistics"]
}

if "Python" in profile["skills"]:
    print("Python is available")

Q41. Create a list of Data Science tools.

Answer:

tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

print(tools)

Q42. Count Data Science tools.

Answer:

tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

print("Total Tools:", len(tools))

Q43. Print every Data Science tool.

Answer:

tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

for tool in tools:
    print(tool)

Q44. Find the longest tool name.

Answer:

tools = ["Python", "Pandas", "NumPy", "Matplotlib", "Scikit-learn"]

longest = max(tools, key=len)

print("Longest Tool:", longest)

Q45. Create a career roadmap list.

Answer:

roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

print(roadmap)

Q46. Print the career roadmap step by step.

Answer:

roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

for step in roadmap:
    print(step)

Q47. Count roadmap steps.

Answer:

roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

print("Roadmap Steps:", len(roadmap))

Q48. Check whether Machine Learning is included.

Answer:

roadmap = [
    "Python",
    "SQL",
    "Statistics",
    "Data Analysis",
    "Machine Learning",
    "Projects"
]

if "Machine Learning" in roadmap:
    print("Machine Learning is included")

Q49. Create a job skills dictionary.

Answer:

job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required",
    "Statistics": "Required"
}

print(job)

Q50. Print all job requirements.

Answer:

job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required",
    "Statistics": "Required"
}

for key, value in job.items():
    print(key, ":", value)

Q51. Count job requirements.

Answer:

job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required",
    "Statistics": "Required"
}

print("Requirements:", len(job))

Q52. Check whether Python is required.

Answer:

job = {
    "role": "Data Scientist",
    "Python": "Required",
    "SQL": "Required"
}

if job["Python"] == "Required":
    print("Python is required")

Q53. Create marks for five students.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

print(marks)

Q54. Print all student marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

for name, mark in marks.items():
    print(name, ":", mark)

Q55. Count students scoring 80 or more.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

count = 0

for mark in marks.values():
    if mark >= 80:
        count += 1

print("Students:", count)

Q56. Calculate total marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

total = sum(marks.values())

print("Total Marks:", total)

Q57. Calculate average marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

average = sum(marks.values()) / len(marks)

print("Average:", average)

Q58. Find the lowest marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

lowest = min(marks.values())

print("Lowest Marks:", lowest)

Q59. Find the student with the lowest marks.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

lowest_student = min(marks, key=marks.get)

print("Lowest Student:", lowest_student)
print("Marks:", marks[lowest_student])

Q60. Print students who passed with 40 or more.

Answer:

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Aman": 90,
    "Rohit": 67,
    "Vikas": 80
}

for name, mark in marks.items():
    if mark >= 40:
        print(name, "Passed")

Q61. Create a list of Data Science tasks.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

print(tasks)

Q62. Print Data Science tasks.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

for task in tasks:
    print(task)

Q63. Count Data Science tasks.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

print("Tasks:", len(tasks))

Q64. Check whether data cleaning is included.

Answer:

tasks = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Visualize Data",
    "Build Model"
]

if "Clean Data" in tasks:
    print("Data cleaning is included")

Q65. Create a simple Data Scientist project.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas",
    "output": "Data Insights"
}

print(project)

Q66. Print project name.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas"
}

print(project["name"])

Q67. Print project technology.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas"
}

print(project["language"])

Q68. Add visualization to the project.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas"
}

project["visualization"] = "Matplotlib"

print(project)

Q69. Count project fields.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas",
    "visualization": "Matplotlib"
}

print("Project Fields:", len(project))

Q70. Print complete project information.

Answer:

project = {
    "name": "Student Performance Analysis",
    "language": "Python",
    "tool": "Pandas",
    "visualization": "Matplotlib"
}

for key, value in project.items():
    print(key, ":", value)

Q71. Create a list of Data Scientist responsibilities.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

print(responsibilities)

Q72. Print responsibilities.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

for responsibility in responsibilities:
    print(responsibility)

Q73. Count responsibilities.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

print(len(responsibilities))

Q74. Check whether analysis is a responsibility.

Answer:

responsibilities = [
    "Collect Data",
    "Clean Data",
    "Analyze Data",
    "Create Visualizations",
    "Build Models"
]

if "Analyze Data" in responsibilities:
    print("Analysis is a responsibility")

Q75. Create a list of career roles.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

print(roles)

Q76. Print all career roles.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

for role in roles:
    print(role)

Q77. Count career roles.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

print("Roles:", len(roles))

Q78. Check whether Data Scientist exists.

Answer:

roles = [
    "Data Analyst",
    "Data Scientist",
    "Data Engineer",
    "ML Engineer"
]

if "Data Scientist" in roles:
    print("Data Scientist exists")

Q79. Create a learning progress dictionary.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress",
    "Machine Learning": "Not Started"
}

print(progress)

Q80. Print learning progress.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress",
    "Machine Learning": "Not Started"
}

for skill, status in progress.items():
    print(skill, ":", status)

Q81. Check whether Python is completed.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress"
}

if progress["Python"] == "Completed":
    print("Python completed")

Q82. Change SQL status to Completed.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "In Progress",
    "Statistics": "In Progress"
}

progress["SQL"] = "Completed"

print(progress)

Q83. Count completed skills.

Answer:

progress = {
    "Python": "Completed",
    "SQL": "Completed",
    "Statistics": "In Progress",
    "Machine Learning": "Not Started"
}

count = 0

for status in progress.values():
    if status == "Completed":
        count += 1

print("Completed Skills:", count)

Q84. Create a simple company data dictionary.

Answer:

company = {
    "name": "ABC Company",
    "industry": "Technology",
    "role": "Data Scientist",
    "location": "India"
}

print(company)

Q85. Print company information.

Answer:

company = {
    "name": "ABC Company",
    "industry": "Technology",
    "role": "Data Scientist",
    "location": "India"
}

for key, value in company.items():
    print(key, ":", value)

Q86. Check company industry.

Answer:

company = {
    "name": "ABC Company",
    "industry": "Technology"
}

if company["industry"] == "Technology":
    print("Technology company")

Q87. Create a salary list.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

print(salaries)

Q88. Calculate average salary.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

average = sum(salaries) / len(salaries)

print("Average Salary:", average)

Q89. Find the highest salary.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

print("Highest Salary:", max(salaries))

Q90. Find the lowest salary.

Answer:

salaries = [30000, 40000, 50000, 60000, 70000]

print("Lowest Salary:", min(salaries))

Q91. Create a Data Science learning plan.

Answer:

learning_plan = {
    "Step 1": "Python",
    "Step 2": "SQL",
    "Step 3": "Statistics",
    "Step 4": "Data Analysis",
    "Step 5": "Machine Learning",
    "Step 6": "Projects"
}

print(learning_plan)

Q92. Print the learning plan.

Answer:

learning_plan = {
    "Step 1": "Python",
    "Step 2": "SQL",
    "Step 3": "Statistics",
    "Step 4": "Data Analysis",
    "Step 5": "Machine Learning",
    "Step 6": "Projects"
}

for step, topic in learning_plan.items():
    print(step, ":", topic)

Q93. Count learning plan steps.

Answer:

learning_plan = {
    "Step 1": "Python",
    "Step 2": "SQL",
    "Step 3": "Statistics",
    "Step 4": "Data Analysis",
    "Step 5": "Machine Learning",
    "Step 6": "Projects"
}

print("Total Steps:", len(learning_plan))

Q94. Create a list of project ideas.

Answer:

projects = [
    "Student Performance Analysis",
    "Sales Analysis",
    "Customer Analysis",
    "House Price Prediction"
]

print(projects)

Q95. Count project ideas.

Answer:

projects = [
    "Student Performance Analysis",
    "Sales Analysis",
    "Customer Analysis",
    "House Price Prediction"
]

print("Project Ideas:", len(projects))

Q96. Check whether Sales Analysis exists.

Answer:

projects = [
    "Student Performance Analysis",
    "Sales Analysis",
    "Customer Analysis",
    "House Price Prediction"
]

if "Sales Analysis" in projects:
    print("Sales Analysis is available")

Q97. Create a final Data Scientist skill profile.

Answer:

data_scientist = {
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ]
}

print(data_scientist)

Q98. Print all final skills.

Answer:

data_scientist = {
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ]
}

for skill in data_scientist["skills"]:
    print(skill)

Q99. Count final Data Scientist skills.

Answer:

data_scientist = {
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ]
}

print("Total Skills:", len(data_scientist["skills"]))

Q100. Build a complete simple Data Science profile.

Answer:

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "skills": [
        "Python",
        "SQL",
        "Statistics",
        "Data Analysis",
        "Visualization",
        "Machine Learning"
    ],
    "project": "Student Performance Analysis"
}

print("Name:", profile["name"])
print("Role:", profile["role"])
print("Project:", profile["project"])

print("Skills:")
for skill in profile["skills"]:
    print("-", skill)

PRACTICAL REVISION

    List → Multiple values store करता है.

    Dictionary → Key-value data store करता है.

    append() → List में item add करता है.

    remove() → List से item remove करता है.

    len() → Number/length बताता है.

    max() → Maximum value देता है.

    min() → Minimum value देता है.

    sum() → Values का total देता है.

    in → किसी item की presence check करता है.

    for loop → Values को one-by-one process करता है.

    startswith() → String के starting characters check करता है.

    dictionary.items() → Key और value दोनों देता है.

FINAL KEY POINT

Practical Data Science learning में Python lists, dictionaries, loops,
conditions और basic calculations का मजबूत knowledge बहुत important है।