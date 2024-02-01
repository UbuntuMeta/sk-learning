import os
from sklearn.datasets import fetch_olivetti_faces

# load the real dataset
data_base_dir = '../realdata'
data = fetch_olivetti_faces(data_home=os.path.join(data_base_dir, "olivetti"))

print(data)