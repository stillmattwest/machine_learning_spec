# Gradient Descent

Gradient Descent is an algorithm used to find the values of $w$ and $b$ in a cost function. 

It is used not only in machine learning but in deep learning and advanced neural networks.

It is one of the most important building blocks in machine learning. 

In fact, gradient descent can be used to find the minimum value of $any$ function. 

## Gradient Descent in a Cost Function

So we have our cost function:

$J_w,_b$

What we want is:

$min_w,_bJ(w,b)$

Here's basically what we'll do:

1. Start with some value for $w,b$. Commonly, this is set to zero.
2. Keep changing $w,b$ to reduce $J(w,b)$ until we settle at or near a minimum.
   
In more complex data sets where we don't get a simple bowl-shaped graph, there can actually be more than one minimum. Imagine a valley with hills and gullies. 

The above situation is common in neural networks, but not really in linear regression.

These various minimums are called *local minima*. 

Gradient descent basically checks to see the most direct path to a local minima. 

## Implementing Gradient Descent

