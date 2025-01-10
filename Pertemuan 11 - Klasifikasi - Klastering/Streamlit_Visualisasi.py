# Main Library
import numpy as np 
import pandas as pd 

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)

import matplotlib.pyplot as plt
import seaborn as sns

# Function Scatterplot
def Scatterplot(dataset, x, y):

    # Define Boxplot
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Set Labels
    sns.scatterplot(data=dataset, x=x, y=y, hue="species")
    ax.set_title("", fontsize=14)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("", fontsize=12)
    ax.grid(True)

    # Show Boxplot
    plt.tight_layout()

    return fig

def Elbow_Plot(range_n_clusters, inertia):
    
    # Define Boxplot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(range_n_clusters, inertia, color="tab:blue", linewidth=2.5, marker="o")

    # Set Labels
    ax.set_title('Analysis Elbow Method for Optimal Cluster')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.grid(True)

    # Show Boxplot
    plt.tight_layout()

    return fig

def KMeans_Plot(kmeans, scaled, y_kmeans):
    # Centroid KMeans
    centers = kmeans.cluster_centers_

    # Define Boxplot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.scatter(scaled[:, 2], scaled[:, 0], c=y_kmeans, cmap='viridis', marker='.', linewidths=2.5)
    plt.scatter(centers[:, 2], centers[:, 0], c='red', s=200, alpha=0.75, marker='x')

    # Set Labels
    ax.set_title('KMeans Clustering of Iris Dataset')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.grid(True)

    # Show Boxplot
    plt.tight_layout()

    return fig