# A15 — Machine Learning Fundamentals

## 1. What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence that allows computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every task.

### Easy Definition

Machine Learning = Learning from Data.

### Example

If we give a computer many examples of houses with their prices, the computer can learn the relationship between house features and prices and predict the price of a new house.

### Simple Flow

Data
↓
Learning
↓
Pattern
↓
Prediction


## 2. Why is Machine Learning Important?

Machine Learning is important because it can:

- Make predictions
- Find patterns
- Classify data
- Automate decisions
- Detect anomalies
- Recommend products
- Recognize images
- Understand text
- Support business decisions

### Key Point

Machine Learning helps computers learn from data and improve predictions.


## 3. Artificial Intelligence vs Machine Learning vs Deep Learning

### Artificial Intelligence (AI)

AI is the broader field of creating systems that can perform tasks requiring human-like intelligence.

### Machine Learning (ML)

ML is a subset of AI that learns patterns from data.

### Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses multi-layer neural networks.

### Relationship

Artificial Intelligence
↓
Machine Learning
↓
Deep Learning


## 4. Traditional Programming vs Machine Learning

### Traditional Programming

Input + Rules
↓
Program
↓
Output

### Machine Learning

Data + Expected Results
↓
Learning Algorithm
↓
Model

The trained model can then make predictions on new data.


## 5. What is Data in Machine Learning?

Data is the information used by a Machine Learning system to learn patterns.

Examples:

- Student marks
- House prices
- Customer information
- Sales records
- Images
- Text
- Sensor readings

### Key Point

Data is the foundation of Machine Learning.


## 6. Dataset

A dataset is a collection of related data used for analysis or Machine Learning.

Example:

| Hours Studied | Attendance | Marks |
|---:|---:|---:|
| 2 | 70 | 45 |
| 4 | 80 | 60 |
| 6 | 90 | 75 |
| 8 | 95 | 90 |

Here:

- Each row = Observation / Record
- Each column = Feature or Target


## 7. Features

Features are input variables used by a Machine Learning model to make predictions.

Example:

To predict house price:

- Area
- Number of rooms
- Location
- Age of house

These can be features.

### Easy Definition

Feature = Input information used by a model.


## 8. Target / Label

The target is the value that the model tries to predict.

Example:

If we want to predict house price:

Features:
- Area
- Rooms
- Location

Target:
- Price

### Easy Definition

Target = Output the model tries to predict.


## 9. Feature vs Target

| Feature | Target |
|---|---|
| Input variable | Output variable |
| Used for prediction | Predicted by model |
| X | y |

Example:

X = Hours Studied

y = Exam Marks


## 10. What is a Machine Learning Model?

A model is a mathematical or computational representation that learns patterns from data.

### Simple Flow

Input Data
↓
Machine Learning Algorithm
↓
Trained Model
↓
Prediction


## 11. What is an Algorithm?

An algorithm is a step-by-step method used to solve a problem or learn patterns from data.

Examples:

- Linear Regression
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors
- K-Means
- Random Forest


## 12. Algorithm vs Model

### Algorithm

The learning method.

### Model

The result produced after the algorithm learns from data.

### Easy Example

Algorithm = Learning method

Model = Learned result


## 13. Types of Machine Learning

The major types are:

1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

### Simple Flow

Machine Learning
       ↓
 ┌─────┼─────────────┐
 ↓     ↓             ↓
Supervised  Unsupervised  Reinforcement


## 14. Supervised Learning

Supervised Learning uses labeled data.

The model learns from:

Input → Known Output

Example:

Hours Studied → Marks

The training data contains the correct answer.

### Easy Definition

Supervised Learning = Learning with labeled data.


## 15. Regression

Regression is a supervised learning problem where the target is usually a continuous numerical value.

Examples:

- House price prediction
- Temperature prediction
- Sales prediction
- Salary prediction

Example:

Hours Studied → Exam Marks

Predicted Marks = 82.5


## 16. Classification

Classification is a supervised learning problem where the target represents a category or class.

Examples:

- Spam / Not Spam
- Pass / Fail
- Cat / Dog
- Fraud / Not Fraud

Example:

Email
↓
Classification Model
↓
Spam / Not Spam


## 17. Regression vs Classification

| Regression | Classification |
|---|---|
| Predicts numerical values | Predicts categories/classes |
| House price | Spam detection |
| Temperature | Pass/Fail |
| Salary | Cat/Dog |

### Remember

Regression → Number

Classification → Category


## 18. Unsupervised Learning

Unsupervised Learning uses data without labeled target values.

The model tries to find hidden patterns or structures in the data.

Examples:

- Customer segmentation
- Grouping similar documents
- Finding similar products

### Easy Definition

Unsupervised Learning = Learning without labeled answers.


## 19. Clustering

Clustering is an unsupervised learning technique that groups similar data points together.

### Example

Customers
↓
Clustering
↓
Group 1
Group 2
Group 3

### Application

A company can group customers according to purchasing behavior.


## 20. Reinforcement Learning

Reinforcement Learning is a type of Machine Learning in which an agent learns by interacting with an environment.

The agent receives:

- Rewards
- Penalties

The goal is to learn actions that maximize long-term reward.

### Example

Game
↓
Action
↓
Reward / Penalty
↓
Learning


## 21. Training Data

Training data is the data used to teach a Machine Learning model.

Example:

A dataset may be divided into training, validation, and test sets.

The exact split depends on the problem and methodology.


## 22. Validation Data

Validation data is used during model development to help select or tune the model.

It can help with:

- Hyperparameter tuning
- Model selection
- Comparing different approaches

### Easy Definition

Validation Data = Data used to improve/select the model during development.


## 23. Test Data

Test data is used to evaluate the final model on data that was not used for training.

### Easy Definition

Test Data = Unseen data used for final evaluation.


## 24. Train, Validation and Test Split

A common workflow is:

Dataset
↓
Training Data
↓
Validation Data
↓
Test Data

Example:

70% → Training
15% → Validation
15% → Testing

These percentages are examples, not fixed rules.


## 25. Model Training

Model training is the process in which a Machine Learning algorithm learns patterns from training data.

### Process

Training Data
↓
Algorithm
↓
Learn Patterns
↓
Model


## 26. Prediction

After training, the model can make predictions on new data.

Example:

New Student Data
↓
Trained Model
↓
Predicted Marks


## 27. Parameters

Parameters are values learned by a Machine Learning model during training.

Example:

In a simple linear model:

y = wx + b

Here:

w = Weight / Parameter

b = Bias / Parameter


## 28. Hyperparameters

Hyperparameters are settings chosen before or during model training rather than learned directly from the training data.

Examples:

- Learning rate
- Number of trees
- Maximum tree depth
- Number of neighbors

### Key Difference

Parameters → Learned from data

Hyperparameters → Set by the practitioner or algorithm configuration


## 29. Linear Regression

Linear Regression is a supervised learning algorithm used mainly for predicting continuous numerical values.

Basic equation:

y = mx + b

Where:

y = Predicted value

x = Input feature

m = Slope

b = Intercept


## 30. Example of Linear Regression

Suppose:

x = Hours Studied

y = Marks

A model may learn a relationship such as:

Marks = 5 × Hours + 40

If:

Hours = 6

Then:

Marks = 5 × 6 + 40
      = 70

This is a simple mathematical example.


## 31. Logistic Regression

Despite its name, Logistic Regression is commonly used for classification.

It predicts probabilities that can be converted into class predictions.

Example:

Email
↓
Logistic Regression
↓
Probability of Spam
↓
Spam / Not Spam


## 32. Decision Tree

A Decision Tree makes predictions using a tree-like structure of questions or conditions.

Example:

Is age > 18?
    ↓
  Yes / No
    ↓
Decision


## 33. K-Nearest Neighbors

K-Nearest Neighbors (KNN) makes predictions using nearby data points.

### Basic Idea

New Data Point
↓
Find Nearby Points
↓
Look at Their Labels
↓
Make Prediction


## 34. Random Forest

Random Forest is an ensemble learning method that combines multiple decision trees.

### Basic Idea

Tree 1
Tree 2
Tree 3
Tree 4
↓
Combined Result
↓
Prediction

It is commonly used for classification and regression.


## 35. K-Means Clustering

K-Means is an unsupervised clustering algorithm.

### Basic Process

1. Choose the number of clusters.
2. Initialize cluster centers.
3. Assign points to the nearest center.
4. Update the centers.
5. Repeat until the process stabilizes.


## 36. Overfitting

Overfitting occurs when a model learns the training data too closely, including patterns that do not generalize well to new data.

### Signs

Training performance → Very high

Test performance → Much lower

### Easy Definition

Overfitting = Model memorizes training data too much.


## 37. Underfitting

Underfitting occurs when a model is too simple to learn the important patterns in the data.

### Signs

Training performance → Poor

Test performance → Poor

### Easy Definition

Underfitting = Model fails to learn enough from the data.


## 38. Overfitting vs Underfitting

| Overfitting | Underfitting |
|---|---|
| Model too complex for the available data | Model too simple |
| Learns training data too closely | Does not learn enough |
| Poor generalization | Poor performance overall |

### Remember

Overfitting → Too much learning

Underfitting → Too little learning


## 39. Generalization

Generalization means the ability of a model to perform well on new, unseen data.

### Key Point

Good Machine Learning models should generalize well.


## 40. Loss Function

A loss function measures how far the model's prediction is from the desired output.

Example:

Actual = 10

Predicted = 8

The loss function calculates a numerical measure of error.


## 41. Cost Function

A cost function generally represents the overall error across a collection of training examples.

In many contexts, the terms loss and cost are used differently depending on the formulation.

### Simple Idea

Loss → Error for an individual example

Cost → Overall or aggregated error


## 42. Optimization

Optimization is the process of finding model parameters that improve the objective, often by minimizing a loss or cost function.

Example:

Loss
↓
Optimization
↓
Lower Loss


## 43. Gradient Descent

Gradient Descent is an optimization algorithm commonly used to minimize a loss function.

### Basic Update

New Parameter =
Old Parameter - Learning Rate × Gradient

### Process

Initialize Parameters
↓
Make Prediction
↓
Calculate Loss
↓
Calculate Gradient
↓
Update Parameters
↓
Repeat


## 44. Learning Rate

Learning rate controls the size of parameter updates during optimization.

### Small Learning Rate

- Smaller steps
- Training may be slower

### Large Learning Rate

- Larger steps
- May overshoot useful solutions


## 45. Model Evaluation

Model evaluation means measuring how well a trained model performs.

Different tasks use different metrics.

### Regression Metrics

- MAE
- MSE
- RMSE
- R²

### Classification Metrics

- Accuracy
- Precision
- Recall
- F1-score


## 46. Accuracy

Accuracy is the proportion of correct predictions among all predictions.

### Formula

Accuracy =
Correct Predictions / Total Predictions


## 47. Precision

Precision measures how many predicted positive cases were actually positive.

### Formula

Precision =
True Positives / (True Positives + False Positives)


## 48. Recall

Recall measures how many actual positive cases were correctly identified.

### Formula

Recall =
True Positives / (True Positives + False Negatives)


## 49. F1-Score

F1-score combines Precision and Recall using their harmonic mean.

### Formula

F1 =
2 × Precision × Recall
----------------------
Precision + Recall


## 50. Confusion Matrix

A confusion matrix summarizes classification predictions.

It contains:

- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)


## 51. Machine Learning Workflow

A basic Machine Learning workflow is:

Problem Definition
↓
Data Collection
↓
Data Cleaning
↓
Data Exploration
↓
Feature Engineering
↓
Train / Validation / Test Split
↓
Model Selection
↓
Model Training
↓
Model Evaluation
↓
Model Improvement
↓
Deployment


## 52. Machine Learning with Python

Python is widely used for Machine Learning because it has many useful libraries.

Important libraries include:

- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- SciPy

For Deep Learning, commonly used frameworks include:

- PyTorch
- TensorFlow


## 53. Scikit-learn

Scikit-learn is a popular Python library for Machine Learning.

It provides tools for:

- Data preprocessing
- Classification
- Regression
- Clustering
- Model selection
- Model evaluation


## 54. Python Practical — Simple Prediction

```python
hours = 6

marks = 5 * hours + 40

print(marks)