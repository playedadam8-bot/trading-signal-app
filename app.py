import streamlit as st
import requests
import time

# Page layout tailored for a premium mobile tracking interface
st.set_page_config(page_title="AI Alpha Signal Matrix", layout="centered")

st.title("🦅 AI Alpha Signal Matrix")
st.caption("Advanced Confluence Scanning Engine • Live Forex Markets")
st.markdown("---")

# 1. Forex Only Selector Block
asset_selection = st.selectbox("💱 Select Forex Currency Pair", ["EURUSD", "GBPJPY", "GBPUSD", "USDJPY"])
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
    with st.spinner("Streaming real-time interbank orderbook..."):
        try:
            # Map selected pairs to Yahoo Finance Forex API symbols
            symbol_map = {
                "EURUSD": "EURUSD=X",
                "GBPJPY": "GBPJPY=X",
                "GBPUSD": "GBPUSD=X",
                "USDJPY": "USDJPY=X"
            }
            yf_symbol = symbol_map[asset_selection]
            
            # Map interval names to Yahoo format
            interval_map = {"1m": "1m", "5m": "5m", "15m": "15m", "1h": "1h"}
            yf_interval = interval_map[timeframe_selection]
            
            # Fetching fresh Forex candles completely free without API keys
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{yf_symbol}?interval={yf_interval}&range=5d"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            
            response = requests.get(url, headers=headers).json()
            result = response['chart']['result'][0]
            
            # Extract live OHLC price vectors
            closing_prices = [float(x) for x in result['indicators']['quote'][0]['close'] if x is not None]
            high_extremes = [float(x) for x in result['indicators']['quote'][0]['high'] if x is not None]
            low_extremes = [float(x) for x in result['indicators']['quote'][0]['low'] if x is not None]
            
            if len(closing_prices) < 25:
                st.error("⚠️ Incomplete market feed. Try changing the timeframe or verify if the Forex market is open (closed on weekends).")
            else:
                live_price = closing_prices[-1]
                
                # Compute indicators
                current_rsi = compute_rsi(closing_prices, 14)
                live_ema9 = compute_ema(closing_prices, 9)[-1]
                live_ema21 = compute_ema(closing_prices, 21)[-1]
                
                # Structural parameters
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
                    st.info(f"💡 **Analysis:** {asset_selection} is highly oversold ({current_rsi:.1f}) near structural support ({structural_support:.5f}). Bullish bounce likely.")
                elif conv_score <= -2:
                    st.error("🔴 **STRONG DOWN (SELL CONFLUENCE)**")
                    st.info(f"💡 **Analysis:** {asset_selection} is heavily overextended ({current_rsi:.1f}) pushing structural resistance ({structural_resistance:.5f}). Bearish drop likely.")
                else:
                    st.warning("⚪ **NEUTRAL (CONSOLIDATION NO-TRADE ZONE)**")
                    st.info("💡 **Analysis:** Structural levels and indicators conflict. Market is tracking sideways inside a tight range.")

                # 5. Core Data Metrics Display
                st.markdown("---")
                st.markdown("### 📊 Metrics Terminal Dashboard")
                left_col, right_col = st.columns(2)
                
                with left_col:
                    st.metric("Live Forex Price", f"{live_price:.5f}")
                    st.metric("RSI Oscillator Value", f"{current_rsi:.2f}")
                with right_col:
                    st.metric("Structural Resistance", f"{structural_resistance:.5f}")
                    st.metric("Structural Support", f"{structural_support:.5f}")
                
        except Exception as error_msg:
            st.error(f"Forex market connection issue: Make sure the interbank market is open.")
