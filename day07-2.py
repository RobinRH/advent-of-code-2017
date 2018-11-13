#answer -> 1853
import csv
import sys

class Program:
    totalweight = 0

    def __init__(self, n, d):
        self.name = n
        self.data = d
        self.children = []
        self.parent = None
        self.weight = int(d[1].replace('(', '').replace(')',''))

# weight of node is self plus all children
def findWeightNode(node):
    return node.weight + sum(findWeightNode(c) for c in node.children)

filename = sys.argv[1]

nodes = dict()
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        # pattern is
        # zdhvqrl (40) -> fpbsu, fwpfjjd, viqhfi
        # create a dictionary with each node so we can look up the nodes and connect them.
        prog = Program(row[0], row)
        nodes[row[0]] = prog
        Program.totalweight += prog.weight

print Program.totalweight

for name in nodes.keys():
    # parse out the children
    prog = nodes[name]
    if '->' in prog.data:
        for ichild in range(3, len(prog.data)):
            childname = prog.data[ichild]
            childname = childname.replace(',', '')
            childnode = nodes[childname]
            prog.children.append(childnode)
            childnode.parent = prog


# now they are all hooked up
# choose any one and follow it up to the top
anode = nodes[nodes.keys()[0]]

aparent = None
hasAParent = (anode.parent is not None)
while (hasAParent):
    anode = anode.parent
    hasAParent = (anode.parent is not None)

print anode.name

# Or, the top node is the only one without a parent
'''
topnode = None
for v in nodes.values():
    if v.parent is None:
        topnode = v.name
        break

print topnode
'''

print findWeightNode(anode)

# now file the broken node
def findBrokenProgram(node):
    weights = map(findWeightNode, node.children)
    print node.weight, str(weights)
    unique = set(weights)
    if len(unique) == 1:
        # It's me, because my child towers are balanced
        print "it's me"
        return node
    else: # find the one that's different
        #there are only two different numbers, find the one with a count of 1
        badweight = 0
        for u in unique:
            if weights.count(u) == 1: # that's the one
                badweight = u
                print badweight

        #find the node with that weight
        for c in node.children:
            if findWeightNode(c) == badweight:
                print "found it"
                return findBrokenProgram(c)

badnode = findBrokenProgram(anode)
print badnode.name

# having found the bad node, what does it's weight need to be?
# find the weight of the siblings
sibweights = map(findWeightNode, badnode.parent.children)
print sibweights
twoweights = list(set(sibweights))
badweight = findWeightNode(badnode)
goodweight = twoweights[0]
if badweight == twoweights[0]:
    goodweight = twoweights[1]
neededweight = goodweight - sum(findWeightNode(c) for c in badnode.children)
print neededweight

 
