import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Config Web
st.set_page_config(page_title="Crypto Dashboard Test", layout="wide")

# Sidebar untuk memilih filter
with st.sidebar:
    st.selectbox("Choose a Product", ("All", "Product 1", "Product 2"))
    st.selectbox("Choose a Retailer", ("All", "Retailer 1", "Retailer 2"))
    st.selectbox("Choose a Region", ("All", "Region 1", "Region 2"))
    st.selectbox("Choose a Sales Method", ("All", "Sales Method 1", "Sales Method 2"))
    st.button("Search")

# Load dataset CSV
dataset = pd.read_csv("../Dataset/ETH-USD update 08-2024.csv", parse_dates=["Date"])

# Pastikan kolom 'Date' berformat datetime
dataset['Date'] = pd.to_datetime(dataset['Date'])

# Membuat kolom layout Streamlit
col1, col2 = st.columns([8, 4])

# Visualisasi di kolom 1
with col1:
    st.header("Time Series of Stock Prices")

    hover = alt.selection_single(
        fields=["Date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    # Membuat grafik garis untuk 'Close' price menggunakan Altair
    lines = (
        alt.Chart(dataset, title="Evolution of Close Prices")
        .mark_line()
        .encode(
            x="Date",  # Kolom Date sebagai sumbu X
            y="Close",  # Kolom Close sebagai sumbu Y
            color=alt.value("#386926"),  # Set warna garis
        )
    )

    points = lines.transform_filter(hover).mark_circle(size=65)

    tooltips = (
        alt.Chart(dataset)
        .mark_rule()
        .encode(
            x="yearmonthdate(Date)",
            y="Close",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("Date", title="Date"),
                alt.Tooltip("Close", title="Close Price (USD)"),
            ],
        )
        .add_selection(hover)
    )

    # Gabungkan garis, titik, dan tooltips
    data_layer  = lines + points + tooltips
    st.altair_chart(data_layer, use_container_width=True)

# Menampilkan data yang telah difilter di kolom 2
with col2:
    st.header("Latest OHLC Metrics")

    # Mendapatkan data OHLC terbaru dari dataset
    latest_data = dataset.iloc[-1]

    st.metric("Open", f"{latest_data['Open']:.2f} USD")
    st.metric("High", f"{latest_data['High']:.2f} USD")
    st.metric("Low", f"{latest_data['Low']:.2f} USD")
    st.metric("Close", f"{latest_data['Close']:.2f} USD")

# Membuat dua kolom untuk visualisasi tambahan (jika diperlukan)
col1, col2 = st.columns([5, 5])


# Menampilkan grafik garis dengan Streamlit chart
with col1:
    col1.subheader("Line Chart")
    col1.line_chart(dataset[['Date', 'Close']].set_index('Date'))  # Menampilkan 'Close' dalam grafik garis

# Menampilkan data mentah di kolom kedua
with col2:
    col2.subheader("Raw Data")
    col2.write(dataset)
