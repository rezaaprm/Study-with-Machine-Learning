# lib getdataset from yahoo
import yfinance as yf

# import library streamlit
import streamlit as st

# lib visualization data
import plotly.express as px
import plotly.graph_objects as go

# import custom func
from class_data import *
from class_visualization import *

# config web streamlit
st.set_page_config(
    page_title="My Dashboard - Cryptocurrency", layout="wide",initial_sidebar_state="auto",
)

# container-header
with st.container():
    st.markdown("> Visualization Data of Cryptocurrency and Stock Price")

# split two columns
coll, col2 = st.columns([0.3, 0.7], gap="small")

# coll - config dataset
with coll:
    # set labels
    st.success("Config Dataset")

    with st.form("my-form"):
        cryptocurrency = st.selectbox(
            "Choose a cryptocurrency", ("BTC-USD", "ETH-USD", "AMZN", "AAPL", "GOOG", "MSFT"),
            placeholder="Choose a cryptocurrency", index=None
        )

        start = st.date_input(
            label="Start Date", value=None, min_value=None, max_value=None,
        )

        end = st.date_input(
            label="End Date",value=None, min_value=None, max_value=None,
        )

        submit = st.form_submit_button(label="Submit", type="secondary", use_container_width=True)

