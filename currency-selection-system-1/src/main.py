def main():
    while True:
        print("Welcome to the Currency Selection System!")
        while True:
            try:
                amount = float(input("Enter the amount of money: "))
                if amount < 0:
                    raise ValueError("Amount cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid amount.")

        from services.currency_calculator import CurrencyCalculator
        calculator = CurrencyCalculator()
        result = calculator.calculate_minimum_bills_and_coins(amount)

        print("Minimum number of bills and coins needed:")
        for denomination, count in result.items():
            print(f"{denomination}: {count}")
        print("Thank you for using the Currency Selection System!")
        print("Do you want to calculate again? (yes/no)")
        if input().strip().lower() != 'yes':
                break
    print("Exiting the Currency Selection System. Goodbye!")    
if __name__ == "__main__":
    main()