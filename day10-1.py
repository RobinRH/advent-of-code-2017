#answer 29240

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

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        #print row
        lengths = map((lambda x : int(x)), row)
        #print lengths

position = 0
skip = 0
numbers = range(256)
print numbers

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

    print numbers, length, position, skip

# multiply the first two numbers
result = numbers[0] * numbers[1]    
print result

