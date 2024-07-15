
while True:

    frac = input("Fraction: ")

    x, y = frac.strip().split('/')

    try:
        p = (100 * int(x)) / int(y)
        if p >= 99:
            print('F')
        elif p <= 1:
            print('E')
        else:
            print(f"{int(p)}%")
        break
    except ValueError or ZeroDivisionError:
        pass

