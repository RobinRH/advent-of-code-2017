# answer 169

import csv
import sys

filename = sys.argv[1]
pipes = dict()

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        print row
        pipes[int(row[0])] = row

# 0 <-> 1352, 1864
# ['1990', '<->', '990,', '1153']
def getConnections(row):
    connections = []
    nConnections = len(row) - 2
    for n in range(2, nConnections + 2):
        connections.append(int(row[n].replace(',', '')))
    print connections
    return connections


def countConnections(start):
    visited = [] # an array of integers
    frontier = set() # an array of integers

    # find the start node
    startNode = pipes[start]

    frontier.add(start)
    while len(frontier) > 0:
        # add all the connections of the frontier to the frontier
        # remove each as it's visited and add it to group
        # don't add anything to frontier that's alreay in group

        numberList = list(frontier)
        for number in numberList:
            visited.append(number)
            frontier.remove(number)
            connections = getConnections(pipes[number])
            for c in connections:
                if not c in visited:
                    frontier.add(c)

    return len(visited)

n = countConnections(0)
print n
