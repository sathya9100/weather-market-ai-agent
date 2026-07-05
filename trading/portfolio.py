from trading.order_manager import get_all_orders


class Portfolio:

    STARTING_BALANCE = 10000.0

    def __init__(self):
        self.orders = get_all_orders()

    def get_summary(self):

        open_orders = [
            o for o in self.orders
            if o["status"] == "OPEN"
        ]

        invested = sum(o["capital"] for o in open_orders)

        capital_at_risk = invested

        today_pl = sum(
            o["profit_loss"]
            for o in self.orders
        )

        balance = (
            self.STARTING_BALANCE
            - invested
            + today_pl
        )

        equity = balance + invested
        return {
    "balance": round(balance, 2),
    "available_cash": round(balance, 2),
    "invested_capital": round(invested, 2),
    "capital_at_risk": round(capital_at_risk, 2),
    "equity": round(equity, 2),
    "today_pl": round(today_pl, 2),
    "open_positions": len(open_orders)
}

    def get_positions(self):
        return self.orders