# Proyek Analisis Data: Bike Sharing
# Nama : [Shakira Angelina Ika Putri]
# Email: [mc254d5x0781@student.devacademy.id]
# ID Dicoding: [MC254D5X0781]

import streamlit as st
import pandas as pd
import plotly.express as px

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

# Visualisasi: Rata-rata Penyewaan Sepeda per Musim
st.subheader("🌤️ Rata-rata Penyewaan Sepeda Berdasarkan Musim")
fig = px.bar(day_data, x='season', y='cnt', color='season', 
             labels={'season': 'Musim', 'cnt': 'Jumlah Penyewaan'}, 
             title="Penyewaan Sepeda Berdasarkan Musim",
             hover_data=['cnt'])
fig.update_xaxes(tickvals=[1, 2, 3, 4], ticktext=['Spring', 'Summer', 'Fall', 'Winter'])
st.plotly_chart(fig)

# Visualisasi: Penyewaan Sepeda Berdasarkan Hari Kerja vs. Hari Libur
st.subheader("📅 Penyewaan Sepeda Berdasarkan Hari Kerja vs. Libur")
fig = px.bar(day_data, x='workingday', y='cnt', color='workingday', 
             labels={'workingday': 'Kategori Hari', 'cnt': 'Jumlah Penyewaan'},
             title="Perbandingan Penyewaan di Hari Kerja vs. Libur",
             hover_data=['cnt'])
fig.update_xaxes(tickvals=[0, 1], ticktext=['Hari Libur', 'Hari Kerja'])
st.plotly_chart(fig)

# Visualisasi: Pola Penyewaan Sepeda Berdasarkan Jam (Dirapikan)
st.subheader("🕒 Pola Penyewaan Sepeda Berdasarkan Jam")
df_hour_avg = hour_data.groupby('hr', as_index=False)['cnt'].mean()
fig = px.line(df_hour_avg, x='hr', y='cnt', markers=True, 
              labels={'hr': 'Jam', 'cnt': 'Jumlah Penyewaan Rata-rata'},
              title="Tren Rata-rata Penyewaan Sepeda Harian",
              hover_data=['cnt'])
fig.update_traces(line=dict(width=2), marker=dict(size=6))
st.plotly_chart(fig)

# Insight Kesimpulan
st.subheader("📌 Insight dan Kesimpulan")
st.markdown("- Penyewaan sepeda lebih tinggi pada hari kerja dibandingkan hari libur, menunjukkan bahwa sepeda digunakan sebagai alat transportasi utama untuk perjalanan kerja atau sekolah.")
st.markdown("- Jam sibuk terjadi pada pagi dan sore hari, mengikuti pola perjalanan pekerja dan pelajar.")
st.markdown("- Faktor cuaca dan musim sangat mempengaruhi jumlah penyewaan, dengan penyewaan tertinggi terjadi di musim panas dan terendah di musim dingin.")

st.markdown("\n💡 **Kesimpulan:** Untuk meningkatkan efisiensi layanan, penyedia sepeda dapat menyesuaikan jumlah unit berdasarkan jam sibuk dan musim, serta menerapkan strategi promosi di akhir pekan dan musim dingin.")