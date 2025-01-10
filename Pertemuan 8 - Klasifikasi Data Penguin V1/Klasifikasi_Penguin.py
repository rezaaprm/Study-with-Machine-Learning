# Library utama
import pandas as pd
import numpy as np
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Lib data preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Lib supervised learning
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Lib evaluation model
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Additional
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from streamlit_navigation_bar import st_navbar
import time
from streamlit_extras.let_it_rain import rain
from st_aggrid import AgGrid, GridOptionsBuilder


st.set_page_config(layout="wide")
dataset = sns.load_dataset("penguins")

page = st_navbar(["Klasifikasi", "Visualisasi", "Data"])

# Config Web
# st.balloons()

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



st.title("Klasifikasi Dataset Penguin")

# info = "______________________________________________________________________"
info = "_______________________________________________________________________________________________________________________"
info = f"<p style='font-size:20px;'>{info}</p>"
st.markdown(info, unsafe_allow_html=True)


# nav = st.radio("Navigasi", ["Klasifikasi", "Data"])
# st.write(page)


# Page 1 : Classification
if page == "Klasifikasi":

    st.write("""
    # 1 Dataset
            """)

    nama_dataset = st.sidebar.selectbox(
        'Dataset',
        ('Penguin')
    )

    st.write(f"## Dataset {nama_dataset}")

    algoritma = st.sidebar.selectbox(
        'Algoritma',
        ('KNN', 'NB')
    )

    def pilih_dataset(nama):
        data = None
        if nama == 'Penguin':
            data = datasets.load_dataset("penguins")
        else:
            data = datasets.load_digits()
        X = data.data
        y = data.target
        return X,y

    def tambah_parameter(nama_algoritma):
        params = dict()
        if nama_algoritma == 'KNN':
            K = st.sidebar.slider('K', 1, 15)
            params['K'] = K
        elif nama_algoritma == 'NB':
            C = st.sidebar.slider('C', 0.01, 10.0)
            params['C'] = C
        else:
            max_depth = st.sidebar.slider('max_depth', 2, 15)
            params['max_depth'] = max_depth
            n_estimators = st.sidebar.slider('n_estimators', 1, 100)
            params['n_estimators'] = n_estimators
        return params


    params = tambah_parameter(algoritma)

    def pilih_klasifikasi(nama_algoritma, params):
        algo = None
        if nama_algoritma == 'KNN':
            algo = KNeighborsClassifier(n_neighbors=params['K'])
        elif nama_algoritma == 'NB':
            algo = GaussianNB
            return GaussianNB()
            # params['C'] = C
            # (C=params['C'])
        
        return algo
        
    ## Classifier
    algo = pilih_klasifikasi(algoritma, params)

    ## Preprocessing
    dataset = dataset.dropna()

    ## Proses Klasifikasi
    dataset["species"] = dataset['species'].replace({
        'Adelie':0, 'Chinstrap':1, 'Gentoo':2
    })
    dataset["island"] = dataset['island'].replace({
        'Torgersen':0, 'Biscoe':1, 'Dream':2
    })
    dataset["sex"] = dataset['sex'].replace({
        'Male': 0, 'Female': 1
    })

    # Feature
    x = dataset[["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]].values
    y = dataset["sex"].values

    # Split Validation
    trainX, testX, trainY, testY = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=7, shuffle=True)
    # Show dimension of data train
    print(trainX.shape, trainY.shape)
    # Show dimension of data test
    print(testX.shape, testY.shape)

    algo.fit(trainX, trainY)
    y_pred = algo.predict(testX)

    ## Evaluate
    acc = accuracy_score(testY, y_pred)

    st.write(f'Algoritma = {algoritma}')
    st.write(f'Akurasi = ', acc)


    ## Plot Dataset
    pca = PCA(2)
    X_projected = pca.fit_transform(x)

    x1 = X_projected[:, 0]
    x2 = X_projected[:, 1]

    fig, ax = plt.subplots()
    scatter = ax.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')
    legend1 = ax.legend(*scatter.legend_elements(), title="Sex")

    fig = plt.figure()
    plt.scatter(x1, x2, c=y, alpha=0.8, cmap='viridis')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar()

    st.pyplot(fig)

# Page 2 : Visualization
elif page == "Visualisasi":
    
    col1, col2, col3, col4, col5 = st.columns([0.2, 0.2, 0.2, 0.2, 0.2], gap="small")

    # Plot 1
    with col1:
        fig, ax = plt.subplots()
        sns.countplot(data=dataset, x="sex", hue="sex", ax=ax)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()
    
    # Plot 2
    with col2:
        fig, ax = plt.subplots()
        sns.countplot(data=dataset, x="species", ax=ax)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()
    
    # Plot 3
    with col3:
        df = dataset.groupby(by=["species", "sex"]).size().reset_index(name="jumlah")
        fig, ax = plt.subplots()
        sns.barplot(data=df, x="species", y="jumlah", hue="sex", ax=ax)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()
    
    # Plot 4
    with col4:
        df = dataset.groupby(by=["species", "island"]).size().reset_index(name="jumlah")
        fig, ax = plt.subplots()
        sns.barplot(data=df, x="species", y="jumlah", hue="island", ax=ax)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()
    
    # Plot 5
    with col5:
        df = dataset.groupby(by=["sex", "island"]).size().reset_index(name="jumlah")
        fig, ax = plt.subplots()
        sns.barplot(data=df, x="island", y="jumlah", hue="sex", ax=ax)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()


    col1, col2, col3 = st.columns([0.333, 0.333, 0.333], gap="small")

    dataset = dataset.ffill()

    dataset["species"] = dataset['species'].replace({'Adelie':0, 'Chinstrap':1, 'Gentoo':2})
    dataset["island"] = dataset['island'].replace({'Torgersen':0, 'Biscoe':1, 'Dream':2})
    x = dataset[["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]].values
    y = dataset["sex"].values
    trainX, testX, trainY, testY = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=7, shuffle=True)

    # Plot 1
    with col2:
        fig, ax = plt.subplots(figsize=(8,4))
        sns.heatmap(dataset.corr(numeric_only=True), vmin = -1, vmax = 1, center = 0, cmap="YlGnBu", annot=True, linewidths=0.5)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()

    # Plot 2
    with col1:
        fig, ax = plt.subplots(figsize=(6,5))
        
        Proses_KNN = KNeighborsClassifier(n_neighbors=2).fit(trainX, trainY)
        Hasil_KNN = Proses_KNN.predict(testX)
        confusion_KNN = confusion_matrix(testY, Hasil_KNN)
        sns.heatmap(confusion_KNN, cmap="viridis", annot=True, linewidths=1, vmin=0, vmax=100)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()

    # Plot 3
    with col3:
        fig, ax = plt.subplots(figsize=(6,5))

        Hasil_NB = GaussianNB().fit(trainX, trainY).predict(testX)
        confusion_NB = confusion_matrix(testY, Hasil_NB)
        sns.heatmap(confusion_NB, cmap="viridis", annot=True, linewidths=1, vmin=0, vmax=100)
        st.pyplot(fig)
        # plt.tight_layout()
        # plt.show()

# Page 3 : Data
elif page == "Data":
    st.write("## Dataset Penguin")
    
    col1, col2 = st.columns([1, 1], gap="large")


    with col1:
        st.write("Berikut adalah data dari dataset Penguin yang digunakan")
        st.write(dataset)
        
    with col2:
        st.write("Describe dataset Penguin")
        st.write(dataset.describe())

    st.info("")
    
    col1, col2, col3 = st.columns([0.25, 0.25, 0.5], gap="small")

    with col1:

        # nav = st.radio("Kategori", ["Species/Sex", "Species/Island", "Sex/Island"])

        # Data yang digunakan
        data = {
            'Kategori': ['Kategori 1', 'Kategori 2', 'Kategori 3'],
            'Opsi': ['Species-Sex', 'Species-Island', 'Sex-Island']
        }

        # Membuat DataFrame
        df = pd.DataFrame(data)

        # Judul aplikasi
        st.write('###### Pilih kategori filter data Penguin')

        # Tampilkan dataframe dengan event seleksi
        event = st.dataframe(
            df,
            on_select='rerun',  # Event untuk memilih data
            selection_mode='single-row'  # Pilihan satu baris
        )

        # Cek apakah ada baris yang dipilih
        if len(event.selection['rows']):
            selected_row = event.selection['rows'][0]  # Ambil baris yang dipilih
            kategori = df.iloc[selected_row]['Kategori']  # Ambil nilai kategori
            opsi = df.iloc[selected_row]['Opsi']  # Ambil nilai opsi

            # Menyimpan data yang dipilih dalam session state
            st.session_state['category_data'] = {'Kategori': kategori, 'Opsi': opsi}

            # Menampilkan informasi pilihan dan memberikan link ke halaman detail
            st.write(f'{kategori} = {opsi}')

    with col2:
    
        if 'category_data' in st.session_state:
            kategori = st.session_state['category_data']['Kategori']
            opsi = st.session_state['category_data']['Opsi']
            
            # Berdasarkan opsi yang dipilih, melakukan pengelompokan dataset
            if opsi == "Species-Sex":
                # Lakukan grouping berdasarkan species dan sex (misalnya dataset adalah 'penguins')
                df_grouped = dataset.groupby(by=["species", "sex"]).size().reset_index(name="jumlah")
            elif opsi == "Species-Island":
                df_grouped = dataset.groupby(by=["species", "island"]).size().reset_index(name="jumlah")
            elif opsi == "Sex-Island":
                df_grouped = dataset.groupby(by=["sex", "island"]).size().reset_index(name="jumlah")

            # Menampilkan pengelompokan berdasarkan opsi yang dipilih
            st.write(f"###### Pengelompokan berdasarkan {opsi}")
            st.write(df_grouped)

    with col3:

        #--- Init session_state
        if 'active_page' not in st.session_state:
            st.session_state.active_page = 'Home'
            st.session_state.slider1 = 0
            st.session_state.check1 = False

        #--- Payload code of each page
        def home():
            st.write('Welcome to download page')
            
            check = st.checkbox('Check me', key='check1')

            if check:
                link = '[Kaggle](https://www.kaggle.com/code/rv1922/penguins-analysis-eda/input?scriptVersionId=191134290)'
                st.markdown(link, unsafe_allow_html=True)
            else:
                st.warning('Please check the box first before downloading.')


            if st.button('Click Here'):
                if not check:
                    st.warning('Please check the box first before downloading.')
                else:
                    st.write('You can now download the file.')

        # def slider():
        #     st.write('Welcome to the slider page')
        #     slide1 = st.slider('this is a slider',min_value=0,max_value=15,key='slider1' )    
        #     st.write('Slider position:',slide1)
            
        def contact():
            st.title('Welcome to contact page')
            if st.button('Click Contact'):
                link2 = '[Kaggle Contact](https://www.kaggle.com/rv1922)'
                st.markdown(link2, unsafe_allow_html=True)
                st.write('Welcome to contact page')

        #--- Callback functions
        def CB_HomeButton():
            st.session_state.active_page = 'Home'

        # def CB_SliderButton():
        #     st.session_state.active_page = 'Slider'

        def CB_ContactButton():
            st.session_state.active_page = 'Contact'
            
        #--- Page selection buttons
        col1, col2, col3 = st.columns(3)
        col1.button('Home', on_click=CB_HomeButton)
        # col2.button('Slider', on_click=CB_SliderButton)
        col3.button('Contact', on_click=CB_ContactButton)
        st.write('____________________________________________________________________')


        #--- Run the active page
        if   st.session_state.active_page == 'Home':
            home()
        # elif st.session_state.active_page == 'Slider':
        #     slider()
        elif st.session_state.active_page == 'Contact':
            contact()
        
    st.info("")

    st.write(f"###### Data yang mengandung atribut NULL")
    filtered_dataset = dataset[dataset.isnull().any(axis=1)]
    AgGrid(
        filtered_dataset.tail(13),
        gridOptions=GridOptionsBuilder.from_dataframe(filtered_dataset).build(), fit_columns_on_grid_load=True
    )
## -