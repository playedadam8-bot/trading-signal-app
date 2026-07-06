import streamlit as st
import requests

# Set up a dark, premium trading matrix layout
st.set_page_config(page_title="SHAWKAT TRADEZ MEGA MATRIX", layout="centered")

# Custom UI styling matching high-end terminal platforms
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
    </style>
""", unsafe_allow_html=True)

st.title("🦅 SHAWKAT TRADEZ MEGA MATRIX")
st.caption("⚡ 24/7 Non-Stop Quant Confluence Engine • Optimized for Quotex Binary Options")
st.markdown("---")

# UI Configuration Panel
left_panel, right_panel = st.columns(2)
with left_panel:
    market_mode = st.radio("📈 Analytics Processing Engine", ["Standard Live Feed", "Simulated OTC Structure Mode"])
with right_panel:
    timeframe_selection = st.selectbox("⏳ Chart Timeframe Interval", ["1m", "5m", "15m", "1h"])

# Complete Quotex Asset Roster List
asset_selection = st.selectbox("💱 Select Target Instrument Pair", [
    # Currencies Part 1
    "USD/PKR", "USD/COP", "NZD/JPY", "USD/ARS", "USD/INR", "USD/DZD", 
    "USD/IDR", "EUR/NZD", "GBP/NZD", "USD/BDT", "USD/NGN", "CAD/CHF", "USD/EGP",
    # Currencies Part 2
    "USD/ZAR", "NZD/CAD", "NZD/USD", "NZD/CHF", "USD/MXN", "USD/PHP", 
    "AUD/NZD", "EUR/JPY", "CAD/JPY", "EUR/GBP", "AUD/JPY", "USD/JPY", "AUD/USD",
    # Currencies Part 3
    "AUD/CAD", "EUR/USD", "EUR/CAD", "AUD/CHF", "GBP/AUD", "GBP/USD", 
    "EUR/AUD", "CHF/JPY", "GBP/CAD", "GBP/CHF", "GBP/JPY", "USD/CHF", "EUR/CHF",
    # Crypto
    "Ripple (XRP)", "Cosmos (ATOM)", "Bitcoin Cash (BCH)", "Chainlink (LINK)", 
    "Zcash (ZEC)", "Litecoin (LTC)", "Bitcoin (BTC)", "Ethereum (ETH)", 
    "Dash (DASH)", "Trump (MAGA)", "Toncoin (TON)", "Solana (SOL)", "Polkadot (DOT)",
    # Commodities
    "Gold (XAUUSD)", "Silver (XAGUSD)", "USCrude (WTI)"
])

# Mathematical Engine Blocks
def compute_ema(data, window):
    if len(data) < window: return [data[-1]]
    k = 2 / (window + 1)
    ema = [sum(data[:window]) / window]
    for price in data[window:]:
        ema.append((price * k) + (ema[-1] * (1 - k)))
    return b_ema if 'b_ema' in locals() else ema

def compute_rsi(data, window=14):
    if len(data) < window + 1: return 50
    gains, losses = [], []
    for i in range(1, len(data)):
        diff = data[i] - data[i-1]
        gains.append(diff if diff > 0 else 0)
        losses.append(abs(diff) if diff < 0 else 0)
    avg_gain = sum(gains[:window]) / window
    avg_loss = sum(losses[:window]) / window
    for i in range(window, len(gains)):
        avg_gain = (avg_gain * (window - 1) + gains[i]) / window
        avg_loss = (avg_loss * (window - 1) + losses[i]) / window
    return 100 if avg_loss == 0 else 100 - (100 / (1 + (avg_gain / avg_loss)))

def compute_stochastic(closing, high, low, k_window=14, d_window=3):
    if len(closing) < k_window: return 50, 50
    k_values = []
    for i in range(len(closing) - k_window + 1):
        highest_high = max(high[i:i+k_window])
        lowest_low = min(low[i:i+k_window])
        current_close = closing[i+k_window-1]
        if (highest_high - lowest_low) == 0: k_val = 50
        else: k_val = ((current_close - lowest_low) / (highest_high - lowest_low)) * 100
        k_values.append(k_val)
    current_k = k_values[-1]
    current_d = sum(k_values[-d_window:]) / d_window
    return current_k, current_d

def compute_bollinger_bands(data, window=20, num_std=2):
    if len(data) < window: return data[-1], data[-1], data[-1]
    sma = sum(data[-window:]) / window
    variance = sum((x - sma) ** 2 for x in data[-window:]) / window
    std_dev = variance ** 0.5
    return sma, sma + (num_std * std_dev), sma - (num_std * std_dev)

# Strategy Scan Trigger
if st.button("🔥 RUN SHAWKAT TRADEZ MULTI-INDICATOR MATRIX", use_container_width=True):
    with st.spinner("Streaming real-time orderbooks across algorithmic structures..."):
        try:
            symbol_clean = asset_selection.split(" ")[0].replace("/", "")
            symbol_map = {
                "USDPKR": "PKR=X", "USDCOP": "COP=X", "NZDJPY": "NZDJPY=X", "USDARS": "ARS=X", 
                "USDINR": "INR=X", "USDDZD": "DZD=X", "USDIDR": "IDR=X", "EURNZD": "EURNZD=X", 
                "GBPNZD": "GBPNZD=X", "USDBDT": "BDT=X", "USDNGN": "NGN=X", "CADCHF": "CADCHF=X", 
                "USDEGP": "EGP=X", "USDZAR": "USDZAR=X", "NZDCAD": "NZDCAD=X", "NZDUSD": "NZDUSD=X", 
                "NZDCHF": "NZDCHF=X", "USDMXN": "USDMXN=X", "USDPHP": "PHP=X", "AUDNZD": "AUDNZD=X", 
                "EURJPY": "EURJPY=X", "CADJPY": "CADJPY=X", "EURGBP": "EURGBP=X", "AUDJPY": "AUDJPY=X", 
                "USDJPY": "USDJPY=X", "AUDUSD": "AUDUSD=X", "AUDCAD": "AUDCAD=X", "EURUSD": "EURUSD=X", 
                "EURCAD": "EURCAD=X", "AUDCHF": "AUDCHF=X", "GBPAUD": "GBPAUD=X", "GBPUSD": "GBPUSD=X", 
                "EURAUD": "EURAUD=X", "CHFJPY": "CHFJPY=X", "GBPCAD": "GBPCAD=X", "GBPCHF": "GBPCHF=X", 
                "GBPJPY": "GBPJPY=X", "USDCHF": "USDCHF=X", "EURCHF": "EURCHF=X",
                "Ripple": "XRP-USD", "Cosmos": "ATOM-USD", "BitcoinCash": "BCH-USD", "Chainlink": "LINK-USD", 
                "Zcash": "ZEC-USD", "Litecoin": "LTC-USD", "Bitcoin": "BTC-USD", "Ethereum": "ETH-USD", 
                "Dash": "DASH-USD", "Trump": "MAGA-USD", "Toncoin": "TON11419-USD", "Solana": "SOL-USD", "Polkadot": "DOT-USD",
                "Gold": "GC=F", "Silver": "SI=F", "USCrude": "CL=F"
            }
            
            yf_symbol = symbol_map.get(symbol_clean, "EURUSD=X")
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{yf_symbol}?interval={timeframe_selection}&range=5d"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers).json()
            result = response['chart']['result'][0]
            
            closing_prices = [float(x) for x in result['indicators']['quote'][0]['close'] if x is not None]
            high_extremes = [float(x) for x in result['indicators']['quote'][0]['high'] if x is not None]
            low_extremes = [float(x) for x in result['indicators']['quote'][0]['low'] if x is not None]
            
            if len(closing_prices) < 30:
                st.error("⚠️ Data pool stream initialization error. Toggle mode to 'Simulated OTC Structure Mode' for weekend trading.")
            else:
                live_price = closing_prices[-1]
                
                # Dynamic thresholds for strategy modes
                if market_mode == "Simulated OTC Structure Mode":
                    rsi_oversold, rsi_overbought, lookback = 28, 72, 10
                    stoch_oversold, stoch_overbought = 18, 82
                else:
                    rsi_oversold, rsi_overbought, lookback = 32, 68, 18
                    stoch_oversold, stoch_overbought = 22, 78

                # Execute Indicators Core
                current_rsi = compute_rsi(closing_prices, 14)
                live_ema9 = compute_ema(closing_prices, 9)[-1]
                live_ema21 = compute_ema(closing_prices, 21)[-1]
                stoch_k, stoch_d = compute_stochastic(closing_prices, high_extremes, low_extremes)
                mid_bb, upper_bb, lower_bb = compute_bollinger_bands(closing_prices)
                
                structural_resistance = max(high_extremes[-lookback:-1])
                structural_support = min(low_extremes[-lookback:-1])
                
                # --- 5-STRATEGY CONFLUENCE SCORING ENGINE ---
                conv_score = 0
                
                # Strat 1: Trend Alignment (EMA Cross)
                if live_ema9 > live_ema21: conv_score += 1
                else: conv_score -= 1
                
                # Strat 2: RSI Exhaustion 
                if current_rsi < rsi_oversold: conv_score += 2
                elif current_rsi > rsi_overbought: conv_score -= 2
                
                # Strat 3: Local Structure Blocks
                if (live_price - structural_support) < (structural_resistance - live_price): conv_score += 1
                else: conv_score -= 1
                
                # Strat 4: Stochastic Reversal Turns
                if stoch_k < stoch_oversold and stoch_k > stoch_d: conv_score += 1
                elif stoch_k > stoch_overbought and stoch_k < stoch_d: conv_score -= 1
                
                # Strat 5: Bollinger Band Boundary Rejection
                if live_price <= lower_bb: conv_score += 1
                elif live_price >= upper_bb: conv_score -= 1

                expiry_time = "1-2 Minutes" if timeframe_selection == "1m" else "3-5 Minutes"

                st.markdown("### 🚦 SHAWKAT TRADEZ SIGNAL OUTPUT")
                
                if conv_score >= 3:
                    st.markdown(f"""
                    <div style="background-color:rgba(46, 204, 113, 0.15); padding: 20px; border-radius: 10px; border-left: 5px solid #2ecc71;">
                        <h2 style="color:#2ecc71; margin:0;">🟢 EXECUTE: CALL (UP)</h2>
                        <p style="margin: 5px 0 0 0; font-size:16px;">⏱️ <b>Quotex Expiry Duration:</b> Keep your chart default to <b>{expiry_time}</b></p>
                        <p style="margin: 5px 0 0 0; font-size:15px; color:#2ecc71;">⚡ <b>ENTRY WINDOW:</b> Open the trade exactly at the opening seconds of the next new candle!</p>
                    </div>
                    """, unsafe_allow_html=True)
                elif conv_score <= -3:
                    st.markdown(f"""
                    <div style="background-color:rgba(231, 76, 60, 0.15); padding: 20px; border-radius: 10px; border-left: 5px solid #e74c3c;">
                        <h2 style="color:#e74c3c; margin:0;">🔴 EXECUTE: PUT (DOWN)</h2>
                        <p style="margin: 5px 0 0 0; font-size:16px;">⏱️ <b>Quotex Expiry Duration:</b> Keep your chart default to <b>{expiry_time}</b></p>
                        <p style="margin: 5px 0 0 0; font-size:15px; color:#e74c3c;">⚡ <b>ENTRY WINDOW:</b> Open the trade exactly at the opening seconds of the next new candle!</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="background-color:rgba(241, 196, 15, 0.11); padding: 20px; border-radius: 10px; border-left: 5px solid #f1c40f;">
                        <h2 style="color:#f1c40f; margin:0;">⚪ STATUS: PATIENTLY WAIT (NO TRADE)</h2>
                        <p style="margin: 5px 0 0 0; font-size:16px;">⏱️ <b>Action:</b> Multi-indicators are conflicting. Hold your capital back until full confirmation occurs.</p>
                    </div>
                    """, unsafe_allow_html=True)

                # Advanced Indicators Data Panel
                st.markdown("---")
                st.markdown("### 📊 MULTI-INDICATOR METRICS MATRIX")
                
                col_1, col_2, col_3, col_4 = st.columns(4)
                with col_1: st.metric("Live Feed Price", f"{live_price:,.4f}")
                with col_2: st.metric("RSI Value", f"{current_rsi:.1f}")
                with col_3: st.metric("Stoch %K / %D", f"{stoch_k:.1f} / {stoch_d:.1f}")
                with col_4: st.metric("Score Alignment", f"{conv_score}")
                
                col_5, col_6, col_7 = st.columns(3)
                with col_5: st.metric("Upper Volatility BB", f"{upper_bb:,.4f}")
                with col_6: st.metric("Structural Ceiling", f"{structural_resistance:,.4f}")
                with col_7: st.metric("Structural Floor", f"{structural_support:,.4f}")
                
        except Exception as error_msg:
            st.error("Market data feed connection error. Ensure your environment mode selector matches the standard global sessions.")
