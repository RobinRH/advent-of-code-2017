# answer -> 388611
# answer -> 27763113

import io

# part 1
input = [int(line) for line in open('input05.txt', 'r')]

index = 0
count = 0
while index < len(input):
    jump = input[index]
    input[index] += 1
    index += jump
    count += 1

print('part 1: ', count)

# part 2

input = [int(line) for line in open('input05.txt', 'r')]
index = 0
count = 0
while index < len(input):
    jump = input[index]
    input[index] += -1 if jump >= 3 else 1
    index += jump
    count += 1

print('part 2: ', count)

