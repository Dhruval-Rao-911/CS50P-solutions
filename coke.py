total = 50
print("Amount Due:", total)

while total > 0:
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        total = total - coin
        print("Amount Due:", total)
    else:
        print("Amount Due:", total)

print("Change Owed:", - total)
