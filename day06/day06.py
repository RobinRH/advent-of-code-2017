# answer -> 7864
# answer -> 1695

input = '0 5 10 0 11 14 13 4 11 8 8 7 1 4 12 11'
input = [int(x) for x in input.split() if x]

# part 1
seen = []
key1 = '-'.join([str(x) for x in input])
seen.append(key1)

while len(seen) == len(set(seen)):

    maxblocks = max(input)
    index = input.index(maxblocks)
    input[index] = 0
    start = index + 1
    for i in range(maxblocks):
        location = (start + i) % len(input)
        input[location] += 1

    key = '-'.join([str(x) for x in input])
    seen.append(key)

print('part 1: ', len(seen) - 1)

lastkey = seen[-1]
firstkey = seen.index(lastkey)
print('part 2: ', len(seen) - 1 - firstkey)
