import streamlit as st
import requests

# Page layout tailored for a premium mobile tracking interface
st.set_page_config(page_title="AI Alpha Quotex Pro Matrix", layout="centered")

st.title("🦅 AI Alpha Signal Matrix")
st.caption("Quotex Binary Options Engine • Standard & OTC Modes")
st.markdown("---")

# 1. Market Mode and Asset Selection
market_mode = st.radio("📈 Choose Market Type", ["Standard Live Feed", "Simulated OTC Structure Mode"])
asset_selection = st.selectbox("💱 Select Currency Asset", ["EURUSD", "GBPJPY", "GBPUSD", "USDJPY"])
timeframe_selection = st.selectbox("⏳ Select Processing Chart Timeframe", ["1m", "5m", "15m"])

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
if st.button("⚡ Scan Reversal Confluences", use_container_width=True):
    with st.spinner("Streaming data matrices..."):
        try:
            # Map selected pairs to data streams
            symbol_map = {
                "EURUSD": "EURUSD=X",
                "GBPJPY": "GBPJPY=X",
                "GBPUSD": "GBPUSD=X",
                "USDJPY": "USDJPY=X"
            }
            yf_symbol = symbol_map[asset_selection]
            
            # Requesting live chart segments
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{yf_symbol}?interval={timeframe_selection}&range=5d"
            headers = {'User-Agent': 'Mozilla/5.0'}
            
            response = requests.get(url, headers=headers).json()
            result = response['chart']['result'][0]
            
            closing_prices = [float(x) for x in result['indicators']['quote'][0]['close'] if x is not None]
            high_extremes = [float(x) for x in result['indicators']['quote'][0]['high'] if x is not None]
            low_extremes = [float(x) for x in result['indicators']['quote'][0]['low'] if x is not None]
            
            if len(closing_prices) < 30:
                st.error("⚠️ Incomplete data. Market might be closed or data stream delayed.")
            else:
                live_price = closing_prices[-1]
                
                # Dynamic Threshold adjustments based on selected mode
                if market_mode == "Simulated OTC Structure Mode":
                    # OTC simulation models strict overextended bounds to counter algorithmic trends
                    rsi_oversold = 28
                    rsi_overbought = 72
                    lookback_bars = 10  # Faster trend shifts
                else:
                    rsi_oversold = 32
                    rsi_overbought = 68
                    lookback_bars = 18

                # Compute indicators
                current_rsi = compute_rsi(closing_prices, 14)
                live_ema9 = compute_ema(closing_prices, 9)[-1]
                live_ema21 = compute_ema(closing_prices, 21)[-1]
                
                # Setup Binary Support & Resistance lookbacks
                structural_resistance = max(high_extremes[-lookback_bars:-1])
                structural_support = min(low_extremes[-lookback_bars:-1])
                
                # 3. Decision Matrix Score Engine
                conv_score = 0
                if live_ema9 > live_ema21: conv_score += 1
                else: conv_score -= 1
                    
                if current_rsi < rsi_oversold: conv_score += 2
                elif current_rsi > rsi_overbought: conv_score -= 2
                    
                if (live_price - structural_support) < (structural_resistance - live_price):
                    conv_score += 1
                else:
                    conv_score -= 1

                # Dynamic Expiration calculation matching the chart interval
                expiry_time = "1 to 2 Minutes" if timeframe_selection == "1m" else "3 to 5 Minutes"

                # 4. Binary Interface Verdict Output
                st.markdown(f"### 🚦 Quotex Verdict ({market_mode})")
                
                if conv_score >= 2:
                    st.success("🟢 **EXECUTE: CALL (UP)**")
                    st.markdown(f"⏱️ **Recommended Expiry Duration:** `{expiry_time}`")
                    st.info(f"💡 **Analysis:** Asset is extremely deep oversold ({current_rsi:.1f}) near floor support ({structural_support:.5f}). Bullish bounce wave expected.")
                elif conv_score <= -2:
                    st.error("🔴 **EXECUTE: PUT (DOWN)**")
                    st.markdown(f"⏱️ **Recommended Expiry Duration:** `{expiry_time}`")
                    st.info(f"💡 **Analysis:** Asset is highly overextended ({current_rsi:.1f}) approaching ceiling resistance ({structural_resistance:.5f}). Bearish drop wave expected.")
                else:
                    st.warning("⚪ **STATUS: NO TRADE (STAY OUT)**")
                    st.info("💡 **Analysis:** Market parameters are hovering within neutral trading zones. Avoid placing entry orders.")

                # 5. Core Data Metrics Display
                st.markdown("---")
                st.markdown("### 📊 Metrics Terminal Feed")
                left_col, right_col = st.columns(2)
                
                with left_col:
                    st.metric("Live Market Price", f"{live_price:.5f}")
                    st.metric("RSI Oscillator", f"{current_rsi:.2f}")
                with right_col:
                    st.metric("Ceiling (Resistance)", f"{structural_resistance:.5f}")
                    st.metric("Floor (Support)", f"{structural_support:.5f}")
                
        except Exception as error_msg:
            st.error("Data stream timeout. Make sure the asset has weekend pricing arrays active.")
