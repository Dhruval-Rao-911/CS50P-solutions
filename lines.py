import sys

def main():
    # Check arguments
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too many command-line arguments")

    # Check file extension
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    # Try opening file
    try:
        with open(sys.argv[1], "r") as f:
            lines = 0
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    lines += 1
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
