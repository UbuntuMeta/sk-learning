import os
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import sklearn.metrics as metrics
home_dir = '../realdata'
data = fetch_california_housing(data_home=os.path.join(home_dir, "cal_housing"))
X = data['data']
y = data['target']
# Split train dataset and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# initialize the Ridge model
reg = Ridge()

# train it
reg.fit(X_train, y_train)

# predict it
y_pred = reg.predict(X_test)
print('Score is', reg.score(X_test, y_test))
rmse = metrics.mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)
middle_error = metrics.median_absolute_error(y_test, y_pred)
print('RMESE is', rmse)
print('R2 is', r2)
print('MIDDLE ERROR is', middle_error)