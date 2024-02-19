from sklearn import preprocessing as pp
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.svm import SVR
import numpy as np
# load the dataset
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

# Standardization
X = pp.scale(X)
y = pp.scale(y)

# Split the train dataset and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create the model
regressor = SVR(kernel='linear')  # use linear as kernel
regressor.fit(X_train, y_train)

# predict the result
y_pred = regressor.predict(X_test)

y_test_repeated = np.repeat(y_test, 10)

plt.scatter(X_test, y_test_repeated, color='red')
plt.plot(X_test, y_pred, color='blue')  # draw the picture
plt.title('SVR Regression')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()