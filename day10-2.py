# answer 4db3799145278dc9f73dcdbc680bd53d

import csv
import sys

def getSegment(numbers, position, length):
    segment = []
    longList = list(numbers)
    longList.extend(numbers)
    for i in range(length):
        segment.append(longList[position + i])

    return segment

filename = sys.argv[1]
# example {{}, {}}
with open(filename, 'r') as f:
    lines = f.readlines()

# there is only one line
line = lines[0]
print "." + line + "."
lengths = map((lambda x : ord(x)), list(line))
# then add 17, 31, 73, 47, 23
lengths.append(17)
lengths.append(31)
lengths.append(73)
lengths.append(47)
lengths.append(23)
print lengths

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
        #print location
        v.append(numbers[location])
    denseHashes.append(xor16(v))
    #print v
    #print

print denseHashes

output = ""
for d in denseHashes:
    output += format(d, '02x')

print output


'''
# checking that new def works on old data
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        lengths = map((lambda x : int(x)), row)

numbers = range(256)
numbers, position, skip = runOneRound(numbers, lengths, 0, 0)
print numbers

# multiply the first two numbers
result = numbers[0] * numbers[1]    
print result
'''
