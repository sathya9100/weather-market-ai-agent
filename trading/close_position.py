from trading.order_manager import (
    get_all_orders,
    update_order
)
from trading.settlement import settle_order


def close_position(order_id):

    orders = get_all_orders()

    for order in orders:

        if order["order_id"] == order_id:

            settled_order = settle_order(order)

            settled_order["status"] = "SETTLED"

            update_order(settled_order)

            return settled_order