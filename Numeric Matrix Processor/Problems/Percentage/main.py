def get_percentage(number, round_digits=None):
    return str(round(number * 100, round_digits)) + "%" if round_digits is not None else str(int(number * 100)) + "%"
