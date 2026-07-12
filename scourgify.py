import sys
import csv

def main():
    # Check arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check file extensions
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Try reading input file
    try:
        with open(sys.argv[1], "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("Could not read file")

    # Write clean output file
    with open(sys.argv[2], "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in rows:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})


if __name__ == "__main__":
    main()
