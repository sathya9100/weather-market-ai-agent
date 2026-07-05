import streamlit as st
import pandas as pd


def show_prior_predictions(orders):

    st.subheader("📅 Prior Predictions")

    if not orders:
        st.info("No prior predictions available.")
        return

    data = []

    for order in orders:

        if order["status"] != "SETTLED":
            continue

        data.append({
            "City": order["city"],
            "Prediction": order["decision"],
            "Outcome": order["result"],
            "P/L": order["profit_loss"],
            "Correct": "✅" if order["result"] == "WIN" else "❌"
        })

    if data:
        st.dataframe(pd.DataFrame(data), use_container_width=True)
    else:
        st.info("No settled predictions yet.")