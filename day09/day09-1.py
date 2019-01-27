#answer -> 11898
import csv
import sys

class Stack:

    def __init__(self):
        self.stack = []

    # the value is the score of the group
    def push(self):
        if len(self.stack) == 0:
            self.stack.append(1)
        else:
            top = self.stack[-1]
            self.stack.append(top+1)

    def pop(self):
        return self.stack.pop()

filename = sys.argv[1]
# example {{}, {}}
with open(filename, 'r') as f:
    lines = f.readlines()

# this is a sort of a state machine, and a stack problem
# just using line 1 for now
line = lines[0]

# iterate for the string
stack = Stack()
def evaluateString(line):
    # state variables
    inGroup = False
    inGarbage = False
    ignoreNext = False
    groups = 0
    score = 0
    stack = Stack()

    for char in line:
        if ignoreNext:
            ignoreNext = False
            continue

        if char == '!':
            ignoreNext = True
            continue

        if char == '<':
            inGarbage = True
            continue

        if inGarbage and char != '>':
            continue

        if char == '{':
            inGroup = True
            stack.push()
            continue

        if char == '}':
            inGroup = False
            groups += 1
            score += stack.pop()
            continue

        if char == '>':
            inGarbage = False
            continue

    return groups, score

totalscore = 0
for line in lines:
    groups, score = evaluateString(line)
    print groups, score
    totalscore += score

print totalscore
