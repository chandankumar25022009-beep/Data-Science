# Step 1 - Data Scientist Basic Information

name ="Chandan"
role = "Data Scientist"
skills = "Python"

print("Name:", name)
print("Role:", role)
print("Skills:", skills)

#Step 2 - Data Scientist Career Path

skills = ["python", "RQL", "Statistics", "Machine Learning"]

print ("Data Scientist skills:")
for skill in skills:
    print(skill)

# Step 3 - Count Data Scientist Skills

skills = ["python", "SQL", "Statistics", "machine Learning"]

skill_count = len(skills)

print("Total Skills:", skill_count)


# Step 4 - Check Data Science Skills

skills = ["python", "SQL", "Statistics", "Machine Learning"]

if "python" in skills:
    print("python is included")
else:
    print("python is not included")

# Step 5 - find a Specific Skill

skills = ["python", "SQL", "Statistics", "Machine Learning"]

for skill in skills:
    if skill == "python":
        print("Found:", skill)



# Step 6 - Count Skills Starting with S

skills = ["python", "SQL", "Statistics", "Machine Learning"]

count = 0

for skill in skills:
    if skill.startswith("S"):
        count = count + 1

print("Skills starting with S:", count)


# Step 7 - Add a New Skill

skills = ["python", "SQL", "Statistics", "Machine Learning"]

skills.append("Data Visualization")

print("Updated Skills:")
for skill in skills:
    print(skill)


# Step 8 - Remove a skill

skills = ["python", "SQL", "Statistics", "Machine Learning"]

skills.remove("SQL")

print("Skills after removing SQL:")
for skill in skills:
    print(skill)


# Step 9 - Count Skills 

skills = ["python", "SQL", "Statistics", "Machine Learning"]

print("Number of Skills:", len(skills))


# Step 10 - Find the Longest Skill Name

skills = ["python", "SQL", "Statistics", "Machine Learning"]

longest_skill = ""
for skill in skills:
    if len(skill) > len(longest_skill):
        longest_skill = skill

print("Longest Skill :", longest_skill)


# Step 11 - Check Skill Length

skills = ["python", "SQL", "Statistics", "Machine Learning"]

for skill in skills:
    print(skill, "->", len(skill), "characters")


    # Step 12 - Skills with More Than 5 Characters

    skills = ["python", "SQL", "Statistics", "Machine Learning"]

for skill in skills:
    if len(skill) > 5:
        print("Long Skill:", skill)


# Step 13 - Data Scientist Progile

profile = {

    "name": "Chandan",
    "role": "Data Scientist",
    "experience": "Beginner",
    "main_skills": "python"
}


print("Name:", profile["name"])
print("Role:", profile["role"])
print("Experience:", profile["experience"])
print("Main Skills:", profile["main_skills"])


# Step 14 - Access Profile Data

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "experience": "Beginner",
    "main_skill": "Python"
}

print("Name:", profile.get("name"))
print("Role:", profile.get("role"))
print("Main Skill:", profile.get("main_skill"))


# Step 15 - Add New profile Field

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "experience": "Beginner",
    "main_skill": "python"
}


profile["learning"] = "Data Science"

print("Profile Learning:", profile["learning"])

# Step 16 - Check Profile Fields

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "experience": "Beginner",
    "main_skill": "Python",
    "learning": "Data Science"
}

for key, value in profile.items():
    print(key, ":", value)


# Step 17 - count profile Fields

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "experience": "Beginner",
    "main_skill": "Python",
    "learning": "Data Science"
}

print("Total Profile Fields:", len(profile))


# Step 18 - Check Main Skill

profile = {
    "name": "Chandan",
    "role": "Data Scientist",
    "experience": "Beginner",
    "main_skill": "Python",
    "learning": "Data Science"
}

if profile["main_skill"] == "Python":
    print("Main skill is Python")
else:
    print("Main skill is not Python")


# Step 19 - Add Another Skill

skills = ["Python", "SQL", "Statistics", "Machine Learning"]

skills.append("Excel")

print("Updated Skills:")
for skill in skills:
    print(skill)


# Step 20 - Check if SQL is Available

skills = ["Python", "SQL", "Statistics", "Machine Learning"]

if "SQL" in skills:
    print("SQL is available")
else:
    print("SQL is not available")


# Step 21 - Count Skills with More Than 5 Characters

skills = ["Python", "SQL", "Statistics", "Machine Learning"]

count = 0

for skill in skills:
    if len(skill) > 5:
        count = count + 1

print("Skills with more than 5 characters:", count)


# Step 22 - Create Student Data

student = {
    "name": "Chandan",
    "course": "Computer Science",
    "year": 2
}

print("Student Name:", student["name"])
print("Course:", student["course"])
print("Year:", student["year"])


# Step 23 - Add Student Skill

student = {
    "name": "Chandan",
    "course": "Computer Science",
    "year": 2
}

student["skill"] = "Python"

print("Student Skill:", student["skill"])


# Step 24 - Check Student Course

student = {
    "name": "Chandan",
    "course": "Computer Science",
    "year": 2,
    "skill": "Python"
}

if student["course"] == "Computer Science":
    print("Student is from Computer Science")


# Step 25 - Create Multiple Students

students = ["Chandan", "Rahul", "Amit", "Ravi"]

print("Students:")

for student in students:
    print(student)


# Step 26 - Count Students

students = ["Chandan", "Rahul", "Amit", "Ravi"]

print("Total Students:", len(students))


# Step 27 - Check Student Name

students = ["Chandan", "Rahul", "Amit", "Ravi"]

if "Chandan" in students:
    print("Chandan is present")
else:
    print("Chandan is not present")


# Step 28 - Student Marks

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Amit": 90,
    "Ravi": 65
}

for student, mark in marks.items():
    print(student, ":", mark)


# Step 29 - Find Students with Good Marks

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Amit": 90,
    "Ravi": 65
}

for student, mark in marks.items():
    if mark >= 80:
        print(student, "-> Good Marks")


# Step 30 - Find Average Marks

marks = {
    "Chandan": 85,
    "Rahul": 72,
    "Amit": 90,
    "Ravi": 65
}

total = 0

for mark in marks.values():
    total = total + mark

average = total / len(marks)

print("Average Marks:", average)
