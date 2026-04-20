# Panduan Kontribusi

Terima kasih sudah berkontribusi pada project **Praktikum Big Data Week 8: Keamanan dan Privasi Big Data (Real-Time Fraud Detection)**.

Repository ini sekarang mencakup:

1. Komponen **Week 6**: batch/streaming analytics, dashboard, dan alert transportation.
2. Komponen **Week 7**: data cleaning, training model ML, dan dashboard prediksi traffic.
3. Komponen **Week 8**: Kafka producer, Spark Structured Streaming, masking data sensitif, encoding/encryption demonstratif, dan dashboard fraud real-time.

Dokumen ini membantu menjaga kualitas kontribusi agar perubahan tetap rapi, mudah direview, dan tidak merusak pipeline yang sudah berjalan.

## Prinsip Kontribusi

1. Perubahan harus **jelas scope-nya** (satu topik utama per PR).
2. Perubahan harus **reproducible** (ada langkah menjalankan dan validasi).
3. Perubahan harus **aman terhadap modul lain** (hindari regresi antar Week 6, Week 7, dan Week 8).
4. Dokumentasi wajib ikut diupdate jika command, path, arsitektur, atau behavior berubah.
5. Untuk area keamanan/privasi, jelaskan **dampak risiko dan mitigasi** pada deskripsi PR.

## Ruang Lingkup Kontribusi

Kontribusi yang diterima:

1. Bug fix pipeline batch, streaming, analytics, dashboard, atau alert.
2. Peningkatan kualitas implementasi Week 8 (fraud detection, security transform, observability).
3. Peningkatan kualitas model traffic Week 7 (fitur, evaluasi, pelatihan, inferensi).
4. Peningkatan UX/dashboard visual untuk monitoring dan analitik.
5. Peningkatan kualitas data pipeline (validasi skema, data quality checks, robust error handling).
6. Refactor kode agar lebih maintainable tanpa mengubah behavior secara tidak sengaja.
7. Peningkatan dokumentasi (`README.md`, `CONTRIBUTING.md`, troubleshooting, runbook).

## Area Project yang Umum Diubah

1. `scripts/`
   - Week 8: `kafka_producer_bank.py`, `spark_streaming_fraud_v2.py`.
   - Week 7: `traffic_data_cleaning_v1.py`.
   - Week 6: batch/streaming dan transportation generator/consumer.
2. `dashboard/`
   - Week 8: `fraud_dashboard_v2.py`.
   - Week 7: `traffic_dashboard_v1.py`.
   - Week 6: dashboard e-commerce dan transportation.
3. `analytics/`
   - Week 7: `traffic_ml_model_v1.py`.
   - Week 6: `transportation_analytics.py`.
4. `alerts/`
   - Rule-based alert transportation.
5. `data/`, `stream_data/`, `models/`
   - Data source/output, checkpoint, dan artifact model.
6. Dokumentasi
   - `README.md`, `CONTRIBUTING.md`.

## Setup Development

### 1) Buat Virtual Environment

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

### 2) Install Dependency

```bash
pip install pyspark kafka-python streamlit pandas pyarrow scikit-learn joblib matplotlib
```

### 3) Validasi Environment

```bash
python --version
pip --version
```

Untuk pipeline Spark/Kafka:

```bash
java -version
```

Pastikan broker Kafka dapat diakses di `localhost:9092` saat validasi Week 8.

## Alur Kontribusi (Workflow)

1. Buat branch baru dari branch utama.
2. Gunakan nama branch yang deskriptif.
3. Lakukan perubahan kecil dan fokus pada satu concern.
4. Jalankan validasi lokal sesuai area yang diubah.
5. Commit dengan pesan yang jelas.
6. Push branch lalu buka Pull Request.
7. Sertakan ringkasan, langkah verifikasi, dan risiko perubahan.

Contoh pola nama branch:

- `feature/week8-fraud-rule-tuning`
- `fix/week8-streaming-parquet-read`
- `docs/update-week8-contributing`
- `refactor/spark-streaming-structure`

## Standar Penulisan Kode

1. Gunakan Python yang readable, konsisten, dan minim side effect tersembunyi.
2. Gunakan nama variabel/fungsi yang deskriptif.
3. Hindari hardcode path, topic, threshold, atau endpoint tanpa alasan jelas.
4. Tambahkan komentar singkat hanya untuk logika yang tidak langsung obvious.
5. Hindari perubahan lintas modul yang tidak diperlukan oleh scope PR.
6. Jika menambah dependency baru, jelaskan alasan dan dampaknya di PR.

## Standar Keamanan dan Privasi Data

1. Jangan commit kredensial, token, password, key, atau rahasia lainnya.
2. Jangan commit data nasabah nyata atau data sensitif produksi.
3. Pertahankan prinsip masking untuk data sensitif di layer output/monitoring.
4. Jika mengubah rule fraud atau transform keamanan, wajib jelaskan:
   - alasan perubahan,
   - dampak false positive/false negative,
   - dampak operasional dashboard.
5. Jika menambah mekanisme enkripsi baru, dokumentasikan asumsi key management dan batasan implementasi.

## Standar Data dan Artifact

1. Hindari commit file output besar hasil streaming yang tidak diperlukan review.
2. Hindari commit file temporary/eksperimen lokal.
3. Jika mengubah skema data, jelaskan perubahan kolom dan kompatibilitas downstream.
4. Jika mengubah artifact model (`models/traffic_model_v1.pkl`), sertakan:
   - perubahan fitur/algoritma,
   - cara training,
   - hasil validasi ringkas.
5. Jaga kompatibilitas path agar script/dashboard lain tidak rusak.

## Quality Gate Sebelum Pull Request

Lakukan pengecekan minimal ini:

1. Tidak ada import error saat script dijalankan.
2. Command utama untuk area yang diubah berhasil dijalankan.
3. Output penting terbentuk di path yang diharapkan.
4. Dashboard tetap bisa dibuka tanpa crash.
5. Dokumentasi terkait sudah diupdate jika command/path berubah.

### Validasi Minimal Week 8 (Jika Mengubah Fraud Streaming/Security)

Jalankan pada 3 terminal terpisah:

```bash
# Terminal 1
python scripts/kafka_producer_bank.py

# Terminal 2
python scripts/spark_streaming_fraud_v2.py

# Terminal 3
streamlit run dashboard/fraud_dashboard_v2.py
```

Checklist hasil:

1. Producer menulis event transaksi secara kontinu.
2. Folder `stream_data/realtime_output/` menghasilkan file parquet valid.
3. Dashboard menampilkan `Total Transaksi` dan `Total Fraud`.
4. Kolom `status`, `rekening_masked`, dan `jumlah_encrypted` tersedia di output data.

### Validasi Minimal Week 7 (Jika Mengubah ML Traffic)

```bash
python scripts/traffic_data_cleaning_v1.py
python analytics/traffic_ml_model_v1.py
streamlit run dashboard/traffic_dashboard_v1.py
```

Checklist hasil:

1. `data/clean/traffic_smartcity_clean_v1.csv` terbentuk.
2. `models/traffic_model_v1.pkl` terbentuk.
3. Dashboard traffic berjalan normal.

### Validasi Minimal Week 6 (Jika Mengubah Transportation/Streaming Lama)

1. Generator tetap menghasilkan data valid.
2. Streaming consumer tetap menulis data ke serving layer.
3. Dashboard transportation tetap menampilkan data.
4. Alert/anomaly logic tidak regress.

## Konvensi Commit

Gunakan format berikut:

- `feat: ...` untuk fitur baru
- `fix: ...` untuk bug fix
- `refactor: ...` untuk perapian kode
- `docs: ...` untuk dokumentasi
- `chore: ...` untuk pekerjaan pendukung

Contoh:

- `feat: add stricter fraud rule for high-value overseas transactions`
- `fix: skip empty parquet files in fraud dashboard reader`
- `docs: update contributing guide for week 8 workflow`

## Pull Request Checklist

Saat membuka PR, sertakan:

1. Ringkasan perubahan.
2. Area/folder yang terdampak.
3. Langkah verifikasi yang dijalankan.
4. Screenshot untuk perubahan visual dashboard (jika ada).
5. Risiko, asumsi, atau dampak kompatibilitas.
6. Khusus perubahan keamanan/privasi: dampak risiko dan mitigasi.
7. Catatan follow-up task (jika perubahan bertahap).

## Pelaporan Bug dan Permintaan Fitur

Agar issue cepat diproses, sertakan:

1. Deskripsi masalah/tujuan secara singkat.
2. Langkah reproduksi.
3. Perilaku yang diharapkan vs aktual.
4. Log error relevan (jika ada).
5. Environment singkat (OS, versi Python, versi Spark/Kafka, dependency utama).

---

Dengan mengikuti panduan ini, kontribusi akan lebih konsisten, proses review lebih cepat, dan kualitas sistem lintas Week 6 + Week 7 + Week 8 tetap terjaga.
