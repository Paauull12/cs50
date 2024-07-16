
fruits={
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grepefruit': 60,
    'grapes': 90,
    'honeydew': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'nectarine': 60,
    'orange': 80,
}

text = input("Input: ").strip().lower()

if text in fruits:
    print(fruits[text])