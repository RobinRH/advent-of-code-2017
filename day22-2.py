#answer -> 2511345

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

clean = 0 
weakened = 1
infected = 2
flagged = 3

evolutions = [1, 2, 3, 0]

filename = sys.argv[1]
offset = 1000
row = 0
visited = {}

with open(filename, 'r') as f:
    for line in f:
        line = line.replace('\n', '')
        lineList = list(line)
        for col in range(len(line)):
            if lineList[col] == '#':
                visited[(row + offset, col + offset)] = 'i'
        row += 1

#pprint(infected)

carrier = (25/2 + offset, 25/2 + offset)
print "carrier: ", carrier


left = 0
right = 1
up = 2
down = 3

rights = [up, down, right, left]
lefts = [down, up, left, right]
reverses = [right, left, down, up]

leftMove = (0, -1)
rightMove = (0, 1)
upMove = (-1, 0)
downMove = (1, 0)

moves = [
    leftMove,
    rightMove,
    upMove,
    downMove
]

direction = up
total = 0
for j in range(10):
    for i in range(1000000):
        if carrier in visited:
            status = visited[carrier]
            if status == 'c': # turn left
                direction = lefts[direction]
                visited[carrier] = 'w'
            elif status == 'w': # if weakened, do not turn, add to infected
                visited[carrier] = 'i'
                total += 1
            elif status ==  'i': # if infected, turn right, add to flagged
                direction = rights[direction]
                visited[carrier] = 'f'
            elif status ==  'f': # if infected, turn right, add to flagged
                direction = reverses[direction]
                visited[carrier] = 'c'
        else:
            direction = lefts[direction]
            visited[carrier] = 'w'

        (row, col) = carrier
        moveRow, moveCol = moves[direction]
        carrier = (row + moveRow, col + moveCol)


print total