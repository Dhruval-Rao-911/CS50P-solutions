from validator_collection import validators, checkers


def main():
    email = input("Email: ")
    if is_valid(email):
        print("Valid")
    else:
        print("Invalid")


def is_valid(email):
    return checkers.is_email(email)


if __name__ == "__main__":
    main()
