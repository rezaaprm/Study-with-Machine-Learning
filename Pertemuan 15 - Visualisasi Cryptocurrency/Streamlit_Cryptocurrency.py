# Add file
from Function_Dataset import *
from streamlit_extras import add_vertical_space as avs

# Lib Main
import streamlit as st
import time as tm
import yfinance as yf

# Lib Load Dataset
import numpy as np
import pandas as pd

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)

# Lib Load Data Visualization
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Lib Load Preprocessing Data
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Lib Load Neural Networks
import tensorflow as tf
from keras.layers import LSTM
from keras.layers import GRU

from tensorflow.python.keras.layers import SimpleRNNCell
from tensorflow.python.keras.layers import RNN

# Lib Evaluate Models
import scipy.stats as sc
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import root_mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

# Set Random Number
import random as rm
rm.seed(1234)

# Set Random Number
import numpy as np
np.random.seed(1234)

# Set Random Number
import tensorflow as tf
tf.random.set_seed(1234)

# Function to create empty space
def add_empty_lines(num_lines):
    """
    Added blank lines to Streamlit
    Parameters:
        num_lines (int): The desired number of blank lines
    """
    for _ in range(num_lines):
        st.text("")  # Adds a blank line with blank text


# Config Web Streamlit
st.set_page_config(page_title="My Dashboard", layout="wide")

# Container Header
st.markdown('## Prediction of Cryptocurrency using Neural Network Algorithm')


col1, col2, col3 = st.columns(([0.3, 0.25, 0.45]), gap='small')
with col1:
    st.info("Config Dataset")
    with st.form("my_form"):
        ticker = st.selectbox('Choose a Cryptocurrency', ['BTC-USD','ETH-USD','BNB', 'GOOG', 'INTC', 'AAPL'])
        start_date = st.date_input(label="Start Date", value=None, min_value=None, max_value=None)
        end_date = st.date_input(label="End Date", value=None, min_value=None, max_value=None)
        reset = st.form_submit_button(label="Reset", use_container_width=True)
        submit = st.form_submit_button(label="Submit", type="secondary", help="", use_container_width=True)
        add_empty_lines(1)

with col2:
    st.info("Top Three Cryptocurrency")
    st.metric(label="1. Bitcoin      (BTC)", value="", delta_color="off")
    st.metric(label="2. Etherium     (ETH)", value="", delta_color="off")
    st.metric(label="3. Binance Coin (BNB)", value="", delta_color="off")

with col2:
    st.info("Top Three Stock Price on Market")
    st.metric(label="1. Google       (GOOG)", value="", delta_color="off")
    st.metric(label="2. Intel        (INTC)", value="", delta_color="off")
    st.metric(label="3. Apple        (AAPL)", value="", delta_color="off")
    add_empty_lines(5)

with col3:
    st.info("Exploration Data Analysis")

    if submit:
        ticker      = ticker
        start_date  = start_date
        end_date    = end_date

    else:
        ticker      = "BTC-USD"
        start_date  = "2015-01-01"
        end_date    = "2024-05-01"

    if reset:
        ticker      = "BTC-USD"
        start_date  = "2015-01-01"
        end_date    = "2024-05-01"

    dataset = getData(ticker, start_date, end_date)

    # Split two tab-index
    tab1, tab2 = st.tabs(["Visualization Data", "Historical Data"])
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(dataset["Date"], dataset["Open"], color="tab:green", label="Open", linewidth=2)
    ax.plot(dataset["Date"], dataset["High"], color="tab:orange", label="High", linewidth=2)
    ax.plot(dataset["Date"], dataset["Low"], color="tab:red", label="Low", linewidth=2)
    ax.plot(dataset["Date"], dataset["Close"], color="tab:blue", label="Close", linewidth=2)

    ax.set_title('')
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.legend(loc="best")
    ax.grid(True)

    plt.tight_layout()
    
    
    tab1.pyplot(fig, use_container_width=True)
    # plt.show()

    tab2.dataframe(dataset, use_container_width=True)
    add_empty_lines(0)


with col1:
    avs.add_vertical_space(2)
    st.info("Config Dataset")
    with st.form("my_config"):
        algorithm = st.selectbox('Choose Algorithm', ['RNN','LSTM','GRU'])
        optimizer = st.selectbox('Choose Optimizer', ['Adam','Adamax','RMSProp', 'SGD'])
        batch_size = int(st.selectbox('Choose Batch Size', ['8','16','24', '32']))
        epoch = int(st.selectbox('Choose Epoch', ['25','50','75', '100']))
        apply = st.form_submit_button(label="Apply", type="secondary", help="", use_container_width=True)


with col2:
    avs.add_vertical_space(2)
    st.info("Evaluation Models")




    # Choose Feature : Close Price
    data = dataset.filter(["Close"])
    data = data.values
    np.round(data[:5],6)

    # Normalize Features
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(np.array(data).reshape(-1,1))



    # Train & Test Data
    train_data, test_data = train_test_split(scaled, train_size=0.8, test_size=0.2, shuffle=False)

    # Function for Supervised Learning
    def create_dataset(look_back, dataset):

        # Declare Variable X & Y
        dataX = []
        dataY = []

        # For loop for create supervised learning
        for i in range(look_back, len(dataset)):
            dataX.append(dataset[i-look_back:i, 0])
            dataY.append(dataset[i, 0])

        # Return value X and Y
        return np.array(dataX), np.array(dataY)
    
    # Supervised Learning
    x_train, y_train = create_dataset(60, train_data)

    # Supervised Learning
    x_test, y_test = create_dataset(60, test_data)

    # Reshape Input to be Sample, Time Step, and Feature
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))



    # Measuring Execution Time
    start_time = tm.time()

    # Set Parameter Tuning
    # optimizers = optimizer    
    # batch_size = batch_size       
    # epoch      = epoch             

    # 1. Build Model : LSTM Architecture
    tf.keras.backend.clear_session()
    model = tf.keras.Sequential([
        tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))),
        tf.keras.layers.Bidirectional(LSTM(units=50, return_sequences=False)),
        tf.keras.layers.Dropout(0.05),
        tf.keras.layers.Dense(1)
    ])

    # 2. Compile Models
    model.compile(optimizer=optimizer, loss="mean_squared_error")

    # 3. Fitting Models
    history = model.fit(
        x=x_train, y=y_train,
        batch_size=batch_size, epochs=epoch, verbose=1,
        validation_data=(x_test, y_test),
        shuffle=False, use_multiprocessing=True,
    )

    # 4. Model Predictions
    predictions = model.predict(x_test, verbose=0)

    # Measuring Execution Time
    end_time = tm.time()

    # Calculating the Total Execution Time
    execution_time = end_time - start_time


    # Function
    def evaluate_models(ytrue, ypred):

        # Calculate R & MAPE
        r    = sc.mstats.pearsonr(ytrue,ypred)[0]
        mape = mean_absolute_percentage_error(ytrue,ypred)

        # Return Values
        return np.round(r,4), np.round(mape,4)
    

    # Calculate Error
    r, mape = evaluate_models(y_test, predictions)
    # print("r    : "+str(np.round(r, 4)))
    # print("mape : "+str(np.round(mape, 4)))
    # print("Time : "+"{:,.2f}".format(execution_time))

    # Add the evaluation results to the dataset as new columns
    dataset['r'] = r
    dataset['mape'] = mape
    dataset['execution_time'] = execution_time
    dataset['algorithm'] = algorithm
    dataset['optimizer'] = optimizer
    dataset['batch_size'] = batch_size
    dataset['epoch'] = epoch

    if apply:
        # st.write(f"Algorithm selected: {algorithm}")
        # st.write(f"Optimizer selected: {optimizer}")
        # st.write(f"Batch size selected: {batch_size}")
        # st.write(f"Epoch selected: {epoch}")
        # st.write(f"r: {r}")
        # st.write(f"mape: {mape}")
        # st.write(f"Execution Time: {execution_time:.2f} seconds")


        # Grouping dataset based on the results
        df_grouped1 = dataset.groupby(by=["algorithm", "optimizer", "batch_size", "epoch"]).size() # .reset_index(name="output")
        df_grouped2 = dataset.groupby(by=["r", "mape", "execution_time"]).size().reset_index(name="output")

        # Display grouped DataFrame
        st.write(f"###### Pengelompokan berdasarkan r, mape, dan execution time")
        st.dataframe(df_grouped1)  # Display interactive table
        st.dataframe(df_grouped2)  # Display interactive table

    else:
        # Menentukan nilai default jika apply belum ditekan
        algorithm = 'RNN'  # Default
        optimizer = 'Adam'  # Default
        batch_size = 32  # Default
        epoch = 1  # Default

        # Menambahkan hasil evaluasi ke dataset sebagai kolom baru
        dataset['algorithm'] = algorithm
        dataset['optimizer'] = optimizer
        dataset['batch_size'] = batch_size
        dataset['epoch'] = epoch

        # Melakukan pengelompokan berdasarkan opsi yang dipilih
        df_grouped = None  # Inisialisasi DataFrame kosong

        # Melakukan pengelompokan berdasarkan opsi yang dipilih
        if algorithm in ['RNN', 'LSTM', 'GRU']:
            df_groupedd = dataset.groupby(by=["algorithm", "optimizer", "batch_size", "epoch"]).size()
            df_grouped = dataset.groupby(by=["r", "mape", "execution_time"]).size().reset_index(name="jumlah")
        elif optimizer in ['Adam', 'Adamax', 'RMSProp', 'SGD']:
            df_groupedd = dataset.groupby(by=["algorithm", "optimizer", "batch_size", "epoch"]).size()
            df_grouped = dataset.groupby(by=["r", "mape", "execution_time"]).size().reset_index(name="jumlah")
        elif batch_size in ['8', '16', '24', '32']:
            df_groupedd = dataset.groupby(by=["algorithm", "optimizer", "batch_size", "epoch"]).size()
            df_grouped = dataset.groupby(by=["r", "mape", "execution_time"]).size().reset_index(name="jumlah")
        elif epoch in ['25', '50', '75', '100']:
            df_groupedd = dataset.groupby(by=["algorithm", "optimizer", "batch_size", "epoch"]).size()
            df_grouped = dataset.groupby(by=["r", "mape", "execution_time"]).size().reset_index(name="jumlah")

        # Tampilkan DataFrame jika pengelompokan berhasil
        if df_grouped is not None:
            st.write(f"###### Pengelompokan berdasarkan r, mape, dan execution time")
            st.dataframe(df_grouped)  # Menampilkan tabel interaktif
        else:
            st.warning("Pengelompokan tidak valid, periksa opsi yang dipilih.")




with col3:
    avs.add_vertical_space(2)
    st.info("Result Prediction")


    # Split two tab-index
    tab1, tab2 = st.tabs(["Visualization Data", "Historical Data"])

    # Create Figure with Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(history.epoch, history.history["loss"], label="training", linewidth=2.5)
    ax.plot(history.epoch, history.history["val_loss"], label="validation", linewidth=2.5)

    # Set Labels
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("", fontsize=12)
    ax.legend(loc="best")
    ax.grid(True)

    # Return Values
    plt.tight_layout()
    tab1.pyplot(fig, use_container_width=True)
    # plt.show()


    # Create Figure with Matplotlib
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dataset[["Date"]].iloc[len(y_train)+120:], y_test,
            label="actual_data", linewidth=2.5)
    ax.plot(dataset[["Date"]].iloc[len(y_train)+120:], predictions,
            label="result_prediction", linewidth=2.5)

    # Set Labels
    ax.xaxis.set_major_formatter(DateFormatter("%Y"))
    ax.set_title("", fontsize=12)
    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("", fontsize=12)
    ax.legend(loc="best")
    ax.grid(True)

    # Return Values
    plt.tight_layout()
    tab2.pyplot(fig, use_container_width=True)
    # plt.show()