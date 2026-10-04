# A16 — Supervised vs Unsupervised Learning

## 1. Introduction

Machine Learning is mainly divided into different learning approaches.

1. Supervised Learning
2. Unsupervised Learning

Supervised Learning → Learning with answers

Unsupervised Learning → Learning without answers


## 2. Supervised Learning

Supervised Learning is a Machine Learning approach where the model learns from labeled data.

Labeled data means the input data already has a known output or target.

### Simple Flow

Input Data
↓
Known Output
↓
Learning Algorithm
↓
Trained Model
↓
Prediction

### Easy Definition

Supervised Learning = Learning from labeled data.


## 3. Examples of Supervised Learning

- House price prediction
- Student marks prediction
- Salary prediction
- Spam detection
- Disease classification
- Fraud detection
- Image classification
- Customer churn prediction


## 4. Types of Supervised Learning

The two major types are:

1. Regression
2. Classification


## 5. Regression

Regression is used when the target is a continuous numerical value.

Examples:

- House price
- Temperature
- Salary
- Sales
- Student marks

Example:

Hours Studied → Marks

Predicted Marks = 82.5

Remember:

Regression → Number


## 6. Classification

Classification is used when the target belongs to a category or class.

Examples:

- Spam / Not Spam
- Pass / Fail
- Cat / Dog
- Fraud / Not Fraud
- Disease / No Disease

Example:

Email
↓
Classification Model
↓
Spam / Not Spam

Remember:

Classification → Category


## 7. Common Supervised Learning Algorithms

- Linear Regression
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors
- Random Forest
- Support Vector Machine
- Naive Bayes


## 8. Unsupervised Learning

Unsupervised Learning is a Machine Learning approach where the model learns from data without labeled target values.

The model tries to discover hidden patterns, structures, or groups.

### Simple Flow

Input Data
↓
Learning Algorithm
↓
Find Patterns
↓
Groups / Structure

### Easy Definition

Unsupervised Learning = Learning without labeled answers.


## 9. Example of Unsupervised Learning

Suppose a company has customer data:

| Age | Spending |
|---:|---:|
| 20 | 2000 |
| 22 | 2500 |
| 45 | 15000 |
| 48 | 18000 |

There is no target column.

The model may discover groups such as:

Group 1 → Younger / Lower Spending

Group 2 → Older / Higher Spending

This is clustering.


## 10. Main Types of Unsupervised Learning

1. Clustering
2. Dimensionality Reduction
3. Association Rule Learning


## 11. Clustering

Clustering groups similar data points together.

### Simple Flow

Data
↓
Clustering Algorithm
↓
Similar Groups

### Example

Customers
↓
Clustering
↓
Customer Group 1
Customer Group 2
Customer Group 3


## 12. K-Means Clustering

K-Means is a popular unsupervised learning algorithm.

### Basic Process

1. Choose the number of clusters.
2. Initialize cluster centers.
3. Assign data points to the nearest center.
4. Update the cluster centers.
5. Repeat the process.
6. Stop when the clusters become stable.


## 13. Dimensionality Reduction

Dimensionality reduction reduces the number of features while trying to preserve important information.

It can help:

- Simplify datasets
- Reduce computation
- Visualize high-dimensional data
- Remove redundant information

Example:

100 Features → Fewer useful dimensions


## 14. Association Rule Learning

Association Rule Learning finds relationships between items or events.

Example:

Laptop → Laptop Bag

A shopping system can discover that customers who buy laptops often also buy laptop bags.

Applications:

- Market basket analysis
- Product recommendation
- Shopping behavior analysis


## 15. Common Unsupervised Learning Algorithms

- K-Means
- Hierarchical Clustering
- DBSCAN
- PCA
- Apriori


## 16. Supervised vs Unsupervised Learning

| Supervised Learning | Unsupervised Learning |
|---|---|
| Uses labeled data | Uses unlabeled data |
| Target is known | Target is not given |
| Learns input-output relationship | Finds hidden patterns |
| Used for prediction | Used for pattern discovery |
| Regression and classification | Clustering and dimensionality reduction |
| House price prediction | Customer segmentation |


## 17. Simple Difference

### Supervised

Data + Answers
↓
Learning
↓
Prediction

### Unsupervised

Data
↓
Learning
↓
Pattern / Groups


## 18. Real-Life Example

### Supervised Approach

An online shopping company wants to predict whether a customer will purchase a product.

Features:

- Age
- Income
- Previous Purchases
- Website Visits

Target:

Purchase = Yes / No

This is classification.

### Unsupervised Approach

The company wants to divide customers into similar groups.

There is no target.

The algorithm finds groups automatically.

This is clustering.


## 19. When to Use Supervised Learning?

Use supervised learning when:

- You have labeled data.
- You know the target/output.
- You want to make predictions.
- You want to classify data.
- You want to estimate numerical values.


## 20. When to Use Unsupervised Learning?

Use unsupervised learning when:

- You do not have labeled data.
- You want to discover hidden patterns.
- You want to group similar data.
- You want to explore a dataset.
- You want to reduce dimensions.


## 21. Advantages of Supervised Learning

- Good for prediction
- Can measure prediction performance
- Useful for classification
- Useful for regression
- Easy to evaluate when correct labels are available


## 22. Limitations of Supervised Learning

- Requires labeled data
- Labeling can be expensive
- Poor-quality labels can affect the model
- Model performance depends on training data


## 23. Advantages of Unsupervised Learning

- Does not require labeled data
- Can discover hidden patterns
- Useful for customer segmentation
- Useful for exploratory analysis
- Can help understand complex datasets


## 24. Limitations of Unsupervised Learning

- Results can be difficult to interpret
- Choosing the number of groups may be difficult
- Evaluation can be less straightforward
- Discovered patterns may not always be meaningful


## 25. Supervised Learning Workflow

Collect Data
↓
Clean Data
↓
Prepare Features and Target
↓
Split Data
↓
Train Model
↓
Evaluate Model
↓
Make Predictions


## 26. Unsupervised Learning Workflow

Collect Data
↓
Clean Data
↓
Prepare Features
↓
Choose Algorithm
↓
Train Algorithm
↓
Find Patterns
↓
Interpret Results


## 27. Labeled vs Unlabeled Data

### Labeled Data

Data contains the correct target/output.

Example:

| Hours | Marks |
|---:|---:|
| 2 | 45 |
| 4 | 60 |
| 6 | 75 |

Marks is the label/target.

### Unlabeled Data

Data does not contain the target.

Example:

| Age | Spending |
|---:|---:|
| 20 | 2000 |
| 22 | 2500 |
| 45 | 15000 |

The algorithm must discover patterns itself.


## 28. Classification vs Clustering

### Classification

- Supervised
- Uses labeled data
- Predicts predefined classes

Example:

Email → Spam

### Clustering

- Unsupervised
- Does not require labels
- Creates groups based on similarity

Example:

Customers → Group 1, Group 2, Group 3


## 29. Regression vs Classification vs Clustering

| Regression | Classification | Clustering |
|---|---|---|
| Supervised | Supervised | Unsupervised |
| Predicts numbers | Predicts classes | Creates groups |
| House price | Spam detection | Customer segmentation |
| Salary | Pass/Fail | Similar customers |


## 30. Machine Learning Decision Guide

Do you have labeled data?

Yes
↓
Supervised Learning
↓
What do you want to predict?

Number → Regression

Category → Classification

If there is no target:

No labeled target
↓
Unsupervised Learning
↓
Find Groups / Patterns
↓
Clustering / Dimensionality Reduction


## 31. Python Example — Supervised Learning

### Linear Regression

```python
from sklearn.linear_model import LinearRegression

X = [[2], [4], [6], [8]]
y = [45, 60, 75, 90]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[7]])

print("Predicted Marks:", prediction[0])