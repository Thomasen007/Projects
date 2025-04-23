def format_currency(amount):
    return "${:,.2f}".format(amount)

def validate_input(amount):
    try:
        value = float(amount)
        if value < 0:
            raise ValueError("Amount must be a non-negative number.")
        return value
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")