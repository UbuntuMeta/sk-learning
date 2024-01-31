from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.datasets import load_diabetes
from sklearn.datasets import load_linnerud
# Set as_frame to be True, to get the data as panda DataFrame
# Set return_X_y to be True, return data like (data, target) format
ds = load_iris(as_frame=True, return_X_y=True)
#print(ds[0])

# load hand written digit dataset
ds = load_digits(as_frame=True, return_X_y=True)
#print(ds[0])
# load Linarud Dataset
ds = load_linnerud(as_frame=True, return_X_y=True)
print(ds[0])
# ds = load_diabetes(as_frame=True, return_X_y=True, scaled=True)
# print(ds[0])