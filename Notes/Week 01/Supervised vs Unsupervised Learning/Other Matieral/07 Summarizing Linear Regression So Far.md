
# Summarizing Linear Regression So Far

As of the last class on Cost Function Intuition:

**Note:** This document isn't for any particular lecture. Rather, it is a quick summary of the most important concepts covered about linear regression so far in Week 01.

## Linear Regression
- Linear Regression is used in supervised learning.
- It trains machine learning models to predict an output ($\hat{y}$) given a certain input ($x$).
- The model is trained using training datasets, which have many examples of $x$ and their true corresponding $y$ values.
- The model runs this training data through an algorithm, applying two parameters: $w$ and $b$.
- $w$ is the *weight* given to $x$, determining the slope's angle on a chart. Linear regression aims to draw a straight line through as many $y$ values as possible, showing how the value of $x$ impacts the predicted value of $y$.
- $b$ is the *bias* of the model, showing the *y-intercept* point if $x$ is zero.

## Cost Functions and Loss
- The model uses an optimization algorithm, like *gradient descent*, to find the best values for $w$ and $b$.
- The model determines the optimal values for $w$ and $b$ by calculating the *loss*, which is the difference between $\hat{y}$ and the true $y$ value, using a *cost function* $J(w, b)$. A well-tuned model will have minimal loss between $\hat{y}$ and $y$.
- When the model is well-tuned, new inputs ($x$) should generate accurate predictions for $y$ based on the learned $w$ and $b$ values. The accuracy of these predictions partly depends on the amount of training data. More data generally leads to more accurate predictions.

## More
- The points above envision training data with a single input. In reality, there could be many more inputs, each with its own weight. This results in models that operate in higher-dimensional space, challenging to represent in physical space. These complex models use *multiple linear regression*, which will be covered later in the course.
