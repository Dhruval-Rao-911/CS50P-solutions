def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    for char in s:
        if not char.isalnum():
            return False
    found_number = False
    for char in s:
        if char.isdigit():
            if char == "0" and not found_number:
                return False
            found_number = True
        else:
            if found_number:
                return False
    return True


if __name__ == "__main__":
    main()
