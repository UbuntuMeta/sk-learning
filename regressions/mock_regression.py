# from sklearn.datasets import make_regression
# import matplotlib.pyplot as plt
#
# fig, ax = plt.subplots(1, 1)
#
# X, y = make_regression(n_samples=100, n_features=1, noise=10)
# ax.scatter(X[:, 0], y, marker="o")
# ax.set_title("样本数据")
#
# plt.show()
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

X, y = make_regression(n_samples=100, n_features=1, noise=10)
ax.scatter(X[:, 0], y, marker="o")
ax.set_title("Mock Sample Data")

plt.show()