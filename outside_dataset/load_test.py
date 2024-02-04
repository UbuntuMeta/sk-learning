from sklearn.datasets import fetch_openml
# load diabetes dataset from openml
data = fetch_openml(name='diabetes', version=1, parser="auto")
print(data)