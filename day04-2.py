#answer -> 223
import csv
import sys

print sys.argv[1]
filename = sys.argv[1]
rows = []

# sort each word and then do the sets

totalCount = 0
badCount = 0
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        #print row
        totalCount += 1
        for i in range(len(row)):
            row[i] = reduce(lambda x,y: x+y, sorted(row[i]))
        unique = set(row)
        if len(row) != len(unique):
            print "bad passwords: " + str(row)
            badCount +=1

print totalCount
goodCount = totalCount - badCount
print goodCount
