from data.city_sources import CITIES
from agents.research_agent import research_weather


def collect_all_weather():

    results = []

    for city in CITIES:

        print("=" * 50)
        print("Collecting:", city)

        try:
            weather = research_weather(city)

            print("Returned:")
            print(weather)

            if weather is not None:
                results.append(weather)
            else:
                print(city, "returned None")

        except Exception as e:
            print("ERROR:", city)
            print(e)

    print("FINAL RESULTS")
    print(results)

    return results