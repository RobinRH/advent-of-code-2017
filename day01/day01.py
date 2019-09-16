# answer -> 1141
# answer -> 950
import io
import copy

# get the string
ifile = open('input01.txt', 'r')

chars = list(ifile.readlines()[0])
otherchars = chars[1:] + list(chars[0])
pairs = zip(chars, otherchars)
counters = [int(p[0]) for p in pairs if p[0]==p[1]]
print('part1: ' + str(sum(counters)))

# part two, most list halfway around
half = len(chars) // 2
otherchars = chars[half:] + chars[:half]
pairs = zip(chars, otherchars)
counters = [int(p[0]) for p in pairs if p[0]==p[1]]
print('part2: ' + str(sum(counters)))

