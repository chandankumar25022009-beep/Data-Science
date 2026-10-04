# A13 — Linear Algebra Fundamentals

## 1. What is Linear Algebra?

Linear Algebra is a branch of mathematics that deals with vectors, matrices, linear equations, and transformations.

### Easy Definition

Linear Algebra = Mathematics of vectors, matrices, and linear relationships.

### Why is it Important?

Linear Algebra is an important mathematical foundation for:

- Data Science
- Machine Learning
- Deep Learning
- Computer Vision
- Natural Language Processing
- Artificial Intelligence

---

## 2. Why is Linear Algebra Important in Data Science?

Data Scientists use Linear Algebra to represent and process data mathematically.

It helps us:

1. Represent data
2. Store data in matrices
3. Perform mathematical operations
4. Work with machine learning algorithms
5. Represent features and observations
6. Perform transformations
7. Understand neural networks

### Key Point

Data → Mathematical Representation → Linear Algebra → Machine Learning

---

## 3. Scalar

A Scalar is a single numerical value.

### Examples

5

10

-3

2.5

### Easy Definition

Scalar = A single number.

### Example

Temperature = 30°C

Here, 30 is a scalar value.

---

## 4. Vector

A Vector is an ordered collection of numbers.

### Example

V = [10, 20, 30]

This vector contains three values.

### Real-Life Example

Suppose a student's features are:

Age = 17

Marks = 85

Attendance = 90

They can be represented as:

V = [17, 85, 90]

### Easy Definition

Vector = An ordered list of numbers.

---

## 5. Vector Components

The individual values inside a vector are called components or elements.

### Example

V = [10, 20, 30]

Components are:

10

20

30

The vector has 3 components.

---

## 6. Dimension of a Vector

The number of components in a vector is called its dimension.

### Example

V = [10, 20, 30]

Dimension = 3

Therefore, V is a 3-dimensional vector.

### Easy Definition

Vector Dimension = Number of components in the vector.

---

## 7. Row Vector

A Row Vector is written horizontally.

### Example

V = [10 20 30]

It has 1 row and 3 columns.

### Shape

1 × 3

---

## 8. Column Vector

A Column Vector is written vertically.

### Example

V =

[10]
[20]
[30]

It has 3 rows and 1 column.

### Shape

3 × 1

---

## 9. Matrix

A Matrix is a rectangular arrangement of numbers in rows and columns.

### Example

A =

[1  2  3]
[4  5  6]

This matrix has:

2 rows

3 columns

Therefore, its shape is:

2 × 3

### Easy Definition

Matrix = Numbers arranged in rows and columns.

---

## 10. Rows and Columns

Consider:

A =

[1  2  3]
[4  5  6]

Rows:

Row 1 → 1 2 3

Row 2 → 4 5 6

Columns:

Column 1 → 1 4

Column 2 → 2 5

Column 3 → 3 6

---

## 11. Matrix Dimensions

The dimensions of a matrix are written as:

Number of Rows × Number of Columns

### Example

A =

[1 2]
[3 4]
[5 6]

Rows = 3

Columns = 2

Shape = 3 × 2

---

## 12. Types of Matrices

Important types of matrices include:

1. Row Matrix
2. Column Matrix
3. Square Matrix
4. Zero Matrix
5. Identity Matrix
6. Diagonal Matrix

---

## 13. Square Matrix

A Square Matrix has the same number of rows and columns.

### Example

A =

[1 2]
[3 4]

Rows = 2

Columns = 2

Therefore, it is a 2 × 2 square matrix.

### Easy Definition

Square Matrix = Matrix with equal rows and columns.

---

## 14. Zero Matrix

A Zero Matrix contains only zeros.

### Example

A =

[0 0]
[0 0]

### Easy Definition

Zero Matrix = Matrix in which every element is zero.

---

## 15. Identity Matrix

An Identity Matrix is a square matrix with:

1 on the main diagonal

0 everywhere else

### Example

I =

[1 0]
[0 1]

For a 3 × 3 matrix:

I =

[1 0 0]
[0 1 0]
[0 0 1]

### Easy Definition

Identity Matrix = Square matrix with 1s on the main diagonal and 0s elsewhere.

---

## 16. Diagonal Matrix

A Diagonal Matrix is a square matrix in which all non-diagonal elements are zero.

### Example

A =

[2 0 0]
[0 5 0]
[0 0 8]

### Easy Definition

Diagonal Matrix = Only diagonal elements may be non-zero.

---

## 17. Matrix Addition

Two matrices can be added when they have the same dimensions.

### Example

A =

[1 2]
[3 4]

B =

[5 6]
[7 8]

A + B =

[6  8]
[10 12]

We add corresponding elements.

---

## 18. Matrix Subtraction

Two matrices with the same dimensions can be subtracted.

### Example

A =

[5 6]
[7 8]

B =

[1 2]
[3 4]

A - B =

[4 4]
[4 4]

---

## 19. Scalar Multiplication

Scalar multiplication means multiplying every element of a matrix or vector by a single number.

### Example

A =

[1 2]
[3 4]

2A =

[2 4]
[6 8]

Every element is multiplied by 2.

---

## 20. Matrix Multiplication

Matrix multiplication is possible when:

Number of columns in the first matrix
=
Number of rows in the second matrix.

### Example

A is 2 × 3

B is 3 × 2

Then:

A × B

is possible.

The resulting matrix will be:

2 × 2

### Important Rule

(m × n) × (n × p) = (m × p)

---

## 21. Dot Product

The Dot Product is an operation between two vectors of the same dimension.

### Example

A = [1, 2, 3]

B = [4, 5, 6]

Dot Product:

A · B

= (1×4) + (2×5) + (3×6)

= 4 + 10 + 18

= 32

### Easy Definition

Dot Product = Multiply corresponding components and add the results.

---

## 22. Transpose of a Matrix

The Transpose of a matrix is obtained by converting rows into columns and columns into rows.

It is represented by:

Aᵀ

### Example

A =

[1 2 3]
[4 5 6]

Then:

Aᵀ =

[1 4]
[2 5]
[3 6]

### Easy Definition

Transpose = Rows become columns and columns become rows.

---

## 23. Determinant

The Determinant is a numerical value calculated from a square matrix.

It is represented as:

det(A)

or

|A|

### For a 2 × 2 Matrix

A =

[a b]
[c d]

Determinant:

det(A) = ad - bc

### Example

A =

[2 3]
[1 4]

det(A)

= (2×4) - (3×1)

= 8 - 3

= 5

---

## 24. Inverse of a Matrix

The Inverse of a matrix A is written as:

A⁻¹

For an invertible matrix:

A × A⁻¹ = I

where I is the identity matrix.

### Important Condition

A square matrix has an inverse only when its determinant is non-zero.

### Easy Definition

Inverse Matrix = A matrix that produces the identity matrix when multiplied by the original matrix.

---

## 25. Linear Equation

A Linear Equation is an equation where variables have power 1.

### Example

2x + 3 = 7

This is a linear equation.

Another example:

2x + y = 10

This can be represented using matrices.

---

## 26. Systems of Linear Equations

Multiple linear equations can be represented using matrices.

### Example

2x + y = 5

x + 3y = 6

These can be written as:

AX = B

Where:

A = Coefficient Matrix

X = Variable Vector

B = Constant Vector

---

## 27. Matrix Representation

For:

2x + y = 5

x + 3y = 6

We can write:

A =

[2 1]
[1 3]

X =

[x]
[y]

B =

[5]
[6]

Therefore:

AX = B

---

## 28. Norm of a Vector

The Norm of a vector represents its length or magnitude.

For:

V = [x, y]

Euclidean norm:

||V|| = √(x² + y²)

### Example

V = [3, 4]

||V||

= √(3² + 4²)

= √25

= 5

### Easy Definition

Vector Norm = Length or magnitude of a vector.

---

## 29. Orthogonal Vectors

Two vectors are orthogonal if their dot product is zero.

### Example

A = [1, 0]

B = [0, 1]

A · B

= (1×0) + (0×1)

= 0

Therefore, they are orthogonal.

### Easy Definition

Orthogonal Vectors = Vectors whose dot product is zero.

---

## 30. Linear Independence

Vectors are linearly independent if no vector can be represented as a linear combination of the others.

### Simple Explanation

If each vector provides new information, the vectors are linearly independent.

### Example

[1, 0]

[0, 1]

These two vectors are linearly independent.

---

## 31. Linear Dependence

Vectors are linearly dependent if at least one vector can be represented using the others.

### Example

A = [1, 2]

B = [2, 4]

Here:

B = 2A

Therefore, A and B are linearly dependent.

---

## 32. Rank of a Matrix

The Rank of a Matrix represents the number of linearly independent rows or columns.

### Easy Definition

Rank = Number of independent rows or columns.

Rank is important in:

- Linear algebra
- Data Science
- Machine Learning
- Dimensionality reduction

---

## 33. Eigenvalues

An Eigenvalue is a scalar associated with a square matrix that describes how a corresponding eigenvector is scaled by the matrix transformation.

### Basic Equation

A v = λv

Where:

A = Matrix

v = Eigenvector

λ = Eigenvalue

### Easy Explanation

An eigenvalue tells us how much an eigenvector is scaled during a particular matrix transformation.

---

## 34. Eigenvectors

An Eigenvector is a non-zero vector whose direction remains unchanged under a specific matrix transformation, although its magnitude may change.

### Equation

A v = λv

### Easy Definition

Eigenvector = A vector whose direction remains unchanged by a matrix transformation.

---

## 35. Linear Algebra in Machine Learning

Linear Algebra is used extensively in Machine Learning.

Examples:

- Representing datasets
- Feature vectors
- Matrix multiplication
- Linear Regression
- Neural Networks
- Principal Component Analysis
- Computer Vision
- Recommendation Systems

### Example

A dataset can be represented as a matrix:

Rows → Observations

Columns → Features

For example:

| Age | Marks | Attendance |
|---:|---:|---:|
| 17 | 85 | 90 |
| 18 | 78 | 85 |
| 19 | 92 | 95 |

This table can be represented mathematically as a matrix.

---

## 36. Linear Algebra in Neural Networks

Neural networks use vectors and matrices extensively.

A simplified operation can be written as:

Output = W × X + b

Where:

W = Weight Matrix

X = Input Vector

b = Bias Vector

This mathematical operation is repeated through neural network layers.

---

## 37. Linear Algebra Using Python

Python provides libraries for numerical and linear algebra operations.

Common libraries include:

- NumPy
- SciPy

### Example: Vector

import numpy as np

v = np.array([1, 2, 3])

print(v)

### Example: Matrix

A = np.array([
    [1, 2],
    [3, 4]
])

print(A)

---

## 38. Vector Addition Using NumPy

import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

C = A + B

print(C)

Output:

[5 7 9]

---

## 39. Dot Product Using NumPy

import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

result = np.dot(A, B)

print(result)

Output:

32

---

## 40. Matrix Multiplication Using NumPy

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

result = A @ B

print(result)

---

## 41. Matrix Transpose Using NumPy

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.T)

---

## 42. Determinant Using NumPy

import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

det = np.linalg.det(A)

print(det)

---

## 43. Matrix Inverse Using NumPy

import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

inverse = np.linalg.inv(A)

print(inverse)

The matrix must be square and invertible.

---

## 44. Real-Life Applications

Linear Algebra is used in:

- Machine Learning
- Deep Learning
- Computer Vision
- Image Processing
- Natural Language Processing
- Recommendation Systems
- Robotics
- 3D Graphics
- Scientific Computing
- Data Analysis

### Example

A digital image can be represented as numerical matrices.

Machine learning algorithms can then process these numerical representations.

---

# Interview Questions

## Q1. What is Linear Algebra?

Answer: Linear Algebra is a branch of mathematics that deals with vectors, matrices, linear equations, and transformations.

## Q2. What is a Scalar?

Answer: A Scalar is a single numerical value.

## Q3. What is a Vector?

Answer: A Vector is an ordered collection of numbers.

## Q4. What is a Matrix?

Answer: A Matrix is a rectangular arrangement of numbers in rows and columns.

## Q5. What is the difference between a Vector and a Matrix?

Answer: A Vector is an ordered list of values, while a Matrix is an arrangement of values in rows and columns.

## Q6. What is a Square Matrix?

Answer: A Square Matrix has the same number of rows and columns.

## Q7. What is an Identity Matrix?

Answer: An Identity Matrix is a square matrix with 1s on the main diagonal and 0s elsewhere.

## Q8. What is Matrix Addition?

Answer: Matrix Addition adds corresponding elements of matrices having the same dimensions.

## Q9. When is Matrix Multiplication possible?

Answer: Matrix multiplication is possible when the number of columns of the first matrix equals the number of rows of the second matrix.

## Q10. What is a Dot Product?

Answer: Dot Product multiplies corresponding vector components and adds the results.

## Q11. What is Matrix Transpose?

Answer: Transpose converts rows into columns and columns into rows.

## Q12. What is a Determinant?

Answer: A Determinant is a numerical value calculated from a square matrix.

## Q13. When does a matrix have an inverse?

Answer: A square matrix has an inverse when its determinant is non-zero.

## Q14. What is Vector Norm?

Answer: Vector Norm represents the length or magnitude of a vector.

## Q15. What are Orthogonal Vectors?

Answer: Orthogonal vectors have a dot product equal to zero.

## Q16. What is Linear Independence?

Answer: Vectors are linearly independent when none of them can be represented as a linear combination of the others.

## Q17. What is Matrix Rank?

Answer: Matrix Rank is the number of linearly independent rows or columns.

## Q18. What is an Eigenvalue?

Answer: An Eigenvalue is a scalar that describes how an eigenvector is scaled by a matrix transformation.

## Q19. What is an Eigenvector?

Answer: An Eigenvector is a non-zero vector whose direction remains unchanged under a particular matrix transformation.

## Q20. Why is Linear Algebra important in Machine Learning?

Answer: Linear Algebra is used to represent data, features, matrices, model parameters, and mathematical operations in Machine Learning.

---

# Revision Questions

1. What is Linear Algebra?
2. Why is Linear Algebra important in Data Science?
3. What is a Scalar?
4. What is a Vector?
5. What are Vector Components?
6. What is the Dimension of a Vector?
7. What is a Row Vector?
8. What is a Column Vector?
9. What is a Matrix?
10. What are Rows and Columns?
11. What is Matrix Shape?
12. What is a Square Matrix?
13. What is a Zero Matrix?
14. What is an Identity Matrix?
15. What is a Diagonal Matrix?
16. What is Matrix Addition?
17. What is Matrix Subtraction?
18. What is Scalar Multiplication?
19. What is Matrix Multiplication?
20. When is Matrix Multiplication possible?
21. What is a Dot Product?
22. What is Matrix Transpose?
23. What is a Determinant?
24. What is a Matrix Inverse?
25. When does a matrix have an inverse?
26. What is a Linear Equation?
27. How can linear equations be represented using matrices?
28. What is a Vector Norm?
29. What are Orthogonal Vectors?
30. What is Linear Independence?
31. What is Linear Dependence?
32. What is Matrix Rank?
33. What are Eigenvalues?
34. What are Eigenvectors?
35. What is the role of Linear Algebra in Machine Learning?
36. How is Linear Algebra used in Neural Networks?
37. How can an image be represented using matrices?
38. Name two Python libraries used for Linear Algebra.
39. What is NumPy?
40. Give three real-life applications of Linear Algebra.

---

# Practical Questions

## Q41. What is the dimension of the vector [10, 20, 30]?

## Q42. Find the shape of this matrix:

[1 2 3]
[4 5 6]

## Q43. Add the matrices:

A = [1 2]
    [3 4]

B = [5 6]
    [7 8]

## Q44. Calculate the dot product:

A = [1, 2, 3]

B = [4, 5, 6]

## Q45. Find the transpose of:

A = [1 2 3]
    [4 5 6]

## Q46. Find the determinant:

A = [2 3]
    [1 4]

## Q47. Find the norm of:

V = [3, 4]

## Q48. Are these vectors orthogonal?

A = [1, 0]

B = [0, 1]

## Q49. Check whether these vectors are linearly dependent:

A = [1, 2]

B = [2, 4]

## Q50. Write a Python program using NumPy to calculate the dot product of two vectors.

## Q51. Write a Python program using NumPy to find the transpose of a matrix.

## Q52. Write a Python program using NumPy to calculate the determinant of a matrix.

## Q53. Write a Python program using NumPy to calculate the inverse of a matrix.

## Q54. Why are matrices useful for representing datasets?

## Q55. Give three applications of Linear Algebra in Machine Learning.


# Remember

Scalar → Single number

Vector → Ordered collection of numbers

Matrix → Numbers arranged in rows and columns

Dimension → Number of vector components

Shape → Rows × Columns

Square Matrix → Equal rows and columns

Identity Matrix → 1s on diagonal, 0s elsewhere

Dot Product → Multiply corresponding values and add

Transpose → Rows become columns

Determinant → Numerical value of a square matrix

Inverse → Matrix that produces Identity Matrix when multiplied

Norm → Length or magnitude of a vector

Orthogonal → Dot product is zero

Rank → Number of independent rows or columns

Eigenvalue → Scaling factor

Eigenvector → Direction-preserving vector

---

# Key Point

Linear Algebra provides the mathematical language used to represent and process data in many areas of Data Science and Machine Learning.

Data
   ↓
Vectors
   ↓
Matrices
   ↓
Linear Algebra
   ↓
Mathematical Operations
   ↓
Machine Learning
   ↓
Prediction