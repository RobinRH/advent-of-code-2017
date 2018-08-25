#answer -> 363010
#input -> 361527
import sys

def sumNeighbors(matrix, row, col):
    sum = (
        matrix[row-1][col-1] +
        matrix[row-1][col] +
        matrix[row-1][col+1] +
        matrix[row][col-1] +
        matrix[row][col+1] +
        matrix[row+1][col-1] +
        matrix[row+1][col] +
        matrix[row+1][col+1])
    return sum

def countNeighbors(matrix, row, col):
    sum = 0
    #print matrix[row-1][col-1]
    if matrix[row-1][col-1] != 0: sum += 1
    if matrix[row-1][col] != 0: sum += 1
    if matrix[row-1][col+1] != 0: sum += 1
    if matrix[row][col-1] != 0: sum += 1
    if matrix[row][col+1] != 0: sum += 1
    if matrix[row+1][col-1] != 0: sum += 1
    if matrix[row+1][col] != 0: sum += 1
    if matrix[row+1][col+1] != 0: sum += 1
    #print "number of neighbors: " + str(sum)
    return sum

def printLocation(matrix, row, col):
    width = 3
    for i in range(row-width, row + width + 1):
        line = ""
        for j in range(col - width, col + width + 1):
            #line += str(matrix[i][j]) + " "
            line += '{:6}'.format(matrix[i][j]) + " "
        print line
    print ""

def printAndQuit(matrix, row, col):
    matrix[row][col] = -1
    printLocation(matrix, row, col)
    exit()
    


number = int(sys.argv[1])
print "The number is: " + str(number)
print number

w, h = 999,999
matrix = [[0 for x in range(w)] for y in range(h)] 

# set the center value
center = w/2
matrix[center][center] = 1

row = center
col = center
left = 0
right = 1
up = 2
down = 3

direction = right

# let's fill in the first square
matrix[center][center] = 1
matrix[center-1][center-1] = 5
matrix[center-1][center] = 4
matrix[center-1][center+1] = 2
matrix[center][center-1] = 10
matrix[center][center+1] = 1
matrix[center+1][center-1] = 11
matrix[center+1][center] = 23
matrix[center+1][center+1] = 25

printLocation(matrix, center, center)

row = center + 1
col = center + 1
print row, col

found = False
count = 1
while not found:
    # row, col are of the previous value
    count += 1
    if count > 60:
        printAndQuit(matrix, row, col)


    if direction == right:
        col += 1
    if direction == left:
        col -= 1
    if direction == up:
        row -= 1
    if direction == down:
        row += 1

    if direction == right:
        if countNeighbors(matrix, row, col) >= 2:
            matrix[row][col] = sumNeighbors(matrix, row, col)
        else:
            direction = up
            col -= 1
            row -= 1
            matrix[row][col] = sumNeighbors(matrix, row, col)
    elif direction == up:
        if countNeighbors(matrix, row, col) >= 2:
            matrix[row][col] = sumNeighbors(matrix, row, col)
        else:
            direction = left
            col -= 1
            row += 1
            matrix[row][col] = sumNeighbors(matrix, row, col)
    elif direction == left:
        if countNeighbors(matrix, row, col) >= 2:
            matrix[row][col] = sumNeighbors(matrix, row, col)
        else:
            direction = down
            col += 1
            row += 1
            matrix[row][col] = sumNeighbors(matrix, row, col)
    elif direction == down:
        if countNeighbors(matrix, row, col) >= 2:
            matrix[row][col] = sumNeighbors(matrix, row, col)
        else:
            direction = right
            col += 1
            row -= 1
            matrix[row][col] = sumNeighbors(matrix, row, col)

    printLocation(matrix, row, col)

    if matrix[row][col] > number:
        found = True
        print "found!"
        printLocation(matrix, row, col)
    else:
        print matrix[row][col], number


print matrix[row][col]

