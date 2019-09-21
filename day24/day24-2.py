#answer -> 1824

import csv
import sys
from pprint import pprint

filename = sys.argv[1]

components = []
doubles = []
ends = []
with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter='/')
    for row in reader:
        (a, b) = (int(row[0]), int(row[1]))
        if a != b:
            components.append((a,b,False)) # end, end, used in bridge
            ends.append(a)
            ends.append(b)
        else:
            doubles.append(a)


ends.sort()
print "ends: ", ends
counts = map(lambda x : ends.count(x), range(50))
print "counts: ", counts


class Graph:
  
    def __init__(self):

        self.pool = []
        self.used = []

        # default dictionary to store graph
        #self.graph = defaultdict(list)
        self.paths = []
  
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.pool.append((u,v))

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, source, destination, path):
        """
        Args:
            source (int, int): segment
            destinations (int): where you want the path to end
        """
        # Mark the current node as visited and store in path

        self.used.append(source)
        path.append(source)
        self.removeSegmentFromPool(source)
 
        # If current vertex is same as destination, then print
        # current path[]
        if source[1] == destination:
            #print path
            newPath = []
            for (a,b) in path: 
                newPath.append((a,b))
            self.paths.append(newPath)
        else:
            # If current vertex is not destination
            #Recur for all the vertices adjacent to this vertex
            matches = self.findSegmentsWithEnd(source[1])
            for m in matches:
                self.printAllPathsUtil(m, destination, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        (a, b) = path[-1]
        path.pop()
        self.pool.append((a,b))
        self.used.remove((a,b))
    
    def findSegmentsWithEnd(self, e):
        # flip segment if necessary so that (a, b) == (e, b)
        matches = []
        for (a,b) in self.pool:
            if (a == e):
                matches.append((a,b))
            elif (b == e):
                matches.append((b, a))

        return matches


    # Prints all paths from 's' to 'd'
    def printAllPaths(self, source, destination):
 
        self.paths = []

        # put everything back in the pool
        for u in self.used:
            self.pool.append(u)
            self.used.remove(u)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        starts = self.findSegmentsWithEnd(source)
        for start in starts:
            self.printAllPathsUtil(start, destination, path)


    def removeSegmentFromPool(self, (a, b)):
        # because we might flip the segment to make the path, we have to find the segment and remove it
        if (a,b) in self.pool:
            self.pool.remove((a,b))
        else:
            self.pool.remove((b,a))


def getPathStrength(path):
    strength = 0
    for (a, b) in path:
        strength += a + b
    
    return strength

graph = Graph()

with open(filename, 'r') as f:
    reader = csv.reader(f, delimiter='/')
    for row in reader:
        (a, b) = (int(row[0]), int(row[1]))
        graph.addEdge(a, b)

maxStrength = 0
maxPath = []
maxLength = 0
maxPaths = []
for i in range(50):
    graph.printAllPaths(0,i)
    for p in graph.paths:
        strength = getPathStrength(p)
        if strength > maxStrength:
            maxStrength = strength
            maxPath = p

        length = len(p)
        if length > maxLength:
            maxLength = length
            maxPaths = []
            maxPaths.append(p)
        elif length == maxLength:
            maxPaths.append(p)

    print "Done: ", i

print maxStrength, ": ", maxPath
print maxLength, ": ", maxLength
print maxPaths, ": ", maxPaths

maxStrength = 0
maxPath = []
for mp in maxPaths:
    strength = getPathStrength(mp)
    if strength > maxStrength:
        maxStrength = strength 
        maxPath = mp

print maxStrength, ": ", maxLength

