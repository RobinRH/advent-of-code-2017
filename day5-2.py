#answer -> 27763113
import csv
import sys

print sys.argv[1]
filename = sys.argv[1]

total = 0
instructions = []
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        total += 1
        instructions.append(int(row[0]))

#print instructions
#print total


nexti = 0
steps = 0
while nexti < total:
    save = nexti
    nexti = nexti + instructions[nexti]
    if instructions[save] >= 3:
        instructions[save] -= 1
    else:
        instructions[save] += 1
    steps += 1
    #print instructions

print steps