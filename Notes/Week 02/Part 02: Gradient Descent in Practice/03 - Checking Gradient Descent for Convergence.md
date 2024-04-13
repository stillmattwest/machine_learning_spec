# Checking Gradient Descent for Convergence

Once way to check for gradient descent convergence is to log the value of the cost $J$ after x number of iterations through the algorithm. You can check it every iteration if you want.

What you should see is $J$ decreasing at each iteration. If it ever *increases* it probably means that either your learning rate $\alpha$ is too high, or else that there's a bug in your code. 

If you plot $J$ on a y-axis against the number of iterations on the x-axis then you should get a downward sloped curve. This is called the **learning curve**. 

When the learning curve is largely flat, gradient descent has converged. 

The amount of iterations gradient descent needs to converge can be hard to predict. It might be 30 iterations or 100,000. 

An automatic convergence test is to check for a value epsilon $\epsilon$, which is set to a very small number like $10^{-3}$ or .001. If the difference between $J$ at each itertion is at or below $\epsilon$ then you've reached convergence.

Ng doesn't like estimating $\epsilon$ so he plots out a graph to see a learning curve. 

