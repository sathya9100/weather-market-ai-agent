import streamlit as st


def show_ai_summary(markets):

    st.subheader("🧠 AI Market Insights")

    if not markets:
        return

    buy_yes = [m for m in markets if m["decision"] == "BUY YES"]
    buy_no = [m for m in markets if m["decision"] == "BUY NO"]

    if buy_yes:
        best = max(buy_yes, key=lambda x: x["probability"])
        st.success(
            f"Highest Conviction BUY YES: **{best['city']}** "
            f"({best['probability']}%) | Kelly {best['kelly']}%"
        )

    if buy_no:
        best = min(buy_no, key=lambda x: x["probability"])
        st.warning(
            f"Highest Conviction BUY NO: **{best['city']}** "
            f"({best['probability']}%) | Kelly {best['kelly']}%"
        )

    avg = sum(m["probability"] for m in markets) / len(markets)

    if avg > 60:
        sentiment = "Bullish Weather Market"
    elif avg < 40:
        sentiment = "Bearish Weather Market"
    else:
        sentiment = "Neutral Weather Market"

    st.info(f"Overall AI Market Sentiment: **{sentiment}**")