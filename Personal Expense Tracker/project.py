import csv
import sys
from datetime import datetime


def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Total")
        print("3. View by Category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            print(f"Total Spent: ${get_total():.2f}")
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            break
        else:
            print("Invalid option")


def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
    print("Expense added!")


def get_total():
    total = 0
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += float(row[2])
    except FileNotFoundError:
        pass
    return total


def view_by_category():
    categories = {}
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                cat = row[1]
                amt = float(row[2])
                categories[cat] = categories.get(cat, 0) + amt
    except FileNotFoundError:
        print("No expenses yet")
        return

    for cat, amt in categories.items():
        print(f"{cat}: ${amt:.2f}")


if __name__ == "__main__":
    main()
