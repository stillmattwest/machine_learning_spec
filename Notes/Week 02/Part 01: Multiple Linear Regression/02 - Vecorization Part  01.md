# Vectorization Part 01

Using vectorization makes code shorter and more efficient. They also allow you to use modern linear algebra libraries. 

They are also key to using GPUs.

In Python and NumPy vectors are laid out as arrays. 

It's important to remember that in math, vector entries start at 1, but of course in Python they start at zero.

Mathematically, you can write your unvectorized formula like so:

$f \vec{w},b(\vec{x}) = \sum^n_{j=1} w_j x_j + b$

In Python, you do it like this:

```python
f = 0
for j in range(n):
    f = f+w[j] * x[j]
f = f + b
```
But... there is a better way.

## How to Vectorize the Formula

Here is the vectorized math formula:

$f \vec{w},b(\vec{x}) = \vec{w} \cdot \vec{x} + b$

and in NumPy...

```python
f = np.dot(w,x) + b
```

The vectorized function is faster because of how NumPy works. It uses parallel hardware, similar to multiprocessing (although not necessarily using that class)

We'll take a closer look at that in the next class.