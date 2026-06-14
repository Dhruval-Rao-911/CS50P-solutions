word = input("Input: ")

for char in word:
    if char.lower() not in "aeiou":
        print(char, end="")

print()
