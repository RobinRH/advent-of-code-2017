# answer: 3025 (counter goes out of range)
# 
# https://adventofcode.com/2017/day/23

import csv
import sys

class Instruction:

    def __init__(self, keywordAndArgs):
        self.keyword = keywordAndArgs[0]

        if keywordAndArgs[1] in 'abcdefgh':
            self.X = keywordAndArgs[1]
        else:
            self.X = int(keywordAndArgs[1])

        if len(keywordAndArgs) == 3:
            if keywordAndArgs[2] in 'abcdefgh':
                self.Y = keywordAndArgs[2]
            else:
                self.Y = int(keywordAndArgs[2])
        else:
            self.Y = 0

    def __str__(self):
        return self.keyword + " " + str(self.X) + " " + str(self.Y)

filename = sys.argv[1]

instructions = []
with open(filename, 'r') as f:
    lines = [line.strip().split(' ') for line in f]

for line in lines:
    instructions.append(Instruction(line))

registers = {r:0 for r in list('abcdefghijklmnop')}

counter = 0
mulTotal = 0
while counter < len(instructions):
    inst = instructions[counter]
    if inst.keyword == 'set': # set register X to value Y
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        registers[inst.X] = yValue
        counter += 1
    elif inst.keyword == 'sub': # increment register X by value Y
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        registers[inst.X] = registers[inst.X] - yValue
        counter += 1
    elif inst.keyword == 'mul': # multiply register X by value Y
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        registers[inst.X] = registers[inst.X] * yValue
        counter += 1
        mulTotal += 1
    elif inst.keyword == 'jnz': # if X > 0, then jump Y
        xValue = inst.X if (type(inst.X) is int) else registers[inst.X]
        yValue = inst.Y if (type(inst.Y) is int) else registers[inst.Y]
        if xValue != 0:
            counter += yValue
        else:
            counter += 1
    else:
        print "instruction not found: " + inst.keyword


print mulTotal
    