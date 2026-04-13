# Panduan Kontribusi

Terima kasih sudah berkontribusi pada project **Praktikum Big Data Week 7: Machine Learning untuk Prediksi Traffic (Smart City AI)**.

Repository ini sekarang mencakup:

1. Komponen **Week 6**: batch/streaming analytics, dashboard, dan alert transportation.
2. Komponen **Week 7**: data cleaning, training model ML, dan dashboard prediksi traffic.

Dokumen ini membantu kita menjaga kualitas kontribusi agar perubahan tetap rapi, mudah direview, dan tidak merusak pipeline yang sudah berjalan.

## Prinsip Kontribusi

1. Perubahan harus **jelas scope-nya** (fokus pada satu topik per PR).
2. Perubahan harus **reproducible** (ada langkah menjalankan dan validasi).
3. Perubahan harus **aman terhadap modul lain** (hindari regression antar Week 6 dan Week 7).
4. Dokumentasi harus ikut diupdate jika command, path, atau behavior berubah.

## Ruang Lingkup Kontribusi

Kontribusi yang diterima:

1. Perbaikan bug pipeline batch, streaming, analytics, dashboard, atau alert.
2. Peningkatan kualitas model traffic (fitur, evaluasi, pelatihan, inferensi).
3. Peningkatan UX/dashboard visual untuk observability dan prediksi.
4. Peningkatan kualitas data pipeline (cleaning, validasi skema, data quality checks).
5. Refactor kode agar lebih maintainable tanpa mengubah behavior secara tidak sengaja.
6. Peningkatan dokumentasi (`README.md`, `CONTRIBUTING.md`, troubleshooting, runbook).

## Area Project yang Umum Diubah

1. `scripts/`
   - Week 6: batch/streaming generator & processing.
   - Week 7: `traffic_data_cleaning_v1.py`.
2. `analytics/`
   - Week 6: analytics transportation.
   - Week 7: `traffic_ml_model_v1.py`.
3. `dashboard/`
   - Week 6: dashboard e-commerce & transportation.
   - Week 7: `traffic_dashboard_v1.py`.
4. `models/`
   - Artifact model (`traffic_model_v1.pkl`) bila ada update baseline model.
5. `data/`
   - `raw/`, `clean/`, `serving/`, `curated/`, `checkpoints/`.
6. `alerts/`
   - Rule-based alert transportation (Week 6).

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
pip install pandas scikit-learn joblib streamlit matplotlib pyspark pyarrow
```

### 3) Validasi Environment

```bash
python --version
pip --version
```

Opsional untuk pipeline Spark Week 6:

```bash
java -version
```

## Alur Kontribusi (Workflow)

1. Buat branch baru dari branch utama.
2. Gunakan nama branch yang deskriptif.
3. Lakukan perubahan kecil dan fokus pada satu concern.
4. Jalankan validasi lokal sesuai area yang diubah.
5. Commit dengan pesan yang jelas.
6. Push branch lalu buka Pull Request.
7. Sertakan ringkasan, langkah verifikasi, dan risiko perubahan.

Contoh pola nama branch:

- `feature/traffic-model-evaluation`
- `fix/dashboard-traffic-empty-data`
- `docs/update-week7-contributing`

## Standar Penulisan Kode

1. Gunakan Python yang readable dan konsisten.
2. Gunakan nama variabel/fungsi yang deskriptif.
3. Hindari hardcode path atau nilai threshold tanpa alasan jelas.
4. Tambahkan komentar singkat hanya untuk logika yang tidak langsung obvious.
5. Hindari perubahan lintas modul yang tidak diperlukan oleh scope.
6. Jika menambah dependency baru, jelaskan alasan dan dampaknya di PR.

## Standar Data, Model, dan Artifact

1. Jangan commit kredensial, data sensitif, atau informasi personal.
2. Hindari commit file temporary/eksperimen lokal yang tidak dibutuhkan.
3. Jika mengubah dataset atau preprocessing, jelaskan skema dan dampaknya.
4. Jika mengubah model (`traffic_model_v1.pkl`), sertakan:
   - perubahan fitur/algoritma,
   - cara training,
   - hasil validasi ringkas.
5. Jaga kompatibilitas path agar dashboard dan script lain tidak rusak.

## Quality Gate Sebelum Pull Request

Lakukan pengecekan minimal ini:

1. Tidak ada import error saat script dijalankan.
2. Command utama untuk area yang diubah berhasil dijalankan.
3. Output penting terbentuk di path yang diharapkan.
4. Dashboard tetap bisa dibuka tanpa crash.
5. Dokumen terkait sudah diupdate jika command/path berubah.

### Validasi Minimal Week 7 (Jika Mengubah ML Traffic)

```bash
python scripts/traffic_data_cleaning_v1.py
python analytics/traffic_ml_model_v1.py
streamlit run dashboard/traffic_dashboard_v1.py
```

Checklist hasil:

1. `data/clean/traffic_smartcity_clean_v1.csv` terbentuk.
2. `models/traffic_model_v1.pkl` terbentuk.
3. Dashboard menampilkan KPI, trend, dan prediksi.

### Validasi Minimal Week 6 (Jika Mengubah Streaming/Transportation)

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

- `feat: add traffic model evaluation metrics section`
- `fix: handle empty clean traffic dataset in dashboard`
- `docs: update contributing guide for week 7`

## Pull Request Checklist

Saat membuka PR, sertakan:

1. Ringkasan perubahan.
2. Area/folder yang terdampak.
3. Langkah verifikasi yang dijalankan.
4. Screenshot untuk perubahan visual dashboard.
5. Risiko, asumsi, atau dampak kompatibilitas (jika ada).
6. Catatan follow-up task (jika perubahan bertahap).

## Pelaporan Bug dan Permintaan Fitur

Agar issue cepat diproses, sertakan:

1. Deskripsi masalah/tujuan secara singkat.
2. Langkah reproduksi.
3. Perilaku yang diharapkan vs aktual.
4. Log error relevan (jika ada).
5. Environment singkat (OS, versi Python, dependency utama).

---

Dengan mengikuti panduan ini, kontribusi akan lebih konsisten, proses review lebih cepat, dan kualitas sistem Week 6 + Week 7 tetap terjaga.
