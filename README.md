# Praktikum Big Data Week 7: Machine Learning untuk Prediksi Traffic (Smart City AI)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-RandomForest-F7931E?logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive%20Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![Joblib](https://img.shields.io/badge/Model-Serialized%20with%20Joblib-2E7D32)
![Smart City](https://img.shields.io/badge/Use%20Case-Traffic%20Prediction-1565C0)

## Tim Praktikum

| Peran | Nama | NIM | Profil GitHub |
| :--- | :--- | :--- | :--- |
| **Pengembang Proyek** | M. Kaspul Anwar | 230104040212 | [![](https://img.shields.io/badge/GitHub-mkaspulanwar-181717?style=flat&logo=github)](https://github.com/mkaspulanwar) |
| **Dosen Pengampu** | Muhayat, M. IT | - | [![](https://img.shields.io/badge/GitHub-muhayat--lab-181717?style=flat&logo=github)](https://github.com/muhayat-lab) |

---

## Ringkasan Praktikum Week 7

Praktikum Week 7 berfokus pada implementasi **Machine Learning untuk Prediksi Traffic Smart City** sebagai kelanjutan dari Week 6 (real-time analytics dan visualisasi skala besar).

Pada Week 6, sistem sudah mampu melakukan ingestion, processing, dan visualisasi data transportation secara near real-time. Pada Week 7, proyek diperluas dengan lapisan **predictive analytics** untuk memprediksi kepadatan traffic menggunakan model machine learning.

## Tujuan Praktikum

1. Menyiapkan data traffic agar layak untuk training model.
2. Membangun baseline model regresi untuk memprediksi jumlah kendaraan.
3. Mengintegrasikan model ke dashboard interaktif untuk inferensi cepat.
4. Mendokumentasikan alur end-to-end dari data mentah sampai prediksi.
5. Menjaga kesinambungan arsitektur Week 6 ke Week 7.

## Cakupan Fitur Week 7

1. **Data cleaning pipeline** untuk dataset traffic smart city.
2. **Feature engineering berbasis waktu** (`hour`, `day`) dan fitur historis (`lag1`).
3. **Model training** menggunakan `RandomForestRegressor`.
4. **Model persistence** ke artifact `models/traffic_model_v1.pkl`.
5. **Dashboard prediksi** berbasis Streamlit untuk eksplorasi metrik dan simulasi prediksi.

## Arsitektur Sistem (Week 6 -> Week 7)

```mermaid
flowchart LR
    A["Raw Traffic Dataset CSV"] --> B["Data Cleaning (Pandas)"]
    B --> C["Clean Dataset (CSV)"]
    C --> D["Feature Engineering (hour, day, lag1)"]
    D --> E["Model Training (RandomForestRegressor)"]
    E --> F["Model Artifact (.pkl)"]
    C --> G["Traffic Dashboard (Streamlit)"]
    F --> G
    G --> H["Interactive Prediction & Monitoring"]

    I["Week 6 Transportation Streaming"] --> G
```

## Struktur Project (Terbaru)

```bash
bigdata-project/
|-- .venv/                                         # Virtual environment lokal
|-- alerts/                                        # Modul alert untuk use case transportation
|   |-- __init__.py
|   `-- transportation_alert.py                    # Rule-based alert (traffic/fare)
|-- analytics/                                     # Modul analytics & machine learning
|   |-- __init__.py
|   |-- transportation_analytics.py                # KPI, trend, anomaly detection (Week 6)
|   `-- traffic_ml_model_v1.py                     # Training model prediksi traffic (Week 7)
|-- dashboard/                                     # Aplikasi dashboard Streamlit
|   |-- dashboard_streamlit.py                     # Dashboard real-time e-commerce
|   |-- dashboard_transportation.py                # Dashboard decision-oriented transportation
|   `-- traffic_dashboard_v1.py                    # Dashboard prediksi traffic (Week 7)
|-- data/
|   |-- checkpoints/                               # Spark streaming checkpoint
|   |   `-- transportation/
|   |-- clean/                                     # Data hasil cleaning
|   |   `-- traffic_smartcity_clean_v1.csv
|   |-- curated/                                   # Data agregasi bisnis (Week 6)
|   |-- raw/
|   |   |-- ecommerce_raw.csv                      # Dataset mentah utama batch
|   |   `-- traffic_smartcity_v1.csv               # Dataset traffic smart city (Week 7)
|   `-- serving/                                   # Data siap konsumsi dashboard
|       |-- avg_transaction/
|       |-- category_revenue/
|       |-- stream/                                # Output streaming e-commerce
|       |-- top_products/
|       |-- total_revenue/
|       `-- transportation/                        # Output streaming transportation
|-- logs/
|   |-- batch_pipeline.log                         # Log proses batch pipeline
|   `-- stream_checkpoint/                         # Checkpoint streaming e-commerce
|-- models/
|   `-- traffic_model_v1.pkl                       # Artifact model prediksi traffic (Week 7)
|-- screenshots/                                   # Screenshot dokumentasi hasil praktikum
|   |-- struktur_project.png
|   |-- scripts_cleaning.png
|   |-- data_cleaning_selesai.png
|   |-- scripts_modeling.png
|   |-- model_berhasil_disimpan.png
|   |-- scripts_dashboard.png
|   |-- dashboard_berjalan.png
|   |-- dashboard_1.png
|   |-- dashboard_2.png
|   `-- nilai_prediksi.png
|-- scripts/                                       # Pipeline utama praktikum
|   |-- analytics_layer.py                         # Analytics + serving layer (e-commerce)
|   |-- batch_pipeline_enterprise.py               # Batch processing pipeline
|   |-- streaming_layer.py                         # Streaming ingestion e-commerce
|   |-- transaction_generator.py                   # Generator transaksi e-commerce
|   |-- traffic_data_cleaning_v1.py                # Data cleaning traffic (Week 7)
|   `-- transportation/
|       |-- streaming_trip_layer.py                # Streaming ingestion transportation
|       `-- trip_generator.py                      # Generator trip transportation
|-- stream_data/                                   # Input simulasi data streaming
|   `-- transportation/
|-- .gitignore
|-- CONTRIBUTING.md
|-- LICENSE
`-- README.md
```

## Bukti Screenshots

<table>
<tr>
<td align="center"><b>Struktur Project</b></td>
<td align="center"><b>Scripts Cleaning</b></td>
</tr>
<tr>
<td><img src="screenshots/struktur_project.png"/></td>
<td><img src="screenshots/scripts_cleaning.png"/></td>
</tr>

<tr>
<td align="center"><b>Data Cleaning Selesai</b></td>
<td align="center"><b>Scripts Modeling</b></td>
</tr>
<tr>
<td><img src="screenshots/data_cleaning_selesai.png"/></td>
<td><img src="screenshots/scripts_modeling.png"/></td>
</tr>

<tr>
<td align="center"><b>Model Berhasil Disimpan</b></td>
<td align="center"><b>Scripts Dashboard</b></td>
</tr>
<tr>
<td><img src="screenshots/model_berhasil_disimpan.png"/></td>
<td><img src="screenshots/scripts_dashboard.png"/></td>
</tr>

<tr>
<td align="center"><b>Dashboard Berjalan</b></td>
<td align="center"><b>Dashboard 1</b></td>
</tr>
<tr>
<td><img src="screenshots/dashboard_berjalan.png"/></td>
<td><img src="screenshots/dashboard_1.png"/></td>
</tr>

<tr>
<td align="center"><b>Dashboard 2</b></td>
<td align="center"><b>Nilai Prediksi</b></td>
</tr>
<tr>
<td><img src="screenshots/dashboard_2.png"/></td>
<td><img src="screenshots/nilai_prediksi.png"/></td>
</tr>
</table>

## Dataset Week 7

Sumber dataset utama berada di:

- `data/raw/traffic_smartcity_v1.csv`

Ringkasan data:

1. Jumlah baris: **168 records**.
2. Rentang waktu: **2025-01-01 00:00:00 sampai 2025-01-07 23:00:00**.
3. Frekuensi: **per jam (hourly)**.

Skema kolom:

| Kolom | Tipe | Deskripsi |
| :--- | :--- | :--- |
| `datetime` | datetime | Timestamp observasi traffic |
| `traffic` | int/float | Jumlah kendaraan pada timestamp tersebut |

## Penjelasan Alur Week 7 (End-to-End)

### 1) Data Cleaning

Script: `scripts/traffic_data_cleaning_v1.py`

Proses utama:

1. Membaca data mentah dari `data/raw/traffic_smartcity_v1.csv`.
2. Parsing kolom `datetime` menjadi tipe waktu.
3. Sort data berdasarkan waktu.
4. Menghapus baris bernilai null (`dropna`).
5. Menyimpan output ke `data/clean/traffic_smartcity_clean_v1.csv`.

Jalankan:

```bash
python scripts/traffic_data_cleaning_v1.py
```

### 2) Modeling Machine Learning

Script: `analytics/traffic_ml_model_v1.py`

Proses utama:

1. Membaca data bersih.
2. Membuat fitur turunan:
   - `hour` = jam (0-23)
   - `day` = indeks hari (0-6)
   - `lag1` = traffic satu periode sebelumnya
3. Menentukan target `y = traffic`.
4. Training model `RandomForestRegressor` (baseline).
5. Menyimpan model ke `models/traffic_model_v1.pkl`.

Jalankan:

```bash
python analytics/traffic_ml_model_v1.py
```

### 3) Dashboard Prediksi

Script: `dashboard/traffic_dashboard_v1.py`

Fitur dashboard:

1. Menampilkan KPI sederhana (`Avg Traffic`, `Max Traffic`).
2. Menampilkan grafik trend traffic.
3. Menyediakan input interaktif (`hour`, `day`, `lag1`) untuk simulasi prediksi.
4. Menampilkan output prediksi jumlah kendaraan.

Jalankan:

```bash
streamlit run dashboard/traffic_dashboard_v1.py
```

## Setup Environment

### 1) Prasyarat

1. Python 3.10+ (disarankan 3.12).
2. Pip dan virtual environment.
3. Java (opsional, jika juga menjalankan pipeline Spark Week 6).

### 2) Membuat Virtual Environment

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install Dependency

```bash
pip install pandas scikit-learn joblib streamlit matplotlib pyspark pyarrow
```

## Quick Run (Rekomendasi Praktikum 7)

Jalankan berurutan dari root project:

```bash
python scripts/traffic_data_cleaning_v1.py
python analytics/traffic_ml_model_v1.py
streamlit run dashboard/traffic_dashboard_v1.py
```

## Validasi Keberhasilan

Praktikum dianggap berhasil jika:

1. File `data/clean/traffic_smartcity_clean_v1.csv` terbentuk setelah cleaning.
2. File `models/traffic_model_v1.pkl` terbentuk setelah training.
3. Dashboard terbuka tanpa error dan menampilkan metrik serta grafik trend.
4. Tombol prediksi menghasilkan nilai prediksi kendaraan dari input pengguna.


## Integrasi Dengan Praktikum 6

Komponen Week 6 tetap dipertahankan di repo (streaming transportation, analytics, alert, dan dashboard). Dengan demikian, repository ini sekarang mencakup dua spektrum analitik:

1. **Descriptive + Real-Time Analytics** (Week 6).
2. **Predictive Analytics (Machine Learning)** (Week 7).

Pendekatan ini merepresentasikan alur smart city data platform yang lebih lengkap: dari observasi traffic hingga prediksi traffic.

## Troubleshooting

1. Jika error `No module named ...`, pastikan virtual environment aktif dan dependency sudah terinstall.
2. Jika model tidak ditemukan di dashboard, jalankan ulang script training model.
3. Jika data bersih tidak ditemukan, jalankan ulang script cleaning.
4. Jika tampilan dashboard kosong, pastikan file `data/clean/traffic_smartcity_clean_v1.csv` berisi data valid.

## Keterbatasan Baseline Saat Ini

1. Model belum menggunakan train/test split dan evaluasi metrik formal (MAE/RMSE/R2).
2. Fitur masih sederhana (`hour`, `day`, `lag1`) dan belum mencakup cuaca/event kota.
3. Belum ada retraining otomatis periodik.

## Rencana Pengembangan Lanjutan

1. Menambahkan evaluasi model terukur (MAE, RMSE, R2) dan visual error analysis.
2. Menambahkan fitur eksternal (cuaca, hari libur, event, kepadatan area).
3. Menyusun pipeline retraining terjadwal dan versioning model.
4. Integrasi prediksi ke layer alert real-time untuk proactive traffic management.

## Penutup

Week 7 berhasil memperluas fondasi Week 6 dari sekadar monitoring real-time menjadi sistem yang mulai memiliki kemampuan prediktif. Hasilnya, repository ini kini lebih siap digunakan sebagai prototipe **Smart City AI** yang menggabungkan ingestion, analytics, visualisasi, dan prediksi traffic dalam satu alur terpadu.



