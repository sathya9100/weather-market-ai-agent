import streamlit as st


def show_hedge_suggestions(portfolio):

    balance = portfolio.get("balance", 0)
    capital_at_risk = portfolio.get("capital_at_risk", 0)
    if balance > 0:
        exposure = (capital_at_risk / balance) * 100
    else:
        exposure = 0

    st.subheader("🛡 Hedge Suggestions")

    if exposure > 70:
        st.error(
            "High exposure detected. Consider placing a BUY NO trade on a low-rain probability city."
        )

    elif exposure > 40:
        st.warning(
            "Moderate exposure. Diversifying positions may reduce portfolio risk."
        )

    else:
        st.success(
            "Portfolio exposure is balanced."
        )