import streamlit as st


def show_research_feed(weather_data):

    st.subheader("📰 Research Feed")

    for weather in weather_data:

        with st.expander(f"📍 {weather['city']}", expanded=False):

            col1, col2 = st.columns(2)
            col1, col2 = st.columns(2)
            
            with col1:
                
                st.markdown(f"""
    <div style="margin-bottom:18px;">
        <div style="color:#9ca3af;font-size:14px;">🌡 Temperature</div>
        <div style="font-size:46px;font-weight:bold;color:#22c55e;">
            {weather['temperature']}°C
        </div>
    </div>

    <div>
        <div style="color:#9ca3af;font-size:14px;">💧 Humidity</div>
        <div style="font-size:46px;font-weight:bold;color:#22c55e;">
            {weather['humidity']}%
        </div>
    </div>
    """, unsafe_allow_html=True)
                with col2:
                    
                    st.markdown(f"""
    <div style="margin-bottom:18px;">
        <div style="color:#9ca3af;font-size:14px;">💨 Wind Speed</div>
        <div style="font-size:46px;font-weight:bold;color:#22c55e;">
            {weather['wind_speed']} km/h
        </div>
    </div>

    <div>
        <div style="color:#9ca3af;font-size:14px;">🌧 Rain</div>
        <div style="font-size:46px;font-weight:bold;color:#22c55e;">
            {weather['rain']} mm
        </div>
    </div>
    """, unsafe_allow_html=True)
            st.divider()

            st.markdown("###  AI Research")

            summary = weather.get("ai_summary")

            if weather["rain"] > 0:
                signal = "BUY YES"
                color = "#22c55e"
                icon = "🟢"
            else:
                signal = "BUY NO"
                color = "#ef4444"
                icon = "🔴"

            if not summary:
                summary = f"""
<b>Weather Summary</b><br>
Live weather data has been collected from multiple sources.<br><br>

<b>Trading Recommendation</b><br>
{icon} <span style="color:{color};font-weight:bold;">{signal}</span><br><br>

<b>Reason</b><br>
Decision generated using weather conditions, humidity, wind speed and rainfall probability.
"""

            st.markdown(
                f"""
<div style="
background:#161b22;
border:1px solid #30363d;
border-left:6px solid {color};
border-radius:12px;
padding:18px;
color:#e6edf3;
font-size:15px;
line-height:1.8;
margin-bottom:12px;
box-shadow:0 0 10px rgba(0,0,0,0.25);
">
{summary}
</div>
""",
                unsafe_allow_html=True,
            )

            confidence = weather.get("confidence", 70)

            st.markdown(
                f"""
<div style="
display:flex;
justify-content:space-between;
margin-bottom:8px;
font-size:15px;
font-weight:600;
">

<span style="color:white;">
Confidence
</span>

<span style="color:#22c55e;">
{confidence}%
</span>

</div>
""",
                unsafe_allow_html=True,
            )

            st.progress(confidence / 100)

            st.markdown("<br>", unsafe_allow_html=True)