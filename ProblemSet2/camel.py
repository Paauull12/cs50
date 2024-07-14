
text = input("Input: ")

result = ""

for char in text:
    if 'A' <= char <= 'Z':
        result += '_' + char.lower()
    else:
        result += char

print(result)