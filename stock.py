import csv
from datetime import datetime

# Hardcoded stock prices (can be updated easily)
STOCK_PRICES = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "MSFT": 330,   # Microsoft
    "GOOGL": 140,  # Google
    "AMZN": 135    # Amazon
}

def get_portfolio():
    """
    Collects stock names and quantities from the user.
    Returns a dictionary {stock: quantity}.
    """
    portfolio = {}
    print("Welcome to Stock Portfolio Tracker!")
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("❌ Stock not available. Choose from:", ", ".join(STOCK_PRICES.keys()))
            continue

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Add to portfolio
        portfolio[stock] = portfolio.get(stock, 0) + quantity

    return portfolio

def calculate_value(portfolio):
    """
    Calculates total investment and returns summary data.
    """
    total_value = 0
    summary = []

    for stock, qty in portfolio.items():
        value = STOCK_PRICES[stock] * qty
        total_value += value
        summary.append((stock, qty, STOCK_PRICES[stock], value))

    return total_value, summary

def display_summary(summary, total_value):
    """
    Prints the portfolio summary in a clean format.
    """
    print("\n--- Portfolio Summary ---")
    print(f"{'Stock':<10}{'Qty':<10}{'Price':<10}{'Value':<10}")
    for stock, qty, price, value in summary:
        print(f"{stock:<10}{qty:<10}${price:<9}${value:<10}")
    print(f"\nTotal Investment Value = ${total_value}")

def save_to_files(summary, total_value):
    """
    Saves portfolio summary to TXT and CSV files.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    txt_file = f"portfolio_summary_{timestamp}.txt"
    csv_file = f"portfolio_summary_{timestamp}.csv"

    # Save TXT
    with open(txt_file, "w") as f:
        f.write("--- Portfolio Summary ---\n")
        for stock, qty, price, value in summary:
            f.write(f"{stock}: {qty} shares @ ${price} = ${value}\n")
        f.write(f"\nTotal Investment Value = ${total_value}\n")

    # Save CSV
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(summary)
        writer.writerow([])
        writer.writerow(["Total", "", "", total_value])

    print(f"\nPortfolio saved as '{txt_file}' and '{csv_file}'")

def main():
    """
    Main program flow.
    """
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting program.")
        return

    total_value, summary = calculate_value(portfolio)
    display_summary(summary, total_value)

    save = input("\nDo you want to save this summary to files? (y/n): ").lower()
    if save == "y":
        save_to_files(summary, total_value)

if __name__ == "__main__":
    main()
