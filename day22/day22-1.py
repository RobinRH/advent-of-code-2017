#answer -> 5256
'''
If the current node is infected, it turns to its right.
Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)

If the current node is clean, it becomes infected.
Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)

The virus carrier moves forward one node in the direction it is facing.
'''

import sys
import csv
import numpy as np 
from pprint import pprint

def printInfections(infections, (xcarrier, ycarrier)):
    map = np.zeros((10,10))
    for (row, col) in infections:
        map[row, col] = 1
    map[xcarrier, ycarrier] = 9
    print map

filename = sys.argv[1]
offset = 1000
row = 0
infections = []
with open(filename, 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        lineList = list(line)
        for col in range(len(line)):
            if lineList[col] == '#':
                infections.append((row + offset, col + offset))
        row += 1

#pprint(infections)

carrier = (25/2 + offset, 25/2 + offset)
print "carrier: ", carrier

left = 1
right = 2
up = 3
down = 4

#printInfections(infections, carrier)
print
direction = up
total = 0
for i in range(10000):
    '''
    If the current node is infected, it turns to its right.
    Otherwise, it turns to its left. (Turning is done in-place; the current node does not change.)

    If the current node is clean, it becomes infected.
    Otherwise, it becomes cleaned. (This is done after the node is considered for the purposes of changing direction.)

    The virus carrier moves forward one node in the direction it is facing.
    '''

    #print i+ 1, total

    if carrier in infections:
        # turn right
        if direction == up:
            direction = right
        elif direction == down:
            direction = left
        elif direction == left:
            direction = up
        else:
            direction = down

        infections.remove(carrier)
        #print "removing"
    else:
        # turn left
        if direction == up:
            direction = left
        elif direction == down:
            direction = right
        elif direction == left:
            direction = down
        else:
            direction = up

        infections.append(carrier)
        #print "adding"
        total += 1

    # move forward one
    (row, col) = carrier
    if direction == up:
        carrier = (row - 1, col)
    elif direction == down:
        carrier = (row + 1, col)
    elif direction == left:
        carrier = (row, col - 1)
    else: #right
        carrier = (row, col + 1)
    

    #print infections
    #print "carrier: ", carrier
    print "i, total: ", i, total
    #printInfections(infections, carrier)
    #print
