import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn import linear_model

# Data
A = np.array([[2,9,7,9,11,16,25,23,22,29,29,35,37,40,46]]).T
b = np.array([[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]).T

# Draw data
fig1 = plt.figure("GD for linear regression")
ax = plt.axes( xlim = (-10,50), ylim = (-1,30))
plt.plot(A,b,'ro')

# line create by linear regression formula
lr = linear_model.LinearRegression()
lr.fit(A,b)
x0_GD = np.linspace(1,46,2)
y0_sklearn = lr.intercept_[0] + lr.coef_[0][0]*x0_GD
plt.plot(x0_GD,y0_sklearn, color = "green")


### Random initial line ###
# x_init mean a and b in y = ax + b
x_init = np.array([[1],[2]])
y0_init = x_init[0][0] + x_init[1][0]*x0_GD
plt.plot(x0_GD,y0_init,color="black")

plt.show()