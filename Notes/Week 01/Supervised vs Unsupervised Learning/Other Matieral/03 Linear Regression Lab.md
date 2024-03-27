# Linear Regression Lab Notes

## Python Variables

Some suggestions for variables:

$x$ => for training values => `x_train`

$y$ => for training targets => `y_train`

$x^i$, $y^i$ => training examples => `x_i`, `y_i`

$m$ => number of training examples => `m`

$w$ => parameter: weight => `w`

$b$ => parameter: bias => `b`

$f_w,_b(x^i)$ => the result of the model evaluation at $x^i$, parameterized by $w$,$b$: $f_w,_b(x^i)$ = $wx^i + b$.


## Training the Model

Our example is a model that is trying to predict house prices by square footage. We only have two points of training data: a house with 1000 sq ft and a house with 2000 sq ft. They sold for $300K and $500K, respectively. 

```python
# x_train is the input variable (size in 1000 square feet)
# y_train is the target (price in 1000s of dollars)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

# m is the number of training examples. This code is using NumPy.

print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is: {m}")

i = 0 # Change this to 1 to see (x^1, y^1)

x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

#plot the data points in MatPlotLib. Creates a chart with two points, one at the bottom left and one at the top right, showing a positive linear relationship between the sq footage and sale price.

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show()
```
## Computing Model Output

```python
def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples 
      w,b (scalar)    : model parameters  
    Returns
      f_wb (ndarray (m,)): model prediction
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
        
    return f_wb


tmp_f_wb = compute_model_output(x_train, w, b,)

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()
```

