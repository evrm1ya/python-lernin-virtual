# Problem 13
# Write a program csv2xls.py that reads a csv file and
# exports it as an Excel file. The program should take
# two arguments. The name of the csv file to read is
# is the first arg. The name of the Excel file to write
# is the second arg.

import sys
import tablib

def main(csv_path, excel_path):
    dataset = tablib.Dataset()
    dataset.load(open(csv_path, 'rU').read())
    with open(excel_path, 'w') as f:
        f.write(dataset.xlsx)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

