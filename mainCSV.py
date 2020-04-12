# This file handles CSV files.
# import csv, a library for handling CSV files.
import csv
with open('MOCK NC Open Cases 04.08.2020.csv') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)