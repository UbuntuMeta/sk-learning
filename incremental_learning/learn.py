import xgboost as xgb
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
# load boston data
housing = fetch_california_housing()

X, y = housing.data, housing.target

# Split the data to train dataset and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Transform data to DMatrix mode
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Define the XGBoost params
params = {
    'objective': 'reg:squarederror',
    'eval_metric': 'rmse',
    'eta': 0.1
}

model = xgb.train(params, dtrain, num_boost_round=10)

# predict with test dataset
preds = model.predict(dtest)

mse = mean_squared_error(y_test, preds)
rmse = np.sqrt(mse)

print("OLD RMSE: {}".format(rmse))

# use new data to predict and get RMSE
new_X, new_y = housing.data[:50], housing.target[:50]
new_data = xgb.DMatrix(new_X, label=new_y)
updated_model = xgb.train(params, new_data, num_boost_round=10, xgb_model=model)
updated_preds = updated_model.predict(dtest)
new_mse = mean_squared_error(y_test, updated_preds)
new_rmse = np.sqrt(mse)
print("NEW RMSE: {}".format(new_rmse))