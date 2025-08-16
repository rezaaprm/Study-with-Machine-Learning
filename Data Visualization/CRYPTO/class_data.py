# lib getdataset from yahoo
import yfinance as yf

# lib manipulation dataset
import pandas as pd
import numpy as np

# func getData by csv file
def getData(ticker, startDate, endDate):

    # set the ticker and datetime
    dataset = ticker.history(start=startDate, end=endDate).reset_index()

    # set the feature
    dataset = dataset[["Date", "Open", "High", "Low", "Close"]]

    # convert datetime format
    dataset["Date"] = pd.to_datetime(dataset["Date"], format="%d-%m-%Y")

    # return values
    return dataset
