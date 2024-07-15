import sys
from pyfiglet import Figlet

figlet = Figlet()

text = input("Input: ")

if len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit(0)
elif len(sys.argv) == 1:
    figlet.setFont(font=figlet.getFonts()[0])
    print(figlet.renderText(text))
else:
    sys.exit(0)
