from sklearn.datasets import load_diabetes
from sklearn import preprocessing as pp
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn import metrics
import matplotlib.pyplot as plt
# get the dataset
diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

# standardization
X = pp.scale(X)
y = pp.scale(y)

# Split the train dataset and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# Define the SVR model
reg = SVR(kernel='linear')

# train it
reg.fit(X_train, y_train)

# predict it
y_pred = reg.predict(X_test)
mse = metrics.mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)
m_error = metrics.median_absolute_error(y_test, y_pred)

print('MSE is {}'.format(mse))
print('R2 is {}'.format(r2))
print('M_ERROR is {}'.format(m_error))

print("The size of X_test", len(X_test))
print("The size of y_test", len(y_test))




