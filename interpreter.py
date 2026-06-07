x = input("Expression: ")

parts = x.split(" ")

if parts[1] == "+":
    print(float(parts[0]) + float(parts[2]))

elif parts[1] == "-":
    print(float(parts[0]) - float(parts[2]))

elif parts[1] == "*":
    print(float(parts[0]) * float(parts[2]))

elif parts[1] == "/":
    print(float(parts[0]) / float(parts[2]))
