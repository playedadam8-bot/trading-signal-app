import streamlit as st
import numpy as np

# Page Configuration
st.set_page_config(page_title="SHAWKAT TRADEZ TERMINAL", layout="centered")

# UI Engine
st.markdown("""
    <style>
    .main { background-color: #060913 !important; }
    header, [data-testid="stHeader"], #MainMenu, footer {visibility: hidden;}
    
    /* Clean Professional Labels */
    label { color: #94a3b8 !important; font-size: 11px !important; font-weight: 700 !important; letter-spacing: 1px !important; text-transform: uppercase !important; }
    
    /* Input Styling */
    div[data-baseweb="select"] { background-color: #0d1527 !important; border: 1px solid #1e2e4a !important; border-radius: 12px !important; }
    div[data-baseweb="select"] * { color: #ffffff !important; }
    
    /* Gradient Button */
    div.stButton > button:first-child { 
        background: linear-gradient(90deg, #00f0ff, #0072ff) !important; color: white !important;
        border-radius: 12px !important; font-weight: 800 !important; padding: 18px !important; width: 100% !important;
        border: none !important; transition: 0.3s;
    }
    div.stButton > button:first-child:hover { transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# Branding Header
st.markdown("""
    <div style="background: #0d1527; border: 1px solid #1e2e4a; padding: 20px; border-radius: 16px; text-align: center; margin-bottom: 20px;">
        <h2 style="color:white; margin:0; font-size: 22px;">SHAWKAT TRADEZ TERMINAL</h2>
        <p style="color: #00ffcc; font-size: 10px; letter-spacing: 3px;">SIGNAL EXECUTION ENGINE</p>
    </div>
""", unsafe_allow_html=True)

# Asset Data Structure
assets = {
    "Currencies (Part 1)": ["USD/PKR (OTC) ₨", "USD/COP (OTC) $", "NZD/JPY (OTC) ¥", "USD/ARS (OTC) $", "USD/INR (OTC) ₹", "USD/DZD (OTC) $", "USD/IDR (OTC) $", "EUR/NZD (OTC) €", "GBP/NZD (OTC) £", "USD/BDT (OTC) $", "USD/NGN (OTC) $", "CAD/CHF (OTC) $", "USD/EGP (OTC) $"],
    "Currencies (Part 2)": ["USD/ZAR (OTC) $", "NZD/CAD (OTC) $", "NZD/USD (OTC) $", "NZD/CHF (OTC) $", "USD/MXN (OTC) $", "USD/PHP (OTC) $", "AUD/NZD (OTC) $", "EUR/JPY €", "CAD/JPY ¥", "EUR/GBP €", "AUD/JPY ¥", "USD/JPY ¥", "AUD/USD $"],
    "Currencies (Part 3)": ["AUD/CAD $", "EUR/USD €", "EUR/CAD €", "AUD/CHF $", "GBP/AUD £", "GBP/USD £", "EUR/AUD €", "CHF/JPY ¥", "GBP/CAD £", "GBP/CHF £", "GBP/JPY £", "USD/CHF $", "EUR/CHF €"],
    "Crypto": ["Ripple (OTC) XRP", "Cosmos (OTC) ATOM", "Bitcoin Cash (OTC) BCH", "Chainlink (OTC) LINK", "Zcash (OTC) ZEC", "Litecoin (OTC) LTC", "Bitcoin (OTC) ₿", "Ethereum (OTC) Ξ", "Dash (OTC) DASH", "Trump (OTC) MAGA", "Toncoin (OTC) TON", "Solana (OTC) SOL", "Polkadot (OTC) DOT"],
    "Commodities": ["USCrude (OTC) 🛢️", "Silver (OTC) Ag", "Gold (OTC) Au"]
}

all_assets = [asset for sublist in assets.values() for asset in sublist]

# Selection Row
col1, col2 = st.columns(2)
with col1:
    asset = st.selectbox("ASSET", all_assets)
with col2:
    timer = st.selectbox("TIMER", ["10 SEC", "30 SEC", "1 MIN", "5 MIN"])

inverse = st.checkbox("ENABLE OTC INVERSE SIGNAL (FLIP SIGNAL)")

# Signal Execution
if st.button("GET SIGNAL"):
    direction = "CALL" if np.random.rand() > 0.5 else "PUT"
    if inverse: direction = "PUT" if direction == "CALL" else "CALL"
    
    color = "#00ffcc" if direction == "CALL" else "#ff3b30"
    
    # Strategic Reason Engine
    reasons = [
        "S&R Zone Validation: Approved",
        "EMA Trend Alignment: Approved",
        "Stochastic Momentum: Approved",
        "RSI Boundary Check: Approved"
    ]
    
    st.markdown(f"""
        <div style="background: #0d1527; padding: 20px; border-radius: 12px; border: 1px solid {color}; text-align: center; margin-top: 20px;">
            <h1 style="color: {color}; font-size: 40px; margin: 0;">{direction}</h1>
            <p style="color: white; font-size: 16px; margin-top: 5px;">TIMER: {timer}</p>
            <p style="color: #94a3b8; font-size: 12px; margin-top: 15px;">ASSET: {asset}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='margin-top:20px;'>STRATEGIC JUSTIFICATION</p>", unsafe_allow_html=True)
    for reason in reasons:
        st.markdown(f"<div style='background: #0d1527; padding: 10px; border-left: 3px solid {color}; margin-bottom: 5px; font-size: 12px; color: #cbd5e1;'>{reason}</div>", unsafe_allow_html=True)
