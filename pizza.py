import sys
import csv
from tabulate import tabulate

def main():
    # Check arguments
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    # Check file extension
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try opening file
    try:
        with open(sys.argv[1], "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            rows = list(reader)
        print(tabulate(rows, headers=header, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
