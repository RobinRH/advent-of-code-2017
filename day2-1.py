import csv
import sys

filename = sys.argv[1]
rows = []

sum = 0
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        introw = map(lambda x : int(x), row)
        sum += max(introw) - min(introw)

print sum
