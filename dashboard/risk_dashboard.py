import streamlit as st


def show_risk_dashboard(portfolio):
    

    balance = portfolio.get("balance", 0)
    capital = portfolio.get("capital_at_risk", 0)

    exposure = (capital / balance * 100) if balance else 0

    if exposure < 30:
        risk = "🟢 LOW"
        color = "#22c55e"
        border = "#22c55e"
        msg = "Portfolio is well diversified."

    elif exposure < 70:
        risk = "🟡 MEDIUM"
        color = "#facc15"
        border = "#facc15"
        msg = "Portfolio is moderately exposed. Diversification recommended."

    else:
        risk = "🔴 HIGH"
        color = "#ef4444"
        border = "#ef4444"
        msg = "High portfolio exposure. Hedge recommended."

    st.subheader("⚠ Risk Dashboard")

    st.markdown(
        f"""
<div style="
background:#111827;
padding:25px;
border-radius:16px;
border:2px solid {border};
">

<h2 style="color:white;margin-top:0;">
Portfolio Risk
</h2>

<div style="font-size:42px;color:{color};font-weight:bold;">
{risk}
</div>

<br>

<table style="width:100%;color:white;font-size:18px;">
<tr>
<td><b>Exposure</b></td>
<td style="color:{color};"><b>{exposure:.1f}%</b></td>
</tr>

<tr>
<td><b>Capital At Risk</b></td>
<td style="color:{color};"><b>${capital:,.0f}</b></td>
</tr>

<tr>
<td><b>Balance</b></td>
<td>${balance:,.0f}</td>
</tr>

</table>

<br>

<div style="
width:100%;
height:16px;
background:#2d3748;
border-radius:8px;
overflow:hidden;
">

<div style="
height:16px;
width:{min(exposure,100)}%;
background:{color};
">
</div>

</div>

<br>

<div style="
padding:15px;
background:#1f2937;
border-left:5px solid {border};
border-radius:8px;
color:white;
font-size:18px;
">

{msg}

</div>

</div>
""",
        unsafe_allow_html=True,
    )