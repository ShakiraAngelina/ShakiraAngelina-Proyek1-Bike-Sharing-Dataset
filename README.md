## Setup Environment - Anaconda

Jika menggunakan Anaconda, jalankan perintah berikut untuk membuat environment:

```bash
conda create --name bike-sharing-env python=3.9
conda activate bike-sharing-env
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

Jika menggunakan terminal biasa atau virtual environment lain:

```bash
mkdir "Proyek Latihan 1 Coding Camp_MC254D5X0781_Shakira Angelina Ika Putri"
cd "Proyek Latihan 1 Coding Camp_MC254D5X0781_Shakira Angelina Ika Putri"
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Run Streamlit App

Untuk menjalankan dashboard:

```bash
streamlit run dashboard.py
```
