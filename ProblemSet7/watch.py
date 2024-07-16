import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^.*((?:https?//)?(?:www\.)?youtube.com/embed/[a-zA-Z0-9]+).*$", s):
        return match.group(1)
    else:
        return None


if __name__ == "__main__":
    main()