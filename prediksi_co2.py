import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load model yang telah dilatih
model = pickle.load(open('prediksi_co2.sav', 'rb'))

# Membaca dataset
df = pd.read_excel("CO2 dataset.xlsx")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')  # Format tahun yang benar
df.set_index(['Year'], inplace=True)

# Judul aplikasi
st.title('Forecasting Kualitas Udara')

# Slider untuk memilih berapa tahun prediksi
year = st.slider("Tentukan Tahun", 1, 30, step=1)

# Prediksi menggunakan model
if st.button("Predict"):
    # Menggunakan model untuk melakukan prediksi (pastikan model memiliki metode forecast)
    pred = model.forecast(year)
    pred = pd.DataFrame(pred, columns=['CO2'])

    # Menampilkan hasil prediksi dan grafik
    col1, col2 = st.columns([2, 3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        # Plot data yang sudah ada (historical)
        df['CO2'].plot(style='--', color='gray', legend=True, label='Known Data')
        # Plot hasil prediksi
        pred['CO2'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)
