import sys

if len(sys.argv) == 2:
    filePath = sys.argv[1]

    if not filePath.endswith(".py"):
        sys.exit()

    try:
        with open(filePath, 'r') as file:

            count = 0
            for line in file:
                line = line.strip()
                if line != "" and line[0] != '#':
                    count += 1

            print(count)
    except FileNotFoundError:
        sys.exit()

else:
    sys.exit()