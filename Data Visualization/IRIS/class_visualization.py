# class_visualization.py

import plotly.express as px
import plotly.graph_objects as go

def barplot(series, title):
    """
    Fungsi untuk membuat barplot menggunakan Plotly.
    """
    fig = px.bar(series, title=title)
    return fig

def heatmap(df, title):
    """
    Fungsi untuk membuat heatmap menggunakan Plotly.
    """
    # Pilih hanya kolom numerik untuk korelasi
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    fig = px.imshow(numeric_df.corr(), title=title)
    return fig

def scatter(df, x_column, y_column, title):
    """
    Fungsi untuk membuat scatterplot menggunakan Plotly.
    """
    fig = px.scatter(df, x=x_column, y=y_column, color='Species', title=title)
    return fig

def histogram(df, column, title):
    """
    Fungsi untuk membuat histogram menggunakan Plotly.
    """
    fig = px.histogram(df, x=column, color='Species', title=title)
    return fig

def boxplot(df, category_column, value_column, title):
    """
    Fungsi untuk membuat boxplot menggunakan Plotly.
    """
    fig = px.box(df, x=category_column, y=value_column, color=category_column, title=title)
    return fig
