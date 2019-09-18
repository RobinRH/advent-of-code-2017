# answer -> 451
# answer -> 223

import io
import itertools

# part 1
valid = 0
for line in open('input04.txt', 'r'):
    words = [s for s in line.strip().split(' ') if s]
    if len(words) == len(set(words)):
        valid += 1

print('part 1: ', valid)

# part 2
valid = 0
for line in open('input04.txt', 'r'):
    words = [''.join(sorted(s)) for s in line.strip().split(' ') if s]
    if len(words) == len(set(words)):
        valid += 1

print('part 2: ', valid)
