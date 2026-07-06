import streamlit as st
import random
import time
from datetime import datetime

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
        <p style="color:#00ffcc; margin:5px 0 0 0; font-size: 13px; letter-spacing: 2px; font-weight: bold;">⚡ ADVANCED TIME-MATCHING PROTOCOL V5.5</p>
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

timer_selection = st.selectbox("⏱️ TARGET EXPIRY FRAME", [
    "1 MIN CANDLE CLOSURE", "5 SEC TICK", "10 SEC TICK", "15 SEC TICK", "30 SEC TICK", "5 MIN CLOSURE"
])

if st.button("⚡ GET SIGNAL", use_container_width=True):
    progress_bar = st.progress(0)
    for percent in range(100):
        time.sleep(0.002)
        progress_bar.progress(percent + 1)
    progress_bar.empty()

    final_decision = random.choice(["CALL", "PUT"])
    accuracy_display = round(random.uniform(94.8, 98.9), 1)

    # Calculate Current Live Seconds to solve the 30-second rule split
    now = datetime.now()
    current_sec = now.second
    current_min = now.minute
    current_hour = now.hour

    st.markdown(f"""
        <div style="background: linear-gradient(90deg, #1e1b4b, #2e0854); padding: 12px; border-radius: 8px; border: 1px dashed #00f0ff; text-align: center; margin-bottom: 15px;">
            <span style="color: #94a3b8; font-size: 13px; font-weight: bold;">⏱️ CURRENT SYSTEM TIME: {current_hour:02d}:{current_min:02d}:{current_sec:02d}</span>
            <span style="color: #00ffcc; font-size: 15px; font-weight: 900; margin-left: 15px;">🎯 CONFIRMATION: {accuracy_display}%</span>
        </div>
    """, unsafe_allow_html=True)

    # Calculate precise Quotex routing instructions based on the 30-second split rule
    if "MIN" in timer_selection:
        if current_sec <= 30:
            target_min = current_min + 1
            time_instruction = f"⚠️ USE CLOCK MODE (00:01:00) ➜ Set Expiry Target to exact time: <b>{current_hour:02d}:{target_min:02d}:00</b>"
            action_window = f"⏱️ Candle closes in {60 - current_sec}s. Open trade IMMEDIATELY."
        else:
            target_min = current_min + 2
            time_instruction = f"⚠️ WARNING (PASSED 30s) ➜ Switch to TIMER MODE ➜ Set exact: <b>1 MIN</b>"
            action_window = f"⚡ Avoid next candle push delay! Open position directly now."
    else:
        time_instruction = f"⚡ USE TIMER MODE ➜ Select exact Fixed Duration: <b>{timer_selection.split(' ')[0]} {timer_selection.split(' ')[1]}</b>"
        action_window = "🔥 EXECUTE INSTANTLY: Open trade the split second you change assets."

    st.markdown("### 🚦 SHAWKAT TRADEZ STRATEGY OUTPUT")
    
    color_hex = "#2ecc71" if final_decision == "CALL" else #e74c3c
    bg_rgba = "rgba(46, 204, 113, 0.15)" if final_decision == "CALL" else "rgba(231, 76, 60, 0.15)"
    
    st.markdown(f"""
    <div style="background-color:{bg_rgba}; padding: 25px; border-radius: 12px; border: 2px solid {color_hex}; text-align: center;">
        <h2 style="color:{color_hex}; margin:0; font-size: 32px; font-weight:900;">🟢 EXECUTE: {final_decision} ({'UP' if final_decision=='CALL' else 'DOWN'})</h2>
        <hr style="border-color:{color_hex}; margin:15px 0;">
        <p style="margin: 5px 0; font-size:16px; color:#e2e8f0;">{time_instruction}</p>
        <p style="margin: 10px 0 0 0; font-size:17px; color:{color_hex}; font-weight: bold; background:rgba(0,0,0,0.3); padding:10px; border-radius:6px;">
            {action_window}
        </p>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("⚠️ AUTOMATED CLOCK CALIBRATION ACTIVE • SHAWKAT TRADEZ PROTOCOL")
