# Import Library
import yfinance as yf
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# Function- getData by Yahoo Finance
def getData(ticker, startDate, endDate):

    # Set the ticker and datetime
    dataset = yf.Ticker(ticker).history(start=startDate, end=endDate).reset_index()

    # Set the feature
    dataset = dataset[["Date", "Open", "High", "Low", "Close"]]

    # Return valure
    return dataset
# ----------------------------------------------------------------------------------------------------

# Function- Lineplot with Plotly
def lineplot(dataset, x, y, ticker):

    # Create Lineplot
    fig = px.line(dataset, x=x, y=y)

    # Update Colors
    colorscale = px.colors.diverging.Portland_r
    for i, trace in enumerate(fig.data):
        trace.update(line=dict(color=colorscale[i]))

    # Update Layout
    fig.update_layout(
        title = "Data Visualization of "+str(ticker), xaxis_title = "", yaxis_title = "",
        legend=dict(title='', orientation='h', yanchor='top', y=1, xanchor='center', x=0.5))

    # return values
    return fig

# Config Web Streamlit
st.set_page_config(page_title="My Dashboard", layout="wide")
st.balloons()

# Container-Header
st.markdown("### Dashboard of Cryptocurrency with Streamlit Framework")

# Container-Header
with st.sidebar:
    st.info("Config dataset")
    form = st.form("my-form")
    cryptocurrency = form.selectbox(label="Choose a type of cryptocurrency", options=("BTC-USD", "ETH-USD"), index=0)
    start_date = form.date_input(label="Start Date", value=None, min_value=None, max_value=None)
    end_date = form.date_input(label="End Date", value=None, min_value=None, max_value=None)
    submit = form.form_submit_button(label="Submit", type="secondary", use_container_width=True)

# Get-dataset
if submit :
    ticker = cryptocurrency
    startDate = start_date
    endDate = end_date

else :
    ticker = "BTC-USD"
    startDate = "2015-01-01"
    endDate = "2024-06-01"

dataset = getData(ticker, startDate, endDate)

# Set two-tab-index
tab1, tab2 = st.tabs(["Data Visualization", "Historical Data"])
tab1.plotly_chart(
    lineplot(
        dataset, "Date", ["Open", "High", "Low", "Close"], ticker
    ))
tab2.dataframe(dataset, use_container_width=True)
