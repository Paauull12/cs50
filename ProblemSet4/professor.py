import random


def main():

    level = get_level()
    x = generate_integer(level)
    y = generate_integer(level)

    questions = 0
    score = 0
    first_try = True

    while questions < 10:

        try:
            result = input(f"{x} + {y} = ")

            if x + y == int(result) and first_try:
                score += 1

            first_try = False
            if x + y != int(result):
                print("EEE")
                raise ValueError

            x = generate_integer(level)
            y = generate_integer(level)
            first_try = True
            questions += 1

        except ValueError:
            pass

    print(score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level not in [1, 2, 3]:
                raise ValueError

            break
        except:
            pass

    return level


def generate_integer(level):

    number1 = random.randint(1, 9)
    for _ in range(level - 1):
        number1 *= 10
        number1 += random.randint(0, 9)

    return number1


if __name__ == "__main__":
    main()