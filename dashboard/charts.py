import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def show_charts(orders):

    st.subheader("📊 Trading Analytics")

    if not orders:
        st.info("No trading data available.")
        return

    df = pd.DataFrame(orders)

    # ==========================
    # Equity Curve + Win/Loss
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("#### 📈 Equity Curve")

        equity = df["profit_loss"].cumsum()

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=list(range(1, len(equity) + 1)),
                y=equity,
                mode="lines",
                line=dict(color="#22c55e", width=4),
                fill="tozeroy",
                fillcolor="rgba(34,197,94,0.15)"
            )
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            xaxis_title="Trades",
            yaxis_title="Profit / Loss",
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.markdown("#### 🍩 Win vs Loss")

        result_counts = df["result"].value_counts()

        fig = px.pie(
            names=result_counts.index,
            values=result_counts.values,
            hole=0.65,
            color=result_counts.index,
            color_discrete_map={
                "WIN": "#22c55e",
                "LOSS": "#ef4444",
                "PENDING": "#facc15"
            }
        )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="#0e1117",
            plot_bgcolor="#0e1117",
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=True
        )

        st.plotly_chart(fig, use_container_width=True)

    # ==========================
    # Investment by City
    # ==========================

    st.markdown("#### 💰 Investment by City")

    investment = (
        df.groupby("city")["capital"]
        .sum()
        .sort_values()
    )

    fig = px.bar(
        x=investment.values,
        y=investment.index,
        orientation="h",
        text=investment.values,
        color=investment.values,
        color_continuous_scale="Viridis"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0e1117",
        plot_bgcolor="#0e1117",
        height=420,
        margin=dict(l=20, r=20, t=20, b=20),
        coloraxis_showscale=False,
        xaxis_title="Investment ($)",
        yaxis_title=""
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(fig, use_container_width=True)