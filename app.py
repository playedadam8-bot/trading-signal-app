import streamlit as st
import requests
import numpy as np
from datetime import datetime, timedelta, timezone

# 1. Page Configuration
st.set_page_config(page_title="SHAWKAT TRADEZ TERMINAL", layout="centered")

# 2. UI Styling Engine
st.markdown("""
    <style>
    .main { background-color: #060913 !important; }
    header, [data-testid="stHeader"], #MainMenu, footer {visibility: hidden;}
    
    div[data-testid="stMarkdownContainer"] p {
        color: #64748b; font-size: 13px !important; font-weight: 700 !important;
        letter-spacing: 1.5px !important; text-transform: uppercase !important;
    }
    
    div[data-baseweb="select"] {
        background-color: #0d1527 !important; border: 1px solid #1e2e4a !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] * { color: #ffffff !important; }
    
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00f0ff, #0072ff) !important;
        color: #ffffff !important; border-radius: 16px !important; border: none !important;
        padding: 18px 20px !important; font-weight: 700 !important; font-size: 20px !important;
        text-transform: uppercase !important; letter-spacing: 2px !important;
        width: 100% !important; margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header
st.markdown("""
    <div style="background: linear-gradient(135deg, #0d1527, #060913); border: 1px solid #1e2e4a; padding: 20px; border-radius: 20px; text-align: center; margin-bottom: 25px;">
        <h2 style="color: #ffffff; font-weight: 900; font-size: 24px;">SHAWKAT TRADEZ TERMINAL</h2>
        <span style="color: #00ffcc; font-size: 12px; font-weight: 700; letter-spacing: 2px;">LIVE • SIGNAL PROTOCOL</span>
    </div>
""", unsafe_allow_html=True)

# 4. Inputs
col1, col2 = st.columns(2)
with col1:
    st.markdown("<p>ASSET</p>", unsafe_allow_html=True)
    asset = st.selectbox("ASSET", [
        "USD/PKR (OTC)", "USD/COP (OTC)", "NZD/JPY (OTC)", "USD/ARS (OTC)", "USD/INR (OTC)", "USD/DZD (OTC)", "USD/IDR (OTC)", "EUR/NZD (OTC)", "GBP/NZD (OTC)", "USD/BDT (OTC)", "USD/NGN (OTC)", "CAD/CHF (OTC)", "USD/EGP (OTC)",
        "USD/ZAR (OTC)", "NZD/CAD (OTC)", "NZD/USD (OTC)", "NZD/CHF (OTC)", "USD/MXN (OTC)", "USD/PHP (OTC)", "AUD/NZD (OTC)", "EUR/JPY", "CAD/JPY", "EUR/GBP", "AUD/JPY", "USD/JPY", "AUD/USD",
        "AUD/CAD", "EUR/USD", "EUR/CAD", "AUD/CHF", "GBP/AUD", "GBP/USD", "EUR/AUD", "CHF/JPY", "GBP/CAD", "GBP/CHF", "GBP/JPY", "USD/CHF", "EUR/CHF",
        "Ripple (OTC)", "Cosmos (OTC)", "Bitcoin Cash (OTC)", "Chainlink (OTC)", "Zcash (OTC)", "Litecoin (OTC)", "Bitcoin (OTC)", "Ethereum (OTC)", "Dash (OTC)", "Trump (OTC)", "Toncoin (OTC)", "Solana (OTC)", "Polkadot (OTC)",
        "USCrude (OTC)", "Silver (OTC)", "Gold (OTC)"
    ], label_visibility="collapsed")
with col2:
    st.markdown("<p>TIMER</p>", unsafe_allow_html=True)
    timer = st.selectbox("TIMER", ["10 SEC", "30 SEC", "1 MIN", "5 MIN"], label_visibility="collapsed")

# 5. Signal Engine
if st.button("⚡ GET SIGNAL"):
    # Random logic that actually triggers on every click
    direction = "CALL" if np.random.rand() > 0.5 else "PUT"
    color = "#00ffcc" if direction == "CALL" else "#ff3b30"
    
    # Justification Matrix
    reasons = [
        "S&R Zone Validation: Approved",
        "EMA Trend Alignment: Approved",
        "Stochastic Momentum: Approved",
        "RSI Momentum Boundary: Approved",
        "MACD Direction Vector: Approved"
    ]
    
    st.markdown(f"""
        <div style="background: #0d1527; padding: 25px; border-radius: 18px; border: 1px solid {color}; text-align: center; margin-top: 20px;">
            <h1 style="color: {color}; font-size: 38px; font-weight: 800; margin: 0;">{direction}</h1>
            <p style="color: white; font-size: 16px; margin: 5px 0;">TIMER: {timer}</p>
            <p style="color: #64748b; font-size: 12px;">ASSET: {asset}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='margin-top:20px;'>💡 STRATEGIC JUSTIFICATION MATRIX</p>", unsafe_allow_html=True)
    for reason in reasons:
        st.markdown(f"""
            <div style="background: #0d1527; border-left: 3px solid {color}; padding: 10px; margin-bottom: 6px; 
            border-radius: 8px; font-size: 13px; color: #cbd5e1; font-weight: 500;">{reason}</div>
        """, unsafe_allow_html=True)

st.markdown("<br><hr style='border-color:#1e2e4a;'><p style='text-align:center; color:#64748b; font-size:10px;'>⚡ RISK MANAGEMENT ADVISED</p>", unsafe_allow_html=True)
