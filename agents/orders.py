import uuid
from datetime import datetime


def create_order(trade):

    return {
        "order_id": str(uuid.uuid4())[:8],
        "city": trade["city"],
        "market": f"Will it rain tomorrow in {trade['city']}?",
        "decision": trade["decision"],
        "probability": trade["probability"],
        "kelly": trade["kelly"],
        "capital": trade["investment"],
        "entry_odds": 2.0,

        # Trade Status
        "status": "OPEN",
        "result": "PENDING",

        # Profit & Loss
        "profit_loss": 0.0,

        # Time
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }