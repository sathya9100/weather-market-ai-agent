import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
import pandas as pd

from agents.hermes_agent import run_system
from trading.trade_executor import execute_trade
from trading.close_position import close_position
from dashboard.research_feed import show_research_feed
from dashboard.risk_dashboard import show_risk_dashboard
from dashboard.charts import show_charts
from dashboard.market_summary import show_market_summary
from dashboard.prior_predictions import show_prior_predictions
from dashboard.hedge import show_hedge_suggestions
from dashboard.ai_summary import show_ai_summary
from database.init_db import initialize_database

initialize_database()

# ---------------------------------------
# Page Config
# ---------------------------------------

st.set_page_config(
    page_title="Weather AI Trading Terminal",
    page_icon="🌧️",
    layout="wide"
)

# ---------------------------------------
# Theme
# ---------------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#0d1117;
    color:white;
}

[data-testid="stMetricValue"]{
    color:#00ff99;
}

div[data-testid="metric-container"]{
    background:#161b22;
    border-radius:12px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.stButton > button{
    background-color:#238636 !important;
    color:white !important;
    border:none !important;
    border-radius:8px !important;
    font-weight:bold !important;
    width:100%;
    height:42px;
}

.stButton > button:hover{
    background-color:#2ea043 !important;
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Expander */
div[data-testid="stExpander"]{
    background-color:#161b22 !important;
    border:1px solid #30363d;
    border-radius:10px;
    color:white !important;
}

/* Expander Header */
div[data-testid="stExpander"] summary{
    background-color:#161b22 !important;
    color:white !important;
}

/* Hover */
div[data-testid="stExpander"] summary:hover{
    background-color:#21262d !important;
}

/* Focus (prevents white flash) */
div[data-testid="stExpander"] summary:focus{
    background-color:#161b22 !important;
    color:white !important;
    outline:none !important;
}

/* Remove white focus ring */
div[data-testid="stExpander"] summary:focus-visible{
    outline:none !important;
}

</style>
""", unsafe_allow_html=True)
# ---------------------------------------
# Run Hermes
# ---------------------------------------


@st.cache_data(ttl=10)
def load_market_data():
    return run_system()


# ---------------------------------------
# First Load
# ---------------------------------------
if "result" not in st.session_state:

    status = st.empty()

    status.markdown("""
    <div style="
    background:#161b22;
    padding:18px;
    border-radius:12px;
    border-left:5px solid #00ff99;
    color:white;
    font-size:18px;">
    🌍 <b>Initializing Weather AI Trading Terminal...</b>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.6)

    status.markdown("""
    <div style="
    background:#161b22;
    padding:18px;
    border-radius:12px;
    border-left:5px solid #00ff99;
    color:white;
    font-size:18px;">
    ⏳ <b>Collecting Global & Local Weather Data...</b>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.6)

    status.markdown("""
    <div style="
    background:#161b22;
    padding:18px;
    border-radius:12px;
    border-left:5px solid #00ff99;
    color:white;
    font-size:18px;">
    🤖 <b>Running Hermes AI Agents...</b>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.6)

    status.markdown("""
    <div style="
    background:#161b22;
    padding:18px;
    border-radius:12px;
    border-left:5px solid #00ff99;
    color:white;
    font-size:18px;">
    📈 <b>Building Trading Dashboard...</b>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.6)

    st.session_state.result = load_market_data()

    status.markdown("""
    <div style="
    background:#0f5132;
    padding:18px;
    border-radius:12px;
    border-left:5px solid #00ff99;
    color:white;
    font-size:18px;">
    ✅ <b>Dashboard Ready!</b>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(0.5)

    status.empty()


# ---------------------------------------
# Always Refresh Dashboard Data
# ---------------------------------------

load_market_data.clear()

st.session_state.result = load_market_data()

result = st.session_state.result

markets = result["markets"]
weather_data = result["weather_data"]
portfolio = result["portfolio"]
positions = result["positions"]
statistics = result["statistics"]

from trading.order_manager import get_all_orders

orders = get_all_orders()
all_orders = pd.DataFrame(orders)


# ---------------------------------------
# Title
# ---------------------------------------

st.markdown("# 🌧️ Weather AI Trading Terminal")

st.markdown("""
<h3 style="color:white; margin-top:-10px;">
AI-powered Weather Prediction & Paper Trading Platform
</h3>

<div style="
color:#3ddc84;
font-size:17px;
font-weight:600;
margin-top:-5px;
margin-bottom:20px;
">
🟢 Live Weather &nbsp; • &nbsp;
🟢 AI Research &nbsp; • &nbsp;
📈 Kelly Criterion &nbsp; • &nbsp;
🛡 Risk Management
</div>
""", unsafe_allow_html=True)

show_market_summary(markets)
st.divider()

# ---------------------------------------
# Portfolio
# ---------------------------------------
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    st.metric("Balance", f"${portfolio.get('balance', 0):,.0f}")

with col2:
    st.metric("Equity", f"${portfolio.get('equity', 0):,.0f}")

with col3:
    st.metric("Today's P/L", f"${portfolio.get('today_pl', 0):,.0f}")

with col4:
    st.metric("Available Cash", f"${portfolio.get('available_cash', 0):,.0f}")

with col5:
    st.metric("Invested Capital", f"${portfolio.get('invested_capital', 0):,.0f}")

with col6:
    st.metric("Capital at Risk", f"${portfolio.get('capital_at_risk', 0):,.0f}")

with col7:
    st.metric("Open Positions", portfolio.get("open_positions", 0))

st.divider()
# ---------------------------------------
# Market Watch
# ---------------------------------------

st.subheader("📈 Market Watch")
header = st.columns([2,2,2,2,2,2,1,1])

header[0].markdown("**City**")
header[1].markdown("**Probability**")
header[2].markdown("**Signal**")
header[3].markdown("**Confidence**")
header[4].markdown("**Kelly %**")
header[5].markdown("**Investment**")
header[6].markdown("**BUY YES**")
header[7].markdown("**BUY NO**")

st.divider()

for market in markets:

    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([2,2,2,2,2,2,1,1])
    col1.write(f"**{market['city']}**")
    col2.write(f"{market['probability']} %")
    col3.write(market["decision"])
    col4.write(f"{market['confidence']}%")
    col5.write(f"{market['kelly']}%")

    investment = col6.number_input(
        "Investment ($)",
        min_value=100,
        max_value=10000,
        value=max(100, int(market["investment"])),
        step=100,
        key=f"investment_{market['city']}"
    )

    if col7.button("BUY YES", key=f"yes_{market['city']}"):

        order = execute_trade(
            market,
            investment,
            "BUY YES"
        )

        st.success(
            f"BUY YES Order {order['order_id']} placed!"
        )
        
       

        st.rerun()

    if col8.button("BUY NO", key=f"no_{market['city']}"):

        order = execute_trade(
            market,
            investment,
            "BUY NO"
        )

        st.success(
            f"BUY NO Order {order['order_id']} placed!"
        )
        
        

        st.rerun()

    st.divider()
    
    
show_research_feed(weather_data)

show_risk_dashboard(portfolio)

show_hedge_suggestions(portfolio)   # ✅ Correct

    
# ---------------------------------------
# Open Positions
# ---------------------------------------
st.subheader("📂 Open Positions")

from trading.order_manager import get_open_orders

positions_df = pd.DataFrame(get_open_orders())

if positions_df.empty:

    st.info("No Open Positions")

else:

    for _, row in positions_df.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 1])

        col1.write(row["city"])
        col2.write(row["decision"])
        col3.write(f"${row['capital']}")
        if row["status"] == "OPEN":
            col4.success("OPEN")
        elif row["status"] == "SETTLED":
            if row["result"] == "WIN":
                col4.success("WIN")
            else:
                col4.error("LOSS")
        else:
            col4.info(row["status"])
        col5.write(row["created_at"])

        if row["status"] == "OPEN":
            if col6.button("Close", key=f"close_{row['order_id']}"):
                close_position(row["order_id"])
                st.session_state.result = load_market_data()
                st.rerun()

st.divider()
# ---------------------------------------
# Statistics
# ---------------------------------------

st.subheader("📊 Trading Statistics")

stats_df = pd.DataFrame(
    statistics.items(),
    columns=["Metric", "Value"]
)

st.dataframe(stats_df, width="stretch")

st.divider()

st.subheader("📜 Order History")

if all_orders.empty:
    st.info("No Orders Yet")
else:
    st.dataframe(all_orders, width="stretch")

show_prior_predictions(orders)

show_charts(orders)