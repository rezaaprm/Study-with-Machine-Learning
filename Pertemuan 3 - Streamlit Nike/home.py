# Deklarasi variabel
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Config Web
st.set_page_config(page_title="My Dashboard", layout="wide")

# Using "with" notation
with st.sidebar:
    st.selectbox("Choose a Product",("All", "Product 1", "Product 2"))
    st.selectbox("Choose a Retailer",("All", "Retailer 1", "Retailer 2"))
    st.selectbox("Choose a Region",("All", "Region 1", "Region 2"))
    st.selectbox("Choose a Sales Method",("All", "Sales Method 1", "Sales Method 2"))
    st.button("Serch")

# Header
st.markdown("## Nike Sales Dashboard on 2020 - 2021")

# Load dataset
dataset = pd.read_csv("../Dataset/nike-sales-dataset_v2.csv", parse_dates=["Invoice Date"])
# st.dataframe(data=dataset,use_container_width=True)

# Fungsi menghitung total sales nike
def agg_total_sales(col):
    df = dataset.groupby(by=[col])["Total Sales"].aggregate("sum").sort_values(ascending=True).reset_index()
    return df

col1, col2= st.columns(2)
with col1:
    # Show barplot
    df_product = agg_total_sales("Product")
    fig = px.bar(df_product, x="Total Sales", y="Product", text_auto=".4s")
    fig.update_traces(marker_color=px.colors.sequential.algae)
    fig.update_layout(title="", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig,use_container_width=True)

with col2:
    # Show barplot
    df_retailer = agg_total_sales("Retailer")
    fig = px.bar(df_retailer, x="Total Sales", y="Retailer", text_auto=".4s")
    fig.update_traces(marker_color=px.colors.sequential.algae)
    fig.update_layout(title="", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig,use_container_width=True)

col1, col2= st.columns(2)
with col1:
    # Show barplot
    df_region = agg_total_sales("Region")
    fig = px.bar(df_region, x="Total Sales", y="Region", text_auto=".4s")
    fig.update_traces(marker_color=px.colors.sequential.algae)
    fig.update_layout(title="", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig,use_container_width=True)

with col2:
    # Show barplot
    df_salesmethod = agg_total_sales("Sales Method")
    fig = px.bar(df_salesmethod, y="Total Sales", x="Sales Method", text_auto=".4s")
    fig.update_traces(marker_color=px.colors.sequential.algae)
    fig.update_layout(title="", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig,use_container_width=True)