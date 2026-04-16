import streamlit as st
import pandas as pd
from pathlib import Path

st.title("🚨 Real-Time Fraud Detection Dashboard")

output_dir = Path("stream_data/realtime_output")

# Ambil hanya file parquet yang valid:
# - bukan file tersembunyi
# - ukurannya > 0 byte
parquet_files = [
    f for f in output_dir.glob("*.parquet")
    if f.is_file() and f.stat().st_size > 0 and not f.name.startswith(".")
]

if not parquet_files:
    st.warning("Belum ada file parquet valid yang bisa dibaca.")
    st.stop()

try:
    df_list = [pd.read_parquet(f) for f in parquet_files]
    df = pd.concat(df_list, ignore_index=True)

    st.metric("Total Transaksi", len(df))

    if "status" in df.columns:
        st.metric("Total Fraud", len(df[df["status"] == "FRAUD"]))
        st.dataframe(df.tail(10))
        st.bar_chart(df["status"].value_counts())
    else:
        st.error("Kolom 'status' tidak ditemukan.")
        st.dataframe(df.tail(10))

except Exception as e:
    st.error(f"Gagal membaca data parquet: {e}")