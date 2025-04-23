class CurrencyCalculator:
    def __init__(self):
        self.denominations = {
            'bills': [100, 50, 20, 10, 5],
            'coins': [1, 0.25, 0.10, 0.05, 0.01]
        }

    def calculate_minimum_bills_and_coins(self, amount):
        if amount < 0:
            raise ValueError("Amount must be a non-negative number.")
        
        result = {}
        remaining_amount = amount

        for bill in self.denominations['bills']:
            count = remaining_amount // bill
            if count > 0:
                result[bill] = int(count)
                remaining_amount -= bill * count

        for coin in self.denominations['coins']:
            count = remaining_amount // coin
            if count > 0:
                result[round(coin, 2)] = int(count)
                remaining_amount -= coin * count

        return result