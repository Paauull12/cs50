
text = input("Input: ")

if (text.isdigit() and int(text) == 42) or text.lower() == "forty two" or text.lower() == "forty-two" :
    print("yes")
else:
    print("no")