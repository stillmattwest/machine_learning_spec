import numpy as np
import random
import time

array_len = 1000000
min_val = 1
max_val = 10

w_vec = np.random.randint(min_val,max_val +1, array_len)

x_vec = np.random.randint(min_val,max_val+1,array_len)

print('starting for loop...')
start_time = time.time()
total = 0

for i,num in enumerate(w_vec):
    subtotal = num * x_vec[i]
    total = total + subtotal

end_time = time.time()
total_time = end_time - start_time

print(f'for loop completed in {total_time:0.6f}. Total is: {total:,}')

print(f'\nstarting np dot...')
start_time = time.time()
total = np.dot(w_vec,x_vec)
end_time = time.time()
total_time = end_time - start_time

print(f'np dot completed in {total_time:0.6f}. Total is {total:,}')