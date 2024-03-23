from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()

print(type(iris))

print(iris.keys())

print(type(iris.data), type(iris.target))

print(iris.data.shape)

print(iris.target_names)

X = iris.data

y = iris.target

df = pd.DataFrame(X, columns = iris.feature_names)

print(df.head())

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(iris['data'], iris['target'])

X = [
    [5.9, 1.0, 5.1, 1.8],
    [3.4, 2.0, 1.1, 4.8],]

print(X)

prediction = knn.predict(X)

print(prediction)

from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import numpy as np

diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20]

regr = linear_model.LinearRegression()

regr.fit(diabetes_X_train, diabetes_y_train)

print('Input Values')
print(diabetes_X_test)

diabetes_y_pred = regr.predict(diabetes_X_test)
