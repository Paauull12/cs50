names = []

while True:
    try:
        text = input("Name: ")

        names.append(text)
    except EOFError:
        break

for index in range(len(names)):
    rez = "Adieu, adieu, to"
    for indexj in range(index + 1):
        if indexj == index and index:
            rez += " and " + names[indexj]
        else:
            rez += " " + names[indexj]
    print(rez)