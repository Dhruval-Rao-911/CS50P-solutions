import sys

fruits = {
    "apple": 130,
    "avocado": 50,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100
}

def main():
    item = input("Item: ").lower()
    if item in fruits:
        print("Calories:", fruits[item])
    else:
        sys.exit()

if __name__ == "__main__":
    main()
