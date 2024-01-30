from sklearn.datasets import load_iris
from sklearn.datasets import load_diabetes

# Set as_frame to be True, to get the data as panda DataFrame
# Set return_X_y to be True, return data like (data, target) format
ds = load_iris(as_frame=True, return_X_y=True)
print(ds[0])


ds = load_diabetes(as_frame=True, return_X_y=True, scaled=True)
print(ds[0])