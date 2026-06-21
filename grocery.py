def main():
    groceries = {}

    while True:
        try:
            item = input("").upper()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            break

    for item in sorted(groceries):
            print(groceries[item], item)

if __name__ == "__main__":
     main()
