def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    result = ""
    for char in word:
        if char.lower() not in "aeiou":
            result += char
    return result


if __name__ == "__main__":
    main()
