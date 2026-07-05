import sqlite3
import os

def get_connection():
    db_path = os.path.abspath("weather_trading.db")
    print("DATABASE PATH:", db_path)
    return sqlite3.connect(db_path)