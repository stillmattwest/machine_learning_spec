# Gradient Descent for Multiple Linear Regression

Reminder: multiple linear regression formula:

$f_{\vec{w},b}(\vec{x}) = \vec{w} \cdot \vec{x} + b$

So when we're applying gradient descent we do this:

repeat {

$w_j = w_j - \alpha \frac{\partial}{\partial w_j} J (\vec{w}b)$

$b = b =\alpha \frac{\partial}{\partial b} J(\vec{w},b)$

}

gradient descent with multiple features:
 We're going to end up with multiple costs J so J = n

 $w_n = w_n = \alpha \frac{1}{m} \sum _{i=1}^m{(f_{\vec{w},_b}(\vec{x}^{(i)}) - y^{(i)})x_n^{(i)}}$

 $b = b - \alpha \frac{1}{m} \sum_{i=1} ^m(f_{\vec{w},{b}}(\vec{x}^{(i)})-y^{(i)}$


 Same deal as before, really. We're getting the mean squared error for both w and b when applied to the entire dataset, but we're calculating a different $j$ for each feature.

## An Alternative to Linear Regression: The Normal Equation

There is an alternative to gradient descent but it only works on linear regression, not other types of machine learning algorithms. It is called the *normal equation*. 

Interestingly, it does not require iteration to find $w$ and $b$. It does it all in one go. 

But it can be slow when the number of features is large.

Engineers should not implement the normal equation on their own, but some machine learning libraries can do it automatically. 