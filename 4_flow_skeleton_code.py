from sklearn import datasets
import numpy as np
import math
import operator

def distance(p1,p2):
	dis = 0
	return distance

def get_k_neighbors(training_X, label_y, point, k):
	distances = []
	neighbors = []
	return neighbors

def highest_votes(labels):
	final_labels = 0
	return final_labels

def predict(training_X, label_y, point, k):
	neighbors_labels = get_k_neighbors(training_X, label_y, point, k)
	return highest_votes(neighbors_labels)

def accuracy_score(predicts, labels):
	accuracy = 0
	return accuracy


iris = datasets.load_iris()
iris_X = iris.data # data 
iris_y = iris.target # label

randIndex = np.arange(iris_X.shape[0])
np.random.shuffle(randIndex)

iris_X = iris_X[randIndex]
iris_y = iris_y[randIndex]

X_train = iris_X[:100,:] # 100 training points
X_test = iris_X[100:,:] # 50 testing points
y_train = iris_y[:100] # 100 labels of 100 training points
y_test = iris_y[100:] # 50 labels of 50 testing points

k=5
y_predict = []
for p in X_test:
	label = predict(X_train, y_train, p, k)
	y_predict.append(label)

acc = accuracy_score(y_predict, y_test)
print(acc)