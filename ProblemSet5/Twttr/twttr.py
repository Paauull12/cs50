def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    rez = ""
    for char in word:
        if char not in 'aeiouAEIOU':
            rez += char
    return rez


if __name__ == "__main__":
    main()