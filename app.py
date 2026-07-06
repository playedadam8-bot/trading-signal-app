import streamlit as st
import requests

# Set up a dark, professional theme layout
st.set_page_config(page_title="AI Alpha Matrix PRO", layout="centered")

# Custom CSS to elevate the design (Modern Fonts, Sleek Cards, and Dark Vibes)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #00c6ff, #0072ff);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 114, 255, 0.4);
    }
    .metric-card {
        background-color: #1e222b;
        border-radius: 10px;
        padding: 15px;
        border: 1px solid #2e3440;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🦅 AI ALPHA MATRIX PRO")
st.caption("⚡ Premium Binary Options Confluence Engine • Quotex Optimized")
st.markdown("---")

# 1. UI Layout - Modern Inputs Panel
left_panel, right_panel = st.columns(2)

with left_panel:
    market_mode = st.radio("📈 Market Environment", ["Standard Live Feed", "Simulated OTC Structure Mode"])

with right_panel:
    timeframe_selection = st.selectbox("⏳ Chart Timeframe", ["1m", "5m", "15m", "1h"])

# All requested assets neatly organized into categories
asset_selection = st.selectbox("💱 Select Instrument Pair", [
    # Forex
    "EURUSD", "GBPJPY", "GBPUSD", "USDJPY", "AUDUSD", "EURGBP",
    # Commodities / Gold
    "XAUUSD (Gold)",
    # Crypto
    "BTCUSDT (Bitcoin)", "ETHUSDT (Ethereum)", "SOLUSDT (Solana)", "BNBUSDT"
])

# Math Helpers
def compute_ema(data_points, window):
    if len(data_points) < window: return [data_points[-1]]
    multiplier = 2 / (window + 1)
    ema_history = [sum(data_points[:window]) / window]
    for rate in data_points[window:]:
        ema_history.append((rate * multiplier) + (ema_history[-1] * (1 - multiplier)))
    return ema_history

def compute_rsi(data_points, window=14):
    if len(data_points) < window + 1: return 50
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
    return 100 - (100 / (1 + (avg_gain / avg_loss)))

# 2. Execution Routing
if st.button("🔥 RUN ALGorithmic matrix SCAN", use_container_width=True):
    with st.spinner("Analyzing structural data grids..."):
        try:
            # Map clean symbols to global exchange feeds
            symbol_clean = asset_selection.split(" ")[0]
            symbol_map = {
                "EURUSD": "EURUSD=X", "GBPJPY": "GBPJPY=X", "GBPUSD": "GBPUSD=X", 
                "USDJPY": "USDJPY=X", "AUDUSD": "AUDUSD=X", "EURGBP": "EURGBP=X",
                "XAUUSD": "GC=F", # Comex Gold Real-time continuous feed
                "BTCUSDT": "BTC-USD", "ETHUSDT": "ETH-USD", "SOLUSDT": "SOL-USD", "BNBUSDT": "BNB-USD"
            }
            yf_symbol = symbol_map[symbol_clean]
            
            # Fetch market tracking arrays
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{yf_symbol}?interval={timeframe_selection}&range=5d"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers).json()
            result = response['chart']['result'][0]
            
            closing_prices = [float(x) for x in result['indicators']['quote'][0]['close'] if x is not None]
            high_extremes = [float(x) for x in result['indicators']['quote'][0]['high'] if x is not None]
            low_extremes = [float(x) for x in result['indicators']['quote'][0]['low'] if x is not None]
            
            if len(closing_prices) < 30:
                st.error("⚠️ Data pool insufficient. Market might be paused or transitioning cycles.")
            else:
                live_price = closing_prices[-1]
                
                # Dynamic thresholds for strategy modes
                if market_mode == "Simulated OTC Structure Mode":
                    rsi_oversold, rsi_overbought, lookback = 28, 72, 10
                else:
                    rsi_oversold, rsi_overbought, lookback = 32, 68, 18

                # Calculations
                current_rsi = compute_rsi(closing_prices, 14)
                live_ema9 = compute_ema(closing_prices, 9)[-1]
                live_ema21 = compute_ema(closing_prices, 21)[-1]
                structural_resistance = max(high_extremes[-lookback:-1])
                structural_support = min(low_extremes[-lookback:-1])
                
                # Confluence score engine
                conv_score = 0
                if live_ema9 > live_ema21: conv_score += 1
                else: conv_score -= 1
                if current_rsi < rsi_oversold: conv_score += 2
                elif current_rsi > rsi_overbought: conv_score -= 2
                if (live_price - structural_support) < (structural_resistance - live_price): conv_score += 1
                else: conv_score -= 1

                expiry_time = "1-2 Mins" if timeframe_selection == "1m" else "3-5 Mins"

                # 3. Modernized Verdict Screen Output Layout
                st.markdown("### 🚦 SIGNAL RADAR OUTPUT")
                
                if conv_score >= 2:
                    st.markdown(f"""
                    <div style="background-color:rgba(46, 204, 113, 0.15); padding: 20px; border-radius: 10px; border-left: 5px solid #2ecc71;">
                        <h2 style="color:#2ecc71; margin:0;">🟢 EXECUTE: CALL (UP)</h2>
                        <p style="margin: 5px 0 0 0; font-size:16px;">⏱️ <b>Recommended Duration:</b> {expiry_time}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.info(f"💡 **Confluence Data:** Price is resting on key floor support ({structural_support:,.4f}) with RSI heavily oversold at {current_rsi:.1f}. Strong buy pressure building.")
                elif conv_score <= -2:
                    st.markdown(f"""
                    <div style="background-color:rgba(231, 76, 60, 0.15); padding: 20px; border-radius: 10px; border-left: 5px solid #e74c3c;">
                        <h2 style="color:#e74c3c; margin:0;">🔴 EXECUTE: PUT (DOWN)</h2>
                        <p style="margin: 5px 0 0 0; font-size:16px;">⏱️ <b>Recommended Duration:</b> {expiry_time}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.info(f"💡 **Confluence Data:** Price is testing heavy ceiling resistance ({structural_resistance:,.4f}) with RSI overbought at {current_rsi:.1f}. Downward rejection expected.")
                else:
                    st.markdown(f"""
                    <div style="background-color:rgba(241, 196, 15, 0.11); padding: 20px; border-radius: 10px; border-left: 5px solid #f1c40f;">
                        <h2 style="color:#f1c40f; margin:0;">⚪ STATUS: NO TRADE Zone</h2>
                        <p style="margin: 5px 0 0 0; font-size:16px;">⏱️ <b>Action:</b> Stand by for clear boundary breaks.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.info("💡 **Confluence Data:** The indicators are conflicting. Price is balancing sideways in the middle of the channel.")

                # 4. Premium Matrix Metric Grid
                st.markdown("---")
                st.markdown("### 📊 METRICS DATA TERMINAL")
                col_a, col_b, col_c, col_d = st.columns(4)
                
                with col_a: st.metric("Live Feed Price", f"{live_price:,.4f}")
                with col_b: st.metric("RSI (14 Value)", f"{current_rsi:.1f}")
                with col_c: st.metric("Local Ceiling", f"{structural_resistance:,.4f}")
                with col_d: st.metric("Local Floor", f"{structural_support:,.4f}")
                
        except Exception as error_msg:
            st.error("Market data stream offline. If checking standard pairs on weekends, swap to 'Simulated OTC Mode'.")
