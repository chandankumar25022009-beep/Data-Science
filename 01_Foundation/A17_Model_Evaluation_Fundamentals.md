# A17 — Model Evaluation Questions

## Interview Questions

### Q1. What is Model Evaluation?
Model Evaluation is the process of measuring how well a Machine Learning model performs on data.

### Q2. Why is Model Evaluation important?
It helps us measure model performance, compare models, detect overfitting and underfitting, and select a suitable model.

### Q3. What is Training Data?
Training data is the data used to train and teach a Machine Learning model.

### Q4. What is Test Data?
Test data is unseen data used to check the final performance of a trained model.

### Q5. What is Validation Data?
Validation data is used during model development to tune parameters and compare models.

### Q6. What is Accuracy?
Accuracy is the percentage of total predictions that are correct.

Formula:
Accuracy = (TP + TN) / (TP + TN + FP + FN)

### Q7. What is Precision?
Precision tells us how many predicted positive cases were actually positive.

Formula:
Precision = TP / (TP + FP)

### Q8. What is Recall?
Recall tells us how many actual positive cases were correctly identified.

Formula:
Recall = TP / (TP + FN)

### Q9. What is F1-Score?
F1-Score is the harmonic mean of Precision and Recall.

Formula:
F1 = 2 × (Precision × Recall) / (Precision + Recall)

### Q10. What is a Confusion Matrix?
A Confusion Matrix is a table used to evaluate classification models using TP, TN, FP, and FN.

### Q11. What is TP?
TP means True Positive. The model predicts positive and the actual value is also positive.

### Q12. What is TN?
TN means True Negative. The model predicts negative and the actual value is also negative.

### Q13. What is FP?
FP means False Positive. The model predicts positive but the actual value is negative.

### Q14. What is FN?
FN means False Negative. The model predicts negative but the actual value is positive.

### Q15. What is MAE?
MAE means Mean Absolute Error. It measures the average absolute difference between actual and predicted values.

### Q16. What is MSE?
MSE means Mean Squared Error. It calculates the average squared error.

### Q17. What is RMSE?
RMSE means Root Mean Squared Error. It is the square root of MSE.

### Q18. What is R² Score?
R² Score measures how well a regression model explains the variation in the target variable.

### Q19. What is Overfitting?
Overfitting occurs when a model performs very well on training data but poorly on unseen data.

### Q20. What is Underfitting?
Underfitting occurs when a model is too simple and performs poorly on both training and test data.

### Q21. What is Generalization?
Generalization is the ability of a model to perform well on new and unseen data.

### Q22. What is Class Imbalance?
Class imbalance occurs when one class has significantly more samples than another class.

### Q23. Why can Accuracy be misleading?
Accuracy can be misleading when the dataset has imbalanced classes.

### Q24. What is Cross-Validation?
Cross-validation is a technique for evaluating a model using multiple train-validation splits.

### Q25. What is K-Fold Cross-Validation?
K-Fold Cross-Validation divides the dataset into K parts and uses each part as validation data once.

### Q26. Which metrics are commonly used for Classification?
Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

### Q27. Which metrics are commonly used for Regression?
MAE, MSE, RMSE, and R² Score.

### Q28. Which metric is generally better when False Positives are costly?
Precision.

### Q29. Which metric is generally better when False Negatives are costly?
Recall.

### Q30. Which metric balances Precision and Recall?
F1-Score.

---

# Revision Questions

### Q1.
Define Model Evaluation.

### Q2.
Why do we evaluate a Machine Learning model?

### Q3.
What is Training Data?

### Q4.
What is Validation Data?

### Q5.
What is Test Data?

### Q6.
What is Train-Test Split?

### Q7.
What is Generalization?

### Q8.
Define Overfitting.

### Q9.
Define Underfitting.

### Q10.
What is Accuracy?

### Q11.
Write the formula of Accuracy.

### Q12.
What is Precision?

### Q13.
Write the formula of Precision.

### Q14.
What is Recall?

### Q15.
Write the formula of Recall.

### Q16.
What is F1-Score?

### Q17.
Write the formula of F1-Score.

### Q18.
What is a Confusion Matrix?

### Q19.
What is True Positive?

### Q20.
What is True Negative?

### Q21.
What is False Positive?

### Q22.
What is False Negative?

### Q23.
What is MAE?

### Q24.
Write the formula of MAE.

### Q25.
What is MSE?

### Q26.
Write the formula of MSE.

### Q27.
What is RMSE?

### Q28.
Write the formula of RMSE.

### Q29.
What is R² Score?

### Q30.
What is Class Imbalance?

### Q31.
Why is accuracy sometimes misleading?

### Q32.
What is Cross-Validation?

### Q33.
What is K-Fold Cross-Validation?

### Q34.
What is the difference between Classification and Regression evaluation?

### Q35.
Which metrics are used for Classification?

### Q36.
Which metrics are used for Regression?

### Q37.
When should Precision be preferred?

### Q38.
When should Recall be preferred?

### Q39.
When should F1-Score be used?

### Q40.
Why should a model be tested on unseen data?

---

# Practical Questions

### Q41.
Calculate Accuracy when:

TP = 80
TN = 90
FP = 10
FN = 20

### Q42.
Calculate Precision when:

TP = 80
FP = 10

### Q43.
Calculate Recall when:

TP = 80
FN = 20

### Q44.
Calculate MAE for:

Actual = [10, 20, 30]
Predicted = [12, 18, 33]

### Q45.
Calculate MSE for:

Actual = [10, 20, 30]
Predicted = [12, 18, 33]

### Q46.
Write Python code to calculate Accuracy using Scikit-learn.

### Q47.
Write Python code to calculate Precision, Recall, and F1-Score.

### Q48.
Write Python code to create a Confusion Matrix.

### Q49.
Write Python code to calculate MAE, MSE, and R² Score.

### Q50.
Explain how you would evaluate a Machine Learning classification model.

---

# Quick Revision

```text
Model Evaluation
        ↓
Measure Model Performance
        ↓
Classification / Regression