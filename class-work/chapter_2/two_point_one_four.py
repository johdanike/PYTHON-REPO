
def target_heart_rate_calculator(age):

    MAX_HEART_RATE = 220 - age
    target_heart_rate_lower = ((50 / 100) * age)
    target_heart_rate_upper = ((85 / 100) * age)

    return f"""
    Age: {age}
    Max heart rate: {MAX_HEART_RATE}
    Range of heart rate is between: {target_heart_rate_lower} - {target_heart_rate_upper}%
    """

print(target_heart_rate_calculator(30))
