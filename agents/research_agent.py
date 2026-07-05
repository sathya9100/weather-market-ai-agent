from data.openmeteo import get_weather
from data.apify_weather import fetch_apify_weather
from utils.llm import ask_llm



def research_weather(city):

    weather = get_weather(city)

    if weather is None:
        return None

# Temporarily disable Apify for faster loading
    apify = []

    summary = f"""
Weather Summary:
Current temperature is {weather['temperature']}°C.

Rain Confidence:
Based on live weather data.

Trading Recommendation:
HOLD

Reason:
Generated using weather API data.
"""

    if summary is None:
        summary = """
Weather Summary:
AI analysis unavailable.

Trading Recommendation: HOLD

Reason:
Using weather data only.
"""

    return {
        "city": weather["city"],
        "country": weather["country"],
        "temperature": weather["temperature"],
        "humidity": weather["humidity"],
        "wind_speed": weather["wind_speed"],
        "rain": weather["rain"],
        "apify": apify,
        "ai_summary": summary
    }