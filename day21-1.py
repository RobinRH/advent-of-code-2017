#answer -> 194

import sys
import csv
import numpy as np 
from pprint import pprint

# determines if input is a match for the rule
def ruleMatches(input, rule, size):
    """ input: '1111' rule: '1111' => '111000111' returns: array or None"""

    intList = map(lambda x: int(x), list(input)) # list like [1,1,1,1]
    inputArray = np.array(intList).reshape((size, size)) # array like [[1,1],[1,1]]

    tokens = rule.split(" => ")
    key, value = tokens[0], tokens[1] # key is like '1111'
    intList = map(lambda x: int(x), list(key)) # list like [1,1,1,1]
    keyArray = np.array(intList).reshape((size, size)) # array like [[1,1],[1,1]]
    
    intList = map(lambda x: int(x), list(value)) # list like [1,1,1,1]
    valueArray = np.array(intList).reshape((size + 1, size + 1)) # array like [[1,1],[1,1]]

    keyBase = keyArray
    keyFlip = np.flip(keyBase, axis=1)
    variations = []
    variations.append(keyBase)
    variations.append(keyFlip)
    variations.append(np.rot90(keyBase, k=1))
    variations.append(np.rot90(keyBase, k=2))
    variations.append(np.rot90(keyBase, k=3))
    variations.append(np.rot90(keyFlip, k=1))
    variations.append(np.rot90(keyFlip, k=2))
    variations.append(np.rot90(keyFlip, k=3))

    # see if the input is in the variations
    found = False
    for v in variations:
        if np.sum(v == inputArray) == size*size:
            found = True
            print 'l', input, key, value
            break

    if found:
        return valueArray
    else:
        return None



start = '.#./..#/###'.replace('\n','').replace('/','').replace('.','0').replace('#', '1')

rules2 = []
rules3 = []

filename = sys.argv[1]
with open(filename, 'r') as f:
    for row in f:
        newRow = row.replace('\n','').replace('/','').replace('.','0').replace('#', '1')
        if len(row) < 25: # is a 2-rule
            rules2.append(newRow)
        else: # is a 3-rule
            rules3.append(newRow)

#pprint(rules2)
#pprint(rules3)


# iteration 1, 3x3 -> 4x4
result1 = np.zeros((4,4), dtype = int)
for r in rules3:
    match = ruleMatches(start, r, 3)
    if not match is None:
        result1 = match
        break

print result1

# iteration 2, 4x4->6x6
# start is an array, so must convert back to list
#start = start.reshape((1,16))
#start = list(start[0])
#print start
result2 = np.zeros((6,6), dtype=int)
for row in [0,1]:
    for col in [0,1]:
        block = result1[row * 2:row*2 + 2, col*2:col*2+ 2]
        # convert block to '1111'
        block = block.reshape((1,4))
        block = list(block[0])
        block = map(lambda x: str(x), block)
        block = ''.join(block)
        # find the match for the block
        for r in rules2:
            match = ruleMatches(block, r, 2)
            if not match is None:
                result2[row*3:row*3+3, col*3:col*3+3] = match

print result2


# iteration 3, 6x6->9x9
result3 = np.zeros((9,9), dtype=int)
for row in range(3):
    for col in range(3):
        block = result2[row * 2:row*2 + 2, col*2:col*2+ 2]
        # convert block to '1111'
        block = block.reshape((1,4))
        block = list(block[0])
        block = map(lambda x: str(x), block)
        block = ''.join(block)
        # find the match for the block
        for r in rules2:
            match = ruleMatches(block, r, 2)
            if not match is None:
                result3[row*3:row*3+3, col*3:col*3+3] = match

print result3
print np.sum(result3)

# iteration 4, 9x9->12x12
result4 = np.zeros((12,12), dtype=int)
for row in range(3):
    for col in range(3):
        block = result3[row * 3:row*3 + 3, col*3:col*3+ 3]
        # convert block to '1111'
        block = block.reshape((1,9))
        block = list(block[0])
        block = map(lambda x: str(x), block)
        block = ''.join(block)
        # find the match for the block
        found = False
        for r in rules3:
            match = ruleMatches(block, r, 3)
            if not match is None:
                result4[row*4:row*4+4, col*4:col*4+4] = match
                found = True
        #print block, found

print result4
print np.sum(result4)

# iteration 5 12x12 -> 18x18
result5 = np.zeros((18,18), dtype=int)
for row in range(6):
    for col in range(6):
        block = result4[row * 2:row*2 + 2, col*2:col*2+ 2]
        # convert block to '1111'
        block = block.reshape((1,4))
        block = list(block[0])
        block = map(lambda x: str(x), block)
        block = ''.join(block)
        # find the match for the block
        for r in rules2:
            match = ruleMatches(block, r, 2)
            if not match is None:
                result5[row*3:row*3+3, col*3:col*3+3] = match

print result5
print np.sum(result5)
