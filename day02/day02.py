# answer -> 47623
# answer -> 312

import io
from itertools import permutations

# part 1
ifile = open('input02.txt', 'r')
total = 0
for line in ifile:
    numbers = [int(n) for n in line.split('\t') if n]
    total += max(numbers) - min(numbers)

print('part 1: ' + str(total))


# part 2
totals = []
for line in open('input02.txt', 'r'):
    numbers = [int(n) for n in line.split('\t') if n]
    totals += [a // b for (a, b) in permutations(numbers, 2) if a % b == 0]

print('part 2: ', sum(totals))
