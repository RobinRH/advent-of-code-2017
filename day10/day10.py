# answer-> 29240
# answer-> 4db3799145278dc9f73dcdbc680bd53d

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
        npos = npos % len(numbers)

    position = (position + length + skip) % len(numbers)

    # increment the skip
    skip += 1

# multiply the first two numbers
result = numbers[0] * numbers[1]    
print ('part 1: ', result)

# part 2

def xor16(v):
    return v[0] ^ v[1] ^ v[2] ^ v[3] ^ v[4] ^ v[5] ^ v[6] ^ v[7] ^ v[8] ^ v[9] ^ v[10] ^ v[11] ^ v[12] ^ v[13]^ v[14] ^ v[15]

def runOneRound(numbers, lengths, position, skip):

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
            npos = npos % len(numbers)

        # move the position forward, length + skip
        position = (position + length + skip) % len(numbers)

        # increment the skip
        skip += 1

    return numbers, position, skip

chars = open('input10.txt', 'r').read().strip()
lengths = [ord(x) for x in list(chars)] + [17, 31, 73, 47, 23]

position = 0
skip = 0
numbers = list(range(256))

for i in range(64):
    numbers, position, skip = runOneRound(numbers, lengths, position, skip)

denseHashes = [xor16(numbers[16*i : 16*i + 16]) for i in range(16)]
stringHashes = [format(dh, '02x') for dh in denseHashes]
output = ''.join(stringHashes)

print ('part 2: ', output)

