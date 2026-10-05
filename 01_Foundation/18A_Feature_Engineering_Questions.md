# A18 — Feature Engineering Questions

## Interview Questions

### Q1. What is Feature Engineering?
Feature Engineering is the process of creating, transforming, selecting, or improving features from raw data for Machine Learning.

### Q2. What is a Feature?
A feature is an input variable used by a Machine Learning model to make predictions.

### Q3. What is a Target?
A target is the output value that a Machine Learning model tries to predict.

### Q4. Why is Feature Engineering important?
It can improve model performance, reduce noise, handle raw data, and help the model learn useful patterns.

### Q5. What is Feature Creation?
Feature Creation means creating a new feature from existing data.

### Q6. What is Feature Transformation?
Feature Transformation means changing the representation or scale of a feature.

### Q7. What is Feature Scaling?
Feature Scaling brings numerical features to a similar scale.

### Q8. What is Normalization?
Normalization commonly scales values into a fixed range such as 0 to 1.

### Q9. Write the Min-Max Normalization formula.
X_normalized = (X - X_min) / (X_max - X_min)

### Q10. What is Standardization?
Standardization transforms data so that it has approximately mean 0 and standard deviation 1.

### Q11. Write the Standardization formula.
Z = (X - Mean) / Standard Deviation

### Q12. What is Encoding?
Encoding converts categorical data into a numerical representation suitable for Machine Learning.

### Q13. What is Label Encoding?
Label Encoding assigns numerical values to categories.

Example:
Red → 0
Blue → 1
Green → 2

### Q14. What is One-Hot Encoding?
One-Hot Encoding creates separate binary columns for different categories.

### Q15. What is Feature Selection?
Feature Selection means selecting the most useful features and removing unnecessary features.

### Q16. Why is Feature Selection important?
It can reduce unnecessary data, model complexity, training time, and noise.

### Q17. What is Feature Extraction?
Feature Extraction means creating useful representations from raw data.

### Q18. What is the difference between Feature Selection and Feature Extraction?
Feature Selection selects existing features, while Feature Extraction creates new useful representations.

### Q19. What are Missing Values?
Missing Values are data values that are not available in a dataset.

### Q20. How can Missing Values be handled?
They can be handled by removing data or using methods such as mean, median, mode, or suitable imputation techniques.

### Q21. What is Mean Imputation?
Mean Imputation replaces a missing numerical value with the mean of available values.

### Q22. What is Median Imputation?
Median Imputation replaces a missing value with the median of available values.

### Q23. What is Mode Imputation?
Mode Imputation replaces a missing categorical value with the most frequently occurring value.

### Q24. What is an Outlier?
An outlier is a data point that is unusually far from other observations.

### Q25. What is Binning?
Binning converts continuous numerical values into groups or ranges.

### Q26. What is Date and Time Feature Engineering?
It means extracting useful features such as year, month, day, weekday, and quarter from date/time data.

### Q27. What is Text Feature Engineering?
It means converting text into useful numerical features such as word count, character count, or TF-IDF values.

### Q28. What is Log Transformation?
Log Transformation changes numerical values using a logarithmic function and can help with highly skewed data.

### Q29. What is Skewed Data?
Skewed data is data that is not symmetrically distributed.

### Q30. What is Data Leakage?
Data Leakage occurs when information that should not be available during prediction enters the model training process.

### Q31. Why is Data Leakage dangerous?
It can make model performance appear unrealistically high and cause poor performance on real-world data.

### Q32. What is a Feature Engineering Pipeline?
It is a sequence of steps used to transform raw data into useful features before Machine Learning.

### Q33. Which Python libraries are commonly used for Feature Engineering?
Pandas, NumPy, and Scikit-learn are commonly used.

### Q34. What is the difference between Normalization and Standardization?
Normalization commonly scales values to a range such as 0–1, while Standardization centers data around mean 0 with standard deviation 1.

### Q35. Why should categorical data be encoded?
Because many Machine Learning algorithms require numerical input.

### Q36. What is BMI Feature Engineering?
BMI can be created from weight and height.

Formula:
BMI = Weight / Height²

### Q37. Can Feature Engineering improve Machine Learning performance?
Yes. Useful features can help a model learn important patterns more effectively.

### Q38. Should all features be used in a model?
No. Unnecessary or irrelevant features may be removed through Feature Selection.

### Q39. What should be checked before Feature Engineering?
The dataset, data types, missing values, outliers, features, target, and possible data leakage should be checked.

### Q40. What is the main goal of Feature Engineering?
The main goal is to convert raw data into useful features that help a Machine Learning model learn better patterns.

---

# Revision Questions

### Q1.
Define Feature Engineering.

### Q2.
What is a Feature?

### Q3.
What is a Target?

### Q4.
Why is Feature Engineering important?

### Q5.
What is Feature Creation?

### Q6.
What is Feature Transformation?

### Q7.
What is Feature Scaling?

### Q8.
Define Normalization.

### Q9.
Write the Min-Max Normalization formula.

### Q10.
Define Standardization.

### Q11.
Write the Standardization formula.

### Q12.
What is Encoding?

### Q13.
What is Label Encoding?

### Q14.
What is One-Hot Encoding?

### Q15.
What is Feature Selection?

### Q16.
Why is Feature Selection important?

### Q17.
What is Feature Extraction?

### Q18.
Differentiate Feature Selection and Feature Extraction.

### Q19.
What are Missing Values?

### Q20.
Name methods used to handle Missing Values.

### Q21.
What is Mean Imputation?

### Q22.
What is Median Imputation?

### Q23.
What is Mode Imputation?

### Q24.
What is an Outlier?

### Q25.
What is Binning?

### Q26.
What are Date and Time Features?

### Q27.
What is Text Feature Engineering?

### Q28.
What is Log Transformation?

### Q29.
What is Skewed Data?

### Q30.
What is Data Leakage?

### Q31.
Why should Data Leakage be avoided?

### Q32.
What is a Feature Engineering Pipeline?

### Q33.
Name Python libraries used for Feature Engineering.

### Q34.
Differentiate Normalization and Standardization.

### Q35.
Why is categorical data encoded?

### Q36.
Write the BMI formula.

### Q37.
How can Feature Engineering improve a model?

### Q38.
Should all features be used?

### Q39.
What should be checked before Feature Engineering?

### Q40.
What is the main goal of Feature Engineering?

---

# Practical Questions

### Q41.
Create a BMI feature using height and weight in Pandas.

### Q42.
Create year, month, and day features from a date using Pandas.

### Q43.
Perform One-Hot Encoding using Pandas.

### Q44.
Perform Standardization using Scikit-learn.

### Q45.
Perform Min-Max Scaling using Scikit-learn.

### Q46.
Fill missing numerical values using the mean in Pandas.

### Q47.
Fill missing numerical values using the median in Pandas.

### Q48.
Write Python code to calculate the logarithm of numerical data using NumPy.

### Q49.
Explain how you would handle categorical and numerical features before training a model.

### Q50.
Create a complete basic Feature Engineering workflow for a Machine Learning dataset.

---

# Important Points

1. Feature = Input variable.
2. Target = Output to be predicted.
3. Feature Engineering prepares useful input features.
4. Feature Creation creates new features.
5. Feature Transformation changes feature representation.
6. Feature Scaling brings numerical features to a similar scale.
7. Normalization commonly scales values to 0–1.
8. Standardization uses mean and standard deviation.
9. Encoding converts categorical data into numerical form.
10. Label Encoding assigns numbers to categories.
11. One-Hot Encoding creates binary columns.
12. Feature Selection selects useful existing features.
13. Feature Extraction creates useful representations from raw data.
14. Missing values must be handled carefully.
15. Outliers should be investigated before removing them.
16. Binning converts continuous values into groups.
17. Dates can provide year, month, day, and weekday features.
18. Text can be converted into numerical features.
19. Log Transformation can help with highly skewed data.
20. Data Leakage must be avoided.
21. Pandas, NumPy, and Scikit-learn are useful for Feature Engineering.
22. Good Feature Engineering can improve Machine Learning performance.

---

# Quick Revision

```text
Raw Data
   ↓
Understand Data
   ↓
Handle Missing Values
   ↓
Handle Outliers
   ↓
Create Features
   ↓
Transform Features
   ↓
Encode Categories
   ↓
Scale Features
   ↓
Select Useful Features
   ↓
Machine Learning Model




Most Important Formulas
Normalization:
X_normalized = (X - X_min) / (X_max - X_min)

Standardization:
Z = (X - Mean) / Standard Deviation

BMI:
BMI = Weight / Height²





One-Line Revision
Feature Engineering = Creating and preparing useful features for Machine Learning.
Feature Selection = Selecting useful features.
Feature Extraction = Creating useful representations.
Normalization = Scaling to a range such as 0–1.
Standardization = Mean 0 and Standard Deviation 1.
Encoding = Converting categorical data into numerical form.
Data Leakage = Unwanted information entering the training process.