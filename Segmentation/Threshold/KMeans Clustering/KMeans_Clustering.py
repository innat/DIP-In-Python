
"""
Image Data Analysis Using Numpy & OpenCV
author: Mohammed Innat
email:  innat1994@gmail.com
website: https://iphton.github.io/iphton.github.io/
Please feel free to use and modify this, but keep the above information. Thanks!
"""
from sklearn import cluster
pic = imageio.imread('<image location>')
plt.imshow(pic)

x, y, z = pic.shape
pic_2d = pic.reshape(x*y, z)

kmeans_cluster = cluster.KMeans(n_clusters=5)
kmeans_cluster.fit(pic_2d)
cluster_centers = kmeans_cluster.cluster_centers_
cluster_labels = kmeans_cluster.labels_

plt.figure(figsize = (15,8))
plt.imshow(cluster_centers[cluster_labels].reshape(x, y, z))
