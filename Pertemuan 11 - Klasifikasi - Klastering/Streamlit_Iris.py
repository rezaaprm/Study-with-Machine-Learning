# Streamlit!
import streamlit as st

# Warning
import warnings
warnings.filterwarnings("ignore")

# Main Library
import pandas as pd 
import numpy as np
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

from Streamlit_Visualisasi import *
from Streamlit_Preprocess import *
from Streamlit_KMeans import *

# Config Web Streamlit
st.set_page_config(page_title="My Dashboard", layout="wide")

# Container Header
st.markdown("## Clustering Iris Dataset with Elbow and K-Means Algorithms")

# Config Dataset
dataset = pd.read_csv("../Dataset/dataset_iris.csv")
dataset = normalize(dataset)

# Columns
col1, col2 = st.columns([0.35, 0.65], gap="small")

with col1:
    st.dataframe(dataset, use_container_width=True)
    
with col2:
    tab1, tab2 = st.tabs(["Exploration Data Analysis", "Result of K-Means Clustering"])
    
    with tab1:
        col1, col2 = st.columns([0.5, 0.5], gap="small")
        
        col1.pyplot(
            Scatterplot(dataset=dataset, x="petal_length", y="petal_width"), 
            use_container_width=True)
        
        col2.pyplot(
            Scatterplot(dataset=dataset, x="sepal_length", y="sepal_width"), 
            use_container_width=True)
        
        col1.pyplot(
            Scatterplot(dataset=dataset, x="petal_length", y="sepal_length"), 
            use_container_width=True)
        
        col2.pyplot(
            Scatterplot(dataset=dataset, x="petal_width", y="sepal_width"), 
            use_container_width=True)
        
    with tab2:
        col1, col2 = st.columns([0.5, 0.5], gap="small")
        

        range_n_clusters, inertia = Elbow(dataset)
        
        col1.pyplot(
            Elbow_Plot(range_n_clusters, inertia),
            use_container_width=True
        )

        # Menentukan jumlah klaster optimal dari hasil Elbow
        optimal_clusters = 3

        scaled = dataset[["sepal_length", "sepal_width", "petal_length", "petal_width"]].values

        kmeans = KMeans(n_clusters=optimal_clusters)
        kmeans.fit(scaled)
        y_kmeans = kmeans.predict(scaled)
        
        col2.pyplot(
            KMeans_Plot(kmeans, scaled, y_kmeans)
        )