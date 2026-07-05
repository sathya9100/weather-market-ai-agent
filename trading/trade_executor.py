from agents.orders import create_order
from trading.order_manager import add_order


def execute_trade(market, investment, decision):

    trade = {
        "city": market["city"],
        "probability": market["probability"],
        "decision": decision,
        "kelly": market["kelly"],
        "investment": investment
    }

    order = create_order(trade)

    # Save as OPEN order
    add_order(order)

    return order