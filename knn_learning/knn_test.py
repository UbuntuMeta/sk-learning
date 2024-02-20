from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import numpy as np

X, y = make_classification(n_samples=1000, n_classes=4, n_clusters_per_class=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

knn_model = KNeighborsClassifier(n_neighbors=4, metric='manhattan')

# train it
knn_model.fit(X_train, y_train)
# predict
y_pred = knn_model.predict(X_test)

# Sum up the correct count of the prediction
correct_predictions = np.sum(y_pred == y_test)
print("Accuracy: {}%".format(correct_predictions / len(y_test) * 100))
