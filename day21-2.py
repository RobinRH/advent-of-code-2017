#answer -> 2536879

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
    
    if np.sum(inputArray) != np.sum(keyArray) : return None

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
            #print 'l', input, key, value
            break

    if found:
        return valueArray
    else:
        return None


def createRule(rule, size):
    """rule: '1111' => '111000111' returns: keyArray, valueArray, variations"""

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

    return (keyArray, valueArray, variations)


# determines if input is a match for the rule
def ruleMatchesTuplet(input, (keyArray, valueArray, variations), size):

    intList = map(lambda x: int(x), list(input)) # list like [1,1,1,1]
    inputArray = np.array(intList).reshape((size, size)) # array like [[1,1],[1,1]]

    if np.sum(inputArray) != np.sum(keyArray) : return None

    # see if the input is in the variations
    found = False
    for v in variations:
        if np.sum(v == inputArray) == size*size:
            found = True
            #print 'l', input, key, value
            break

    if found:
        return valueArray
    else:
        return None




start = '.#./..#/###'.replace('\n','').replace('/','').replace('.','0').replace('#', '1')

rules2 = []
rules3 = []


# instead of storing the string for a rule, store the string and the variations
# could also limit search to only those rules where the key has the same number of dots (try that next)
filename = sys.argv[1]
with open(filename, 'r') as f:
    for row in f:
        newRow = row.replace('\n','').replace('/','').replace('.','0').replace('#', '1')
        if len(row) < 25: # is a 2-rule
            rules2.append(createRule(newRow,2))
        else: # is a 3-rule
            rules3.append(createRule(newRow,3))

#pprint(rules2)
#pprint(rules3)

startList = map(lambda x: int(x), list(start)) # list like [1,1,1,1]
startArray = np.array(startList).reshape((3, 3)) # array like [[1,1],[1,1]]
result = startArray
size = 3
for i in range(18):
    if size%2 == 0: # divisible by 2
        newSize = (size / 2) * 3
        # iteration 3, 6x6->9x9
        newResult = np.zeros((newSize, newSize), dtype=int)
        for row in range(size / 2):
            for col in range(size / 2):
                block = result[row * 2:row*2 + 2, col*2:col*2+ 2]
                # convert block to '1111'
                block = block.reshape((1,4))
                block = list(block[0])
                block = map(lambda x: str(x), block)
                block = ''.join(block)
                # find the match for the block
                for r in rules2:
                    match = ruleMatchesTuplet(block, r, 2)
                    if not match is None:
                        newResult[row*3:row*3+3, col*3:col*3+3] = match

        #print newResult
        print "i: ", i
        print "size: ", newSize
        print "total: ", np.sum(newResult)
        result = newResult
        size = newSize
    else: # divisible by 3
        # iteration 4, 9x9->12x12
        newSize = (size / 3) * 4
        newResult = np.zeros((newSize, newSize), dtype=int)
        for row in range(size / 3):
            for col in range(size / 3):
                block = result[row * 3:row*3 + 3, col*3:col*3+ 3]
                # convert block to '1111'
                block = block.reshape((1,9))
                block = list(block[0])
                block = map(lambda x: str(x), block)
                block = ''.join(block)
                # find the match for the block
                found = False
                for r in rules3:
                    match = ruleMatchesTuplet(block, r, 3)
                    if not match is None:
                        newResult[row*4:row*4+4, col*4:col*4+4] = match
                        found = True
                #print block, found

        #print newResult
        print "i: ", i
        print "size: ", newSize
        print "total: ", np.sum(newResult)
        result = newResult
        size = newSize

'''
takes several minutes to run
i:  0
size:  4
total:  12
i:  1
size:  6
total:  28
i:  2
size:  9
total:  55
i:  3
size:  12
total:  59
i:  4
size:  18
total:  194
i:  5
size:  27
total:  389
i:  6
size:  36
total:  563
i:  7
size:  54
total:  1762
i:  8
size:  81
total:  3481
i:  9
size:  108
total:  5093
i:  10
size:  162
total:  15826
i:  11
size:  243
total:  31339
i:  12
size:  324
total:  45903
i:  13
size:  486
total:  142110
i:  14
size:  729
total:  281939
i:  15
size:  972
total:  413597
i:  16
size:  1458
total:  1277562
i:  17
size:  2187
total:  2536879

'''