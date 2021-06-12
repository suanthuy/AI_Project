import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# random data
A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# Visualize data
plt.plot(A,b,'ro')

# array to [[   ]]
# change row vector to column vector
A = np.array([A]).T
b = np.array([b]).T

# Create vector 1
ones = np.ones_like(A, dtype = np.int8)
A = np.concatenate((A,ones),axis = 1)

# Use formula
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b) 

x0 = np.array([1,46]).T
y0 = x[0][0]*x0 + x[1][0]   
# ko co phep toan matrix cong mot so
# nhung trong numpy cong mot so voi tat ca cac phan tu cua matrix

# Test predict data
x_test = 12
y_test = x[0][0]*x_test + x[1][0]
print(y_test)

# Visualize x0,y0
plt.plot(x0,y0)
plt.show()


