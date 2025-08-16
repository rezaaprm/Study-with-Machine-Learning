import pandas as pd
from sklearn.preprocessing import StandardScaler

def getDataset(file_path):
    """
    Fungsi untuk memuat dataset dari file CSV.
    """
    return pd.read_csv(file_path)

def normalized(df):
    # Pisahkan kolom numerik dan kategorikal
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    # Normalisasi hanya kolom numerik
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Gabungkan kembali kolom kategorikal
    df[categorical_cols] = df[categorical_cols]

    return df
