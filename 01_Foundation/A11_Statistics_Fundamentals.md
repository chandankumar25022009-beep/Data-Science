# A11 — Statistics Fundamentals

## 1. What is Statistics?

Statistics is the branch of mathematics that deals with collecting, organizing, analyzing, interpreting, and presenting data.

### Easy Definition

Statistics = The study of data to understand information and make decisions.

### Example

Suppose a college has marks of 500 students.

Statistics can help us find:

- Average marks
- Highest marks
- Lowest marks
- Middle value
- Variation in marks
- Distribution of marks

---

## 2. Why is Statistics Important in Data Science?

Statistics is important because it helps Data Scientists:

1. Understand data
2. Summarize data
3. Find patterns
4. Measure variation
5. Identify relationships
6. Make predictions
7. Test assumptions
8. Make data-driven decisions

### Key Point

Data + Statistics → Better Understanding → Better Decisions

---

## 3. Population

Population means the complete group of people, objects, or observations that we are interested in studying.

### Example

Suppose we want to study the marks of all students in a college.

All students in that college are the population.

### Easy Definition

Population = The complete group being studied.

---

## 4. Sample

A Sample is a smaller group selected from the population for study.

### Example

A college has 5,000 students.

If we select 500 students for a study, those 500 students are the sample.

### Easy Definition

Sample = A smaller part of the population.

---

## 5. Population vs Sample

| Population | Sample |
|---|---|
| Complete group | Part of the group |
| Usually larger | Usually smaller |
| Example: All college students | Example: 500 selected students |

### Remember

Population → Whole group

Sample → Part of the group

---

## 6. Variable

A Variable is a characteristic or value that can change between observations.

### Examples

- Age
- Height
- Marks
- Salary
- Temperature
- Attendance

### Example

Students may have different ages:

17, 18, 19, 20

Age is a variable.

### Easy Definition

Variable = A characteristic that can have different values.

---

## 7. Mean

Mean is the average value of a dataset.

### Formula

Mean = Sum of all values / Number of values

### Example

Values:

10, 20, 30, 40, 50

Mean:

(10 + 20 + 30 + 40 + 50) / 5

= 150 / 5

= 30

### Easy Definition

Mean = Average value.

---

## 8. Median

Median is the middle value when data is arranged in ascending or descending order.

### Example

Values:

10, 20, 30, 40, 50

Median = 30

### Even Number of Values

Values:

10, 20, 30, 40

The two middle values are 20 and 30.

Median:

(20 + 30) / 2 = 25

### Easy Definition

Median = Middle value of ordered data.

---

## 9. Mode

Mode is the value that appears most frequently in a dataset.

### Example

Values:

10, 20, 20, 30, 40

Mode = 20

Because 20 appears two times.

### Easy Definition

Mode = Most frequently occurring value.

---

## 10. Mean vs Median vs Mode

| Measure | Meaning |
|---|---|
| Mean | Average value |
| Median | Middle value |
| Mode | Most frequent value |

### Remember

Mean → Average

Median → Middle

Mode → Most Frequent

---

## 11. Range

Range is the difference between the maximum and minimum values.

### Formula

Range = Maximum - Minimum

### Example

Values:

20, 30, 40, 50, 60

Maximum = 60

Minimum = 20

Range = 60 - 20

Range = 40

### Easy Definition

Range = Difference between maximum and minimum.

---

## 12. Variance

Variance measures how much the values in a dataset differ from the mean.

A higher variance generally means the values are more spread out.

A lower variance generally means the values are closer to the mean.

### Easy Definition

Variance = A measure of how spread out data is around the mean.

---

## 13. Standard Deviation

Standard Deviation measures the amount of variation or spread in a dataset.

### Example

Dataset A:

48, 49, 50, 51, 52

The values are close to the mean, so the spread is small.

Dataset B:

10, 30, 50, 70, 90

The values are more spread out, so the spread is larger.

### Easy Definition

Standard Deviation = A measure of how much data values vary around the mean.

---

## 14. Variance vs Standard Deviation

| Variance | Standard Deviation |
|---|---|
| Measures spread | Measures spread |
| Expressed in squared units | Expressed in original units |
| Square of standard deviation | Square root of variance |

### Formula Relationship

Standard Deviation = √Variance

---

## 15. Distribution

A Distribution describes how values are spread across a dataset.

### Example

Student marks may be distributed as:

- Many students with medium marks
- Few students with very low marks
- Few students with very high marks

Understanding distributions is important in statistics and data science.

---

## 16. Normal Distribution

A Normal Distribution is a common probability distribution with a symmetric, bell-shaped pattern.

In an ideal normal distribution:

Mean = Median = Mode

### Example

Some measurements in nature and other processes can approximately follow a normal distribution.

### Easy Definition

Normal Distribution = A symmetric, bell-shaped probability distribution.

---

## 17. Probability

Probability measures how likely an event is to happen.

### Formula

Probability = Favorable Outcomes / Total Possible Outcomes

### Example

A fair coin has two possible outcomes:

Heads
Tails

Probability of getting Heads:

1 / 2

= 0.5

= 50%

### Easy Definition

Probability = Measure of the likelihood of an event.

---

## 18. Correlation

Correlation describes the strength and direction of a relationship between two variables.

### Example

Study Hours and Marks.

If study hours generally increase while marks also increase, there may be a positive correlation.

### Types

Positive Correlation → Variables generally move in the same direction.

Negative Correlation → Variables generally move in opposite directions.

Little or No Correlation → No clear linear relationship.

### Important Point

Correlation does not automatically mean causation.

---

## 19. Positive Correlation

Positive correlation means two variables generally increase or decrease together.

### Example

Study Hours ↑

Marks ↑

This may indicate a positive relationship.

---

## 20. Negative Correlation

Negative correlation means one variable generally increases while the other decreases.

### Example

As the price of a product increases, demand may decrease.

This may indicate a negative relationship.

---

## 21. No or Weak Correlation

If two variables do not show a clear linear relationship, they may have little or no linear correlation.

### Example

Shoe size and exam marks may have little meaningful relationship in a particular dataset.

---

## 22. Statistical Summary

A statistical summary gives important information about a dataset.

It may include:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median
- 75th percentile
- Maximum

### Example

In Python, Pandas can provide a statistical summary using:

data.describe()

We will practice this later.

---

## 23. Percentile

A Percentile tells us the value below which a certain percentage of observations fall.

### Example

If a student's score is at the 90th percentile, the student scored higher than or equal to approximately 90% of the observations in the reference dataset.

### Easy Definition

Percentile = A position of a value relative to the rest of the data.

---

## 24. Quartiles

Quartiles divide ordered data into four parts.

The important quartiles are:

Q1 → 25th percentile

Q2 → 50th percentile (Median)

Q3 → 75th percentile

### Easy Definition

Quartiles = Values that divide ordered data into four parts.

---

## 25. Interquartile Range (IQR)

IQR measures the spread of the middle 50% of the data.

### Formula

IQR = Q3 - Q1

### Example

Q1 = 20

Q3 = 60

IQR = 60 - 20

IQR = 40

### Easy Definition

IQR = Difference between the third and first quartiles.

---

## 26. Outliers and Statistics

An outlier is an observation that is unusually different from other observations.

One common statistical rule uses the IQR:

Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

Values outside these bounds may be considered potential outliers.

### Important Point

A potential outlier is not automatically an error. It should be investigated.

---

## 27. Statistics in Data Science

Statistics is used throughout Data Science.

```text
Data Collection
       ↓
Data Cleaning
       ↓
Statistics
       ↓
Data Analysis
       ↓
Data Visualization
       ↓
Machine Learning
       ↓
Prediction
       ↓
Decision