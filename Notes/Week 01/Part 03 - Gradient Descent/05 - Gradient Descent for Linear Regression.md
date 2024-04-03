# Gradient Descent for Linear Regression

Okay, we're ready to build our first machine learning algorithm! All we have to do is combine linear regression with gradient descent.

In other courses this week, we leared:

1. The linear regression model

    $f_w,_b = wx + b$

2. The Cost Function

    $J(w, b) = \frac{1}{2m} \sum_{i=1}^{m} (h_{w, b}(x^{(i)}) - y^{(i)})^2$

3. The Gradient Descent Algorithm

    $w=w - \alpha \frac{\partial}{\partial w} J(w,b)$

    $b=b - \alpha \frac{\partial}{\partial b} J(w,b)$

The derivatives of gradient descent end up using these formulae:

$\frac{1}{m} \sum_{i=1}^{m}(f_w,_b(x^(i))-y^(i))x^(i)$

$\frac{1}{m} \sum_{i=1}^{m}(f_w,_b(x^(i))-y^(i))$

Note: these are exactly the same except the $b$ formula lacks the $x^(i)$ at the end.

If you implement gradient descent with those formulae, it should work.

Those foruma are dervived from gradient descent using calculus, which is covered briefly in the class but I didn't take notes because it was a bit over my head.

If you want to review the full deriviation you should refer back to the Gradient Descent for Linear Regression class in Week 01 at about three minutes in.


## The Full Algorithm

*repeat until convergence* {

   $w = w - \alpha \frac{1}{m} \sum_{i=1}^{m} (f_w, _b(x^{(i)}) - y^{(i)}) x^{(i)}$

  $b = b - \alpha \frac{1}{m} \sum_{i=1}^{m} (f_{w, b}(x^{(i)}) - y^{(i)})$

}

Reminder: update $w$ and $b$ *simultaneously* at each step.

Note: In a linear regression squared error cost function, there is only one minimum, never multiple local minima. This is because the squared error cost function is a convex function when plotted against $w$ and $b$. 

Technically, a convex function has the property that any local minima is also a global minimum. There is only one optimal set of parameters ($w$ and $b$) that minimizes the cost function. 

This property is one of the reasons why gradient descent, a local optimization algorithm, works for linear regression with a squared error cost function. It guarantees convergence to the global minmium.