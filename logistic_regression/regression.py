from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
X, y = make_moons(noise=0.05, n_samples=1000)
ax.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=25)

plt.show()