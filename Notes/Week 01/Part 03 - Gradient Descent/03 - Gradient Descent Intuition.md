# Gradient Descent Intuition

Our gradient descent formulae:

$w = w - \alpha \frac{\partial}{\partial w}J(w,b)$

and

$b = b - \alpha \frac{\partial}{\partial b}J(w,b)$

Note: $\partial$ is not the same as $d$. $\partial$ is the symbol for a *partial derivative*, which is just called a derivative at this point in the course. 

The symbol for a total derivative is just $d$.

An easy way to visualize gradient descent is to simplify by removing $b$ and putting $w$ and $J$ on a 2D graph. This creates a "U" shape, with the minimum at the base of the U. 

Things to know:

$\alpha$ is always a positive number. It defines the size of the step taken towards the local minimum.

We multiply $\alpha$ by the derivative of $J(w)$, which is going to work differently on the left or right side of the minimum. 

On the left side, where the slope of the gradient is positive, the derivative will be positive. When we subtract that value from $w$, we decrease it, moving it towards the minimum.

On the right side of the graph, where the slope is negative, our derivative will be negative. Since subtracting a negative number is the same as adding, $w$ will increase, moving it towards the minimum. 

So, gradient descent "finds" the gradient, and then moves the value of $w$ in the opposite direction, "descending" the gradient.

That's a simplified example. In reality, gradient descent will also use $b$ in a linear regression, and on even more parameters in a more complex type of model. But that's the idea. It moves "downhill" on the graph. 


