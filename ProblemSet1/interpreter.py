text = input("Input: ").strip().split()

if text[1] == '+':
    print(int(text[0]) + int(text[2]))
elif text[1] == '-':
    print(int(text[0]) - int(text[2]))
elif text[1] == '/':
    print(int(text[0]) / int(text[2]))
elif text[1] == '*':
    print(int(text[0]) * int(text[2]))