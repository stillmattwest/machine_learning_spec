# Multiple Features

Linear Regression can also work with multiple inputs, which can help make a more accurate prediction.

These can be denoted x_1, x_2, etc.

We group these inputs into *vectors*. 

## Terminology

**Vectors** are ordered collections of numbers. They can be row or column vectors.

$\mathbf{v} = (v_1,v_2, \ldots, v_n)$

Each "element" of a vector is called an *entry* or a *component*.

$x^i$ the "ith" input vector

$x_j$ = "jth" feature

$x^i_j$ the jth feature of the ith input vector.

$n$ is the total number of features (variables)

The *dot product* of two vectors is a way of summing up the "multiple pairs" of two vectors.

The "multiple pairs" are better referred to as *product terms*.

## How We Define the Model with Multiple Features

$f_w,_b(x) = w_1 x_1 + w_2 x_2 + \ldots + w_nx_n + b$

Not all of these multiples have to be positive. For example, the age of a house might actually reduce the predicted price.

Vectors can be denoted with a small arrow above the vector variable.

With that notation, we have a simpler way to write our equation:

$f \vec{w},b(\vec{x}) = \vec{w} \cdot vec{x} + b$

That center dot does NOT mean multiplication, it means "dot product."

Let's walk through that equation:

When you calculate the dot product of two vectors, what you are doing is *iterating* though each number in either vector. So, for example, we have $\vec{w}$ and $\vec{x}$. If each vector has four entries, then $\vec{w} \cdot \vec{x}$ is actually the **sum** of these product terms. I.E: $w1x1$ + $w2x2$ + $w3x3$ + $w4x4$.


This type of model is called **multiple linear regression**. Note: it is NOT called multi-variate regression, because that term refers to something else. 

