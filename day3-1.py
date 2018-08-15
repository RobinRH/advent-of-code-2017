#answer -> 326
#input -> 361527
import sys

number = int(sys.argv[1])

# find the first square larger than the number
found = False
root = -1
while (not found):
    if (root > 1000): found = True
    root += 2
    if (root * root > number):
        found = True

print root

# complete square
root = root - 2

#remainder = number - (complete * complete)

#side = complete + 1

#center = (side/2, side/2) + 1

# create a dictionary of the last ring, stop when you read the number
col = root + 1
row = root
for i in range(root * root + 1, number + 1):
    print i, row, col
    if (i == number): 
        break
    # where does the next number go?
    if (col == root + 1):
        row -= 1
        if (row < 0):
            row = 0
            col -= 1
            continue
        continue
    if (row == 0):
        col -= 1
        if (col < 0):
            col = 0
            row = 1
            continue
        continue
    if (col == 0):
        row += 1
        if (row > root + 1):
            row = root + 1
            col = 1
            continue
        continue
    if (row == root + 1):
        col += 1
        continue

print row, col

center = ((root + 2) / 2)

distance = abs(row - center) + abs(col - center)

print distance
