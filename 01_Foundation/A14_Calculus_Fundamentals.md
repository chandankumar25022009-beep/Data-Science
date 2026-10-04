# A14 — Calculus Fundamentals

## 1. What is Calculus?

Calculus is a branch of mathematics used to study change, motion, growth, and accumulation.

### Easy Definition

Calculus = Mathematics of Change and Accumulation.

Calculus mainly has two parts:

1. Differentiation
2. Integration


## 2. Why is Calculus Important in Data Science?

Calculus is important in Data Science and Machine Learning because it helps us understand:

- Rate of change
- Optimization
- Loss minimization
- Gradient Descent
- Neural Networks
- Model training
- Parameter updates

### Key Point

Calculus → Change + Optimization


## 3. Function

A function is a rule that converts an input into an output.

Example:

f(x) = x²

If x = 2:

f(2) = 2²
     = 4

Therefore:

Input → Function → Output

2 → x² → 4


## 4. Limit

A limit describes the value that a function approaches as the input approaches a particular value.

Example:

lim x→2 (x + 3) = 5

### Easy Definition

Limit = The value a function approaches.


## 5. Continuity

A function is continuous when there is no sudden break or jump in its graph.

### Easy Definition

Continuity = A function changes smoothly without a break.


## 6. Derivative

A derivative measures the rate of change of a function.

### Easy Definition

Derivative = Rate of Change.

Example:

y = x²

dy/dx = 2x

At x = 3:

2 × 3 = 6

Therefore, the derivative is 6.


## 7. Real-Life Example of Derivative

Distance changes with time.

Distance → Time

The derivative of distance with respect to time gives velocity.

Velocity = Rate of change of distance.

Similarly:

Acceleration = Rate of change of velocity.


## 8. Power Rule

If:

f(x) = xⁿ

Then:

f'(x) = nxⁿ⁻¹

Example:

f(x) = x³

f'(x) = 3x²


## 9. Constant Rule

If:

f(x) = c

Then:

f'(x) = 0

Example:

f(x) = 5

f'(x) = 0


## 10. Constant Multiple Rule

If:

f(x) = cxⁿ

Then:

f'(x) = cnxⁿ⁻¹

Example:

f(x) = 5x²

f'(x) = 10x


## 11. Sum Rule

If:

f(x) = x² + x³

Then:

f'(x) = 2x + 3x²


## 12. Product Rule

For:

y = u × v

Formula:

dy/dx = u(dv/dx) + v(du/dx)

### Easy Meaning

First × derivative of second
+
Second × derivative of first


## 13. Chain Rule

The chain rule is used when one function is inside another function.

Example:

y = (x² + 1)³

The chain rule helps differentiate composite functions.

### Easy Definition

Chain Rule = Method for differentiating a function inside another function.


## 14. Partial Derivative

A partial derivative is used when a function has multiple variables.

Example:

f(x,y) = x² + y²

With respect to x:

∂f/∂x = 2x

With respect to y:

∂f/∂y = 2y


## 15. Gradient

A gradient is a vector containing the partial derivatives of a function.

For:

f(x,y) = x² + y²

Gradient:

∇f = [2x, 2y]

### Easy Definition

Gradient = Vector of partial derivatives.


## 16. Gradient in Machine Learning

In Machine Learning, a model has parameters.

The model makes predictions.

Predictions are compared with actual values.

A loss function measures the error.

The gradient tells us how the loss changes when parameters change.

The parameters are then updated to reduce the loss.


## 17. Gradient Descent

Gradient Descent is an optimization algorithm used to minimize a loss or cost function.

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


## 18. Learning Rate

Learning Rate controls the size of each parameter update.

Small Learning Rate
→ Small steps
→ Training may be slower

Large Learning Rate
→ Large steps
→ May overshoot the minimum

### Easy Definition

Learning Rate = Step size used to update parameters.


## 19. Optimization

Optimization means finding parameter values that achieve the desired objective.

In Machine Learning, the objective is often to minimize the loss function.


## 20. Local Minimum

A local minimum is a point where a function has a lower value than nearby points.

Simple idea:

        \      /
         \____/

Bottom point = Local Minimum


## 21. Global Minimum

A global minimum is the lowest value of a function over the entire considered domain.

Simple idea:

          \        /
           \      /
            \____/

Lowest point overall = Global Minimum


## 22. Integration

Integration is used to calculate accumulation and areas under curves.

### Easy Definition

Integration = Accumulation or area under a curve.


## 23. Differentiation vs Integration

| Differentiation | Integration |
|---|---|
| Measures rate of change | Measures accumulation |
| Finds derivative | Finds integral |
| Used in optimization | Used in accumulation |
| Important in Gradient Descent | Used in probability and modeling |

### Remember

Derivative → Change

Integral → Accumulation


## 24. Indefinite Integral

An indefinite integral does not have fixed limits.

Example:

∫ x dx

Result:

x²/2 + C

C = Constant of Integration


## 25. Definite Integral

A definite integral has fixed limits.

Example:

∫₀² x dx

It calculates the accumulated value between 0 and 2.


## 26. Area Under a Curve

Integration can calculate the area under a curve.

The area between the curve and the x-axis can be calculated using integration.


## 27. Calculus and Machine Learning

Calculus is used for:

- Optimization
- Gradient Descent
- Loss minimization
- Parameter updates
- Neural Networks
- Backpropagation
- Continuous probability models


## 28. Calculus and Neural Networks

Neural networks contain parameters called weights and biases.

During training:

Input
  ↓
Neural Network
  ↓
Prediction
  ↓
Loss
  ↓
Gradient
  ↓
Weight Update


## 29. Backpropagation

Backpropagation is used to calculate gradients in neural networks.

It uses the chain rule to propagate error information backward through the network.

### Process

Forward Pass
     ↓
Prediction
     ↓
Loss
     ↓
Backward Pass
     ↓
Gradients
     ↓
Update Weights


## 30. Loss Function

A loss function measures the difference between predicted and actual values.

Example:

Actual = 10
Predicted = 8

There is an error between them.

The loss function converts this error into a numerical value.

### Key Point

Lower Loss → Generally Better Model Fit


## 31. Mean Squared Error

Mean Squared Error (MSE) is commonly used for regression problems.

Formula:

MSE = (1/n) Σ(y - ŷ)²

Where:

y = Actual Value

ŷ = Predicted Value

n = Number of observations


## 32. MSE Example

Actual:

[10, 20]

Predicted:

[8, 18]

Errors:

10 - 8 = 2
20 - 18 = 2

Squared Errors:

2² = 4
2² = 4

Mean:

(4 + 4) / 2 = 4

Therefore:

MSE = 4


## 33. Calculus in Data Science Workflow

Data
 ↓
Data Cleaning
 ↓
EDA
 ↓
Statistics
 ↓
Machine Learning
 ↓
Loss Function
 ↓
Calculus
 ↓
Gradient
 ↓
Optimization
 ↓
Better Model


## 34. Python Practical — Function

```python
def f(x):
    return x**2

print(f(5))