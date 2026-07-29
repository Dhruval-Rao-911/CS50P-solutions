import sys
from datetime import date
import inflect


def main():
    try:
        birth = input("Date of Birth: ")
        year, month, day = birth.split("-")
        birth_date = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    print(convert(birth_date))


def convert(birth_date):
    today = date.today()
    days = (today - birth_date).days
    minutes = days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
