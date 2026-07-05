from database.database import get_connection


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
                  CREATE TABLE IF NOT EXISTS orders(
    order_id TEXT PRIMARY KEY,
    city TEXT,
    market TEXT,
    decision TEXT,
    probability REAL,
    kelly REAL,
    capital REAL,
    entry_odds REAL,
    status TEXT,
    result TEXT,
    profit_loss REAL,
    created_at TEXT
)
""")

    conn.commit()
    conn.close()