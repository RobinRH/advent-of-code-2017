# answer -> 326
# answer -> 363010

import math

# ulam spiral
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

# part 1

left, right, up, down = 1, 2, 3, 4
input = 361527

# create grid
size = int(math.sqrt(input)) * 3
grid = [ [ 0 for x in range(size)] for y in range(size)]
start = size // 2
direction = right
current = (start, start)
grid[start][start] = 1
n = 1
while n < input:
    n += 1

    # move straight
    if direction == right:
        current = (current[0] + 1, current[1])
    elif direction == left:
        current = (current[0] - 1, current[1])
    elif direction == up:
        current = (current[0], current[1]-1)
    else:
        current = (current[0], current[1] + 1)

    grid[current[0]][current[1]] = n

    # turn if square to the left is empty
    if direction == right:
        if grid[current[0]][current[1]-1] == 0:
            direction = up
    elif direction == left:
        if grid[current[0]][current[1]+1] == 0:
            direction = down
    elif direction == up:
        if grid[current[0]-1][current[1]] == 0:
            direction = left
    else: # down
        if grid[current[0]+1][current[1]] == 0:
            direction = right

distance = abs(start - current[0]) + abs(start - current[1])
print('part 1: ', distance)


# part 2
left, right, up, down = 1, 2, 3, 4
input = 361527

# create grid
size = int(math.sqrt(input)) * 3
grid = [ [ 0 for x in range(size)] for y in range(size)]
start = size // 2
direction = right
current = (start, start)
grid[start][start] = 1
n = 1
local = 0
while local < input:
    n += 1

    # move straight
    if direction == right:
        current = (current[0] + 1, current[1])
    elif direction == left:
        current = (current[0] - 1, current[1])
    elif direction == up:
        current = (current[0], current[1]-1)
    else:
        current = (current[0], current[1] + 1)

    # get sum of surrounding squares
    local = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            xlocal = current[0] + i
            ylocal = current[1] + j
            local += grid[xlocal][ylocal]
    grid[current[0]][current[1]] = local

    # turn if square to the left is empty
    if direction == right:
        if grid[current[0]][current[1]-1] == 0:
            direction = up
    elif direction == left:
        if grid[current[0]][current[1]+1] == 0:
            direction = down
    elif direction == up:
        if grid[current[0]-1][current[1]] == 0:
            direction = left
    else: # down
        if grid[current[0]+1][current[1]] == 0:
            direction = right


distance = abs(start - current[0]) + abs(start - current[1])
print('part 2: ', local)
