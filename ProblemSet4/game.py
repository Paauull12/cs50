import random

while True:

    try:
        number = int(input("Level: "))

        if number <= 0:
            raise ValueError

        break;

    except ValueError:
        pass

number = random.randint(1,number)

while True:

    try:
        val = int(input("Guess: "))

        if val <= 0:
            raise ValueError
        elif val < number:
            print("Too small!")
            raise ValueError
        elif val > number:
            print("Too large!")
            raise ValueError
        else:
            print("Just right!")

        break
    except ValueError:
        pass