import pandas as pd
import yfinance as yf

# Func Get Crypto
@staticmethod
def getData(ticker, start_date, end_date):
    # Set the ticker and datetime
    dataset = yf.Ticker(ticker).history(start=start_date, end=end_date).reset_index()

    # Set the feature
    dataset = dataset[["Date", "Open", "High", "Low", "Close"]]
    dataset["Date"] = pd.to_datetime(dataset["Date"]).dt.date
    
    # Return values
    return dataset