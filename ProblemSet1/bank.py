
text = input("Input: ")

if text.lower() == "hello":
    print("$0")
elif text.lower()[0] == 'h':
    print("$20")
elif text.lower()[0] != ' ':
    print("$100")