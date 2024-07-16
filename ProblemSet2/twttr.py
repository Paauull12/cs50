
text = input("Input: ")

for char in text:
    if char not in 'aeiouAEIOU':
        print(char, end='')