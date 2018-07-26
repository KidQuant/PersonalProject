from sklearn import datasets
import matplotlib.pyplot as plt

iris_df = datasets.load_iris()

print(iris_df)

print(iris_df.feature_names)

print(iris_df.target)

print(iris_df.target_names)

label = {0: 'red', 1: 'blue', 2: 'green'}

x_axis = iris_df.data[:, 0]
y_axis = iris_df.data[:, 2]

plt.scatter(x_axis, y_axis, c=iris_df.target)

from sklearn import datasets
from sklearn.cluster import KMeans

iris_df = datasets.load_iris()

model = KMeans(n_clusters=3)

model.fit(iris_df.data)

predicted_label = model.predict([[7.2, 3.5, 0.8, 1.6]])

all_predictions = model.predict(iris_df.data)

print(predicted_label)
print(all_predictions)

from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd

seeds_df = pd.read_csv(
    "https://raw.githubusercontent.com/vihar/unsupervised-learning-with-python/master/seeds-less-rows.csv")
)

varieties = list(seeds_df.pop('grain_variety'))

samples = seeds_df.values

mergings = linkage(samples, method = 'complete')

dendrogram(mergings,
    labels=varieties,
    leaf_rotation=90,
    leaf_font_size=6,
    )

from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

iris_df = datasets.load_iris()

model = TSNE(learning_rate=100)

transformed = model.fit_transform(iris_df.data)

x_axis = transformed[:,0]
y_axis = transformed[:,1]

plt.scatter(x_axis, y_axis, c=iris_df.target)

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

iris = load_iris()

dbscan = DBSCAN()

dbscan.fit(iris.data)

pca = PCA(n_components=2).fit(iris.data)
pca_2d = pca.transform(iris.data)

for i in range(0, pca_2d.shape[0]):
    if dbscan.labels_[i] == 0:
        c1 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='r', marker='+')
    elif dbscan.labels_[i] == 1:
        c2 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='g', marker='o')
    elif dbscan.labels_[i] == -1:
        c3 = plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c='b', marker='*')

plt.legend([c1, c2, c3], ['Cluster 1', 'Cluster 2', 'Noise'])
plt.title('DBSCAN finds 2 clusters and Noise')
