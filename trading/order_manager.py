from database.database import get_connection


def add_order(order):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
INSERT INTO orders VALUES
(?,?,?,?,?,?,?,?,?,?,?,?)
""", (
    order["order_id"],
    order["city"],
    order["market"],
    order["decision"],
    order["probability"],
    order["kelly"],
    order["capital"],
    order["entry_odds"],
    order["status"],
    order["result"],
    order["profit_loss"],
    order["created_at"]
))

    conn.commit()
    conn.close()


def get_all_orders():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")

    rows = cursor.fetchall()

    conn.close()

    orders = []

    for row in rows:

        orders.append({
    "order_id": row[0],
    "city": row[1],
    "market": row[2],
    "decision": row[3],
    "probability": row[4],
    "kelly": row[5],
    "capital": row[6],
    "entry_odds": row[7],
    "status": row[8],
    "result": row[9],
    "profit_loss": row[10],
    "created_at": row[11]
})
    return orders


def get_open_orders():

    return [
        order
        for order in get_all_orders()
        if order["status"] == "OPEN"
    ]

def update_order(order):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE orders
        SET
            status=?,
            result=?,
            profit_loss=?
        WHERE order_id=?
    """, (
        order["status"],
        order["result"],
        order["profit_loss"],
        order["order_id"]
    ))

    conn.commit()
    conn.close()