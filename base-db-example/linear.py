from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [5]])  # Input feature
y = np.array([2, 3.5, 2.8, 4.6, 5.2])     # Output target

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
X_new = np.array([[6], [7]])  # New data for prediction
y_pred = model.predict(X_new)

print("Predictions:", y_pred)

mse = metrics.mean_squared_error(y, y_pred)
r2 = metrics.r2_score(y, y_pred)
m_error = metrics.median_absolute_error(y, y_pred)

print('MSE is {}'.format(mse))
print('R2 is {}'.format(r2))
print('M_ERROR is {}'.format(m_error))
