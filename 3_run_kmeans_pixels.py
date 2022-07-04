import matplotlib.pyplot
from sklearn.cluster import KMeans

img = matplotlib.pyplot.imread("a.jpg")

width = img.shape[0]
height = img.shape[1]

print(img.shape)

img = img.reshape(width*height,3)

kmeans = KMeans(n_clusters=4).fit(img)

labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

print(labels)
print(clusters)