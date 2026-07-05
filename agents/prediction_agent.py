import json
import re

from agents.research_agent import research_weather
from utils.llm import ask_llm


def predict_weather(city):

    research = research_weather(city)

    prompt = f"""
You are a JSON API.

Return ONLY valid JSON.

Do not explain.
Do not think.
Do not include reasoning.
Do not include markdown.
Do not include any text before or after the JSON.

Analyze the following weather data.

City: {research['city']}
Country: {research['country']}

Current Temperature: {research['temperature']} °C
Humidity: {research['humidity']} %
Wind Speed: {research['wind_speed']} km/h
Current Rain: {research['rain']} mm

10-Day Forecast:
{research['apify']}

Example Output:

{{
    "rain_probability": 76,
    "confidence": "High",
    "reason": "Explain in 2-3 sentences.",
    "decision": "BUY YES"
}}

Rules:
- rain_probability must be between 0 and 100.
- confidence must be Low, Medium or High.
- decision must be BUY YES, BUY NO or HOLD.
- Return ONLY a valid JSON object.
"""

    response = ask_llm(prompt)

    print("LLM Output:")
    print(response)

    try:
        match = re.search(r"\{.*\}", response, re.DOTALL)

        if match:
            analysis = json.loads(match.group())
        else:
            analysis = {
                "rain_probability": 0,
                "confidence": "Unknown",
                "reason": response,
                "decision": "HOLD"
            }

    except Exception:
        analysis = {
            "rain_probability": 0,
            "confidence": "Unknown",
            "reason": response,
            "decision": "HOLD"
        }

    return {
        "research": research,
        "analysis": analysis
    }