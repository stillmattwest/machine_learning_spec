# Feature Scaling Part 02

One easy technique you can use to scale features is to divide the minimum of the expected range by the maximum. For example, if our house price algorithm has square feet that range from 500 to 5000 we can divide min by max and get a scaled range from .1 to 1. 

Another trick is to use **mean normalization** which has much more complicated math but does a similar thing. 

Another common normalization method is to use **Z-score normalization**, which is calculated using a standard deviation. 

All of these calculations provide ways to scale a problematic input variable.

```
A good thing to aim for in feature scaling is to have each scaled input range from -1 to 1. 
```

But small scale numbers -- say from 0 to 3 -- don't necessarily need to be rescaled. 

But something that ranges from -100 to 100 should probably be scaled so it doesn't dominate the algorithm.

Very small scale numbers like .0001 to .001 might need to be scaled *up* to avoid being completely discounted.

When it doubt, rescale. It never hurts. 