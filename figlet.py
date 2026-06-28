import pyfiglet
import sys
import random

def main():

    f = pyfiglet.Figlet()

    all_fonts = f.getFonts()

    if len(sys.argv) == 1:
        chosen_font = random.choice(all_fonts)
        f.setFont(font=chosen_font)

    elif len(sys.argv) == 3:
        flag = sys.argv[1]
        font_name = sys.argv[2]

        if flag in ["-f", "--font"] and font_name in all_fonts:
            f.setFont(font=font_name)
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")

    print(f.renderText(text))


if __name__ == "__main__":
    main()
