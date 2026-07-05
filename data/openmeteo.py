import requests
from functools import lru_cache

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


@lru_cache(maxsize=20)
def get_weather(city: str):
    """
    Fetch current weather for a city using Open-Meteo.
    """

    # Step 1: Get Latitude & Longitude
    geo_response = requests.get(
        GEOCODING_URL,
        params={
            "name": city,
            "count": 1
        },
        timeout=5
    )

    geo_response.raise_for_status()

    geo_data = geo_response.json()

    if "results" not in geo_data:
        return None

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]
    country = location["country"]

    # Step 2: Current Weather
    weather_response = requests.get(
        WEATHER_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,rain"
        },
        timeout=5
    )

    weather_response.raise_for_status()

    weather = weather_response.json()["current"]

    return {
        "city": city,
        "country": country,
        "latitude": latitude,
        "longitude": longitude,
        "temperature": weather["temperature_2m"],
        "humidity": weather["relative_humidity_2m"],
        "wind_speed": weather["wind_speed_10m"],
        "rain": weather["rain"]
    }