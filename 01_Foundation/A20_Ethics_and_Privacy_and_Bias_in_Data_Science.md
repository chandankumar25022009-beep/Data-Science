# A20 — Ethics, Privacy & Bias in Data Science

## 1. What is Ethics in Data Science?

Ethics in Data Science means using data and technology in a responsible, fair, safe, and honest way.

A Data Scientist should think about:
- Is the data being used fairly?
- Is people's privacy protected?
- Can the model harm someone?
- Is the result biased?
- Is the data being used with proper permission?

### Simple Example

If a company uses customer data to build a recommendation system, it should not misuse or expose customers' private information.

---

## 2. Why is Ethics Important?

Ethics is important because Data Science can affect real people.

Main reasons:
1. Protect people's privacy.
2. Reduce unfair decisions.
3. Prevent misuse of data.
4. Build trust.
5. Make responsible AI and ML systems.
6. Reduce possible harm.

### Example

A hiring company uses an ML model to select candidates.

If the model unfairly rejects candidates because of gender, age, religion, or another protected characteristic, the system can create serious unfairness.

---

## 3. What is Data Privacy?

Data Privacy means protecting personal information and controlling how that information is collected, stored, processed, and shared.

### Examples of Personal Data

- Name
- Phone number
- Email address
- Home address
- Date of birth
- Location
- Financial information
- Health information
- Account information

---

## 4. Why is Data Privacy Important?

Data privacy protects people from:
- Unauthorized access
- Data misuse
- Identity theft
- Fraud
- Unwanted exposure
- Security risks

### Simple Example

A website collects users' email addresses.

The company should protect those email addresses and should not expose them publicly.

---

## 5. Personal Data

Personal data is information that can identify a person directly or indirectly.

### Direct Identification

Examples:
- Full name
- Phone number
- Email address

### Indirect Identification

A combination of information may identify a person.

Example:
- Age
- City
- Occupation

Together, these may help identify a person in some datasets.

---

## 6. Sensitive Data

Sensitive data requires stronger protection because misuse can cause significant harm.

Examples may include:
- Health information
- Financial information
- Authentication information
- Certain biometric information
- Other legally protected information

Data Scientists should follow applicable laws, regulations, organizational policies, and ethical standards when handling sensitive data.

---

## 7. Data Collection Ethics

Data should be collected responsibly.

Important principles:
1. Collect only necessary data.
2. Explain why data is being collected.
3. Use appropriate permission or legal basis where required.
4. Protect collected data.
5. Avoid unnecessary collection.
6. Respect user rights and applicable laws.

### Example

If an application only needs an email address, it should not unnecessarily collect a user's home address.

---

## 8. Data Consent

Consent means a person agrees to the collection or use of their data when consent is the appropriate legal basis.

Good consent should be:
- Clear
- Understandable
- Informed
- Specific
- Voluntary

### Example

A website clearly tells users why their data is being collected before asking for permission.

---

## 9. Data Security vs Data Privacy

### Data Privacy

Focuses on:
- How data is collected
- Why data is collected
- Who can use it
- How data should be used

### Data Security

Focuses on:
- Protecting data from unauthorized access
- Preventing data loss
- Preventing data theft
- Securing systems

### Simple Difference

Privacy = Proper use of data.

Security = Protection of data.

---

## 10. Data Anonymization

Data anonymization means modifying data so that individuals cannot reasonably be identified from it.

### Example

Original:

Name: Rahul
Age: 21
City: Delhi

After anonymization, identifying information may be removed or transformed.

Anonymization should be carefully designed because simply removing names does not always guarantee that a person cannot be identified.

---

## 11. Data Pseudonymization

Pseudonymization replaces identifying information with another identifier.

Example:

Original:
Name = Rahul

Pseudonymized:
User_ID = U1024

The original identity may still be recoverable using additional information, so pseudonymized data still needs protection.

---

## 12. Anonymization vs Pseudonymization

| Anonymization | Pseudonymization |
|---|---|
| Designed to prevent identification | Replaces identifiers |
| Identity should not be reasonably recoverable | Identity may be recoverable |
| Strong privacy protection | Privacy protection with additional controls |
| Data is transformed more strongly | Original mapping may exist |

---

## 13. What is Bias in Data Science?

Bias means a systematic unfairness or distortion in data, decisions, or model results.

A biased dataset can produce biased predictions.

### Simple Example

Suppose a hiring dataset mostly contains successful candidates from one demographic group.

A model trained on that data may learn patterns that do not fairly represent the wider candidate population.

---

## 14. Why Does Bias Occur?

Bias can occur because of:
1. Biased data collection
2. Historical inequality
3. Unbalanced datasets
4. Sampling problems
5. Human decisions
6. Measurement errors
7. Biased labels
8. Model design choices

---

## 15. Types of Bias

Common types include:

1. Sampling Bias
2. Selection Bias
3. Measurement Bias
4. Label Bias
5. Historical Bias
6. Confirmation Bias
7. Algorithmic Bias

---

## 16. Sampling Bias

Sampling bias occurs when the collected sample does not properly represent the population.

### Example

A survey about internet usage is conducted only among people who already use smartphones.

The result may not represent the entire population.

---

## 17. Selection Bias

Selection bias occurs when the way people or data points are selected creates an unrepresentative dataset.

### Example

A company studies employee satisfaction using responses only from employees who voluntarily completed a survey.

The people who did not respond may have different opinions.

---

## 18. Measurement Bias

Measurement bias occurs when the method used to collect or measure information systematically produces inaccurate results.

### Example

A sensor works less accurately for one group of conditions than another.

The resulting data may be systematically distorted.

---

## 19. Label Bias

Label bias occurs when labels or target values contain systematic errors or unfair judgments.

### Example

If historical decisions were unfair, using those decisions as training labels can pass the same unfairness to an ML model.

---

## 20. Historical Bias

Historical bias occurs when past data reflects inequalities or unfair practices that existed in the real world.

### Example

If historical hiring decisions were unequal, training a model directly on those decisions may reproduce historical patterns.

---

## 21. Algorithmic Bias

Algorithmic bias occurs when an algorithm or ML system produces systematically unfair outcomes for certain groups.

Bias may come from:
- Training data
- Features
- Labels
- Model design
- Evaluation method
- Deployment environment

---

## 22. What is Fairness?

Fairness means designing and evaluating systems so that people are not treated unfairly.

Fairness is context-dependent.

Different applications may require different fairness considerations.

### Example

A hiring model should be evaluated carefully to ensure that its decisions do not systematically disadvantage protected groups.

---

## 23. Fairness in Machine Learning

Fairness can involve checking model performance across different groups.

For example:
- Accuracy by group
- False positive rate by group
- False negative rate by group
- Precision by group
- Recall by group

Fairness should be evaluated according to the specific problem and applicable requirements.

---

## 24. What is Transparency?

Transparency means making important information about a data or ML system understandable.

A transparent system should help stakeholders understand:
- What data is used?
- What is the purpose?
- How is the system evaluated?
- What are its limitations?
- Who is responsible for it?

---

## 25. What is Explainability?

Explainability means providing understandable reasons or evidence for a model's outputs.

### Example

A bank's ML system rejects a loan application.

An explainable system can help identify important factors that contributed to the decision.

---

## 26. Transparency vs Explainability

Transparency:
- Explains how a system is designed and used.

Explainability:
- Helps explain why a particular prediction or output occurred.

---

## 27. Accountability

Accountability means people and organizations are responsible for the systems they build and use.

A Data Scientist should:
- Document important decisions.
- Test models.
- Monitor results.
- Report problems.
- Correct harmful issues.
- Follow organizational and legal requirements.

---

## 28. Responsible AI

Responsible AI means developing and using AI systems in a safe, fair, transparent, privacy-conscious, and accountable manner.

Important principles:
1. Fairness
2. Privacy
3. Security
4. Transparency
5. Explainability
6. Accountability
7. Human oversight
8. Reliability

---

## 29. Human Oversight

Human oversight means humans remain involved in important decisions where automated systems can cause significant consequences.

### Example

An AI system may assist a doctor or organization, but important decisions may require qualified human review.

---

## 30. Data Minimization

Data minimization means collecting and using only the data necessary for a specific purpose.

### Example

A weather application may need location information for weather forecasts, but it may not need unrelated personal information.

---

## 31. Purpose Limitation

Purpose limitation means data should be used for legitimate and clearly defined purposes.

### Example

If data was collected to provide a service, using it for an unrelated purpose may require additional justification, permission, or legal basis.

---

## 32. Data Retention

Data retention means deciding how long data should be stored.

Organizations should avoid keeping personal data longer than necessary, subject to legal and business requirements.

### Example

Old temporary records may be deleted according to an approved retention policy when they are no longer needed.

---

## 33. Data Governance

Data governance is the system of policies, processes, responsibilities, and controls used to manage data properly.

It includes:
- Data quality
- Data security
- Data privacy
- Data ownership
- Access control
- Data lifecycle
- Compliance

---

## 34. Access Control

Access control determines who can access specific data.

### Example

A company's customer database should not be accessible to every employee.

Only authorized users should have access according to their role.

---

## 35. Least Privilege

Least privilege means giving a user or system only the access necessary to perform its job.

### Example

A Data Analyst who only needs aggregated data should not automatically receive access to all personal customer records.

---

## 36. Data Breach

A data breach occurs when protected information is accessed, disclosed, altered, or stolen without proper authorization.

### Example

A database containing customer information is accessed by an unauthorized attacker.

Organizations should have security and incident-response procedures to reduce harm.

---

## 37. Ethics in Data Visualization

Data visualization should communicate information honestly.

Avoid:
- Misleading scales
- Unnecessary distortion
- Selective presentation
- Hiding important context
- Incorrect labels

### Example

Changing the y-axis scale can make a small difference appear much larger than it really is.

---

## 38. Ethical Use of AI

AI should not be used simply because it is technically possible.

Before deployment, ask:
1. What problem does it solve?
2. Who can be affected?
3. What can go wrong?
4. Is the data appropriate?
5. Is the system fair?
6. Can humans review important decisions?
7. How will the system be monitored?

---

## 39. Data Scientist Code of Conduct

A responsible Data Scientist should:
- Be honest.
- Protect data.
- Respect privacy.
- Avoid discrimination.
- Document work.
- Validate results.
- Report limitations.
- Avoid misleading conclusions.
- Follow applicable laws and organizational policies.

---

# PYTHON PRACTICAL

## 40. Checking Missing Values

    import pandas as pd

    df = pd.read_csv("data.csv")

    print(df.isnull().sum())

Purpose:
Find missing values in each column.

---

## 41. Checking Duplicate Data

    import pandas as pd

    df = pd.read_csv("data.csv")

    print(df.duplicated().sum())

Purpose:
Find the number of duplicate rows.

---

## 42. Removing Duplicate Data

    df = df.drop_duplicates()

    print(df)

Purpose:
Remove duplicate rows from the dataset.

---

## 43. Removing Unnecessary Personal Information

    df = df.drop(columns=["phone", "email"])

    print(df)

Purpose:
Remove personal columns when they are not required for the analysis.

Important:
Do not remove or use personal information automatically. First understand the purpose, requirements, and applicable rules.

---

## 44. Basic Data Access Control Example

    allowed_columns = ["age", "city", "purchase_amount"]

    safe_df = df[allowed_columns]

    print(safe_df)

Purpose:
Create an analysis dataset containing only the fields required for the task.

---

## 45. Checking Data Distribution

    print(df["gender"].value_counts())

Purpose:
Understand the distribution of values in a categorical column.

This can help identify possible representation issues, but a distribution difference alone does not prove unfairness.

---

## 46. Comparing Model Performance by Group

    from sklearn.metrics import accuracy_score

    for group in df["group"].unique():
        group_data = df[df["group"] == group]

        accuracy = accuracy_score(
            group_data["actual"],
            group_data["prediction"]
        )

        print(group, accuracy)

Purpose:
Compare model accuracy across groups.

Note:
Fairness cannot be determined from one metric alone. The correct evaluation depends on the application.

---

## 47. Data Anonymization Example

    df = df.drop(columns=["name", "phone", "email"])

    print(df.head())

Purpose:
Remove direct identifiers before an analysis when those identifiers are not required.

Important:
Simply removing direct identifiers does not always guarantee that a dataset is anonymous.

---

## 48. Detecting Potentially Imbalanced Data

    print(df["target"].value_counts(normalize=True))

Purpose:
Check the proportion of target classes.

Example output:

    Yes    0.80
    No     0.20

This indicates that the classes are imbalanced.

---

## 49. Basic Responsible Data Science Workflow

    import pandas as pd

    df = pd.read_csv("data.csv")

    # Understand the data
    print(df.info())

    # Check missing values
    print(df.isnull().sum())

    # Check duplicates
    print(df.duplicated().sum())

    # Check distributions
    print(df.describe(include="all"))

    # Check categorical values
    print(df["target"].value_counts())

Purpose:
Start with basic data-quality and responsible-use checks before modeling.

---

# INTERVIEW QUESTIONS WITH ANSWERS

## Q1. What is Data Science Ethics?

Answer:
Data Science Ethics means using data and technology responsibly, fairly, safely, and honestly.

## Q2. Why is ethics important in Data Science?

Answer:
It helps protect privacy, reduce unfairness, prevent misuse of data, and build trust.

## Q3. What is data privacy?

Answer:
Data privacy is the responsible collection, use, storage, and sharing of personal information.

## Q4. What is personal data?

Answer:
Personal data is information that can identify a person directly or indirectly.

## Q5. What is sensitive data?

Answer:
Sensitive data is information that requires stronger protection because misuse can cause significant harm.

## Q6. What is data security?

Answer:
Data security means protecting data from unauthorized access, loss, theft, or misuse.

## Q7. Difference between privacy and security?

Answer:
Privacy focuses on proper collection and use of data, while security focuses on protecting data.

## Q8. What is data anonymization?

Answer:
Data anonymization transforms data so individuals cannot reasonably be identified from it.

## Q9. What is pseudonymization?

Answer:
Pseudonymization replaces identifying information with another identifier while the original identity may still be recoverable.

## Q10. What is bias?

Answer:
Bias is a systematic distortion or unfairness in data, decisions, or model results.

## Q11. What is sampling bias?

Answer:
Sampling bias occurs when the selected sample does not properly represent the population.

## Q12. What is selection bias?

Answer:
Selection bias occurs when the selection process creates an unrepresentative dataset.

## Q13. What is measurement bias?

Answer:
Measurement bias occurs when the measurement process systematically produces inaccurate or distorted data.

## Q14. What is label bias?

Answer:
Label bias occurs when training labels contain systematic errors or unfair judgments.

## Q15. What is historical bias?

Answer:
Historical bias occurs when historical data reflects past inequalities or unfair practices.

## Q16. What is algorithmic bias?

Answer:
Algorithmic bias occurs when an algorithm produces systematically unfair outcomes for certain groups.

## Q17. What is fairness?

Answer:
Fairness means designing and evaluating systems to avoid unjust or discriminatory outcomes.

## Q18. What is transparency?

Answer:
Transparency means making important information about a system understandable to stakeholders.

## Q19. What is explainability?

Answer:
Explainability means providing understandable reasons or evidence for model outputs.

## Q20. What is accountability?

Answer:
Accountability means people and organizations are responsible for the systems they create and use.

## Q21. What is responsible AI?

Answer:
Responsible AI means developing and using AI in a fair, safe, privacy-conscious, transparent, and accountable way.

## Q22. What is human oversight?

Answer:
Human oversight means keeping humans involved in important decisions where automated systems can create significant consequences.

## Q23. What is data minimization?

Answer:
Data minimization means collecting and using only the data necessary for a specific purpose.

## Q24. What is purpose limitation?

Answer:
Purpose limitation means using data for clearly defined and legitimate purposes.

## Q25. What is data retention?

Answer:
Data retention means deciding how long data should be stored according to legitimate requirements.

## Q26. What is data governance?

Answer:
Data governance is the system of policies, processes, responsibilities, and controls used to manage data.

## Q27. What is access control?

Answer:
Access control determines who can access specific data.

## Q28. What is least privilege?

Answer:
Least privilege means giving users only the access necessary for their work.

## Q29. What is a data breach?

Answer:
A data breach occurs when protected information is accessed, disclosed, changed, or stolen without proper authorization.

## Q30. How can a Data Scientist reduce bias?

Answer:
A Data Scientist can use representative data, inspect data quality, evaluate model performance across relevant groups, document assumptions, and continuously monitor the system.

## Q31. Why is transparency important?

Answer:
Transparency helps users and stakeholders understand how a system is designed, used, evaluated, and limited.

## Q32. Why is explainability important?

Answer:
Explainability can help people understand important model decisions and identify possible problems.

## Q33. What is ethical data collection?

Answer:
Ethical data collection means collecting necessary data responsibly, explaining its purpose, respecting user rights, and following applicable requirements.

## Q34. What is data misuse?

Answer:
Data misuse means using data in an unauthorized, inappropriate, harmful, or unethical way.

## Q35. How can privacy be protected?

Answer:
Privacy can be protected through data minimization, appropriate access controls, security measures, anonymization or pseudonymization where suitable, and proper data governance.

## Q36. What is fairness evaluation?

Answer:
Fairness evaluation examines whether a model produces significantly different or potentially unfair outcomes across relevant groups.

## Q37. Why should Data Scientists document their work?

Answer:
Documentation improves transparency, reproducibility, accountability, and future maintenance.

## Q38. What is responsible data visualization?

Answer:
Responsible data visualization presents information accurately without misleading scales, labels, or selective presentation.

## Q39. What should be considered before deploying an AI system?

Answer:
Consider the purpose, data quality, privacy, security, fairness, explainability, risks, human oversight, and monitoring requirements.

## Q40. What is the role of a Data Scientist in ethical AI?

Answer:
A Data Scientist should identify risks, protect data, evaluate models, reduce unfairness, document limitations, and support responsible deployment.

---

# REVISION QUESTIONS

## Q1. Define Data Science Ethics.
## Q2. Why is ethics important?
## Q3. Define data privacy.
## Q4. What is personal data?
## Q5. What is sensitive data?
## Q6. Define data security.
## Q7. Difference between privacy and security.
## Q8. What is anonymization?
## Q9. What is pseudonymization?
## Q10. Difference between anonymization and pseudonymization.
## Q11. What is bias?
## Q12. What is sampling bias?
## Q13. What is selection bias?
## Q14. What is measurement bias?
## Q15. What is label bias?
## Q16. What is historical bias?
## Q17. What is algorithmic bias?
## Q18. What is fairness?
## Q19. What is transparency?
## Q20. What is explainability?
## Q21. What is accountability?
## Q22. What is Responsible AI?
## Q23. What is human oversight?
## Q24. What is data minimization?
## Q25. What is purpose limitation?
## Q26. What is data retention?
## Q27. What is data governance?
## Q28. What is access control?
## Q29. What is least privilege?
## Q30. What is a data breach?
## Q31. How can bias enter a dataset?
## Q32. How can bias affect ML models?
## Q33. Why should personal data be protected?
## Q34. Why is documentation important?
## Q35. Why is transparency important?
## Q36. Why is explainability important?
## Q37. How can Data Scientists reduce bias?
## Q38. How can data privacy be improved?
## Q39. What is ethical data visualization?
## Q40. What is responsible AI development?

---

# PRACTICAL QUESTIONS

## Q41. How do you check missing values using Pandas?

    print(df.isnull().sum())

## Q42. How do you check duplicate rows?

    print(df.duplicated().sum())

## Q43. How do you remove duplicate rows?

    df = df.drop_duplicates()

## Q44. How do you remove unnecessary columns?

    df = df.drop(columns=["column_name"])

## Q45. How do you check class distribution?

    print(df["target"].value_counts())

## Q46. How do you check class proportions?

    print(df["target"].value_counts(normalize=True))

## Q47. How can you create an analysis dataset with only required columns?

    safe_df = df[["age", "city", "purchase_amount"]]

## Q48. How can you compare model accuracy between groups?

    from sklearn.metrics import accuracy_score

    for group in df["group"].unique():
        group_data = df[df["group"] == group]

        score = accuracy_score(
            group_data["actual"],
            group_data["prediction"]
        )

        print(group, score)

## Q49. Why should fairness not be judged using only one metric?

Answer:
Because fairness depends on the application, data, decision process, and relevant performance measures.

## Q50. Why is removing names not always enough for anonymization?

Answer:
Other combinations of information may still allow a person to be identified.

---

# IMPORTANT POINTS

1. Ethics means responsible use of data and technology.
2. Privacy protects people's information and rights.
3. Security protects data from unauthorized access and loss.
4. Personal data can identify a person directly or indirectly.
5. Sensitive data needs stronger protection.
6. Anonymization aims to prevent reasonable identification.
7. Pseudonymization replaces identifiers but identity may remain recoverable.
8. Bias can enter through data collection, labels, measurements, or models.
9. Sampling bias occurs when a sample is not representative.
10. Historical bias can reflect past inequalities.
11. Algorithmic bias can create unfair outcomes.
12. Fairness should be evaluated in context.
13. Transparency helps stakeholders understand a system.
14. Explainability helps understand model outputs.
15. Accountability means taking responsibility for systems.
16. Responsible AI includes fairness, privacy, security, transparency, and human oversight.
17. Data minimization means collecting only necessary data.
18. Purpose limitation means using data for defined purposes.
19. Access control limits who can access data.
20. Least privilege gives only necessary access.
21. Data governance manages data responsibly.
22. Data breaches can expose protected information.
23. Data visualization should not mislead users.
24. Data Scientists should document assumptions and limitations.
25. Models should be monitored after deployment.

---

# QUICK REVISION

Ethics
→ Responsible and fair use of data.

Privacy
→ Proper handling and protection of personal information.

Security
→ Protection against unauthorized access and attacks.

Bias
→ Systematic unfairness or distortion.

Fairness
→ Avoiding unjust outcomes.

Transparency
→ Making important system information understandable.

Explainability
→ Helping explain model outputs.

Accountability
→ Taking responsibility for systems and decisions.

Responsible AI
→ Fair + Safe + Private + Transparent + Accountable.

Data Minimization
→ Collect only necessary data.

Access Control
→ Only authorized users can access data.

Least Privilege
→ Give only necessary permissions.

Data Governance
→ Policies and processes for responsible data management.

---

# ONE-LINE REVISION

Ethics = Use data responsibly.

Privacy = Protect personal information.

Security = Protect data from unauthorized access.

Bias = Systematic unfairness or distortion.

Fairness = Avoid unjust outcomes.

Transparency = Make important system information understandable.

Explainability = Explain model outputs.

Accountability = Take responsibility.

Anonymization = Reduce the ability to identify individuals.

Pseudonymization = Replace identifiers with pseudonyms.

Data Minimization = Collect only necessary data.

Purpose Limitation = Use data for defined purposes.

Access Control = Control who can access data.

Least Privilege = Give minimum necessary access.

Responsible AI = Build and use AI responsibly.

---

# FINAL KEY CONCEPT

A professional Data Scientist does not only ask:

"Can we build this model?"

A responsible Data Scientist also asks:

"Should we build it?"
"Is the data appropriate?"
"Is privacy protected?"
"Could the model be unfair?"
"Who can be affected?"
"How can we reduce the risk?"
"How will we monitor the system?"

Data Science is not only about data, Python, statistics, and machine learning.

Good Data Science also requires:

ETHICS + PRIVACY + FAIRNESS + SECURITY + TRANSPARENCY + ACCOUNTABILITY

This completes A20 — Ethics, Privacy & Bias in Data Science.