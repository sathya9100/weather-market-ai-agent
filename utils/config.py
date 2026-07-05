import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")

OPENROUTER_MODEL = model="qwen/qwen3-32b:free",
BASE_CAPITAL = 10000

SUPPORTED_CITIES = [
    "New York",
    "London",
    "Tokyo",
    "Mumbai",
    "Sydney"
    ]