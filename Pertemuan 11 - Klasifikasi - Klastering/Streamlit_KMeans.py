# Unsupervised Learning
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

def Elbow(dataset):

    x = dataset[["sepal_length", "sepal_width", "petal_length", "petal_width"]].values

    # Menentukan range untuk jumlah klaster
    range_n_clusters = range(1, 11)
    inertia = []

    # Menggunakan Metode Elbow unntuk menemukan jumlah klaster optimal
    for n_clusters in range_n_clusters:
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(x)
        inertia.append(kmeans.inertia_)

    return range_n_clusters, inertia
