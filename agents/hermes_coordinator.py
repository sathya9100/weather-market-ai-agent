from agents.multi_city_agent import collect_all_weather
from agents.risk_agent import calculate_risk
from agents.trading_agent import create_trade


class HermesCoordinator:

    def run(self):

        weather_data = collect_all_weather()

        markets = []

        for weather in weather_data:

            risk = calculate_risk(weather)
            trade = create_trade(weather, risk)

            markets.append(trade)

        return weather_data, markets