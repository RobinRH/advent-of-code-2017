#answer -> 451
import csv
import sys

print sys.argv[1]
filename = sys.argv[1]
rows = []

totalCount = 0
badCount = 0
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        #print row
        totalCount += 1
        unique = set(row)
        if len(row) != len(unique):
            print "bad passwords: " + str(row)
            badCount +=1

print totalCount
goodCount = totalCount - badCount
print goodCount
