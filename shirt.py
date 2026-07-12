import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()

    if input_ext not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        input_image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    input_image = ImageOps.fit(input_image, shirt.size)

    input_image.paste(shirt, shirt)

    input_image.save(sys.argv[2])


if __name__ == "__main__":
    main()
