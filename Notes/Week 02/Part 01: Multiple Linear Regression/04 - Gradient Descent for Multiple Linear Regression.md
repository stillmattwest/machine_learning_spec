# Gradient Descent for Multiple Linear Regression

Reminder: multiple linear regression formula:

$f_{\vec{w},b}(\vec{x}) = \vec{w} \cdot \vec{x} + b$

So when we're applying gradient descent to multiple variables we do this:

repeat until convergence {

$w_j = w_j - \alpha \frac{\partial J(\vec{w},b)}{\partial w_j}$

$b = b =\alpha \frac{\partial J(\vec{w},b)}{\partial b}$

}

gradient descent with multiple features:
 We're going to end up with multiple costs $J$.

 $w_n = w_n = \alpha \frac{1}{m} \sum _{i=1}^m{(f_{\vec{w},_b}(\vec{x}^{(i)}) - y^{(i)})x_n^{(i)}}$

 $b = b - \alpha \frac{1}{m} \sum_{i=1} ^m(f_{\vec{w},{b}}(\vec{x}^{(i)})-y^{(i)}$


 Same deal as before, really. We're getting the mean squared error for both w and b when applied to the entire dataset, but we're calculating a different $j$ for each feature.

## An Alternative to Linear Regression: The Normal Equation

There is an alternative to gradient descent but it only works on linear regression, not other types of machine learning algorithms. It is called the *normal equation*. 

Interestingly, it does not require iteration to find $w$ and $b$. It does it all in one go. 

But it can be slow when the number of features is large.

Engineers should not implement the normal equation on their own, but some machine learning libraries can do it automatically. 

When looking at vector parameters, we often see notation like this:

$x^{(i)} _j$

Read that equation like a *nested loop*, left to right. So we have $i$ as rows, $j$ as individual cells (row $i$ by column $j$)

You can remember it as

$x^{(row)}_{col}$


## Parameter Vectors
Parameter vectors are annotated as column vectors:

$\begin{bmatrix} w0 \\ w1 \\ w2 \\ ... \\w^n\end{bmatrix}$

