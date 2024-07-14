
amount = 50

while amount > 0:
    number = input("Baga un numar: ")
    if int(number) in [5, 10, 25]:
        amount -= int(number)

    if amount > 0:
        print(f"Amount due: {amount}")

print(f"Amount owed: {abs(amount)}")