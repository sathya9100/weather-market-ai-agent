def calculate_risk(weather):

    if weather is None:
        return {
            "risk_score": 0,
            "risk_level": "LOW"
        }

    score = 0

    if weather["humidity"] >= 70:
        score += 30

    if weather["wind_speed"] >= 20:
        score += 20

    if weather["rain"] > 0:
        score += 30

    apify = weather.get("apify") or []

    print("DEBUG APIFY:", apify)
    print("DEBUG TYPE :", type(apify))

    if len(apify) > 1:
        chance = apify[1].get("precipChance")

        if chance is not None:
            score += chance * 0.5

    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": round(score, 2),
        "risk_level": level
    }