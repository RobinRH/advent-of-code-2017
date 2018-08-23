# test flqrgnkx -> 1242
# input ljoxqyyw -> 1074

import csv
import sys
import numpy as np
np.set_printoptions(threshold=np.nan, linewidth=2000,)

# convert each character in output to 4 bits (binary)

def charToBin(letter):
    bins = {
        "0" : "0000",
		"1" : "0001",
		"2" : "0010",
		"3" : "0011",
		"4" : "0100",
		"5" : "0101",
		"6" : "0110",
		"7" : "0111",
		"8" : "1000",
		"9" : "1001",
		"a" : "1010",
		"b" : "1011",
		"c" : "1100",
		"d" : "1101",
		"e" : "1110",
		"f" : "1111"
	}

    return bins[letter]



def getLengths(input):
    lengths = map((lambda x : ord(x)), list(input))
    # then add 17, 31, 73, 47, 23
    lengths.append(17)
    lengths.append(31)
    lengths.append(73)
    lengths.append(47)
    lengths.append(23)
    return lengths



def getSegment(numbers, position, length):
    segment = []
    longList = list(numbers)
    longList.extend(numbers)
    for i in range(length):
        segment.append(longList[position + i])

    return segment

def runOneRound(numbers, lengths, position, skip):
    '''
    For each length:
    Reverse the order of that length of elements in the list, starting with the element at the current position.
    Move the current position forward by that length plus the skip size.
    Increase the skip size by one.
    '''

    for length in lengths:
        # get the list to reverse
        segment = getSegment(numbers, position, length)

        # reverse the list
        segment.reverse()

        # copy the list to the numbers at position
        npos = position
        for i in range(length):
            numbers[npos] = segment[i]
            npos += 1
            if npos == len(numbers):
                npos = 0

        # move the position forward, length + skip
        for i in range(length + skip):
            position += 1
            if position == len(numbers):
                position = 0

        # increment the skip
        skip += 1

    return numbers, position, skip

def getInputs(input):
    inputs = []
    for i in range(128):
        inputs.append(input + '-' + str(i))
    return inputs

inputs = getInputs('ljoxqyyw')

totalOnes = 0
outputs = []
for input in inputs:

    lengths = getLengths(input)

    position = 0
    skip = 0
    numbers = range(256)

    for i in range(64):
        numbers, position, skip = runOneRound(numbers, lengths, position, skip)

    def xor16(v):
        return v[0] ^ v[1] ^ v[2] ^ v[3] ^ v[4] ^ v[5] ^ v[6] ^ v[7] ^ v[8] ^ v[9] ^ v[10] ^ v[11] ^ v[12] ^ v[13]^ v[14] ^ v[15]

    sparseHash = numbers

    # create the 16 elements of the dense hash
    denseHashes = []
    for i in range(16):
        v = []
        for j in range(16):
            location = (16 * i) + j
            v.append(numbers[location])
        denseHashes.append(xor16(v))

    output = ""
    for d in denseHashes:
        output += format(d, '02x')

    sys.stdout.write(".")
    sys.stdout.flush() 

    row = ''.join(map((lambda x : charToBin(x)), output))
    outputs.append(row)
    totalOnes += row.count('1')

# convert the 1s and 0s to integers in an array
numbers = []
for output in outputs:
    n = map(lambda x : int(x), output)
    numbers.append(n)

arr = np.array(numbers)
arr = np.pad(arr, 1, 'constant')
numbers = arr

def findOne(numbers):
    for i in range(130):
        for j in range(130):
            if numbers[i][j] == 1:
                return i, j

    return -1, -1


def assignNeigbors(numbers, nGroup, row, col):
    new = 0
    locs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for loc in locs:
        if numbers[row+loc[0]][col+loc[1]] == 1: 
            numbers[row+loc[0]][col+loc[1]] = nGroup
            new += 1
    return new
    
def hasOnes(numbers):
    for i in range(130):
        for j in range(130):
            if numbers[i][j] == 1:
                return True

    return False

assigned = 0
nGroup = 2
while hasOnes(numbers):
    # find a 1
    row, col = findOne(numbers)
    # assign the next group number to it (nGroup)
    numbers[row][col] = nGroup
    
    foundSome = True
    while (foundSome) :
        foundCount = 0
        foundSome = False
        for i in range(130):
            for j in range(130):
                if numbers[i][j] == nGroup:
                    foundCount += assignNeigbors(numbers, nGroup, i, j)
        if foundCount > 0: foundSome = True
        
    nGroup += 1
    if nGroup > 2000: exit()

print "answer: " + str(nGroup - 2)


