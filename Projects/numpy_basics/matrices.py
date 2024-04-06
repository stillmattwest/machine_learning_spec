import numpy as np

# Matrix creation

a = np.zeros((2,5)) # passing a tuple to define the shape of the array

print(f'a shape = {a.shape}, a = {a}')

# shape is (2,5)
# a is [[0,0,0,0,0],[0,0,0,0,0]]

# chessboard = np.zeros((8,8)) 
# print(f'\a chessboard of zeroes:\n {chessboard}')

## indexing

a = np.arange(6)

print(f'a = np.arrange(6):\n {a}') # [1...5]
a = a.reshape((3,2))
print(f'a = a.reshape(3,2):\n {a}') #[[0,1],[2,3],[4,5]]



