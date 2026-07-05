class Statistics:

    def __init__(self):
        self.total_trades = 0
        self.winning_trades = 0
        self.losing_trades = 0

        self.total_profit = 0.0
        self.total_loss = 0.0

        self.trade_history = []

    def record_trade(self, order):

        self.total_trades += 1

        pnl = order["profit_loss"]

        if pnl >= 0:
            self.winning_trades += 1
            self.total_profit += pnl
        else:
            self.losing_trades += 1
            self.total_loss += abs(pnl)

        self.trade_history.append(order)

    def get_statistics(self):

        if self.total_trades == 0:
            win_rate = 0
        else:
            win_rate = round(
                (self.winning_trades / self.total_trades) * 100,
                2
            )

        roi = round(
            self.total_profit - self.total_loss,
            2
        )

        return {
            "Total Trades": self.total_trades,
            "Winning Trades": self.winning_trades,
            "Losing Trades": self.losing_trades,
            "Win Rate": win_rate,
            "Net Profit": round(self.total_profit, 2),
            "Net Loss": round(self.total_loss, 2),
            "ROI": roi
        }

    def history(self):
        return self.trade_history