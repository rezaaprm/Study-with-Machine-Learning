# Streamlit!
import streamlit as st

# Warning
import warnings
warnings.filterwarnings("ignore")
import time as tm

# Library Utama
import pandas as pd
import numpy as np

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)

import matplotlib.pyplot as plt
import seaborn as sns
import scipy

# Library Visualisasi Blobs
from sklearn.datasets import make_blobs

# Library for Data Preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Unsupervised Learning
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import contingency_matrix

from sklearn.metrics import accuracy_score
from sklearn.metrics import adjusted_rand_score

from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score


# Config Web Streamlit
st.set_page_config(page_title="My Dashboard", layout="wide")

# Container Header
st.markdown("## Dashboard Visualization of Clustering Make Blobs")

# Load dataset
x, y = make_blobs(n_samples=500, centers=4, cluster_std=0.5, random_state=0)

df = pd.concat([
    pd.DataFrame(x, columns=['X1', 'X2']),
    pd.DataFrame(y, columns=['Y'])
], axis=1)

st.info('')

col1, col2 = st.columns(([0.3, 0.7]), gap='medium')
with col1:
    st.dataframe(df, use_container_width=True)
    with st.form("my_form"):
        my_algorithm = st.selectbox('Choose Algorithm', ['K-Means','DBSCAN'])
        submit = st.form_submit_button('Submit', use_container_width=True)

with col2:
    tab1, tab2, tab3 = st.tabs(["Scatterplot", "Histplot", "Barplot"])

    with tab1:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.scatterplot(data=df, x="X1", y="X2", hue="Y", palette="viridis")

        ax.set_title('Scatterplot with Dataset make_blobs')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.grid(True)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)

    with tab2:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(data=df, x="X1", hue="Y", palette="Set1", kde=True, ax=ax, bins=25)

        ax.set_title('Histogram with Dataset make_blobs')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.grid(True)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(data=df, x="X2", hue="Y", palette="Set1", kde=True, ax=ax, bins=25)

        ax.set_title('Histogram with Dataset make_blobs')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.grid(True)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)

    with tab3:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.countplot(data=df, x="Y", hue="Y", palette="viridis")

        ax.set_title('Countplot with Dataset make_blobs')
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.grid(True)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)


st.info('Result of Clustering Make Blobs : ')


# Menentukan range untuk jumlah klaster
range_n_clusters = range(1, 11)
inertia = []

# Menggunakan Metode Elbow unntuk menemukan jumlah klaster optimal
for n_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(x)
    inertia.append(kmeans.inertia_)



if submit :

    col1, col2 = st.columns(([0.35, 0.65]), gap='medium')
    with col1:
        global centers
        # st.write("Jika K-Means yang muncul Nilai SSE")
        # st.write("Jika DBSCAN yang muncul Nilai Silhouette")
        note = "Jika K-Means yang muncul Nilai SSE"

        st.write(f" :blue[{note}]")
        st.write(" :blue[Jika DBSCAN yang muncul Nilai Silhouette]")

        if my_algorithm in ['K-Means']:

            # Measuring Execution Time
            start_time = tm.time()

            # Menentukan jumlah klaster optimal dari hasil Elbow
            optimal_clusters = 4
            # Menerapkan KMeans dengan jumlah klaster optimal
            kmeans = KMeans(n_clusters=optimal_clusters)
            kmeans.fit(df)
            y_kmeans = kmeans.predict(df)

            # Centroid KMeans
            centers = kmeans.cluster_centers_

            # Measuring Execution Time
            end_time = tm.time()

            # Calculating the Total Execution Time
            execution_time = end_time - start_time

            # Menghitung skor adjusted rand index (ARI)
            ari_score_km = adjusted_rand_score(y, y_kmeans)

            # Akurasi
            # Mengakses Nilai SSE (inertia_)

            sse = kmeans.inertia_


            df['my_algorithm'] = my_algorithm
            df['ari_score_km'] = ari_score_km
            df['sse'] = sse
            df['execution_time'] = execution_time

            df_grouped1 = df.groupby(by=["my_algorithm", "ari_score_km", "sse", "execution_time"]).size().reset_index(name="jumlah")
            st.dataframe(df_grouped1)  # Display interactive table


            centers_df = pd.DataFrame(centers, columns=[f"Center_{i}" for i in range(centers.shape[1])])
            st.dataframe(centers_df)

        
        elif my_algorithm in ['DBSCAN']:
            global clustering
            # Measuring Execution Time
            start_time2 = tm.time()

            clustering = DBSCAN(eps=0.6, min_samples=2).fit_predict(df[["X1", "X2"]])

            # Measuring Execution Time
            end_time2 = tm.time()

            # Calculating the Total Execution Time
            execution_time2 = end_time2 - start_time2

            # Menghitung skor adjusted rand index (ARI)
            ari_score_db = adjusted_rand_score(y, clustering)

            # Akurasi
            # Mengakses Silhouette Score
            sil_score = silhouette_score(x, clustering)


            df['my_algorithm'] = my_algorithm
            df['ari_score_db'] = ari_score_db
            df['sil_score'] = sil_score
            df['execution_time2'] = execution_time2

            df_grouped2 = df.groupby(by=["my_algorithm", "ari_score_db", "sil_score", "execution_time2"]).size().reset_index(name="jumlah")
            st.dataframe(df_grouped2)  # Display interactive table


            clustering_df = pd.DataFrame(clustering, columns=["Cluster"])
            st.dataframe(clustering_df)


        # # Konversi centers dan clustering ke dataframe
        # centers_df = pd.DataFrame(centers, columns=[f"Center_{i}" for i in range(centers.shape[1])])
        # clustering_df = pd.DataFrame(clustering, columns=["Cluster"])

        # # Gabungkan kedua dataframe
        # merged_df = pd.concat([centers_df, clustering_df], axis=1)

        # # Ubah nama kolom agar sesuai dengan format yang diinginkan
        # merged_df.columns = ["Centers"] * centers.shape[1] + ["Clustering"]

        # # Tampilkan dataframe di Streamlit
        # st.dataframe(merged_df)

    with col2:
        tab1, tab2 = st.tabs(["Cluster", "Elbow"])

        with tab1:
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.scatterplot(data=df, x="X1", y="X2", hue="Y", palette="viridis")

            ax.set_title('Hasil Visualisasi Klastering')
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.grid(True)

            plt.tight_layout()
            st.pyplot(fig, use_container_width=True)

        with tab2:
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
            # plt.show()
            st.pyplot(fig, use_container_width=True)