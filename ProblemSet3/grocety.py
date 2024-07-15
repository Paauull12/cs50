
grocery = {}

while True:
    try:
        item = input("").strip().lower()

        try:
            grocery[item] += 1
        except KeyError:
            grocery[item] = 1

    except EOFError:
        break

sorted(grocery)

for item in grocery:
    print(f"{grocery[item]} {item.upper()}")