from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

X, y = make_regression(n_samples=100, n_features=1, noise=10)
# Split the train dataset and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
# initialize the linear model
reg = LinearRegression()

# fit
reg.fit(X_train, y_train)
print("coefficient vector of the model", reg.coef_)
print("Coefficient intercept of the model", reg.intercept_)
