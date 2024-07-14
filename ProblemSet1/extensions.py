

text = input("Input: ")

if text.endswith(".gif") or text.endswith(".jpg"):
    print(text.replace('.', '/'))
else:
    print(f"{text[:text.find('.')]}/octet-stream")