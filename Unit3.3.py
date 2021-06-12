import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import linear_model

# Random data
A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# Numpy array
A = np.array([A]).T
b = np.array([b]).T

# Plot random data
plt.plot(A,b,'ro')

# Create model
lr = linear_model.LinearRegression()
lr.fit(A,b)

# y = ax + b, a: coefficient, b: intercept
print(lr.intercept_)
print(lr.coef_)

# Draw line
x0 = np.array([[1,46]]).T               # Shapes (2,) mean [] (1 dimension)
y0 = lr.coef_*x0 + lr.intercept_

plt.plot(x0,y0)
plt.show()