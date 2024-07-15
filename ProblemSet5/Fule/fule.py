def main():
    text = input("Input: ")
    print(gauge(convert(text)))

def convert(fraction):
    x, y = fraction.strip().split('/')
    return [x, y]

def gauge(percentage):
    try:
        p = (100 * int(percentage[0])) / int(percentage[1])
        if p >= 99:
            return 'F'
        elif p <= 1:
            return 'E'
        else:
            return f"{int(p)}%"

    except ValueError or ZeroDivisionError:
        raise ValueError

if __name__ == "__main__":
    main()