# Choosing the Learning Rate

Gradient descent depends on a good learning rate. 

Red flags that you have a poorly chosen learning rate (or bug) include seeing the learning curve bounce around, sometimes increasing and sometimes decreasing. 

This can happen because of a learning rate that is too large. What's happening is that you're overshooting your minimum.

Ng debugs gradient descent by setting $\alpha$ to a very small number. If that doesn't solve the problem, there's probably a bug rather than a bad learning rate. 

An optimal learning rate should decrease the learning curve rapidly without overshooting the minimum. 

Ng likes to adjust the $\alpha$ by a factor of three until he sees a learning rate that he likes.

