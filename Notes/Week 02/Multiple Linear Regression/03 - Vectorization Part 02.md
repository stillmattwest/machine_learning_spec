# Vectorization Part 02

  NumPy has a lot of numerical and array-based operations that utilize languages like C and Fortran under the hood to implement hardware-level parallelism. This makes it a LOT faster than your standard Python for-loop, especially when the arrays get large. 

  I tested this using arrays filled with 1,000,000 random ints. I made two operations to get the dot product of these vectors, one implemeted with a for loop at the other with `np.dot`. 

  The `np.dot` method was over 200 times faster.

## Gradient Descent with Multiple Linear Regression

In the video for this section, Ng gave an example of implementing gradient descent with np arrays for $w$ and $\partial$ or $d$. 

If we use a standard iteration method like a for loop, a large dataset could take a long time. Hours, even, if the data set was sufficiently large. 

However, with Numpy we get parallelization that chunk up the arrays and handle muliplying $w$ by $\alpha$ and $d$ and reassigning them back to $w$ simultaneously. It can take those hours and reduce them to minutes. 

So, yeah, Numpy. I'm sold.

## NumPy Basics

NumPy is the primary scientific computing library for Python. At its core, it allows for the use of arrays and has many methods for manipulating those arrays. 

**vectors** are ordered arrays of numbers. Thier length is referred to as their *dimension* or their *rank*. In math, vector entries run from 1 to $n$. In computer science they generally run from 0 to $n-1$. 

Vectors can be denoted via boldface type (**x**) or with an arrow ($\vec{x}$). The arrow shows up better in dark mode.

The term "dimension" can be overloaded in computer science because it usually referrs to the number of indexes in an array. An array with one index is 1D such as [0,1,2,3,4]. A two-index array is a 2D array like so: [[1,2,3],[1,2,3],[4,5,6]]

## Vector Creation in NumPy

Data creation routines in NumPy generally have a first parameter which is the *shape* of the object. For a 1D array, the shape is a single value. For a multi-dimensional array the shape is a tuple such as (n,m).

```python
# NumPy routines which allocate memory and fill arrays with value
a = np.zeros(4);                
print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.zeros((4,));             
print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.random.random_sample(4); 
print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
```

See the vector_ops.py project for a sampling of numpy vector operations.

## Vector Vector Operations
Linear algebra often involves vector vector operations, which are simply operations on two vectors. Dot product is an example of a vector vector op.

## Matrices
A matrix is a two dimensional array. Not as exciting as THE Matrix, but probably more useful. 

The elements of a matrix are all of the same type. 

In notation, Matrices are denoted with a bold, capitol letter such as **X**. 

In many labs, $m$ is the number of rows and $n$ is the number of columns in a matrix. Why did they use such similar sounding letters? Bad decision.






