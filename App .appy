import streamlit as st
import requests

# Page layout tailored for a premium mobile tracking interface
st.set_page_config(page_title="AI Alpha Signal Matrix", layout="centered")

st.title("🦅 AI Alpha Signal Matrix")
st.caption("Advanced Confluence Scanning Engine • Forex & Crypto")
st.markdown("---")

# 1. Inputs Selector Block (Using globally available Binance Spot pairs)
asset_selection = st.selectbox("💱 Select Instrument Pair", ["BTCUSDT", "ETHUSDT", "SOLUSDT", "PAXGUSDT (Gold Token)"])
timeframe_selection = st.selectbox("⏳ Select Processing Timeframe", ["1m", "5m", "15m", "1h"])

# Math Helper: Exponential Moving Average
def compute_ema(data_points, window):
    if len(data_points) < window:
        return [data_points[-1]]
    multiplier = 2 / (window + 1)
    ema_history = [sum(data_points[:window]) / window]
    for rate in data_points[window:]:
        ema_history.append((rate * multiplier) + (ema_history[-1] * (1 - multiplier)))
    return ema_history

# Math Helper: Relative Strength Index 
def compute_rsi(data_points, window=14):
    if len(data_points) < window + 1:
        return 50
    gains, losses = [], []
    for i in range(1, len(data_points)):
        delta = data_points[i] - data_points[i-1]
        gains.append(delta if delta > 0 else 0)
        losses.append(abs(delta) if delta < 0 else 0)
    
    avg_gain = sum(gains[:window]) / window
    avg_loss = sum(losses[:window]) / window
    
    for i in range(window, len(gains)):
        avg_gain = (avg_gain * (window - 1) + gains[i]) / window
        avg_loss = (avg_loss * (window - 1) + losses[i]) / window
        
    if avg_loss == 0: return 100
    relative_strength = avg_gain / avg_loss
    return 100 - (100 / (1 + relative_strength))

# 2. Strategic Analyzer Core Execution
if st.button("🔍 Execute Algorithmic Deep Scan", use_container_width=True):
    with st.spinner("Streaming orderbook data..."):
        try:
            # Filter symbol text
            clean_symbol = asset_selection.split(" ")[0]
            
            # Using the highly stable public spot market endpoint
            endpoint_url = f"https://api.binance.com/api/v3/klines?symbol={clean_symbol}&interval={timeframe_selection}&limit=100"
            response = requests.get(endpoint_url)
            raw_feed = response.json()
            
            # Safety check: Ensure we received a valid list of candles
            if not isinstance(raw_feed, list) or len(raw_feed) == 0:
                st.error("⚠️ Connection timed out or symbol unavailable. Please try again in a moment.")
            else:
                # Parsing OHLC candle array structure safely
                closing_prices = [float(bar[4]) for bar in raw_feed]
                high_extremes = [float(bar[2]) for bar in raw_feed]
                low_extremes = [float(bar[3]) for bar in raw_feed]
                
                live_price = closing_prices[-1]
                
                # Compute indicators
                current_rsi = compute_rsi(closing_prices, 14)
                live_ema9 = compute_ema(closing_prices, 9)[-1]
                live_ema21 = compute_ema(closing_prices, 21)[-1]
                
                # Identify Key Support & Resistance over a 20-candle lookback zone
                structural_resistance = max(high_extremes[-20:-1])
                structural_support = min(low_extremes[-20:-1])
                
                # 3. Decision Matrix Score Engine
                conv_score = 0
                if live_ema9 > live_ema21: conv_score += 1
                else: conv_score -= 1
                    
                if current_rsi < 35: conv_score += 1
                elif current_rsi > 65: conv_score -= 1
                    
                if (live_price - structural_support) < (structural_resistance - live_price):
                    conv_score += 1
                else:
                    conv_score -= 1

                # 4. Interface Rendering 
                st.markdown("### 🚦 Engine Output Verdict")
                if conv_score >= 2:
                    st.success("🟢 **STRONG UP (BUY CONFLUENCE)**")
                    st.info(f"💡 **Analysis:** Market is oversold ({current_rsi:.1f}) and sitting near support ({structural_support:,}). Structure indicates an upward bounce.")
                elif conv_score <= -2:
                    st.error("🔴 **STRONG DOWN (SELL CONFLUENCE)**")
                    st.info(f"💡 **Analysis:** Price is overextended ({current_rsi:.1f}) and directly approaching resistance ({structural_resistance:,}). Downward rejection is likely.")
                else:
                    st.warning("⚪ **NEUTRAL (CONSOLIDATION NO-TRADE ZONE)**")
                    st.info("💡 **Analysis:** Moving averages and structural levels are conflicting. The market is tracking sideways.")

                # 5. Core Data Metrics Display
                st.markdown("---")
                st.markdown("### 📊 Metrics Terminal Dashboard")
                left_col, right_col = st.columns(2)
                
                with left_col:
                    st.metric("Live Market Price", f"{live_price:,}")
                    st.metric("RSI Oscillator Value", f"{current_rsi:.2f}")
                with right_col:
                    st.metric("Local Structural Resistance", f"{structural_resistance:,}")
                    st.metric("Local Structural Support", f"{structural_support:,}")
                
        except Exception as error_msg:
            st.error(f"Data interface delivery error: {error_msg}")
