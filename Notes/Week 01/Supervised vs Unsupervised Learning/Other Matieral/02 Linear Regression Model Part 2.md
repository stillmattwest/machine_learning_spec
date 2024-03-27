# Linear Regression Part 02

Remember, a training set contains the input AND output variables ($x$ and $y$). This is because it is a training set, and this is supervised learning. 

We feed the training set into a learning algorithm ($f$ )

$f$ is the model.

Outputs (predictions) are written as $\hat y$.

The prediciton is the estimated value of $y$. 

$x -> f -> \hat y$

## How to Represent $f$?

$f_w,_b(x) = wx+b$

or

$f(x)$

or

$f(x) = wx + b$

This is linear regression with one variable. One input variable in our case. 

Let's breakdown the formula:

$f(x)$ represents the function when the input is x. It represents the dependent, or output, variable that we're trying to predict. 

$\hat y$ vs. $y$: $\hat y$ is the *predicted* output of $f(x)$. $y$ is the *true output*. That's the difference.

$w$ is the weight, or slope, of the linear function. It indicates how much the output $f(x)$ changes for a unit change in the input $x$.  A positive w indicates that the function is increasing with the increasing input, and a negative $w$ indicates a decreasing function.

$b$ is the y-intercept of the linear function. It represents the value of $f(x)$ when x is zero. Geometrically, its the point where the function intersects the y axis. 

Put it all togehter and the formula $f(x) = wx +b$ describes a linear relationship between the input variable and the output variable. W is the slope of the line and b is a y-intercept

one-variable linear regression is called *univariable linear regression*. Obviously, it's not the only type or the most useful type. If we're calculating home sale prices, for example, we'd want more than one data point to predict the price.






