# Proyek Analisis Data: Bike Sharing
# Nama : [Shakira Angelina Ika Putri]
# Email: [mc254d5x0781@student.devacademy.id]
# ID Dicoding: [MC254D5X0781]

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Memuat dataset
day_data = pd.read_csv("day.csv")
hour_data = pd.read_csv("hour.csv")

# Mengonversi kolom tanggal
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# Judul Aplikasi Streamlit
st.title("📊 Dashboard Bike Sharing by: MC254D5X0781")
st.sidebar.header("🔎 Filter Data")

# Filter di sidebar
selected_season = st.sidebar.selectbox("Pilih Musim:", ['Semua', 'Spring', 'Summer', 'Fall', 'Winter'])
selected_workingday = st.sidebar.selectbox("Pilih Hari Kerja / Libur:", ['Semua', 'Hari Kerja', 'Hari Libur'])

# Memetakan filter ke dataset
df_filtered = day_data.copy()
if selected_season != 'Semua':
    season_map = {'Spring': 1, 'Summer': 2, 'Fall': 3, 'Winter': 4}
    df_filtered = df_filtered[df_filtered['season'] == season_map[selected_season]]
if selected_workingday != 'Semua':
    work_map = {'Hari Kerja': 1, 'Hari Libur': 0}
    df_filtered = df_filtered[df_filtered['workingday'] == work_map[selected_workingday]]

# Ringkasan Data
st.subheader("📌 Ringkasan Data Penyewaan Sepeda")
st.write(df_filtered.describe())

# =====================================================================
# 1️⃣ Pola Penyewaan Sepeda: Hari Kerja vs. Hari Libur
st.header("1. Pola Penyewaan Sepeda: Hari Kerja vs. Hari Libur")
workingday_counts = day_data.groupby('workingday')['cnt'].mean().reset_index()
workingday_counts['Kategori Hari'] = workingday_counts['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})
fig1 = px.bar(workingday_counts, x='Kategori Hari', y='cnt', color='Kategori Hari',
              labels={'cnt': 'Rata-rata Penyewaan Sepeda', 'Kategori Hari': 'Kategori Hari'},
              title='Perbandingan Penyewaan di Hari Kerja vs. Libur',
              hover_name='Kategori Hari', hover_data={'cnt': True})
st.plotly_chart(fig1)

# =====================================================================
# 2️⃣ Jam Sibuk Penyewaan Sepeda
st.header("2. Jam Sibuk Penyewaan Sepeda")
hourly_counts = hour_data.groupby('hr')['cnt'].mean().reset_index()
fig2 = px.line(hourly_counts, x='hr', y='cnt', markers=True,
               labels={'cnt': 'Rata-rata Penyewaan Sepeda', 'hr': 'Jam dalam Sehari'},
               title='Tren Penyewaan Sepeda Berdasarkan Jam',
               hover_name='hr', hover_data={'cnt': True})
st.plotly_chart(fig2)

# =====================================================================
# 3️⃣ Pengaruh Cuaca terhadap Penyewaan Sepeda
st.header("3. Pengaruh Cuaca terhadap Penyewaan Sepeda")
weather_counts = day_data.groupby(['weathersit', 'season'])['cnt'].mean().reset_index()
weather_counts['Kondisi Cuaca'] = weather_counts['weathersit'].map({1: 'Cerah', 2: 'Berkabut', 3: 'Hujan Ringan', 4: 'Hujan Lebat'})
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_counts['Musim'] = weather_counts['season'].map(season_map)
fig3 = px.bar(weather_counts, x='Kondisi Cuaca', y='cnt', color='Musim',
              barmode='group', labels={'cnt': 'Rata-rata Penyewaan', 'Kondisi Cuaca': 'Kondisi Cuaca'},
              title='Dampak Cuaca dan Musim terhadap Penyewaan Sepeda',
              hover_name='Kondisi Cuaca', hover_data={'cnt': True})
st.plotly_chart(fig3)

# =====================================================================
# Insight Kesimpulan
st.subheader("📌 Insight")
st.markdown("**Insight Pertanyaan 1:** Penyewaan sepeda lebih tinggi pada hari kerja dibandingkan hari libur, menunjukkan bahwa sepeda digunakan sebagai alat transportasi utama.")
st.markdown("**Insight Pertanyaan 2:** Puncak penyewaan terjadi pada pagi (08:00) dan sore (17:00 - 18:00), menunjukkan pola commuting pekerja dan pelajar.")
st.markdown("**Insight Pertanyaan 3:** Penyewaan sepeda tertinggi terjadi pada cuaca cerah, sedangkan hujan atau kabut cenderung menurunkan jumlah penyewaan.")
