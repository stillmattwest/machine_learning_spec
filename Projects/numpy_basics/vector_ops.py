import numpy as np
# Single vetor operations in NumPy
a = np.array([1,2,3,4])
print(f'a: {a}')

#negate elements of a
b = -a
print(f'b = -a: {b}') #[-1,-2, etc]

# sum all elements of a, returns a scalar
# A scalar is a single numerical entity without additional attributes. An int is a scalar
b = np.sum(a)
print(f'b = np.sum(a): {b}')

#get the mean
b = np.mean(a)
print(f'b = np.mean(a): {b}')

# square each element of an array
b = a**2
print(f'b= a**2: {b}')

# add 3 to each element in an array. There are similar ops to scale each scalar in an array using normal mathematical operators
b = a+3
print(f'b = a+3: {b}')

## Vector dot product
# The dot product multiplies an array element by its mirror in another array. It then sums the total of these products.

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])

print(f'Dot product of a and b: {np.dot(a,b)}') # 1+4+9+16 = 30. prints 30.

