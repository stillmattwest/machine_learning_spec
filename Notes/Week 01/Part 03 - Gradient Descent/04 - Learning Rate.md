# Learning Rate

The choice of the learning rate ($\alpha$) has a huge impact on the efficiency of a gradient descent algorithm. If it is poorly chosen, the algorithm may not work at all.

Remember that $\alpha$ is the "step size" of the descent. So, if its too small, the algorithm will work but inefficient. If it is too large, you may not be able to hit your target minima. So you get "effciency" of a sort, but you lose accuracy. In a worst case scenario you can bounce to either side of the minimum and create an infinite loop of sorts.

This failure is called a *failure to converge* or can even diverge. 

Note: Thinking about gradient descent, since we're modifying $w$ and $b$, if we hit the local minimum exactly, loss will be zero, and $w$ == $w$ and $b$ == $b$.

The best way is to start with larger steps and then take smaller steps as we approach the minimum.

Luckily, gradient descent just works that way. You don't need to adjust $\alpha$ as you go. 