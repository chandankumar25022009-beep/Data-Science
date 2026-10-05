# =============================
#A1 - WHat is DAta Science
# Coding practice
# ==============================



#Step 1 - Basic Data
name = "Chandan"
subject = "Data Science"
year = 2026

print("Name:", name)
print("Subject:", subject)
print("Year:", year)




# Step 2 - Variables 
student_name = "Chandan kumar"
course = "Data Science"
skill = "Data Science"

print("Student Name:", student_name)
print("Course:", course)
print("Skill:", skill)


# Step 3 - List of Subjects
subjects = ["python", "Statistics", "Data Science",]

print("My subjects:")
print(subjects)


# Step 4 - Access List Items


print("First subject", subjects[0])
print("Second subject", subjects[1])
print("Third subject", subjects[2])

# Step 5 - Add New Sata to List
subjects.append("Machine Learning")
print("Updated subjects:")
print(subjects)


"""# Step 6 - Numerical DAta

Students = 50
Projects = 3


print("Number of students:", students)
print("Number of projects:", projects)
print("Study hours per day:", hours_per_day)"""


# Step 6 - Numerical Data

students = 50
projects = 3
hours_per_day = 2

print("Number of students:", students)
print("Number of projects:", projects)
print("Study hours per day:", hours_per_day)



# Step 7 - Calculations with Data

students = 50
projects = 3

total_work = students * projects

print("Total student-project work:", total_work)


# Step 8 - Average Calculation

marks = [70, 80, 90, 60, 100]

total_marks = sum(marks)
number_of_subjects = len(marks)

average_marks = total_marks / number_of_subjects

print("Total Marks:", total_marks)
print("Number of Subjects:", number_of_subjects)
print("Average Marks:", average_marks)


#Step 9 - Find Maximum and Minimum

marks = [70, 80, 90, 60, 100]


highest_marks = max(marks)
lowest_marks = min(marks)

print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)


# Step 10 - Conditional Statements

marks = [70, 80, 90, 60, 100]

number_of_subjects = len(marks)


print("Number of Marks:", number_of_subjects)



# Step 11 - Conditional Statements

average_marks = 80

if average_marks >= 60:
    print("Result: Good")
else:
    print("Result: Needs Improvement")


    # Step 12 - Multiple Conditions

average_marks = 80

if average_marks >= 90:
    print("Grade: A+")
elif average_marks >= 75:
    print("Grade: A")
elif average_marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")


   # Step 13 - User Input

student_name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name:", student_name)
print("Age:", age)

# 14 - Input and Calculation

marks1 = int(input("Enter marks of Subject 1:"))
marks2 = int(input("Enter marks of Subject 2:"))
marks3 = int(input("Enter marks of Subject 3:"))

total = marks1 + marks2 + marks3
average = total / 3

print("Total Marks:", total)
print("Average Marks:", average)

# 15 - Data classification

marks = 61

if marks >= 75:
    category = "Good"
elif marks >= 50:
    category = "Average"
else:
    category = "Needs Improvement"

print("Marks:", marks)
print("Category:", category)

# step 16 - Loop through Data

marks = [70, 80, 90,60, 100]

for mark in marks:
    print("Mark:", mark)


# Step 17 - Loop with Condition

marks = [70, 80, 90, 60, 100]

for mark in marks:
    if mark >= 75:
        print(mark, "-> Good")
    else:
        print(mark, "-> Needs Improvement")

# Step 18 - Count Good Marks
marks = [70, 80, 90,60, 100]

good_marks = 0

for mark in marks:
    if mark >= 75:
        good_marks = good_marks + 1

print("number of Good Marks:", good_marks)

# Step 19 - Function to Calculate Total Using Loop

marks = [70, 80, 90, 60, 100]

total = 0

for mark in marks:
    total += mark

print("Total Marks Using Loop:", total)


#Step 20 - Calculate Average Using Loop

marks = [70, 80, 90, 60, 100]

total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("Average Using Loop:", average)

# Step 21 - Even and odd Numbers

numbers = [10, 15, 20, 25, 30]

for number in numbers:
    if number % 2 == 0:
        print(number, "-> Even")
    else:
        print(number, "-> Odd")

# Step 22 -Positive and Negative Numbers

numbers = [10, -5, 20, -15, 0]

for number in numbers:
    if number > 0:
        print(number, "-> positive")
    elif number < 0:
        print(number, "-> Negative")
    else:
        print(number, "-> Zero")

# Step 23 - Zero and Non-Zero Numbers

numbers = [10, 0, 25, 0, -5]

for number in numbers:
    if number == 0:
        print(number, "-> Zero")
    else:
        print(number, "-> Non-Zero")

# Step 24 - Count positive Numbers

numbers = [10, -5, 20, -15, 30]


positive_count = 0

for number in numbers:
    if number > 0:
        positive_count = positive_count + 1

print("Positive Numbers:", positive_count)


# 25 - Count Negative Numbers

numbers = [10, -5, 20, -15, 30]

negative_count = 0

for number in numbers:
    if number < 0:
        negative_count = negative_count + 1

print("Negative Numbers:", negative_count)

# 26 - Count Zero Numbers

numbers = [10, 0, 20, 0, -5, 0]

zero_count = 0

for number in numbers:
    if number == 0:
        zero_count = zero_count + 1

print("Zero Numbers:", zero_count)


# Step 27 - Count Even and Odd Numbers

numbers = [10, -5, 20, -15, 30]


positive_sum = 0

for number in numbers:
    if number > 0:
        positive_sum = positive_sum + number

print("Sum of Positive Numbers:", positive_sum)


# Step 28 - Sum of Negative Numbers

numbers = [10, -5, 20, -15, 30]

negative_sum = 0

for number in numbers:
    if number < 0:
        negative_sum = negative_sum + number

print("Sum of Negative Numbers:", negative_sum)


# Step 29 - Count Even Numbers

numbers = [10, 15, 20, 25, 30]

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1

print("Even Numbers:", even_count)

# Step 30 - Count Odd Numbers

numbers = [10, 15, 20, 25, 30]

odd_count = 0

for number in numbers:
    if number % 2 != 0:
        odd_count = odd_count + 1

print("Odd Numbers:", odd_count)