# answer -> hmvwl
# answer -> 1853

from pprint import pprint
from collections import Counter

# make a list of all the nodes
nodes = []

for line in open('input07.txt', 'r'):
    words = line.split()
    prg = words[0]
    nodes.append(prg)

# remove all children from the list
# the parent of all does not appear in any of the children
# just need to count how many times each word appears
whole = open('input07.txt', 'r').read()
root = ''
for node in nodes:
    if whole.count(node) == 1:
        root = node
        break

print('part 1: ', root)

# part 2
# now build a dictionary for each line
nodes = {}
for line in open('input07.txt', 'r'):
    words = line.replace(',', '').replace('(', '').replace(')', '').split()
    # create weight, children tuple
    children = words[3:]
    weight = int(words[1])
    nodes[words[0]] = (weight, children)


# part 2

def getWeight(node):
    sum = 0
    weight, children = nodes[node]
    sum += weight
    for child in children:
        sum += getWeight(child)
    return sum

def isNodeBalanced(node):
    _, childrenN = nodes[node]
    if len(childrenN) == 0:
        return True
    weights = [getWeight(x) for x in childrenN]
    return len(set(weights)) == 1

def findBadNode(node):
    # if my children are balanced, then I'm the bad node
    # if my children are unbalanced, then find the culprit
    if isNodeBalanced(node):
        # then it's me
        return node
    else:
        # find the offending node
        wt, ch = nodes[node]
        wtdict = {getWeight(x): x for x in ch}
        wts = [getWeight(x) for x in ch]
        badnode = ''
        for key in list(wtdict.keys()):
            if wts.count(key) == 1:
                badnode = wtdict[key]
        return findBadNode(badnode)


# get the offset
rootweights = [getWeight(x) for x in nodes[root][1]]
rootweights.sort()
offset = rootweights[-1] - rootweights[0]

badnode = findBadNode(root)
print('part 2: ', nodes[badnode][0] - offset)
