import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.cluster import KMeans
import numpy as np
#import cv

img = plt.imread("a.jpg")
height = img.shape[0] 
width = img.shape[1]
print(img)

plt.imshow(img)
plt.show()

