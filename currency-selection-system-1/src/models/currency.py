class Currency:
    def __init__(self, value, currency_type):
        self.value = value
        self.currency_type = currency_type

    def __repr__(self):
        return f"{self.currency_type.capitalize()}({self.value})"