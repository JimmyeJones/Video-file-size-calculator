import streamlit as st

st.title("OBS Recording Time Calculator")

# User inputs
video_bitrate_kbps = st.number_input("Enter video bitrate (kbps)", min_value=1, value=8000)
audio_bitrate_kbps = st.number_input("Enter audio bitrate (kbps)", min_value=1, value=192)
available_storage_gb = st.number_input("Enter available storage (GB)", min_value=0.1, value=50.0)

# Calculations
total_bitrate_kbps = video_bitrate_kbps + audio_bitrate_kbps
total_bitrate_mbps = total_bitrate_kbps / 1000
available_storage_mb = available_storage_gb * 8192

# Recording time in seconds
recording_time_seconds = available_storage_mb / total_bitrate_mbps
recording_time_hours = recording_time_seconds / 3600

st.write(f"You can record for approximately {recording_time_hours:.2f} hours.")
