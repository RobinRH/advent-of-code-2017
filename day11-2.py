# answer 1544

import csv
import sys

# find the maximum distance
# get the distance after each step and keep the max


filename = sys.argv[1]
moves = []

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        #print row
        moves = row

def getCounts(moves):
    # count up each occurence
    # n, w, ne, nw, se, sw
    nCount = moves.count('n')
    sCount =  moves.count('s')
    neCount =  moves.count('ne')
    nwCount =  moves.count('nw')
    seCount =  moves.count('se')
    swCount =   moves.count('sw')

    return nCount, sCount, neCount, nwCount, seCount, swCount


def firstTry(nCount, sCount, neCount, nwCount, seCount, swCount):
    # north cancels south
    n_sDiff = abs(nCount - sCount)

    # ne cancels sw
    ne_swDiff = abs(neCount - swCount)

    # nw cancels se
    nw_seDiff = abs(nwCount - seCount)

    # what's left is the number of steps
    steps = n_sDiff + ne_swDiff + nw_seDiff

    return steps

def secondTry(nCount, sCount, neCount, nwCount, seCount, swCount):

    steps = 0

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
    return steps

#print nCount, sCount, neCount, nwCount, seCount, swCount, len(moves)

#steps = secondTry(nCount,sCount,neCount,nwCount, seCount, swCount)
#print steps

nCount, sCount, neCount, nwCount, seCount, swCount = getCounts(moves)
steps = secondTry(nCount,sCount,neCount,nwCount, seCount, swCount)
print steps

maxSteps = 0
while (len(moves) > 0):
    nCount, sCount, neCount, nwCount, seCount, swCount = getCounts(moves)
    steps = secondTry(nCount,sCount,neCount,nwCount, seCount, swCount)
    if steps > maxSteps:
        maxSteps = steps

    moves.pop()

print maxSteps
