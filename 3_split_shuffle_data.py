from sklearn import datasets
import numpy as np

# load dataset
iris = datasets.load_iris()
iris_X = iris.data # data (petal length, petal width, sepal length, sepal width)
iris_y = iris.target # label

# create random index list
randIndex = np.arange(iris_X.shape[0])
np.random.shuffle(randIndex)

# shuffle data
iris_X = iris_X[randIndex]
iris_y = iris_y[randIndex]

# split data, training (100), test (50)
X_train = iris_X[:100,:]
X_test = iris_X[100:,:]
y_train = iris_y[:100]
y_test = iris_y[100:]
