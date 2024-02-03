import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, Y = make_blobs(n_samples=1000, centers=5)
plt.scatter(X[:, 0], X[:, 1], marker="o", c=Y, s=25)

plt.show()

#  Generate complex two-dimensional data
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

X, Y = make_classification(n_samples=100, n_classes=4, n_clusters_per_class=1)
plt.scatter(X[:, 0], X[:, 1], marker="o", c=Y, s=25)

plt.show()