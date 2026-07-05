import streamlit as st


def show_market_summary(markets):

    st.subheader("🤖 AI Market Summary")

    buy_yes = [m for m in markets if m["decision"] == "BUY YES"]
    buy_no = [m for m in markets if m["decision"] == "BUY NO"]

    if buy_yes:
        best = max(buy_yes, key=lambda x: x["probability"])

        st.success(
            f"Best Opportunity: BUY YES • {best['city']} ({best['probability']}%)"
        )

    if buy_no:
        worst = min(buy_no, key=lambda x: x["probability"])

        st.warning(
            f"Best BUY NO Opportunity: {worst['city']} ({worst['probability']}%)"
        )

    st.info(
        f"Today's Markets: {len(markets)} | BUY YES: {len(buy_yes)} | BUY NO: {len(buy_no)}"
    )