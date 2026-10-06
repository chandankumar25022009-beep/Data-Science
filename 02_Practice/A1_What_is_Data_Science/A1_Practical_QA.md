# A1 - What is Data Science
# Practical Q&A

## Practical Questions

Q1. Create a list of student marks.
Answer:
marks = [85, 72, 90, 65, 78]
print(marks)

Q2. Find the total of student marks.
Answer:
marks = [85, 72, 90, 65, 78]
total = sum(marks)
print("Total:", total)

Q3. Find the average of student marks.
Answer:
marks = [85, 72, 90, 65, 78]
average = sum(marks) / len(marks)
print("Average:", average)

Q4. Find the highest mark.
Answer:
marks = [85, 72, 90, 65, 78]
highest = max(marks)
print("Highest:", highest)

Q5. Find the lowest mark.
Answer:
marks = [85, 72, 90, 65, 78]
lowest = min(marks)
print("Lowest:", lowest)

Q6. Count the number of students.
Answer:
marks = [85, 72, 90, 65, 78]
count = len(marks)
print("Number of Students:", count)

Q7. Print only marks greater than 75.
Answer:
marks = [85, 72, 90, 65, 78]

for mark in marks:
    if mark > 75:
        print(mark)

Q8. Count students who scored more than 75.
Answer:
marks = [85, 72, 90, 65, 78]

count = 0

for mark in marks:
    if mark > 75:
        count = count + 1

print("Students:", count)

Q9. Find the total of positive numbers.
Answer:
numbers = [10, -5, 20, -15, 30]

positive_sum = 0

for number in numbers:
    if number > 0:
        positive_sum = positive_sum + number

print("Positive Sum:", positive_sum)

Q10. Count positive numbers.
Answer:
numbers = [10, -5, 20, -15, 30]

count = 0

for number in numbers:
    if number > 0:
        count = count + 1

print("Positive Numbers:", count)

Q11. Count negative numbers.
Answer:
numbers = [10, -5, 20, -15, 30]

count = 0

for number in numbers:
    if number < 0:
        count = count + 1

print("Negative Numbers:", count)

Q12. Count zero values.
Answer:
numbers = [10, 0, 20, 0, -5, 0]

count = 0

for number in numbers:
    if number == 0:
        count = count + 1

print("Zero Numbers:", count)

Q13. Separate positive, negative, and zero numbers.
Answer:
numbers = [10, -5, 20, -15, 30]

for number in numbers:
    if number > 0:
        print(number, "-> Positive")
    elif number < 0:
        print(number, "-> Negative")
    else:
        print(number, "-> Zero")

Q14. Find even numbers.
Answer:
numbers = [10, 15, 20, 25, 30]

for number in numbers:
    if number % 2 == 0:
        print(number)

Q15. Find odd numbers.
Answer:
numbers = [10, 15, 20, 25, 30]

for number in numbers:
    if number % 2 != 0:
        print(number)

Q16. Count even numbers.
Answer:
numbers = [10, 15, 20, 25, 30]

count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

print("Even Numbers:", count)

Q17. Count odd numbers.
Answer:
numbers = [10, 15, 20, 25, 30]

count = 0

for number in numbers:
    if number % 2 != 0:
        count = count + 1

print("Odd Numbers:", count)

Q18. Store student names and marks.
Answer:
students = {
    "Chandan": 85,
    "Rahul": 72,
    "Amit": 90
}

print(students)

Q19. Print each student's name and marks.
Answer:
students = {
    "Chandan": 85,
    "Rahul": 72,
    "Amit": 90
}

for name, mark in students.items():
    print(name, ":", mark)

Q20. Find students who scored more than 80.
Answer:
students = {
    "Chandan": 85,
    "Rahul": 72,
    "Amit": 90
}

for name, mark in students.items():
    if mark > 80:
        print(name, ":", mark)


## Data Science Practical Concepts

Q21. What is the practical use of a dataset?
Answer: A dataset stores related information that can be analyzed to find patterns and insights.

Q22. Why do we calculate the average?
Answer: Average helps us understand the central value of numerical data.

Q23. Why do we find maximum and minimum values?
Answer: They help identify the highest and lowest values in data.

Q24. Why do we use loops in data processing?
Answer: Loops allow us to process multiple data values automatically.

Q25. Why do we use conditions?
Answer: Conditions help classify or filter data according to specific rules.

Q26. Why do we count data?
Answer: Counting helps understand the number of records or values satisfying a condition.

Q27. Why is Python useful for practical Data Science?
Answer: Python provides simple syntax and powerful libraries for data processing and analysis.

Q28. What is data filtering?
Answer: Data filtering means selecting only the records that satisfy a specific condition.

Q29. What is data classification?
Answer: Data classification means grouping data into categories based on defined rules.

Q30. What is a data insight?
Answer: A data insight is useful information discovered by analyzing data.


## Mini Practical Tasks

Task 1:
Create a list containing 5 student marks and print the list.

Task 2:
Calculate the total and average of the marks.

Task 3:
Find the highest and lowest marks.

Task 4:
Count how many students scored above 75.

Task 5:
Create a list of positive, negative, and zero numbers and classify them.

Task 6:
Find all even numbers from a list.

Task 7:
Find all odd numbers from a list.

Task 8:
Create a dictionary containing student names and marks.

Task 9:
Print students who scored more than 80.

Task 10:
Calculate the average marks of all students.


## Important Practical Functions

print()  = Display data
len()    = Count items
sum()    = Calculate total
max()    = Find highest value
min()    = Find lowest value
type()   = Check data type
input()  = Take user input
range()  = Generate number sequence


## Important Operators

+   = Addition
-   = Subtraction
*   = Multiplication
/   = Division
%   = Remainder
>   = Greater than
<   = Less than
==  = Equal to
!=  = Not equal to


## Quick Practical Revision

- List stores multiple values.
- Dictionary stores key-value pairs.
- len() counts items.
- sum() calculates total.
- max() finds highest value.
- min() finds lowest value.
- for loop processes multiple values.
- if checks conditions.
- % helps identify even and odd numbers.
- Filtering selects required data.
- Classification groups data.
- Data analysis finds useful information from data.


## One-Line Practical Revision

Python can be used to store, process, filter, classify, and analyze data.


## Key Point

Practical Data Science starts with understanding data and using programming to process that data.