# Vectorization Part 02

  NumPy has a lot of numerical and array-based operations that utilize languages like C and Fortran under the hood to implement hardware-level parallelism. This makes it a LOT faster than your standard Python for-loop, especially when the arrays get large. 

  I tested this using arrays filled with 1,000,000 random ints. I made two operations to get the dot product of these vectors, one implemeted with a forloop at the other with `np.dot`. 

  


