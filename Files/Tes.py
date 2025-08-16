# # Library utama
# import pandas as pd
# import numpy as np
# import streamlit as st

# import matplotlib.pyplot as plt
# import seaborn as sns

# # Lib data preprocessing
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.model_selection import train_test_split

# # Lib supervised learning
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC

# # Lib evaluation model
# from sklearn.metrics import classification_report, confusion_matrix
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# # Additional
# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.decomposition import PCA

# # # Home.py
# # if st.session_state.active_page == "Corpus":
# #     corpus()
# # elif st.session_state.active_page == "ChatBot":
# #     chatbot()
# # elif st.session_state.active_page == "Analytics":
# #     analytics()

# # # sites.Corpus.py
# # if scrape_btn:
# #     with st.spinner('Loading articles...'):
# #         st.session_state.sd.scrape_articles()
# #     st.session_state.active_page = "ChatBot"   
# #     st.experimental_rerun()

# # Import Library
# import pandas as pd
# import numpy as np
# import streamlit as st

# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import plotly.graph_objects as go

# from sklearn.preprocessing import MinMaxScaler
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.decomposition import PCA
# from sklearn.metrics import accuracy_score

# from streamlit_extras.let_it_rain import rain
# import time

# # Load dataset
# dataset = sns.load_dataset("penguins").dropna()

# # Navigation
# page = st.radio("Navigasi", ["Klasifikasi", "Visualisasi", "Data"])

# # Config Web
# rain(emoji="☀️", font_size=3, falling_speed=3, animation_length="infinite")
# st.title("Klasifikasi Dataset Penguin")

# # Navigasi berdasarkan pilihan
# if page == "Klasifikasi":
#     st.write("## Dataset Penguin")

#     # Pilih algoritma
#     algoritma = st.sidebar.selectbox('Algoritma', ('KNN', 'NB'))
    
#     # Konfigurasi parameter berdasarkan algoritma
#     def tambah_parameter(nama_algoritma):
#         params = {}
#         if nama_algoritma == 'KNN':
#             params['K'] = st.sidebar.slider('K', 1, 15)
#         return params

#     params = tambah_parameter(algoritma)
    
#     # Pilih classifier berdasarkan algoritma
#     def pilih_klasifikasi(nama_algoritma, params):
#         if nama_algoritma == 'KNN':
#             return KNeighborsClassifier(n_neighbors=params['K'])
#         elif nama_algoritma == 'NB':
#             return GaussianNB()
    
#     algo = pilih_klasifikasi(algoritma, params)
    
#     # Preprocessing
#     dataset["species"] = dataset['species'].map({'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2})
#     dataset["island"] = dataset['island'].map({'Torgersen': 0, 'Biscoe': 1, 'Dream': 2})
#     dataset["sex"] = dataset['sex'].map({'Male': 0, 'Female': 1})
    
#     # Feature dan label
#     x = dataset[["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]].values
#     y = dataset["sex"].values
    
#     # Split data
#     trainX, testX, trainY, testY = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=7, shuffle=True)
    
#     # Training model
#     algo.fit(trainX, trainY)
#     y_pred = algo.predict(testX)
    
#     # Evaluasi
#     acc = accuracy_score(testY, y_pred)
#     st.write(f'Algoritma = {algoritma}')
#     st.write(f'Akurasi = {acc}')
    
#     # Visualisasi PCA
#     pca = PCA(2)
#     X_projected = pca.fit_transform(x)
#     x1 = X_projected[:, 0]
#     x2 = X_projected[:, 1]
    
#     fig, ax = plt.subplots()
#     scatter = ax.scatter(x1, x2, c=y, cmap='viridis')
#     ax.legend(*scatter.legend_elements(), title="Sex")
#     plt.colorbar(scatter)
#     st.pyplot(fig)

# elif page == "Visualisasi":
#     col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    
#     # Plot 1
#     with col1:
#         fig, ax = plt.subplots()
#         sns.countplot(data=dataset, x="sex", hue="sex", ax=ax)
#         st.pyplot(fig)
    
#     # Plot 2
#     with col2:
#         fig, ax = plt.subplots()
#         sns.countplot(data=dataset, x="species", ax=ax)
#         st.pyplot(fig)
    
#     # Plot 3
#     with col3:
#         df = dataset.groupby(by=["species", "sex"]).size().reset_index(name="jumlah")
#         fig, ax = plt.subplots()
#         sns.barplot(data=df, x="species", y="jumlah", hue="sex", ax=ax)
#         st.pyplot(fig)
    
#     # Plot 4
#     with col4:
#         df = dataset.groupby(by=["species", "island"]).size().reset_index(name="jumlah")
#         fig, ax = plt.subplots()
#         sns.barplot(data=df, x="species", y="jumlah", hue="island", ax=ax)
#         st.pyplot(fig)
    
#     # Plot 5
#     with col5:
#         df = dataset.groupby(by=["sex", "island"]).size().reset_index(name="jumlah")
#         fig, ax = plt.subplots()
#         sns.barplot(data=df, x="island", y="jumlah", hue="sex", ax=ax)
#         st.pyplot(fig)

# elif page == "Data":
#     st.write("## Dataset Penguin")
#     st.write(dataset)
    
#     # Pengelompokan kategori
#     nav = st.radio("Kategori", ["Species/Sex", "Species/Island", "Sex/Island"])
#     if nav == "Species/Sex":
#         df = dataset.groupby(by=["species", "sex"]).size().reset_index(name="jumlah")
#     elif nav == "Species/Island":
#         df = dataset.groupby(by=["species", "island"]).size().reset_index(name="jumlah")
#     elif nav == "Sex/Island":
#         df = dataset.groupby(by=["sex", "island"]).size().reset_index(name="jumlah")
    
#     st.write(f"#### Pengelompokan berdasarkan {nav}")
#     st.write(df)
