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

img2 = np.zeros_like(img)

# method 1
for i in range(len(img2)):
    img2[i] = clusters[labels[i]] 

img2 = img2.reshape(height, width, 3)

plt.imshow(img2)
plt.show()
