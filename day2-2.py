#answer -> 312
import csv
import sys

filename = sys.argv[1]

sum = 0
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        introw = map(lambda x : int(x), row)
        # do the pairwise comparisons
        found = False
        for i in range(len(introw)):
            if (not found):
                for j in range(len(introw)):
                    if (i == j): continue
                    if (not found):
                        if (introw[i] % introw[j] == 0) :
                            sum += introw[i] / introw[j]
                            found = True


print sum

