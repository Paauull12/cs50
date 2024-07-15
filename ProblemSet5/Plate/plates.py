
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) != 6:
        return False

    for it in [' ', '.', ',']:
        if it in s:
            return False

    firstN = -1
    lastL = -1

    for it in range(len(s)):
        if firstN == -1 and s[it].isdigit():
            firstN = it
        if s[it].isalpha():
            lastL = it

    if firstN < lastL:
        return False

    if lastL < 1:
        return False

    return True


if __name__ == "__main__":
    main()