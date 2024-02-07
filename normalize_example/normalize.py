import numpy as np
from sklearn import preprocessing as pp


# norm calculation
def norm():
    arr = np.random.randint(0, 100, 10)
    print("vector: {}".format(arr))

    l1 = np.linalg.norm(arr, 1)
    print("l1 norm: {}".format(l1))
    l2 = np.linalg.norm(arr, 2)
    print("l2 norm: {}".format(l2))
    l_inf = np.linalg.norm(arr, np.inf)
    print("l_inf norm: {}".format(l_inf))


def normalize():
    data = np.random.randint(1, 100, size=(3, 3))
    l1 = pp.normalize(data, norm="l1")
    l2 = pp.normalize(data, norm="l2")
    l_max = pp.normalize(data, norm="max")

    print("l1 normalize: {}".format(l1))
    print("l2 normalize: {}".format(l2))
    print("l max normalize: {}".format(l_max))


if __name__ == "__main__":
    norm()
    print("#######################")
    normalize()
