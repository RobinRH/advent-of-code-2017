#answer part 1 -> 7864
#answer part 2 -> 1695

import csv
import sys

print sys.argv[1]
filename = sys.argv[1]

# row1 is test input, row2 is real input
banks = []
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        banks = list(map(lambda x: int(x), row))

print banks
states = []
state = ""
states.append(reduce((lambda x, y: str(x) + "-" + str(y)), banks))
foundRepeat = False
count = 0
while (not foundRepeat):
    # find the back with the most blocks
    maxBank = (0, 0) # tuple is number of blocks and bank index

    for i in range(len(banks)):
        if banks[i] > maxBank[0]:
            maxBank = (banks[i], i)

    print maxBank

    # redistribute the blocks
    banks[maxBank[1]] = 0
    location = maxBank[1] + 1
    for block in range(maxBank[0]):
        if (location == len(banks)): location = 0
        banks[location] += 1
        location += 1

    # change to string and join
    state = reduce((lambda x, y: str(x) + "-" + str(y)), banks)
    states.append(state)

    print state
    print count
    count += 1
    if count > 10000: exit()

    # find out if there are any duplicates in the states
    unique = set(states)
    if (len(states) != len(unique)):
        foundRepeat = True

print "Answer part 1: ", count

# find out the two locations of the repeat
firstIndex = states.index(state)
lastIndex = count
loopsize =  lastIndex - firstIndex
print "Answer part 2, loop size: " + str(loopsize)

