import numpy as np
from sklearn import preprocessing as pp


def data_scale_by_min_max_scaling():
    data = np.array([10, 20, 30, 40, 50])
    min = np.min(data)
    max = np.max(data)

    data_new = (data - min) / (max - min)

    print("before:", data)
    print("after:", data_new)


def data_scale_by_sk():
    data = np.array([10, 20, 30, 40, 50])
    res = pp.minmax_scale(data, feature_range=(0, 1))
    print(res)


data_scale_by_sk()
