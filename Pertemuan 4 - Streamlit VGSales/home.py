# Import Dashboard Library
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Library Visualization
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Library Manipulation Data
import pandas as pd 
import numpy as np 

# Config Web Streamlit
st.set_page_config(page_title="Video Games Sales", layout="wide")
st.balloons()

# Container-Header
st.markdown("## Dashboard of Video Games Sales using Streamlit Framework")

# Dataset
dataset = pd.read_csv("../Dataset/vgsales.csv")

# Calculate Global-Sales
df = dataset[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].aggregate("sum").sort_values(ascending=True).reset_index()
df.columns = ["Region", "Sales"]

# Container-Global_Sales
add_vertical_space(2)
st.info("Exploration Data Analysis on Global Sales")
col1, col2 = st.columns([0.5, 0.5], gap="small")

with col1:
    fig = px.bar(df, y="Region", x="Sales", text_auto='.4s')
    fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
    fig.update_layout(title="Sum of games sales by regions", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig)

with col2:
    fig = px.pie(df, values="Sales", names="Region", hole=0.5, color_discrete_sequence=px.colors.sequential.Bluyl_r)
    fig.update_traces(textinfo="percent")
    fig.update_layout(title="Percentage of games sales by region")
    st.plotly_chart(fig)



st.info("Analyze of Best Games Names, Publisher, Genre, and Platform on Global Sales")
col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25], gap="small")

# Calculate by Platform
with col1:
    df = dataset.groupby("Platform")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum").reset_index()
    df = df.sort_values(by=["Global_Sales"]).reset_index().tail(5)

    fig = px.bar(df, y="Platform", x="Global_Sales", text_auto='.4s')
    fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
    fig.update_layout(title="Best platform by regions", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig)

# Calculate by Genre
with col2:
    df = dataset.groupby("Genre")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum").reset_index()
    df = df.sort_values(by=["Global_Sales"]).reset_index().tail(5)

    fig = px.bar(df, y="Genre", x="Global_Sales", text_auto='.4s')
    fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
    fig.update_layout(title="Best genre by regions", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig)

# Calculate by Publisher
with col3:
    df = dataset.groupby("Publisher")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum").reset_index()
    df = df.sort_values(by=["Global_Sales"]).reset_index().tail(5)

    fig = px.bar(df, y="Publisher", x="Global_Sales", text_auto='.4s')
    fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
    fig.update_layout(title="Best publisher by regions", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig)

# Calculate by Name
with col4:
    df = dataset.groupby("Name")[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].aggregate("sum").reset_index()
    df = df.sort_values(by=["Global_Sales"]).reset_index().tail(5)

    fig = px.bar(df, y="Name", x="Global_Sales", text_auto='.4s')
    fig.update_traces(marker_color=px.colors.sequential.Bluyl_r)
    fig.update_layout(title="Best games by regions", xaxis_title="", yaxis_title="")
    st.plotly_chart(fig)