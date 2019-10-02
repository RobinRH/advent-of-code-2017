#answer 29240

import sys
import io


inputString = open('input10.txt', 'r').read().strip()
lengths = [int(x) for x in inputString.split(',')]
position = 0
skip = 0
numbers = list(range(256))

'''
For each length:
Reverse the order of that length of elements in the list, starting with the element at the current position.
Move the current position forward by that length plus the skip size.
Increase the skip size by one.
'''

for length in lengths:
    # get the list to reverse
    segment = (numbers*2)[position:position+length]

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
    for i in list(range(length + skip)):
        position += 1
        if position == len(numbers):
            position = 0

    # increment the skip
    skip += 1

# multiply the first two numbers
result = numbers[0] * numbers[1]    
print ('part 1: ', result)
