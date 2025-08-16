# Import Dashboard Library
import streamlit as st
import yfinance as yf
from streamlit_extras.add_vertical_space import add_vertical_space

# Library Tambahan
import time
import streamlit as st
from streamlit_extras.let_it_rain import rain 
from plotly.subplots import make_subplots
import plotly.graph_objects as go

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

def example():
    rain(
        emoji="☀️",
        font_size=3,
        falling_speed=3,
        animation_length="infinite",
    )
example()

with st.spinner("Please Wait..."):
    time.sleep(3)


# Container-Header
st.markdown("## Dashboard of Adidas Sales using Streamlit Framework")

# Container-Header
with st.sidebar:
    st.info("Config dataset")
    form = st.form("my-form")
    data = form.selectbox(label="Choose a type", options=("Visualization", "Data"), index=0)
    submit = form.form_submit_button(label="Submit", type="secondary", use_container_width=True)

# Get-dataset
if submit :
    ticker = data

else :
    ticker = ""
    dataset = pd.read_excel("../Dataset/Adidas US Sales Datasets.xlsx", sheet_name='Sheet1')
    dataset.info()
    


# Dataset
dataset = pd.read_excel("../Dataset/Adidas US Sales Datasets.xlsx", sheet_name='Sheet1')
dataset.info()


col1, col2 = st.columns([0.5, 0.5], gap="small")

with col1:
    df = dataset.groupby(by=["Retailer"])["Total Sales"].aggregate("sum").sort_values(ascending=True).reset_index()

    fig = px.bar(df, x="Retailer", y="Total Sales", text="Total Sales", text_auto=".2s", color="Total Sales")

    st.plotly_chart(fig)
    # fig.show()


with col2:
    df = dataset.groupby(by=["Product"])[["Total Sales", "Operating Profit"]].aggregate("sum").reset_index().sort_values("Product")

    fig = px.bar(df, x="Product", y=["Operating Profit", "Total Sales"], title="Long-Form Input", text_auto=True)
    
    st.plotly_chart(fig)
    # fig.show()


col1, col2 = st.columns([0.5, 0.5], gap="small")

with col1:
    df = dataset.groupby(by=["Retailer"])["Total Sales"].aggregate("sum").sort_values(ascending=True).reset_index()

    fig, ax = plt.subplots(figsize=(15,5))
    sns.barplot(data=df, x="Retailer", y="Total Sales", hue="Total Sales")

    ax.set_title("", fontsize=14)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("", fontsize=12)
    ax.grid(True)
    ax.set_facecolor("midnightblue")
    fig.patch.set_facecolor("#0A0A23")
    ax.tick_params(colors='white')

    plt.figure(facecolor='lightblue')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=None, use_container_width=True)
    # plt.show()


with col2:
    df = dataset.groupby(by=["Product"])[["Total Sales", "Operating Profit"]].aggregate("sum").reset_index().sort_values("Product")

    fig, ax = plt.subplots(figsize=(15, 5))
    sns.barplot(data=df, x="Product", y="Operating Profit", hue="Product")

    ax.set_title("", fontsize=14)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("", fontsize=12)
    ax.grid(True)
    ax.set_facecolor("#1C1C3A")
    fig.patch.set_facecolor("#0A0A23")
    ax.tick_params(colors='white')

    plt.figure(facecolor='lightblue')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=None, use_container_width=True)
    # plt.show()


col1, col2 = st.columns([0.5, 0.5], gap="small")

with col1:
    df = dataset.groupby(by=["Sales Method"])["Operating Profit"].aggregate("sum").reset_index().sort_values(by=["Operating Profit"], ascending=False)

    fig = px.pie(df, values='Operating Profit', names='Sales Method', hole=0.8)
    fig.update_traces(hoverinfo='label+percent', textinfo='value')

    plt.figure(facecolor='lightblue')
    plt.tight_layout()
    st.plotly_chart(fig)
    # plt.show()


with col2:
    df = dataset.groupby(by=["Sales Method"])["Operating Profit"].aggregate("sum").reset_index().sort_values(by=["Operating Profit"], ascending=False)

    fig, ax = plt.subplots(figsize=(6,3))
    # sns.pieplot(data=df, x="Retailer", y="Total Sales", hue="Retailer")
    ax.pie(x=df["Operating Profit"], labels=df["Sales Method"], autopct='%.0f%%', startangle=314, explode=[0.1, 0.0, 0.0], shadow=True)
    s = pd.Series([1,2,3])
    s.plot.pie(cmap='cool')
    ax.set_title("", fontsize=4)
    ax.set_xlabel("", fontsize=2)
    ax.set_ylabel("", fontsize=2)
    ax.grid(True)
    ax.set_facecolor("#1C1C3A")
    fig.patch.set_facecolor("#0A0A23")
    ax.tick_params(colors='white')

    plt.figure(facecolor='lightblue')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=None, use_container_width=True)
    # plt.show()


col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25], gap="small")

with col1:
    df = dataset.groupby(by=["Invoice Date"])[["Total Sales", "Operating Profit"]].aggregate("sum")
    df = df.reset_index()
    
    fig = px.line(df, x="Invoice Date", y="Total Sales", title='', markers=True, text="Total Sales")
    fig.update_traces(texttemplate='%{text:.2s}', textposition='top center')
    
    st.plotly_chart(fig)
    # fig.show()


with col2:
    df = dataset.groupby(by=["Product"])[["Total Sales", "Operating Profit"]].aggregate("sum").reset_index().sort_values("Product")

    fig = px.bar(df, x="Product", y=["Operating Profit", "Total Sales"], title="Long-Form Input", text_auto=True)

    st.plotly_chart(fig)
    # fig.show()


with col3:
    df = dataset.groupby(by=["Product"])[["Total Sales", "Operating Profit"]].aggregate("sum").reset_index().sort_values("Product")


    fig = go.Figure()
    fig.add_trace(go.Bar(x=df["Product"], y=df["Total Sales"],
                    marker_color='crimson',
                    name='higher (Sales)'))
    fig.add_trace(go.Bar(x=df["Product"], y=df["Operating Profit"],
                    marker_color='lightslategrey',
                    name='lower (Profit)'
                    ))

    fig.update_layout(
        barmode='group',
        title="Total Sales dan Operating Profit per Product",
        xaxis_title="Product",
        yaxis_title="Jumlah (dalam unit)",
        showlegend=True,
        template="plotly_white"
    )

    st.plotly_chart(fig)
    # fig.show()


with col4:
    df = dataset.groupby(by=["Invoice Date"])[["Total Sales", "Operating Margin"]].aggregate("mean")
    df = df.reset_index()

    x = np.array(df["Invoice Date"])
    y = np.array(df["Total Sales"])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Invoice Date"], y=df["Total Sales"] + 1, name="vh", line_shape='vh'))

    fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))

    st.plotly_chart(fig)
    # fig.show()
    
    