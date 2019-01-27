# answer = gjmiofcnaehpdlbk

import csv
import sys
import datetime as dt


class Step:

    def __init__(self, dtype = '', length=0, i=0, j=0, a='', b=''):
        self.length = length
        self.i = i
        self.j = j
        self.a = a
        self.b = b
        self.dtype = dtype

    def toString(self):
        print self.dtype, self.length, self.i, self.j, self.a, self.b

tran = 's'
swPo = 'x'
swPr = 'p'

filename = sys.argv[1]
stepStrings = []
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        stepStrings = row


current = list('abcdefghijklmnop')
steps = []
for step in stepStrings:
    if step.startswith('s'):
        ss = step.replace('s', '')
        a = Step(dtype = tran, length=int(ss))
        steps.append(a)

    if step.startswith('x'):
        ss = step.replace('x', '')
        parts = ss.split('/')
        a = Step(dtype = swPo, i = int(parts[0]), j = int(parts[1]))
        steps.append(a)

    if step.startswith('p'):
        ss = step[1:]
        parts = ss.split('/')
        a = Step(dtype = swPr, a = parts[0], b = parts[1])
        steps.append(a)

def executeRound(current, steps):
    for step in steps:
        if step.dtype == tran:
            current = current[16-step.length:] + current[:16-step.length]
        elif step.dtype == swPo:
            temp = current[step.i]
            current[step.i] = current[step.j]
            current[step.j] = temp
        else:
            aloc = current.index(step.a)
            bloc = current.index(step.b)
            temp = current[aloc]
            current[aloc] = current[bloc]
            current[bloc] = temp

    return current

# find the repeat
repeat = 0
seen = []
for i in range(100):
    current = executeRound(current, steps)
    output = ''.join(current)
    if output in seen:
        print "repeat: ", i
        repeat = i
        break
    else:
        seen.append(output)


howmany = 1000000000 % repeat
current = list('abcdefghijklmnop')
for i in range(howmany):
    current = executeRound(current, steps)

current = ''.join(current)
print current

