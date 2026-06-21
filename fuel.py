def main():
    while True:
        try:
            fraction = input("fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x < 0 or y < 0:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            percent = round(x / y * 100)
            break
        except (ValueError, ZeroDivisionError):
            pass

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

if __name__ == "__main__":
    main()
