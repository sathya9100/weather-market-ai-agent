import os
from dotenv import load_dotenv
from apify_client import ApifyClient
from functools import lru_cache



load_dotenv()

client = ApifyClient(os.getenv("APIFY_API_TOKEN"))


@lru_cache(maxsize=10)

def fetch_apify_weather(city):
    """
    
    Fetch 10-day weather forecast from Apify.
    """

    try:
        run_input = {
            "locations": [city]
        }

        run = client.actor(
            "filip_cicvarek/weather-data-scraper"
        ).call(run_input=run_input)

        dataset_id = run.default_dataset_id

        items = list(
            client.dataset(dataset_id).iterate_items()
        )

        return items

    except Exception as e:
        print("Apify Error:", e)
        return []