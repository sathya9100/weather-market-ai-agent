def calculate_kelly(probability, odds=2.0):

    p = probability / 100
    q = 1 - p
    b = odds - 1

    kelly = ((b * p) - q) / b

    if kelly < 0:
        kelly = 0

    if kelly > 1:
        kelly = 1

    return round(kelly * 100, 2)