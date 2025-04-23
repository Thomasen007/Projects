# Currency Selection System

This project is a currency selection system that minimizes the number of bills and coins needed to make a specified amount of money. It provides a user-friendly interface to input an amount and returns the optimal combination of currency denominations.

## Project Structure

```
currency-selection-system
├── src
│   ├── main.py                  # Entry point of the application
│   ├── services
│   │   └── currency_calculator.py # Contains the CurrencyCalculator class
│   ├── models
│   │   └── currency.py           # Defines the Currency class
│   └── utils
│       └── helpers.py            # Utility functions for input validation and formatting
├── requirements.txt              # Lists project dependencies
└── README.md                     # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd currency-selection-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Follow the prompts to enter an amount. The application will calculate and display the minimum number of bills and coins needed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.