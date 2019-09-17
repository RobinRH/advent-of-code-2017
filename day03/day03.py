# input -> 361527
# answer -> 326
# answer -> 363010

import math
import itertools

# ulam spiral
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

input = 361527

left, right, up, down = 1, 2, 3, 4
# xmove, ymove, xleft, yleft, newdirection
moves = {
    right: (1, 0, 0, -1, up),
    left: (-1, 0, 0, 1, down),
    up: (0, -1, -1, 0, left),
    down: (0, 1, 1, 0, right)
}

size = int(math.sqrt(input)) * 3
start = size // 2

# part 1

# create grid
grid = [ [ 0 for x in range(size)] for y in range(size)]
direction = right
x = start
y = start
grid[start][start] = 1
n = 1
while n < input:
    n += 1

    # move straight
    xmove, ymove, xleft, yleft, newdirection = moves[direction]
    x, y = x + xmove, y + ymove
    
    grid[x][y] = n

    # move left if empty
    if grid[x + xleft][y + yleft] == 0:
        direction = newdirection

distance = abs(start - x) + abs(start - y)
print('part 1: ', distance)

# part 2

# create grid
grid = [ [ 0 for x in range(size)] for y in range(size)]
direction = right
x = start
y = start
grid[start][start] = 1
local = 0
neighbors = [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1]]

while local < input:
    # move straight
    xmove, ymove, xleft, yleft, newdirection = moves[direction]
    x, y = x + xmove, y + ymove

    local = 0
    for i, j in neighbors:
        xlocal, ylocal = x + i, y + j
        local += grid[xlocal][ylocal]
    grid[x][y] = local

    # move left if empty
    if grid[x + xleft][y + yleft] == 0:
        direction = newdirection

print('part 2: ', local)
