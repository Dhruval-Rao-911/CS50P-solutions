import inflect
import sys

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    result = p.join(names)
    print(f"Adieu, adieu, to {result}")


if __name__ == "__main__":
    main()
