import random


def settle_order(order):
    """
    Simulate whether the prediction wins or loses.
    """

    probability = order["probability"]

    random_value = random.randint(1, 100)

    if order["decision"] == "BUY YES":

        win = random_value <= probability

    elif order["decision"] == "BUY NO":

        win = random_value > probability

    else:
        return order

    capital = order["capital"]

    if win:

        profit = round(capital * 0.35, 2)

        order["profit_loss"] = profit

        order["status"] = "SETTLED"

        order["result"] = "WIN"

    else:

        loss = round(capital * 0.25, 2)

        order["profit_loss"] = -loss

        order["status"] = "SETTLED"

        order["result"] = "LOSS"

    return order