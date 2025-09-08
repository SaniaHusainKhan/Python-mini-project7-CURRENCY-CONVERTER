import requests

BASE_URL = "https://open.er-api.com/v6/latest/"

def get_currencies(base="USD"):
    url = BASE_URL + base
    response = requests.get(url)
    data = response.json()
    if data.get("result") != "success":
        print("Error fetching currencies:", data.get("error-type", "Unknown error"))
        return None
    return data["rates"]

def print_currencies(rates):
    print("\nAvailable currencies:")
    for code in sorted(rates.keys()):
        print(code, end="  ")
    print("\n")

def exchange_rate(currency1, currency2):
    rates = get_currencies(currency1)
    if rates is None or currency2 not in rates:
        print("Invalid currencies.")
        return None
    rate = rates[currency2]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return
    converted_amount = rate * amount
    print(f"{amount} {currency1} = {converted_amount:.2f} {currency2}")
    return converted_amount

def main():
    print("🌍 Welcome to the Currency Converter!")
    print("Commands:")
    print("  list     - list available currencies")
    print("  rate     - get exchange rate between two currencies")
    print("  convert  - convert an amount")
    print("  q        - quit")
    print()
    while True:
        command = input("Enter a command: ").lower()
        if command == "q":
            break
        elif command == "list":
            rates = get_currencies()
            if rates:
                print_currencies(rates)
        elif command == "rate":
            c1 = input("Enter base currency (e.g., USD): ").upper()
            c2 = input("Enter target currency (e.g., INR): ").upper()
            exchange_rate(c1, c2)
        elif command == "convert":
            c1 = input("Enter base currency (e.g., USD): ").upper()
            amt = input(f"Enter amount in {c1}: ")
            c2 = input("Enter target currency (e.g., EUR): ").upper()
            convert(c1, c2, amt)
        else:
            print("❌ Unrecognized command! Try again.")

if __name__ == "__main__":
    main()
