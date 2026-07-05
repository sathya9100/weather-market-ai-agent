from trading.kelly import calculate_kelly


def create_trade(weather, risk):

    probability = risk["risk_score"]

    if probability >= 60:
        decision = "BUY YES"

    elif probability <= 40:
        decision = "BUY NO"

    else:
        decision = "HOLD"

    kelly = calculate_kelly(probability)

    capital = 10000

    investment = round(capital * (kelly / 100), 2)

    return {
    "city": weather["city"],
    "probability": probability,
    "decision": decision,
    "kelly": kelly,
    "confidence": probability,
    "investment": investment
}