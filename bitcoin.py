import requests
import sys

def main():
    # Check command line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Check if valid number
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Fetch Bitcoin price from CoinCap v3 API
    try:
        api_key = "1b3ea71a6a695d0c4c1df24f541fcacdeb7eafef804618799ddfcf301f1608ce"
        response = requests.get(
            "https://api.coincap.io/v3/assets/bitcoin",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not fetch Bitcoin price")

    # Calculate and print total
    total = bitcoins * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
