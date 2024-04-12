# Feature Scaling Part 01

Feature scaling is a technique that allows gradient descent to run much faster.

The problem we're trying to solve here is that not all parameters share a common scale. 

For example, if we go back to calculating house prices, the size in square feet can range quite a bit, from 500 to 4000, easily. The size is also a relatively large number compared to something like total bedrooms, which probably only ranges between 1 and 5. 

If we used a common weight for those parameters, sq. feet would completely dominate the predicted price, while the number of bedrooms would barely factor in. 

The solution is to have a dynamic weight, which would be smaller for parameters with a large range, and larger for parameters with a small range. 

Makes sense, right?

BUT, that can wreak havoc on gradient descent, which might bounce around quite a bit trying to scale w. 

What you want is to apply feature scaling so that each feature in your vector has a similar scale. That gives you a nice round contour graph, and allows gradient descent to quickly find the minimum cost. 

But how? See part 2.