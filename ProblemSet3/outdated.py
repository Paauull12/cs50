mounths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:

    text = input("Date: ").strip().split()

    try:
        if text[0][0].isalpha():
            #suntem in cazul de Jan / January

            if text[0] in mounths:

                print(f"{text[2]}-{(mounths.index(text[0]) + 1):02}-{int(text[1].split(',')[0]):02}")
            else:
                raise ValueError
        else:
            #aici suntem in cazul unei date normale
            text = text[0].split('/')

            print(f"{int(text[2])}-{int(text[0]):02}-{int(text[1]):02}")

        break
    except ValueError:
        pass