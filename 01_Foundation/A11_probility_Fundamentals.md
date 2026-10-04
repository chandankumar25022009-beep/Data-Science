# A12 — Probability Fundamentals

## 1. What is Probability?

Probability is a branch of mathematics that measures how likely an event is to happen.

### Easy Definition

Probability = The chance or likelihood of an event happening.

### Example

When a fair coin is tossed, there are two possible outcomes:

- Heads
- Tails

The probability of getting Heads is:

P(Heads) = 1 / 2 = 0.5 = 50%

---

## 2. Why is Probability Important in Data Science?

Probability is important in Data Science because it helps us:

1. Understand uncertainty
2. Analyze random events
3. Make predictions
4. Build machine learning models
5. Understand data distributions
6. Estimate risks
7. Make data-driven decisions

### Key Point

Probability → Uncertainty → Prediction → Decision

---

## 3. Random Experiment

A Random Experiment is an experiment whose exact outcome cannot be predicted with certainty before it happens.

### Examples

- Tossing a coin
- Rolling a dice
- Drawing a card
- Selecting a student randomly

### Example

When a dice is rolled, we cannot know in advance whether the result will be 1, 2, 3, 4, 5, or 6.

### Easy Definition

Random Experiment = An experiment with an uncertain outcome.

---

## 4. Outcome

An Outcome is a possible result of a random experiment.

### Example

When a dice is rolled:

Possible outcomes:

1, 2, 3, 4, 5, 6

Each number is an outcome.

### Easy Definition

Outcome = A possible result of an experiment.

---

## 5. Sample Space

Sample Space is the set of all possible outcomes of a random experiment.

It is usually represented by S.

### Example: Coin Toss

S = {Heads, Tails}

### Example: Dice Roll

S = {1, 2, 3, 4, 5, 6}

### Easy Definition

Sample Space = Set of all possible outcomes.

---

## 6. Event

An Event is a set of one or more outcomes from the sample space.

### Example

A dice is rolled.

Sample Space:

S = {1, 2, 3, 4, 5, 6}

Event A = Getting an even number

A = {2, 4, 6}

### Easy Definition

Event = A desired outcome or group of outcomes.

---

## 7. Probability Formula

For equally likely outcomes:

Probability of an event is:

P(E) = Number of favorable outcomes / Total number of possible outcomes

### Example

A dice is rolled.

Find the probability of getting 4.

Favorable outcomes = 1

Total outcomes = 6

Therefore:

P(4) = 1 / 6

---

## 8. Probability Range

Probability always lies between 0 and 1.

### Formula

0 ≤ P(E) ≤ 1

### Meaning

P(E) = 0

→ Event is impossible.

P(E) = 1

→ Event is certain.

P(E) = 0.5

→ Event has a 50% probability.

### Percentage Form

0 = 0%

0.5 = 50%

1 = 100%

---

## 9. Impossible Event

An Impossible Event is an event that cannot happen.

### Example

Rolling a normal six-sided dice and getting 7.

There is no 7 on the dice.

Therefore:

P(7) = 0

### Easy Definition

Impossible Event = An event that cannot occur.

---

## 10. Certain Event

A Certain Event is an event that must happen.

### Example

Rolling a normal six-sided dice and getting a number from 1 to 6.

This must happen.

Therefore:

P(1 to 6) = 1

### Easy Definition

Certain Event = An event that must occur.

---

## 11. Complement of an Event

The Complement of an event means the event does not happen.

The complement of event A is written as:

A'

### Formula

P(A') = 1 - P(A)

### Example

If:

P(A) = 0.7

Then:

P(A') = 1 - 0.7

P(A') = 0.3

So, the probability that A does not happen is 0.3.

---

## 12. Coin Toss Probability

A fair coin has two possible outcomes:

S = {Heads, Tails}

### Probability of Heads

P(Heads) = 1 / 2

### Probability of Tails

P(Tails) = 1 / 2

Therefore:

P(Heads) + P(Tails) = 1

---

## 13. Dice Probability

A normal dice has six outcomes:

S = {1, 2, 3, 4, 5, 6}

### Probability of Getting an Even Number

Even numbers:

{2, 4, 6}

Favorable outcomes = 3

Total outcomes = 6

P(Even) = 3 / 6

P(Even) = 1 / 2

= 0.5

= 50%

---

## 14. Probability of an Odd Number

Odd numbers on a dice:

{1, 3, 5}

Favorable outcomes = 3

Total outcomes = 6

P(Odd) = 3 / 6

P(Odd) = 1 / 2

= 50%

---

## 15. Mutually Exclusive Events

Two events are mutually exclusive if they cannot happen at the same time.

### Example

In one coin toss:

Getting Heads and Tails at the same time is impossible.

Therefore, Heads and Tails are mutually exclusive events.

### Easy Definition

Mutually Exclusive Events = Events that cannot occur together.

---

## 16. Independent Events

Two events are independent if the occurrence of one event does not affect the probability of the other event.

### Example

Tossing a coin twice.

The result of the first toss does not change the probability of the second toss.

### Easy Definition

Independent Events = One event does not affect the other.

---

## 17. Dependent Events

Two events are dependent if the occurrence of one event affects the probability of the other.

### Example

Suppose a bag contains red and blue balls.

If one ball is removed without replacement, the number of remaining balls changes.

Therefore, the probability of the next draw may change.

### Easy Definition

Dependent Events = One event affects the probability of another event.

---

## 18. Addition Rule of Probability

For two events A and B:

P(A or B) = P(A) + P(B) - P(A and B)

This general formula avoids double-counting overlapping outcomes.

### For Mutually Exclusive Events

If A and B cannot happen together:

P(A and B) = 0

Therefore:

P(A or B) = P(A) + P(B)

### Example

A dice is rolled.

Event A = Getting 1

Event B = Getting 2

These events are mutually exclusive.

P(A or B)

= 1/6 + 1/6

= 2/6

= 1/3

---

## 19. Multiplication Rule of Probability

For independent events:

P(A and B) = P(A) × P(B)

### Example

A fair coin is tossed twice.

Probability of Heads on the first toss:

P(H) = 1/2

Probability of Heads on the second toss:

P(H) = 1/2

Therefore:

P(H and H)

= 1/2 × 1/2

= 1/4

---

## 20. Conditional Probability

Conditional Probability is the probability of an event occurring given that another event has already occurred.

It is written as:

P(A | B)

This means:

Probability of A given B.

### Formula

P(A | B) = P(A and B) / P(B)

where P(B) > 0.

### Easy Definition

Conditional Probability = Probability of an event given another event has already happened.

---

## 21. Real-Life Example of Conditional Probability

Suppose a college has students who study different programming languages.

We may ask:

"What is the probability that a student knows Python given that the student is from CSE?"

Here:

A = Student knows Python

B = Student is from CSE

We are finding:

P(A | B)

---

## 22. Bayes' Theorem

Bayes' Theorem is used to calculate conditional probabilities by relating different probabilities.

### Formula

P(A | B) = [P(B | A) × P(A)] / P(B)

### Easy Explanation

Bayes' Theorem helps us update the probability of an event when we receive new information.

### Applications

- Medical diagnosis
- Spam detection
- Fraud detection
- Machine learning
- Risk analysis

---

## 23. Expected Value

Expected Value represents the long-run average value of a random variable.

For discrete outcomes:

Expected Value = Sum of (Outcome × Probability)

### Example

Suppose a game has:

Outcome 1 with probability 0.5

Outcome 3 with probability 0.5

Expected Value:

E(X) = (1 × 0.5) + (3 × 0.5)

E(X) = 0.5 + 1.5

E(X) = 2

### Easy Definition

Expected Value = Long-run average outcome.

---

## 24. Random Variable

A Random Variable is a variable whose value depends on the outcome of a random experiment.

### Example

When a dice is rolled, let X represent the number obtained.

Then:

X ∈ {1, 2, 3, 4, 5, 6}

X is a random variable.

### Easy Definition

Random Variable = A variable whose value depends on a random outcome.

---

## 25. Probability Distribution

A Probability Distribution describes the probabilities associated with the possible values of a random variable.

### Example

For a fair dice:

| X | Probability |
|---|---|
| 1 | 1/6 |
| 2 | 1/6 |
| 3 | 1/6 |
| 4 | 1/6 |
| 5 | 1/6 |
| 6 | 1/6 |

The probabilities add up to 1.

---

## 26. Probability in Machine Learning

Probability is widely used in Machine Learning.

It can help with:

- Classification
- Prediction
- Risk estimation
- Uncertainty measurement
- Bayesian methods
- Probabilistic models

### Example

A spam detection model may calculate:

Probability of email being spam = 0.95

This means the model estimates a 95% probability that the email is spam.

---

## 27. Probability in Data Science

Probability is used throughout Data Science.

```text
Data
  ↓
Statistics
  ↓
Probability
  ↓
Data Analysis
  ↓
Machine Learning
  ↓
Prediction
  ↓
Decision
# Interview Questions

## Q1. What is Probability?

Answer: Probability is a measure of how likely an event is to happen.

## Q2. Why is Probability important in Data Science?

Answer: Probability helps understand uncertainty, estimate risks, make predictions, and support data-driven decisions.

## Q3. What is a Random Experiment?

Answer: A Random Experiment is an experiment whose exact outcome cannot be predicted with certainty in advance.

## Q4. What is an Outcome?

Answer: An Outcome is a possible result of a random experiment.

## Q5. What is Sample Space?

Answer: Sample Space is the set of all possible outcomes of a random experiment.

## Q6. What is an Event?

Answer: An Event is a set of one or more outcomes from the sample space.

## Q7. What is the basic Probability formula?

Answer: Probability = Number of Favorable Outcomes / Total Number of Possible Outcomes.

## Q8. What is the range of Probability?

Answer: Probability ranges from 0 to 1.

## Q9. What is an Impossible Event?

Answer: An Impossible Event cannot occur and has probability 0.

## Q10. What is a Certain Event?

Answer: A Certain Event must occur and has probability 1.

## Q11. What are Mutually Exclusive Events?

Answer: Mutually Exclusive Events are events that cannot occur at the same time.

## Q12. What are Independent Events?

Answer: Independent Events are events where one event does not affect the probability of another event.

## Q13. What are Dependent Events?

Answer: Dependent Events are events where one event affects the probability of another event.

## Q14. What is Conditional Probability?

Answer: Conditional Probability is the probability of an event given that another event has already occurred.

## Q15. What is Bayes' Theorem?

Answer: Bayes' Theorem is used to calculate conditional probability using prior and related probability information.


# Revision Questions

1. What is Probability?
2. Why is Probability important in Data Science?
3. What is a Random Experiment?
4. What is an Outcome?
5. What is Sample Space?
6. What is an Event?
7. Write the basic Probability formula.
8. What is the range of Probability?
9. What is an Impossible Event?
10. What is a Certain Event?
11. What is the Complement of an Event?
12. What are Mutually Exclusive Events?
13. What are Independent Events?
14. What are Dependent Events?
15. What is the Addition Rule of Probability?
16. What is the Multiplication Rule of Probability?
17. What is Conditional Probability?
18. Write the formula for Conditional Probability.
19. What is Bayes' Theorem?
20. Write the formula for Bayes' Theorem.
21. What is Expected Value?
22. What is a Random Variable?
23. What is a Probability Distribution?
24. What is the difference between an Outcome and an Event?
25. What is the difference between Independent and Dependent Events?
26. What is the difference between Impossible and Certain Events?
27. How is Probability used in Machine Learning?
28. Give three real-life applications of Probability.
29. Name four Python libraries or modules useful for probability/statistical work.
30. Give one real-life example of Conditional Probability.


# Practical Questions

## Q31. A fair coin is tossed once. What is the probability of getting Heads?

## Q32. A fair dice is rolled once. What is the probability of getting 6?

## Q33. A fair dice is rolled once. What is the probability of getting an even number?

## Q34. A fair dice is rolled once. What is the probability of getting an odd number?

## Q35. A fair coin is tossed twice. What is the probability of getting Heads on both tosses?

## Q36. If P(A) = 0.7, what is P(A')?

## Q37. A dice is rolled. What is the probability of getting a number greater than 4?

## Q38. A dice is rolled. What is the probability of getting a number less than 3?

## Q39. What is the probability of getting either 1 or 2 when a fair dice is rolled?

## Q40. Give one real-life example where Probability is used in Data Science.


# Remember

Probability → Likelihood of an event

Random Experiment → Experiment with uncertain outcome

Outcome → Possible result

Sample Space → All possible outcomes

Event → Desired outcome or group of outcomes

Impossible Event → Probability 0

Certain Event → Probability 1

Independent Events → One does not affect the other

Dependent Events → One affects the other

Conditional Probability → Probability given another event

Bayes' Theorem → Updates probability using new information

Expected Value → Long-run average outcome

Random Variable → Variable based on random outcome

Probability Distribution → Probabilities of possible values


# Key Point

Probability helps Data Scientists understand uncertainty, calculate likelihoods, estimate risks, and make predictions.

Random Experiment
       ↓
Outcomes
       ↓
Sample Space
       ↓
Events
       ↓
Probability
       ↓
Statistics
       ↓
Data Science
       ↓
Machine Learning
       ↓
Prediction