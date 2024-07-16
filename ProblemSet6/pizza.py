import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.csv>")

    filename = sys.argv[1]

    if not filename.endswith('.csv'):
        sys.exit("The file must be a CSV file.")

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
    except FileNotFoundError:
        sys.exit(f"The file {filename} does not exist.")

    if data:
        headers = data[0].keys()
        rows = [list(row.values()) for row in data]
        table = tabulate(rows, headers=headers, tablefmt='grid')

        print(table)
    else:
        print("The CSV file is empty.")


if __name__ == "__main__":
    main()
