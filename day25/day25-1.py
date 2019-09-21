#answer -> 4230

import csv
import sys
from pprint import pprint

class Rule:

    def __init__(self, state, value, write, move, newState):
        self.state = state
        self.value = value
        self.write = write
        self.move = move
        self.newState = newState

    def __str__(self):
        #return self.state
        return ' '.join([self.state, str(self.value), str(self.write), str(self.move), self.newState])

    def __format__(self):
        return self.state
        #return ' '.join([self.state, str(self.value), str(self.write), str(self.move), self.newState])


#filename = sys.argv[1]
real = True # vs. test
if real:
    state = 'A'
    steps = 12317297
    filename = "input25.txt"
else:
    state = 'A'
    steps = 6
    filename = "input25-test.txt"


total = 0
rules = {}
#values = {}
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        rstate, value, write, move, newState = row
        print state, value, write, move, newState
        #rules.append(Rule(state, value, write, move, newState))
        value = int(value)
        write = int(write)
        print move
        move = 1 if (move == 'R') else -1
        print move
        key = rstate + '-' + str(value)
        rules[key] = Rule(rstate, value, write, move, newState)

pprint(rules)
for r in rules.values():
    print r


loc = 0
values = {}
ones = set()
zeros = set()
current = 0
for i in range(steps):
    #print i
    # find the matching rule, which is based on state and value    
    key = state + '-' + str(current)
    rule = rules[key]
    #print rule
    if rule.write == 1:
        ones.add(loc)
        #if loc in zeros: zeros.remove(loc)
    else:
        if loc in ones: ones.remove(loc)
        #zeros.add(loc)
    loc += rule.move
    state = rule.newState
    current = 1 if loc in ones else 0 
    #print ones

'''
lst = [0] * 20
for k in values.keys():
    lst[k + 10] = values[k]

print lst
'''

print ones
print len(ones)
