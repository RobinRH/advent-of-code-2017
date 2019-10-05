# answer -> 747
# answer -> 1544

import io 
import collections

moves = open('input11.txt', 'r').readline().split(',')

def getDistance(nCount, sCount, neCount, nwCount, seCount, swCount):
    if nCount > sCount:
        nCount -= sCount
        sCount = 0
    else:
        sCount -= nCount
        nCount = 0

    if neCount > swCount:
        neCount -= swCount
        swCount = 0
    else:
        swCount -= neCount
        neCount = 0

    if nwCount > seCount:
        nwCount -= seCount
        seCount = 0
    else:
        seCount -= nwCount
        nwCount = 0

    # ne + s -> se
    if min(neCount, sCount) > 0:
        diff = min(neCount, sCount)
        neCount -= diff
        sCount -= diff
        seCount += diff

    # se + n -> ne
    if min(seCount, nCount) > 0:
        diff = min(seCount, nCount)
        seCount -= diff
        nCount -= diff
        neCount += diff

    # nw + s -> sw
    if min(nwCount, sCount) > 0:
        diff = min(nwCount, sCount)
        nwCount -= diff
        sCount -= diff
        swCount += diff

    # sw + n -> nw
    if min(swCount, nCount) > 0:
        diff = min(swCount, nCount)
        swCount -= diff
        nCount -= diff
        nwCount += diff

    # se + sw -> s
    if min(seCount, swCount) > 0:
        diff = min(seCount, swCount)
        seCount -= diff
        swCount -= diff
        sCount += diff

    # ne + nw -> n
    if min(neCount, nwCount) > 0:
        diff = min(neCount, nwCount)
        neCount -= diff
        nwCount -= diff
        nCount += diff

    steps = nCount + sCount + nwCount + swCount + neCount + seCount
    return(steps)

counts = collections.Counter(moves)
print('part 1: ', getDistance(counts['n'], counts['s'], counts['ne'], counts['nw'], counts['se'], counts['sw']))

maxsteps = 0
for i in range(len(moves)):
    counts = collections.Counter(moves[:i])
    distance = getDistance(counts['n'], counts['s'], counts['ne'], counts['nw'], counts['se'], counts['sw'])
    maxsteps = max(maxsteps, distance)

print('part 2: ', maxsteps)
