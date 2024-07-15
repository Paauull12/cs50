
def main():
    text = input("Input: ")
    print(value(text))


def value(greeting):
    if greeting.lower() == "hello":
        return "$0"
    elif greeting.lower()[0] == 'h':
        return "$20"
    elif greeting.lower()[0] != ' ':
        return "$100"
    return -1


if __name__ == "__main__":
    main()