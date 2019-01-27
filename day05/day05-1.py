#answer -> 388611
import csv
import sys

with open(sys.argv[1], 'r') as f:
    content = f.read()
instructions = map(lambda x: int(x), content.split('\n'))

total = len(instructions)

nexti = 0
steps = 0
while nexti < total:
    save = nexti
    nexti = nexti + instructions[nexti]
    instructions[save] += 1
    steps += 1

print steps
