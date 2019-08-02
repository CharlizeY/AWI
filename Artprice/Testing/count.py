import csv
import sys

with open(sys.argv[1]) as csv_file:
    row_count = sum(1 for row in csv_file)
    print(row_count)
