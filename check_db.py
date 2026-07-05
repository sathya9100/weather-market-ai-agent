import sqlite3

conn = sqlite3.connect("weather_trading.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM orders")

conn.commit()

print("✅ All orders deleted.")

cursor.execute("SELECT COUNT(*) FROM orders")
print("Orders:", cursor.fetchone()[0])

conn.close()