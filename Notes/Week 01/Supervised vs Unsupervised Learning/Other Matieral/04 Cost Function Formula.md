# Cost Function Formula

In order to implement linear regression, the first step is to define something called a **cost function**.

## Review

We've got a training set of features x and targets y.

Our model is:

$f_w,_b(x)=wx+b$

## Parameters

in the formula above, w and b can be called *parameters*. They can also be called *coefficients* or *weights*.

The parameters have a strong effect on the output of the model. For example, if w is 0 we will always get a flat line. If b is then 1.5, we will always have a $\hat y$ that is 1.5. Right? B is the bias, and w is a flat line at zero, so that's all we can have. A flat line that starts at 1.5 on the y axis. 

We can prove it with math:

$f(x) = 0 * x + 1.5$

Since anything multiplied by zero is zero, viola, we have a flat line.

If we make it a little more interesting, with w = 0.5 and b = 1, then we get a line that starts at 1 on the y-axis and slopes up based on w. Since w is 0.5 the $\hat y$ will increase by 0.5 for every unit of x. 

Reminder: training examples are notated as:

$x^i, y^i$, with x being the input and y the target.

In machine learning, you want to find w and b values that give you a $\hat y$ that matches the true value of y. 

So, how do we do that?

## How to get $w,b$

To get w and b we need to measure how accurately our graph line matches the training data. 

To do that, we need to calculate our cost function. 

This is a gnarly looking equation. 

$J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} (h_{w, b}(x^{(i)}) - y^{(i)})^2$

From left to right:

$J(w,b)$ is the cost function.

$m$ is the number of training examples.

$h_w,_b(x^i)$ is the hypothesis function for the ith training example, predicting the output based on the input features of $x^i$. 

$y^i$ is the true value of the ith training example.

The summation of $\sum^m_i=1$ is taken over all the training examples. We use $1/2m$ as the multiple to get a more usable input when we have very large training sets. 

 $\sum^m_i=1$ is fancy notation for taking the sum starting at 1 and going up to m, which is the total size of the training data. it's `for i in range(1,m+1): total += i`, basically.

That equaltion is also called the **squared error cost function** and its the most used cost function for all regression problems, but especially in linear regressions. 

It's not the only cost function out there, though.


