import emoji

def main():
    code = input("Input: ")
    print(emoji.emojize(code, language = "alias"))


if __name__ == "__main__":
    main()
