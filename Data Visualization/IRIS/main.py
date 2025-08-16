# main.py

# Import library streamlit dan plotly
# import library streamlit
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# import custom func
from class_data import getDataset, normalized
from class_visualization import barplot, heatmap, scatter, histogram, boxplot

# config web streamlit
st.set_page_config(
    page_title="My Dashboard - Iris Dataset", layout="wide", initial_sidebar_state="auto",
)

# load dataset iris
dataset = getDataset("Iris.csv")

# normalized data
dataset = normalized(dataset)

# code visualisasi seperti sebelumnya...


# Container header
with st.container():
    st.markdown("## Data Visualization of Iris Dataset")

# Container untuk visualisasi data
with st.container():

    # Split dua kolom untuk barplot dan heatmap
    col1, col2 = st.columns([1, 1], gap="medium")

    # Barplot untuk melihat jumlah kelas
    col1.plotly_chart(
        barplot(dataset["Species"], "Bar Chart to Find the Number of Classes"),
        use_container_width=True
    )

    # Heatmap untuk melihat korelasi antara fitur
    col2.plotly_chart(
        heatmap(dataset, "Heatmap Corr to calculate correlation between features"),
        use_container_width=True
    )

# Scatterplot untuk melihat linearitas antara fitur
col1.plotly_chart(
    scatter(
        dataset, "PetalLengthCm", "SepalLengthCm", "Scatterplot to see linearity between features"
    ), use_container_width=True
)
    
col2.plotly_chart(
    scatter(
        dataset, "PetalLengthCm", "SepalWidthCm", "Scatterplot to see linearity between features"
    ), use_container_width=True
)

col1.plotly_chart(
    scatter(
        dataset, "SepalLengthCm", "SepalWidthCm", "Scatterplot to see linearity between features"
    ), use_container_width=True
)

col2.plotly_chart(
    scatter(
        dataset, "SepalLengthCm", "PetalWidthCm", "Scatterplot to see linearity between features"
    ), use_container_width=True
)

# Histogram untuk melihat distribusi data antar fitur
col1.plotly_chart(
    histogram(
        dataset, "SepalLengthCm", "Histogram to see the distribution of data between features"
    ), use_container_width=True
)

col2.plotly_chart(
    histogram(
        dataset, "SepalWidthCm", "Histogram to see the distribution of data between features"
    ), use_container_width=True
)

col1.plotly_chart(
    histogram(
        dataset, "PetalLengthCm", "Histogram to see the distribution of data between features"
    ), use_container_width=True
)

col2.plotly_chart(
    histogram(
        dataset, "PetalWidthCm", "Histogram to see the distribution of data between features"
    ), use_container_width=True
)

# Boxplot untuk melihat nilai outlier pada setiap fitur berdasarkan spesies
col1.plotly_chart(
    boxplot(
        dataset, "Species", "SepalLengthCm", "Boxplot to see the outlier value in each feature"
    ), use_container_width=True
)

col2.plotly_chart(
    boxplot(
        dataset, "Species", "SepalWidthCm", "Boxplot to see the outlier value in each feature"
    ), use_container_width=True
)

col1.plotly_chart(
    boxplot(
        dataset, "Species", "PetalLengthCm", "Boxplot to see the outlier value in each feature"
    ), use_container_width=True
)

col2.plotly_chart(
    boxplot(
        dataset, "Species", "PetalWidthCm", "Boxplot to see the outlier value in each feature"
    ), use_container_width=True
)
