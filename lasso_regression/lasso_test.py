from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn import metrics

# generate the dataset for regression
X, y = make_regression(n_samples=80, n_features=100,noise=10)
# Split the train dataset and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
# initialize the model
lasso = Lasso()
# Train it
lasso.fit(X_train, y_train)

y_pred = lasso.predict(X_test)
rmse = metrics.mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)
m_error = metrics.mean_absolute_error(y_test, y_pred)
print('RMSE is', rmse)
print('R2 is', r2)
print('Mean absolute error is', m_error)

