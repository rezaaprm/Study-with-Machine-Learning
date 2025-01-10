# Main Library
import numpy as np 
import pandas as pd 

# Library for Data Preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


def normalize(dataset):

    # Set Features & Target
    x = dataset[["sepal_length", "sepal_width", "petal_length", "petal_width"]].values
    y = dataset["species"]

    # Normalizing Data
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled = np.round(scaler.fit_transform(x), 5)

    # Concatinate Data
    df1 = pd.DataFrame(data=scaled, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    df2 = pd.DataFrame(data=y, columns=["species"])
    df_normalize = pd.concat([df1, df2], axis=1)

    # Return Values
    return df_normalize