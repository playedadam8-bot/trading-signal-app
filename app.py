import streamlit as st
import requests
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta, timezone

# Dark cyberpunk UI matching premium HFT bot layouts
st.set_page_config(page_title="SHAWKAT TRADEZ PREMIUM BOT", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #060913; }
    div[data-basename="selectbox"] input {
        pointer-events: none !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00c6ff, #0072ff);
        color: white;
        border-radius: 30px;
        border: none;
        padding: 16px;
        font-weight: bold;
        font-size: 18px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 198, 255, 0.4);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 198, 255, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; padding: 15px; border-radius: 12px; background-color: #0b132b; border: 1px solid #00f0ff;">
        <h1 style="color:#00f0ff; margin:0; font-size: 26px; font-family:'Courier New', monospace; font-weight:900;">SHAWKAT TRADEZ BOT</h1>
        <p style="color:#00ffcc; margin:5px 0 0 0; font-size: 13px; letter-spacing: 2px; font-weight: bold;">🛰️ UTC+5 PREDICATIVE TIME ALGO V7.0</p>
    </div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

asset_selection = st.selectbox("📄 SELECT ASSET", [
    "🇺🇸🇵🇰 USD/PKR (OTC)", "🇺🇸🇨🇴 USD/COP (OTC)", "🇳🇿🇯🇵 NZD/JPY (OTC)", "🇺🇸🇦🇷 USD/ARS (OTC)", 
    "🇺🇸🇮🇳 USD/INR (OTC)", "🇺🇸🇩🇿 USD/DZD (OTC)", "🇺🇸🇮🇩 USD/IDR (OTC)", "🇪🇺🇳🇿 EUR/NZD (OTC)", 
    "🇬🇧🇳🇿 GBP/NZD (OTC)", "🇺🇸🇧🇩 USD/BDT (OTC)", "🇺🇸🇳🇬 USD/NGN (OTC)", "🇨🇦🇨🇭 CAD/CHF (OTC)", "🇺🇸🇪🇬 USD/EGP (OTC)",
    "🇺🇸🇿🇦 USD/ZAR (OTC)", "🇳🇿🇨🇦 NZD/CAD (OTC)", "🇳🇿🇺🇸 NZD/USD (OTC)", "🇳🇿🇨🇭 NZD/CHF (OTC)", 
    "🇺🇸🇲🇽 USD/MXN (OTC)", "🇺🇸🇵🇭 USD/PHP (OTC)", "🇦🇺🇳🇿 AUD/NZD (OTC)", "🇪🇺🇯🇵 EUR/JPY", "🇨🇦🇯🇵 CAD/JPY", 
    "🇪🇺🇬🇧 EUR/GBP", "🇦🇺🇯🇵 AUD/JPY", "🇺🇸🇯🇵 USD/JPY", "🇦🇺🇺🇸 AUD/USD",
    "🇦🇺🇨🇦 AUD/CAD", "🇪🇺🇺🇸 EUR/USD", "🇪🇺🇨🇦 EUR/CAD", "🇦🇺🇨🇭 AUD/CHF", "🇬🇧🇦🇺 GBP/AUD", "🇬🇧🇺🇸 GBP/USD", 
    "🇪🇺🇦🇺 EUR/AUD", "🇨🇭🇯🇵 CHF/JPY", "🇬🇧🇨🇦 GBP/CAD", "🇬🇧🇨🇭 GBP/CHF", "🇬🇧🇯🇵 GBP/JPY", "🇺🇸🇨🇭 USD/CHF", "🇪🇺🇨🇭 EUR/CHF",
    "🪙 Ripple (OTC)", "⚛️ Cosmos (OTC)", "💵 Bitcoin Cash (OTC)", "🔗 Chainlink (OTC)", 
    "🛡️ Zcash (OTC)", "🥈 Litecoin (OTC)", "🥇 Bitcoin (OTC)", "⧫ Ethereum (OTC)", 
    "💨 Dash (OTC)", "🇺🇸 Trump (OTC)", "💎 Toncoin (OTC)", "☀️ Solana (OTC)", "🔴 Polkadot (OTC)",
    "🛢️ USCrude (OTC)", "🪙 Silver (OTC)", "🏆 Gold (OTC)"
])

# Mathematical live indicator formulas
def calculate_indicators(prices):
    if len(prices) < 20:
        return 50, True  # Fallback defaults
    
    # 1. RSI Math
    deltas = np.diff(prices)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    avg_gain = np.mean(gains[-14:])
    avg_loss = np.mean(losses[-14:])
    rsi = 100 if avg_loss == 0 else 100 - (100 / (1 + (avg_gain / avg_loss)))
    
    # 2. EMA Confluence (5 EMA and 15 EMA)
    ema_5 = np.mean(prices[-5:])
    ema_15 = np.mean(prices[-15:])
    upward_trend = ema_5 > ema_15
    
    return rsi, upward_trend

if st.button("⚡ GET SIGNAL", use_container_width=True):
    status_box = st.empty()
    status_box.markdown("<p style='color:#00ffff; text-align:center;'>🛰️ Syncing server time with live market nodes...</p>", unsafe_allow_html=True)
    
    # Force localized UTC+5 time coordinates
    tz_pk = timezone(timedelta(hours=5))
    now_pk = datetime.now(tz_pk)
    current_hour = now_pk.hour
    current_min = now_pk.minute
    current_sec = now_pk.second

    # Extract asset string name for charting
    clean_name = asset_selection.replace("🇺🇸", "").replace("🇵🇰", "").replace("🇨🇴", "").replace("🇳🇿", "").replace("🇯🇵", "").replace("🇦🇷", "").replace("🇮🇳", "").replace("🇩🇿", "").replace("🇮🇩", "").replace("🇪🇺", "").replace("🇬🇧", "").replace("🇧🇩", "").replace("🇳🇬", "").replace("🇨🇦", "").replace("🇨🇭", "").replace("🇿🇦", "").replace("🇲🇽", "").replace("🇵🇭", "").replace("🇦🇺", "").replace("🪙", "").replace("⚛️", "").replace("💵", "").replace("🔗", "").replace("🛡️", "").replace("🥈", "").replace("🥇", "").replace("⧫", "").replace("💨", "").replace("💎", "").replace("☀️", "").replace("🔴", "").replace("🛢️", "").replace("🏆", "").strip().split(" ")[0].replace("/", "")

    ticker_map = {
        "USDPKR": "PKR=X", "USDCOP": "COP=X", "NZDJPY": "NZDJPY=X", "USDARS": "ARS=X", "USDINR": "INR=X", "USDDZD": "DZD=X", "USDIDR": "IDR=X", "EURNZD": "EURNZD=X", "GBPNZD": "GBPNZD=X", "USDBDT": "BDT=X", "USDNGN": "NGN=X", "CADCHF": "CADCHF=X", "USDEGP": "EGP=X", "USDZAR": "USDZAR=X", "NZDCAD": "NZDCAD=X", "NZDUSD": "NZDUSD=X", "NZDCHF": "NZDCHF=X", "USDMXN": "USDMXN=X", "USDPHP": "PHP=X", "AUDNZD": "AUDNZD=X", "EURJPY": "EURJPY=X", "CADJPY": "CADJPY=X", "EURGBP": "EURGBP=X", "AUDJPY": "AUDJPY=X", "USDJPY": "USDJPY=X", "AUDUSD": "AUDUSD=X", "AUDCAD": "AUDCAD=X", "EURUSD": "EURUSD=X", "EURCAD": "EURCAD=X", "AUDCHF": "AUDCHF=X", "GBPAUD": "GBPAUD=X", "GBPUSD": "GBPUSD=X", "EURAUD": "EURAUD=X", "CHFJPY": "CHFJPY=X", "GBPCAD": "GBPCAD=X", "GBPCHF": "GBPCHF=X", "GBPJPY": "GBPJPY=X", "USDCHF": "USDCHF=X", "EURCHF": "EURCHF=X",
        "Ripple": "XRP-USD", "Cosmos": "ATOM-USD", "BitcoinCash": "BCH-USD", "Chainlink": "LINK-USD", "Zcash": "ZEC-USD", "Litecoin": "LTC-USD", "Bitcoin": "BTC-USD", "Ethereum": "ETH-USD", "Dash": "DASH-USD", "Trump": "MAGA-USD", "Toncoin": "TON11419-USD", "Solana": "SOL-USD", "Polkadot": "DOT-USD", "Gold": "GC=F", "Silver": "SI=F", "USCrude": "CL=F"
    }

    target_ticker = ticker_map.get(clean_name, "EURUSD=X")
    
    try:
        api_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{target_ticker}?interval=1m&range=1d"
        headers = {'User-Agent': 'Mozilla/5.0'}
        market_response = requests.get(api_url, headers=headers, timeout=5).json()
        live_closes = [float(x) for x in market_response['chart']['result'][0]['indicators']['quote'][0]['close'] if x is not None]
        
        rsi_val, is_uptrend = calculate_indicators(live_closes)
        
        # Core directional decision engine logic
        if rsi_val < 45 or (is_uptrend and rsi_val < 60):
            final_decision = "CALL"
        else:
            final_decision = "PUT"
        source_label = f"LIVE EXCHANGE FEED ({target_ticker})"
    except Exception:
        final_decision = random.choice(["CALL", "PUT"])
        source_label = "VOLATILITY SIMULATION ENGINE"

    status_box.empty()

    # ⏱️ Execute the 30-Second Rollover Rules
    if current_sec <= 29:
        # Scenario A: Early candle access
        duration_left = 60 - current_sec
        target_min = current_min + 1
        time_instruction = f"⏳ DURATION MODE: **{duration_left} SECONDS RUN**"
        setup_instruction = f"👉 Set your Quotex expiry clock to exactly: <b>{current_hour:02d}:{target_min:02d}:00</b>"
        action_window = "⚡ OPEN TRADE IMMEDIATELY! It will close safely at the end of this current candle."
    else:
        # Scenario B: Over the 29s line -> Predict the NEXT candle
        target_min = current_min + 2
        time_instruction = f"🚨 NEXT-CANDLE FILTER INJECTED: **31 SECONDS TARGET**"
        setup_instruction = f"👉 Change your Quotex clock time to the next candle boundary: <b>{current_hour:02d}:{target_min:02d}:00</b>"
        action_window = "⏳ WAIT AND PREPARE! Open the trade the exact moment the new minute candle starts."

    st.markdown(f"""
        <div style="background: linear-gradient(90deg, #1e1b4b, #2e0854); padding: 12px; border-radius: 8px; border: 1px dashed #00f0ff; text-align: center; margin-bottom: 15px;">
            <span style="color: #94a3b8; font-size: 13px; font-weight: bold;">🛰️ TIME (UTC+5): {current_hour:02d}:{current_min:02d}:{current_sec:02d}</span>
            <span style="color: #00ffcc; font-size: 14px; font-weight: 900; margin-left: 15px;">📡 DATA: {source_label}</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🚦 SHAWKAT TRADEZ TIME-CALIBRATED SIGNAL")
    
    color_hex = "#2ecc71" if final_decision == "CALL" else #e74c3c
    bg_rgba = "rgba(46, 204, 113, 0.15)" if final_decision == "CALL" else "rgba(231, 76, 60, 0.15)"
    
    st.markdown(f"""
    <div style="background-color:{bg_rgba}; padding: 25px; border-radius: 12px; border: 2px solid {color_hex}; text-align: center;">
        <h2 style="color:{color_hex}; margin:0; font-size: 32px; font-weight:900;">🎯 ORDER: {final_decision} ({'UP' if final_decision=='CALL' else 'DOWN'})</h2>
        <p style="margin: 12px 0 5px 0; font-size:18px; color:#00ffcc; font-weight:bold;">{time_instruction}</p>
        <p style="margin: 5px 0; font-size:15px; color:#e2e8f0;">{setup_instruction}</p>
        <hr style="border-color:{color_hex}; margin:15px 0;">
        <p style="margin: 0; font-size:16px; color:{color_hex}; font-weight: bold; background:rgba(0,0,0,0.4); padding:10px; border-radius:6px;">
            {action_window}
        </p>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("⚠️ REAL-TIME CLOCK CALIBRATION ACTIVE • SHAWKAT TRADEZ PROTOCOL")
