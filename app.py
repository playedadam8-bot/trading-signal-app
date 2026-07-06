import streamlit as st
import requests
import numpy as np
from datetime import datetime, timedelta, timezone

st.set_page_config(page_title="PRO TRADING TERMINAL", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #060913 !important; }
    div[data-testid="stMarkdownContainer"] p { color: #64748b; font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
    div[data-baseweb="select"] { background-color: #0d1527 !important; border-radius: 10px !important; }
    div.stButton > button:first-child { background: linear-gradient(90deg, #00f0ff, #0072ff) !important; color: white !important; font-weight: 800 !important; width: 100% !important; padding: 15px !important; border-radius: 12px !important; }
    </style>
""", unsafe_allow_html=True)

# Asset Architecture
asset_groups = {
    "Currencies (Part 1)": ["USD/PKR (OTC)", "USD/COP (OTC)", "NZD/JPY (OTC)", "USD/ARS (OTC)", "USD/INR (OTC)", "USD/DZD (OTC)", "USD/IDR (OTC)", "EUR/NZD (OTC)", "GBP/NZD (OTC)", "USD/BDT (OTC)", "USD/NGN (OTC)", "CAD/CHF (OTC)", "USD/EGP (OTC)"],
    "Currencies (Part 2)": ["USD/ZAR (OTC)", "NZD/CAD (OTC)", "NZD/USD (OTC)", "NZD/CHF (OTC)", "USD/MXN (OTC)", "USD/PHP (OTC)", "AUD/NZD (OTC)", "EUR/JPY", "CAD/JPY", "EUR/GBP", "AUD/JPY", "USD/JPY", "AUD/USD"],
    "Currencies (Part 3)": ["AUD/CAD", "EUR/USD", "EUR/CAD", "AUD/CHF", "GBP/AUD", "GBP/USD", "EUR/AUD", "CHF/JPY", "GBP/CAD", "GBP/CHF", "GBP/JPY", "USD/CHF", "EUR/CHF"],
    "Crypto": ["Ripple (OTC)", "Cosmos (OTC)", "Bitcoin Cash (OTC)", "Chainlink (OTC)", "Zcash (OTC)", "Litecoin (OTC)", "Bitcoin (OTC)", "Ethereum (OTC)", "Dash (OTC)", "Trump (OTC)", "Toncoin (OTC)", "Solana (OTC)", "Polkadot (OTC)"],
    "Commodities": ["USCrude (OTC)", "Silver (OTC)", "Gold (OTC)"]
}

# Layout
col1, col2 = st.columns(2)
with col1:
    st.markdown("<p>Select Asset</p>", unsafe_allow_html=True)
    all_assets = [item for sublist in asset_groups.values() for item in sublist]
    asset = st.selectbox("Asset", all_assets, label_visibility="collapsed")
with col2:
    st.markdown("<p>Duration</p>", unsafe_allow_html=True)
    duration = st.selectbox("Duration", ["1 Min", "5 Min", "15 Min"], label_visibility="collapsed")

# OTC Inverse Toggle
is_otc = "(OTC)" in asset
inverse_mode = False
if is_otc:
    inverse_mode = st.checkbox("Enable OTC Inverse Signal (Flip Signal)")

if st.button("GET SIGNAL"):
    # Logic: Simulated signal calculation
    direction = "CALL" if np.random.rand() > 0.5 else "PUT"
    
    # Flip if Inverse Mode is active
    if inverse_mode and direction == "CALL": direction = "PUT"
    elif inverse_mode and direction == "PUT": direction = "CALL"
    
    st.markdown(f"### Signal: {direction} ({duration})")
    st.write(f"Asset: {asset}")
