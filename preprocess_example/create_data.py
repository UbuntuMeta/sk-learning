import numpy as np

# standardization
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
sd = np.std(data)

# get the standard data
standard_data = (data - mean) / sd

print("Before standardization: {}".format(data))
print("After standardization: {}".format(standard_data))