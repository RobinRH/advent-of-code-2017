#answer -> hmvwl
import csv
import sys

class Program:
    def __init__(self, n, d):
        self.name = n
        self.data = d
        self.children = []
        self.parent = None
        self.weight = int(d[1].replace('(', '').replace(')',''))


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
topnode = None
for v in nodes.values():
    if v.parent is None:
        topnode = v.name
        break

print topnode
    

