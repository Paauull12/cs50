import emoji

text = input("Input: ")

if ":)" in text:
    print(text.replace(":)", emoji.emojize(":smiling_face_with_halo:")))
else:
    print(text.replace(":(", emoji.emojize(":neutral_face:")))