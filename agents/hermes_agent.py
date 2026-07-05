from agents.multi_city_agent import collect_all_weather
from agents.risk_agent import calculate_risk
from agents.trading_agent import create_trade

from trading.portfolio import Portfolio
from trading.statistics import Statistics
from trading.order_manager import (
    get_all_orders,
    get_open_orders
)


def run_system():

    print("\n==========================================")
    print("   WEATHER AI TRADING TERMINAL")
    print("==========================================\n")

    statistics = Statistics()

    # ---------------------------------------
    # Collect Weather
    # ---------------------------------------
    weather_data = collect_all_weather()

    # ---------------------------------------
    # Generate Trades
    # ---------------------------------------
    trades = []

    for weather in weather_data:

        risk = calculate_risk(weather)
        trade = create_trade(weather, risk)

        trades.append(trade)

    # ---------------------------------------
    # Market Watch Data
    # ---------------------------------------
    markets = []

    for trade in trades:

        markets.append({
            "city": trade["city"],
            "probability": trade["probability"],
            "decision": trade["decision"],
            "kelly": trade["kelly"],
            "confidence": trade["confidence"],
            "investment": trade["investment"]
        })

    # ---------------------------------------
    # Orders & Portfolio
    # ---------------------------------------
    orders = get_all_orders()

    portfolio = Portfolio()

    # ---------------------------------------
    # Statistics
    # ---------------------------------------
    for order in orders:
        statistics.record_trade(order)

    # ---------------------------------------
    # Return Dashboard Data
    # ---------------------------------------
    return {
        "markets": markets,
        "weather_data": weather_data,
        "orders": orders,
        "portfolio": portfolio.get_summary(),
        "positions": portfolio.get_positions(),
        "statistics": statistics.get_statistics()
    }