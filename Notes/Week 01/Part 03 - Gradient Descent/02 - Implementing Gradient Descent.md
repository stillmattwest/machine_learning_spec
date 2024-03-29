# Implementing Gradient Descent

Gradient descent is an *optimization algorithm* used to minimize the cost function in machine learning models, including linear regression. It is a way of finding the optimal value of both $w$ and $b$. 

The gradient is actually a vector that points towards the steepest *increase* of the cost function, so gradient descent moves us in the opposite direction of that. 

In machine learning, the model will run gradient descent repeatedly until either the cost function reaches a minimum or else the difference between iterations becomes negligibly small.

## The Algorithm

There are two formulae in gradient descent, one to reassign the value of $w$, the other to reassign the value of $b$.

$w = w-\alpha \frac{\partial}{\partial w}J(w,b)$

**A Note About = For Coders**

In coding, = is an assignment operator but that is not true in mathematics. In math, = is a *truth assertion*. 

$5 = 3+2$

$\varnothing = \pi r^2$

We can never write something like:

$a = a +1$

While that works in code, it can never be true in mathematics.

**End Note**

*All that about the equals being said, in this context we ARE using = as an assignment operator. We are assigning $w$ a new value based on the equation above.* 

$\alpha$ is the *learning rate*. In gradient descent, it sets how big of a "step" we take towards the local minimum. 

$\frac{\partial}{\partial w}J(w,b)$ is a derivative (technically a partial derivative) of the cost function.

Derivatives come from calculus, of course. But Ng says we're good even if our calculus might be a little rusty.

We won't go into the derivative of the cost function now, but it basically determined the "direction" we need to go to get to the local minimum. Combined with $\alpha$, it tells us how big a step to take, and in what direction.

But that's not all! 

We also need to re-assign the value of $b$.

$b = b-\alpha\frac{\partial}{\partial b}J(w,b)$

We update both these parameters at the same time. This means that update $w$ from its *original* value and $b$ from its *original* value. Don't modify $w$ and then use the new value in $b$, that's no bueno.

In code, you'd make temp variables, calculate, and then reassign $w$ and $b$ using the temp variables.

Just remember to do BOTH variables before moving on. Simultaneous. Right? Okay.



