#answer -> 388611
import csv
import sys

filename = sys.argv[1]

instructions = []
with open(filename, 'r') as f:
    for line in f:
        instructions.append(int(line))

total = len(instructions)

nexti = 0
steps = 0
while nexti < total:
    save = nexti
    nexti = nexti + instructions[nexti]
    instructions[save] += 1
    steps += 1
    #print instructions

print steps