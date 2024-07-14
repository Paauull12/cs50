def main():
    time = input("Input: ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(':')
    h = int(h)
    m = (int(m) * 10) / 600

    return h + m


if __name__ == "__main__":
    main()