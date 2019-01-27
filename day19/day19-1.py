# answer -> FEZDNIVJWT
# answer -> 17200
'''
     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
'''

import csv
import sys
import numpy as np 
np.set_printoptions(threshold=np.nan, linewidth=2000,)



filename = sys.argv[1]

f = open(filename, 'r')
lines = f.readlines()
charlines = map(lambda x: x.replace(' ', '.'), lines)
charlines = map(lambda x: list(x), charlines)
diagram = np.array(charlines)
diagram=np.pad(diagram, 1, 'constant', constant_values = 4)
for r in range(diagram.shape[0]):
    for c in range(diagram.shape[1]):
        if diagram[r, c] == '4':
            diagram[r, c] = ' '


def canMove(diagram, direction, (row, col)):
    if direction == down:
        if diagram[row + 1, col] in list(' .'):
            return False
    elif direction == up:
        if diagram[row - 1, col] in list(' .'):
            return False
    elif direction == left:
        if diagram[row, col - 1] in list(' .'):
            return False
    elif direction == right:
        if diagram[row, col + 1] in list(' .'):
            return False

    return True



def nextLocation(diagram, direction, (row, col)):
    if direction == down:
        return (row + 1, col)
    elif direction == up:
        return (row - 1, col)
    elif direction == left:
        return (row, col - 1)
    elif direction == right:
        return (row, col + 1)

    return (-1, -1)

def getNextDirection(diagram, direction, (row, col)):
    if direction == down: #look left and right
        if diagram[row, col-1] in list('-ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return left 
        else:
            return right
    elif direction == up:
        if diagram[row, col-1] in list('-ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return left 
        else:
            return right
    elif (direction == left) or (direction == right):
        if diagram[row -1, col] in list('|ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            return up
        else:
            return down

down = 1
up = 2
left = 3
right = 4

# find the starting point
(row, col) = (1, charlines[0].index('|') + 1)
direction = down

word = []
moves = 0
while canMove(diagram, direction, (row, col)):
    # move to next space
    row, col = nextLocation(diagram, direction, (row, col))
    element = diagram[row, col]
    if element in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        word.append(element)

    if element == '+': # change direction
        direction = getNextDirection(diagram, direction, (row, col))

    moves += 1
    if moves > 50000:
        exit()

print ''.join(word)
print moves + 1


