import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.cluster import KMeans
import numpy as np
#import cv

img = plt.imread("a.jpg")
height = img.shape[0] 
width = img.shape[1]
# print(img.shape)

img = img.reshape(height*width,3)

kmeans = KMeans(n_clusters = 4).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

img2 = np.zeros((height,width,3), dtype = np.uint8)

# method 2
index = 0
for i in range(height):
    for j in range(width):
        label_of_pixel = labels[index]
        img2[i][j] = clusters[label_of_pixel]
        index += 1

plt.imshow(img2)
plt.show()

