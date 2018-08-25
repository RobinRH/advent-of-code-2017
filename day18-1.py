#answer: 7071

import csv
import sys

class Instruction:

    def __init__(self, keywordAndArgs):
        self.keyword = keywordAndArgs[0]

        if keywordAndArgs[1] in 'abcdefghijklmnop':
            self.X = keywordAndArgs[1]
        else:
            self.X = int(keywordAndArgs[1])

        if len(keywordAndArgs) == 3:
            if keywordAndArgs[2] in 'abcdefghijklmnop':
                self.Y = keywordAndArgs[2]
            else:
                self.Y = int(keywordAndArgs[2])
        else:
            self.Y = 0

    def __str__(self):
        return self.keyword + " " + str(self.X) + " " + str(self.Y)

print sys.argv[1]
filename = sys.argv[1]

total = 0
instructions = []
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        total += 1
        instructions.append(Instruction(row))
        print row

for i in instructions:
    print i

regNames = list('abcdefghijklmnop')
registers = dict()
for r in regNames:
    registers[r] = 0

#print registers

counter = 0
lastFrequency = 0
while True:
    inst = instructions[counter]
    if inst.keyword == 'snd': # play sound with frequency X and record last frequency
        lastFrequency = inst.X if (type(inst.X) is int) else registers[inst.X]
        print "playing: ", lastFrequency
        counter += 1
    elif inst.keyword == 'set': # set register X to value Y
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        registers[inst.X] = yValue
        counter += 1
    elif inst.keyword == 'add': # increment register X by value Y
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        registers[inst.X] = registers[inst.X] + yValue
        counter += 1
    elif inst.keyword == 'mul': # multiply register X by value Y
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        registers[inst.X] = registers[inst.X] * yValue
        counter += 1
    elif inst.keyword == 'mod': # set register X to X % Y
        print inst
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        registers[inst.X] = registers[inst.X] % yValue
        counter += 1
    elif inst.keyword == 'rcv': # recover lastFrequency if X > 0
        xValue = inst.X if (type(inst.X) is int) else registers[inst.X]

        if xValue > 0:
            print "recovering: ", lastFrequency
            break
        else:
            counter += 1
    elif inst.keyword == 'jgz': # if X > 0, then jump Y
        xValue = inst.X if (type(inst.X) is int) else registers[inst.X]
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        if xValue > 0:
            counter += yValue
        else:
            counter += 1
    else:
        print "instruction not found: " + inst.keyword

    print registers